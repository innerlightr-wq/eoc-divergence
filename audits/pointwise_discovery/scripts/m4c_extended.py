"""M4 extended: the pointwise test over a complete scan of every odd m < 2^36,
at several depths, and stratified by the seed's bit length (i.e. by delta)."""
import os, sys, math, glob, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from eoc import Map
from m3_dependence import load
from m4_integers_vs_words import integer_cohort, cohort_features, compare

mp = Map(3, 1)
print("M4c  every odd m < 2^36 that is n-confined, against 2x10^4 generic")
print("     confined words sampled from the exact dyadic law.")
print("     Under H0 the two cohorts have identical word law - including S.")
print("     t = Welch t;  d = mean difference in sd units of the generic cohort.")
print()
print(f"{'n':>4} {'integers':>9} {'mean delta':>10} {'max|t|':>7} {'max|d|':>7} "
      f"{'t(S)':>7}   worst statistic")
allrows = []
# scan_A36 dumped only seeds of depth >= 140, so n < 140 would be a
# biased sub-cohort; n = 100 is covered by m4_integers_vs_words.py,
# which reads scan_A32deep (threshold 100).
for n in [140, 160, 180, 200]:
    ms = integer_cohort("results/scan_A36", n)
    gp = f"results/words/3x+1_n{n}.csv"
    if len(ms) < 200 or not os.path.exists(gp): continue
    A = cohort_features(mp, ms, n); Bd = load(gp)
    keys = [k for k in sorted(Bd) if k in A and k not in ("n", "delta")]
    out = compare(A, Bd, keys)
    tS = [t for _, t, _, k in out if k == "S"][0]
    a, t, dd, k = out[0]
    print(f"{n:>4} {len(ms):>9} {A['delta'].mean():>10.1f} {a:>7.2f} "
          f"{abs(dd):>7.4f} {tS:>7.2f}   {k}")
    allrows.append((n, len(ms), out))
print()
print("     Bonferroni threshold over all statistics x depths: |t| > 3.7 at 5%.")
print()
print("M4c(b)  stratified by seed bit length within the n=140 cohort")
print("        (each stratum has the same word law under H0)")
n = 140
ms = integer_cohort("results/scan_A36", n)
Bd = load(f"results/words/3x+1_n{n}.csv")
ms = np.array(ms)
print(f"{'bits':>7} {'count':>8} {'mean delta':>10} {'max|t|':>7}   worst statistic")
for lo, hi in [(20, 28), (28, 32), (32, 34), (34, 37)]:
    sub = [int(m) for m in ms if lo <= int(m).bit_length() < hi]
    if len(sub) < 200: continue
    A = cohort_features(mp, sub, n)
    keys = [k for k in sorted(Bd) if k in A and k not in ("n", "delta")]
    out = compare(A, Bd, keys)
    print(f"{lo:>3}-{hi-1:<3} {len(sub):>8} {A['delta'].mean():>10.1f} "
          f"{out[0][0]:>7.2f}   {out[0][3]}")
