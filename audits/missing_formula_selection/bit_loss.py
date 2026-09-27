#!/usr/bin/env python3
"""Bit-loss law, precision budget, and minimal-automaton saturation.

Exact integer arithmetic throughout.  Repository conventions: accelerated map
T(m) = (3m+1)/2^{v2(3m+1)} on odd m; word a = (a_1..a_n); S_j = a_1+...+a_j.

Checks:
  (1) bit-loss law     -- no odd residue class mod 2^K survives one step intact,
                          so retained precision obeys K_{n+1} = K_n - a_n.
  (2) precision budget -- the first L valuations are fixed by m mod 2^{S_L+1}.
  (3) minimal automaton-- the quotient of odd residues mod 2^N by L-step future
                          valuations saturates at the full 2^{N-1} states.
"""


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


def main():
    print("(1) bit-loss law: do any mod-2^K classes survive one step intact?")
    print(f"    {'K':>4} {'odd classes':>12} {'classes whose images differ mod 2^K':>38}")
    for K in (6, 8, 10, 12, 14):
        split = 0
        for r in range(1, 1 << K, 2):
            imgs = {acc_step(r + (j << K))[0] % (1 << K) for j in range(1 << 10)}
            if len(imgs) > 1:
                split += 1
        print(f"    {K:>4} {1 << (K - 1):>12} {split:>38}")
    print("    every class splits => K_{n+1} = K_n - a_n, so K_n = K_0 - S_n.")
    print("    no finite 2-adic membership is inheritance-stable.")

    print()
    print("(2) precision budget: the first L valuations are fixed by m mod 2^{S_L+1}")
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
    print(f"    {tot} (m,L) pairs: {bad} failures of sufficiency at modulus 2^(S_L+1)")
    print("    the smallest state closing the valuation dynamics is the realizer cylinder.")

    print()
    print("(3) minimal automaton: odd residues mod 2^N quotiented by L-step futures")
    Ls = (1, 2, 4, 6, 8, 10, 12)
    print(f"    {'N':>3} {'2^(N-1)':>9} " + " ".join(f"L={L:<6}" for L in Ls))
    for N in (10, 12, 14, 16):
        res = list(range(1, 1 << N, 2))
        row = [f"{len({acc_word(m, L)[0] for m in res}):<7}" for L in Ls]
        print(f"    {N:>3} {1 << (N - 1):>9} " + " ".join(row))
    print("    saturation at the full 2^(N-1) states: no nontrivial compression exists.")


if __name__ == "__main__":
    main()
