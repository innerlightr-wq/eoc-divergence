#!/usr/bin/env python3
"""The finite-height selection ratio Q_{N,M}, and its exact relation to Delta_N.

Exact integer / rational arithmetic: p_N is an exact Fraction, A_{N,M} and
r_min(N,0) are exact integer counts.  Floating point is used only to report
logarithms.

Definitions (repository conventions):
  A_{N,M} = #{ m odd, 1 <= m <= M : m is zero-confined for N steps }   (integer)
  O_M     = #{ m odd, 1 <= m <= M } = ceil(M/2)
  p_N     = sum over zero-confined words of length N of 2^{-S_N}       (exact)
  Q_{N,M} = A_{N,M} / (O_M p_N)                    so  A = Q * O_M * p_N.

The identity A = Q O_M p_N is definitional.  Nothing here is a theorem about how
Q behaves.
"""
import math
from fractions import Fraction


def confined_mass(nmax):
    """exact p_n for n = 0..nmax, by DP over (length, cumulative valuation)"""
    f = {0: 1}
    P = [Fraction(1)]
    for n in range(1, nmax + 1):
        g = {}
        for S, c in f.items():
            a = 1
            while (1 << (S + a)) <= 3 ** n:
                g[S + a] = g.get(S + a, 0) + c
                a += 1
        f = g
        P.append(sum(Fraction(c, 1 << S) for S, c in f.items()))
    return P


def survivors(M, nmax, p=3, q=1):
    """A_{n,M} for n = 0..nmax: exact counts of odd m <= M still confined"""
    m_ = [m for m in range(1, M + 1, 2)]
    S = [0] * len(m_)
    out = [len(m_)]
    for n in range(1, nmax + 1):
        nc, ns, pn = [], [], p ** n
        for m, s in zip(m_, S):
            x = p * m + q
            if x <= 0:
                continue
            a = (x & -x).bit_length() - 1
            s2 = s + a
            if (1 << s2) <= pn:
                nc.append(x >> a)
                ns.append(s2)
        m_, S = nc, ns
        out.append(len(m_))
        if not m_:
            break
    return out


def is_confined(m, N):
    S = 0
    for j in range(1, N + 1):
        x = 3 * m + 1
        a = (x & -x).bit_length() - 1
        S += a
        m = x >> a
        if (1 << S) > 3 ** j:
            return False
    return True


def r_min(N, cap=10 ** 7):
    """least positive odd m that is zero-confined for N steps"""
    m = 1
    while m <= cap:
        if is_confined(m, N):
            return m
        m += 2
    return None


def main():
    P = confined_mass(60)

    print("(1) the identity A_{N,M} = Q_{N,M} * O_M * p_N, with Q measured")
    print(f"    {'B':>3} {'N':>4} {'A_(N,M)':>10} {'O_M':>10} {'p_N':>12} {'O_M p_N':>13} {'Q':>8}")
    for B in (16, 20, 22):
        M = (1 << B) - 1
        O = (M + 1) // 2
        sv = survivors(M, 50)
        for N in (8, 16, 24, 32, 40, 48):
            if N >= len(sv):
                continue
            pred = O * float(P[N])
            print(f"    {B:>3} {N:>4} {sv[N]:>10} {O:>10} {float(P[N]):>12.5e}"
                  f" {pred:>13.3f} {sv[N] / pred:>8.4f}")
    print("    measured over M = 2^16..2^22, N = 8..48 only.  No extrapolation is made.")

    print()
    print("(2) extinction depths: least N with A_{N,M} = 0 (A is integer-valued)")
    print(f"    {'B':>3} {'M':>10} {'last N with A>0':>17} {'A there':>9} {'first N with A=0':>18}")
    for B in (8, 10, 12, 14, 16):
        M = (1 << B) - 1
        sv = survivors(M, 120)
        last = max(i for i, v in enumerate(sv) if v > 0)
        print(f"    {B:>3} {M:>10} {last:>17} {sv[last]:>9} {last + 1:>18}")

    print()
    print("(3) relation to Delta_N, checked at M = r_min(N,0) where A_{N,M} = 1")
    print("    claims:  Q = 2/((M+1) p_N)   and   Delta_N = 1 - log2 Q - log2(1 + 1/M)")
    print(f"    {'N':>3} {'r_min':>8} {'A':>3} {'Q':>13} {'2/((M+1)p_N)':>14}"
          f" {'Delta_N':>9} {'1-log2Q-log2(1+1/M)':>21}")
    bad = 0
    for N in (4, 8, 12, 16, 20, 24, 28, 32, 36):
        M = r_min(N)
        if M is None:
            continue
        O = (M + 1) // 2
        A = sum(1 for m in range(1, M + 1, 2) if is_confined(m, N))
        Q = Fraction(A, 1) / (Fraction(O, 1) * P[N])
        Qclaim = Fraction(2, 1) / (Fraction(M + 1, 1) * P[N])
        delta = math.log2(M) - math.log2(1 / float(P[N]))
        rhs = 1 - math.log2(float(Q)) - math.log2(1 + 1 / M)
        ok = (A == 1) and (Q == Qclaim) and abs(delta - rhs) < 1e-9
        if not ok:
            bad += 1
        print(f"    {N:>3} {M:>8} {A:>3} {float(Q):>13.6f} {float(Qclaim):>14.6f}"
              f" {delta:>9.5f} {rhs:>21.5f}")
    print(f"    mismatches (A=1, Q formula, Delta relation): {bad}")
    print("    both relations are exact algebra, verified here on exact rationals.")

    print()
    print("(4) conditional extinction mechanism -- NOT a theorem")
    print("    A_{N,M} is a non-negative INTEGER, so any rigorous estimate giving")
    print("        Q_{N,M} * O_M * p_N < 1     forces     A_{N,M} = 0.")
    print("    Since p_N decays exponentially at rate I0 = 0.0793186 (with a polynomial")
    print("    correction), a bound Q <= poly(N) uniform in M would give A_{N,M} = 0 for")
    print("    N large depending on M.  No such bound on Q is known, and establishing one")
    print("    implies (DE): it is at least as strong, not an intermediate target.")


if __name__ == "__main__":
    main()
