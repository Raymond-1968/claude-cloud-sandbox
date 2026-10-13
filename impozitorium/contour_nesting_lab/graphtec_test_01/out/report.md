# Graphtec test 01 — independent check

Status: SANDBOX_RESEARCH_ONLY. Not a production adapter.

| Check | Result | Detail |
|---|---|---|
| K1 marks: template = print = cut | PASS | 2 marks; max deviation 0.00000 mm; centres (mm from lower-left): (47.60, 8.52), (422.60, 8.52) |
| K2 counts | PASS | print placements 15, cut paths 30 (expected 15 and 30) |
| K3 every cut path explicitly closed ('s') and end = start | PASS | max end-start gap 0.000000 mm |
| K4 all cut paths inside the knife field | PASS | min margin to field 5.500 mm |
| K5 contour clearance between neighbouring outer contours | PASS | measured 4.0000 mm (flattening tolerance 0.002 mm per curve); required 4.0 mm |
| K6 every hole lies inside its outer contour | PASS | min hole-to-contour distance 16.498 mm |
| K7 print placements match cut contours (translation only, no reflection) | PASS | max offset mismatch 0.00000 mm; all placement matrices identity rotation: True |
| K8 print file contains no cut / hole strokes and no optional-content wrappers | PASS | cut-coloured strokes 0, OC markers present: False |
| K9 printed area inside the sheet | PASS | distance from printed area to sheet edge: left 31.60 mm, bottom 42.02 mm, right 8.40 mm, top 31.98 mm |
| K10 cut order from the leading edge; hole cut before its outer contour | PASS | lead edge assumed: left; longest straight cut 0.0 mm |

Layout: {'strategy': 'grid, centred in knife field', 'nx': 5, 'ny': 3, 'gap_mm': 4.0, 'lead_edge_assumed': 'left', 'orientation': 'identity (0 deg, no reflection)'}
Knife field (mm, lower-left origin): [28.1, 15.02, 445.1, 315.02]

Overlay: `overlay_print_plus_cut.png` — print render, cut contours (magenta), holes (green),
knife field (blue dashes), marks (orange), cut order numbers.
