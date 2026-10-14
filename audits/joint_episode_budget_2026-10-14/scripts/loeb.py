"""Step 4a: replicate the Loeb benchmark m_0 = 285175, c = 1, from scratch.

The manuscript's Remark 6.2 states L_1 = 14, tau_1 = 15, O_1 = 98 and the
decomposition 15+4+6+64+1+5+3 = 98.  The displayed endpoints in the brief are
treated as REPLICATION TARGETS, not inputs.  No later return is omitted: the
horizon is certified by the fixed-point drift, not by a scan cutoff.
"""
import os, sys, resource
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
resource.setrlimit(resource.RLIMIT_AS, (1 << 32, 1 << 32))
from fractions import Fraction as F
from eoc import *

m0, c = 285175, 1
Hc, n_one = last_return_certified(m0, c)
print(f"m_0 = {m0}, c = {c}")
print(f"first index with m_n = 1 : n_one = {n_one}")
print(f"certified horizon        : H = {Hc}  (for n >= n_one, R increases by 2-alpha")
print(f"                             each step, so no occupied index exists at or after H)")
d, S, m = orbit(m0, Hc + 40)
# certify: every n in [Hc, Hc+40) is NOT occupied, and R is increasing there
after = [n for n in range(Hc, Hc + 40) if in_corridor(S, n, c)]
print(f"occupied indices in [H, H+40): {after}  (must be empty)")
eps = episodes(S, Hc, c)
lens = [b - a for (a, b, trunc) in eps]
print()
print(f"episodes (maximal occupied runs) in [0,{Hc}):")
for (a, b, trunc) in eps:
    print(f"   [{a},{b})  length {b-a}{'   <-- truncated at H' if trunc else ''}")
print(f"lengths: {' + '.join(map(str,lens))} = {sum(lens)}")
L1 = max([N for N in range(Hc) if all(in_corridor(S, j, c) for j in range(N + 1))])
tau1 = min(n for n in range(1, Hc) if not in_corridor(S, n, c))
print()
print(f"REPLICATION:  O_1 = {sum(lens)}   (manuscript: 98)      match={sum(lens)==98}")
print(f"              L_1 = {L1}          (manuscript: 14)      match={L1==14}")
print(f"              tau_1 = {tau1}      (manuscript: 15)      match={tau1==15}")
target_runs = [(0,15),(16,20),(21,27),(31,95),(98,99),(100,105),(108,111)]
got = [(a,b) for (a,b,_) in eps]
print(f"              runs  = {got}")
print(f"              target= {target_runs}")
print(f"              runs match = {got == target_runs}")
print(f"              lengths match 15+4+6+64+1+5+3 = {lens == [15,4,6,64,1,5,3]}")

# ---- W_i, eta_i, gaps, block products, all exact
C, _ = carries(S, Hc)
z = zs(S, Hc); B = Bcal(m, z, Hc)
print()
print(f"{'i':>2} {'[a,b)':>12} {'l_i':>4} {'W_i (exact float)':>20} "
      f"{'3(B_b - B_a)':>20} {'eta_i':>12} {'z_{a_i}':>12} {'(2/3)2^c':>10}")
tollbad = 0
for i, (a, b, _) in enumerate(eps):
    Wi = sum(z[n] for n in range(a, b))
    tel = 3 * (B[b] - B[a])
    eta = Wi / (F(1 << c) * (b - a))
    ok = (Wi == tel) and (0 < eta <= 1)
    toll = z[a] > F(2, 3) * (1 << c)
    if a > 0 and not toll: tollbad += 1
    print(f"{i:>2} {f'[{a},{b})':>12} {b-a:>4} {float(Wi):>20.9f} {float(tel):>20.9f} "
          f"{float(eta):>12.9f} {float(z[a]):>12.6f} {float(F(2,3)*(1<<c)):>10.6f}"
          f"{'' if ok else '   IDENTITY FAIL'}{'' if (a==0 or toll) else '   TOLL FAIL'}")
print(f"entry-toll violations (re-entries only): {tollbad}")

occW = sum(z[n] for n in range(Hc) if in_corridor(S, n, c))
gapW = sum(z[n] for n in range(Hc) if not in_corridor(S, n, c))
tot  = 3 * (B[Hc] - m0)
print()
print("GLOBAL ACCOUNTING (gaps included; Bcal is not conserved):")
print(f"  sum_{{n<H}} z_n                 = {float(tot):.9f}  = 3(Bcal_H - m_0)")
print(f"  occupied part (sum W_i)       = {float(occW):.9f}")
print(f"  gap part                      = {float(gapW):.9f}")
print(f"  occupied + gap == total       : {occW + gapW == tot}")
print(f"  Bcal_H = m_0 2^{{E_H}}           = {float(B[Hc]):.6f},  2^{{E_H}} = {float(B[Hc]/m0):.9f}")
print(f"peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024:.1f} MiB")
