"""M9b - attribute the 5x-1 departure: is it cycle capture?

Proposition (5x-1) proves that persistence forces m_n < m_0, so a persistent
orbit is trapped in [1, m_0] and is eventually periodic.  If that is the whole
story, the departure should vanish on the sub-cohort that has NOT yet repeated
a value by depth n.
"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from eoc import Map
from m4d_strata import cohort
from m7_exact_letter_law import exact_letter_law

mp = Map(5, -1); n = 140
law = exact_letter_law(mp, n, list(range(n)), dmax=40)
Pbar = {d: float(sum(law[k][d] for k in range(n)) / n) for d in range(1, 10)}
Pbar[10] = float(sum(sum(law[k][d] for d in range(10, 41)) for k in range(n)) / n)

ms = cohort("results/scan_E32deep", n)
cap, free, maxrat = [], [], []
for m0 in ms:
    x = m0; seen = {x}; w = []; rep = None
    for k in range(n):
        x, a = mp.step(x); w.append(min(a, 10))
        if rep is None and x in seen: rep = k
        seen.add(x)
    (cap if rep is not None else free).append(w)
print(__doc__.strip()); print()
print(f"5x-1, depth {n}, every odd m < 2^32 that is {n}-persistent: {len(ms)} seeds")
print(f"   repeated an orbit value by depth {n}:  {len(cap)}  "
      f"({100*len(cap)/len(ms):.2f} %)")
print(f"   still injective at depth {n}:          {len(free)}")
print()
for label, WW in (("captured", cap), ("not yet captured", free)):
    if len(WW) < 50: 
        print(f"   {label}: too few"); continue
    W = np.array(WW, dtype=np.int8); K = len(W)
    counts = np.stack([(W == d).sum(1) for d in range(1, 11)], 1).astype(float)
    obs = counts.sum(0) / (K * n)
    rng = np.random.default_rng(3)
    se = np.stack([counts[rng.integers(0, K, K)].sum(0)/(K*n) for _ in range(400)]).std(0)
    z = [(obs[i] - Pbar[i+1]) / se[i] if se[i] > 0 else 0.0 for i in range(10)]
    print(f"   {label:18s} K={K:7d}   max |z| vs the exact law = "
          f"{max(abs(t) for t in z):8.2f}")
