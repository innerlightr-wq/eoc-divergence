"""Step 2/3: the candidate joint bound, and the amortization hypothesis, tested.

CANDIDATE (written in ANALYSIS_PLAN.md before testing):
   per-episode toll   W_i >= z_{a_i} > (2/3) 2^c   at every re-entry a_i > 0
   global pot         sum_i W_i = 3 sum_i (Bcal_{b_i} - Bcal_{a_i}) <= 3(Bcal_H - m_0)
   ==>  P - 1 < (9/2) 2^{-c} m_0 (2^{E_H} - 1) .

AMORTIZATION HYPOTHESIS (the thing Remark 13.3's charge needs):
   the single-window allowance  A_i := log2 m_{a_i} + c_i  must be CONSUMED, i.e.
   decrease (or at least not grow) across episodes.  Tested directly.
"""
import os, sys, math, resource
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
resource.setrlimit(resource.RLIMIT_AS, (1 << 32, 1 << 32))
from fractions import Fraction as F
from eoc import *

CASES = [(285175, 1), (285175, 2), (27, 1), (703, 1), (10087, 1), (35655, 1),
         (381727, 1), (626331, 1), (63728127, 1), (63728127, 2)]
print("=" * 100)
print("A. THE CANDIDATE BOUND  P - 1 < (9/2) 2^{-c} (Bcal_H - m_0) * 3 ... tested exactly")
print("=" * 100)
print(f"{'m_0':>10} {'c':>2} {'H':>5} {'P':>4} {'O_c':>5} {'sum W_i':>14} "
      f"{'toll (2/3)2^c (P-1)':>20} {'pot 3(B_H-m_0)':>18} {'RHS':>14} {'holds':>6} {'slack':>10}")
rows = []
for (m0, c) in CASES:
    Hc, n_one = last_return_certified(m0, c)
    d, S, m = orbit(m0, Hc)
    z = zs(S, Hc); B = Bcal(m, z, Hc)
    eps = episodes(S, Hc, c)
    P = len(eps); Oc = sum(b - a for (a, b, _) in eps)
    SW = sum(sum(z[n] for n in range(a, b)) for (a, b, _) in eps)
    toll = F(2, 3) * (1 << c) * (P - 1)
    pot = 3 * (B[Hc] - m0)
    rhs = F(9, 2) * pot / (1 << c) / 3 * 3   # = (9/2) 2^{-c} pot
    rhs = F(3, 2) / (1 << c) * pot
    holds = (P - 1) < rhs
    rows.append((m0, c, Hc, P, Oc, SW, pot))
    print(f"{m0:>10} {c:>2} {Hc:>5} {P:>4} {Oc:>5} {float(SW):>14.6f} "
          f"{float(toll):>20.6f} {float(pot):>18.3f} {float(rhs):>14.1f} "
          f"{str(holds):>6} {float(rhs)/(P-1) if P>1 else float('inf'):>10.1f}x")
print()
print("The bound HOLDS everywhere and is VACUOUS everywhere (slack 1e3-1e8).")
print("Diagnosis, exactly: the pot sum_n z_n is dominated by the GAP times, where")
print("z_n = 2^{R_n} > 2^c and grows, while on the corridor z_n <= 2^c.  Split it:")
print(f"{'m_0':>10} {'c':>2} {'occupied part':>15} {'gap part':>18} {'gap share':>10}")
for (m0, c) in CASES[:6]:
    Hc, _ = last_return_certified(m0, c)
    d, S, m = orbit(m0, Hc); z = zs(S, Hc)
    occ = sum(z[n] for n in range(Hc) if in_corridor(S, n, c))
    gap = sum(z[n] for n in range(Hc) if not in_corridor(S, n, c))
    print(f"{m0:>10} {c:>2} {float(occ):>15.6f} {float(gap):>18.3f} "
          f"{float(gap/(occ+gap)):>10.6f}")
print()
print("So amortizing the episode toll against the global carry pot can only bound")
print("GAP time from above, i.e. it yields LOWER bounds on O_c, never upper ones.")
print("Explicitly, with G = H - O_c the gap-time count and z_n > 2^c on gaps:")
print("     2^c G  <  pot  ==>  O_c > H - 2^{-c} * pot    (a lower bound).")
for (m0, c) in CASES[:4]:
    Hc, _ = last_return_certified(m0, c)
    d, S, m = orbit(m0, Hc); z = zs(S, Hc)
    eps = episodes(S, Hc, c); Oc = sum(b-a for (a,b,_) in eps)
    pot = 3 * (sum(z[n] for n in range(Hc))/3)
    G = Hc - Oc
    print(f"   m_0={m0:>9} c={c}: 2^c G = {float((1<<c)*G):>10.1f} < pot = {float(pot):>12.1f}  "
          f"=> O_c > {float(Hc - pot/(1<<c)):>12.1f}  (actual O_c = {Oc})")

print()
print("=" * 100)
print("B. THE AMORTIZATION HYPOTHESIS: is the single-window allowance CONSUMED?")
print("=" * 100)
print("   A_i = log2 m_{a_i} + c_i  (Remark 13.3's per-episode charge, up to K)")
print("   claim under test: A_i decreases, or at least does not grow, in i.")
viol = 0
for (m0, c) in CASES[:7]:
    Hc, _ = last_return_certified(m0, c)
    d, S, m = orbit(m0, Hc); z = zs(S, Hc); B = Bcal(m, z, Hc)
    eps = episodes(S, Hc, c)
    print(f"  m_0 = {m0}, c = {c}:")
    A = []
    for i, (a, b, _) in enumerate(eps):
        # c_i = c - R_{a_i}; exact via z: R_a = log2 z_a, so c_i = c - log2 z_a
        ci = c - math.log2(float(z[a]))
        Ai = math.log2(m[a]) + ci
        A.append(Ai)
        print(f"     i={i} a={a:>4} m_a={m[a]:>22} c_i={ci:>9.6f}  A_i={Ai:>10.6f}  "
              f"Bcal_a={float(B[a]):>14.4f}  m_a >= m_0 2^-c : {m[a] >= F(m0, 1<<c)}")
    nondec = all(A[i+1] >= A[i] - 1e-9 for i in range(len(A)-1))
    print(f"     A_i non-decreasing in i : {nondec}   (min={min(A):.4f}, max={max(A):.4f}, "
          f"log2 m_0 - c = {math.log2(m0)-c:.4f})")
    if not nondec: viol += 1
print()
print(f"cases where A_i was NOT non-decreasing: {viol} / 7")
print(f"peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024:.1f} MiB")
