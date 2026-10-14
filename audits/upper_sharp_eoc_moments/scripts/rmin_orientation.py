#!/usr/bin/env python3
"""rmin_orientation.py  --  [V] exact r_min(N,0) well past the audit depths, for orientation.

Not part of any gate.  Reported because the audit's own depths (N <= 20) turn out to sit entirely
inside the r_min = 27 plateau, so they cannot discriminate between exponents c at all; this table
shows where the plateau ends and what the true exponent looks like beyond it.

r_min(N,0) = the least odd m that is zero-confined for N steps (Descent.ConfinedUpTo), by direct
ascending orbit scan with the actual accelerated map.  Exact integers.

Usage:  python3 rmin_orientation.py [--quick]
"""

import sys
import math

import zn


def conf_depth(m, cap):
    """Largest j <= cap with 2^{s_i} <= 3^i for every i <= j."""
    x, s = m, 0
    for j in range(cap):
        y = 3 * x + 1
        a = zn.v2(y)
        x = y >> a
        s += a
        if (1 << s) > 3 ** (j + 1):
            return j
    return cap


def main(quick=False):
    nmax = 40 if quick else 70
    print("=" * 76)
    print("Exact r_min(N,0) and the plateaux   [V]")
    print("=" * 76)

    print("\n[1] zero-confinement depth of the small record holders  (exact [V])")
    print("%8s %18s" % ("m", "confinement depth"))
    for m in (3, 7, 27, 703, 10087):
        print("%8d %18d" % (m, conf_depth(m, 400)))

    print("\n[2] r_min(N,0) for N = 1..%d, printed one row per plateau  (exact [V])" % nmax)
    print("%12s %12s %12s %14s %12s" % ("N range", "r_min", "log2 r_min", "log2 r_min/N", "A[N]+1"))
    prev, start = None, None
    rows = []
    for N in range(1, nmax + 1):
        r = zn.rmin_direct(N)
        if r != prev:
            if prev is not None:
                rows.append((start, N - 1, prev))
            prev, start = r, N
    rows.append((start, nmax, prev))
    for (a, b, r) in rows:
        rng = "%d" % a if a == b else "%d-%d" % (a, b)
        print("%12s %12d %12.4f %14.4f %12d"
              % (rng, r, math.log2(r), math.log2(r) / b, zn.A(b) + 1))

    print("\n[3] reading  [V] for the range printed, no asymptotics")
    print("    The audit depths N = 8..20 lie entirely inside the r_min = 27 plateau, so at those")
    print("    depths r_min(N,0) <= 2^{cN} holds for every c >= %.4f and the finite data cannot"
          % (math.log2(27) / 20))
    print("    discriminate between candidate exponents.  What the audit can measure is the LOSS")
    print("    of each method, not the truth.  Compare the c_k ladder: c_2 = 0.8321,")
    print("    c_4 = 0.5812, c_6 = 0.4557, I_0 = 0.0793.")
    return 0


if __name__ == "__main__":
    sys.exit(main(quick="--quick" in sys.argv))
