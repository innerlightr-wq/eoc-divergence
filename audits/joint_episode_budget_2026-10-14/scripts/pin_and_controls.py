"""Proposition J (exact, integral) + controls A-E.

PROPOSITION J (two-sided allowance pin).  For a re-entry a > 0 put
    A_a = log2 m_a + c_a ,   c_a = c - R_a .
Then, EXACTLY and with no logarithm:
    1  <=  2^{2c} m_a^2 / (m_0 Bcal_a)  <  (9/4) Bcal_a / m_0 ,
equivalently   log2 m_0 - c  <=  A_a  <  log2 m_0 - c + E_a + 2(alpha-1),
2(alpha-1) = log2(9/4) = 1.169925001.
The left half is carry positivity (C_a > 0 <=> Bcal_a > m_0); the right half is
exactly the entry lemma z_a > (2/3)2^c of Prop. 13.1.  So J is a REARRANGEMENT
of two known facts, not an independent restriction -- its value is the corollary:
    A_a - (log2 m_0 - c) = E_a + 2 c_a ,  both terms >= 0, E monotone INCREASING.
Hence the per-episode allowance never decreases below its floor and the only
monotone piece enters with the WRONG SIGN.  No amortization is available.
"""
import os, sys, math, resource
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
resource.setrlimit(resource.RLIMIT_AS, (1 << 32, 1 << 32))
from fractions import Fraction as F
from eoc import *

CASES = [(285175,1),(285175,2),(285175,3),(626331,1),(63728127,1),(63728127,2),
         (27,1),(703,1),(10087,1),(35655,1),(381727,1)]
print("="*96)
print("PROPOSITION J, exact integral form, at every re-entry")
print("="*96)
bad = 0; nre = 0
for (m0,c) in CASES:
    Hc,_ = last_return_certified(m0,c)
    d,S,m = orbit(m0,Hc); z = zs(S,Hc); B = Bcal(m,z,Hc)
    eps = episodes(S,Hc,c)
    for i,(a,b,_) in enumerate(eps):
        if a == 0: continue
        nre += 1
        ratio = F(1 << (2*c)) * F(m[a])**2 / (F(m0) * B[a])
        lo_ok = ratio >= 1
        hi_ok = ratio < F(9,4) * B[a] / m0
        idA   = (F(2,3)*(1<<c) < z[a] <= F(1<<c))      # entry toll, exact
        idB   = B[a] >= m0                              # carry positivity
        # the identity A_a - (log2 m_0 - c) = E_a + 2 c_a, checked in exact 2-powers:
        lhs = F(1 << (2*c)) * F(m[a])**2 / (F(m0) * B[a])     # 2^{A_a-(log2 m_0-c)}
        rhs = (B[a]/m0) * (F(1<<c)/z[a])**2                   # 2^{E_a} * 2^{2 c_a}
        idC = lhs == rhs
        if not (lo_ok and hi_ok and idA and idB and idC): bad += 1
print(f"  re-entries tested: {nre};  violations: {bad}")
print(f"  (checks: ratio>=1, ratio<(9/4)B_a/m_0, (2/3)2^c<z_a<=2^c, B_a>=m_0,")
print(f"   and the exact identity 2^{{A_a-(log2 m_0-c)}} = 2^{{E_a}} 2^{{2c_a}})")
print()
print("  the band, numerically (m_0=285175, c=1): floor = log2 m_0 - c = "
      f"{math.log2(285175)-1:.6f}")
Hc,_ = last_return_certified(285175,1)
d,S,m = orbit(285175,Hc); z = zs(S,Hc); B = Bcal(m,z,Hc)
EH = math.log2(float(B[Hc]/285175))
print(f"  E_H = {EH:.6f}, so for i>=1 all A_i lie in "
      f"[{math.log2(285175)-1:.4f}, {math.log2(285175)-1+EH+math.log2(9/4):.4f}]  "
      f"(width {EH+math.log2(9/4):.4f})")
for i,(a,b,_) in enumerate(episodes(S,Hc,1)):
    Ai = math.log2(m[a]) + 1 - math.log2(float(z[a]))
    print(f"     i={i} A_i={Ai:.6f}{'   <- initial episode, c_0=c, J does not apply' if a==0 else ''}")

print()
print("="*96)
print("CONTROLS")
print("="*96)
print("A. least realizer vs larger lifts in the SAME exact realizer class.")
print("   The word, R-profile, episode structure, W_i and eta_i of the shared prefix")
print("   are class invariants; the absolute seed and entry heights are not.")
def word_of(m0,N):
    d,_,_ = orbit(m0,N); return tuple(d)
N0 = 12
base = 285175
w = word_of(base,N0)
S0 = sum(w); M = 1 << (S0+1)
r = base % M
print(f"   prefix of 285175, N={N0}: word={w}, S={S0}, class = {r} mod {M}")
print(f"   {'lift':>14} {'word matches':>13} {'R-profile id':>13} {'W over prefix':>16} {'log2 m_0':>9}")
for k in range(5):
    lift = r + k*M
    if lift % 2 == 0 or lift < 3: continue
    dd,SS,mm = orbit(lift,N0); zz = zs(SS,N0)
    same_word = tuple(dd) == w
    same_R = SS == [sum(w[:j]) for j in range(N0+1)]
    Wp = sum(zz[n] for n in range(N0) if (1<<SS[n]) <= 2*3**n)
    print(f"   {lift:>14} {str(same_word):>13} {str(same_R):>13} {float(Wp):>16.9f} "
          f"{math.log2(lift):>9.4f}")
print("   => occupation/W/eta of the prefix are IDENTICAL across lifts while log2 m_0")
print("      grows without bound.  Any charge containing log2 m_0 is therefore not a")
print("      function of the prefix, which is precisely Remark 13.3's mechanism.")

print()
print("B. long all-ones prefixes (zero-confined, positively realizable at finite depth).")
print(f"   {'k':>3} {'least realizer 2^(k+1)-1':>24} {'#leading d=1':>13} {'R_k':>9} "
      f"{'W over [0,k)':>14} {'mean z':>9}")
for k in (4,8,12,16,20):
    seed = (1 << (k+1)) - 1
    dd,SS,mm = orbit(seed,k); zz = zs(SS,k)
    lead = 0
    while lead < len(dd) and dd[lead]==1: lead += 1
    Wk = sum(zz[n] for n in range(k))
    print(f"   {k:>3} {seed:>24} {lead:>13} {math.log2(float(zz[k])):>9.4f} "
          f"{float(Wk):>14.6f} {float(Wk)/k:>9.6f}")
print("   => mean corridor weight stays O(1) while the least realizer is 2^{k+1}-1:")
print("      height is in the accounting, and small mean weight does not make an")
print("      episode cheap in seed scale.")

print()
print("C. the Prop. 13.2 oscillator: digit 2 inside the corridor, digit 1 outside.")
def oscillator(c, N):
    """Prescribed word; returns the R-profile only (symbolic, no seed yet)."""
    S=[0]; d=[]
    for n in range(N):
        # digit chosen by membership AT step n: d=2 if R_n <= c, else d=1
        dn = 2 if (1 << S[n]) <= (1<<c)*3**n else 1
        d.append(dn); S.append(S[-1]+dn)
    return d,S
for c in (0,1):
    d,S = oscillator(c, 200)
    occ = [n for n in range(200) if (1<<S[n]) <= (1<<c)*3**n]
    runs=[];a=occ[0];p=occ[0]
    for n in occ[1:]:
        if n==p+1: p=n; continue
        runs.append(p+1-a); a=n;p=n
    runs.append(p+1-a)
    print(f"   c={c}: {len(runs)} episodes in [0,200), lengths {sorted(set(runs))}, "
          f"occupation {sum(runs)}, max gap {max(1,200-sum(runs))}")
print("   => many short episodes; episode COUNT is unbounded (Prop. 13.2) so no")
print("      bound of the form P <= const can exist.  Consistent with A above.")

print()
print("D. the -1 all-ones trajectory (negative control).")
print("   -1 is a fixed point of T(x)=(3x+1)/2: d=1 forever, R_n = n(1-alpha) -> -inf,")
print("   so EVERY n is occupied for every c >= 0: one infinite episode, O_c = infinity.")
print("   It satisfies the corridor condition with no positivity: the hypothesis the")
print("   argument needs is m_n >= 1 (used in Bcal_a >= m_0 and in m_n >= m_0 2^-c),")
print("   i.e. POSITIVITY OF THE STATES, not positivity of the seed alone.")

print()
print("E. affine recurrence over positive reals, no integer ray.")
print("   Fix the word of 285175 and run x_{n+1} = (3 x_n + 1)/2^{d_n} from real x_0:")
d8,S8,m8 = orbit(285175, 40)
for x0 in (F(285175), F(1,2), F(10**6), F(1,10**6)):
    x = x0; Rs=[]
    for n in range(40):
        x = (3*x+1)/ (1 << d8[n])
    print(f"     x_0={float(x0):>12.4g} -> x_40={float(x):>14.6g}   "
          f"(integer orbit m_40 = {m8[40]})")
print("   The R-profile is prescribed by the word, so corridor membership, W_i and")
print("   eta_i are IDENTICAL for every real x_0.  Any argument that never uses")
print("   integrality or m_n >= 1 is valid here too and therefore proves nothing")
print("   arithmetic.  Proposition J uses Bcal_a >= m_0 (i.e. C_a > 0), which holds")
print("   for every positive real start, and the entry lemma, which is purely")
print("   symbolic -- so J is NOT an integer obstruction.  Recorded as such.")
print()
print(f"peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024:.1f} MiB")
