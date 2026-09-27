"""The 5x-1 rare-side record ladder, recomputed over EVERY odd m < 2^32.

The published ladder in eoc-divergence/audits/cross_map sieves the scan to
m == 5 (mod 16) (scan_rare.c steps by the first-letter class modulus).  For
q > 4 that class is the seeds with v2(5m-1) = A[1]+1 = 3 exactly; seeds with
v2(5m-1) >= 4 are the class m == 13 (mod 16) and are never visited.  They are
admissible: the rare-side condition at n=1 is S_1 >= 3, not S_1 = 3.
"""
import os, sys, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eoc import Map, rare_depth
from pmass import p_series

mp = Map(5, -1)
d = json.load(open("results/scan_E32/merged.json"))
L = {int(k): v for k, v in d["L"].items()}
lad = []
for n in sorted(L):
    if not lad or L[n] != lad[-1][1]: lad.append((n, L[n]))
Nmax = max(L)
ps, errs = p_series(mp, Nmax)

print("5x-1 rare-side (anti-confinement) record ladder, COMPLETE scan of every")
print(f"odd m < 2^32 = 4.295e9.  {len(lad)} distinct holders, deepest N = {Nmax}.")
print()
print(f"{'N':>5} {'r_min(N)':>14} {'mod 16':>7} {'log2 r':>9} {'log2(1/p_N)':>12} {'Delta1':>8}")
rows = []
for n, m in lad:
    lg = math.log2(m); lp = -math.log2(float(ps[n]))
    rows.append((n, m, lg, lp, lg - lp))
    print(f"{n:>5} {m:>14} {m%16:>7} {lg:>9.4f} {lp:>12.4f} {lg-lp:>8.4f}")
json.dump(rows, open("results/m5_5x1_ladder.json", "w"))

bad = [r for r in rows if r[1] % 16 != 5]
print()
print(f"holders with r_min(N) != 5 (mod 16): {len(bad)} of {len(rows)}")
print(f"the smallest counterexample is N={bad[0][0]}, r_min={bad[0][1]} == {bad[0][1]%16} (mod 16)")
# independent exact recheck of the first few
print()
print("independent exact recheck (pure-Python rare_depth):")
for n, m, *_ in rows[:6]:
    dd = rare_depth(mp, m, cap=1000)
    smaller = [x for x in range(1, m, 2) if rare_depth(mp, x, cap=n) >= n]
    print(f"  N={n:>4}: depth({m}) = {dd:>4}  and no smaller odd m persists {n} steps: "
          f"{len(smaller) == 0}")
# Delta1 trend
xs = [r[0] for r in rows]; ys = [r[4] for r in rows]
mx, my = sum(xs)/len(xs), sum(ys)/len(ys)
sxy = sum((a-mx)*(b-my) for a, b in zip(xs, ys)); sxx = sum((a-mx)**2 for a in xs)
print()
print(f"Delta1 > 0 at {sum(1 for y in ys if y > 0)} of {len(ys)} holders; "
      f"least-squares slope = {sxy/sxx:+.4f} per unit N "
      f"(published, on the sieved ladder: +0.0211)")
