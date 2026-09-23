"""Q5 -- the record holders against the random-placement null N0, on two populations.

ALL    the k-th smallest N-confined odd integer, null density p_N(0);
ROOTS  the k-th smallest N-confined CHAIN ROOT (m != 2 mod 3), null density
       q_N(0) = (2/3) p_N(0) exactly, because 2^{S+1} is invertible mod 3 so each
       residue class mod 2^{S+1} is exactly 2/3 roots.

Why ROOTS.  L1 says a confined m = 2 (mod 3) has a smaller, more-confined backward
image, and by L2 the chain has length v3(m+1).  So confined integers come in chains
and are NOT independent; the Poisson expectations for Delta_2, Delta_3 assume an
independence that fails.  Thinning to chain roots removes exactly that dependence.

Delta_k = log2 r_k(N) - log2 k - log2(1/density_N) ,
E[Delta_k] = 1 + psi(k)/ln2 - log2 k  =  +0.167, +0.610, +0.746  for k = 1,2,3.
"""
import sys, math, collections
from nullmodel import transfer, log2_inv_p
from anatomy import A

G = 0.5772156649015329
PSI = [-G, 1 - G, 1.5 - G]
EXP = [1 + PSI[k] / math.log(2) - math.log2(k + 1) for k in range(3)]

def load(paths, tag=None):
    acc = collections.defaultdict(list)
    for p in paths:
        for line in open(p):
            f = line.split()
            if f[0] in ("A", "R"):
                if tag and f[0] != tag: continue
                N = int(f[1]); vals = [int(x) for x in f[3:]]
            else:
                if tag == "R": continue
                N = int(f[0]); vals = [int(x) for x in f[2:]]
            acc[N] += vals
    return {N: sorted(v)[:3] for N, v in acc.items()}

def analyse(tab, nums, label, shift):
    """shift = log2(p_N / density_N):  0 for ALL, log2(3/2) for ROOTS."""
    Nmax = max(tab)
    rows = []
    for N in sorted(tab):
        L = log2_inv_p(N, nums) + shift
        r = tab[N] + [None] * (3 - len(tab[N]))
        d = [(math.log2(r[i]) - math.log2(i + 1) - L) if r[i] else None for i in range(3)]
        rows.append((N, r, L, d))
    print(f"\n{'='*84}\n{label}   (N = 1..{Nmax})\n{'='*84}")
    out = {}
    for i in range(3):
        pts, seen = [], None
        for N, r, L, d in rows:
            if r[i] is None: continue
            if r[i] != seen:
                seen = r[i]; pts.append((N, d[i], r[i]))
        pts = [(N, v, m) for N, v, m in pts if N >= 10]
        if len(pts) < 5: continue
        xs = [N for N, _, _ in pts]; ys = [v for _, v, _ in pts]
        n = len(xs); mx = sum(xs)/n; my = sum(ys)/n
        sxx = sum((x-mx)**2 for x in xs)
        sl = sum((x-mx)*(y-my) for x, y in zip(xs, ys)) / sxx
        res = [y - (my + sl*(x-mx)) for x, y in zip(xs, ys)]
        sd = (sum(t*t for t in res)/max(1, n-2)) ** 0.5
        se = sd / math.sqrt(sxx)
        span = sl * (max(xs) - min(xs))
        print(f"\nDelta_{i+1}, at {n} jump points, N = {min(xs)}..{max(xs)}")
        print(f"   mean {my:+.3f}   sd {(sum((y-my)**2 for y in ys)/max(1,n-1))**0.5:.3f}"
              f"   min {min(ys):+.3f}   max {max(ys):+.3f}")
        print(f"   Poisson E[Delta_{i+1}] = {EXP[i]:+.3f}   ->  offset {my-EXP[i]:+.3f} bits")
        print(f"   slope {sl:+.6f}/step  ({span:+.2f} bits across the range),"
              f"  s.e. {se*(max(xs)-min(xs)):.2f} bits  ->  {abs(span)/(se*(max(xs)-min(xs))+1e-12):.1f} sigma")
        out[i+1] = (my, my-EXP[i], span, se*(max(xs)-min(xs)))
    return out

if __name__ == "__main__":
    paths = sys.argv[1:]
    both = any(open(p).readline().startswith(("A ", "R ")) for p in paths)
    tabA = load(paths, "A" if both else None)
    nums = transfer(max(tabA))
    analyse(tabA, nums, "POPULATION 'ALL' -- every N-confined odd integer", 0.0)
    if both:
        tabR = load(paths, "R")
        analyse(tabR, nums, "POPULATION 'ROOTS' -- chain roots only (m != 2 mod 3), "
                            "null density (2/3) p_N(0)", math.log2(1.5))
