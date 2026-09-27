#!/usr/bin/env python3
"""The realizer-cylinder tree, the exponent identity, and the selection ratio Q.

Verifies, by exhaustive enumeration and exact integer/rational arithmetic:
  tree conservation      C(w) = disjoint union of C(wa), so N_M(w) = sum_a N_M(wa).
  precision/multiplicity mu(wa)/mu(w) = 2^{-a} and sum_a 2^{-a} = 1: the bits the
                         forward map destroys are exactly the tree's mass subdivision.
  exponent identity      h + I0 = alpha, h = alpha H2(1/alpha), I0 = alpha(1-H2(1/alpha)).
  selection ratio        A_{N,M} = Q_{N,M} * O_M * p_N, with Q measured.
  3x-1 control           Q collapses for 3x+1 and diverges for 3x-1.

Conventions match the repository.  C(w) is the residue class r_w + 2^{S_n+1} Z.
"""
import itertools, math
from fractions import Fraction

ALPHA = math.log2(3)


def H2(x):
    return -x * math.log2(x) - (1 - x) * math.log2(1 - x)


H_ENT = ALPHA * H2(1 / ALPHA)
I0 = ALPHA * (1 - H2(1 / ALPHA))


def prefS(w):
    S = [0]
    for a in w:
        S.append(S[-1] + a)
    return S


def C_direct(w):
    C = S = 0
    for a in w:
        C = 3 * C + (1 << S)
        S += a
    return C


def realizer(w):
    C, S, n = C_direct(w), prefS(w)[-1], len(w)
    M = 1 << (S + 1)
    return ((1 << S) - C) * pow(pow(3, n, M), -1, M) % M


def modulus(w):
    return 1 << (prefS(w)[-1] + 1)


def acc_word(m, n, p=3, q=1):
    w, t = [], m
    for _ in range(n):
        x = p * t + q
        a = (x & -x).bit_length() - 1
        w.append(a)
        t = x >> a
    return tuple(w), t


def N_M(w, M):
    r, mod = realizer(w), modulus(w)
    return 0 if r > M else 1 + (M - r) // mod


def confined_mass(nmax):
    """exact p_n = sum over zero-confined words of length n of 2^{-S_n}"""
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
    m_, S = [m for m in range(1, M + 1, 2)], None
    S = [0] * len(m_)
    out = [len(m_)]
    for n in range(1, nmax + 1):
        nc, ns, p3 = [], [], p ** n
        for m, s in zip(m_, S):
            x = p * m + q
            if x <= 0:
                continue
            a = (x & -x).bit_length() - 1
            s2 = s + a
            if (1 << s2) <= p3:
                nc.append(x >> a)
                ns.append(s2)
        m_, S = nc, ns
        out.append(len(m_))
        if not m_:
            break
    return out


def main():
    print("tree conservation -- C(w) partitioned by the next valuation")
    bad = tot = 0
    for M in (10 ** 4, 10 ** 6):
        for n in range(0, 6):
            for w in itertools.product((1, 2, 3), repeat=n):
                r = realizer(w) if w else 1
                mod = modulus(w) if w else 2
                elems = list(range(r, M + 1, mod)) if r <= M else []
                if w and len(elems) != N_M(w, M):
                    bad += 1
                buckets = {}
                for m in elems:
                    a = acc_word(m, n + 1)[0][n]
                    buckets[a] = buckets.get(a, 0) + 1
                for a, c in buckets.items():
                    if N_M(w + (a,), M) != c:
                        bad += 1
                tot += 1
    print(f"  {tot} nodes at M=1e4,1e6: {bad} partition failures")

    print()
    print("precision / multiplicity duality -- sum_a mu(wa) = mu(w)")
    bad = tot = 0
    A = 60
    for n in range(0, 8):
        for w in itertools.product((1, 2), repeat=n):
            S = prefS(w)[-1]
            s = sum(Fraction(1, 1 << (S + a)) for a in range(1, A + 1))
            tot += 1
            if s != Fraction(1, 1 << S) * (1 - Fraction(1, 1 << A)):
                bad += 1
    print(f"  {tot} words: {bad} failures (exact truncated geometric sum)")
    print("  precision lost per step = a_n = log2(1 / relative child mass).")

    print()
    print("exponent identity")
    print(f"  h  = alpha H2(1/alpha)       = {H_ENT:.7f}")
    print(f"  I0 = alpha (1 - H2(1/alpha)) = {I0:.7f}")
    print(f"  h + I0 = alpha               = {H_ENT + I0:.7f}")
    print("  the union bound adds 1 per confined word and so fails by 2^{h n}.")

    print()
    print("selection ratio  A_{N,M} = Q_{N,M} O_M p_N   (O_M = #odd m <= M)")
    P = confined_mass(60)
    print(f"  {'B':>3} {'N':>4} {'A_(N,M)':>10} {'O_M p_N':>13} {'Q':>8}")
    for B in (16, 20, 22):
        M = (1 << B) - 1
        sv = survivors(M, 50)
        O = (M + 1) // 2
        for N in (8, 16, 24, 32, 40, 48):
            if N >= len(sv):
                continue
            pred = O * float(P[N])
            print(f"  {B:>3} {N:>4} {sv[N]:>10} {pred:>13.3f} {sv[N]/pred:>8.4f}")

    print()
    print("3x-1 control -- same alpha, same p_N, but m=1 is a confined positive fixed point")
    M = (1 << 16) - 1
    O = (M + 1) // 2
    P = confined_mass(200)
    sp, sm = survivors(M, 190, 3, 1), survivors(M, 190, 3, -1)
    print(f"  {'N':>5} {'A(3x+1)':>9} {'A(3x-1)':>9} {'O_M p_N':>11} {'Q(3x+1)':>9} {'Q(3x-1)':>10}")
    for N in (48, 80, 100, 140, 180):
        pred = O * float(P[N])
        ap = sp[N] if N < len(sp) else 0
        am = sm[N] if N < len(sm) else 0
        print(f"  {N:>5} {ap:>9} {am:>9} {pred:>11.3e} {ap/pred:>9.3f} {am/pred:>10.3f}")
    print(f"  3x+1 extinct at N={max(i for i,v in enumerate(sp) if v>0)};"
          f"  3x-1 alive at N={max(i for i,v in enumerate(sm) if v>0)}")


if __name__ == "__main__":
    main()
