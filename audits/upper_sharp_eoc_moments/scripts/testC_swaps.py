#!/usr/bin/env python3
"""testC_swaps.py  --  Test C: how much cancellation can local (1,2)<->(2,1) swaps supply?

See ../PREREGISTRATION.md section 6 for Gate C, fixed before this script was run.

DERIVATION (re-derived here; stated in FINDINGS.md section C1).  A swap at position j exchanges
(d_j, d_{j+1}) = (1,2) <-> (2,1).  It leaves s_j and s_{j+2} = s_j + 3 fixed and moves s_{j+1} by
one, so in the additive form

    r(D) == 2^S - sum_{i<N} 3^{-(i+1)} 2^{s_i}   (mod 2^{S+1})

exactly ONE summand changes -- the one with i = j+1 -- and r moves by
-3^{-(j+2)} * 2^{s_j+1} (mod 2^{S+1}) in the (1,2) -> (2,1) direction.  The terminal sum S, and
hence the modulus, are unchanged.  Averaging the character over the two orientations multiplies it
by (1 + e(phi_j))/2, of modulus |cos(pi phi_j)|, where with Q_S = 2^{S+1}

    phi_j(h) = ( - h * 3^{-(j+2)} * 2^{s_j+1}  mod  Q_S ) / Q_S .

A site is USABLE iff {d_j, d_{j+1}} = {1,2} and both orientations are zero-confined; since only
s_{j+1} moves, that is exactly  s_j + 2 <= A[j+1].

Exact structural facts, asserted below:
  (i)  for a usable site s_j + 3 = s_{j+2} <= S, so S - s_j >= 3;
  (ii) for ODD h, v2( h * 3^{-(j+2)} * 2^{s_j+1} ) = s_j + 1, so phi_j is an ODD multiple of
       2^{-(S-s_j)} with S - s_j >= 3.  In particular phi_j is never 0 and never 1/2: a single
       swap can neither leave the character untouched nor annihilate it.
  (iii) BUT an odd multiple of 2^{-k} can sit within 2^{-k} of 1/2 (7/16, for instance), so
       |cos(pi phi_j)| is bounded below only by sin(pi 2^{-(S-s_j)}), and the bits from ONE site
       are bounded only by about (S - s_j) - log2 pi.  Per-site cancellation is therefore NOT
       O(1).  (An earlier version of this script asserted a universal per-site ceiling of
       -log2 cos(3 pi/8) = 1.386 bits; that was WRONG and the assertion failed at N = 30.  The
       corrected statement is the one above, and the per-site distribution is reported.)
  (iv) disjointness: each site occupies two positions, so at most N/2 disjoint sites, i.e. the
       density nu of usable disjoint sites is at most 0.5 per step;
  (v)  for phi uniform on [0,1), E[-log2 |cos(pi phi)|] = 1 bit exactly (because
       int_0^1 log|2 cos(pi x)| dx = 0) and the median is 0.5 bits (|cos(pi phi)| < 2^{-1/2} on a
       set of measure exactly 1/2).  So for equidistributed phases swap-averaging delivers about
       nu bits per step in the MEAN, and nu <= 0.5 by (iv).

Needed: alpha - 1 = 0.58496 bits/step merely to beat c = 1; full square root is h/2 = 0.75282
(h an external input, [D]).  Note 0.5 < 0.58496: by (iv) and (v) the mechanism is short of what
is needed even at the maximal site density, for equidistributed phases.  The heavy right tail in
(iii) is why the MEDIAN, not the mean, is the gate statistic.

Gate C (preregistered): record [R] for "local swaps alone supply the needed cancellation" iff the
MEDIAN bits per step is < 0.3 at EVERY tested depth.  This does NOT refute Lemma D1 -- only this
mechanism for it.

Usage:  python3 testC_swaps.py [--quick]      exits non-zero on any failed assertion
"""

import sys
import math
import random
import statistics

import zn

DEPTHS = (20, 30, 40)
NWORDS = 256               # preregistered >= 200
SEED_WORDS = 20261013
SEED_FREQ = 20261014
NRANDH = 256               # preregistered >= 256 random odd h
MEDIAN_GATE = 0.3
NEEDED_BEAT1 = math.log2(3) - 1.0          # 0.584963
NEEDED_SQRT = 1.505644 / 2                 # 0.752822, h/2, external input [D]


def prefix_sums(word):
    s = [0] * (len(word) + 1)
    for j, d in enumerate(word):
        s[j + 1] = s[j] + d
    return s


def usable_sites(word, s, caps):
    """j with {d_j,d_{j+1}} = {1,2} and BOTH orientations zero-confined (s_j + 2 <= A[j+1])."""
    return [j for j in range(len(word) - 1)
            if {word[j], word[j + 1]} == {1, 2} and s[j] + 2 <= caps[j + 1]]


def greedy_disjoint(sites):
    """Maximal disjoint set, greedily left to right (the preregistered rule)."""
    chosen, nxt = [], -1
    for j in sites:
        if j >= nxt:
            chosen.append(j)
            nxt = j + 2
    return chosen


def main(quick=False):
    fail = []
    depths = (20, 30) if quick else DEPTHS
    nwords = 48 if quick else NWORDS
    nrandh = 64 if quick else NRANDH

    print("=" * 110)
    print("Test C -- swap-only cancellation rate")
    print("needed: %.5f bits/step to beat c = 1 (alpha - 1);  %.5f for full square root (h/2, [D])"
          % (NEEDED_BEAT1, NEEDED_SQRT))
    print("=" * 110)

    print("\n[1] structural facts, exact (derivations in the module docstring)")
    print("    phi_j is an odd multiple of 2^{-(S-s_j)}, S - s_j >= 3: never 0, never 1/2   [P]")
    print("    one site can still give up to about (S - s_j) - log2 pi bits: NOT O(1)        [P]")
    print("    at most 0.5 disjoint usable sites per step (disjointness)                     [P]")
    print("    E[-log2|cos(pi phi)|] = 1 bit, median 0.5 bits, for phi uniform               [P]")
    print("    => for equidistributed phases the mechanism gives about nu <= 0.5 bits/step")
    print("       in the mean, against %.5f needed: short even at maximal density" % NEEDED_BEAT1)

    med_primary = {}
    for ens_label, S_fixed in (("terminal shell S = A[N]  (PRIMARY)", True),
                               ("all terminal sums        (secondary)", False)):
        print("\n" + "-" * 110)
        print("[2] ensemble: %s" % ens_label)
        print("    %d base words (seed %d); frequencies: 512 odd h <= 1024 plus %d random odd h"
              % (nwords, SEED_WORDS, nrandh))
        print("-" * 110)
        print("%4s %11s %9s %13s %9s %9s %9s %9s %9s %11s"
              % ("N", "sites/word", "nu", "usable pairs", "mean", "median", "p10", "p90",
                 "max", "per-site med"))
        for N in depths:
            caps = [zn.A(j) for j in range(N + 1)]
            AN = caps[N]
            cnt = zn.completion_counts(N, AN if S_fixed else None)
            wrng = random.Random(SEED_WORDS)
            hrng = random.Random(SEED_FREQ)
            base_odd = list(range(1, 1025, 2))
            bits_all = []
            per_site = []
            nsel, npair = [], []
            for _ in range(nwords):
                word, S = zn.sample_word(N, cnt, wrng)
                assert sum(word) == S
                if S_fixed and S != AN:
                    fail.append("N=%d: sampled word off the terminal shell" % N)
                s = prefix_sums(word)
                for j in range(N):
                    assert (1 << s[j + 1]) <= 3 ** (j + 1), "sampled word not zero-confined"
                QS = 1 << (S + 1)
                sites = usable_sites(word, s, caps)
                J = greedy_disjoint(sites)
                npair.append(len(sites))
                nsel.append(len(J))
                hs = base_odd + [hrng.randrange(0, QS // 2) * 2 + 1 for _ in range(nrandh)]
                coefs = []
                for j in J:
                    # exact structural assertions (i)-(ii)
                    assert S - s[j] >= 3, "usable site with S - s_j < 3"
                    coef = (pow(pow(3, j + 2, QS), -1, QS) * (1 << (s[j] + 1))) % QS
                    assert zn.v2(coef) == s[j] + 1, "v2 of the swap coefficient is not s_j + 1"
                    coefs.append((j, coef))
                for hh in hs:
                    tot = 0.0
                    for (j, coef) in coefs:
                        num = (-hh * coef) % QS
                        assert num != 0 and num != QS // 2, "phi_j hit 0 or 1/2"
                        cc = abs(math.cos(math.pi * (num / QS)))
                        b = -math.log2(cc)
                        tot += b
                        if hh <= 1024:
                            per_site.append(b)
                    bits_all.append(tot / N)
            med = statistics.median(bits_all)
            print("%4d %11.3f %9.4f %13.3f %9.4f %9.4f %9.4f %9.4f %9.4f %11.4f"
                  % (N, statistics.mean(nsel), statistics.mean(nsel) / N,
                     statistics.mean(npair),
                     statistics.mean(bits_all), med,
                     sorted(bits_all)[int(0.10 * len(bits_all))],
                     sorted(bits_all)[int(0.90 * len(bits_all))],
                     max(bits_all),
                     statistics.median(per_site) if per_site else float('nan')))
            if S_fixed:
                med_primary[N] = med

    print("\n[3] GATE C -- preregistered: [R] iff the median bits/step < %.1f at EVERY depth"
          % MEDIAN_GATE)
    print("    (primary ensemble: the terminal shell, where the odd-frequency Fourier")
    print("     coefficients of Z_N are supported -- see check_zn.py section 6)")
    print("%4s %14s %16s %22s %22s"
          % ("N", "median bits", "vs gate 0.3", "fraction of 0.58496", "fraction of 0.75282"))
    for N in depths:
        m = med_primary[N]
        print("%4d %14.4f %16s %22.4f %22.4f"
              % (N, m, "below" if m < MEDIAN_GATE else "AT OR ABOVE",
                 m / NEEDED_BEAT1, m / NEEDED_SQRT))
    trig = all(med_primary[N] < MEDIAN_GATE for N in depths)
    print()
    if trig:
        print("GATE C: [R] -- local swaps alone do NOT supply the needed cancellation.")
        print("  The Tao-style swap mechanism is CLOSED as a sufficient route at every tested depth.")
        print("  This does NOT refute Lemma D1; it refutes only this mechanism for it.")
    else:
        print("GATE C: not refuted at some depth -- the swap mechanism stays [C], supported at the")
        print("  tested depths only.")

    print("\n" + "=" * 110)
    print("Sampled statistics [F]: %d base words per depth per ensemble (seed %d);" % (nwords, SEED_WORDS))
    print("512 odd h <= 1024 plus %d random odd h < Q_S (seed %d)." % (nrandh, SEED_FREQ))
    if fail:
        print("FAILED (%d):" % len(fail))
        for f in sorted(set(fail)):
            print("  - " + f)
        return 1
    print("exact structural assertions passed; the statistics above are [F] sampled")
    return 0


if __name__ == "__main__":
    sys.exit(main(quick="--quick" in sys.argv))
