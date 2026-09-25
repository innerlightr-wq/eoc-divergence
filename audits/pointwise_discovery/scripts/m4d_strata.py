"""M4d - THE SHARPEST FORM OF THE FINITE-HEIGHT TEST.

Take every odd m < 2^36 that is n-confined (complete enumeration, no sampling
anywhere) and split the cohort by the seed's bit length b.  Under H0 every
stratum has the SAME word law: P(r(w) in [2^{b-1}, 2^b)) = 2^{b-2-S(w)}, which
is proportional to 2^{-S(w)} for every b, so b drops out.

So: do small integers have different valuation words from large integers at the
same depth?  That is the finite-height question in its purest computable form.
Both sides are complete enumerations, so there is no Monte-Carlo error on either
side and no null model is fitted.
"""
import os, sys, math, glob, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from eoc import Map
from m4_integers_vs_words import cohort_features

DUMP_MIN = 140          # the depth threshold the scan dumped at

def cohort(scan_dir, n):
    assert n >= DUMP_MIN, "the scan only dumped seeds of depth >= %d" % DUMP_MIN
    ms = []
    for fn in glob.glob(os.path.join(scan_dir, "part_*.txt")):
        for line in open(fn):
            if line[0] != "D": continue
            t = line.split()
            if int(t[2]) >= n: ms.append(int(t[1]))
    return sorted(ms)

def welch(a, b):
    return (a.mean() - b.mean()) / math.sqrt(a.var(ddof=1)/len(a) + b.var(ddof=1)/len(b))

if __name__ == "__main__":
    mp = Map(3, 1)
    print(__doc__.strip())
    print()
    for n in [140, 160, 180]:
        ms = cohort("results/scan_A36", n)
        F = cohort_features(mp, ms, n)
        bits = np.array([int(m).bit_length() for m in ms])
        keys = [k for k in sorted(F) if k not in ("n", "delta", "logm")]
        splits = [(0, 32), (32, 34), (34, 40)]
        groups = [(lo, hi, bits >= lo) & (bits < hi) if False else (lo, hi, (bits >= lo) & (bits < hi))
                  for lo, hi in splits]
        print(f"n = {n}:  {len(ms)} integers; strata "
              + ", ".join(f"[{lo},{hi}) : {g.sum()}" for lo, hi, g in groups))
        # every pair of strata
        worst = []
        for i in range(len(groups)):
            for j in range(i + 1, len(groups)):
                gi, gj = groups[i][2], groups[j][2]
                if gi.sum() < 300 or gj.sum() < 300: continue
                for k in keys:
                    t = welch(F[k][gi], F[k][gj])
                    worst.append((abs(t), t, k, groups[i][:2], groups[j][:2]))
        worst.sort(reverse=True)
        ntest = len(worst)
        thr = 3.9      # ~ Bonferroni 5% for a few hundred tests
        print(f"   {ntest} pairwise tests; |t| > {thr} flagged.  Top 5:")
        for a, t, k, gi, gj in worst[:5]:
            print(f"      {k:14s} bits{gi} vs bits{gj}   t = {t:+7.2f}"
                  + ("   FLAG" if a > thr else ""))
        print(f"   number of |t| > {thr}: {sum(1 for a,*_ in worst if a > thr)}")
        # the S-marginal specifically, which is the one H0 pins
        for i in range(len(groups)):
            for j in range(i + 1, len(groups)):
                gi, gj = groups[i][2], groups[j][2]
                if gi.sum() < 300 or gj.sum() < 300: continue
                print(f"      S: bits{groups[i][:2]} mean {F['S'][gi].mean():.3f}  vs  "
                      f"bits{groups[j][:2]} mean {F['S'][gj].mean():.3f}   "
                      f"t = {welch(F['S'][gi], F['S'][gj]):+.2f}")
        print()
