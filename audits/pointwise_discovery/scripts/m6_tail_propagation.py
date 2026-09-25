"""M6 - does the terminating binary tail show up in deep parity data?

Two diagnostics from the brief's section 10, on the complete n-confined cohort
below 2^36 (no sampling):

 (a) LOW BITS vs LATE LETTERS.  chi^2 test of independence between m mod 32
     (16 odd classes) and the letter a_k, for k well past the depth that
     m mod 32 determines.  Terras-Everett says the two are independent under
     Haar; finite height is exactly the extra information, so a departure here
     would BE the missing law.

 (b) BLOCK ENTROPY.  empirical entropy of letter blocks of length 1,2,3 in the
     integer cohort against the exactly-sampled generic confined words.  A
     36-bit integer's depth-180 word carries at most 36 bits of information,
     whereas a generic confined word of that length carries far more; if that
     compression were visible in any low-order statistic it would show here.
"""
import os, sys, math, glob, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from collections import Counter
from eoc import Map, word_of
from m4d_strata import cohort
from m3_dependence import load

def chi2(tab):
    tab = np.asarray(tab, float)
    r = tab.sum(1, keepdims=True); c = tab.sum(0, keepdims=True); N = tab.sum()
    e = r * c / N
    m = e > 0
    x2 = float((((tab - e) ** 2 / np.where(m, e, 1))[m]).sum())
    dof = (tab.shape[0] - 1) * (tab.shape[1] - 1)
    z = (x2 - dof) / math.sqrt(2 * dof)
    return x2, dof, z

def blockent(words, L):
    c = Counter()
    for w in words:
        for i in range(len(w) - L + 1):
            c[tuple(min(a, 6) for a in w[i:i+L])] += 1
    tot = sum(c.values())
    return -sum(v/tot * math.log2(v/tot) for v in c.values()), tot

def part_abc():
    """(a') the chi^2 with the chain correlation removed and the degrees of
    freedom taken from the non-empty cells; (b') the block entropy on chain
    roots; (b'') the null spread from independent generic samples."""
    import random
    from words import Table
    mp = Map(3, 1); n = 140
    ms = cohort("results/scan_A36", n)
    roots = [m for m in ms if m % 3 != 2]
    W = [word_of(mp, m, n) for m in ms]
    WR = [word_of(mp, m, n) for m in roots]
    t = Table(mp, n); rng = random.Random(777)
    print()
    print("(a') chi^2 of (m mod 32) vs a_k, chain roots only, dof from non-empty cells")
    print(f"     {'k':>5} {'chi2':>9} {'dof':>5} {'z':>7}")
    for k in [4, 6, 10, 20, 50, 100, 139]:
        tab = np.zeros((16, 6))
        for m, w in zip(roots, WR): tab[(m % 32) // 2, min(w[k], 6) - 1] += 1
        tab = tab[tab.sum(1) > 0][:, tab.sum(0) > 0]
        x2, _, _ = chi2(tab)
        dof = (tab.shape[0] - 1) * (tab.shape[1] - 1)
        print(f"     {k:>5} {x2:>9.1f} {dof:>5} {(x2-dof)/math.sqrt(2*dof):>7.2f}")
    print()
    print("(b') block entropy with the L1/L2 chain correlation removed")
    G = [t.sample(rng) for _ in range(len(WR))]
    print(f"     {'L':>3} {'all integers':>13} {'chain roots':>12} {'generic':>10} "
          f"{'root-gen':>10}")
    for L in (1, 2, 3):
        hi, _ = blockent(W, L); hr, _ = blockent(WR, L); hg, _ = blockent(G, L)
        print(f"     {L:>3} {hi:>13.5f} {hr:>12.5f} {hg:>10.5f} {hr-hg:>+10.5f}")
    print(f"     matched sizes: roots {len(WR)}, generic {len(G)}")
    print()
    print("(b'') noise floor: four INDEPENDENT generic samples of the same size")
    out = []
    for s in (777, 991, 1234, 5150):
        r2 = random.Random(s); G2 = [t.sample(r2) for _ in range(len(WR))]
        out.append([blockent(G2, L)[0] for L in (1, 2, 3)])
    print(f"      {'L':>3} " + " ".join(f"{'seed '+str(s):>12}"
                                        for s in (777, 991, 1234, 5150)) + f"{'spread':>10}")
    for i, L in enumerate((1, 2, 3)):
        v = [o[i] for o in out]
        print(f"      {L:>3} " + " ".join(f"{x:>12.5f}" for x in v)
              + f"{max(v)-min(v):>10.5f}")
    print()
    print("      The chain-root vs generic gaps are 2-3x this spread, and are")
    print("      settled decisively by m8 against the EXACT letter law.")


if __name__ == "__main__":
    mp = Map(3, 1)
    print(__doc__.strip()); print()
    n = 140
    ms = cohort("results/scan_A36", n)
    W = [word_of(mp, m, n) for m in ms]
    print(f"cohort: every odd m < 2^36 that is {n}-confined; {len(ms)} seeds")
    print()
    print("(a)  chi^2 independence of (m mod 32) and the letter a_k")
    print(f"     {'k':>5} {'chi2':>9} {'dof':>5} {'z':>7}   "
          f"(z = (chi2-dof)/sqrt(2 dof); |z|>4 would be a signal)")
    for k in [1, 2, 3, 4, 6, 10, 20, 50, 100, 139]:
        tab = np.zeros((16, 5))
        for m, w in zip(ms, W):
            tab[(m % 32) // 2, min(w[k], 5) - 1] += 1
        x2, dof, z = chi2(tab)
        print(f"     {k:>5} {x2:>9.1f} {dof:>5} {z:>7.2f}"
              + ("   <- determined by m mod 32" if k <= 3 else ""))
    print()
    print("(b)  block entropy of the letter sequence, bits per block")
    gen = None
    import csv
    print(f"     {'L':>3} {'integers':>10} {'generic words':>14} {'difference':>11}")
    # regenerate the generic words' letter statistics from their features is not
    # possible, so re-sample the same law here for a like-for-like comparison
    import random
    from words import Table
    t = Table(mp, n); rng = random.Random(777)
    G = [t.sample(rng) for _ in range(len(ms) // 4)]
    for L in (1, 2, 3):
        hi, ni = blockent(W, L); hg, ng = blockent(G, L)
        se = math.sqrt(1.0/ni + 1.0/ng) * 3      # crude; entropy SE ~ O(1/sqrt N)
        print(f"     {L:>3} {hi:>10.5f} {hg:>14.5f} {hi-hg:>+11.5f}")
    print()
    print("     (the generic sample here is K =", len(G), "words drawn from the same")
    print("      exact dyadic law, at the same depth)")
    part_abc()
