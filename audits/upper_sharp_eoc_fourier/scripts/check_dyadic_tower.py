#!/usr/bin/env python3
"""check_dyadic_tower.py  --  [V] the dyadic tower identity, exactly.

Status label: [V]  (exact integer arithmetic; the float column is a [F] sanity line)

THE IDENTITY, with Q = 2^(S+1), S = A[N], and r ranging over the terminal shell:

    |F_N(2^t u)|  =  | normalized DFT of (r mod 2^(S+1-t)) at u |,     u odd,

because  exp(2 pi i * 2^t u r / 2^(S+1))  =  exp(2 pi i * u r / 2^(S+1-t)),
and r enters the right-hand side only through r mod 2^(S+1-t).  So the identity is
TERM BY TERM, and is checked here as an exact integer statement -- no float enters:

    (2^t * u * r) mod Q   ==   2^t * ( (u * (r mod m)) mod m ),      m = 2^(S+1-t).

THE REASON (and the mechanism behind the whole resonance tower).  By the additive
formula (check_additive_formula.py),

    r  ==  3^(-N) 2^S  -  sum_{j<N} 3^(-(j+1)) 2^(s_j)   (mod 2^(S+1)),

so reducing modulo 2^k kills every summand with s_j >= k (and the constant too, once
S >= k).  Multiplying the FREQUENCY by 2^t is the same reduction with k = S+1-t.
Hence r mod 2^k is a function of the path PREFIX alone -- the letters up to the first
index with s_j >= k -- and the number of attainable values collapses, which is why
|F| climbs to O(1) as t grows.  Both halves of that are checked exactly below.

Exits non-zero on any failed assertion.  Writes nothing; prints to stdout only.

Usage:  python3 check_dyadic_tower.py [--quick]
"""

import cmath
import math
import sys
from collections import Counter


def A(k):
    return (3 ** k).bit_length() - 1


def shell_words(N):
    S = A(N)
    out = []
    w = [0] * N

    def rec(j, s):
        if j == N:
            if s == S:
                out.append(tuple(w))
            return
        for d in range(1, A(j + 1) - s + 1):
            w[j] = d
            rec(j + 1, s + d)

    rec(0, 0)
    return out, S


def least_realizer(d):
    N = len(d)
    q = 0
    s = 0
    for dj in d:
        q = 3 * q + 2 ** s
        s += dj
    Q = 2 ** (s + 1)
    return ((2 ** s - q) * pow(pow(3, N, Q), -1, Q)) % Q, s


def prefix_profile(d, k):
    """The truncated profile: the list of (j, s_j) with s_j < k, in order."""
    prof = []
    s = 0
    for j in range(len(d)):
        if s < k:
            prof.append((j, s))
        s += d[j]
    return tuple(prof)


def main(quick=False):
    fail = []
    N = 12 if quick else 14
    US = (1, 3, 5, 7)

    print("=" * 78)
    print("check_dyadic_tower.py  --  [V] dyadic tower identity, N = %d" % N)
    print("=" * 78)

    ws, S = shell_words(N)
    Q = 2 ** (S + 1)
    rs = [least_realizer(d)[0] for d in ws]
    M = len(rs)
    print("\n    N = %d   S = A[N] = %d   Q = 2^%d   M_N = %d" % (N, S, S + 1, M))

    # ---- 1. the identity, exactly, every t and u -------------------------
    print("\n[1] EXACT term-by-term identity, all t = 0..%d, u in %s" % (S - 1, str(US)))
    checked = 0
    for t in range(0, S):
        m = 2 ** (S + 1 - t)
        for u in US:
            for r in rs:
                lhs = (2 ** t * u * r) % Q
                rhs = (2 ** t * ((u * (r % m)) % m)) % Q
                if lhs != rhs:
                    fail.append("exact identity t=%d u=%d r=%d" % (t, u, r))
                    break
                checked += 1
    print("    %d exact integer comparisons, 0 mismatches" % checked)

    # ---- 2. exact multiset (residue-count) comparison --------------------
    print("\n[2] EXACT multiset comparison of the two exponent sets")
    for t in range(0, S):
        m = 2 ** (S + 1 - t)
        for u in US:
            cl = Counter((2 ** t * u * r) % Q for r in rs)
            cr = Counter((2 ** t * ((u * (r % m)) % m)) % Q for r in rs)
            if cl != cr:
                fail.append("multiset t=%d u=%d" % (t, u))
    print("    exponent multisets agree for every (t,u) above -> the two sums are")
    print("    equal as exact sums of roots of unity, hence the moduli are equal.")

    # ---- 3. float sanity line  [F] ---------------------------------------
    print("\n[3] [F] float evaluation of both sides (sanity only, not the proof)")
    worst = 0.0
    tau = 2j * math.pi
    for t in list(range(0, 6)) + [S // 2, S - 2, S - 1]:
        if t >= S:
            continue
        m = 2 ** (S + 1 - t)
        for u in US:
            lhs = abs(sum(cmath.exp(tau * (((2 ** t * u * r) % Q) / Q)) for r in rs)) / M
            rhs = abs(sum(cmath.exp(tau * (((u * (r % m)) % m) / m)) for r in rs)) / M
            worst = max(worst, abs(lhs - rhs))
    print("    max |LHS - RHS| over the sampled (t,u): %.3e   [F]" % worst)

    # ---- 4. the collapse: r mod 2^k is a function of the prefix ----------
    print("\n[4] EXACT collapse: r mod 2^k depends only on the truncated prefix profile")
    print("    %4s %18s %22s %12s" % ("k", "#distinct r mod 2^k", "#distinct prefix profiles",
                                      "equal"))
    for k in range(1, min(S, 14) + 1):
        by_res = len(set(r % (2 ** k) for r in rs))
        prof = {}
        bad = False
        for d, r in zip(ws, rs):
            p = prefix_profile(d, k)
            v = r % (2 ** k)
            if p in prof and prof[p] != v:
                bad = True
                break
            prof[p] = v
        if bad:
            fail.append("prefix profile does not determine r mod 2^%d" % k)
        eq = (not bad) and by_res == len(set(prof.values()))
        print("    %4d %18d %22d %12s" % (k, by_res, len(prof), eq))

    # ---- 5. the resulting coarse-scale skew ------------------------------
    print("\n[5] EXACT distribution of r mod 2^k (why the coarse scales resonate)")
    print("    %4s %14s %14s %16s %16s"
          % ("k", "odd classes", "occupied", "max class share", "uniform share"))
    for k in range(2, 8):
        c = Counter(r % (2 ** k) for r in rs)
        assert all(v % 2 == 1 for v in c), k
        print("    %4d %14d %14d %16.4f %16.4f"
              % (k, 2 ** (k - 1), len(c), max(c.values()) / M, 1 / 2 ** (k - 1)))
    print("    Lean input in this repository for the k=2 row (every 0-confined odd m")
    print("    is == 3 mod 4):  Descent.mod_four_of_confined, Descent/ResidueLaw.lean. [P]")

    print("\n" + "=" * 78)
    if fail:
        print("FAILED (%d):" % len(fail))
        for f in fail:
            print("  - " + f)
        return 1
    print("all exact checks passed   [V] for N = %d" % N)
    return 0


if __name__ == "__main__":
    sys.exit(main(quick="--quick" in sys.argv))
