#!/usr/bin/env python3
"""O5 -- law-of-the-iterated-logarithm envelope of the drift.

LIL for i.i.d. letters with mean 2 and variance 2:

    limsup_n (S_n - 2n) / sqrt(4 n ln ln n) = +1 ,   liminf = -1   (a.s.)

Three populations:
  (1) Haar words  -- the reference; the envelope must approach 1.
  (2) integer orbits of A and B -- finite, because every orbit is captured by a
      cycle in O(log x) steps.  The point of the measurement is that the LIL
      cannot be probed on them at all.
  (3) integer orbits of C -- (conjecturally) infinite for almost every seed, so
      the envelope can be probed; big-integer arithmetic, exact.
"""
import random
from math import log, sqrt, log2

SEED = 20260924
random.seed(SEED)

def geom():
    """a ~ geometric(1/2) on {1,2,...}: count trailing zeros of a uniform odd-shifted draw."""
    k = 1
    while random.getrandbits(1):
        k += 1
    return k

def lil_scan(letters, label, report_at=(100, 1000, 10000, 100000, 1000000, 10000000)):
    S = 0
    n = 0
    hi = -1e18
    lo = 1e18
    out = []
    nxt = set(report_at)
    for a in letters:
        S += a
        n += 1
        if n >= 100:
            d = sqrt(4.0 * n * log(log(n)))
            if d > 0:
                z = (S - 2.0 * n) / d
                if z > hi: hi = z
                if z < lo: lo = z
        if n in nxt:
            out.append((n, hi, lo, (S - 2.0 * n) / n))
    print(f"  {label}")
    print(f"      n          running max     running min     (S_n-2n)/n")
    for n, h, l, m in out:
        print(f"    {n:10d}   {h:+.6f}      {l:+.6f}      {m:+.6f}")
    return out

def haar_stream(N):
    for _ in range(N):
        yield geom()

def orbit_letters(x, q, r, maxsteps, cycleset):
    S = 0
    for k in range(maxsteps):
        y = q * x + r
        a = (y & -y).bit_length() - 1
        y >>= a
        x = y
        yield a
        if x in cycleset:
            return

CYC = {"A": {1}, "B": {1, 5, 7, 17, 25, 37, 55, 41, 61, 91}, "C": {1, 3, 13, 33, 83, 17, 43, 27}}

def main():
    print("=" * 78)
    print("O5a  Haar reference (exact LIL target: limsup = +1, liminf = -1)")
    print("=" * 78)
    lil_scan(haar_stream(10 ** 7), f"Haar word, seed {SEED}")

    print()
    print("=" * 78)
    print("O5b  integer orbits of A and B: how long is an orbit, actually?")
    print("=" * 78)
    for M, (q, r) in (("A", (3, 1)), ("B", (3, -1))):
        lens = []
        random.seed(SEED)
        for _ in range(20000):
            x = random.randrange(1, 10 ** 12, 2)
            n = sum(1 for _ in orbit_letters(x, q, r, 100000, CYC[M]))
            lens.append(n)
        lens.sort()
        mx = lens[-1]
        print(f"  {M}: seeds < 10^12, orbit length to capture: mean {sum(lens)/len(lens):.2f}, "
              f"median {lens[len(lens)//2]}, max {mx}")
        print(f"     at n = {mx}:  ln ln n = {log(log(mx)):.4f},  sqrt(4 n lnln n) = "
              f"{sqrt(4*mx*log(log(mx))):.2f}  -- the LIL normalizer is barely defined")

    print()
    print("=" * 78)
    print("O5c  integer orbits of C (exact big-integer arithmetic, 20000 steps)")
    print("=" * 78)
    random.seed(SEED)
    his, los = [], []
    for t in range(200):
        x = random.randrange(1, 10 ** 9, 2)
        S = 0
        hi, lo = -1e18, 1e18
        for n, a in enumerate(orbit_letters(x, 5, 1, 20000, CYC["C"]), start=1):
            S += a
            if n >= 100:
                d = sqrt(4.0 * n * log(log(n)))
                z = (S - 2.0 * n) / d
                hi = max(hi, z); lo = min(lo, z)
        his.append(hi); los.append(lo)
    his.sort(); los.sort()
    print(f"  200 seeds < 10^9, 20000 steps each (envelope accumulated from n>=100; ln ln 20000 = {log(log(20000)):.4f})")
    print(f"    running max of (S_n-2n)/sqrt(4n lnln n): median {his[100]:+.6f}, "
          f"max {his[-1]:+.6f}")
    print(f"    running min                            : median {los[100]:+.6f}, "
          f"min {los[0]:+.6f}")
    print("  (a single Haar word of the same length, for comparison:)")
    random.seed(SEED + 1)
    lil_scan(haar_stream(20000), "Haar, 20000 letters", report_at=(20000,))

if __name__ == "__main__":
    main()
