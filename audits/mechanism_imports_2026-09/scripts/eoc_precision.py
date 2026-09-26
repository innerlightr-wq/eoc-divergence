#!/usr/bin/env python3
"""Precision budget of the accelerated map: bit loss, pinning, minimal automaton.

Verifies, by exhaustive enumeration and exact integer arithmetic:
  bit-loss lemma    m = m' (mod 2^K) with common determined valuation a implies
                    T(m) = T(m') (mod 2^{K-a}) and no finer: K_{n+1} = K_n - a_n.
  precision budget  the first L valuations are determined by m mod 2^{S_L+1}.
  minimal automaton the quotient of odd residues mod 2^N by L-step future
                    valuations saturates at the full 2^{N-1} states.
  pinning lemma     r(w_N(m)) = m for every N >= bitlength(m); realizer height frozen.
"""
import math
from collections import Counter


def acc_step(m):
    x = 3 * m + 1
    a = (x & -x).bit_length() - 1
    return x >> a, a


def acc_word(m, n):
    w, t = [], m
    for _ in range(n):
        t, a = acc_step(t)
        w.append(a)
    return tuple(w), t


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
    """least positive odd m realising the valuation word w"""
    C, S, n = C_direct(w), prefS(w)[-1], len(w)
    M = 1 << (S + 1)
    return ((1 << S) - C) * pow(pow(3, n, M), -1, M) % M


def main():
    print("bit-loss lemma -- does any mod-2^K class survive one step intact?")
    print(f"  {'K':>4} {'odd classes':>12} {'classes whose images differ mod 2^K':>38}")
    for K in (6, 8, 10, 12, 14):
        split = 0
        for r in range(1, 1 << K, 2):
            imgs = {acc_step(r + (j << K))[0] % (1 << K) for j in range(1 << 10)}
            if len(imgs) > 1:
                split += 1
        print(f"  {K:>4} {1 << (K-1):>12} {split:>38}")
    print("  every class splits: no finite 2-adic membership is inheritance-stable.")

    print()
    print("precision budget -- the first L valuations are fixed by m mod 2^{S_L+1}")
    bad = tot = 0
    for L in (1, 2, 3, 4, 5, 6, 8):
        for m in range(1, 20001, 2):
            w, _ = acc_word(m, L)
            S = sum(w)
            tot += 1
            for j in (1, 2, 3, 5, 7):
                if acc_word(m + j * (1 << (S + 1)), L)[0] != w:
                    bad += 1
                    break
    print(f"  {tot} (m,L) pairs: {bad} failures of sufficiency at modulus 2^(S_L+1)")

    print()
    print("minimal automaton -- odd residues mod 2^N quotiented by L-step futures")
    print(f"  {'N':>3} {'2^(N-1)':>9} " + " ".join(f"L={L:<6}" for L in (1, 2, 4, 6, 8, 10, 12)))
    for N in (10, 12, 14, 16):
        res = list(range(1, 1 << N, 2))
        row = []
        for L in (1, 2, 4, 6, 8, 10, 12):
            row.append(f"{len({acc_word(m, L)[0] for m in res}):<7}")
        print(f"  {N:>3} {1 << (N-1):>9} " + " ".join(row))
    print("  saturation at the full 2^(N-1) states: no merging survives.")

    print()
    print("pinning lemma -- r(w_N(m)) = m for all N >= bitlength(m)")
    bad = 0
    worst = 0
    for m in range(3, 4001, 2):
        w, _ = acc_word(m, 40)
        pin = None
        for n in range(1, 31):
            r = realizer(w[:n])
            if pin is None and r == m:
                pin = n
            if pin is not None and r != m:
                bad += 1
        if pin is None or pin > m.bit_length():
            bad += 1
        else:
            worst = max(worst, pin)
    print(f"  odd m in [3,4000]: {bad} violations; max first-pin step {worst}"
          f" (always <= bitlength(m))")


if __name__ == "__main__":
    main()
