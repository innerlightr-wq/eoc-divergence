#!/usr/bin/env python3
"""Exact verification of Phase 0 (F1, F3) for all three maps.

No floating point in the decisions: every count is an exact integer, and every
probability is an exact Fraction.  Usage: python3 phase0_verify.py
"""
from fractions import Fraction
from itertools import product

MAPS = {"A (3x+1)": (3, 1), "B (3x-1)": (3, -1), "C (5x+1)": (5, 1)}


def v2(n):
    n = abs(n)
    k = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    return k


def step(x, q, r):
    y = q * x + r
    a = v2(y)
    return y >> a, a


def f1_exact(q, r, m):
    """Distribution of a(x) over ALL odd residues mod 2^m, as exact Fractions."""
    tot = 1 << (m - 1)
    dist = {}
    for x in range(1, 1 << m, 2):
        a = v2(q * x + r)
        if a >= m:            # residue class not resolved at this modulus
            a = ">= %d" % m
        dist[a] = dist.get(a, 0) + 1
    return {k: Fraction(c, tot) for k, c in dist.items()}


def f3_exact(q, r, n, dmax, m):
    """For every word D of length n with letters <= dmax, count the odd residues
    mod 2^m realizing it.  F3 predicts exactly 2^{m-1-S} for S = sum(D) < m."""
    counts = {}
    for x in range(1, 1 << m, 2):
        y, word, ok = x, [], True
        for _ in range(n):
            y, a = step(y, q, r)
            if a > dmax:
                ok = False
                break
            word.append(a)
        if ok:
            counts[tuple(word)] = counts.get(tuple(word), 0) + 1
    bad = []
    for D, c in counts.items():
        S = sum(D)
        if S + 1 <= m:
            pred = 1 << (m - 1 - S)
            if c != pred:
                bad.append((D, c, pred))
    return len(counts), bad


def main():
    print("=" * 72)
    print("F1  valuation law over all odd residues mod 2^20 (exact counts)")
    print("=" * 72)
    m = 20
    for name, (q, r) in MAPS.items():
        d = f1_exact(q, r, m)
        row = ", ".join(f"P(a={k})={v}" for k, v in sorted(d.items(), key=lambda t: str(t[0]))[:6])
        ok = all(d[k] == Fraction(1, 2 ** k) for k in range(1, m - 1) if k in d)
        mean = sum(Fraction(k) * v for k, v in d.items() if isinstance(k, int))
        print(f"{name:10s} {row}")
        print(f"{'':10s} geometric(1/2) exactly for 1<=k<{m-1}: {ok};  "
              f"truncated mean = {float(mean):.6f}  (exact limit 2)")

    print()
    print("=" * 72)
    print("F3  word -> residue-class correspondence, n=4 letters, letters<=4, mod 2^18")
    print("=" * 72)
    for name, (q, r) in MAPS.items():
        nwords, bad = f3_exact(q, r, 4, 4, 18)
        print(f"{name:10s} words seen: {nwords:4d};  violations of the exact count "
              f"2^(m-1-S): {len(bad)}")
        for b in bad[:3]:
            print("           ", b)

    print()
    print("=" * 72)
    print("F2  x -> -x conjugates A to B, checked on every odd |x| < 2^14")
    print("=" * 72)
    bad = 0
    for x in range(1, 1 << 14, 2):
        ax, aa = step(-x, 3, 1)
        bx, ab = step(x, 3, -1)
        if aa != ab or ax != -bx:
            bad += 1
    print(f"           A(-x) = -B(x) and equal valuations: violations = {bad}")


if __name__ == "__main__":
    main()
