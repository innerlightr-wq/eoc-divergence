"""Delta_2 and Delta_3 on both populations: are the r2/r3 deviations explained by the chains?

For k = 1 the two populations coincide, because L4 says r_1(N) is ALWAYS a chain root, so
the first confined integer and the first confined root are the same number and the thinned
null differs only by the constant log2(3/2).  For k = 2, 3 they genuinely differ.
"""
import math, glob, collections
from q5b import load
from q5fit import compare, bootstrap
from nullmodel import transfer, log2_inv_p

E = [1 + p/math.log(2) - math.log2(k+1) for k, p in
     enumerate([-0.5772156649015329, 1-0.5772156649015329, 1.5-0.5772156649015329])]
CH2 = '/tmp/claude-1000/-home-elias/c3a43061-2697-4bee-adda-ceb1e6215d18/scratchpad/chunks2/*.txt'
BOUND = 2.5e11

def jumps(tab, nums, k, shift):
    pts, seen = [], None
    B = math.log2(BOUND)
    for N in sorted(tab):
        row = tab[N]
        if len(row) <= k: continue
        if row[k] != seen:
            seen = row[k]; L = log2_inv_p(N, nums) + shift
            d = math.log2(seen) - math.log2(k+1) - L
            thr = B - L - math.log2(k+1)
            if thr >= d + 3.5: pts.append((N, d, seen))
    return pts

R = glob.glob(CH2)
tabA = load(R, "A"); tabR = load(R, "R")
nums = transfer(max(tabA))
print("Does the lineage thinning explain the r2 / r3 deviation?")
print("(k = 1 is identical on the two populations up to the constant log2(3/2) = 0.585,")
print(" because L4 makes r_1 always a root -- verified below.)\n")
same = all(tabA[N][0] == tabR[N][0] for N in tabA if N in tabR)
print(f"  r_1(N) == rho_1(N) at every N:  {'YES (this is L4)' if same else 'NO'}")
n2 = sum(1 for N in tabA if N in tabR and len(tabA[N])>1 and len(tabR[N])>1 and tabA[N][1]!=tabR[N][1])
n3 = sum(1 for N in tabA if N in tabR and len(tabA[N])>2 and len(tabR[N])>2 and tabA[N][2]!=tabR[N][2])
print(f"  r_2 differs from rho_2 at {n2} values of N;  r_3 from rho_3 at {n3}\n")
print(f"{'k':>2} {'population':>8} {'n':>4} {'mean D':>8} {'Poisson E':>10} {'offset':>8} "
      f"{'slope b':>10} {'95% CI for b':>26}")
for k in (0, 1, 2):
    for name, tab, sh in (("ALL", tabA, 0.0), ("ROOTS", tabR, math.log2(1.5))):
        pts = jumps(tab, nums, k, sh)
        if len(pts) < 6: continue
        xs = [N for N, _, _ in pts]; ys = [d for _, d, _ in pts]
        my = sum(ys)/len(ys)
        wins, ci, ms = bootstrap(xs, ys, B=4000)
        print(f"{k+1:>2} {name:>8} {len(pts):>4} {my:>8.3f} {E[k]:>10.3f} {my-E[k]:>8.3f} "
              f"{ms:>10.5f} {f'[{ci[0]:+.5f}, {ci[1]:+.5f}]':>26}")
