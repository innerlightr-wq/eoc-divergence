"""M1b - per-bitlength (disjoint) occupancy against the exact word mass,
with the known L1/L2 chain mechanism residualized by restricting to chain roots.

  E_b(n)      = H[b][n]      / (2^{b-2} p_n)
  E^root_b(n) = R[b][n]      / ((2/3) 2^{b-2} p_n)     (q_n = (2/3) p_n, PROVED)

Populations at different b are disjoint, so the cells are independent up to the
(real) dependence induced by the chains themselves.
"""
import os, sys, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction
from eoc import Map
from words import Table

def load(tag):
    d = json.load(open(f"results/scan_{tag}/merged.json"))
    H = {tuple(map(int, k.split(","))): v for k, v in d["H"].items()}
    R = {tuple(map(int, k.split(","))): v for k, v in d["R"].items()}
    L = {int(k): v for k, v in d["L"].items()}
    return H, R, L, d.get("guard", 0)

def run(tag, mp, ns, bmax, out):
    H, R, L, guard = load(tag)
    tabs = {n: Table(mp, n) for n in ns}
    rows = []
    for b in range(4, bmax + 1):
        for n in ns:
            p = tabs[n].p()
            exp = Fraction(1 << (b - 2)) * p
            if exp == 0: continue
            cnt = H.get((b, n), 0); cr = R.get((b, n), 0)
            rows.append(dict(b=b, n=n, lam=n / b, cnt=cnt, exp=float(exp),
                             E=cnt / float(exp),
                             cnt_root=cr, exp_root=float(exp) * 2 / 3,
                             Eroot=cr / (float(exp) * 2 / 3),
                             logrmin=(math.log2(L[n]) if n in L else None)))
    json.dump({"rows": rows, "guard": guard}, open(out, "w"))
    return rows, L, guard

if __name__ == "__main__":
    mp = Map(3, 1)
    ns = [10,14,20,24,28,32,40,50,60,70,80,100,120,140,160,180,200,220,240,260]
    rows, L, guard = run("A32", mp, ns, 32, "results/m1b_bitlength.json")
    print(f"guard hits (overflow, would make depths lower bounds): {guard}")
    print()
    print("Per-bitlength occupancy.  ALL = full population, ROOT = chain roots only.")
    print(f"{'n':>4} {'lam@b':>6} {'b':>3} {'obs':>10} {'exp':>12} {'E':>7} {'+-':>6} "
          f"{'Eroot':>7} {'lg rmin':>8}")
    for n in ns:
        sel = [r for r in rows if r["n"] == n and r["exp"] >= 25]
        for r in sel:
            sd = 1 / math.sqrt(r["exp"])
            print(f"{n:>4} {r['lam']:>6.2f} {r['b']:>3} {r['cnt']:>10} {r['exp']:>12.1f} "
                  f"{r['E']:>7.4f} {sd:>6.4f} {r['Eroot']:>7.4f} "
                  f"{(r['logrmin'] or 0):>8.2f}")
        if sel: print()
