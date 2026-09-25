"""M1 - the lambda grid.

E(B,n) = #{odd m < 2^B : n-confined} / (2^{B-1} p_n(0)),  exact numerator,
exact denominator.  Pre-registered: E == 1 identically for A[n]+1 <= B.
"""
import os, sys, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction
from eoc import Map
from words import Table

def grid(tag, mp, Bmax, ns):
    d = json.load(open(f"results/scan_{tag}/merged.json"))
    H = {}
    for k, v in d["H"].items():
        b, n = map(int, k.split(",")); H[(b, n)] = v
    Nmax = max(n for (_, n) in H)
    tabs = {n: Table(mp, n) for n in ns if n <= Nmax}
    rows = []
    for B in range(8, Bmax + 1):
        for n in ns:
            if n not in tabs: continue
            cnt = sum(H.get((b, n), 0) for b in range(1, B + 1))
            p = tabs[n].p()
            exp = Fraction(1 << (B - 1)) * p
            rows.append(dict(B=B, n=n, lam=n / B, cnt=cnt, exp=float(exp),
                             E=(float(Fraction(cnt) / exp) if exp > 0 else None),
                             exact_one=(mp.A(n) + 1 <= B),
                             unique=(n >= B - 1)))
    return rows

if __name__ == "__main__":
    mp = Map(3, 1)
    ns = [1,2,3,4,5,6,8,10,12,14,16,20,24,28,32,40,50,60,70,80,100,120,140,160,180,200,220,250,280]
    rows = grid("A32", mp, 32, ns)
    json.dump(rows, open("results/m1_lambda_grid.json", "w"))
    # (a) the pre-registered identity
    viol = [r for r in rows if r["exact_one"] and r["cnt"] > 0 and abs(r["E"] - 1) > 1e-12]
    print(f"M1a  E(B,n) == 1 exactly whenever A[n]+1 <= B :  "
          f"{len(viol)} violations out of "
          f"{sum(1 for r in rows if r['exact_one'])} cells")
    # exactness also as integers
    bad = 0
    for r in rows:
        if r["exact_one"]:
            p = Table(mp, r["n"]).p()
            if Fraction(r["cnt"]) != Fraction(1 << (r["B"] - 1)) * p: bad += 1
    print(f"M1a' integer check: {bad} mismatches")
    print()
    print("M1b  E(B,n) by lambda = n/B  (3x+1, complete scan of odd m < 2^B)")
    print(f"{'B':>3} {'n':>4} {'lam':>6} {'count':>12} {'expected':>14} {'E':>8}  regime")
    for r in rows:
        if r["cnt"] == 0 and r["exp"] < 0.05: continue
        if r["lam"] < 0.5: continue
        reg = "vacuous" if r["exact_one"] else ("unique" if r["unique"] else "mixed")
        print(f"{r['B']:>3} {r['n']:>4} {r['lam']:>6.3f} {r['cnt']:>12} {r['exp']:>14.4f} "
              f"{r['E']:>8.4f}  {reg}")
