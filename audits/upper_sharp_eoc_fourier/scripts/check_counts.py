#!/usr/bin/env python3
"""check_counts.py  --  [V] exact counts of zero-confined positive valuation words.

Status label: [V]  (verified by exact integer computation, for the stated finite range only)

Conventions (see ../README.md for the Lean sources in this repository):
  word         d = (d_0, ..., d_{N-1}), every d_j >= 1
  prefix sum   s_j = d_0 + ... + d_{j-1}          (Occupation.psum)
  terminal sum S   = s_N
  0-confined   2^{s_j} <= 3^j for every j <= N    (Descent.ConfinedUpTo / Occupation.Confined 0)
  A[k]         = floor(k log2 3) = (3**k).bit_length() - 1   (Occupation.sN)

Every assertion below is decided by exact integer arithmetic.  No floats are used.
Exits non-zero on any failed assertion.  Writes nothing; prints to stdout only.

Usage:  python3 check_counts.py [--quick]
"""

import sys

# ---------------------------------------------------------------- primitives

def A(k):
    """floor(k * log2 3), by bit length of 3^k.  Exact integer route."""
    return (3 ** k).bit_length() - 1


def confined_step(s_j, j):
    """Exact 0-confinement test at index j:  2^{s_j} <= 3^j."""
    return 2 ** s_j <= 3 ** j


def shell_table(N):
    """f[S] = number of 0-confined positive words of length N with terminal sum S.

    Forward DP on (j, s_j).  Confinement caps s_{j+1} at A[j+1], so the state
    space is finite and the recursion is exact.
    """
    f = {0: 1}
    for j in range(N):
        g = {}
        cap = A(j + 1)
        for s, c in f.items():
            for d in range(1, cap - s + 1):
                s2 = s + d
                assert confined_step(s2, j + 1), (N, j, s2)
                g[s2] = g.get(s2, 0) + c
        f = g
    return f


def brute_count(N):
    """Independent route: enumerate the words directly (no DP).  Small N only."""
    total = 0
    w = [0] * N

    def rec(j, s):
        nonlocal total
        if j == N:
            total += 1
            return
        for d in range(1, A(j + 1) - s + 1):
            w[j] = d
            rec(j + 1, s + d)

    rec(0, 0)
    return total


# ---------------------------------------------------------------- the checks

EXPECTED_TOTAL = {
    15: 108950,
    20: 13472296,
    25: 1899474678,
    30: 248369601964,
}


def main(quick=False):
    fail = []

    print("=" * 78)
    print("check_counts.py  --  [V] zero-confined positive word counts")
    print("=" * 78)

    # ---- 0. A[k] is characterised exactly -------------------------------
    print("\n[0] A[k] = floor(k log2 3) via bit length, characterised exactly")
    kmax = 25 if quick else 40
    for k in range(kmax + 1):
        assert 2 ** A(k) <= 3 ** k < 2 ** (A(k) + 1), k
    print("    2^A[k] <= 3^k < 2^(A[k]+1) verified for k = 0..%d" % kmax)
    print("    A[k], k=0..30: %s" % [A(k) for k in range(31)])

    # ---- 1. DP vs direct word enumeration -------------------------------
    print("\n[1] counting DP cross-checked against direct word enumeration")
    for N in range(1, 13):
        dp = sum(shell_table(N).values())
        bf = brute_count(N)
        ok = dp == bf
        if not ok:
            fail.append("N=%d DP=%d enum=%d" % (N, dp, bf))
        print("    N=%2d  DP=%8d  enum=%8d  %s" % (N, dp, bf, "ok" if ok else "MISMATCH"))

    # ---- 2. total counts against the recorded reference values ----------
    print("\n[2] total zero-confined positive words of length N (all terminal sums)")
    print("    %3s %20s %20s" % ("N", "computed", "reference"))
    targets = [15, 20] if quick else [15, 20, 25, 30]
    for N in targets:
        got = sum(shell_table(N).values())
        exp = EXPECTED_TOTAL[N]
        ok = got == exp
        if not ok:
            fail.append("total N=%d computed=%d reference=%d" % (N, got, exp))
        print("    %3d %20d %20d  %s" % (N, got, exp, "ok" if ok else "MISMATCH"))
    if quick:
        print("    (--quick: N=25,30 skipped)")

    # ---- 3. terminal-shell sizes M_N ------------------------------------
    print("\n[3] terminal-shell size M_N = |W_0(N)| at S = A[N]   (Q = 2^(S+1))")
    print("    %3s %4s %10s %18s %12s" % ("N", "S", "Q", "M_N", "M_N/total"))
    shells = [12, 14, 15, 16, 20] if quick else [12, 14, 15, 16, 20, 25, 30]
    MN = {}
    for N in shells:
        t = shell_table(N)
        S = A(N)
        M = t.get(S, 0)
        MN[N] = (S, M)
        assert M > 0, N
        print("    %3d %4d %10s %18d %12.4f"
              % (N, S, "2^%d" % (S + 1), M, M / sum(t.values())))
    if quick:
        print("    (--quick: N=25,30 skipped)")

    # ---- 4. the shell is the top shell, and it is nonempty --------------
    print("\n[4] S = A[N] is the largest attainable terminal sum")
    for N in shells:
        t = shell_table(N)
        assert max(t) == A(N), (N, max(t), A(N))
    print("    max attainable terminal sum == A[N] for N in %s" % shells)

    print("\n" + "=" * 78)
    if fail:
        print("FAILED (%d):" % len(fail))
        for f in fail:
            print("  - " + f)
        return 1
    print("all exact checks passed   [V] for the finite ranges printed above")
    return 0


if __name__ == "__main__":
    sys.exit(main(quick="--quick" in sys.argv))
