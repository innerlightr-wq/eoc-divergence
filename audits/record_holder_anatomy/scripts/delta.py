"""Q5 -- the residual of the record holders against the random-placement null N0.

Delta_k(N) = log2 r_k(N) - log2 k - log2(1/p_N(0)) ,  expected ~ +1 under random
placement (the k-th smallest N-confined ODD integer sits near 2k/p_N(0), since odd
integers have density 1/2 and the confined ones have density p_N(0) among them).
p_N(0) is exact (nullmodel.transfer).  A systematic NEGATIVE drift means the record
holders are smaller than random placement predicts.
"""
import sys, math, collections
from nullmodel import transfer, log2_inv_p
from anatomy import A

def load(paths):
    acc = collections.defaultdict(list)
    for p in paths:
        for line in open(p):
            f = line.split(); acc[int(f[0])] += [int(x) for x in f[2:]]
    return {N: sorted(v)[:3] for N, v in acc.items()}

if __name__ == "__main__":
    tab = load(sys.argv[1:])
    Nmax = max(tab)
    nums = transfer(Nmax)
    print(f"{'N':>5} {'r1':>16} {'log2 r1':>9} {'log2(1/p_N)':>12} "
          f"{'D1':>7} {'D2':>7} {'D3':>7}")
    rows = []
    for N in sorted(tab):
        if N > Nmax: break
        L = log2_inv_p(N, nums)
        r = tab[N] + [None] * (3 - len(tab[N]))
        d = [ (math.log2(r[i]) - math.log2(i + 1) - L) if r[i] else None for i in range(3) ]
        rows.append((N, r, L, d))
    for N, r, L, d in rows:
        if N % 10 and N != Nmax: continue
        f = lambda x: f"{x:7.3f}" if x is not None else "      —"
        print(f"{N:>5} {r[0]:>16} {math.log2(r[0]):>9.3f} {L:>12.3f} "
              f"{f(d[0])} {f(d[1])} {f(d[2])}")
    # trend
    for i in range(3):
        xs = [N for N, _, _, d in rows if d[i] is not None and N >= 20]
        ys = [d[i] for N, _, _, d in rows if d[i] is not None and N >= 20]
        if len(xs) < 5: continue
        n = len(xs); mx = sum(xs)/n; my = sum(ys)/n
        sl = sum((x-mx)*(y-my) for x, y in zip(xs, ys)) / sum((x-mx)**2 for x in xs)
        res = [y - (my + sl*(x-mx)) for x, y in zip(xs, ys)]
        sd = (sum(t*t for t in res)/(n-2)) ** 0.5
        print(f"\nDelta_{i+1}:  N = 20..{max(xs)},  n = {n}")
        print(f"   mean = {my:+.3f}   min = {min(ys):+.3f}   max = {max(ys):+.3f}   "
              f"range = {max(ys)-min(ys):.3f}")
        print(f"   least-squares slope = {sl:+.5f} per step of N   "
              f"(over the whole range: {sl*(max(xs)-min(xs)):+.2f} bits)")
        print(f"   residual sd about the line = {sd:.3f} bits")

    # --- the unbiased sample: only the N at which r_k first takes a new value ---
    # r_k(N) is a step function while log2(1/p_N) rises smoothly, so Delta_k decays
    # deterministically inside a step (a saw-tooth).  The order statistic is sampled
    # exactly at the jumps, so that is where the null must be tested.
    print("\n" + "=" * 78)
    print("Q5 -- Delta at the JUMP points only (r_k first takes a new value)")
    # Poisson: r_k ~ Gamma(k, lambda), lambda = p_N/2 per integer, so
    #   E[log2 r_k] = log2(1/lambda) + psi(k)/ln2 ,  Delta_k = E[log2 r_k] - log2 k - log2(1/p_N)
    import math as _m
    G = 0.5772156649015329
    PSI = [-G, 1 - G, 1.5 - G]
    EXP = [1 + PSI[k] / _m.log(2) - _m.log2(k + 1) for k in range(3)]
    print("Poisson expectation (r_k ~ Gamma(k, p_N/2)):  "
          + ",  ".join(f"E[Delta_{k+1}] = {EXP[k]:+.3f}" for k in range(3)))
    print("=" * 78)
    for i in range(3):
        pts, seen = [], None
        for N, r, L, d in rows:
            if r[i] is None: continue
            if r[i] != seen:
                seen = r[i]; pts.append((N, d[i]))
        pts = [(N, v) for N, v in pts if N >= 10]
        if len(pts) < 5: continue
        xs = [N for N, _ in pts]; ys = [v for _, v in pts]
        n = len(xs); mx = sum(xs)/n; my = sum(ys)/n
        sl = sum((x-mx)*(y-my) for x, y in zip(xs, ys)) / sum((x-mx)**2 for x in xs)
        res = [y - (my + sl*(x-mx)) for x, y in zip(xs, ys)]
        sd = (sum(t*t for t in res)/max(1, n-2)) ** 0.5
        print(f"\nDelta_{i+1} at {n} jump points, N = {min(xs)}..{max(xs)}")
        print(f"   values: " + " ".join(f"{v:+.2f}" for _, v in pts))
        print(f"   mean = {my:+.3f}   sd = {(sum((y-my)**2 for y in ys)/max(1,n-1))**0.5:.3f}"
              f"   min = {min(ys):+.3f}   max = {max(ys):+.3f}")
        print(f"   slope = {sl:+.5f} per step of N  ->  {sl*(max(xs)-min(xs)):+.2f} bits "
              f"across the whole range;  residual sd {sd:.3f}")
        print(f"   offset against the Poisson expectation {EXP[i]:+.3f}:  {my-EXP[i]:+.3f} bits")
