"""Exact admissible-word counterexamples to the invalid implications A..G.

A. S_N <= alpha N for all N              (zero confinement, Delta_N >= 0)
B. liminf ordinary odd density >= beta
C. liminf ordinary odd density = beta
D. liminf Delta_N / N = 0
E. Delta_N = o(N)
F. Delta_N = O(log N)
G. Delta_N bounded

Confinement is decided EXACTLY by 2^{S_j} <= 3^j on integers; Delta_j is only
printed.  Every word below has all letters >= 1, so it is an admissible
valuation word (realizability as a positive-integer orbit is a separate
question -- see COUNTEREXAMPLES.md section 4).
"""
import math
alpha = math.log2(3)


def report(name, d, skip=50):
    S, Ss = 0, []
    for dj in d:
        S += dj; Ss.append(S)
    N = len(d)
    conf = all((1 << S) <= 3 ** (j + 1) for j, S in enumerate(Ss))
    De = [alpha * (j + 1) - S for j, S in enumerate(Ss)]
    rat = [De[j] / (j + 1) for j in range(skip, N)]
    lgr = [De[j] / math.log2(j + 2) for j in range(skip, N)]
    print(f"  {name}")
    print(f"     N={N}  0-confined (exact) = {conf}   min Delta = {min(De):.4f}")
    print(f"     Delta_N/N      : liminf {min(rat):.6f}   limsup {max(rat):.6f}")
    print(f"     Delta_N/log2 N : max {max(lgr):.3f}      max Delta_N = {max(De):.2f}")
    return conf, min(rat), max(rat), max(lgr)


print("=== W1: all ones.  A holds, Delta grows LINEARLY. ===")
report("d_j = 1", [1] * 3000)
print("     => A does NOT imply D, E, F or G.  (liminf Delta/N = alpha-1 > 0.)")
print()

print("=== W2: geometric climb/descend stages.  D holds, E FAILS. ===")
def w_D_not_E(target):
    """Climb with d=1 (Delta += alpha-1), descend with d=2 (Delta -= 2-alpha),
    returning to Delta ~ 0 at the end of each stage; stage lengths geometric."""
    d = []
    S = 0
    A = 8
    while len(d) < target:
        n0 = len(d)
        for _ in range(A):                      # climb
            d.append(1); S += 1
        # descend with d=2 while Delta stays >= 0
        while True:
            j = len(d) + 1
            if (1 << (S + 2)) > 3 ** j: break   # would break confinement
            d.append(2); S += 2
        A = int(A * 2.2) + 1
    return d[:target]
report("climb/descend stages", w_D_not_E(6000), skip=200)
print("     => D holds (liminf -> 0) but E FAILS (limsup Delta/N stays positive),")
print("        so D does NOT imply E.  F and G fail a fortiori.")
print()

print("=== W3: Delta_N ~ sqrt(N).  E holds, F FAILS. ===")
def w_E_not_F(target):
    d, S = [], 0
    for j in range(1, target + 1):
        want = alpha * j - math.sqrt(j)
        dj = max(1, int(round(want - S)))
        while (1 << (S + dj)) > 3 ** j and dj > 1: dj -= 1
        d.append(dj); S += dj
    return d
report("Delta ~ sqrt N", w_E_not_F(4000), skip=100)
print("     => E holds but F FAILS, so E does NOT imply F.  In particular")
print("        liminf Delta_N/N = 0 gives NO O(log N) or O(sqrt N) corridor.")
print()

print("=== W4: Delta_N bounded (G).  Exists symbolically. ===")
def w_G(target):
    d, S = [], 0
    for j in range(1, target + 1):
        dj = 2 if (1 << (S + 2)) <= 3 ** j else 1
        d.append(dj); S += dj
    return d
report("greedy d=2 when allowed", w_G(4000), skip=100)
print("     => G holds symbolically (bounded Delta).  This word is NOT excluded")
print("        symbolically; it is excluded for positive-integer orbits by the")
print("        repository's bounded-drift theorems (see PRIOR_DETERMINISTIC_BARRIERS.md).")
print()

print("=== two-clock check on each word: liminf ordinary density vs 1/limsup(S_N/N) ===")
for nm, d in [("W1", [1] * 600), ("W2", w_D_not_E(1200)), ("W3", w_E_not_F(800)),
              ("W4", w_G(800))]:
    bits = []
    for dj in d:
        bits.append(1); bits.extend([0] * (dj - 1))
    h = 0; lo = 9.9; hi = -9.9
    for l, b in enumerate(bits, start=1):
        h += b; lo = min(lo, h / l); hi = max(hi, h / l)
    S = 0; Ss = []
    for dj in d:
        S += dj; Ss.append(S)
    endmin = min((j + 1) / Ss[j] for j in range(len(d)))
    sup = max(Ss[j] / (j + 1) for j in range(len(d)))
    print(f"  {nm}: ordinary liminf h/l = {lo:.9f}   endpoint min N/S_N = {endmin:.9f} "
          f"  1/limsup(S_N/N) = {1/sup:.9f}   equal = {abs(lo-endmin)<1e-12 and abs(lo-1/sup)<1e-12}")
