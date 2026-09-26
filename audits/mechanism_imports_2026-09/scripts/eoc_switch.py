#!/usr/bin/env python3
"""Switch decomposition of C_n, and the margin-switch theorem.

Verifies, by exhaustive enumeration and exact integer arithmetic:
  Lemma A   C_n has exactly r+2 boundary terms, coefficients +-1 / +-2, distinct monomials.
  Lemma C/D r(w)+1 >= 2*kappa*n/W - (alpha-1) for a word confined to a drift band of width W.
  the mechanical extremal word has switch density r/n -> 2(2-alpha).

Conventions match the repository: word a=(a_1..a_n) over {1,2}; S_j = a_1+...+a_j;
H_j = j*alpha - S_j >= 0 is zero-confinement (2^{S_j} <= 3^j).
"""
import itertools, math
from collections import Counter

ALPHA = math.log2(3)
KAPPA = (ALPHA - 1) * (2 - ALPHA)


def prefS(w):
    S = [0]
    for a in w:
        S.append(S[-1] + a)
    return S


def C_direct(w):
    """C_n from the repository recursion C_0 = 0, C_{k+1} = 3 C_k + 2^{S_k}."""
    C = S = 0
    for a in w:
        C = 3 * C + (1 << S)
        S += a
    return C


def runs(w):
    """maximal constant runs as (letter, length, start, end)"""
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
    """Lemma A: C_n = s_1 B_0 + sum_{t=1}^{l-1} 2 s_{t+1} B_t - s_l B_l,
       B_t = 2^{S_{p_t}} 3^{n-p_t}.  Returns {(e3,e2): coeff}."""
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


def ev(t):
    return sum(c * 3 ** e3 * (1 << e2) for (e3, e2), c in t.items())


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


def main():
    print("Lemma A -- boundary form of C_n, exhaustive over {1,2}-words")
    bad_val = bad_cnt = bad_dist = tot = 0
    coeffs = Counter()
    for n in range(1, 16):
        for w in itertools.product((1, 2), repeat=n):
            tot += 1
            tb = C_boundary(w)
            if ev(tb) != C_direct(w):
                bad_val += 1
            if len(tb) != switches(w) + 2:
                bad_cnt += 1
            P = [0] + [q for (_, _, _, q) in runs(w)]
            S = prefS(w)
            mons = [(n - p, S[p]) for p in P]
            if len(set(mons)) != len(mons):
                bad_dist += 1
            coeffs.update(tb.values())
    print(f"  words tested                : {tot}")
    print(f"  boundary form evaluates to C: {bad_val} mismatches")
    print(f"  term count == r+2           : {bad_cnt} mismatches")
    print(f"  monomials pairwise distinct : {bad_dist} violations")
    print(f"  coefficient multiset        : {dict(sorted(coeffs.items()))}")

    print()
    print("Lemma C/D -- margin-switch tradeoff, exhaustive over zero-confined words")
    print(f"  kappa = (alpha-1)(2-alpha) = {KAPPA:.7f}   2*kappa = {2*KAPPA:.7f}")
    bad = tot = 0
    for n in range(1, 17):
        for w in itertools.product((1, 2), repeat=n):
            H = margins(w)
            if min(H) < -1e-12:
                continue
            W = max(H)
            if W <= 0:
                continue
            tot += 1
            if switches(w) + 1 < 2 * KAPPA * n / W - (ALPHA - 1) - 1e-9:
                bad += 1
    print(f"  zero-confined words tested  : {tot}")
    print(f"  violations of r+1 >= 2*kappa*n/W - (alpha-1): {bad}")

    print()
    print("mechanical extremal word a_j = floor(j*alpha) - floor((j-1)*alpha)")
    print(f"  predicted switch density 2(2-alpha) = {2*(2-ALPHA):.7f}")
    for n in (1000, 10000, 100000):
        w = tuple(int(j * ALPHA) - int((j - 1) * ALPHA) for j in range(1, n + 1))
        assert confined(w)
        print(f"  n={n:>7}  max margin={max(margins(w)):.4f}  r/n={switches(w)/n:.7f}")


if __name__ == "__main__":
    main()
