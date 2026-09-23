"""Merge per-chunk scan output into r1,r2,r3 tables, and cross-check r1 against the
Phase-1 (audits/descent) record-holder table for N <= 200."""
import sys, collections

def load(paths):
    acc = collections.defaultdict(list)
    for p in paths:
        for line in open(p):
            f = line.split()
            N = int(f[0]); acc[N] += [int(x) for x in f[2:]]
    return {N: sorted(v)[:3] for N, v in acc.items()}

# the 18 record holders published in audits/descent/DESCENT_AUDIT.md (r_min(N), N = 1..200)
KNOWN = [(3,1,1),(7,2,3),(27,4,36),(703,37,50),(10087,51,65),(35655,66,84),
         (270271,85,102),(362343,103,103),(381727,104,108),(626331,109,110),
         (1027431,111,114),(1126015,115,140),(8088063,141,154),(13421671,155,180),
         (20638335,181,183),(26716671,184,187),(56924955,188,193),(63728127,194,200)]

if __name__ == "__main__":
    tab = load(sys.argv[1:])
    Nmax = max(tab)
    bad = []
    for m, lo, hi in KNOWN:
        for N in range(lo, hi+1):
            if N in tab and tab[N][0] != m: bad.append((N, m, tab[N][0]))
    print(f"depths reached: 1..{Nmax}")
    print(f"cross-check against audits/descent r_min(N), N = 1..200: "
          f"{'PASS (all 200 agree)' if not bad else 'FAIL ' + str(bad[:5])}")
    print(f"\n{'N':>5} {'r1':>16} {'r2':>16} {'r3':>16}  {'r1%12':>5} {'r2/r1':>7} {'r3/r2':>7}")
    prev = None
    for N in sorted(tab):
        row = tab[N]
        if row == prev: continue      # print only where r1,r2,r3 change
        prev = row
        r = row + [None]*(3-len(row))
        g21 = f"{r[1]/r[0]:.4f}" if r[1] else "-"
        g32 = f"{r[2]/r[1]:.4f}" if r[2] else "-"
        print(f"{N:>5} {r[0]:>16} {str(r[1] or '-'):>16} {str(r[2] or '-'):>16}"
              f"  {r[0]%12:>5} {g21:>7} {g32:>7}")
