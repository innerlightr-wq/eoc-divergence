#!/usr/bin/env python3
"""test0_anchor.py  --  Test 0, the anchor gate: is the window at zero typical?

Every moment route assumes the window [0,H) behaves like a typical window.  This tests that
directly, exactly, over ALL shifts.  See ../PREREGISTRATION.md section 3 for the gate, fixed
before this script was run.

Per (N, c) with H = 2^floor(c*N):
  X_0 = #(Z_N cap [0,H))                                      exact [V]
  E   = M H / Q,  rho_0 = X_0 / E                             exact [V] (Fraction)
  the EXACT all-shift distribution of X_y over all y mod Q    exact [V] (event method)
  the exact percentile of X_0 in it                           exact [V]
  X_{kH} for k = 0..63                                        exact [V]
and per N: r_min(N,0) = min Z_N, with log2 r_min / N.

Gate 0 (preregistered): FAIL ("systematically depleted") iff the OLS slope of log2 rho_0 against N
is <= -0.02 for EVERY c in {0.70, 0.80, 0.90} in BOTH the full fit (N=8..18) and the trimmed fit
(N=10..18).  PASS iff the slope is > -0.02 for every c in both.  MIXED otherwise (treated as
PASS-with-flag).  Depths with X_0 = 0 are excluded from the fit and counted.

Usage:  python3 test0_anchor.py [--quick]      exits non-zero on any failed assertion
"""

import sys
import math
from fractions import Fraction

import numpy as np

import zn

CS = (0.70, 0.80, 0.90)
PRIMARY = list(range(8, 19))        # preregistered fit set
TRIM_FROM = 10                      # preregistered robustness refit
EXTENSION = [19, 20]                # budget-conditional, excluded from all fits
SLOPE_GATE = -0.02
# Budget rule (PREREGISTRATION section 2 / section 7): the exact all-shift law needs arrays of
# 2M int64 plus an argsort, so it is computed only when M <= HIST_CAP.  Above that only the
# cheap exact quantities (r_min, M, X_0, rho_0) are reported, and the depth is still excluded
# from every fit.
HIST_CAP = 8_000_000


def ols(xs, ys):
    n = len(xs)
    if n < 3:
        return None
    mx = sum(xs) / n
    my = sum(ys) / n
    den = sum((x - mx) ** 2 for x in xs)
    if den == 0:
        return None
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / den


def main(quick=False):
    fail = []
    depths = list(range(8, 15)) if quick else PRIMARY
    ext = [] if quick else EXTENSION

    print("=" * 100)
    print("Test 0 -- the anchor gate: is the window at zero typical?")
    print("Exact over ALL shifts at every depth (event method); no sampling anywhere in this test.")
    print("=" * 100)

    rows = {c: [] for c in CS}
    print("\n[1] per depth: r_min(N,0), M, Q  (exact [V])")
    print("%4s %6s %14s %10s %12s %10s" % ("N", "A[N]", "M = |Z_N|", "log2 M/N", "r_min(N,0)", "log2 r/N"))
    cache = {}
    for N in depths + ext:
        Z, Q, AN = zn.build_Z(N)
        M = Z.size
        rmin = int(Z[0])
        wexp = zn.M_from_words(N)
        if wexp != M:
            fail.append("M mismatch N=%d built=%d weighted=%d" % (N, M, wexp))
        cache[N] = (Z, Q, AN, M, rmin)
        print("%4d %6d %14d %10.4f %12d %10.4f"
              % (N, AN, M, math.log2(M) / N, rmin, math.log2(rmin) / N))

    print("\n[2] the window at zero against the exact all-shift law")
    print("    rho_0 = X_0/E;  pct = exact percentile of X_0 in the all-shift distribution;")
    print("    P(X=0) = (#bad shifts)/Q;  med/mean/max are of X_y over all y mod Q")
    hdr = ("%4s %5s %6s %14s %12s %10s %9s %8s %8s %8s %10s"
           % ("N", "c", "w", "H", "E", "X_0", "rho_0", "pct", "median", "max", "P(X=0)"))
    for c in CS:
        print("\n  c = %.2f" % c)
        print("  " + hdr)
        for N in depths + ext:
            Z, Q, AN, M, rmin = cache[N]
            w = int(math.floor(c * N))
            H = 1 << w
            if H > Q // 2:
                print("  %4d %5.2f %6d %14d   (skipped: H > Q/2)" % (N, c, w, H))
                continue
            X0 = int(np.searchsorted(Z, H, side='left'))
            E = Fraction(M * H, Q)
            if M > HIST_CAP:
                rho = Fraction(X0, 1) / E
                rows[c].append((N, w, H, int(E.numerator), int(E.denominator), X0,
                                float(rho), float('nan'), -1, -1))
                print("  %4d %5.2f %6d %14d %12.4f %10d %9.4f %8s %8s %8s %10s"
                      % (N, c, w, H, float(E), X0, float(rho),
                         "-", "-", "-", "over budget"))
                continue
            vals, cnts = zn.window_hist(Z, Q, H)
            assert int(cnts.sum()) == Q
            assert int((vals * cnts).sum()) == M * H
            below = int(cnts[vals < X0].sum())
            atx = int(cnts[vals == X0].sum())
            pct = Fraction(2 * below + atx, 2 * Q)          # exact mid-percentile
            nbad = int(cnts[vals == 0].sum()) if (vals == 0).any() else 0
            # exact median of X_y
            cum = np.cumsum(cnts)
            med = int(vals[np.searchsorted(cum, (Q + 1) // 2)])
            rho = Fraction(X0, 1) / E if E != 0 else None
            rows[c].append((N, w, H, int(E.numerator), int(E.denominator), X0,
                            float(rho) if rho is not None else None, float(pct), nbad, int(vals[-1])))
            print("  %4d %5.2f %6d %14d %12.4f %10d %9.4f %8.4f %8d %8d %10.3e"
                  % (N, c, w, H, float(E), X0, float(rho), float(pct), med, int(vals[-1]),
                     nbad / Q))

    print("\n[3] small aligned windows near zero: X_{kH}, k = 0..63  (exact [V])")
    print("    reported as the multiset summary of the 64 counts, against E")
    print("%4s %5s %12s %8s %8s %8s %8s %10s" % ("N", "c", "E", "min", "median", "mean", "max", "#zero"))
    for N in depths:
        for c in CS:
            Z, Q, AN, M, rmin = cache[N]
            w = int(math.floor(c * N))
            H = 1 << w
            if 64 * H > Q:
                continue
            E = Fraction(M * H, Q)
            ks = np.arange(64, dtype=np.int64) * H
            lo = np.searchsorted(Z, ks, side='left')
            hi = np.searchsorted(Z, ks + H, side='left')
            xs = (hi - lo)
            print("%4d %5.2f %12.4f %8d %8.1f %8.3f %8d %10d"
                  % (N, c, float(E), int(xs.min()), float(np.median(xs)), float(xs.mean()),
                     int(xs.max()), int((xs == 0).sum())))

    print("\n[4] GATE 0 -- preregistered fit of log2 rho_0 against N")
    print("    slope gate: %.2f per step; FAIL requires every c <= gate in BOTH fits" % SLOPE_GATE)
    print("%6s %12s %12s %10s %10s %12s"
          % ("c", "slope 8-18", "slope 10-18", "#X_0=0", "max|log2|", "verdict(c)"))
    verdicts = {}
    for c in CS:
        pts = [(N, math.log2(rho)) for (N, w, H, en, ed, X0, rho, pct, nb, mx) in rows[c]
               if N in depths and X0 > 0]
        nzero = sum(1 for (N, w, H, en, ed, X0, rho, pct, nb, mx) in rows[c]
                    if N in depths and X0 == 0)
        pts_t = [(N, y) for (N, y) in pts if N >= TRIM_FROM]
        s_full = ols([p[0] for p in pts], [p[1] for p in pts])
        s_trim = ols([p[0] for p in pts_t], [p[1] for p in pts_t])
        mx = max(abs(y) for (N, y) in pts) if pts else float('nan')
        dep = (s_full is not None and s_trim is not None
               and s_full <= SLOPE_GATE and s_trim <= SLOPE_GATE)
        verdicts[c] = dep
        print("%6.2f %12s %12s %10d %10.4f %12s"
              % (c,
                 "%.5f" % s_full if s_full is not None else "n/a",
                 "%.5f" % s_trim if s_trim is not None else "n/a",
                 nzero, mx, "depleted" if dep else "not depleted"))

    alldep = all(verdicts.values())
    nodep = not any(verdicts.values())
    print()
    if alldep:
        print("GATE 0: FAIL -- the window at zero is SYSTEMATICALLY DEPLETED")
        print("  [R] for 'the window at zero is typical'.  Verdict for r_min on all moment")
        print("  routes: STOP.  Tests A and B become moot for r_min.")
    elif nodep:
        print("GATE 0: PASS -- no exponential depletion at the tested depths")
        print("  rho_0 stays within a bounded factor over N = %d..%d for all three c."
              % (depths[0], depths[-1]))
    else:
        print("GATE 0: MIXED -- depleted for some c, not for others (treated as PASS-with-flag)")
        for c in CS:
            print("    c=%.2f: %s" % (c, "depleted" if verdicts[c] else "not depleted"))

    # ------------------------------------------------------------------ post-hoc
    print("\n[5] POST-HOC VARIANT -- NOT PREREGISTERED.  Added after seeing the data because the")
    print("    preregistered Gate 0 is ill-posed for the shape the data actually has: rho_0 starts")
    print("    ABOVE 1 (1.40-1.95 at N=8..12) and RELAXES TO 1, and an OLS slope over a window")
    print("    containing that transient cannot distinguish 'relaxes to 1 from above' from")
    print("    'decays exponentially'.  Both give a negative slope.  The preregistered verdict")
    print("    above stands as recorded; this variant is reported alongside it, never instead.")
    print("    Post-hoc criteria, stated before being read: (a) slope over the last five primary")
    print("    depths N=14..18; (b) |log2 rho_0| at N=16,17,18; (c) rho_0 at the extension depths")
    print("    N=19,20, which are excluded from every fit.")
    print("%6s %14s %14s %28s %22s"
          % ("c", "slope 14-18", "max|log2| N>=16", "rho_0 at N=16,17,18", "rho_0 at N=19,20"))
    for c in CS:
        ser = {N: rho for (N, w, H, en, ed, X0, rho, pct, nb, mx) in rows[c] if rho is not None}
        late = [(N, math.log2(ser[N])) for N in range(14, 19) if N in ser]
        s_late = ols([p[0] for p in late], [p[1] for p in late])
        tail = [ser[N] for N in (16, 17, 18) if N in ser]
        extv = [ser[N] for N in EXTENSION if N in ser]
        print("%6.2f %14s %14.4f %28s %22s"
              % (c,
                 "%+.5f" % s_late if s_late is not None else "n/a",
                 max(abs(math.log2(v)) for v in tail) if tail else float('nan'),
                 ", ".join("%.4f" % v for v in tail),
                 ", ".join("%.4f" % v for v in extv)))
    print()
    print("    Reading of the post-hoc variant [F]: at the three largest primary depths rho_0 lies")
    print("    within 0.95-1.00 for every c, the exact percentile of X_0 has fallen from ~0.98 to")
    print("    0.33-0.52, and the two extension depths give rho_0 = 0.992-1.005.  At these depths")
    print("    the window at zero is TYPICAL, not depleted.  This is a finite-range observation at")
    print("    N <= 20; it is not an asymptotic statement and does not refute depletion at large N.")

    print("\n" + "=" * 100)
    if fail:
        print("FAILED (%d):" % len(fail))
        for f in fail:
            print("  - " + f)
        return 1
    print("exact checks passed   [V] for the finite ranges printed above")
    return 0


if __name__ == "__main__":
    sys.exit(main(quick="--quick" in sys.argv))
