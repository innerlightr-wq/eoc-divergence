"""How far the smallest confined seed sits below the equidistribution prediction.

If the 0-confined residues were equidistributed in an initial window, the least
0-confined seed at depth N would sit near  rho(N) := 2/p(N,0)  (density p/2
among the integers, so the first hit is at ~2/p).  The actual least seed is
r_min(N).  The ratio  rho(N)/r_min(N)  measures the whole failure of the
aggregate-to-pointwise bridge: it is the factor by which one atypical integer
beats the average.
"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mass import mass

# r_min(N) over all odd seeds, from the repository's record-seed ladder, verified
# below by direct orbit iteration (depth of each record seed).
RECORDS = [3, 7, 27, 703, 10087, 35655, 381727]


def depth(m, cap=2000):
    x, S, p3 = m, 0, 1
    for j in range(1, cap + 1):
        t = 3 * x + 1
        v = (t & -t).bit_length() - 1
        S += v; x = t >> v; p3 *= 3
        if (1 << S) > p3:
            return j - 1
    return cap


print("record seed  confinement depth (direct iteration)")
dep = {}
for m in RECORDS:
    dep[m] = depth(m)
    print(f"{m:>11}  {dep[m]}")
print()
print(f"{'N':>4} {'r_min(N)':>10} {'rho(N)=2/p(N,0)':>17} {'rho/r_min':>10}")
best = 0.0
for N in [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 48, 56, 64, 72, 80]:
    cand = [m for m in RECORDS if dep[m] >= N]
    if not cand:
        break
    r = min(cand)
    p = float(mass(N, 0))
    rho = 2.0 / p
    best = max(best, rho / r)
    print(f"{N:>4} {r:>10} {rho:>17.2f} {rho/r:>10.4f}")
print()
print(f"largest observed rho/r_min over this range: {best:.4f}")
print("NOTE: r_min(N) here is the minimum over the record ladder only, so it is an")
print("UPPER bound on the true r_min(N); the ratio is therefore a LOWER bound.")
