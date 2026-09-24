#!/usr/bin/env python3
"""O1 -- the drift fingerprint, exactly.

Under Haar the letters are i.i.d. geometric(1/2) (Phase 0, F1), so S_N is a
negative binomial and the whole distribution of the drift is computable in exact
rational arithmetic -- no sampling, no floating point in the decisions.

    P(S_N = s) = C(s-1, N-1) 2^{-s},   s >= N.

The drift used here is the user's convention  D_N = N*alpha - S_N  (per-step
increment alpha - a), so E[D_N] = N(alpha - 2) and Var(D_N) = 2N for every map.
"""
from fractions import Fraction
from math import comb, log2, sqrt, erf, exp, pi

MAPS = {"A (3x+1)": 3, "B (3x-1)": 3, "C (5x+1)": 5}


def exact_letter_moments():
    """Central moments of a ~ Geom(1/2) on {1,2,...}, exact."""
    # closed forms for p = 1/2
    mean = Fraction(2)
    var = Fraction(2)
    mu3 = Fraction(6)
    mu4 = Fraction(38)
    return mean, var, mu3, mu4


def phi(z):
    return exp(-z * z / 2) / sqrt(2 * pi)


def Phi(z):
    return 0.5 * (1 + erf(z / sqrt(2)))


def sN_cdf_points(N):
    """Exact P(S_N <= s) as Fractions, for s in [N, N + 12*sqrt(2N)]."""
    out = {}
    acc = Fraction(0)
    hi = int(2 * N + 14 * sqrt(2 * N)) + 20
    for s in range(N, hi + 1):
        acc += Fraction(comb(s - 1, N - 1), 1) / Fraction(2 ** s)
        out[s] = acc
    return out


def main():
    mean, var, mu3, mu4 = exact_letter_moments()
    print("=" * 78)
    print("O1a  per-step drift increment  Delta = alpha - a,  EXACT (Phase 0, F1')")
    print("=" * 78)
    print(f"  letter a:  mean {mean}  var {var}  mu3 {mu3}  mu4 {mu4}")
    skew = -float(mu3) / float(var) ** 1.5
    exk = float(mu4) / float(var) ** 2 - 3
    for name, q in MAPS.items():
        a = log2(q)
        print(f"  {name:10s} alpha = {a:.10f}   mean {a - 2:+.10f}   var {float(var):.10f}   "
              f"skew {skew:+.10f}   exkurt {exk:+.10f}")
    print("  -> variance, skewness and excess kurtosis are IDENTICAL across the three maps;")
    print("     only the mean differs, by exactly log2(5/3) = %.10f." % (log2(5) - log2(3)))

    print()
    print("=" * 78)
    print("O1b  finite-N shape of the normalized drift, EXACT vs Gaussian vs Edgeworth")
    print("=" * 78)
    print("  The law of S_N does not involve q at all, so the normalized drift")
    print("  Z_N = (D_N - N(alpha-2)) / sqrt(2N) = (2N - S_N)/sqrt(2N) is the SAME")
    print("  random variable for A, B and C.  One table therefore serves all three.")
    print()
    print("     N     sup|F_N - Phi|   sup|F_N - Edgeworth1|   ratio   N^(1/2)*sup|F-Phi|")
    g1 = skew                      # skewness of Delta = skewness of -a
    for N in (2, 4, 8, 16, 32, 64, 128, 256, 512, 1024):
        cdf = sN_cdf_points(N)
        sd = sqrt(2 * N)
        worst_g = 0.0
        worst_e = 0.0
        for s, F in cdf.items():
            # Z = (2N - s)/sd ; P(D <= d) with D = N*alpha - S  <=>  S >= N*alpha - d
            # use the lattice midpoint (continuity correction) for a fair comparison
            z = (2 * N - (s + 0.5)) / sd
            Fz = float(1 - F)                     # exact subtraction first, then round
            worst_g = max(worst_g, abs(Fz - Phi(z)))
            ed = Phi(z) - phi(z) * (g1 / 6.0) * (z * z - 1) / sqrt(N)
            worst_e = max(worst_e, abs(Fz - ed))
        print(f"  {N:5d}   {worst_g:.6e}        {worst_e:.6e}    {worst_e/worst_g:6.3f}   "
              f"{sqrt(N)*worst_g:.6f}")
    print("  The Edgeworth correction uses gamma1 = %.6f, which is map-independent." % g1)


if __name__ == "__main__":
    main()
