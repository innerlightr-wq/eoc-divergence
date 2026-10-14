"""r_min(N) and the initial-window count of 0-confined seeds.

Defines  W(N,X) = #{ m odd, m < X : 2^{S_j(m)} <= 3^j for all j <= N },
         r_min(N) = least such m (over all X), and compares W(N,X) with the
"fair value" X*p(N,0)/2 that equidistribution of the confined residues would
give.  Integer arithmetic throughout.

The point: a purely MULTIPLICATIVE bound  W(N,X) <= C N^B X p(N,0)  with no
additive term would force W(N,X_0)=0 for every fixed X_0 and all large N,
i.e. r_min(N) -> infinity, i.e. pointwise divergence exclusion.  So the exact
size of the additive discrepancy is the whole question.
"""
import os, sys, math
from fractions import Fraction as Q
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mass import mass, sN


def depth(m: int, cap: int) -> int:
    """The largest N <= cap with 2^{S_j} <= 3^j for all j <= N."""
    x, S, p3 = m, 0, 1
    for j in range(1, cap + 1):
        t = 3 * x + 1
        v = (t & -t).bit_length() - 1
        S += v; x = t >> v; p3 *= 3
        if (1 << S) > p3:
            return j - 1
    return cap


CAP = 40
X = 1 << 17          # scan all odd m < 131072
dep = {}
for m in range(1, X, 2):
    dep[m] = depth(m, CAP)

print(f"scanned all {X//2} odd m < {X}, confinement depth capped at {CAP}")
print()
print(f"{'N':>3} {'r_min(N)':>10} {'W(N,X)':>9} {'fair = X p/2':>14} {'W/fair':>9} "
      f"{'p(N,0)':>12}")
for N in range(1, 25):
    conf = [m for m, d in dep.items() if d >= N]
    p = mass(N, 0)
    fair = float(Q(X, 2) * p)
    rmin = min(conf) if conf else None
    print(f"{N:>3} {str(rmin):>10} {len(conf):>9} {fair:>14.3f} "
          f"{(len(conf)/fair if fair else float('nan')):>9.4f} {float(p):>12.5e}")

print()
print("r_min(N) for N = 1..40 (over odd m < 2^17):")
row = []
for N in range(1, CAP + 1):
    conf = [m for m, d in dep.items() if d >= N]
    row.append(min(conf) if conf else '>2^17')
print("  " + "  ".join(f"N={i+1}:{v}" for i, v in enumerate(row)))
