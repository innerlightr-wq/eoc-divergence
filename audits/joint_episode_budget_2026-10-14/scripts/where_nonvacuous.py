"""Where is the candidate bound  P-1 < (3/2) 2^{-c} * 3(Bcal_H - m_0)  non-vacuous?

Test it on the Prop. 13.2 oscillator realizers, whose drift is confined to a
bounded TWO-SIDED window by construction, against the real seeds whose drift
escapes.  Exact arithmetic throughout.
"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
from eoc import *

def oscillator(c, N):
    S=[0]; d=[]
    for n in range(N):
        dn = 2 if (1 << S[n]) <= (1<<c)*3**n else 1
        d.append(dn); S.append(S[n]+dn)
    return d,S

def realizer(S,N):
    C=0
    for j in range(N): C = 3*C + (1 << S[j])
    SN=S[N]; M=1<<(SN+1)
    return (pow(3**N,-1,M)*((1<<SN)-C)) % M

print("ON THE OSCILLATOR (bounded two-sided drift by construction):")
print(f"{'c':>2} {'N':>4} {'P':>4} {'O_c':>5} {'pot=3(B_N-m_0)':>16} {'RHS':>12} "
      f"{'P-1<RHS':>8} {'slack':>8} {'max R_n':>8} {'min R_n':>8}")
for c in (0,1,2):
    for N in (60,120,200):
        d,S = oscillator(c,N)
        r = realizer(S,N)
        dd,SS,mm = orbit(r,N)
        assert tuple(dd)==tuple(d), "realizer does not reproduce the word"
        z = zs(SS,N); B = Bcal(mm,z,N)
        eps = episodes(SS,N,c)
        P = len(eps); Oc = sum(b-a for (a,b,_) in eps)
        pot = 3*(B[N]-mm[0])
        rhs = F(3,2)/(1<<c)*pot
        Rs = [math.log2(float(z[n])) for n in range(N+1)]
        print(f"{c:>2} {N:>4} {P:>4} {Oc:>5} {float(pot):>16.4f} {float(rhs):>12.4f} "
              f"{str((P-1)<rhs):>8} {float(rhs)/max(P-1,1):>8.3f}x {max(Rs):>8.4f} {min(Rs):>8.4f}")
print()
print("ON REAL SEEDS WHOSE DRIFT ESCAPES (the orbit reaches 1):")
print(f"{'m_0':>10} {'c':>2} {'P':>4} {'pot':>16} {'RHS':>14} {'slack':>12} {'max R_n':>9}")
for (m0,c) in [(285175,1),(626331,1),(63728127,1)]:
    Hc,_ = last_return_certified(m0,c)
    d,S,m = orbit(m0,Hc); z = zs(S,Hc); B = Bcal(m,z,Hc)
    eps = episodes(S,Hc,c); P=len(eps)
    pot = 3*(B[Hc]-m0); rhs = F(3,2)/(1<<c)*pot
    Rs=[math.log2(float(z[n])) for n in range(Hc+1)]
    print(f"{m0:>10} {c:>2} {P:>4} {float(pot):>16.1f} {float(rhs):>14.1f} "
          f"{float(rhs)/max(P-1,1):>12.1f}x {max(Rs):>9.3f}")
print()
print("READ-OFF: the candidate bound is tight-to-within-a-small-factor exactly where")
print("the drift is confined to a bounded two-sided window -- the sector already closed")
print("by BoundedDrift -- and loses 10^3..10^7 as soon as R_n is allowed to escape,")
print("because the pot then absorbs the exponentially large gap weights z_n = 2^{R_n}.")
