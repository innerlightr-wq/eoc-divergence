"""M3 - does any word statistic predict the realizer deficit delta?

Under H0 (realizer uniform in its class, independent of the word) every
correlation below is zero.  Tests:
  (a) Spearman rho(feature, delta), with S partialled out by within-S ranking;
  (b) the same on chain roots only (the L1/L2 mechanism removed).
The Fisher z SE for Spearman is 1/sqrt(K-3); |z| > 4 is flagged.
"""
import sys, math, csv, glob, os
import numpy as np

SKIP = {"delta", "r_bits", "root", "v3r1", "r_mod8", "r_mod3", "n"}

def rank(a):
    o = a.argsort(kind="mergesort"); r = np.empty(len(a)); r[o] = np.arange(len(a))
    # average ties
    s = a[o]; i = 0
    while i < len(s):
        j = i
        while j + 1 < len(s) and s[j + 1] == s[i]: j += 1
        if j > i: r[o[i:j+1]] = (i + j) / 2
        i = j + 1
    return r

def spearman(x, y):
    rx, ry = rank(x), rank(y)
    rx = rx - rx.mean(); ry = ry - ry.mean()
    d = math.sqrt((rx*rx).sum() * (ry*ry).sum())
    return 0.0 if d == 0 else float((rx*ry).sum() / d)

def within_S_resid(x, S):
    """rank x within each S-stratum, then centre: removes any dependence on S."""
    out = np.zeros(len(x))
    for s in np.unique(S):
        m = S == s
        if m.sum() < 5: out[m] = 0.0; continue
        r = rank(x[m]); out[m] = (r - r.mean()) / max(r.std(), 1e-12)
    return out

def load(path):
    rows = list(csv.DictReader(open(path)))
    return {k: np.array([float(r[k]) for r in rows]) for k in rows[0]}

def analyse(path, verbose=True):
    c = load(path)
    d = c["delta"]; S = c["S"]; K = len(d)
    feats = [k for k in sorted(c) if k not in SKIP]
    se = 1 / math.sqrt(K - 3)
    res = []
    dr = within_S_resid(d, S)
    for f in feats:
        xr = within_S_resid(c[f], S)
        rho = spearman(xr, dr)
        res.append((abs(rho), rho, f))
    res.sort(reverse=True)
    return res, se, K, c

def main():
    files = sorted(glob.glob("results/words/*.csv"),
                   key=lambda s: (s.split('/')[-1].split('_')[0], int(s.split('_n')[1][:-4])))
    print("M3  Spearman rho(feature, delta) with S partialled out (within-S ranks).")
    print("    Null: rho = 0.  SE = 1/sqrt(K-3).  Top 6 features by |rho| per dataset.")
    print()
    for path in files:
        name = os.path.basename(path)[:-4]
        res, se, K, c = analyse(path)
        top = res[:6]
        flag = [t for t in res if abs(t[1]) > 4 * se]
        print(f"{name:12s} K={K:6d}  SE={se:.4f}  4SE={4*se:.4f}   "
              f"#|rho|>4SE = {len(flag)}")
        print("     " + "  ".join(f"{f}={r:+.3f}" for _, r, f in top))
    print()

if __name__ == "__main__":
    main()
