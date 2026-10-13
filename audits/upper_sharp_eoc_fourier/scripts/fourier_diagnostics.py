#!/usr/bin/env python3
"""fourier_diagnostics.py  --  [F] Fourier diagnostics for the terminal shell.

Status labels:
  everything involving a complex exponential            [F]  float diagnostic, NOT a proof
  the direct interval-hit counts #{r < 2^floor(cN)}     [V]  exact integer counts
  the DP-vs-brute agreement figure                      [F]  bounds the implementation only

ENSEMBLE.  Terminal shell: 0-confined positive words of length N with terminal sum
exactly S = A[N].  Modulus Q = 2^(S+1).  Uniform weights (within one shell every word
has geometric density 2^(-S), and D |-> r(D) is injective on the shell -- proved
exactly in check_realizers.py).  NO SHELLS ARE MIXED.  Normalization:

    F_N(h) = (1/M_N) * sum_{D in W_0(N)} exp(2 pi i h r(D) / Q),      F_N(0) = 1.

THE DP.  By the additive formula (check_additive_formula.py) the j-th summand of r
depends on the path only through (j, s_j), so the twisted sum factorizes through a
forward DP on that state, of size O(N^2).  Validated against brute-force enumeration
below.

ERDOS-TURAN.  Form used:   D_N  <=  C_ET * ( 1/K + sum_{h=1}^{K} |F_N(h)|/h ).
C_ET is a STATED PARAMETER here.  It has NOT been verified against a printed primary
source in this round; the margins below are 2^5-2^8, so the verdict is unchanged for
any C_ET in [1,10], but a theorem would need the constant pinned down.

ROUNDING.  H = 2^floor(c*N) (integer).  K* = ceil(Q/H).  Success condition for a hit
in the initial interval [0, H/Q):  C_ET * B_N(K*) < H/Q.

Writes nothing; prints to stdout only.  Exits non-zero only if an exact check or the
DP validation fails.

Usage:  python3 fourier_diagnostics.py [--quick] [--cet=4.0]
"""

import cmath
import math
import random
import sys

ALPHA = math.log2(3)          # log2 3
H_RATE = 1.505644             # the confined-word growth exponent (external input, [D])


def A(k):
    return (3 ** k).bit_length() - 1


def shell_size(N):
    S = A(N)
    f = {0: 1}
    for j in range(N):
        g = {}
        cap = A(j + 1)
        for s, c in f.items():
            for d in range(1, cap - s + 1):
                g[s + d] = g.get(s + d, 0) + c
        f = g
    return f[S], S


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
    return ((2 ** s - q) * pow(pow(3, N, Q), -1, Q)) % Q


def fourier_dp(N, hlist):
    """Unnormalized twisted sums sum_D exp(2 pi i h r(D)/Q), via the O(N^2) DP.  [F]"""
    S = A(N)
    Q = 2 ** (S + 1)
    inv3 = pow(3, -1, Q)
    pw2 = [pow(2, s, Q) for s in range(S + 1)]
    inv3p = [pow(inv3, j + 1, Q) for j in range(N)]
    const = (pow(3, -N, Q) * pow(2, S, Q)) % Q
    caps = [A(k) for k in range(N + 1)]
    tau = 2j * math.pi
    out = {}
    for h in hlist:
        cur = {0: 1 + 0j}
        for j in range(N):
            nxt = {}
            cj = caps[j + 1]
            hj = (h * inv3p[j]) % Q
            for s, v in cur.items():
                vv = v * cmath.exp(tau * (((-hj * pw2[s]) % Q) / Q))
                for d in range(1, cj - s + 1):
                    s2 = s + d
                    nxt[s2] = nxt.get(s2, 0j) + vv
            cur = nxt
        out[h] = cur.get(S, 0j) * cmath.exp(tau * (((h * const) % Q) / Q))
    return out, S, Q


def main(quick=False, cet=4.0):
    fail = []
    random.seed(20261013)

    print("=" * 78)
    print("fourier_diagnostics.py  --  [F] diagnostics, C_ET = %g (stated parameter)" % cet)
    print("=" * 78)

    # ---- 1. DP validated against brute force -----------------------------
    print("\n[1] [F] DP vs brute-force enumeration (two independent routes)")
    print("    %3s %10s %28s" % ("N", "M_N", "max relative deviation"))
    for N in (10, 15):
        ws, S = shell_words(N)
        Q = 2 ** (S + 1)
        rs = [least_realizer(d) for d in ws]
        hl = [1, 2, 3, 7, 17, 100, Q // 8, Q // 4, Q // 2]
        dp, _, _ = fourier_dp(N, hl)
        worst = 0.0
        for h in hl:
            bf = sum(cmath.exp(2j * math.pi * ((h * r) % Q) / Q) for r in rs)
            worst = max(worst, abs(bf - dp[h]) / max(1.0, abs(bf)))
        if worst > 1e-9:
            fail.append("DP/brute disagreement at N=%d: %.3e" % (N, worst))
        print("    %3d %10d %28.3e" % (N, len(rs), worst))

    # ---- 2. the forced mod-4 peak ----------------------------------------
    print("\n[2] [F] the forced peak: |F_N(Q/4)| = 1 identically  (r == 3 mod 4)")
    print("    %3s %10s %12s %12s %12s %12s %12s"
          % ("N", "M_N", "|F(Q/2)|", "|F(Q/4)|", "|F(Q/8)|", "|F(1)|", "M^-1/2"))
    for N in (12, 14, 15, 16):
        ws, S = shell_words(N)
        Q = 2 ** (S + 1)
        rs = [least_realizer(d) for d in ws]
        M = len(rs)

        def F(h):
            return abs(sum(cmath.exp(2j * math.pi * ((h * r) % Q) / Q) for r in rs)) / M

        f4 = F(Q // 4)
        if abs(f4 - 1.0) > 1e-9:
            fail.append("|F(Q/4)| != 1 at N=%d: %.6f" % (N, f4))
        print("    %3d %10d %12.6f %12.6f %12.6f %12.3e %12.3e"
              % (N, M, F(Q // 2), f4, F(Q // 8), F(1), M ** -0.5))
    print("    => sup_{h!=0} |F_N(h)| CANNOT decay.  'sup |F| -> 0' is not a usable test.")

    # ---- 3. low frequencies vs the square-root scale ---------------------
    K = 1024
    print("\n[3] [F] mean |F_N(h)| over h = 1..%d against M_N^(-1/2)" % K)
    print("    %3s %4s %22s %11s %11s %11s %14s %11s"
          % ("N", "S", "M_N", "M^-1/2", "mean|F|", "max|F|", "mean/M^-1/2", "B_N(K)"))
    Ns = [15, 20, 25, 30] if quick else [15, 20, 25, 30, 40, 50]
    store = {}
    for N in Ns:
        M, S = shell_size(N)
        res, _, Q = fourier_dp(N, list(range(1, K + 1)))
        Fv = [abs(res[h]) / M for h in range(1, K + 1)]
        B = 1.0 / K + sum(Fv[h - 1] / h for h in range(1, K + 1))
        store[N] = (M, S, Q, Fv, B)
        print("    %3d %4d %22d %11.3e %11.3e %11.3e %14.3f %11.3e"
              % (N, S, M, M ** -0.5, sum(Fv) / K, max(Fv), (sum(Fv) / K) / M ** -0.5, B))
    if quick:
        print("    (--quick: N=40,50 skipped)")
    print("\n    log2 of mean|F| and the slope against the square-root target -h/2 = %.4f"
          % (-H_RATE / 2))
    xs = [(N, math.log2(sum(store[N][3]) / K)) for N in Ns]
    print("    " + ", ".join("N=%d:%.2f" % (n, v) for n, v in xs))
    if len(xs) >= 2:
        sl = (xs[-1][1] - xs[-2][1]) / (xs[-1][0] - xs[-2][0])
        print("    slope over the last two depths: %+.4f   (target %+.4f)"
              % (sl, -H_RATE / 2))

    # ---- 3b. mean |F| by 2-adic level t = v2(h)  (the dyadic tower law) ---
    print("\n[3b] [F] mean |F_N(2^t u)| by 2-adic level t = v_2(h), u odd")
    print("     the measured law is  |F_N(2^t u)| ~ max( M_N^(-1/2), 2^(-(S+1-t)/2) ),")
    print("     with crossover at t* = S + 1 - log2(M_N)  (asymptotically I_0 * N).")
    nu = 64 if quick else 256
    for N in (20, 25, 30):
        M, S = shell_size(N)
        nrm = M ** -0.5
        tstar = S + 1 - math.log2(M)
        print("\n     N=%d  S=%d  M_N=%d  M^-1/2=%.3e  predicted t* = %.1f"
              % (N, S, M, nrm, tstar))
        print("     %4s %12s %12s %14s %14s %12s"
              % ("t", "modulus", "mean|F|", "ratio/M^-1/2", "2^(-(S+1-t)/2)", "max|F|"))
        levels = [0, 1, 2, 4, 6, 8, 12, 16, 20, S - 6, S - 4, S - 2, S - 1]
        for t in levels:
            if t < 0 or t > S - 1:
                continue
            m = 2 ** (S + 1 - t)
            if m > 512:
                us = [random.randrange(1, m, 2) for _ in range(nu)]
            else:
                us = list(range(1, m, 2))
            hs = sorted(set((2 ** t) * u for u in us))
            r = fourier_dp(N, hs)[0]
            vals = [abs(r[h]) / M for h in hs]
            mean = sum(vals) / len(vals)
            print("     %4d %12s %12.3e %14.3f %14.3e %12.3e"
                  % (t, "2^%d" % (S + 1 - t), mean, mean / nrm,
                     2.0 ** (-(S + 1 - t) / 2.0), max(vals)))
    print("\n     => mean |F| stays at the square-root scale for t below t* and is")
    print("        governed by 2^(-(S+1-t)/2) above it.  [F], sampled, not a proof.")

    # ---- 4. band means and the Erdos-Turan margins -----------------------
    nprobe = 48 if quick else 128
    print("\n[4] [F] band-mean |F| (uniform random h per dyadic band, %d probes)" % nprobe)
    print("    sum_{h in [2^k,2^(k+1))} |F(h)|/h  ~  mean_k * ln2  (h log-uniform in band)")
    bands = {}
    for N in (20, 25, 30):
        M, S = shell_size(N)
        Q = 2 ** (S + 1)
        means = []
        for k in range(0, S + 1):
            lo, hi = 2 ** k, min(2 ** (k + 1), Q)
            if hi - lo <= 1:
                hs = [lo]
            else:
                hs = [random.randrange(lo, hi) for _ in range(min(nprobe, hi - lo))]
            r = fourier_dp(N, hs)[0]
            means.append(sum(abs(r[h]) for h in hs) / len(hs) / M)
        bands[N] = (M, S, Q, means)
        print("    N=%2d  M_N=%d  mean over all bands / M^-1/2 = %.3f"
              % (N, M, (sum(means) / len(means)) / M ** -0.5))

    print("\n[5] [F] Erdos-Turan test.  H = 2^floor(cN), K* = ceil(Q/H), C_ET = %g" % cet)
    print("    %3s %6s %14s %12s %16s %12s %20s %18s"
          % ("N", "c", "H", "H/Q", "K*", "1/K*", "est sum|F|/h to K*", "verdict"))
    for N in (20, 25, 30):
        M, S, Q, means = bands[N]
        for c in (0.90, 0.95, 0.99):
            H = 2 ** int(math.floor(c * N))
            HQ = H / Q
            Kstar = -(-Q // H)
            kmax = max(0, Kstar.bit_length() - 1)
            ssum = sum(means[k] * math.log(2) for k in range(0, min(kmax + 1, len(means))))
            B = 1.0 / Kstar + ssum
            if cet * B < HQ:
                verdict = "PASS"
            else:
                verdict = "FAIL by 2^%.1f" % math.log2(cet * B / HQ)
            print("    %3d %6.2f %14d %12.3e %16d %12.3e %20.3e %18s"
                  % (N, c, H, HQ, Kstar, 1.0 / Kstar, ssum, verdict))

    # ---- 6. the finite-size deficit --------------------------------------
    print("\n[6] [F] why it fails: need log2(M_N)/N > 2(alpha - c).  alpha = %.6f" % ALPHA)
    print("    %4s %14s %18s %18s %18s"
          % ("N", "log2(M_N)/N", "2(a-c), c=0.90", "c=0.95", "c=0.99"))
    for N in Ns:
        lm = math.log2(store[N][0]) / N
        cells = []
        for c in (0.90, 0.95, 0.99):
            need = 2 * (ALPHA - c)
            cells.append("%8.4f %7s" % (need, "OK" if lm > need else "SHORT"))
        print("    %4d %14.4f %18s %18s %18s" % (N, lm, cells[0], cells[1], cells[2]))
    print("    the limit of log2(M_N)/N is h ~ %.6f  ([D], external input), so the" % H_RATE)
    print("    asymptotic condition is  c > alpha - h/2 = %.6f" % (ALPHA - H_RATE / 2))
    print("    and no equidistribution method of this kind can go below")
    print("    alpha - h = I_0 ~ %.6f" % (ALPHA - H_RATE))

    # ---- 7. projected first viable depth ---------------------------------
    print("\n[7] [F] projected first depth where the bound could hold  (EXTRAPOLATION)")
    print("    using M_N ~ 0.4 * 2^(-3.28) * 2^(hN) * N^(-3/2), the fitted count")
    print("    asymptotic of the synthesis note's Prop 4.7  ([D], external input)")

    def logM(N):
        return H_RATE * N - 1.5 * math.log2(N) - 3.28 + math.log2(0.4)

    print("    %6s %10s %12s %22s" % ("c", "alpha-c", "first N", "K* at that N"))
    for c in (0.99, 0.95, 0.90):
        gap = ALPHA - c
        Nc = None
        for N in range(10, 4001):
            lhs = math.log2(cet) + math.log2(0.5 * math.log(2) * (gap * N + 1)) - logM(N) / 2
            if lhs < -(gap * N + 1):
                Nc = N
                break
        if Nc:
            ex = gap * Nc + 1
            print("    %6.2f %10.4f %12d %22s"
                  % (c, gap, Nc, "2^%.1f ~ 10^%.0f" % (ex, ex * 0.301)))
    print("    => the hypothesis first bites where it ranges over 10^17-10^53")
    print("       frequencies.  It is not numerically verifiable.  [F], extrapolated.")

    # ---- 8. exact direct interval hits  [V] ------------------------------
    print("\n[8] [V] EXACT direct interval-hit counts in the shell (integer counts)")
    print("    %3s %4s %10s %10s %6s %12s %8s %18s"
          % ("N", "S", "M_N", "min r", "c", "H", "#r<H", "uniform M*H/Q"))
    for N in (14, 15, 16):
        ws, S = shell_words(N)
        Q = 2 ** (S + 1)
        rs = sorted(least_realizer(d) for d in ws)
        M = len(rs)
        for c in (0.90, 0.95, 0.99):
            H = 2 ** int(math.floor(c * N))
            n = sum(1 for r in rs if r < H)
            if c == 0.90:
                assert n > 0 and rs[0] < H, (N, c)
            print("    %3d %4d %10d %10d %6.2f %12d %8d %18.3f"
                  % (N, S, M, rs[0], c, H, n, M * H / Q))
    print("    => r_min(N,0) <= 2^(0.9N) for N = 14,15,16, as an EXACT finite fact.")
    print("       Nothing asymptotic follows, and these hits certify neither the")
    print("       Fourier estimate nor any statement for large N.")

    print("\n" + "=" * 78)
    if fail:
        print("FAILED (%d):" % len(fail))
        for f in fail:
            print("  - " + f)
        return 1
    print("diagnostics complete.  Float quantities above are [F]; section [8] is [V].")
    return 0


if __name__ == "__main__":
    cet = 4.0
    for a in sys.argv[1:]:
        if a.startswith("--cet="):
            cet = float(a.split("=", 1)[1])
    sys.exit(main(quick="--quick" in sys.argv, cet=cet))
