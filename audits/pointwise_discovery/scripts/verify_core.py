"""Verification of the exact core against facts already established in
eoc-divergence.  Every check is exact; any mismatch aborts."""
import os, sys, math
from fractions import Fraction
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eoc import Map, T31, orbit, rare_depth, word_of, carry, realizer, \
                confined_word, p_mass_lower

FAIL = []
def check(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + (("  " + detail) if detail else ""))
    if not cond: FAIL.append(name)

MAPS = [Map(3,1), Map(3,-1), Map(5,1), Map(5,-1), Map(7,1), Map(7,-1), Map(3,5)]

# --- V1  aggregate identity, every map, exact -------------------------------
bad = 0
for mp in MAPS:
    for m0 in range(1, 4000, 2):
        o = orbit(mp, m0, 25)
        for n in range(len(o["a"]) + 1):
            if (1 << o["S"][n]) * o["m"][n] != mp.qpow(n) * m0 + mp.r * o["C"][n]:
                bad += 1
check("V1 aggregate identity 2^{S_n} m_n = q^n m_0 + r C_n", bad == 0,
      f"(7 maps, odd m0<4000, n<=25; violations {bad})")

# --- V2  Terras-Everett: word <-> one class mod 2^{S+1} ---------------------
bad = 0; tested = 0
for mp in [Map(3,1), Map(3,-1), Map(5,1), Map(5,-1)]:
    for m0 in range(1, 2000, 2):
        for n in (1, 3, 6, 9):
            w = word_of(mp, m0, n)
            C, S = carry(mp, w)
            r = realizer(mp, w)
            tested += 1
            # r realizes w, r is odd, r < 2^{S+1}, and m0 = r (mod 2^{S+1})
            if word_of(mp, r, n) != w or r % 2 == 0 or r >= (1 << (S+1)) \
               or (m0 - r) % (1 << (S+1)) != 0:
                bad += 1
check("V2 realizer(w) is least odd in the class mod 2^{S+1}", bad == 0,
      f"({tested} word/seed pairs, 4 maps; violations {bad})")

# --- V3  exact class count: #{odd m < 2^B : word_n(m) = w} = 2^{B-1-S} ------
mp = T31; bad = 0
B = 16
from collections import Counter
for n in (2, 4, 6):
    cnt = Counter(tuple(word_of(mp, m, n)) for m in range(1, 1 << B, 2))
    for w, c in cnt.items():
        S = sum(w)
        exp = (1 << (B - 1 - S)) if S + 1 <= B else None
        if exp is not None and c != exp: bad += 1
check("V3 class occupancy 2^{B-1-S} exact at X = 2^B", bad == 0,
      f"(B=16, n=2,4,6; violations {bad})")

# --- V4  p_N(0) transfer recursion vs published values ----------------------
p = p_mass_lower(T31, 300)
num2 = p[2] * (1 << T31.A(2))
conf2 = [m for m in range(1, 16, 2) if rare_depth(T31, m, cap=2) >= 2]
check("V4a num_2 = 3 and the 2-confined odd m<16 are {7,11,15}",
      num2 == 3 and conf2 == [7, 11, 15], f"(num_2={num2}, set={conf2})")
num14 = p[14] * (1 << T31.A(14))
check("V4b num_14 = 168807", num14 == 168807, f"(got {num14})")
tab = {10:-1.822, 20:-2.371, 50:-2.876, 100:-3.075, 150:-3.169,
       200:-3.202, 250:-3.283, 300:-3.277}
I0 = math.log2(3)*(1 - (lambda b: -b*math.log2(b)-(1-b)*math.log2(1-b))(1/math.log2(3)))
ok = True; rows = []
for N, want in tab.items():
    lg = -math.log2(float(p[N]))
    got = lg - I0*N - 1.5*math.log2(N)
    rows.append(f"N={N}:{got:+.3f}")
    if abs(got - want) > 0.002: ok = False
check("V4c log2(1/p_N) - I0 N - 1.5 log2 N reproduces the audit table", ok,
      " ".join(rows))
check("V4d I0 = 0.0793186128", abs(I0 - 0.0793186128) < 1e-10, f"({I0:.10f})")

# --- V5  num_N counts N-confined odd m in [1, 2^{A[N]+1}) -------------------
bad = 0
for N in (2, 3, 4, 5, 6, 8, 10, 12):
    Bn = T31.A(N) + 1
    cnt = sum(1 for m in range(1, 1 << Bn, 2) if rare_depth(T31, m, cap=N) >= N)
    if cnt != p[N] * (1 << T31.A(N)): bad += 1
check("V5 num_N = #{odd m < 2^{A[N]+1} : N-confined}", bad == 0,
      f"(N=2..12; violations {bad})")

# --- V6  record ladder start (published: 3,7,27,703,10087,...) --------------
best = {}
for m in range(1, 40000, 2):
    d = rare_depth(T31, m, cap=400)
    for n in range(1, d + 1):
        best.setdefault(n, m)
ladder = sorted(set(best[n] for n in best))
check("V6 3x+1 record ladder below 4e4 = [3,7,27,703,10087,35655]",
      ladder == [3,7,27,703,10087,35655], f"({ladder})")

# --- V7  the 3x-1 / 3x+1 sign conjugacy ------------------------------------
A, Bm = Map(3,1), Map(3,-1)
bad = 0
for m in range(1, 4000, 2):
    wa = word_of(Bm, m, 40)
    x = -m
    wb = []
    for _ in range(40):
        y = 3*x + 1
        a = (abs(y) & -abs(y)).bit_length() - 1
        x = y >> a if y % (1 << a) == 0 else y // (1 << a)
        wb.append(a)
    if wa != wb: bad += 1
check("V7 m -> -m conjugates 3x-1 on Z>0 to 3x+1 on Z<0 (identical words)",
      bad == 0, f"(odd m<4000, depth 40; violations {bad})")

# --- V8  3x-1 has the persistent seed m=1; 5x+1 has m=3 --------------------
check("V8a 3x-1: m=1 is rare-side confined to depth 2000",
      rare_depth(Map(3,-1), 1, cap=2000) == 2000)
check("V8b 5x+1: m=3 persists to depth 2000",
      rare_depth(Map(5,1), 3, cap=2000) == 2000)
check("V8c 5x-1: no odd m<20000 persists past depth 600",
      max(rare_depth(Map(5,-1), m, cap=600) for m in range(1,20000,2)) < 600)

print()
print("FAILURES:", FAIL if FAIL else "none")
