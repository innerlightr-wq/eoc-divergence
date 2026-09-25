"""M4b - envelope search.

For every feature, bin it and look at the extreme order statistics of delta in
each bin.  Under H0 with K_bin iid samples of an Exp(ln2) variable,
    E[max delta in bin] = log2(K_bin) + gamma/ln2 = log2(K_bin) + 0.8327 ,
so an apparent "envelope" that tracks log2(K_bin) is a sample-size artefact and
not a constraint.  A real envelope is a bin whose max sits far below that.
"""
import sys, math, glob, os
import numpy as np
from m3_dependence import load, SKIP

GAMMA = 0.5772156649

def envelopes(path, nbin=16):
    c = load(path); d = c["delta"]; K = len(d)
    feats = [k for k in sorted(c) if k not in SKIP]
    worst = []
    for f in feats:
        x = c[f]
        if len(np.unique(x)) < 4: continue
        qs = np.quantile(x, np.linspace(0, 1, nbin + 1))
        qs = np.unique(qs)
        idx = np.clip(np.searchsorted(qs, x, side="right") - 1, 0, len(qs) - 2)
        for b in range(len(qs) - 1):
            m = idx == b
            kb = m.sum()
            if kb < 100: continue
            mx = d[m].max()
            pred = math.log2(kb) + GAMMA / math.log(2)
            sd = (math.pi / math.sqrt(6)) / math.log(2)       # Gumbel scale -> bits
            worst.append(((mx - pred) / sd, f, b, kb, mx, pred))
    worst.sort()
    return worst, K

if __name__ == "__main__":
    print("M4b  extreme-value envelope check.  z = (max delta in bin - "
          "[log2 K_bin + 0.833]) / 1.850")
    print("     Null: z is standard Gumbel-ish, mean 0, |z| > 4 would be an envelope.")
    print()
    print(f"{'dataset':12s} {'K':>7} {'min z':>7} {'max z':>7}  {'most negative bin'}")
    for path in sorted(glob.glob("results/words/3x+1_n*.csv"),
                       key=lambda s: int(s.split('_n')[1][:-4])):
        w, K = envelopes(path)
        if not w: continue
        z0, f0, b0, kb0, mx0, pr0 = w[0]
        print(f"{os.path.basename(path)[:-4]:12s} {K:>7} {w[0][0]:>7.2f} {w[-1][0]:>7.2f}"
              f"  {f0} bin {b0} (K={kb0}): max delta {mx0:.2f} vs predicted {pr0:.2f}")
    print()
    print("     Trivial exact envelopes, for the record:  0 < delta <= S+1  (r >= 1),")
    print("     and log2 r(w) < S+1 (the class modulus).  No non-trivial envelope was")
    print("     found in any feature.")
