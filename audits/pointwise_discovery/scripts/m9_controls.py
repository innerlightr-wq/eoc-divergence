"""M9 - the same exact letter-law test on the control maps.

 * 3x-1  is the SIGN control: m -> -m conjugates it to 3x+1 on the negatives,
   and it has positive rare-side cycles ({1}, {5,7}, {17,...}).  A positive
   fraction of its confined integers is therefore CAPTURED by a cycle, whose
   deep letters follow the cycle word and not the generic confined law.
   This is a known effect that the test MUST detect - it is the power
   calibration for the whole pipeline.
 * 5x-1  is the structural twin of 3x+1: same sign misalignment, opposite drift,
   and no positive rare-side cycle.  It should behave like 3x+1: null.
"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from eoc import Map, word_of
from m4d_strata import cohort
from m7_exact_letter_law import exact_letter_law

def test(mp, scan, n, rootfilter):
    law = exact_letter_law(mp, n, list(range(n)), dmax=40)
    Pbar = {d: float(sum(law[k][d] for k in range(n)) / n) for d in range(1, 10)}
    Pbar[10] = float(sum(sum(law[k][d] for d in range(10, 41)) for k in range(n)) / n)
    ms = cohort(scan, n)
    if rootfilter: ms = [m for m in ms if m % 3 != 2]
    W = np.array([[min(a, 10) for a in word_of(mp, m, n)] for m in ms], dtype=np.int8)
    K = len(W)
    counts = np.stack([(W == d).sum(1) for d in range(1, 11)], 1).astype(float)
    obs = counts.sum(0) / (K * n)
    rng = np.random.default_rng(7)
    boots = np.stack([counts[rng.integers(0, K, K)].sum(0) / (K * n) for _ in range(400)])
    se = boots.std(0)
    z = [(obs[i] - Pbar[i + 1]) / se[i] if se[i] > 0 else 0.0 for i in range(10)]
    return K, Pbar, obs, se, z

if __name__ == "__main__":
    print(__doc__.strip()); print()
    jobs = [("3x-1 (sign control, cycles present)", Map(3, -1), "results/scan_B32deep", 140),
            ("5x-1 (structural twin of 3x+1)",      Map(5, -1), "results/scan_E32deep", 140)]
    for label, mp, scan, n in jobs:
        K, Pbar, obs, se, z = test(mp, scan, n, rootfilter=False)
        print(f"{label}:  {K} integers < 2^32, {n}-persistent")
        print(f"   {'d':>3} {'exact Pbar':>13} {'observed':>12} {'boot SE':>10} {'z':>9}")
        for i, d in enumerate(range(1, 11)):
            print(f"   {d:>3} {Pbar[d]:>13.7f} {obs[i]:>12.7f} {se[i]:>10.7f} {z[i]:>9.2f}")
        print(f"   max |z| = {max(abs(t) for t in z):.2f}")
        print()
