import sys, json, math
from dataclasses import asdict
from pathlib import Path
lab, out = Path(sys.argv[1]), Path(sys.argv[2])
sys.path.insert(0, str(lab))
import fitz
from extractor_probe import FinishingContourExtractor
from placement_honeycomb import build_honeycomb_plan_from_extraction
mm = 72/25.4
side, rad, gap = 40*mm, 4*mm, 3*mm
pdf = out/"rounded_square.pdf"
doc = fitz.open(); page = doc.new_page(width=60*mm, height=60*mm)
ocg = doc.add_ocg("CutContour", on=True)
r = fitz.Rect(10*mm, 10*mm, 10*mm+side, 10*mm+side)
sh = page.new_shape(); sh.draw_rect(r, radius=rad/side); sh.finish(color=(1,0,1), width=0.5, closePath=True, oc=ocg); sh.commit()
doc.save(pdf); doc.close()
ex = FinishingContourExtractor(["CutContour"]).analyze_pdf(pdf)
exd = asdict(ex)
s = exd["shapes"][0]["outer_contour"] if exd["shapes"] else None
print("status", exd["status"], "shapes", len(exd["shapes"]), "is_circular", s and s["is_circular"], "diameter_mm", s and round(s["diameter_pt"]/mm,3))
plan = build_honeycomb_plan_from_extraction(exd, gap_pt=gap, machine_profile="PFI_BLADE_B2_ALPHA")
P = plan.placements
print("placements", len(P), "warnings", plan.warnings)
# exact overlap test for rounded squares: Minkowski view -> squares of side (side-2rad) dilated by rad
core = side/2 - rad
def dist(c1, c2):
    dx = max(0.0, abs(c1[0]-c2[0]) - 2*core); dy = max(0.0, abs(c1[1]-c2[1]) - 2*core)
    return math.hypot(dx, dy) - 2*rad   # boundary-to-boundary distance (negative = overlap)
worst = min(dist(a.center_pt, b.center_pt) for i,a in enumerate(P) for b in P[i+1:])
bad = sum(1 for i,a in enumerate(P) for b in P[i+1:] if dist(a.center_pt,b.center_pt) < gap - 1e-9)
print("min boundary distance mm", round(worst/mm,3), "pairs violating 3mm gap", bad)
