import math
W, H, g = 430.0, 290.0, 3.0   # PFI_BLADE_B2_ALPHA working area, mm
def n1(L, p, d):  # items of size d at pitch p in length L
    return 0 if L < d else int((L - d) // p + 1e-9) + 1
def hex_rows(Wx, Hy, d, g):  # Alpha: rows along x, odd rows shifted by p/2
    p = d + g; vy = p*math.sqrt(3)/2; rows = n1(Hy, vy, d)
    return sum(n1(Wx - (p/2 if r % 2 else 0), p, d) for r in range(rows))
def square(Wx, Hy, d, g): p = d + g; return n1(Wx, p, d)*n1(Hy, p, d)
worse, better_rot = [], []
for d10 in range(150, 1201, 5):
    d = d10/10
    a, s, b = hex_rows(W, H, d, g), square(W, H, d, g), hex_rows(H, W, d, g)
    if s > a: worse.append((d, a, s, b))
    if b > a: better_rot.append((d, a, b))
print("diameters 15..120 mm step 0.5, gap 3 mm, area 430x290")
print("Alpha hex < square grid:", len(worse), "cases; examples:", worse[:6])
print("hex rotated 90 > Alpha hex:", len(better_rot), "cases; examples:", better_rot[:6])
best_gain = max(((max(s, b)-a)/a, d, a, s, b) for d, a, s, b in [(d, hex_rows(W,H,d,g), square(W,H,d,g), hex_rows(H,W,d,g)) for d in [x/10 for x in range(150,1201,5)]])
print("max relative shortfall of Alpha hex vs best of {square, rotated hex}: %.1f%% at d=%s (alpha=%d square=%d rot=%d)" % (best_gain[0]*100, best_gain[1], best_gain[2], best_gain[3], best_gain[4]))
