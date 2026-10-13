"""Circles in a narrow roll: fixed honeycomb (dX = 2R) vs. a lattice with free dX.

D is the circle diameter including the gap (D = 2R = d + g); W is usable roll width.
"""
import math

D, W = 40.0, 72.0  # W = 1.8 D
R = D / 2
# fixed honeycomb, rows across the width: dX = 2R, shift R, dY = sqrt(3) R
even = int((W - 2 * R) // (2 * R)) + 1
odd = int((W - 3 * R) // (2 * R)) + 1
dy = math.sqrt(3) * R
print("fixed hex, rows across: per row", even, odd, "row pitch %.2f" % dy, "-> %.1f pcs/m" % (1000 / dy * (even + odd) / 2))
# fixed honeycomb rotated 90 (columns along the feed)
cols = int((W - 2 * R) // (math.sqrt(3) * R)) + 1
print("fixed hex, columns along feed:", cols, "-> %.1f pcs/m" % (1000 / D * cols))
# lattice v1 = (2*dx, 0), v2 = (dx, b): zig-zag fitted to the width
dx = W - D
b = math.sqrt(D * D - dx * dx)
assert 2 * b >= D and 2 * dx >= D
print("fitted lattice: v1=(%.0f,0) v2=(%.0f,%.0f) -> %.1f pcs/m" % (2 * dx, dx, b, 1000 / b))
