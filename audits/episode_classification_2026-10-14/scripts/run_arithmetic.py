"""Step 1-2: the 2-adic characterisation of direction, the two run estimates,
and the chained fixed-turn lifetime bound.  Exact integers; floats only printed.
"""
import os, sys, math, resource
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
resource.setrlimit(resource.RLIMIT_AS, (1 << 32, 1 << 32))
from fractions import Fraction as F
from eoc import *
alpha = math.log2(3); phi = alpha - 1; psi = 2 - alpha
fails = []
def chk(c, m):
    print(('PASS  ' if c else 'FAIL  ') + m)
    if not c: fails.append(m)

print("=" * 92)
print("LEMMA A (2-adic characterisation of the direction symbol)")
print("=" * 92)
print("  d_n = 1  <=>  v2(m_n+1) >= 2  ;  a d=1 step sends v2(m+1) -> v2(m+1)-1 ;")
print("  hence the MAXIMAL d=1 run from x has length exactly v2(x+1) - 1.")
bad = 0; badrun = 0
for m0 in range(3, 60002, 2):
    d, S, m = orbit(m0, 12)
    for n in range(12):
        e = v2(m[n] + 1)
        if (d[n] == 1) != (e >= 2): bad += 1
        if d[n] == 1 and v2(m[n+1] + 1) != e - 1: bad += 1
    lead = 0
    while lead < len(d) and d[lead] == 1: lead += 1
    if lead < 12 and lead != v2(m0 + 1) - 1: badrun += 1
chk(bad == 0, f"d_n=1 <=> v2(m_n+1)>=2, and the step decrements v2(m+1): "
              f"all odd 3<=m0<=60001, n<12 ({bad} violations)")
chk(badrun == 0, f"maximal d=1 run length = v2(x+1) - 1 exactly ({badrun} violations)")

print()
print("=" * 92)
print("LEMMA B (the two run estimates)")
print("=" * 92)
print("  u consecutive d=1 steps:   y+1 = 3^u (x+1)/2^u   (EXACT), needs 2^u | x+1;")
print("    for the run to be realisable at all, 2^{u+1} | x+1, so x >= 2^{u+1}-1.")
print("  v consecutive d>=2 steps:  y-1 <= (3/4)^v (x-1), with equality stalling at x=1.")
b1 = b2 = b3 = 0
for m0 in range(3, 40002, 2):
    d, S, m = orbit(m0, 14)
    # exact ones-run identity
    u = 0
    while u < 14 and d[u] == 1: u += 1
    if u:
        if F(m[u] + 1) != F(3 ** u * (m0 + 1), 1 << u): b1 += 1
        if (m0 + 1) % (1 << (u + 1)) != 0: b2 += 1
    # twos-run contraction, states > 1
    for a in range(10):
        v = 0
        while a + v < 14 and d[a + v] >= 2 and m[a + v] > 1: v += 1
        if v and m[a] > 1:
            if not (F(m[a + v] - 1) <= F(3, 4) ** v * (m[a] - 1)): b3 += 1
chk(b1 == 0, f"y+1 = 3^u(x+1)/2^u exact on every maximal leading ones-run ({b1})")
chk(b2 == 0, f"2^{{u+1}} | x+1 for a maximal ones-run of length u ({b2})")
chk(b3 == 0, f"y-1 <= (3/4)^v (x-1) on every maximal twos-run with states > 1 ({b3})")

print()
print("=" * 92)
print("THEOREM C (chained fixed-turn lifetime bound) -- derived, and the brief's")
print("candidate F(k) = O((k+1) alpha^{k+1}) CORRECTED")
print("=" * 92)
print("""  Write h = log2(m+1), phi = log2(3/2) = alpha-1, psi = log2(4/3) = 2-alpha,
  so phi + psi = 1 and 1 + phi = alpha.  A ones-run of length u sends h -> h + u phi
  EXACTLY.  A twos-run of length v sends h -> h' with h' <= h - v psi + 1, using
  m-1 <= m+1 <= 2(m-1) for m >= 3.  With u_i <= h_i - 1 (Lemma A) and v_i >= 1,

        h_{i+1} <= h_i + (h_i - 1) phi - psi + 1 = alpha h_i ,

  so h_i <= alpha^{i-1} L with L = log2(m_0+1), and for j ones-runs

        sum u_i <= L (alpha^j - 1)/(alpha - 1) - j .

  Staying above m = 1 forces (sum v_i) psi <= L + (sum u_i) phi + j' - 1, and since
  1 + phi/psi = 1/psi,

        N  <=  (1/psi) [ sum u_i + L + j' - 1 ]
            <=  (L/(2-alpha)) * (alpha^j + alpha - 2)/(alpha - 1) ,      (*)

  with j = #ones-runs <= ceil((k+1)/2) and j' = #twos-runs.  So

        F(k) = Theta( alpha^{ceil((k+1)/2)} ) ,   NOT  O((k+1) alpha^{k+1}) :
  only the ones-runs compound, and there are about k/2 of them.  The brief's
  candidate overshoots by a factor about (k+1) alpha^{(k+1)/2}.""")
Fk = lambda j: (alpha ** j + alpha - 2) / (alpha - 1) / psi
print(f"  coefficient of L in (*):  j=1 -> {Fk(1):.6f}   j=2 -> {Fk(2):.6f}   "
      f"j=3 -> {Fk(3):.6f}   j=5 -> {Fk(5):.6f}")
print()
print("  SHARPNESS at j=1.  A Mersenne seed 2^{u+1}-1 does exactly u ones-steps first,")
print("  but its orbit generally starts FURTHER ones-runs before reaching 1, so j > 1")
print("  and the j=1 bound does not apply to it.  (An earlier version of this panel")
print("  compared N against the j=1 bound for Mersennes and reported three spurious")
print("  failures; the test was mis-specified, not the theorem.)  Below: the ACTUAL j,")
print("  the bound at that j, and -- for the j=1 case proper -- the prefix consisting of")
print("  the first ones-run plus the following twos-run only.")
print(f"  {'u':>3} {'m_0=2^(u+1)-1':>16} {'L':>7} {'N(->1)':>7} {'j':>3} "
      f"{'bound at j':>12} {'holds':>6} | {'j=1 prefix N1':>14} {'bound j=1':>10} {'holds':>6}")
for u in (4, 8, 12, 16, 20, 24):
    m0 = (1 << (u + 1)) - 1
    d, S, m = orbit(m0, 4000)
    N1 = next(n for n in range(len(m)) if m[n] == 1)
    L = math.log2(m0 + 1)
    sym = direction(d[:N1]); rr = runs(sym)
    j = sum(1 for (s, _) in rr if s == 0)
    bd = Fk(max(j, 1)) * L
    # the genuine j=1 prefix: first ones-run + the twos-run that follows it
    n1 = rr[0][1] + (rr[1][1] if len(rr) > 1 else 0)
    bd1 = Fk(1) * L
    print(f"  {u:>3} {m0:>16} {L:>7.3f} {N1:>7} {j:>3} {bd:>12.1f} "
          f"{str(N1 <= bd):>6} | {n1:>14} {bd1:>10.2f} {str(n1 <= bd1):>6}")
print("  The j=1 prefix ratio N1/(L-1) approaches 1/(2-alpha) = 2.4094 from the")
print("  ones-run alone and 4.8188 once the twos-run is included only when the twos-run")
print("  runs all the way to m=1, which it does not in general; so (*) is an upper")
print("  bound that is attained only by the all-the-way-down configuration.")

print()
print("  the bound tested on real seeds, with j the ACTUAL number of ones-runs")
print("  before arrival at 1 (all states > 1 on the prefix tested):")
print(f"  {'m_0':>10} {'N(->1)':>7} {'k':>4} {'j':>3} {'L':>8} {'bound (*)':>11} {'holds':>6}")
bad4 = 0
for m0 in (3, 7, 27, 31, 703, 10087, 35655, 285175, 381727, 626331, 63728127):
    d, S, m = orbit(m0, 4000)
    N1 = next(n for n in range(len(m)) if m[n] == 1)
    sym = direction(d[:N1]); j = sum(1 for (s, _) in runs(sym) if s == 0)
    k = changes(sym); L = math.log2(m0 + 1)
    bd = Fk(max(j, 1)) * L
    ok = N1 <= bd
    bad4 += (not ok)
    print(f"  {m0:>10} {N1:>7} {k:>4} {j:>3} {L:>8.4f} {bd:>11.2f} {str(ok):>6}")
chk(bad4 == 0, f"bound (*) holds on 11 real seeds up to arrival at 1 ({bad4} failures)")

print()
print("  FORCED GROWTH OF k (an elementary consequence, NOT divergence exclusion):")
print("  inverting (*), a prefix of length N with all states > 1 needs")
print("        alpha^j >= N (2-alpha)(alpha-1)/L - alpha + 2 ,  j >= log_alpha(...) ,")
print("  so k >= 2j - 1 grows at least like (2/log2 alpha) log2(N/L) = "
      f"{2/math.log2(alpha):.4f} log2(N/L).")
print()
print(('ALL PASS' if not fails else f'{len(fails)} FAILURES'))
print(f"peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024:.1f} MiB")
sys.exit(1 if fails else 0)
