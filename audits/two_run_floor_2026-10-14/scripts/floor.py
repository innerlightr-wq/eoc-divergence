"""An unconditional exponential least-realizer floor for the two-run family.

Self-contained: the only input is Theorem D of
  audits/episode_classification_2026-10-14/RUN_ARITHMETIC.md  (sec. 5),
which states that an odd m realizes 1^u q 1^v with both ones-runs maximal iff
     m + 1 = 2^{u+1} A ,  A odd,  Z := 3^{u+1} A  satisfies
     Z == 1 - 2^{q-1}   (mod 2^{q+v})   and   Z != 1 - 2^{q-1}   (mod 2^{q+v+1}) .
Writing n = q+v, those two conditions together say exactly
     Z == c  (mod 2^{n+1}) ,      c := 1 - 2^{q-1} + 2^n ,
since "v2(Z - 1 + 2^{q-1}) = n exactly" is the same as "== 2^n mod 2^{n+1}".
Hence A lies in ONE residue class mod 2^{n+1} and r = 2^{u+1} A* - 1 with A* its
least positive representative.

THEOREM U.  For all u >= 0, q >= 2, v >= 0, with S = u + n:
     (i)  A* >= 1                                  => log2(r+1) >= u+1 ;
     (ii) 3^{u+1}A* > 0 and == c (mod 2^{n+1}) with 0 < c < 2^{n+1}
          => 3^{u+1}A* >= c ;  and q <= n gives 2^{q-1} <= 2^{n-1}, so
             c = 1 - 2^{q-1} + 2^n > 2^{n-1}
          => A* > 2^{n-1}/3^{u+1}  => log2(r+1) > S - (u+1) log2 3 .
(i) increases and (ii) decreases in u, so with b = (u+1)/S
     log2(r+1) >= S * max(b, 1 - b log2 3) >= S/(1 + log2 3) = (log_6 2) S ,
with NO error term and NO digit hypothesis.  log_6 2 = 0.38685280723...

All arithmetic exact; floats are printed diagnostics only.
"""
import math, sys, resource
resource.setrlimit(resource.RLIMIT_AS, (1 << 32, 1 << 32))
alpha = math.log2(3); eps0 = 1/(1+alpha)
fails = []
def chk(c, m):
    print(('PASS  ' if c else 'FAIL  ') + m)
    if not c: fails.append(m)
def v2(x): return (x & -x).bit_length() - 1
def word(m, L):
    d = []; x = m
    for _ in range(L):
        t = 3*x+1; k = v2(t); d.append(k); x = t >> k
    return d
def realizes(m, u, q, v):
    d = word(m, u+v+2)
    return (tuple(d[:u]) == (1,)*u and d[u] == q
            and tuple(d[u+1:u+1+v]) == (1,)*v and d[u+1+v] >= 2)
def Astar(u, q, v):
    n = q+v; Mod = 1 << (n+1); c = 1 - (1 << (q-1)) + (1 << n)
    return (pow(pow(3, u+1, Mod), -1, Mod) * (c % Mod)) % Mod, n, c

print("="*88); print("the single class mod 2^{n+1}, and r = 2^{u+1} A* - 1"); print("="*88)
bad = 0; tested = 0
for u in range(0, 6):
    for q in range(2, 6):
        for v in range(0, 5):
            A, n, c = Astar(u, q, v); r = (1 << (u+1))*A - 1
            if not realizes(r, u, q, v): bad += 1
            if next((y for y in range(1, r+2, 2) if realizes(y, u, q, v)), None) != r: bad += 1
            tested += 1
chk(bad == 0, f"r = 2^(u+1)A* - 1 is exact and minimal on {tested} triples ({bad} failures)")

print(); print("="*88); print("THEOREM U"); print("="*88)
print(f"  eps_uncond = 1/(1+log2 3) = log_6 2 = {eps0:.11f}")
bad = 0; worst = (9.9, None)
for u in range(0, 14):
    for q in range(2, 10):
        for v in range(0, 26):
            A, n, c = Astar(u, q, v); S = u+n; r1 = (1 << (u+1))*A
            if c <= (1 << (n-1)): bad += 1                 # step: c > 2^{n-1}
            if 3**(u+1)*A < c: bad += 1                    # step: 3^{u+1}A* >= c
            if r1 * 3**(u+1) <= (1 << S): bad += 1         # bound (ii), exact
            if math.log2(r1) < eps0*S - 1e-9: bad += 1     # Theorem U
            lg = math.log2(r1)/S
            if lg < worst[0]: worst = (lg, (u, q, v, S))
chk(bad == 0, f"every step of Theorem U, exact, over 14*8*26 triples ({bad} violations)")
print(f"  worst observed log2(r+1)/S = {worst[0]:.6f} at (u,q,v,S) = {worst[1]}  "
      f"(floor {eps0:.6f})")

print(); print("="*88)
print("the quantifier trap: A* is PERIODIC in u for fixed (q,v)"); print("="*88)
print("  A*_u is the least residue of 3^{-(u+1)} c mod 2^{n+1}, and")
print("  ord_{2^{n+1}}(3) = 2^{n-1} for n >= 2, so u -> A*_u has period 2^{n-1}")
print("  and dips to O(1) within every period.  Hence NO lower bound on A* holds")
print("  uniformly in u for fixed (q,v).  This is harmless for Theorem U: for")
print("  fixed n, bound (i) alone gives log2(r+1) >= u+1 = S-n+1, so the ratio")
print("  tends to 1.  But a hypothesis must be stated for A*/2^{n+1} or")
print("  equivalently relative to S -- never as an absolute floor on A*.")
print(f"  {'(q,v)':>8} {'n':>3} {'period':>7} {'periodic':>9} {'min A* over a period':>21}")
for (q, v) in ((3,1),(2,3),(3,4),(2,6)):
    n = q+v
    if n < 3: continue
    per = 1 << (n-1); seq = [Astar(u,q,v)[0] for u in range(2*per)]
    print(f"  {str((q,v)):>8} {n:>3} {per:>7} "
          f"{str(all(seq[i]==seq[i+per] for i in range(per))):>9} {min(seq[:per]):>21}")

print(); print("="*88)
print("the corridor-admissible cone, and the critical diagonal"); print("="*88)
def admissible(u, q, v, cc):
    if (1 << (u+q)) > (1 << cc)*3**(u+1): return False
    for i in range(1, v+1):
        if (1 << (u+q+i)) > (1 << cc)*3**(u+1+i): return False
    return (1 << u) <= (1 << cc)*3**u
bad = 0
for cc in (0,1,2):
    for u in range(0,12):
        for q in range(2,14):
            for v in (0,1,5,20):
                if admissible(u,q,v,cc) != ((1 << (u+q)) <= (1 << cc)*3**(u+1)): bad += 1
chk(bad == 0, "confinement at level c is the single inequality 2^{u+q} <= 2^c 3^{u+1}; "
              "v is unrestricted")
print(f"  Theorem U is worst at b = (u+1)/S = {eps0:.6f}.  With q = 2 the cone")
print(f"  condition 2 <= c + log2 3 + (log2 3 - 1)u holds for every u >= 0 at c = 1,")
print(f"  and v = n-2 is then free, so every b in (0,1) is admissible:")
print(f"  {'target b':>9} {'u':>4} {'q':>3} {'v':>5} {'S':>4} {'admissible c=1':>15} {'log2(r+1)/S':>12}")
for b in (0.2, 0.3, 0.386853, 0.45, 0.6):
    S = 50; u = max(0, round(b*S)-1); q = 2; v = S-u-q
    if v < 0: continue
    A, n, c = Astar(u,q,v)
    print(f"  {b:>9.6f} {u:>4} {q:>3} {v:>5} {u+n:>4} {str(admissible(u,q,v,1)):>15} "
          f"{math.log2((1 << (u+1))*A)/(u+n):>12.6f}")
print()
print(('ALL PASS' if not fails else f'{len(fails)} FAILURES'))
print(f"peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024:.1f} MiB")
sys.exit(1 if fails else 0)
