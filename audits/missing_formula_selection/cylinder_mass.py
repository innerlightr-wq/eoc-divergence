#!/usr/bin/env python3
"""Structure of C_n and mass conservation on the realizer-cylinder tree.

Exact integer / rational arithmetic throughout.  Repository conventions:
C_0 = 0, C_{k+1} = 3 C_k + 2^{S_k}; aggregate identity 2^{S_n} m_n = 3^n m_0 + C_n;
alpha = log2 3; H_j = j*alpha - S_j, so zero-confinement is 2^{S_j} <= 3^j.
The cylinder of a word w is the residue class C(w) = r_w + 2^{S_n+1} Z.

Checks:
  (1) switch decomposition      -- C_n is a signed sum of exactly r+2 monomials 3^a 2^b.
  (2) margin-switch tradeoff    -- r+1 >= 2*kappa*n/W - (alpha-1), kappa=(alpha-1)(2-alpha).
  (3) automatic confined height -- C_n <= (n/3) max(2^{S_n}, 3^n) on any confined word.
  (4) cylinder conservation     -- C(w) = disjoint union of C(wa): N_M(w) = sum_a N_M(wa).
  (5) precision/multiplicity    -- mu(wa)/mu(w) = 2^{-a} and sum_a 2^{-a} = 1.
  (6) exponent identity         -- h + I0 = alpha.
"""
import itertools, math
from collections import Counter
from fractions import Fraction

ALPHA = math.log2(3)
KAPPA = (ALPHA - 1) * (2 - ALPHA)


def H2(x):
    return -x * math.log2(x) - (1 - x) * math.log2(1 - x)


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


def N_M(w, M):
    r, q = realizer(w), modulus(w)
    return 0 if r > M else 1 + (M - r) // q


def runs(w):
    out, i = [], 0
    while i < len(w):
        j = i
        while j < len(w) and w[j] == w[i]:
            j += 1
        out.append((w[i], j - i, i, j))
        i = j
    return out


def switches(w):
    return sum(1 for i in range(1, len(w)) if w[i] != w[i - 1])


def C_boundary(w):
    """C_n = s_1 B_0 + sum_{t=1}^{l-1} 2 s_{t+1} B_t - s_l B_l, B_t = 2^{S_{p_t}} 3^{n-p_t}."""
    n, S, R = len(w), prefS(w), runs(w)
    sig = [1 if a == 1 else -1 for (a, _, _, _) in R]
    P = [0] + [q for (_, _, _, q) in R]
    t = {}

    def add(c, e3, e2):
        k = (e3, e2)
        t[k] = t.get(k, 0) + c
        if t[k] == 0:
            del t[k]

    add(sig[0], n - P[0], S[P[0]])
    for i in range(1, len(R)):
        add(2 * sig[i], n - P[i], S[P[i]])
    add(-sig[-1], n - P[-1], S[P[-1]])
    return t


def confined(w):
    S = 0
    for j, a in enumerate(w, 1):
        S += a
        if (1 << S) > 3 ** j:
            return False
    return True


def margins(w):
    S = prefS(w)
    return [j * ALPHA - S[j] for j in range(len(w) + 1)]


def acc_word(m, n):
    w, t = [], m
    for _ in range(n):
        x = 3 * t + 1
        a = (x & -x).bit_length() - 1
        w.append(a)
        t = x >> a
    return tuple(w), t


def main():
    print("(1) switch decomposition: C_n has exactly r+2 monomials, coeffs +-1 / +-2")
    badv = badc = badd = tot = 0
    coeffs = Counter()
    for n in range(1, 16):
        for w in itertools.product((1, 2), repeat=n):
            tot += 1
            tb = C_boundary(w)
            if sum(c * 3 ** e3 * (1 << e2) for (e3, e2), c in tb.items()) != C_direct(w):
                badv += 1
            if len(tb) != switches(w) + 2:
                badc += 1
            S, P = prefS(w), [0] + [q for (_, _, _, q) in runs(w)]
            mons = [(n - p, S[p]) for p in P]
            if len(set(mons)) != len(mons):
                badd += 1
            coeffs.update(tb.values())
    print(f"    {tot} words (all {{1,2}}-words, n<=15): value {badv}, count {badc}, distinctness {badd}")
    print(f"    coefficient multiset: {dict(sorted(coeffs.items()))}")

    print()
    print("(2) margin-switch tradeoff on zero-confined words")
    print(f"    kappa = (alpha-1)(2-alpha) = {KAPPA:.7f}; 2*kappa = {2 * KAPPA:.7f}")
    bad = tot = 0
    for n in range(1, 17):
        for w in itertools.product((1, 2), repeat=n):
            H = margins(w)
            if min(H) < -1e-12 or max(H) <= 0:
                continue
            tot += 1
            if switches(w) + 1 < 2 * KAPPA * n / max(H) - (ALPHA - 1) - 1e-9:
                bad += 1
    print(f"    {tot} zero-confined words (n<=16): {bad} violations of r+1 >= 2*kappa*n/W-(alpha-1)")

    print()
    print("(3) automatic confined height: C_n <= (n/3) max(2^{S_n}, 3^n), no balance needed")
    bad = tot = 0
    worst = 0.0
    for n in range(1, 17):
        for w in itertools.product((1, 2), repeat=n):
            if not confined(w):
                continue
            tot += 1
            C = C_direct(w)
            if 3 * C > n * 3 ** n:
                bad += 1
            worst = max(worst, C / 3 ** n)
    print(f"    {tot} zero-confined words (n<=16): {bad} violations; max C_n/3^n = {worst:.5f}")

    print()
    print("(4) cylinder conservation: C(w) partitioned by the next valuation")
    bad = tot = 0
    for M in (10 ** 4, 10 ** 6):
        for n in range(0, 6):
            for w in itertools.product((1, 2, 3), repeat=n):
                r = realizer(w) if w else 1
                q = modulus(w) if w else 2
                elems = list(range(r, M + 1, q)) if r <= M else []
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
    print(f"    {tot} nodes at M=1e4,1e6: {bad} partition failures (no truncation used)")

    print()
    print("(5) precision/multiplicity duality: sum_a mu(wa) = mu(w), mu(w)=2^{-S_n}")
    bad = tot = 0
    A = 60
    for n in range(0, 8):
        for w in itertools.product((1, 2), repeat=n):
            S = prefS(w)[-1]
            s = sum(Fraction(1, 1 << (S + a)) for a in range(1, A + 1))
            tot += 1
            if s != Fraction(1, 1 << S) * (1 - Fraction(1, 1 << A)):
                bad += 1
    print(f"    {tot} words: {bad} failures (exact truncated geometric sums)")
    print("    precision lost per step = a_n = log2(1 / relative child mass).")

    print()
    print("(6) exponent identity")
    h = ALPHA * H2(1 / ALPHA)
    I0 = ALPHA * (1 - H2(1 / ALPHA))
    print(f"    h  = alpha*H2(1/alpha)       = {h:.7f}")
    print(f"    I0 = alpha*(1 - H2(1/alpha)) = {I0:.7f}")
    print(f"    h + I0 = alpha               = {h + I0:.7f}")
    print("    a union bound over confined words over-counts the finite-height population")
    print("    by 2^{h n}: population counting alone cannot close the placement gap.")


if __name__ == "__main__":
    main()
