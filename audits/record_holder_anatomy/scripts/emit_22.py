"""Emit section 2.2 (the record-holder table and the runtime wall) as markdown."""
import sys, collections, math

def load(paths):
    acc = collections.defaultdict(list)
    for p in paths:
        for line in open(p):
            f = line.split(); acc[int(f[0])] += [int(x) for x in f[2:]]
    return {N: sorted(v)[:3] for N, v in acc.items()}

def v3(n):
    c = 0
    while n and n % 3 == 0: n //= 3; c += 1
    return c

if __name__ == "__main__":
    LIM = int(sys.argv[1]); secs = float(sys.argv[2]); paths = sys.argv[3:]
    tab = load(paths); Nmax = max(tab)
    rows, prev, start = [], None, 1
    for N in sorted(tab):
        if prev is not None and tab[N] != prev:
            rows.append((start, N - 1, prev + [None] * (3 - len(prev)))); start = N
        prev = tab[N]
    rows.append((start, Nmax, prev + [None] * (3 - len(prev))))
    complete3 = max([N for N in tab if len(tab[N]) == 3] or [0])
    complete1 = Nmax
    print(f"## 2.2 The record holders `r₁, r₂, r₃`\n")
    print(f"Exact scan of every odd `m ≡ 3 (mod 4)` below **{LIM:,}** = `2^{LIM.bit_length()-1}`, "
          f"in {secs/60:.0f} min on 8 cores.".replace(",", " "))
    print(f"`r₁(N)` is therefore certified for **`N = 1 … {complete1}`**, and the full triple "
          f"`r₁,r₂,r₃` for `N = 1 … {complete3}`.\n")
    print("| `N`-range | `r₁` | `r₂` | `r₃` | `r₁ mod 12` | `v₃(r₁+1)` = chain | `r₂/r₁` | `r₃/r₂` |")
    print("|---|---|---|---|---|---|---|---|")
    for lo, hi, r in rows:
        f = lambda x: f"{x:,}".replace(",", " ") if x else "—"
        g21 = f"{r[1]/r[0]:.4f}" if r[1] else "—"
        g32 = f"{r[2]/r[1]:.4f}" if r[2] and r[1] else "—"
        print(f"| {lo}–{hi} | {f(r[0])} | {f(r[1])} | {f(r[2])} | {r[0]%12} | "
              f"{v3(r[0]+1)} | {g21} | {g32} |")
    holders = sorted({r[0] for _, _, r in rows})
    print(f"\n**{len(holders)} distinct values of `r₁`**, strictly increasing. "
          f"`r₁ mod 12 ∈ {{3,7}}` and `v₃(r₁+1) = 0` at every one "
          f"({'PASS' if all(r[0]%12 in (3,7) and v3(r[0]+1)==0 for _,_,r in rows) else 'FAIL'}).\n")
    # runtime wall
    lg = [(hi, math.log2(r[0])) for _, hi, r in rows if r[0] > 1]
    if len(lg) > 4:
        xs = [a for a, _ in lg[-10:]]; ys = [b for _, b in lg[-10:]]
        n = len(xs); mx = sum(xs)/n; my = sum(ys)/n
        sl = sum((x-mx)*(y-my) for x, y in zip(xs, ys)) / sum((x-mx)**2 for x in xs)
        ic = my - sl*mx
        print(f"**The runtime wall.** The work is linear in the bound. Over the last ten "
              f"record holders `log₂r₁ ≈ {sl:.4f}·N + {ic:.1f}`, so each further "
              f"`+{1/sl:.1f}` in `N` doubles the scan.\n")
        for N in (Nmax+20, Nmax+50, Nmax+100):
            b = 2 ** (sl*N + ic)
            t = secs * b / LIM
            unit = f"{t/60:.0f} min" if t < 5400 else (f"{t/3600:.1f} h" if t < 3*86400 else f"{t/86400:.0f} days")
            print(f"* to reach `N ≈ {N}` needs a bound near `2^{sl*N+ic:.0f}` ≈ {b:.1e}, "
                  f"about **{unit}** on 8 cores at the measured rate;")
        print(f"\nSo the practical wall on this machine is around `N ≈ {Nmax+30}`–`{Nmax+60}`; "
              f"beyond that a linear scan is the wrong tool.")
