#!/usr/bin/env python3
"""check_zn.py  --  [V] the preregistered validation of the Z_N machinery.

Everything here is required to pass by ../PREREGISTRATION.md sections 0b, 1b and 4 before any
gate is read.  Exact integer arithmetic except section 6 (Fourier, complex128, [F]).

  (1) the lift weighting identity  sum_S |W(N,S)| 2^{A[N]-S} == #{odd m < Q : confined N steps},
      against an independent brute orbit scan, at N = 8, 10, 12, 14,
      with the reference counts 367 / 2114 / 27328 / 168807;
  (2) Z_N as built == the brute-scan set, ELEMENTWISE, same depths; all elements odd, distinct, < Q;
  (3) min Z_N == r_min(N,0) from an independent direct ascending orbit scan;
  (4) window_hist: exact all-shift histogram against a brute all-y computation at N = 8, 10,
      and its invariants sum(counts) == Q, sum(values*counts) == M*H at every depth;
  (5) pair_stats: P_ordered against brute O(M^2) at the depths where M <= 2500, and the
      exact identity  sum_y X_y^2 == M*H + sum_{m!=m'} (H-d)_+  at every depth;
  (6) [F] the word-level Fourier DP against direct exponential sums over Z_N, N = 8, 10,
      all h <= 512 plus h = Q/8, Q/4, Q/2; preregistered tolerance 1e-9;
  (7) the shell-support structure: for ODD h, F(h) comes from the terminal shell S = A[N] alone.

Usage:  python3 check_zn.py [--quick]        exits non-zero on any failed assertion
"""

import sys
import numpy as np
from fractions import Fraction

import zn

REFERENCE = {8: 367, 10: 2114, 12: 27328, 14: 168807}


def main(quick=False):
    fail = []
    depths = [8, 10, 12] if quick else [8, 10, 12, 14]
    allN = list(range(8, 15)) if not quick else list(range(8, 13))

    print("=" * 78)
    print("check_zn.py  --  [V] validation of the Z_N construction and the exact window machinery")
    print("=" * 78)

    print("\n[1] lift weighting identity vs independent brute orbit scan")
    print("    sum_S |W(N,S)| * 2^(A[N]-S)  ==  #{odd m < 2^(A[N]+1) : 0-confined N steps}")
    print("    %3s %6s %14s %14s %14s" % ("N", "A[N]", "weighted", "brute", "reference"))
    Zcache = {}
    for N in depths:
        Z, Q, AN = zn.build_Z(N)
        Zcache[N] = (Z, Q, AN)
        B, QB = zn.brute_Z(N)
        w = zn.M_from_words(N)
        ref = REFERENCE[N]
        ok = (w == B.size == ref == Z.size) and QB == Q
        if not ok:
            fail.append("weighting N=%d weighted=%d brute=%d ref=%d built=%d" % (N, w, B.size, ref, Z.size))
        print("    %3d %6d %14d %14d %14d  %s" % (N, AN, w, B.size, ref, "ok" if ok else "MISMATCH"))

        # (2) elementwise
        same = bool(np.array_equal(Z, B))
        odd = bool(np.all(Z % 2 == 1))
        distinct = bool(np.all(np.diff(Z) > 0))
        inrange = bool(Z[0] >= 0 and Z[-1] < Q)
        if not (same and odd and distinct and inrange):
            fail.append("elementwise N=%d same=%s odd=%s distinct=%s inrange=%s"
                        % (N, same, odd, distinct, inrange))
        print("        elementwise equal=%s  all odd=%s  distinct=%s  all < Q=%s"
              % (same, odd, distinct, inrange))

    print("\n[2] min Z_N == r_min(N,0) by independent direct ascending orbit scan")
    print("    %3s %12s %12s %10s" % ("N", "min Z_N", "direct scan", "log2/N"))
    import math
    for N in depths:
        Z, Q, AN = Zcache[N]
        rd = zn.rmin_direct(N)
        ok = int(Z[0]) == rd
        if not ok:
            fail.append("rmin N=%d minZ=%d direct=%s" % (N, int(Z[0]), rd))
        print("    %3d %12d %12s %10.4f  %s"
              % (N, int(Z[0]), rd, math.log2(int(Z[0])) / N, "ok" if ok else "MISMATCH"))

    print("\n[3] window_hist: exact all-shift histogram vs brute all-y, and its invariants")
    print("    %3s %5s %10s %10s %12s %12s" % ("N", "H", "segments", "brute ok", "sum counts", "sum v*c"))
    for N in depths:
        Z, Q, AN = Zcache[N]
        M = Z.size
        for H in (1 << 4, 1 << 6):
            if H > Q // 2:
                continue
            vals, cnts = zn.window_hist(Z, Q, H)
            inv1 = int(cnts.sum()) == Q
            inv2 = int((vals * cnts).sum()) == M * H
            brute_ok = "skipped"
            if Q <= 1 << 20:
                ind = np.zeros(Q, dtype=np.int64)
                ind[Z] = 1
                cum = np.concatenate([[0], np.cumsum(np.concatenate([ind, ind]))])
                X = cum[np.arange(Q) + H] - cum[np.arange(Q)]
                bv, bc = np.unique(X, return_counts=True)
                brute_ok = str(bool(np.array_equal(vals, bv) and np.array_equal(cnts, bc)))
                if brute_ok != "True":
                    fail.append("window_hist N=%d H=%d disagrees with brute" % (N, H))
            if not (inv1 and inv2):
                fail.append("window_hist invariants N=%d H=%d" % (N, H))
            print("    %3d %5d %10d %10s %12d %12d" % (N, H, vals.size, brute_ok, int(cnts.sum()),
                                                       int((vals * cnts).sum())))

    print("\n[4] pair_stats vs brute, and the exact identity sum_y X_y^2 == M*H + sum_{m!=m'}(H-d)_+")
    print("    %3s %6s %14s %14s %16s %16s" % ("N", "H", "P_ordered", "P brute", "sum X^2", "M*H+weighted"))
    for N in allN:
        if N in Zcache:
            Z, Q, AN = Zcache[N]
        else:
            Z, Q, AN = zn.build_Z(N)
            Zcache[N] = (Z, Q, AN)
        M = Z.size
        for H in (1 << 5,):
            P, w = zn.pair_stats(Z, Q, H)
            vals, cnts = zn.window_hist(Z, Q, H)
            sumX2 = int((vals.astype(object) ** 2 * cnts.astype(object)).sum())
            idok = sumX2 == M * H + w
            if not idok:
                fail.append("pair identity N=%d H=%d sumX2=%d rhs=%d" % (N, H, sumX2, M * H + w))
            pb = "skipped"
            if M <= 2500:       # the brute O(M^2) difference matrix is the memory ceiling here
                d = (Z[:, None] - Z[None, :]) % Q
                dd = np.minimum(d, Q - d)
                np.fill_diagonal(dd, Q)
                pb = int((dd < H).sum())
                if pb != P:
                    fail.append("pair count N=%d H=%d dp=%d brute=%d" % (N, H, P, pb))
            print("    %3d %6d %14d %14s %16d %16d  %s"
                  % (N, H, P, pb, sumX2, M * H + w, "ok" if idok else "MISMATCH"))

    print("\n[5] [F] word-level Fourier DP vs direct exponential sums over Z_N (tolerance 1e-9)")
    print("    %3s %10s %14s %14s" % ("N", "#freqs", "max |dev|", "verdict"))
    for N in (8, 10):
        Z, Q, AN = Zcache[N]
        M = Z.size
        hs = list(range(1, 513)) + [Q // 8, Q // 4, Q // 2]
        a = zn.F_batch(N, hs, M)
        b = zn.F_brute(Z, Q, hs)
        dev = float(np.abs(a - b).max())
        ok = dev < 1e-9
        if not ok:
            fail.append("Fourier DP N=%d dev=%.3e" % (N, dev))
        print("    %3d %10d %14.3e %14s" % (N, len(hs), dev, "ok" if ok else "TOO LARGE"))

    print("\n[6] shell support: for ODD h, F(h) comes from the terminal shell S = A[N] alone")
    print("    compared against the direct sum over Z_N, 128 odd h (tolerance 1e-9)")
    print("    %3s %14s %14s %12s" % ("N", "max |dev|", "M_shell/M", "verdict"))
    for N in (8, 10, 12):
        Z, Q, AN = Zcache[N]
        M = Z.size
        tab = zn.shell_table(N)
        hs = np.arange(1, 256, 2, dtype=np.int64)
        # terminal-shell-only transform, by brute force over shell words
        mS = 1 << (AN + 1)
        assert mS == Q
        shell_res = []
        stack = [(0, 0, 0)]
        inv3 = [pow(pow(3, j, Q), -1, Q) for j in range(N + 2)]
        while stack:
            j, s, acc = stack.pop()
            if j == N:
                if s == AN:
                    shell_res.append((pow(2, s, Q) - acc) % (1 << (s + 1)))
                continue
            term = (acc + inv3[j + 1] * (1 << s)) % Q
            for d in range(1, zn.A(j + 1) - s + 1):
                stack.append((j + 1, s + d, term))
        R = np.array(shell_res, dtype=np.int64)
        assert R.size == tab[AN]
        direct = zn.F_brute(Z, Q, hs)
        shell = np.array([np.exp(2j * np.pi * (((R * h) % Q).astype(np.float64) / Q)).sum() / M
                          for h in hs.tolist()])
        dev = float(np.abs(direct - shell).max())
        ok = dev < 1e-9
        if not ok:
            fail.append("shell support N=%d dev=%.3e" % (N, dev))
        print("    %3d %14.3e %14.6f %12s" % (N, dev, R.size / M, "ok" if ok else "MISMATCH"))

    print("\n" + "=" * 78)
    if fail:
        print("FAILED (%d):" % len(fail))
        for f in fail:
            print("  - " + f)
        return 1
    print("all checks passed   [V] for the finite ranges printed above ([F] for sections 5-6)")
    return 0


if __name__ == "__main__":
    sys.exit(main(quick="--quick" in sys.argv))
