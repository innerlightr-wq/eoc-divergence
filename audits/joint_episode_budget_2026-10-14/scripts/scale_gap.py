"""The decisive scale comparison: the carry pot is Theta(m_0); EOC needs Theta(log m_0).

pot := sum_{n<H} z_n = 3(Bcal_H - m_0) = 3 m_0 (2^{E_H} - 1).
EOC (manuscript Sec.15) is an O_c <= K log2 m_0 statement; the certified maximum
of O_c / log2 m_0 over odd 3 <= m < 2^33 is 11.3402.
So any bound obtained by amortizing a per-episode toll against the pot is at best
O(pot), i.e. O(m_0), against a target of O(log m_0).
"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
from eoc import *
CASES=[(285175,1),(285175,2),(626331,1),(63728127,1),(27,1),(703,1),(10087,1),
       (35655,1),(381727,1),(2097151,1),(1234567891,1)]
print(f"{'m_0':>12} {'c':>2} {'O_c':>5} {'log2 m_0':>9} {'O_c/log2 m_0':>13} "
      f"{'pot':>16} {'pot/m_0':>9} {'pot/log2 m_0':>14} {'scale gap':>12}")
for (m0,c) in CASES:
    Hc,_ = last_return_certified(m0,c,cap=4000)
    if Hc is None: print(f"{m0:>12} {c:>2}  (no fixed point within cap)"); continue
    d,S,m = orbit(m0,Hc); z=zs(S,Hc); B=Bcal(m,z,Hc)
    eps=episodes(S,Hc,c); Oc=sum(b-a for (a,b,_) in eps)
    pot=3*(B[Hc]-m0); lg=math.log2(m0)
    print(f"{m0:>12} {c:>2} {Oc:>5} {lg:>9.3f} {Oc/lg:>13.4f} {float(pot):>16.1f} "
          f"{float(pot)/m0:>9.4f} {float(pot)/lg:>14.1f} {float(pot)/lg/(Oc/lg):>12.1f}x")
print()
print("The last column is the factor by which a PERFECT solution of the small-eta")
print("problem would still overshoot the actual occupation, i.e. the irreducible loss")
print("of the pot as a resource.  It grows like m_0/log m_0.")
print()
print("For comparison, the certified EOC frontier (manuscript Sec.15, Revision 8):")
print("   max over odd 3 <= m < 2^33 of O_c/log2 m  =  11.3402  (attained at c=8),")
print("so the target constant is ~10, while pot/log2 m_0 above is 10^3..10^8.")
