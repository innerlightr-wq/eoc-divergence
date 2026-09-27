"""M4 - THE POINTWISE TEST.

Under H0 (realizer uniform in its class) the set of n-confined odd integers
below 2^B, read as a set of words, is distributed EXACTLY as the dyadic law
2^{-S(w)}/p_n on confined words - i.e. exactly as a random confined 2-adic
integer.  Reason: P(r(w) < 2^B) = 2^{B-1-S(w)} under H0, so the induced measure
on words is proportional to 2^{-S(w)}.

So finite height induces no bias at all under H0, and ANY measured difference
between the real-integer cohort and the exactly-sampled generic cohort is a
finite-height law.  No stratification, no matching, no fitted parameter.

This is the far tail of delta: a 32-bit integer 100-confined has
delta = S+1-log2 m ~ 130, where sampling can never reach.
"""
import os, sys, math, csv, glob, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from eoc import Map, word_of
from words import features
from m3_dependence import load, rank

def integer_cohort(scan_dir, n, nmax_seeds=None, seed=1):
    ms = []
    for fn in glob.glob(os.path.join(scan_dir, "part_*.txt")):
        for line in open(fn):
            if line[0] != "D": continue
            t = line.split()
            if int(t[2]) >= n: ms.append(int(t[1]))
    ms.sort()
    if nmax_seeds and len(ms) > nmax_seeds:
        random.Random(seed).shuffle(ms); ms = ms[:nmax_seeds]
    return ms

def cohort_features(mp, ms, n):
    rows = []
    for m in ms:
        w = word_of(mp, m, n)
        f = features(mp, w)
        f["delta"] = (f["S"] + 1) - math.log2(m)
        f["logm"] = math.log2(m)
        rows.append(f)
    return {k: np.array([r[k] for r in rows]) for k in rows[0]}

def compare(A, Bd, keys):
    """Welch t of A vs B for each key, in units of B's sd."""
    out = []
    for k in keys:
        a, b = A[k], Bd[k]
        sd = b.std()
        if sd == 0: continue
        t = (a.mean() - b.mean()) / math.sqrt(a.var()/len(a) + b.var()/len(b))
        out.append((abs(t), t, (a.mean()-b.mean())/sd, k))
    out.sort(reverse=True)
    return out

if __name__ == "__main__":
    mp = Map(3, 1)
    print("M4  real 32-bit integers vs exactly-sampled generic confined words.")
    print("    Under H0 the two cohorts have IDENTICAL word law (see module docstring).")
    print("    t = Welch t of the difference; d = difference in sd units of the")
    print("    generic cohort.  Null: t = 0 for every statistic, including S.")
    print()
    for n in [100, 120, 140, 160, 180, 200]:
        ms = integer_cohort("results/scan_A32deep", n, nmax_seeds=80000)
        if len(ms) < 300: 
            print(f"n={n}: only {len(ms)} integers, skipped"); continue
        A = cohort_features(mp, ms, n)
        gp = f"results/words/3x+1_n{n}.csv"
        if not os.path.exists(gp):
            print(f"n={n}: no generic sample at this n"); continue
        Bd = load(gp)
        keys = [k for k in sorted(Bd) if k in A and k not in ("n",)]
        out = compare(A, Bd, keys)
        nflag = sum(1 for a, *_ in out if a > 4)
        print(f"n={n:4d}  integers={len(ms):6d}  generic={len(Bd['S']):6d}  "
              f"mean delta(int)={A['delta'].mean():.1f}   #|t|>4 = {nflag}")
        for a, t, d, k in out[:8]:
            print(f"      {k:14s} t={t:+8.2f}  d={d:+7.4f} sd   "
                  f"int={A[k].mean():10.4f}  gen={Bd[k].mean():10.4f}")
        print()
