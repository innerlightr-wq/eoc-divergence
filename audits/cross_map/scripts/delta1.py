#!/usr/bin/env python3
"""Item 3 -- record holders of D = 5x-1 against the exact rare-side mass.

Delta1(N) = log2 r_min(N) - log2(1 / p_N),  with p_N the EXACT dyadic mass of the
rare-side words of length N (integer prefix-sum transfer recursion, q = 5, upper
side).  This is the same null model as audits/record_holder_anatomy uses for A:
if the rare-side integers were placed at random with the density the words carry,
log2 r_min(N) would sit at log2(1/p_N) up to an O(1) residual.

Given Theorem P0, r_min(N) -> infinity is a THEOREM for D, not a conjecture; the
only open part is the rate.  That is the reverse of the situation for A.

Exact integers throughout; the only floating point is in the reported fits.
"""
import math
import random
import sys

random.seed(20260924)


def Afloor(q, N):
    out = [0] * (N + 1)
    p = 1
    for k in range(1, N + 1):
        p *= q
        out[k] = p.bit_length() - 1
    return out


def log2_mass(q, N, want, side, slack=300):
    """log2 p_k for k in `want`, where p_k = P(S_j >= A[j]+1 for all j <= k).
    States are truncated `slack` above A[k]; the discarded mass is < 2^{-slack}."""
    A = Afloor(q, N)
    hi = A[N] + (slack if side == "upper" else 0)
    w = [0] * (hi + 2)
    w[0] = 1
    out = {}
    want = set(want)
    for k in range(1, N + 1):
        acc = 0
        pre = [0] * (hi + 2)
        for S in range(hi + 1):
            acc += w[S]
            pre[S] = acc
        nw = [0] * (hi + 2)
        lo, cap = (A[k] + 1, hi) if side == "upper" else (1, A[k])
        for S2 in range(lo, cap + 1):
            nw[S2] = pre[S2 - 1]
        w = nw
        if k in want:
            # p_k = sum_S w[S] 2^{-S};  scale by 2^hi to stay in integers
            num = 0
            for S in range(hi + 1):
                if w[S]:
                    num += w[S] << (hi - S)
            out[k] = math.log2(num) - hi if num else float("-inf")
    return out


def load_ladder(paths):
    best = {}
    for p in paths:
        for line in open(p):
            n, m = line.split()
            n, m = int(n), int(m)
            if n not in best or m < best[n]:
                best[n] = m
    return best


def jumps(best):
    out = []
    prev = None
    for n in sorted(best):
        if best[n] != prev:
            out.append((n, best[n]))
            prev = best[n]
    return out


def theil_sen(xs, ys):
    sl = []
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            if xs[j] != xs[i]:
                sl.append((ys[j] - ys[i]) / (xs[j] - xs[i]))
    sl.sort()
    return sl[len(sl) // 2] if sl else float("nan")


def ols(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    return sxy / sxx, my - (sxy / sxx) * mx


def block_bootstrap(xs, ys, block=3, B=4000):
    n = len(xs)
    nb = max(1, n // block)
    out = []
    for _ in range(B):
        idx = []
        while len(idx) < n:
            s = random.randrange(0, max(1, n - block + 1))
            idx.extend(range(s, min(s + block, n)))
        idx = idx[:n]
        bx = [xs[i] for i in idx]
        by = [ys[i] for i in idx]
        if len(set(bx)) > 1:
            out.append(ols(bx, by)[0])
    out.sort()
    return out[int(0.025 * len(out))], out[int(0.975 * len(out))]


def main(q, side, paths):
    best = load_ladder(paths)
    J = jumps(best)
    Nmax = max(best)
    print(f"q={q} {side}-side ladder: depths 1..{Nmax}, {len(J)} distinct record holders")
    print(f"  deepest: r_min({Nmax}) = {best[Nmax]}")
    want = [n for n, _ in J]
    masses = log2_mass(q, Nmax, want, side)
    a = math.log2(q)
    I = a * (1 - (lambda b: -b * math.log2(b) - (1 - b) * math.log2(1 - b))(1 / a))
    print()
    print(f"  {'N':>4s} {'r_min(N)':>15s} {'log2 r_min':>11s} {'log2(1/p_N)':>12s} "
          f"{'Delta1':>9s} {'I*N+1.5log2N':>13s}")
    xs, ys = [], []
    for n, m in J:
        lr = math.log2(m)
        lp = -masses[n]
        d1 = lr - lp
        xs.append(n)
        ys.append(d1)
        print(f"  {n:4d} {m:15d} {lr:11.4f} {lp:12.4f} {d1:9.4f} "
              f"{I*n + 1.5*math.log2(n):13.4f}")
    pos = sum(1 for y in ys if y > 0)
    print()
    print(f"  Delta1 > 0 at {pos} of {len(ys)} record holders "
          f"(for A the published count is 24 of 24)")
    sl, ic = ols(xs, ys)
    ts = theil_sen(xs, ys)
    print(f"  OLS slope of Delta1 vs N : {sl:+.6f}   intercept {ic:+.4f}")
    print(f"  Theil-Sen slope          : {ts:+.6f}")
    for blk in (3, 8, 16):
        blo, bhi = block_bootstrap(xs, ys, block=blk)
        print(f"  block bootstrap 95% CI   : [{blo:+.6f}, {bhi:+.6f}]   "
              f"(blocks of {blk:2d}, 4000 resamples)")
    print(f"  implied growth exponent I(q) + slope = {I + sl:.6f}   (I({q}) = {I:.6f})")
    print()
    print("  Effective sample size: the holders are strongly serially correlated -- consecutive")
    print(f"  depths share a holder, so the {len(J)} rows are {len(J)} independent draws only if")
    print("  each new holder is independent of the last; lag-1 autocorrelation of Delta1:")
    d = [y - sum(ys) / len(ys) for y in ys]
    r1 = sum(d[i] * d[i + 1] for i in range(len(d) - 1)) / sum(x * x for x in d)
    neff = len(ys) * (1 - r1) / (1 + r1) if r1 < 1 else float("nan")
    print(f"    rho_1 = {r1:+.4f},  n_eff = n(1-rho)/(1+rho) = {neff:.1f}")


if __name__ == "__main__":
    main(int(sys.argv[1]), sys.argv[2], sys.argv[3:])
