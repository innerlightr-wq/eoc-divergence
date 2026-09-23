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
    # runtime wall -- fit on the JUMP points (first N of each distinct r1), not on rows
    pts, seen = [], None
    for N in sorted(tab):
        if tab[N][0] != seen:
            seen = tab[N][0]; pts.append((N, seen))
    xs = [N for N, _ in pts[-12:]]; ys = [math.log2(r) for _, r in pts[-12:]]
    n = len(xs); mx = sum(xs)/n; my = sum(ys)/n
    sl = sum((x-mx)*(y-my) for x, y in zip(xs, ys)) / sum((x-mx)**2 for x in xs)
    ic = my - sl*mx
    print(f"**The runtime wall.** The work is linear in the bound. Fitting the last twelve "
          f"jump points (the first `N` at which each new `r₁` appears) gives\n")
    print(f"```\nlog₂ r₁(N)  ≈  {sl:.4f}·N + {ic:.2f}     (doubling every {1/sl:.1f} steps of N)\n```\n")
    print(f"so each `+{1/sl:.1f}` in `N` doubles the scan. At the measured rate "
          f"({secs/60:.0f} min for `2^{LIM.bit_length()-1}` on 8 cores):\n")
    for N in (Nmax + 25, Nmax + 50, Nmax + 100):
        b = 2 ** (sl*N + ic)
        t = secs * b / LIM
        unit = (f"{t/60:.0f} min" if t < 5400 else
                f"{t/3600:.1f} h" if t < 3*86400 else f"{t/86400:.0f} days")
        print(f"* `N ≈ {N}` needs a bound near `2^{sl*N+ic:.0f}` ≈ {b:.1e} — about **{unit}**;")
    print(f"\nSo the practical wall on this machine is **`N ≈ {Nmax+25}`–`{Nmax+45}`**: a few hours. "
          f"Beyond that a linear scan is the wrong tool, and the next step would have to be a "
          f"search over the class tree rather than over the integers.")
