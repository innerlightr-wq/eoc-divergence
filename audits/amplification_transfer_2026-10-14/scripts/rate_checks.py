"""Three exact checks against the repository's own statements -- see README."""
import math, os, sys
from fractions import Fraction as Q
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mass import counts, mass, sN, ok

alpha = math.log2(3)
H = lambda x: 0.0 if x <= 0.0 or x >= 1.0 else -x*math.log2(x)-(1-x)*math.log2(1-x)
J = lambda a: a*(1-H(1/a))                      # terminal-slope rate, in bits/step
I0 = J(alpha)

def tt(N, s):
    """C(s-1,N-1) 2^{-s}, exactly -- Occupation.tt."""
    return Q(math.comb(s-1, N-1), 1 << s)

print("=" * 78)
print("(1) the Lean sandwich  tt/N <= p <= (sN+1) tt   [Occupation/Rate.lean le_p, p_le]")
print("=" * 78)
print(f"{'N':>5} {'tt(N,sN)/N <= p':>18} {'p <= (sN+1)tt':>16}  both hold")
bad1 = 0
for N in [4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96]:
    p = mass(N, 0); s = sN(N); t = tt(N, s)
    lo, hi = t/N <= p, p <= (s+1)*t
    bad1 += (not lo) or (not hi)
    print(f"{N:>5} {str(lo):>18} {str(hi):>16}  {lo and hi}")
print(f"violations: {bad1}")

print()
print("=" * 78)
print("(2) IDENTITY  p(N,c) = P[S_j <= alpha j + c for all j<=N],  d_i iid Geom(1/2)")
print("    independent transfer-matrix over exact rationals; also sum over ALL words = 1")
print("=" * 78)
def walk_prob(N, c):
    """P[confined] by forward convolution on the exact distribution of S_j."""
    f = {0: Q(1)}
    for j in range(1, N+1):
        Smax = c + sN(j)
        g = {}
        for S, w in f.items():
            for d in range(1, Smax-S+1):
                T = S+d
                if ok(T, j, c):
                    g[T] = g.get(T, Q(0)) + w*Q(1, 1 << d)
        f = g
    return sum(f.values(), Q(0))
bad2 = 0
for N in [3, 5, 8, 11, 14, 18, 22, 26, 30]:
    for c in (0, 1, 3):
        a, b = mass(N, c), walk_prob(N, c)
        if a != b:
            bad2 += 1; print(f"  MISMATCH N={N} c={c}: {a} != {b}")
print(f"  exact agreement on 27 (N,c) pairs; mismatches: {bad2}")
# unconstrained total mass = 1 (no confinement): sum_s C(s-1,N-1)2^-s = 1
tot = [sum((tt(N, s) for s in range(N, 400)), Q(0)) for N in (3, 7, 12)]
print(f"  sum over ALL words of 2^-S_N (N=3,7,12): {[str(t) for t in tot]}   (must be 1)")

print()
print("=" * 78)
print("(3) drifting confinement budget  c = theta*N:  rate vs  J(alpha+theta)")
print(f"    I0 = J(alpha) = {I0:.12f};   J vanishes at theta = 2-alpha = {2-alpha:.9f}")
print("=" * 78)
print(f"{'theta':>7} {'J(alpha+theta)':>15} {'N=60':>11} {'N=120':>11} {'N=200':>11}")
for theta in [0.0, 0.05, 0.1, 0.2, 0.3, 0.41504, 0.5, 0.8]:
    pred = J(min(alpha+theta, 2.0)) if alpha+theta < 2.0 else 0.0
    row = []
    for N in (60, 120, 200):
        c = round(theta*N)
        p = mass(N, c)
        r = -(math.log2(p.numerator)-math.log2(p.denominator))/N if p else float('inf')
        row.append(r)
    print(f"{theta:>7.5f} {pred:>15.9f} " + " ".join(f"{x:>11.7f}" for x in row))
