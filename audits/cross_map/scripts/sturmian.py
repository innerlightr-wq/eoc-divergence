#!/usr/bin/env python3
"""Item 6 -- the Sturmian depth law and the Liouville argument, for general odd q.

Objects (following audits/sturmian_irrationality, with q in place of 3):

    alpha = log2 q,  theta = alpha - 1,  s_j = floor(j*alpha)
    Xi    = sum_{j>=0} q^{-(j+1)} 2^{s_j}   in Z_2   (v2 of term j is s_j -> infinity)
    p_n/q_n  convergents of alpha;  R_n = p_n - q_n*alpha, sign tested EXACTLY by 2^p vs q^k
    X_n    the lower mechanical block of the shell: |X_n| = q_n, S(X_n) = p_n
    delta_n = q^{q_n} - 2^{p_n},  C_n = C(X_n),  x_n = -C_n/delta_n  in Z_2

    DEPTH LAW:   v2(x_n + Xi) = p_n - 1                 at an upper convergent (R_n > 0)
                 v2(x_n + Xi) = p_n + p_{n+1} - 1       at a lower convergent (R_n < 0)

Everything below is exact integer / 2-adic arithmetic modulo 2^K.
"""
import sys
from decimal import Decimal, getcontext

getcontext().prec = 120


def alpha_dec(q):
    return Decimal(q).ln() / Decimal(2).ln()


def convergents(q, n_terms=14):
    a = alpha_dec(q)
    x = a
    cf = []
    for _ in range(n_terms):
        k = int(x)
        cf.append(k)
        frac = x - k
        if frac == 0:
            break
        x = 1 / frac
    ps, qs = [], []
    p0, q0, p1, q1 = 1, 0, cf[0], 1
    ps.append(p1); qs.append(q1)
    for k in cf[1:]:
        p0, q0, p1, q1 = p1, q1, k * p1 + p0, k * q1 + q0
        ps.append(p1); qs.append(q1)
    return cf, ps, qs


def sign_R(p, k, q):
    """sign(p - k*alpha) = sign(2^p - q^k), exact."""
    A, B = 1 << p, q ** k
    return (A > B) - (A < B)


def block_partials(pn, qn):
    """s_j of the lower mechanical block of the shell (p_n, q_n): s_j = j + floor(j*p'/q)."""
    pp = pn - qn
    return [j + (j * pp) // qn for j in range(qn)]


def carry(partials, q):
    """C = sum_{j<L} q^{L-1-j} 2^{s_j}, exact integer."""
    A = 0
    for s in partials:
        A = q * A + (1 << s)
    return A


def xi_mod(q, K):
    """Xi mod 2^K, via C_N * (q^N)^{-1} with s_N >= K."""
    M = 1 << K
    A = 0
    N = 0
    while True:
        s = (q ** N).bit_length() - 1          # floor(N*alpha), exact
        if s >= K:
            break
        A = (q * A + (1 << s)) % M
        N += 1
    return (A * pow(pow(q, N, M), -1, M)) % M


def v2(n, cap):
    if n == 0:
        return cap
    return (n & -n).bit_length() - 1


def check(q, K, nmax):
    cf, ps, qs = convergents(q)
    print(f"  alpha = log2 {q} = {alpha_dec(q):.15f}")
    print(f"  continued fraction: {cf}")
    print(f"  convergents p_n/q_n: {[f'{p}/{k}' for p, k in zip(ps, qs)][:nmax+2]}")
    Xi = xi_mod(q, K)
    M = 1 << K
    print(f"  {'n':>2s} {'q_n':>7s} {'p_n':>8s} {'shell':>6s} {'predicted depth':>16s} "
          f"{'measured v2(x_n+Xi)':>21s}  ok")
    for n in range(2, min(nmax, len(ps) - 1)):
        pn, qn = ps[n], qs[n]
        sg = sign_R(pn, qn, q)
        shell = "upper" if sg > 0 else "lower"
        pred = (pn - 1) if sg > 0 else (pn + ps[n + 1] - 1)
        if pred >= K - 4:
            print(f"  {n:2d} {qn:7d} {pn:8d} {shell:>6s} {pred:16d} "
                  f"{'(beyond modulus 2^%d)' % K:>21s}   -")
            continue
        Cn = carry(block_partials(pn, qn), q) % M
        dn = (q ** qn - (1 << pn)) % M
        xn = (-Cn * pow(dn, -1, M)) % M
        meas = v2((xn + Xi) % M, K)
        print(f"  {n:2d} {qn:7d} {pn:8d} {shell:>6s} {pred:16d} {meas:21d}  "
              f"{'OK' if meas == pred else 'MISMATCH'}")


def xi_upper_relation(q, K):
    """For q > 4 the extremal rare-side word is the UPPER mechanical word s_j = ceil(j*alpha).
    Since j*alpha is never an integer for j >= 1, ceil = floor + 1 there, so
        Xi_upper = 1/q + 2*(Xi_lower - 1/q) = 2*Xi_lower - 1/q,
    an affine relation over Q: one constant is irrational iff the other is."""
    M = 1 << K
    A, N = 0, 0
    while True:
        s = (q ** N).bit_length() - 1
        s_up = s + (1 if N >= 1 else 0)
        if s_up >= K:
            break
        A = (q * A + (1 << s_up)) % M
        N += 1
    xi_up = (A * pow(pow(q, N, M), -1, M)) % M
    xi_lo = xi_mod(q, K)
    pred = (2 * xi_lo - pow(q, -1, M)) % M
    return xi_up, pred, xi_up == pred


for q, K, nmax in ((3, 3000, 9), (5, 40000, 9), (7, 20000, 9)):
    print("=" * 92)
    print(f"q = {q}")
    print("=" * 92)
    check(q, K, nmax)
    if q > 4:
        _, _, ok = xi_upper_relation(q, 2000)
        print(f"  upper-side extremal word: Xi_upper = 2*Xi_lower - 1/{q} mod 2^2000 : "
              f"{'VERIFIED' if ok else 'FAILS'}")
    print()
