#!/usr/bin/env python3
"""I1 adversarial: scan many intercepts; find those whose word has the FEWEST /
SHORTEST initial squares.  If some intercept has no square prefix with L in a
long range, I1 as stated fails."""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sturmian import *

def max_square_L(g, r, N, Lmax):
    s = word(g, r, N)
    best = 0; cnt = 0
    for L in range(1, Lmax + 1):
        if s[:L] == s[L:2*L]:
            best = L; cnt += 1
    return best, cnt

def best_exponent_above(g, r, N, Lmin, Lmax):
    """max over Lmin<=L<=Lmax of e(L) = (L+m(L))/L"""
    s = word(g, r, N)
    b, bl = 0.0, 0
    for L in range(Lmin, Lmax + 1):
        e = (L + initial_period_run(s, L)) / L
        if e > b: b, bl = e, L
    return b, bl

if __name__ == "__main__":
    N, LMAX = 2600, 1200
    TRIALS = 4000
    for name, g in [("log_3 2", log3_2()),
                    ("1/phi", from_cf([0] + [1] * 300)),
                    ("sqrt2-1", from_cf([0] + [2] * 250))]:
        rng = random.Random(7)
        worst_L, worst_r = 10**9, None
        worst_e, worst_er = 10.0, None
        nosq = 0
        for _ in range(TRIALS):
            r = rng.randrange(ONE)
            L, cnt = max_square_L(g, r, N, LMAX)
            if cnt == 0: nosq += 1
            if L < worst_L: worst_L, worst_r = L, r
            e, _ = best_exponent_above(g, r, N, 64, LMAX)
            if e < worst_e: worst_e, worst_er = e, r
        print(f"slope {name:<9}  {TRIALS} random intercepts, N={N}, L<= {LMAX}")
        print(f"   intercepts with NO square prefix at all      : {nosq}")
        print(f"   smallest 'largest square half-length'        : {worst_L}")
        print(f"   smallest best-exponent over 64<=L<={LMAX}    : {worst_e:.4f}")
        print(f"   (I4 needs e > max(1, gamma*log2 3); for these slopes that is 1.0)")
        print()
