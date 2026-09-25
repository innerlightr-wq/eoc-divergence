"""M8 - the decisive form of the letter-law test.

Aggregate letter frequency over all depths,  Pbar(d) = (1/n) sum_k P(a_k = d),
computed EXACTLY from the transfer tables, against the chain-root integer
cohort.  The error bar is a word-level bootstrap, so within-word correlation
(which confinement certainly creates) is handled, and chain correlation is
removed by the root restriction.
"""
import os, sys, math, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from fractions import Fraction
from eoc import Map, word_of
from words import Table
from m4d_strata import cohort
from m7_exact_letter_law import exact_letter_law

if __name__ == "__main__":
    mp = Map(3, 1); n = 140
    law = exact_letter_law(mp, n, list(range(n)), dmax=40)
    # d = 1..9 exactly, d = 10 is the lumped tail  a >= 10
    Pbar = {d: float(sum(law[k][d] for k in range(n)) / n) for d in range(1, 10)}
    Pbar[10] = float(sum(sum(law[k][d] for d in range(10, 41)) for k in range(n)) / n)
    ms = cohort("results/scan_A36", n)
    roots = [m for m in ms if m % 3 != 2]
    W = np.array([[min(a, 10) for a in word_of(mp, m, n)] for m in roots], dtype=np.int8)
    K = len(W)
    obs = {d: float((W == d).sum()) / (K * n) for d in range(1, 11)}
    rng = np.random.default_rng(20260925)
    B = 500
    boots = {d: [] for d in range(1, 11)}
    counts = np.stack([(W == d).sum(1) for d in range(1, 11)], 1).astype(float)
    for _ in range(B):
        idx = rng.integers(0, K, K)
        s = counts[idx].sum(0) / (K * n)
        for i, d in enumerate(range(1, 11)): boots[d].append(s[i])
    print(__doc__.strip()); print()
    print(f"chain-root cohort: {K} words of length {n}, every odd m < 2^36 that is")
    print(f"{n}-confined with 3 not dividing m+1.  Word-level bootstrap, B = {B}.")
    print()
    print(f"{'d':>3} {'exact Pbar(d)':>15} {'observed':>12} {'boot SE':>10} {'z':>8}")
    zs = []
    for d in range(1, 11):
        se = float(np.std(boots[d]))
        z = (obs[d] - Pbar[d]) / se if se > 0 else 0.0
        zs.append(z)
        print(f"{d:>3} {Pbar[d]:>15.7f} {obs[d]:>12.7f} {se:>10.7f} {z:>8.2f}")
    print()
    print(f"max |z| = {max(abs(z) for z in zs):.2f} over 10 letter values.")
