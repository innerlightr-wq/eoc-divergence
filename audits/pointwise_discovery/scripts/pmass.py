"""Exact rare-side word mass p_N for any (q,r), both sides, by forward counting.

nu_k(S) = number of rare-side words of length k with total S   (exact integers)
p_k     = sum_S nu_k(S) 2^{-S}                                  (exact Fraction)

For the upper side the totals are capped at Smax and the omitted mass is
returned as an exact upper bound, so every p_k is a certified bracket.
"""
from fractions import Fraction
from math import comb
from eoc import Map


def p_series(mp, N, smax=None):
    if mp.upper:
        smax = smax if smax is not None else 3 * N + 60
    else:
        smax = mp.A(N)
    nu = [0] * (smax + 2); nu[0] = 1
    ps, errs = [Fraction(1)], [Fraction(0)]
    for k in range(1, N + 1):
        lo = mp.A(k) + 1 if mp.upper else 0
        hi = smax if mp.upper else min(mp.A(k), smax)
        pre = 0; nxt = [0] * (smax + 2)
        for S in range(0, smax + 1):
            pre += nu[S - 1] if S >= 1 else 0
            if lo <= S <= hi: nxt[S] = pre
        nu = nxt
        ps.append(sum(Fraction(nu[S], 1 << S) for S in range(lo, hi + 1)))
        if mp.upper:
            e = Fraction(0)
            for S in range(smax + 1, smax + 300):
                e += Fraction(comb(S - 1, k - 1), 1 << S)
            errs.append(e)
        else:
            errs.append(Fraction(0))
    return ps, errs
