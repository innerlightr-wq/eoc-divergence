#!/usr/bin/env python3
"""(1) singleton characterisation, (2) payoff arithmetic, (3) best finite diagnostic."""
import math
from math import comb, floor
from collections import defaultdict
ALPHA=math.log2(3); I0=ALPHA-ALPHA*math.log2(ALPHA)+(ALPHA-1)*math.log2(ALPHA-1); SS=1-I0/ALPHA

print("="*78);print("P1. Singleton characterisation: for ell>=3, |family|=1 iff b=ell");print("="*78)
print("  Proof: if b>ell the two words  (1^{ell-1}, b-ell+1)  and  (1^{ell-2}, 2, b-ell)  are")
print("  distinct, positive, total b, and both admissible: the only extra check for the second is")
print("  ell <= alpha(ell-1)+A, and ell/(ell-1) <= 3/2 < alpha for ell>=3.  b=ell forces all-ones.")
def family(ell,b,A):
    out=[]
    def rec(m,S,w):
        if m==ell:
            if S==b: out.append(tuple(w))
            return
        if S+(ell-m) > b: return
        a=1
        while S+a <= b:
            if S+a <= ALPHA*(m+1)+A+1e-12:
                w.append(a); rec(m+1,S+a,w); w.pop()
            a+=1
    rec(0,0,[]); return out
bad=0; tot=0; sing=0
for ell in range(3,10):
    for A in (0,0.5,1,2,3):
        for b in range(ell, floor(ALPHA*ell+A)+1):
            fam=family(ell,b,A); tot+=1
            if len(fam)==0: continue
            is1=(len(fam)==1); should=(b==ell)
            sing+=is1
            if is1!=should: bad+=1
print(f"  (ell,b,A) cases with a nonempty family: {tot}   singletons: {sing}"
      f"   mismatches with 'b=ell': {bad}")
print("  => |U_a|=1 (prefix, A=0) iff a=j ;  |V_a|=1 (suffix, A=alpha*j-a) iff b=N-j.")
print("     Both are the zero-excess endpoints k=0 and e-k=0, inside the band for every delta>=0.")

print();print("="*78);print("P2. The payoff arithmetic at tau=24/25, kappa=13/20");print("="*78)
from fractions import Fraction
kap=Fraction(13,20)
ak1=ALPHA*float(kap)-1
eta=ak1/25
expo=1-I0*float(kap)+eta
base=1-I0/ALPHA
print(f"  alpha*kappa-1            = {ak1:.15f}")
print(f"  eta = (alpha*kappa-1)/25 = {eta:.15f}   (claimed 0.00120902501875)")
print(f"  exponent 1-I0*kappa+eta  = {expo:.15f}   (claimed 0.949651926715094)")
print(f"  baseline H2(1/alpha)     = {base:.15f}   (claimed 0.949955527188331)")
print(f"  improvement              = {base-expo:.15f}   (claimed 0.000303600473237)")
print(f"  all four match to {max(abs(eta-0.00120902501875),abs(expo-0.949651926715094),abs(base-0.949955527188331),abs((base-expo)-0.000303600473237)):.2e}")
print(f"  sanity: eta < I0*(kappa-1/alpha) = {I0*(float(kap)-1/ALPHA):.15f} ? "
      f"{eta < I0*(float(kap)-1/ALPHA)}")

print();print("="*78);print("P3. Best finite diagnostic: min of BOTH valid bounds on EVERY class");print("="*78)
def SC(w):
    S=0;C=0
    for a in w: C=3*C+(1<<S); S+=a
    return S,C
def rz(n,S,C):
    q=1<<(S+1); r=((1<<S)-C)*pow(3,-n,q)%q
    return q if r==0 else r
def words(N):
    out=[]
    def rec(k,S,C,w):
        if k==N: out.append(tuple(w)); return
        Cn=3*C+(1<<S); a=1
        while (1<<(S+a))<=3**(k+1):
            w.append(a); rec(k+1,S+a,Cn,w); w.pop(); a+=1
    rec(0,0,0,[]); return out
for (B,N,lab) in ((20,13,"kappa=0.65"),(20,18,"kappa=0.90")):
    j=N//2; cap=floor(0.1*N); ws=words(N)
    G=defaultdict(lambda:{"u":set(),"v":set()}); Lt=defaultdict(int)
    for w in ws:
        s,_=SC(w); Lt[s]+=1
        if s+1-B<1: continue
        a,_=SC(w[:j]); g=G[(s,a)]; g["u"].add(w[:j]); g["v"].add(w[j:])
    gb=0.0; gm=0.0
    for (s,a),D in G.items():
        d=s+1-B; q=1<<d; mod=1<<(s+1); inv=pow(3,-j,mod)
        U=sorted(D["u"]); V=sorted(D["v"]); L=len(U)*len(V)
        f=defaultdict(int); h=defaultdict(int)
        for u in U:
            _,Cu=SC(u); f[((-inv*Cu)%mod)>>B]+=1
        for v in V:
            b,Cv=SC(v); rv=rz(len(v),b,Cv); h[((inv*(1<<a)*rv)%mod)>>B]+=1
        xU=q*sum(c*c for c in f.values())/len(U)**2-1
        xV=q*sum(c*c for c in h.values())/len(V)**2-1
        pr=math.sqrt(max(xU,0)*max(xV,0))
        gb += min(L, (2*L/q)*(1+pr))          # min of BOTH bounds, every class
    gm = sum(Lt[s]/(1<<(s+1-B)) for s in set(k[0] for k in G))
    print(f"  {lab}: best finite proved C = {gb/gm:.4f}   (was 29.52 when the band was given the"
          f" trivial bound only)")
print("  The frozen band is for the asymptotic proof; the finite record keeps the smaller of the")
print("  two rigorous bounds on every class.  Neither settles the asymptotics.")
