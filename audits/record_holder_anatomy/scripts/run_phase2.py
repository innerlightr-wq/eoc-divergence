"""Phase 2 driver: record-holder data + M1 on the record holders and every control.
Exact arithmetic; floats only in printed columns."""
import sys, random, collections
from fractions import Fraction
from anatomy import A, acc_orbit, conf_depth, minrep, parity_word
from m1 import repetitions, profile
from controls import (sturmian_valuations, sturmian_realizers, random_confined_word,
                      shuffled_surrogate, acc_orbit_minus, parity_word_minus, M_minus)

def v3(n):
    c = 0
    while n % 3 == 0 and n: n //= 3; c += 1
    return c

def load(paths):
    acc = collections.defaultdict(list)
    for p in paths:
        for line in open(p):
            f = line.split(); N = int(f[0]); acc[N] += [int(x) for x in f[2:]]
    return {N: sorted(v)[:3] for N, v in acc.items()}

def banner(t): print("\n" + "=" * 96 + f"\n{t}\n" + "=" * 96)

if __name__ == "__main__":
    tab = load(sys.argv[1:])
    Nmax = max(tab)

    banner("PHASE 2.1  record holders r1, r2, r3  (exact scan; see scan.c for the method)")
    print(f"depths reached: 1..{Nmax}")
    print(f"{'N-range':>13} {'r1':>15} {'r2':>15} {'r3':>15} {'r1%12':>6} "
          f"{'v3(r1+1)':>9} {'chain':>6} {'r2/r1':>8} {'r3/r2':>8}")
    prev, start = None, 1
    rows = []
    for N in sorted(tab):
        row = tab[N]
        if prev is not None and row != prev:
            rows.append((start, N - 1, prev + [None] * (3 - len(prev)))); start = N
        prev = row
    rows.append((start, Nmax, prev + [None] * (3 - len(prev))))
    for lo, hi, r in rows:
        g21 = f"{r[1]/r[0]:.4f}" if r[1] else "-"
        g32 = f"{r[2]/r[1]:.4f}" if r[2] and r[1] else "-"
        print(f"{f'{lo}-{hi}':>13} {r[0]:>15} {str(r[1] or '-'):>15} {str(r[2] or '-'):>15}"
              f" {r[0]%12:>6} {v3(r[0]+1):>9} {v3(r[0]+1):>6} {g21:>8} {g32:>8}")
    bad12 = [r[0] for _, _, r in rows if r[0] % 12 not in (3, 7)]
    print(f"\nL4 (r1 = 3 or 7 mod 12): {'PASS' if not bad12 else 'FAIL ' + str(bad12)}")
    print(f"L4 read through L2 (v3(r1+1) = 0, i.e. no backward d=1 chain): "
          f"{'PASS' if all(v3(r[0]+1)==0 for _,_,r in rows) else 'FAIL'}")
    bad12b = [r[1] for _,_,r in rows if r[1] and r[1] % 12 not in (3,7)]
    print(f"does L4 extend to r2?  r2 mod 12 in {{3,7}}: "
          f"{'yes for all' if not bad12b else f'NO -- {len(bad12b)} exceptions, e.g. {bad12b[:4]}'}")
    bad12c = [r[2] for _,_,r in rows if r[2] and r[2] % 12 not in (3,7)]
    print(f"                      r3 mod 12 in {{3,7}}: "
          f"{'yes for all' if not bad12c else f'NO -- {len(bad12c)} exceptions, e.g. {bad12c[:4]}'}")

    holders = sorted({r[0] for _, _, r in rows})
    banner("PHASE 2.2  M1 -- square-poorness, exact, with the per-block ceiling")
    print("Q = l*(e - max(1,theta_W)) in bits, maximised over all initial repetitions at every")
    print("step of the confined run; the ceiling says Q <= log2|m_k| + O(log l) for BALANCED")
    print("blocks.  `slack` is the worst (rhs - R) over all rows; a balanced row with slack < 0")
    print("or a failed isometry check is a violation.\n")
    hdr = (f"{'object':>26} {'depth':>6} {'log2 m':>7} {'sq/2':>5} {'rep':>5} "
           f"{'Qmax':>5} {'log2 m_k':>9} {'headroom':>9} {'reps':>6} {'viol':>5}")
    print(hdr)
    def show(name, m, cap=4000, maxsteps=None):
        p = profile(m, cap, maxsteps)
        at = p['Qat']
        lg = (abs(at[1]).bit_length() - 1) if at else None
        head = (lg - p['Qmax']) if (at and p['Qmax'] is not None) else None
        print(f"{name:>26} {p['depth']:>6} {p['log2m']:>7} {p['longest_square_half']:>5} "
              f"{p['longest_rep']:>5} {str(p['Qmax']):>5} {str(lg):>9} {str(head):>9} "
              f"{p['n_reps']:>6} {len(p['violations']):>5}")
        return p
    allviol = []
    for m in holders:
        allviol += show(f"r1 = {m}", m, maxsteps=260)['violations']

    banner("PHASE 2.3  controls")
    print(hdr)
    # C1: the negative zero-confined cycles and small preimages
    for m in (-1, -5, -7, -17, -25, -91):
        allviol += show(f"C1 cycle {m}", m, cap=240, maxsteps=120)['violations']
    for m in (-3, -11, -43):          # d>=3 preimages of -1: NOT confined (L3)
        print(f"{f'C1 preimage {m}':>26} {conf_depth(m,240):>6} "
              f"{abs(m).bit_length()-1:>7}   (L3: only d=1 preserves confinement backward)")
    # C2: the critical Sturmian edge
    d = sturmian_valuations(64)
    print()
    for N in (10, 20, 30, 40, 50, 60):
        r, S, mk = minrep(d[:N])
        print(f"{f'C2 Sturmian r(D_{N})':>26} {conf_depth(r, 400):>6} "
              f"{r.bit_length()-1:>7}   S_N = {S:<4} modulus 2^{S+1}  "
              f"realizer/modulus = 2^{r.bit_length()-1-S-1}")
    for N in (20, 30, 40):
        r, _, _ = minrep(d[:N])
        allviol += show(f"C2 Sturmian r(D_{N})", r, cap=400, maxsteps=N)['violations']
    # C3: random confined words and shuffled surrogates
    rng = random.Random(20260923)
    print()
    for N in (40, 80, 160):
        rs = []
        for _ in range(12):
            w = random_confined_word(N, rng)
            if w: rs.append(minrep(w)[0])
        rs.sort()
        print(f"{f'C3 random word N={N}':>26} {'':>6} "
              f"median log2 r = {rs[len(rs)//2].bit_length()-1:<5} "
              f"min = 2^{rs[0].bit_length()-1}  max = 2^{rs[-1].bit_length()-1}  (12 draws)")
        allviol += show(f"C3 random N={N} (median)", rs[len(rs)//2], cap=400, maxsteps=N)['violations']
    for m in holders[-3:]:
        dep, orows = acc_orbit(m)
        w = [dd for _, dd, _ in orows[:dep]]
        sw = shuffled_surrogate(w, rng)
        if sw:
            r = minrep(sw)[0]
            print(f"{f'C3 shuffle of {m}':>26} {'':>6} log2 r = {r.bit_length()-1:<5} "
                  f"vs log2 r1 = {m.bit_length()-1}  (same multiset of valuations)")
            allviol += show(f"C3 shuffled({m})", r, cap=400, maxsteps=dep)['violations']

    banner("PHASE 2.4  violations of the M1 ceiling by a BALANCED block")
    bal = [v for v in allviol if v[2].get('balanced') and (v[2].get('slack') or 0) < 0]
    iso = [v for v in allviol if not v[2].get('isometry_ok', True)]
    print(f"balanced blocks with negative slack: {len(bal)}")
    print(f"isometry check v2(M) = R failures:   {len(iso)}")
    if bal: print("  STOP -- first:", bal[0])
    if iso: print("  STOP -- first:", iso[0])
    print(f"other flagged rows (unbalanced, or periodic-to-horizon): {len(allviol)-len(bal)-len(iso)}")
