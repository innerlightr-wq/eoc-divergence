#!/usr/bin/env python3
"""Exactness check on the rare-side mass: Terras-Everett says the number of odd
m < 2^{K+1} that are N-persistent equals exactly 2^K * p_N, for K >= max admissible S.
Brute force against the transfer recursion, for both sides."""
import math
from fractions import Fraction

def Afloor(q, N):
    out = [0]*(N+1); p = 1
    for k in range(1, N+1):
        p *= q; out[k] = p.bit_length()-1
    return out

def mass(q, N, upper, slack):
    A = Afloor(q, N); hi = A[N] + (slack if upper else 0)
    w = [0]*(hi+2); w[0] = 1
    for k in range(1, N+1):
        acc = 0; pre = [0]*(hi+2)
        for S in range(hi+1):
            acc += w[S]; pre[S] = acc
        nw = [0]*(hi+2)
        lo, cap = (A[k]+1, hi) if upper else (1, A[k])
        for S2 in range(lo, cap+1):
            nw[S2] = pre[S2-1]
        w = nw
    return sum(Fraction(c, 1 << S) for S, c in enumerate(w) if c), w, hi

def v2(n):
    return (n & -n).bit_length()-1

def brute(q, r, N, K, upper):
    A = Afloor(q, N); c = 0
    for m in range(1, 1 << (K+1), 2):
        x, S, ok = m, 0, True
        for k in range(1, N+1):
            y = q*x + r
            a = v2(y); S += a; x = y >> a
            if (S < A[k]+1) if upper else (S > A[k]):
                ok = False; break
        if ok: c += 1
    return c

print("  q  r  side   N   K   brute count   2^K * p_N (truncated at K)   equal?")
for q, r, upper in ((3, 1, False), (5, -1, True), (5, 1, True)):
    for N in (3, 5, 7):
        p, w, hi = mass(q, N, upper, 12)
        K = min(hi, 22)
        # restrict the recursion mass to words with S <= K, which is what m < 2^{K+1} can see
        pk = sum(Fraction(c, 1 << S) for S, c in enumerate(w) if c and S <= K)
        pred = pk * (1 << K)
        b = brute(q, r, N, K, upper)
        print(f"  {q}  {r:+d}  {'upper' if upper else 'lower'}  {N:2d}  {K:2d}   {b:11d}   "
              f"{str(pred):>26s}   {'YES' if Fraction(b) == pred else 'NO'}")
