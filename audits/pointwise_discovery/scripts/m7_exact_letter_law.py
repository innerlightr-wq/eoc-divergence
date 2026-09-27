"""M7 - the letter law at depth k under the confined ensemble, EXACTLY.

With  fwd[k][S] = #{confined prefixes of length k with total S}  and the
backward table  g_{k}(S)  of words.Table,

    P(a_k = d)  =  sum_S  fwd[k][S] * g_{k+1}(S+d)  /  num_n          (exact)

so both the integer cohort and the sampler can be tested against an exact
rational null with no Monte Carlo anywhere on the null side.
"""
import os, sys, math, glob, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction
import numpy as np
from eoc import Map, word_of
from words import Table
from m4d_strata import cohort

def exact_letter_law(mp, n, ks, dmax=12):
    t = Table(mp, n)
    num = t.num()
    # forward counts
    fwd = [[0] * (t.smax + 2) for _ in range(n + 1)]
    fwd[0][0] = 1
    for k in range(n):
        lo, hi = t.lo(k + 1), t.hi(k + 1)
        run = 0
        for S in range(0, t.smax + 1):
            run += fwd[k][S - 1] if S >= 1 else 0
            if lo <= S <= hi: fwd[k + 1][S] = run
    out = {}
    for k in ks:
        P = {}
        for d in range(1, dmax + 1):
            tot = 0
            for S in range(0, t.smax + 1):
                f = fwd[k][S]
                if f and S + d <= t.smax:
                    tot += f * t.gval(k + 1, S + d)
            P[d] = Fraction(tot, num)
        out[k] = P
    return out

def chi2_against(counts, P, N):
    x2 = 0.0; dof = 0
    for d, p in P.items():
        e = N * float(p)
        if e < 5: continue
        x2 += (counts.get(d, 0) - e) ** 2 / e
        dof += 1
    return x2, dof - 1

if __name__ == "__main__":
    mp = Map(3, 1); n = 140
    ks = [10, 30, 60, 90, 120, 139]
    print(__doc__.strip()); print()
    law = exact_letter_law(mp, n, ks)
    ms = cohort("results/scan_A36", n)
    roots = [m for m in ms if m % 3 != 2]
    W = [word_of(mp, m, n) for m in ms]
    WR = [word_of(mp, m, n) for m in roots]
    t = Table(mp, n); rng = random.Random(777)
    G = [t.sample(rng) for _ in range(20000)]
    print(f"{'k':>5} {'exact P(a=1)':>13} | "
          f"{'integers':>10} {'chi2':>8} {'dof':>4} {'z':>7} | "
          f"{'roots':>10} {'z':>7} | {'sampler':>9} {'z':>7}")
    for k in ks:
        P = law[k]
        row = f"{k:>5} {float(P[1]):>13.6f} | "
        for lbl, words in (("int", W), ("root", WR), ("gen", G)):
            from collections import Counter
            c = Counter(w[k] for w in words)
            x2, dof = chi2_against(c, P, len(words))
            z = (x2 - dof) / math.sqrt(2 * dof)
            if lbl == "int":
                row += f"{c[1]/len(words):>10.6f} {x2:>8.1f} {dof:>4} {z:>7.2f} | "
            else:
                row += f"{c[1]/len(words):>10.6f} {z:>7.2f} | " if lbl == "root" \
                       else f"{c[1]/len(words):>9.6f} {z:>7.2f}"
        print(row)
    print()
    print(f"integers: {len(W)} words ({len(WR)} chain roots); sampler: {len(G)} words.")
    print("z = (chi2 - dof)/sqrt(2 dof) against the EXACT rational law.")
    print("Note the integer cohort's words are correlated through the L1/L2 chains,")
    print("so its nominal chi2 is anticonservative; the chain-root column is not.")
