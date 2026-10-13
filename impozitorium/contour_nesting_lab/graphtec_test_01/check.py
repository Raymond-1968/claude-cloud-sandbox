"""Independent check of Graphtec test 01 outputs. SANDBOX_RESEARCH_ONLY.

Reads the produced files with its own parsers (it does not import build.py):
  - the AI8 cut file is tokenised here,
  - the print PDF and the inputs are parsed here with pikepdf,
then checks marks, closure, knife-field containment, contour clearance, holes,
print/cut registration, absence of cut layers in the print file and cut order,
renders an overlay PNG and writes report.md.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import pikepdf
import pypdfium2 as pdfium
from PIL import ImageDraw

MM = 25.4 / 72.0
EPS_FLAT_MM = 0.002


# ------------------------------------------------------------------ parsing helpers (independent of build.py)
def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def parse_ai(path: Path):
    """Return a list of paths: {'paint': op, 'segs': [(op, pts...)]} from AI path operators."""
    paths, segs = [], []
    stack = []
    for raw in path.read_text(encoding="ascii").splitlines():
        line = raw.strip()
        if not line or line.startswith("%"):
            continue
        toks = line.split()
        for t in toks:
            v = num(t)
            if v is not None:
                stack.append(v)
                continue
            if t in ("m", "l", "L", "c", "C"):
                n = 2 if t in ("m", "l", "L") else 6
                pts, stack = stack[-n:], stack[:-n]
                segs.append(("m" if t == "m" else ("l" if t in ("l", "L") else "c"), *pts))
            elif t in ("f", "F", "s", "S", "b", "B"):
                paths.append({"paint": t, "segs": segs})
                segs = []
                stack = []
            else:
                stack = []
    return paths


def bezier_point(p0, p1, p2, p3, t):
    mt = 1 - t
    return (mt ** 3 * p0[0] + 3 * mt * mt * t * p1[0] + 3 * mt * t * t * p2[0] + t ** 3 * p3[0],
            mt ** 3 * p0[1] + 3 * mt * mt * t * p1[1] + 3 * mt * t * t * p2[1] + t ** 3 * p3[1])


def flatten(segs, eps_pt):
    pts, cur = [], None
    for s in segs:
        if s[0] == "m":
            cur = (s[1], s[2]); pts.append(cur)
        elif s[0] == "l":
            cur = (s[1], s[2]); pts.append(cur)
        else:
            p0, p1, p2, p3 = cur, (s[1], s[2]), (s[3], s[4]), (s[5], s[6])
            m = max(math.dist((0, 0), (p0[0] - 2 * p1[0] + p2[0], p0[1] - 2 * p1[1] + p2[1])),
                    math.dist((0, 0), (p1[0] - 2 * p2[0] + p3[0], p1[1] - 2 * p2[1] + p3[1])))
            n = max(1, math.ceil(math.sqrt(0.75 * m / eps_pt)))  # Wang's bound for cubics
            pts += [bezier_point(p0, p1, p2, p3, k / n) for k in range(1, n + 1)]
            cur = p3
    return pts


def exact_bbox(segs):
    """Bounding box from a dense sampling plus endpoints (tight to < 1e-4 pt for these curves)."""
    pts = flatten(segs, 1e-4)
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    return (min(xs), min(ys), max(xs), max(ys))


def seg_dist(p, a, b):
    ax, ay, bx, by = a[0], a[1], b[0], b[1]
    dx, dy = bx - ax, by - ay
    L2 = dx * dx + dy * dy
    t = 0 if L2 == 0 else max(0, min(1, ((p[0] - ax) * dx + (p[1] - ay) * dy) / L2))
    return math.dist(p, (ax + t * dx, ay + t * dy))


def poly_dist(P, Q):
    best = math.inf
    for p in P:
        for a, b in zip(Q, Q[1:] + Q[:1]):
            best = min(best, seg_dist(p, a, b))
    for q in Q:
        for a, b in zip(P, P[1:] + P[:1]):
            best = min(best, seg_dist(q, a, b))
    return best


def inside(pt, poly):
    x, y, c = pt[0], pt[1], False
    for (x1, y1), (x2, y2) in zip(poly, poly[1:] + poly[:1]):
        if (y1 > y) != (y2 > y) and x < x1 + (y - y1) * (x2 - x1) / (y2 - y1):
            c = not c
    return c


def pdf_paths(content_ops, oc_names=None):
    """Very small PDF path reader: returns painted paths with fill/stroke CMYK and OC name."""
    out, segs, ctm, stack, ocs = [], [], (1, 0, 0, 1, 0, 0), [], []
    fill = stroke = None
    for operands, op in content_ops:
        op = str(op)
        v = [num(x) for x in operands]
        if op == "q":
            stack.append(ctm)
        elif op == "Q":
            ctm = stack.pop()
        elif op == "cm":
            a = ctm
            b = v
            ctm = (b[0] * a[0] + b[1] * a[2], b[0] * a[1] + b[1] * a[3], b[2] * a[0] + b[3] * a[2],
                   b[2] * a[1] + b[3] * a[3], b[4] * a[0] + b[5] * a[2] + a[4], b[4] * a[1] + b[5] * a[3] + a[5])
        elif op in ("BDC", "BMC"):
            ocs.append(oc_names.get(str(operands[1])) if (oc_names and op == "BDC" and str(operands[0]) == "/OC") else None)
        elif op == "EMC":
            ocs.pop()
        elif op == "k":
            fill = tuple(v)
        elif op == "K":
            stroke = tuple(v)
        elif op in ("m", "l"):
            x, y = v
            segs.append((op, ctm[0] * x + ctm[2] * y + ctm[4], ctm[1] * x + ctm[3] * y + ctm[5]))
        elif op == "c":
            pts = []
            for i in (0, 2, 4):
                x, y = v[i], v[i + 1]
                pts += [ctm[0] * x + ctm[2] * y + ctm[4], ctm[1] * x + ctm[3] * y + ctm[5]]
            segs.append(("c", *pts))
        elif op in ("f", "F", "f*", "S", "s", "B", "b"):
            out.append({"paint": op, "segs": segs, "fill": fill, "stroke": stroke,
                        "layer": next((n for n in reversed(ocs) if n), None)})
            segs = []
        elif op == "n":
            segs = []
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lab-dir", type=Path, required=True)
    args = ap.parse_args()
    lab, out_dir = args.lab_dir, args.lab_dir / "out"
    rec = json.loads((out_dir / "placement.json").read_text(encoding="utf-8"))
    results = []

    def check(name, ok, detail):
        results.append((name, "PASS" if ok else "FAIL", detail))

    # inputs, parsed independently
    tpl = pikepdf.open(lab / "inputs" / "graphtec_template.pdf")
    tpl_paths = pdf_paths(pikepdf.parse_content_stream(tpl.pages[0]))
    tpl_marks = sorted(exact_bbox(p["segs"]) for p in tpl_paths if p["paint"] in ("f", "F"))
    field = exact_bbox(next(p for p in tpl_paths if p["paint"] in ("s", "S"))["segs"])
    sheet_w = float(tpl.pages[0].obj.MediaBox[2]); sheet_h = float(tpl.pages[0].obj.MediaBox[3])

    src = pikepdf.open(lab / "inputs" / "test_A_split_layers.pdf")
    sp = src.pages[0]
    names = {str(k): str(v.Name) for k, v in sp.obj.Resources.Properties.items()}
    s_paths = pdf_paths(pikepdf.parse_content_stream(sp), names)
    src_contour = next(p for p in s_paths if p["layer"] == "CutContour")
    src_cbox = exact_bbox(src_contour["segs"])

    # cut file
    ai = parse_ai(out_dir / rec["outputs"]["cut_ai"])
    ai_marks = sorted(exact_bbox(p["segs"]) for p in ai if p["paint"] == "f")
    ai_cuts = [p for p in ai if p["paint"] in ("s", "S")]

    # print file
    pr = pikepdf.open(out_dir / rec["outputs"]["print_pdf"])
    pp = pr.pages[0]
    placements, pr_mark_paths, ctm_stack, ctm = [], [], [], (1, 0, 0, 1, 0, 0)
    for operands, op in pikepdf.parse_content_stream(pp):
        op = str(op)
        if op == "q":
            ctm_stack.append(ctm)
        elif op == "Q":
            ctm = ctm_stack.pop()
        elif op == "cm":
            ctm = tuple(num(x) for x in operands)
        elif op == "Do":
            placements.append((ctm[4], ctm[5], ctm[:4]))
    pr_marks = sorted(exact_bbox(p["segs"]) for p in pdf_paths(pikepdf.parse_content_stream(pp)) if p["paint"] in ("f", "F"))
    form = pp.obj.Resources.XObject.Fm0
    form_ops = pikepdf.parse_content_stream(form)
    form_strokes = [p for p in pdf_paths(form_ops) if p["paint"] in ("S", "s", "B", "b")]
    form_bbox = [float(x) for x in form.BBox]

    # K1 marks identical across template, print and cut
    d1 = max(abs(a - b) for m1, m2, m3 in zip(tpl_marks, pr_marks, ai_marks) for a, b in zip(m1 + m1, m2 + m3))
    check("K1 marks: template = print = cut", len(tpl_marks) == len(pr_marks) == len(ai_marks) == 2 and d1 < 1e-3,
          f"{len(ai_marks)} marks; max deviation {d1 * MM:.5f} mm; centres (mm from lower-left): "
          + ", ".join(f"({(b[0] + b[2]) / 2 * MM:.2f}, {(b[1] + b[3]) / 2 * MM:.2f})" for b in ai_marks))

    # K2 counts
    n_inst = rec["layout"]["nx"] * rec["layout"]["ny"]
    check("K2 counts", len(placements) == n_inst and len(ai_cuts) == n_inst * (1 + rec["sample"]["holes"]),
          f"print placements {len(placements)}, cut paths {len(ai_cuts)} (expected {n_inst} and {n_inst * (1 + rec['sample']['holes'])})")

    # K3 explicit closure
    gaps = []
    for p in ai_cuts:
        start, last = p["segs"][0][1:3], p["segs"][-1][-2:]
        gaps.append(math.dist(start, last))
    check("K3 every cut path explicitly closed ('s') and end = start", all(p["paint"] == "s" for p in ai_cuts) and max(gaps) < 1e-6,
          f"max end-start gap {max(gaps) * MM:.6f} mm")

    # K4 knife-field containment
    margins = []
    for p in ai_cuts:
        b = exact_bbox(p["segs"])
        margins.append(min(b[0] - field[0], b[1] - field[1], field[2] - b[2], field[3] - b[3]))
    check("K4 all cut paths inside the knife field", min(margins) >= 0, f"min margin to field {min(margins) * MM:.3f} mm")

    # classify outer contours vs holes by area of bbox
    boxes = [exact_bbox(p["segs"]) for p in ai_cuts]
    areas = [(b[2] - b[0]) * (b[3] - b[1]) for b in boxes]
    big = max(areas)
    outer_idx = [i for i, a in enumerate(areas) if a > 0.9 * big]
    hole_idx = [i for i in range(len(ai_cuts)) if i not in outer_idx]
    eps = EPS_FLAT_MM / MM
    outer_poly = {i: flatten(ai_cuts[i]["segs"], eps)[:-1] for i in outer_idx}

    # K5 contour clearance
    dmin, pair = math.inf, None
    for a in outer_idx:
        for b in outer_idx:
            if a < b:
                ba, bb = boxes[a], boxes[b]
                gapx = max(0, max(ba[0], bb[0]) - min(ba[2], bb[2]))
                gapy = max(0, max(ba[1], bb[1]) - min(ba[3], bb[3]))
                if math.hypot(gapx, gapy) > 10 / MM:
                    continue
                d = poly_dist(outer_poly[a], outer_poly[b])
                if d < dmin:
                    dmin, pair = d, (a, b)
    req = rec["layout"]["gap_mm"]
    check("K5 contour clearance between neighbouring outer contours", dmin * MM >= req - 2 * EPS_FLAT_MM,
          f"measured {dmin * MM:.4f} mm (flattening tolerance {EPS_FLAT_MM} mm per curve); required {req} mm")

    # K6 holes inside their outer contour
    worst = math.inf
    ok6 = True
    for h in hole_idx:
        hb = boxes[h]
        hc = ((hb[0] + hb[2]) / 2, (hb[1] + hb[3]) / 2)
        owner = min(outer_idx, key=lambda o: math.dist(hc, ((boxes[o][0] + boxes[o][2]) / 2, (boxes[o][1] + boxes[o][3]) / 2)))
        hp = flatten(ai_cuts[h]["segs"], eps)[:-1]
        ok6 &= all(inside(p, outer_poly[owner]) for p in hp)
        worst = min(worst, poly_dist(hp, outer_poly[owner]))
    check("K6 every hole lies inside its outer contour", ok6, f"min hole-to-contour distance {worst * MM:.3f} mm")

    # K7 print/cut registration
    dev = 0.0
    for o in outer_idx:
        shift = (boxes[o][0] - src_cbox[0], boxes[o][1] - src_cbox[1])
        nearest = min(placements, key=lambda pl: math.dist(shift, pl[:2]))
        dev = max(dev, math.dist(shift, nearest[:2]))
    ident = all(abs(pl[2][0] - 1) < 1e-9 and abs(pl[2][3] - 1) < 1e-9 and abs(pl[2][1]) < 1e-9 and abs(pl[2][2]) < 1e-9 for pl in placements)
    check("K7 print placements match cut contours (translation only, no reflection)", dev < 1e-3 and ident,
          f"max offset mismatch {dev * MM:.5f} mm; all placement matrices identity rotation: {ident}")

    # K8 cut layers absent from the print projection
    magenta_or_green = [p for p in form_strokes if p["stroke"] in ((0.0, 1.0, 0.0, 0.0), (1.0, 0.0, 1.0, 0.0))]
    has_oc = any(str(op) in ("BDC", "BMC") for _, op in form_ops)
    check("K8 print file contains no cut / hole strokes and no optional-content wrappers", not magenta_or_green and not has_oc,
          f"cut-coloured strokes {len(magenta_or_green)}, OC markers present: {has_oc}")

    # K9 print extents vs sheet edges (for printer blind zones)
    ext = [(pl[0] + form_bbox[0], pl[1] + form_bbox[1], pl[0] + form_bbox[2], pl[1] + form_bbox[3]) for pl in placements]
    edge = {"left": min(e[0] for e in ext), "bottom": min(e[1] for e in ext),
            "right": sheet_w - max(e[2] for e in ext), "top": sheet_h - max(e[3] for e in ext)}
    check("K9 printed area inside the sheet", min(edge.values()) >= 0,
          "distance from printed area to sheet edge: " + ", ".join(f"{k} {v * MM:.2f} mm" for k, v in edge.items()))

    # K10 cut order: columns from the leading edge, hole before its outer contour
    seq_x = [(boxes[o][0] + boxes[o][2]) / 2 for o in outer_idx]
    cols_ok = all(b >= a - 1e-6 for a, b in zip(seq_x, seq_x[1:]))
    holes_first = all(i - 1 in hole_idx for i in outer_idx)
    longest_line = max((math.dist(s1[-2:], s2[1:3]) for p in ai_cuts for s1, s2 in zip(p["segs"], p["segs"][1:]) if s2[0] == "l"), default=0.0)
    check("K10 cut order from the leading edge; hole cut before its outer contour", cols_ok and holes_first,
          f"lead edge assumed: {rec['layout']['lead_edge_assumed']}; longest straight cut {longest_line * MM:.1f} mm")

    # overlay render
    pdf = pdfium.PdfDocument(str(out_dir / rec["outputs"]["print_pdf"]))
    scale = 3.0 * 25.4 / 72  # 3 px per mm
    img = pdf[0].render(scale=scale).to_pil().convert("RGB")
    draw = ImageDraw.Draw(img)
    H = img.height

    def px(p):
        return (p[0] * scale, H - p[1] * scale)

    fx = [px((field[0], field[1])), px((field[2], field[3]))]
    for t in range(0, int(fx[1][0] - fx[0][0]), 12):
        draw.line([(fx[0][0] + t, fx[0][1]), (fx[0][0] + t + 6, fx[0][1])], fill=(40, 90, 200), width=2)
        draw.line([(fx[0][0] + t, fx[1][1]), (fx[0][0] + t + 6, fx[1][1])], fill=(40, 90, 200), width=2)
    for t in range(0, int(fx[0][1] - fx[1][1]), 12):
        draw.line([(fx[0][0], fx[1][1] + t), (fx[0][0], fx[1][1] + t + 6)], fill=(40, 90, 200), width=2)
        draw.line([(fx[1][0], fx[1][1] + t), (fx[1][0], fx[1][1] + t + 6)], fill=(40, 90, 200), width=2)
    for i, p in enumerate(ai_cuts):
        poly = [px(q) for q in flatten(p["segs"], 0.05 / MM)]
        draw.line(poly, fill=(220, 0, 140) if i in outer_idx else (0, 150, 70), width=3)
    for n, o in enumerate(outer_idx):
        b = boxes[o]
        c = px(((b[0] + b[2]) / 2, (b[1] + b[3]) / 2))
        draw.rectangle([c[0] - 22, c[1] + 70, c[0] + 22, c[1] + 100], fill=(255, 255, 255))
        draw.text((c[0] - 8, c[1] + 76), str(n + 1), fill=(0, 0, 0))
    for b in ai_marks:
        draw.rectangle([px((b[0], b[3])), px((b[2], b[1]))], outline=(255, 120, 0), width=3)
    img.save(out_dir / "overlay_print_plus_cut.png")

    # report
    lines = [
        "# Graphtec test 01 — independent check",
        "",
        "Status: SANDBOX_RESEARCH_ONLY. Not a production adapter.",
        "",
        "| Check | Result | Detail |",
        "|---|---|---|",
    ] + [f"| {n} | {r} | {d} |" for n, r, d in results] + [
        "",
        f"Layout: {rec['layout']}",
        f"Knife field (mm, lower-left origin): {[round(v * MM, 2) for v in field]}",
        "",
        "Overlay: `overlay_print_plus_cut.png` — print render, cut contours (magenta), holes (green),",
        "knife field (blue dashes), marks (orange), cut order numbers.",
    ]
    (out_dir / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    for n, r, d in results:
        print(f"{r:4s}  {n}: {d}")
    if any(r == "FAIL" for _, r, _ in results):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
