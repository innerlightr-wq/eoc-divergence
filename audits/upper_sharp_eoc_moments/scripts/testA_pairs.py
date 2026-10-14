#!/usr/bin/env python3
"""testA_pairs.py  --  Test A: pair collisions / low-frequency Fourier mass.

See ../PREREGISTRATION.md section 4 for Gate A, fixed before this script was run.

[1] The identity, derived in FINDINGS.md section A1 and verified here:

        sum_{y mod Q} (X_y - E)^2  =  (M^2/Q) * sum_{h != 0} |F(h)|^2 |W(h)|^2 ,
        W(h) = sum_{t<H} e(-h t/Q),   |W(h)| = |sin(pi h H/Q)/sin(pi h/Q)| ,

    with the Parseval normalization sum_{h mod Q} |F(h)|^2 = Q/M (mean |F|^2 = 1/M).
    Checked at N = 8, 10, 12 over ALL h by FFT of the indicator of Z_N, against the exact
    integer variance from the all-shift histogram.

[2] R_2(N,K) = (M/K) * sum_{0<h<=K} |F(h)|^2 over ALL h (odd and even, dyadic tower included),
    K = ceil(Q/H), c in {0.70,0.80,0.90}.  Word-level DP with lift weights, cross-validated
    against the FFT at N = 8, 10, 12.  Under near-independence R_2 = O(poly N).

[3] Exact pair counts P(N,H) = #{(m,m') in Z_N^2, m != m', circular |m-m'| < H} (ordered),
    against the independence prediction M^2 (2H-1)/Q; and the exact dispersion index mu_2/E.

Gate A (preregistered): record [R] for the pair-collision hypothesis iff, for EVERY c, the OLS
slope of log2 R_2 against N over N=8..18 is >= 0.03 OR the OLS slope of log2 ratio_P is >= 0.03.
Otherwise the pair-collision bound is marked [C], supported at the tested depths only.

Usage:  python3 testA_pairs.py [--quick]      exits non-zero on any failed assertion
"""

import sys
import math
from fractions import Fraction

import numpy as np

import zn

CS = (0.70, 0.80, 0.90)
PRIMARY = list(range(8, 19))
SLOPE_GATE = 0.03
SUBSAMPLE_CAP = 1 << 17          # preregistered: exact for K <= this, else subsample, seed 20261014
SEED_FREQ = 20261014


def ols(xs, ys):
    n = len(xs)
    if n < 3:
        return None
    mx = sum(xs) / n
    my = sum(ys) / n
    den = sum((x - mx) ** 2 for x in xs)
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / den if den else None


def main(quick=False):
    fail = []
    depths = list(range(8, 15)) if quick else PRIMARY

    print("=" * 104)
    print("Test A -- pair collisions and low-frequency Fourier mass")
    print("=" * 104)

    print("\n[1] the variance identity, verified over ALL h by FFT  (exact LHS, [F] RHS)")
    print("    sum_y (X_y-E)^2  ==  (M^2/Q) sum_{h!=0} |F(h)|^2 |W(h)|^2")
    print("%4s %6s %6s %22s %22s %12s %16s"
          % ("N", "H", "Q", "exact LHS", "Fourier RHS", "rel dev", "Parseval dev"))
    for N in ([8, 10] if quick else [8, 10, 12]):
        Z, Q, AN = zn.build_Z(N)
        M = Z.size
        ind = np.zeros(Q, dtype=np.float64)
        ind[Z] = 1.0
        # np.fft.fft uses e^{-2pi i}, F(h) is defined with e^{+2pi i}: conjugate.
        Fh = np.conj(np.fft.fft(ind)) / M              # F(h) for h = 0..Q-1
        p2 = np.abs(Fh) ** 2
        pars = float(p2.sum())
        pars_dev = abs(pars - Q / M) / (Q / M)
        if pars_dev > 1e-9:
            fail.append("Parseval N=%d dev=%.3e" % (N, pars_dev))
        for H in (1 << 4, 1 << 6):
            vals, cnts = zn.window_hist(Z, Q, H)
            E = Fraction(M * H, Q)
            lhs = sum(Fraction(c) * (Fraction(int(v)) - E) ** 2 for v, c in
                      zip(vals.tolist(), cnts.tolist()))
            h = np.arange(1, Q)
            W2 = (np.sin(np.pi * h * H / Q) / np.sin(np.pi * h / Q)) ** 2
            rhs = (M * M / Q) * float((p2[1:] * W2).sum())
            rel = abs(float(lhs) - rhs) / float(lhs)
            if rel > 1e-8:
                fail.append("variance identity N=%d H=%d rel=%.3e" % (N, H, rel))
            print("%4d %6d %6d %22.6f %22.6f %12.3e %16.3e"
                  % (N, H, Q, float(lhs), rhs, rel, pars_dev))

    print("\n[2] DP vs FFT cross-validation of F(h) at low frequencies  ([F], tolerance 1e-9)")
    print("%4s %10s %14s" % ("N", "#h", "max |dev|"))
    for N in ([8, 10] if quick else [8, 10, 12]):
        Z, Q, AN = zn.build_Z(N)
        M = Z.size
        ind = np.zeros(Q, dtype=np.float64)
        ind[Z] = 1.0
        Fh = np.conj(np.fft.fft(ind)) / M              # conjugate: FFT sign convention
        K = min(Q - 1, 4096)
        hs = np.arange(1, K + 1, dtype=np.int64)
        dp = zn.F_batch(N, hs, M)
        dev = float(np.abs(dp - Fh[1:K + 1]).max())
        if dev > 1e-9:
            fail.append("DP vs FFT N=%d dev=%.3e" % (N, dev))
        print("%4d %10d %14.3e" % (N, K, dev))

    print("\n[3] R_2(N,K) = (M/K) sum_{0<h<=K} |F(h)|^2,  K = ceil(Q/H)   ([F] Fourier values)")
    print("    all h in (0,K] exactly (no subsampling needed: K <= 2^17 throughout)")
    print("%4s %5s %6s %10s %16s %12s %12s %12s"
          % ("N", "c", "w", "K", "sum |F|^2", "R_2", "M/K", "odd-h share"))
    R2 = {c: [] for c in CS}
    for N in depths:
        Z, Q, AN = zn.build_Z(N)
        M = Z.size
        ws = {}
        for c in CS:
            w = int(math.floor(c * N))
            ws[c] = w
        Kmax = max((Q + (1 << w) - 1) >> w for w in ws.values())
        if Kmax > SUBSAMPLE_CAP:
            rng = np.random.default_rng(SEED_FREQ)
            hs = np.unique(rng.integers(1, Kmax + 1, size=SUBSAMPLE_CAP, dtype=np.int64))
            sampled = True
        else:
            hs = np.arange(1, Kmax + 1, dtype=np.int64)
            sampled = False
        F = zn.F_batch(N, hs, M)
        p2 = np.abs(F) ** 2
        for c in CS:
            w = ws[c]
            K = (Q + (1 << w) - 1) >> w
            sel = hs <= K
            tot = float(p2[sel].sum())
            if sampled:
                tot *= K / float(sel.sum())
            r2 = (M / K) * tot
            oddsel = sel & (hs % 2 == 1)
            oddshare = float(p2[oddsel].sum()) / tot if tot > 0 else float('nan')
            R2[c].append((N, K, r2))
            print("%4d %5.2f %6d %10d %16.6e %12.5f %12.3e %12.4f"
                  % (N, c, w, K, tot, r2, M / K, oddshare))

    print("\n[4] exact pair counts and the dispersion index   (exact [V])")
    print("    ratio_P = P(N,H) / (M^2 (2H-1)/Q);  disp = mu_2/E  (= 1 for Poisson)")
    print("%4s %5s %8s %16s %18s %18s %10s %10s"
          % ("N", "c", "H", "P ordered", "independence pred", "ratio_P", "disp", "E"))
    ratP = {c: [] for c in CS}
    for N in depths:
        Z, Q, AN = zn.build_Z(N)
        M = Z.size
        for c in CS:
            w = int(math.floor(c * N))
            H = 1 << w
            if H > Q // 2:
                continue
            P, wt = zn.pair_stats(Z, Q, H)
            pred = Fraction(M * M * (2 * H - 1), Q)
            ratio = float(Fraction(P, 1) / pred)
            vals, cnts = zn.window_hist(Z, Q, H)
            E = Fraction(M * H, Q)
            mu2 = sum(Fraction(cc) * (Fraction(int(v)) - E) ** 2 for v, cc in
                      zip(vals.tolist(), cnts.tolist())) / Q
            # exact cross-check of the pair identity
            sumX2 = sum(int(v) ** 2 * int(cc) for v, cc in zip(vals.tolist(), cnts.tolist()))
            if sumX2 != M * H + wt:
                fail.append("pair identity N=%d c=%.2f" % (N, c))
            disp = float(mu2 / E)
            ratP[c].append((N, ratio))
            print("%4d %5.2f %8d %16d %18.3f %18.6f %10.5f %10.3f"
                  % (N, c, H, P, float(pred), ratio, disp, float(E)))

    print("\n[5] GATE A -- preregistered fits (slope gate %+.2f per step)" % SLOPE_GATE)
    print("%6s %16s %16s %16s" % ("c", "slope log2 R_2", "slope log2 ratio_P", "verdict(c)"))
    verd = {}
    for c in CS:
        xs = [N for (N, K, r) in R2[c] if r > 0]
        ys = [math.log2(r) for (N, K, r) in R2[c] if r > 0]
        s_r2 = ols(xs, ys)
        xs2 = [N for (N, r) in ratP[c] if r > 0]
        ys2 = [math.log2(r) for (N, r) in ratP[c] if r > 0]
        s_rp = ols(xs2, ys2)
        trig = ((s_r2 is not None and s_r2 >= SLOPE_GATE) or
                (s_rp is not None and s_rp >= SLOPE_GATE))
        verd[c] = trig
        print("%6.2f %16s %16s %16s"
              % (c,
                 "%+.5f" % s_r2 if s_r2 is not None else "n/a",
                 "%+.5f" % s_rp if s_rp is not None else "n/a",
                 "growing" if trig else "not growing"))
    print()
    if all(verd.values()):
        print("GATE A: [R] -- the pair-collision hypothesis is REFUTED at the tested depths:")
        print("  low-frequency mass / pair excess grows exponentially in N for every c.")
    else:
        print("GATE A: not refuted -- the pair-collision bound is marked [C], supported at the")
        print("  tested depths only (N = %d..%d).  No slope reached the %+.2f gate for every c."
              % (depths[0], depths[-1], SLOPE_GATE))

    print("\n" + "=" * 104)
    if fail:
        print("FAILED (%d):" % len(fail))
        for f in fail:
            print("  - " + f)
        return 1
    print("exact checks passed   [V] for exact quantities; Fourier values are [F]")
    return 0


if __name__ == "__main__":
    sys.exit(main(quick="--quick" in sys.argv))
