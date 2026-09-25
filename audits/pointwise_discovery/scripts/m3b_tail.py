"""M3b - the two tests that actually bear on the frontier.

(1) Multivariate: can ALL word features together predict delta (within S)?
    R^2 of within-S-ranked delta on within-S-ranked features.  Null: R^2 ~ p/K.
(2) The small-realizer tail: take the words with the smallest log2 r(w) - the
    same selection that produces r_min - and compare their feature distribution
    with the rest at matched S.  This is the record-holder-anatomy question with
    a sample of thousands instead of 24, and it is the one that matters for the
    frontier.
"""
import sys, math, csv, glob, os
import numpy as np
from m3_dependence import load, rank, within_S_resid, SKIP

def multi_r2(c):
    d = c["delta"]; S = c["S"]; K = len(d)
    feats = [k for k in sorted(c) if k not in SKIP]
    X = np.column_stack([within_S_resid(c[f], S) for f in feats])
    y = within_S_resid(d, S)
    X = np.column_stack([X, np.ones(K)])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    r2 = 1 - ((y - X @ beta) ** 2).sum() / ((y - y.mean()) ** 2).sum()
    return r2, len(feats), K

def tail_test(c, frac=0.01):
    """Compare the frac-smallest-realizer words with the rest, at matched S."""
    d = c["delta"]; S = c["S"]; K = len(d)
    logr = (S + 1) - d
    feats = [k for k in sorted(c) if k not in SKIP and k != "S"]
    k = max(20, int(frac * K))
    sel = np.argsort(logr)[:k]
    mask = np.zeros(K, bool); mask[sel] = True
    out = []
    for f in feats:
        z = within_S_resid(c[f], S)            # mean 0, sd 1 within each S
        m1 = z[mask].mean(); m0 = z[~mask].mean()
        se = math.sqrt(1.0 / mask.sum() + 1.0 / (~mask).sum())
        out.append((abs((m1 - m0) / se), (m1 - m0) / se, f))
    out.sort(reverse=True)
    # the S-marginal itself: is the tail's S smaller than generic?  (expected: yes)
    dS = (S[mask].mean() - S.mean()) / (S.std() / math.sqrt(mask.sum()))
    return out, k, dS

def main():
    files = sorted(glob.glob("results/words/*.csv"),
                   key=lambda s: (s.split('/')[-1].split('_')[0], int(s.split('_n')[1][:-4])))
    print("M3b(1)  multivariate R^2 of within-S delta on ALL word features")
    print(f"{'dataset':12s} {'p':>4} {'K':>7} {'R2':>9} {'null p/K':>10} {'ratio':>7}")
    for path in files:
        c = load(path); r2, p, K = multi_r2(c)
        print(f"{os.path.basename(path)[:-4]:12s} {p:>4} {K:>7} {r2:>9.5f} "
              f"{p/K:>10.5f} {r2/(p/K):>7.2f}")
    print()
    print("M3b(2)  the 1% smallest realizers vs the rest, features standardised")
    print("        within each S-stratum.  Null: every t = 0.  |t| > 4 flagged.")
    print(f"{'dataset':12s} {'k':>5} {'t(S)':>8}   top-4 |t| features")
    for path in files:
        c = load(path); out, k, dS = tail_test(c)
        flag = sum(1 for a, _, _ in out if a > 4)
        s = "  ".join(f"{f}={t:+.2f}" for _, t, f in out[:4])
        print(f"{os.path.basename(path)[:-4]:12s} {k:>5} {dS:>8.2f}   {s}   [#|t|>4: {flag}]")

if __name__ == "__main__":
    main()
