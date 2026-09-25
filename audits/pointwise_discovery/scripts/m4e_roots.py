"""M4e - the finite-height test with the known L1/L2 chain correlation removed.

Confined integers come in backward chains (L1/L2): if m is n-confined and
m == 2 (mod 3) then back(m) = (2m-1)/3 is smaller, (n+1)-confined, and its word
is 1.word(m).  A chain therefore contributes several members with nearly the same
word AND with bit lengths 0.585 apart, so it straddles bit-length strata and the
nominal Welch t is anticonservative.

Two corrections, both applied:
 (a) restrict to chain roots (3 does not divide m+1), one member per chain;
 (b) a chain-level bootstrap: resample whole chains, not individual seeds, and
     read the SE off the resamples.

Statistic: Spearman rho(word statistic, log2 m) over the n-confined cohort.
Under H0 it is 0 for every statistic - the seed's size tells you nothing about
its word.
"""
import os, sys, math, glob, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from eoc import Map
from m4_integers_vs_words import cohort_features
from m4d_strata import cohort
from m3_dependence import spearman

def chain_id(m):
    """The root of m's backward d=1 chain, used as a cluster label."""
    while m % 3 == 2:
        m = (2 * m - 1) // 3
    return m

def boot_se(x, y, cid, B=400, seed=11):
    rng = random.Random(seed)
    groups = {}
    for i, c in enumerate(cid): groups.setdefault(c, []).append(i)
    keys = list(groups); out = []
    for _ in range(B):
        idx = []
        for _ in range(len(keys)):
            idx.extend(groups[keys[rng.randrange(len(keys))]])
        idx = np.array(idx)
        out.append(spearman(x[idx], y[idx]))
    return float(np.std(out))

if __name__ == "__main__":
    mp = Map(3, 1)
    print(__doc__.strip()); print()
    for n in [140, 160, 180]:
        ms = cohort("results/scan_A36", n)
        F = cohort_features(mp, ms, n)
        logm = np.array([math.log2(m) for m in ms])
        root = np.array([m % 3 != 2 for m in ms])
        cid = np.array([chain_id(m) for m in ms])
        keys = [k for k in sorted(F) if k not in ("n", "delta", "logm")
                and F[k].std() > 0]
        res = []
        for k in keys:
            rho_all = spearman(F[k], logm)
            rho_rt = spearman(F[k][root], logm[root])
            res.append((abs(rho_rt), rho_all, rho_rt, k))
        res.sort(reverse=True)
        se_naive = 1 / math.sqrt(root.sum() - 3)
        # bootstrap SE for the top statistic
        top = res[0][3]
        se_b = boot_se(F[top], logm, cid)
        print(f"n = {n}:  {len(ms)} integers, {root.sum()} chain roots, "
              f"{len(set(cid))} distinct chains")
        print(f"   naive SE (roots) = {se_naive:.4f};  chain-bootstrap SE for "
              f"'{top}' = {se_b:.4f}  (inflation x{se_b/se_naive:.1f})")
        print(f"   {'statistic':14s} {'rho(all)':>9} {'rho(roots)':>11} "
              f"{'z_naive':>8} {'z_boot':>8}")
        for a, ra, rr, k in res[:6]:
            print(f"   {k:14s} {ra:>9.4f} {rr:>11.4f} {rr/se_naive:>8.2f} "
                  f"{rr/se_b:>8.2f}")
        print()
