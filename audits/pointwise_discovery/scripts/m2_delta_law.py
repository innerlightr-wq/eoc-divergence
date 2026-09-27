"""M2 - the marginal law of the realizer deficit  delta(w) = S+1 - log2 r(w).

Null H0:  P(delta > t) = 2^{-t},  mean delta = 1/ln2 = 1.442695.
"""
import sys, math, glob, os
import numpy as np

def load(path):
    import csv
    rows = list(csv.DictReader(open(path)))
    cols = {k: np.array([float(r[k]) for r in rows]) for k in rows[0]}
    return cols

def main():
    print("M2  marginal law of delta = S+1-log2 r(w), sampled exactly from the")
    print("    dyadic law on rare-side words.   Null: P(delta>t) = 2^-t, mean = 1.442695")
    print()
    ts = [1, 2, 3, 4, 6, 8, 10]
    hdr = f"{'map':>6} {'n':>4} {'K':>6} {'mean':>8} {'null':>8} " + \
          " ".join(f"P>{t}".rjust(9) for t in ts)
    for f in sorted(glob.glob("results/words/*.csv"),
                    key=lambda s: (s.split('/')[-1].split('_')[0], int(s.split('_n')[1][:-4]))):
        name = os.path.basename(f)[:-4]
        mp, n = name.split("_n"); n = int(n)
        c = load(f)
        d = c["delta"]; K = len(d)
        if mp == "3x+1" and n == 20: print(hdr)
        line = f"{mp:>6} {n:>4} {K:>6} {d.mean():>8.4f} {1/math.log(2):>8.4f} "
        for t in ts:
            emp = (d > t).mean(); null = 2.0 ** -t
            se = math.sqrt(max(null*(1-null), 1e-12) / K)
            z = (emp - null) / se if se > 0 else 0
            line += f"{emp:>6.4f}{'*' if abs(z) > 4 else ' '}{'':>2}"
        print(line)
    print()
    print("  '*' marks |z| > 4 against the null (binomial, independent-sample SE).")

if __name__ == "__main__":
    main()
