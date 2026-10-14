"""The small-eta problem, made quantitative: the corridor LOCAL-TIME profile.

Exactly:  sum_{n<H} z_n = 3(Bcal_H - m_0).  Stratify the occupied times by depth
below the corridor top,  L_w = #{n<H : c-w-1 < R_n <= c-w}  (w = 0,1,2,...).
On that stratum z_n > 2^{c-w-1}, so
      sum_w L_w 2^{-w}  <  2^{1-c} * 3(Bcal_H - m_0) =: Lambda ,
while   O_c = sum_w L_w .
So O_c is controlled by the carry pot ONLY IF the profile L_w decays fast enough
to beat 2^w.  Exactly how it decays is the missing input.  Measured here.
Depth strata are decided exactly: c-w-1 < R_n <= c-w  <=>  2^{S_n+w} <= 2^c 3^n
and 2^{S_n+w+1} > 2^c 3^n.
"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
from eoc import *

CASES = [(285175,1),(626331,1),(63728127,1),(27,1),(703,1),(10087,1),(35655,1),(381727,1)]
print(f"{'m_0':>10} {'c':>2} {'O_c':>5} {'profile L_0,L_1,L_2,...':>44} "
      f"{'sum L_w 2^-w':>13} {'Lambda':>14} {'O_c/sum L_w 2^-w':>17}")
for (m0,c) in CASES:
    Hc,_ = last_return_certified(m0,c)
    d,S,m = orbit(m0,Hc)
    prof = {}
    for n in range(Hc):
        if not in_corridor(S,n,c): continue
        w = 0
        while not ((1 << (S[n]+w)) <= (1<<c)*3**n and (1 << (S[n]+w+1)) > (1<<c)*3**n):
            w += 1
            if w > 200: break
        prof[w] = prof.get(w,0)+1
    Oc = sum(prof.values())
    wmax = max(prof)
    wt = sum(F(cnt, 1 << w) for w,cnt in prof.items())
    z = zs(S,Hc); B = Bcal(m,z,Hc)
    Lam = F(2,1<<c)*3*(B[Hc]-m0)/2*2   # 2^{1-c} * 3(B_H - m_0)
    Lam = F(1 << 1, 1 << c)*3*(B[Hc]-m0)
    shown = [prof.get(w,0) for w in range(min(wmax+1,14))]
    print(f"{m0:>10} {c:>2} {Oc:>5} {str(shown)+('...' if wmax>=14 else ''):>44} "
          f"{float(wt):>13.6f} {float(Lam):>14.2f} {Oc/float(wt):>17.3f}")
print()
print("w_max per case (deepest stratum reached inside the corridor):")
for (m0,c) in CASES:
    Hc,_ = last_return_certified(m0,c)
    d,S,m = orbit(m0,Hc)
    ws=[]
    for n in range(Hc):
        if not in_corridor(S,n,c): continue
        w=0
        while not ((1 << (S[n]+w)) <= (1<<c)*3**n and (1 << (S[n]+w+1)) > (1<<c)*3**n):
            w+=1
            if w>200: break
        ws.append(w)
    print(f"   m_0={m0:>9} c={c}: w_max = {max(ws)}, mean w = {sum(ws)/len(ws):.3f}, "
          f"O_c = {len(ws)}")
print()
print("READ-OFF: the profiles are NOT concentrated at small w -- they spread to")
print("w_max comparable to O_c itself, with mean depth growing with O_c.  The ratio")
print("O_c / sum_w L_w 2^-w is the exact inverse-eta loss, and it is already 10^1-10^3")
print("on these finite orbits.  So the carry pot does not see the deep strata at all:")
print("that is the small-eta problem in its exact form.")
