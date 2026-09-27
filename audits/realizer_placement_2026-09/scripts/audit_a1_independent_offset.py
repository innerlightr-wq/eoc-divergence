#!/usr/bin/env python3
"""A1: INDEPENDENT prediction of the failure offset t*_w (no failure labels used).

DERIVATION (DERIVED HERE).  Prefix w of length N, S = S_w, C = C_w, q_w = 2^(S+1),
r_w the least positive exact realizer (terminal parity: m_N odd).  Put
    x_w = (3^N r_w + C_w) / 2^S      (= m_N for the seed r_w; odd)
Lifted seeds r_w + q_w t have endpoint
    m_N(t) = x_w + 2*3^N*t.
Then
    3 m_N(t) + 1 = (3 x_w + 1) + 2*3^(N+1)*t = 2*( y + 3^(N+1) t ),   y := (3 x_w + 1)/2,
using that x_w is odd so 3x_w+1 is even.  Hence
    v_2(3 m_N(t)+1) = 1 + v_2( y + 3^(N+1) t ),
so, for a next-valuation cap K,
    FAILURE  <=>  v_2(3 m_N(t)+1) > K  <=>  y + 3^(N+1) t = 0 (mod 2^K)
             <=>  t = t*_w := -y * 3^(-(N+1))  (mod 2^K).
K from zero confinement at step N+1: 2^(S+a) <= 3^(N+1), so
    K = K(N,S) = max{a : 2^(S+a) <= 3^(N+1)} = floor((N+1)*alpha - S).
Confinement gives S <= floor(N*alpha), hence (N+1)*alpha - S >= alpha > 1, so K >= 1 ALWAYS.
This is asserted, not assumed.
"""
from fractions import Fraction
import math

def Kcap(N, S):
    a = 0
    while (1 << (S + a + 1)) <= 3 ** (N + 1): a += 1
    return a

def words(N):
    """all zero-confined words of length N as (word, S, C); exact integer test 2^S <= 3^j"""
    out = []
    def rec(k, S, C, w):
        if k == N:
            out.append((tuple(w), S, C)); return
        Cn = 3 * C + (1 << S)
        a = 1
        while (1 << (S + a)) <= 3 ** (k + 1):
            w.append(a); rec(k + 1, S + a, Cn, w); w.pop(); a += 1
    rec(0, 0, 0, [])
    return out

def realizer(N, S, C):
    """least positive EXACT realizer: modulus 2^(S+1), terminal parity m_N odd"""
    q = 1 << (S + 1)
    r = ((1 << S) - C) * pow(3, -N, q) % q
    return q if r == 0 else r

def acc_word(m, n):
    w = []; S = 0
    for _ in range(n):
        x = 3 * m + 1; a = (x & -x).bit_length() - 1
        w.append(a); S += a; m = x >> a
    return tuple(w), S, m

print(__doc__)
print("="*78)
print("A1. K >= 1 on every confined word, and the closed-form realizer realises w exactly")
print("="*78)
badK = badword = tot = 0
for N in range(1, 13):
    for w, S, C in words(N):
        tot += 1
        K = Kcap(N, S)
        if K < 1: badK += 1
        r = realizer(N, S, C)
        ww, SS, mN = acc_word(r, N)
        if ww != w or SS != S or mN % 2 == 0: badword += 1
print(f"  confined words N=1..12: {tot:,}   K<1: {badK}   word/parity mismatches: {badword}")

print()
print("="*78)
print("A1. INDEPENDENT offset prediction vs direct iteration, with edge-case census")
print("="*78)
cases = {k: 0 for k in ("no_fail_tstar_ge_n","exactly_one","multiple","tstar_outside",
                        "extinction_next","n_eq_1")}
mismatch = predbad = checked = 0
for B in (6, 8, 10, 12, 14):
    M = (1 << B) - 1
    for N in range(1, 13):
        for w, S, C in words(N):
            q = 1 << (S + 1)
            r = realizer(N, S, C)
            if r > M: continue
            n = (M - r) // q + 1              # lift interval size: t in [0,n)
            num = 3**N * r + C
            assert num % (1 << S) == 0, "x_w not integral"
            x = num >> S
            assert x % 2 == 1, "x_w not odd (terminal parity broken)"
            K = Kcap(N, S)
            # ---- PREDICTION, computed with no reference to failure labels ----
            y = (3 * x + 1) // 2
            tstar = (-y * pow(3, -(N + 1), 1 << K)) % (1 << K)
            nfail_pred = ((n - 1 - tstar) // (1 << K) + 1) if tstar < n else 0
            surv_pred = n - nfail_pred
            # ---- OBSERVATION by direct accelerated iteration ----
            fails = []
            for t in range(n):
                m0 = r + q * t
                mN = x + 2 * 3**N * t
                assert acc_word(m0, N)[2] == mN, "endpoint formula wrong"
                xx = 3 * mN + 1
                if ((xx & -xx).bit_length() - 1) > K: fails.append(t)
            checked += 1
            if len(fails) != nfail_pred: mismatch += 1
            if fails and {t % (1 << K) for t in fails} != {tstar}: predbad += 1
            # census
            if not fails and tstar >= n: cases["no_fail_tstar_ge_n"] += 1
            if len(fails) == 1: cases["exactly_one"] += 1
            if len(fails) > 1: cases["multiple"] += 1
            if tstar >= n: cases["tstar_outside"] += 1
            if surv_pred == 0: cases["extinction_next"] += 1
            if n == 1: cases["n_eq_1"] += 1
print(f"  (w,B) cylinder cases checked: {checked:,}")
print(f"  predicted-vs-observed failure COUNT mismatches: {mismatch}")
print(f"  observed failure class != predicted t*_w:        {predbad}")
print("  edge-case census (all reached, none skipped):")
for k, v in cases.items(): print(f"     {k:<22} {v:,}")
