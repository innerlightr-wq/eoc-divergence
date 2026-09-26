#!/usr/bin/env python3
"""The 3x-1 control for the finite-height selection ratio.

3x-1 shares alpha = log2 3, the confined-word count and the confined mass p_N with
3x+1: the symbolic side is identical.  It differs in that m = 1 is a zero-confined
POSITIVE fixed point, so its finite-height ensemble never empties.

Exact integer / rational arithmetic; floats only for reporting ratios.
"""
import math
from fractions import Fraction


def confined_mass(nmax):
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


def survivors(M, nmax, q):
    """A_{n,M} for the map m -> (3m+q)/2^{v2(3m+q)}"""
    m_ = [m for m in range(1, M + 1, 2)]
    S = [0] * len(m_)
    out = [len(m_)]
    for n in range(1, nmax + 1):
        nc, ns, pn = [], [], 3 ** n
        for m, s in zip(m_, S):
            x = 3 * m + q
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


def main():
    P = confined_mass(200)
    B = 16
    M = (1 << B) - 1
    O = (M + 1) // 2
    sp = survivors(M, 190, +1)
    sm = survivors(M, 190, -1)

    print(f"finite-height ensemble M = 2^{B} - 1 = {M}, O_M = {O}")
    print("the symbolic side (alpha, confined-word count, p_N) is IDENTICAL for both maps.")
    print()
    print(f"    {'N':>5} {'A(3x+1)':>9} {'A(3x-1)':>9} {'O_M p_N':>12}"
          f" {'Q(3x+1)':>9} {'Q(3x-1)':>10}")
    for N in (8, 24, 48, 64, 80, 100, 140, 180):
        if N >= len(P):
            break
        pred = O * float(P[N])
        ap = sp[N] if N < len(sp) else 0
        am = sm[N] if N < len(sm) else 0
        print(f"    {N:>5} {ap:>9} {am:>9} {pred:>12.4e}"
              f" {ap / pred:>9.3f} {am / pred:>10.3f}")

    lp = max(i for i, v in enumerate(sp) if v > 0)
    lm = max(i for i, v in enumerate(sm) if v > 0)
    print()
    print(f"    3x+1: last N with A>0 is {lp}; A = 0 from N = {lp + 1} onward.")
    print(f"    3x-1: still A = {sm[lm]} at N = {lm} (the fixed point m = 1 never dies).")
    print()
    print("    Q collapses to 0 for 3x+1 and grows for 3x-1 while p_N shrinks identically.")
    print("    Consequence for any future bound on Q: it must be SIGN-SENSITIVE, and it must")
    print("    fail on the 3x-1 positive anchor.  A bound blind to the sign of the anchor")
    print("    would falsely exclude m = 1 under 3x-1.")
    print()
    print("    This is a constraint on proofs, not evidence that Q is a powerful coordinate:")
    print("    Q separates the two maps because it is DEFINED from A_{N,M}, which is the")
    print("    quantity that differs.")


if __name__ == "__main__":
    main()
