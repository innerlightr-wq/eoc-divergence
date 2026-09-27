#!/usr/bin/env python3
"""Controls: shuffled valuation words (multiset-, hence density- and drift-preserving).

A shuffle keeps S_N and the letter histogram exactly and destroys only the ORDER.
Any regularity that survives shuffling is a property of the letter multiset;
any regularity that does not is a property of the arrangement.

Also computes the exact least positive odd realizer r(D) of a word D, by the
affine lifting of Phase 0 F3 (one residue class mod 2^{S+1}), in exact integers.
"""
import random
from math import log2

SEED = 20260924
MAPS = {"A": (3, 1), "B": (3, -1), "C": (5, 1)}


def v2(n):
    return (n & -n).bit_length() - 1


def word_of(x, q, r, L, guard=1 << 4000):
    w = []
    for _ in range(L):
        y = q * x + r
        if y <= 0 or y >= guard:
            break
        a = v2(y)
        w.append(a)
        x = y >> a
    return w


def realizer_simple(D, q, r):
    """Least positive odd x realizing the word D: lift one letter at a time
    (Phase 0 F3 says the answer is a single residue class mod 2^{S+1}),
    replaying the fixed prefix to reach the current iterate.  Exact integers."""
    c, M = 1, 1
    prefix = []
    for d in D:
        found = None
        for j in range(1 << d):
            cand = c + (j << M)
            xx, ok = cand, True
            for dd in prefix:
                yy = q * xx + r
                if v2(yy) != dd:
                    ok = False
                    break
                xx = yy >> dd
            if ok and v2(q * xx + r) == d:
                found = cand
                break
        if found is None:
            return None
        c, M = found, M + d
        prefix.append(d)
    return c


def confined(w, q, upper=False):
    """S_k <= floor(k log2 q) for all k (or >= +1 for the upper side)."""
    S = 0
    p = 1
    for k, a in enumerate(w, start=1):
        p *= q
        A = p.bit_length() - 1
        S += a
        if upper:
            if S < A + 1:
                return k - 1
        else:
            if S > A:
                return k - 1
    return len(w)


def main():
    random.seed(SEED)
    print("=" * 78)
    print("Control 1 -- shuffling a confined word of A destroys the confinement")
    print("=" * 78)
    holders = [27, 703, 10087, 270271, 626331, 1126015, 13421671, 26716671, 63728127]
    print("  holder        depth   shuffles still confined to that depth (of 2000)   "
          "median shuffled depth")
    for h in holders:
        w = word_of(h, 3, 1, 400)
        d = confined(w, 3)
        w = w[:d]
        keep, depths = 0, []
        for _ in range(2000):
            s = w[:]
            random.shuffle(s)
            dd = confined(s, 3)
            depths.append(dd)
            if dd >= d:
                keep += 1
        depths.sort()
        print(f"  {h:12d}  {d:5d}   {keep:6d}                                     "
              f"{depths[1000]:5d}")

    print()
    print("=" * 78)
    print("Control 2 -- least realizer r(D) of the record holders' own words (exact)")
    print("=" * 78)
    for h in holders[:6]:
        w = word_of(h, 3, 1, 400)
        d = confined(w, 3)
        w = w[:d]
        rr = realizer_simple(w, 3, 1)
        S = sum(w)
        print(f"  holder {h:10d}  depth {d:3d}  S = {S:4d}  r(D) = {rr:12d}  "
              f"(equals the holder: {rr == h})  log2 r = {log2(rr):.3f}  S - log2 r = {S - log2(rr):.3f}")

    print()
    print("=" * 78)
    print("Control 3 -- shuffled Haar words: confinement depth, all three maps")
    print("=" * 78)
    for M, (q, r) in MAPS.items():
        upper = (M == "C")
        random.seed(SEED)
        real, shuf = [], []
        for _ in range(4000):
            w = []
            for _ in range(300):
                k = 1
                while random.getrandbits(1):
                    k += 1
                w.append(k)
            real.append(confined(w, q, upper))
            s = w[:]
            random.shuffle(s)
            shuf.append(confined(s, q, upper))
        real.sort(); shuf.sort()
        side = "anti-confinement" if upper else "confinement"
        print(f"  {M} ({side}): Haar words, depth reached -- "
              f"median {real[2000]}, mean {sum(real)/len(real):.3f}; "
              f"shuffled: median {shuf[2000]}, mean {sum(shuf)/len(shuf):.3f}")
    print("  (a shuffle of a Haar word is again a Haar word in law, so these must agree:")
    print("   the control is calibrating the test, not testing the maps.)")


if __name__ == "__main__":
    main()
