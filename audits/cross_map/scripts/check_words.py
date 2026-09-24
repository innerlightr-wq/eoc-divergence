#!/usr/bin/env python3
"""Combinatorial check of the transfer recursion: enumerate the admissible words
directly (DFS) and compare the tally w[S] with the prefix-sum recursion."""
from itertools import product

def Afloor(q, N):
    out = [0]*(N+1); p = 1
    for k in range(1, N+1):
        p *= q; out[k] = p.bit_length()-1
    return out

def rec(q, N, upper, hi):
    A = Afloor(q, N); w = [0]*(hi+2); w[0] = 1
    for k in range(1, N+1):
        acc = 0; pre = [0]*(hi+2)
        for S in range(hi+1):
            acc += w[S]; pre[S] = acc
        nw = [0]*(hi+2)
        lo, cap = (A[k]+1, hi) if upper else (1, A[k])
        for S2 in range(lo, min(cap, hi)+1):
            nw[S2] = pre[S2-1]
        w = nw
    return w

def brute(q, N, upper, hi):
    A = Afloor(q, N); w = [0]*(hi+2)
    def dfs(k, S):
        if k == N:
            w[S] += 1; return
        for a in range(1, hi - S + 1):
            S2 = S + a
            if upper:
                if S2 < A[k+1]+1: continue
            else:
                if S2 > A[k+1]: break
            if S2 > hi: break
            dfs(k+1, S2)
    dfs(0, 0)
    return w

print("  q  side   N  hi   recursion == brute enumeration?   total words")
for q, upper in ((3, False), (5, True), (7, True)):
    for N in (4, 6, 8):
        hi = Afloor(q, N)[N] + (8 if upper else 0)
        a, b = rec(q, N, upper, hi), brute(q, N, upper, hi)
        same = a[:hi+1] == b[:hi+1]
        print(f"  {q}  {'upper' if upper else 'lower'}  {N:2d}  {hi:3d}   "
              f"{'YES' if same else 'NO':3s}                              {sum(b)}")
