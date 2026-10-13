"""Graphtec test 01: print PDF + single-layer AI8 cut file for a grid of test_A labels.

SANDBOX_RESEARCH_ONLY. Not a production adapter. The source PDF is never modified.

Inputs:  sample PDF with OCG layers Print / CutContour / Holes, Graphtec sheet template
         (two filled K100 marks and a stroked knife-field rectangle).
Outputs: print PDF (artwork + marks, cut layers removed), AI8 cut file (marks + closed
         Bezier contours, holes before outer contour, ordered from the leading edge),
         a single-layer cut preview PDF, and placement.json for the independent check.
"""
from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

import pikepdf

PT_PER_MM = 72.0 / 25.4
PAINT_OPS = {"f", "F", "f*", "S", "s", "B", "B*", "b", "b*", "n"}


@dataclass
class PaintedPath:
    layer: str | None
    paint: str
    fill: tuple
    stroke: tuple
    subpaths: list = field(default_factory=list)  # [[("m", x, y) | ("l", x, y) | ("c", x1, y1, x2, y2, x3, y3) | ("h",)]]


def _mul(a, b):
    """Compose affine matrices given as (a, b, c, d, e, f): result = a then b."""
    return (
        a[0] * b[0] + a[1] * b[2], a[0] * b[1] + a[1] * b[3],
        a[2] * b[0] + a[3] * b[2], a[2] * b[1] + a[3] * b[3],
        a[4] * b[0] + a[5] * b[2] + b[4], a[4] * b[1] + a[5] * b[3] + b[5],
    )


def _apply(m, x, y):
    return (m[0] * x + m[2] * y + m[4], m[1] * x + m[3] * y + m[5])


def _num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return x


def collect_paths(page: pikepdf.Page) -> list[PaintedPath]:
    """Painted vector paths in page user space, tagged with their OCG name."""
    props = page.obj.Resources.get("/Properties", {})
    oc_name = {str(k): str(v.get("/Name")) for k, v in props.items()}
    ctm, stack, oc_stack = (1, 0, 0, 1, 0, 0), [], []
    fill, stroke = ("g", 0.0), ("g", 0.0)
    subpaths, out = [], []
    for operands, op in pikepdf.parse_content_stream(page):
        op = str(op)
        v = [_num(x) for x in operands]
        if op == "q":
            stack.append(ctm)
        elif op == "Q":
            ctm = stack.pop()
        elif op == "cm":
            ctm = _mul(tuple(v), ctm)
        elif op in ("BDC", "BMC"):
            name = None
            if op == "BDC" and str(operands[0]) == "/OC":
                name = oc_name.get(str(operands[1]))
            oc_stack.append(name)
        elif op == "EMC":
            oc_stack.pop()
        elif op == "k":
            fill = ("cmyk",) + tuple(v)
        elif op == "K":
            stroke = ("cmyk",) + tuple(v)
        elif op in ("g", "rg"):
            fill = (("gray",) if op == "g" else ("rgb",)) + tuple(v)
        elif op in ("G", "RG"):
            stroke = (("gray",) if op == "G" else ("rgb",)) + tuple(v)
        elif op == "m":
            subpaths.append([("m",) + _apply(ctm, v[0], v[1])])
        elif op == "l":
            subpaths[-1].append(("l",) + _apply(ctm, v[0], v[1]))
        elif op == "c":
            p = [_apply(ctm, v[i], v[i + 1]) for i in (0, 2, 4)]
            subpaths[-1].append(("c",) + p[0] + p[1] + p[2])
        elif op in ("v", "y"):
            raise SystemExit(f"unsupported path operator {op}; extend the collector")
        elif op == "h":
            subpaths[-1].append(("h",))
        elif op == "re":
            x, y, w, h = v
            pts = [_apply(ctm, *pt) for pt in ((x, y), (x + w, y), (x + w, y + h), (x, y + h))]
            subpaths.append([("m",) + pts[0], ("l",) + pts[1], ("l",) + pts[2], ("l",) + pts[3], ("h",)])
        elif op in ("W", "W*"):
            pass
        elif op in PAINT_OPS:
            if op != "n":
                layer = next((n for n in reversed(oc_stack) if n), None)
                out.append(PaintedPath(layer, op, fill, stroke, subpaths))
            subpaths = []
    return out


def cubic_extrema_bbox(subpaths):
    """Exact bounding box of a path made of lines and cubic Beziers."""
    xs, ys = [], []
    cur = None
    for sp in subpaths:
        for seg in sp:
            if seg[0] in ("m", "l"):
                cur = seg[1:3]
                xs.append(cur[0]); ys.append(cur[1])
            elif seg[0] == "c":
                p0, p1, p2, p3 = cur, seg[1:3], seg[3:5], seg[5:7]
                for axis, acc in ((0, xs), (1, ys)):
                    a0, a1, a2, a3 = p0[axis], p1[axis], p2[axis], p3[axis]
                    acc.append(a3)
                    # derivative coefficients of B(t) on this axis
                    qa = -a0 + 3 * a1 - 3 * a2 + a3
                    qb = 2 * (a0 - 2 * a1 + a2)
                    qc = a1 - a0
                    roots = []
                    if abs(qa) < 1e-12:
                        if abs(qb) > 1e-12:
                            roots.append(-qc / qb)
                    else:
                        disc = qb * qb - 4 * qa * qc
                        if disc >= 0:
                            s = math.sqrt(disc)
                            roots += [(-qb + s) / (2 * qa), (-qb - s) / (2 * qa)]
                    for t in roots:
                        if 0 < t < 1:
                            mt = 1 - t
                            acc.append(mt ** 3 * a0 + 3 * mt * mt * t * a1 + 3 * mt * t * t * a2 + t ** 3 * a3)
                cur = seg[5:7]
    return (min(xs), min(ys), max(xs), max(ys))


def translate(subpaths, tx, ty):
    out = []
    for sp in subpaths:
        nsp = []
        for seg in sp:
            if seg[0] == "h":
                nsp.append(seg)
            else:
                vals = list(seg[1:])
                nsp.append((seg[0],) + tuple(vals[i] + (tx if i % 2 == 0 else ty) for i in range(len(vals))))
        out.append(nsp)
    return out


def ensure_closed(subpaths):
    """Explicit closure: drop a final segment end that duplicates the start, then close with h."""
    out = []
    for sp in subpaths:
        sp = [s for s in sp if s[0] != "h"]
        start = sp[0][1:3]
        end = sp[-1][-2:]
        gap = math.dist(start, end)
        if gap > 0.05 * PT_PER_MM:
            raise SystemExit(f"contour not closed: gap {gap / PT_PER_MM:.3f} mm")
        if sp[-1][0] == "c":
            last = sp[-1]
            sp[-1] = last[:5] + start  # snap the end exactly onto the start
        elif sp[-1][0] == "l":
            sp[-1] = ("l",) + start
        out.append(sp + [("h",)])
    return out


def filter_print_only(page: pikepdf.Page, drop_layers: set[str]):
    """Content stream with the given OCG blocks removed and the remaining OC wrappers unwrapped."""
    props = page.obj.Resources.get("/Properties", {})
    oc_name = {str(k): str(v.get("/Name")) for k, v in props.items()}
    out, depth_drop, stack = [], 0, []
    for operands, op in pikepdf.parse_content_stream(page):
        sop = str(op)
        if sop in ("BDC", "BMC"):
            name = oc_name.get(str(operands[1])) if sop == "BDC" and str(operands[0]) == "/OC" else None
            stack.append(name)
            if depth_drop or name in drop_layers:
                depth_drop += 1
                continue
            if name is not None:
                continue  # unwrap kept OC layer: print content becomes unconditional
        elif sop == "EMC":
            name = stack.pop()
            if depth_drop:
                depth_drop -= 1
                continue
            if name is not None:
                continue
        elif depth_drop:
            continue
        out.append(pikepdf.ContentStreamInstruction(operands, op))
    return pikepdf.unparse_content_stream(out)


def fmt(x):
    return f"{x:.4f}".rstrip("0").rstrip(".") if abs(x) >= 1e-9 else "0"


def path_ops_pdf(subpaths):
    parts = []
    for sp in subpaths:
        for seg in sp:
            if seg[0] == "m":
                parts.append(f"{fmt(seg[1])} {fmt(seg[2])} m")
            elif seg[0] == "l":
                parts.append(f"{fmt(seg[1])} {fmt(seg[2])} l")
            elif seg[0] == "c":
                parts.append(" ".join(fmt(x) for x in seg[1:]) + " c")
            else:
                parts.append("h")
    return "\n".join(parts)


def path_ops_ai(subpaths):
    parts = []
    for sp in subpaths:
        for seg in sp:
            if seg[0] == "m":
                parts.append(f"{fmt(seg[1])} {fmt(seg[2])} m")
            elif seg[0] == "l":
                parts.append(f"{fmt(seg[1])} {fmt(seg[2])} L")
            elif seg[0] == "c":
                parts.append(" ".join(fmt(x) for x in seg[1:]) + " C")
    return "\n".join(parts)


def ai8_document(width_pt, height_pt, title, marks, cut_paths):
    w, h = width_pt, height_pt
    now = datetime.now(timezone.utc)
    lines = [
        "%!PS-Adobe-3.0",
        "%%Creator: Adobe Illustrator(R) 8.0",
        "%%AI8_CreatorVersion: 8.0",
        "%%For: (Impozitorium sandbox) ()",
        f"%%Title: ({title})",
        f"%%CreationDate: ({now:%m/%d/%y}) ({now:%H:%M})",
        f"%%BoundingBox: 0 0 {math.ceil(w)} {math.ceil(h)}",
        f"%%HiResBoundingBox: 0 0 {fmt(w)} {fmt(h)}",
        "%%DocumentProcessColors: Magenta Black",
        "%AI5_FileFormat 4.0",
        "%AI3_ColorUsage: Color",
        f"%AI3_TemplateBox: {fmt(w / 2)} {fmt(h / 2)} {fmt(w / 2)} {fmt(h / 2)}",
        f"%AI3_TileBox: 0 0 {fmt(w)} {fmt(h)}",
        "%AI3_DocumentPreview: None",
        f"%AI5_ArtSize: {fmt(w)} {fmt(h)}",
        "%AI5_RulerUnits: 1",
        "%AI5_ArtFlags: 0 0 0 1 0 0 1 0 0",
        "%AI5_TargetResolution: 800",
        "%AI5_NumLayers: 1",
        "%AI5_OpenViewLayers: 7",
        "%%PageOrigin:0 0",
        "%%EndComments",
        "%%BeginProlog",
        "%%EndProlog",
        "%%BeginSetup",
        "%%EndSetup",
        "%AI5_BeginLayer",
        "1 1 1 1 0 0 1 0 79 128 255 0 50 Lb",
        "(Cut) Ln",
        "0 A",
        "0 O",
        "0 R",
    ]
    for mark in marks:
        lines += ["0 0 0 1 k", "0 i 0 J 0 j 1 w 4 M []0 d", "%AI3_Note:", "0 D", "0 XR", path_ops_ai(mark), "f"]
    for p in cut_paths:
        lines += ["0 1 0 0 K", "0 i 0 J 0 j 0.5 w 4 M []0 d", "%AI3_Note:", "0 D", "0 XR", path_ops_ai(p), "s"]
    lines += [
        "LB",
        "%AI5_EndLayer--",
        "%%PageTrailer",
        "gsave annotatepage grestore showpage",
        "%%Trailer",
        "%%EOF",
    ]
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sample", type=Path, required=True)
    ap.add_argument("--template", type=Path, required=True)
    ap.add_argument("--out-dir", type=Path, required=True)
    ap.add_argument("--gap-mm", type=float, default=4.0, help="contour clearance between neighbouring outer contours")
    ap.add_argument("--lead", choices=["left", "right", "top", "bottom"], default="left", help="assumed leading edge")
    ap.add_argument("--cut-layer", default="CutContour")
    ap.add_argument("--hole-layer", default="Holes")
    args = ap.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)

    # ---------------------------------------------------------------- template
    tpl = pikepdf.open(args.template)
    tpl_page = tpl.pages[0]
    media = [float(x) for x in tpl_page.obj.MediaBox]
    sheet_w, sheet_h = media[2] - media[0], media[3] - media[1]
    tpaths = collect_paths(tpl_page)
    marks = [p for p in tpaths if p.paint in ("f", "F", "f*")]
    frames = [p for p in tpaths if p.paint in ("S", "s")]
    if len(marks) != 2 or len(frames) != 1:
        raise SystemExit(f"template: expected 2 filled marks and 1 stroked frame, got {len(marks)} / {len(frames)}")
    field_box = cubic_extrema_bbox(frames[0].subpaths)
    mark_geoms = [m.subpaths for m in marks]

    # ---------------------------------------------------------------- sample
    src = pikepdf.open(args.sample)
    src_page = src.pages[0]
    spaths = collect_paths(src_page)
    cut = [p for p in spaths if p.layer == args.cut_layer]
    holes = [p for p in spaths if p.layer == args.hole_layer]
    if len(cut) != 1:
        raise SystemExit(f"sample: expected exactly one {args.cut_layer} path, got {len(cut)}")
    contour = ensure_closed(cut[0].subpaths)
    hole_geoms = [ensure_closed(h.subpaths) for h in holes]
    cx0, cy0, cx1, cy1 = cubic_extrema_bbox(contour)
    item_w, item_h = cx1 - cx0, cy1 - cy0
    bleed_box = [float(x) for x in src_page.obj.get("/BleedBox", src_page.obj.MediaBox)]

    # ---------------------------------------------------------------- layout: grid, centred in the knife field
    g = args.gap_mm * PT_PER_MM
    fx0, fy0, fx1, fy1 = field_box
    nx = math.floor((fx1 - fx0 + g) / (item_w + g))
    ny = math.floor((fy1 - fy0 + g) / (item_h + g))
    grid_w, grid_h = nx * item_w + (nx - 1) * g, ny * item_h + (ny - 1) * g
    offx, offy = (fx1 - fx0 - grid_w) / 2, (fy1 - fy0 - grid_h) / 2
    instances = []
    for i in range(nx):
        for j in range(ny):  # j = 0 is the top row
            left = fx0 + offx + i * (item_w + g)
            top = fy1 - offy - j * (item_h + g)
            instances.append({"col": i, "row": j, "tx": left - cx0, "ty": (top - item_h) - cy0})

    # cut order: columns from the leading edge, serpentine inside a column
    def order_key(inst):
        if args.lead in ("left", "right"):
            col = inst["col"] if args.lead == "left" else nx - 1 - inst["col"]
            row = inst["row"] if col % 2 == 0 else ny - 1 - inst["row"]
            return (col, row)
        row = inst["row"] if args.lead == "top" else ny - 1 - inst["row"]
        col = inst["col"] if row % 2 == 0 else nx - 1 - inst["col"]
        return (row, col)

    instances.sort(key=order_key)
    for n, inst in enumerate(instances):
        inst["cut_sequence"] = n

    # ---------------------------------------------------------------- print projection (PDF)
    out = pikepdf.new()
    out_page = out.add_blank_page(page_size=(sheet_w, sheet_h))
    out_page.obj.MediaBox = pikepdf.Array([0, 0, sheet_w, sheet_h])
    out_page.obj.TrimBox = pikepdf.Array([0, 0, sheet_w, sheet_h])
    # Resources is a direct dictionary in the sample: wrap an in-memory copy as indirect to copy it across.
    res = out.copy_foreign(src.make_indirect(pikepdf.Dictionary(src_page.obj.Resources)))
    if "/Properties" in res:
        del res["/Properties"]
    form = pikepdf.Stream(out, filter_print_only(src_page, {args.cut_layer, args.hole_layer}))
    form.Type = pikepdf.Name.XObject
    form.Subtype = pikepdf.Name.Form
    form.BBox = pikepdf.Array(bleed_box)
    form.Resources = res
    out_page.obj.Resources = pikepdf.Dictionary(XObject=pikepdf.Dictionary(Fm0=form))
    content = []
    for inst in instances:
        content.append(f"q 1 0 0 1 {fmt(inst['tx'])} {fmt(inst['ty'])} cm /Fm0 Do Q")
    for mg in mark_geoms:
        content.append("q 0 0 0 1 k\n" + path_ops_pdf(mg) + "\nf Q")
    out_page.obj.Contents = out.make_stream("\n".join(content).encode())
    out.docinfo["/Title"] = "Graphtec test 01 - print (sandbox)"
    out.docinfo["/Creator"] = "Impozitorium contour_nesting_lab (sandbox research only)"
    print_pdf = args.out_dir / "graphtec_print_test_A_grid.pdf"
    out.save(print_pdf)

    # ---------------------------------------------------------------- cut projection (AI8 + preview PDF)
    cut_paths = []
    for inst in instances:
        for hg in hole_geoms:
            cut_paths.append(translate(hg, inst["tx"], inst["ty"]))
        cut_paths.append(translate(contour, inst["tx"], inst["ty"]))
    cut_ai = args.out_dir / "graphtec_cut_test_A_grid.ai"
    cut_ai.write_text(ai8_document(sheet_w, sheet_h, cut_ai.name, mark_geoms, cut_paths), encoding="ascii")

    prev = pikepdf.new()
    pp = prev.add_blank_page(page_size=(sheet_w, sheet_h))
    body = [f"q 0 0 0 1 k\n{path_ops_pdf(m)}\nf Q" for m in mark_geoms]
    body += [f"q 0 1 0 0 K 0.5 w\n{path_ops_pdf(p)}\nS Q" for p in cut_paths]
    pp.obj.Contents = prev.make_stream("\n".join(body).encode())
    prev.save(args.out_dir / "graphtec_cut_test_A_grid_preview.pdf")

    # ---------------------------------------------------------------- placement record for the independent check
    record = {
        "status": "SANDBOX_RESEARCH_ONLY",
        "units": "pt (PDF user space, y up, origin = sheet lower-left)",
        "sheet": [0, 0, sheet_w, sheet_h],
        "knife_field": list(field_box),
        "marks": [cubic_extrema_bbox(m) for m in mark_geoms],
        "sample": {"cut_layer": args.cut_layer, "hole_layer": args.hole_layer,
                   "contour_bbox": [cx0, cy0, cx1, cy1], "bleed_box": bleed_box, "holes": len(hole_geoms)},
        "layout": {"strategy": "grid, centred in knife field", "nx": nx, "ny": ny, "gap_mm": args.gap_mm,
                   "lead_edge_assumed": args.lead, "orientation": "identity (0 deg, no reflection)"},
        "instances": instances,
        "outputs": {"print_pdf": print_pdf.name, "cut_ai": cut_ai.name,
                    "cut_preview_pdf": "graphtec_cut_test_A_grid_preview.pdf"},
    }
    (args.out_dir / "placement.json").write_text(json.dumps(record, indent=2), encoding="utf-8")
    print(f"built {nx}x{ny} = {len(instances)} instances; outputs in {args.out_dir}")


if __name__ == "__main__":
    main()
