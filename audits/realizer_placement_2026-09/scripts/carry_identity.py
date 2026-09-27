#!/usr/bin/env python3
"""The carry term is EXACTLY a signed difference of two counts on the carry set.

Claim (DERIVED HERE): with M = 2^d and the notation of balanced.py,
   carry := 2^{-d} sum_{g != 0} (e(g/M)-1) T(g)
          = #{(u,v) : c=1, P_hi+Q_hi = -1 mod M} - #{(u,v) : c=1, P_hi+Q_hi = 0 mod M}.
Proof sketch: the g=0 term of (e(g/M)-1)T(g) vanishes, so the sum over g != 0 equals the sum
over all g, which is M times the difference of the two Fourier inversions at -1 and 0.
Hence the ONLY unestimated quantity is a difference of two counts on the threshold set {c=1}
-- signed, so favourable cancellation is retained by construction.
"""
import math
from collections import defaultdict
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
B,N=20,18
ws=words(N)
G=defaultdict(lambda:{"u":set(),"v":set(),"p":[]})
for w in ws:
    s,_=SC(w); d=s+1-B
    if d<3 or d>7: continue
    for j in range(4,N-3):
        a,_=SC(w[:j]); g=G[(s,j,a)]
        g["u"].add(w[:j]); g["v"].add(w[j:]); g["p"].append((w[:j],w[j:]))
cands=[(k,v) for k,v in G.items() if len(v["u"])>=32 and len(v["v"])>=32
       and len(v["p"])==len(v["u"])*len(v["v"])]
cands.sort(key=lambda kv: -min(len(kv[1]["u"]),len(kv[1]["v"])))
print(f"{'s':>4} {'j':>3} {'d':>3} {'#c=1':>10} {'N(-1)':>8} {'N(0)':>8} {'diff':>7}"
      f" {'carry(FFT)':>11} {'match':>6} {'|diff|/#c1':>11}")
bad=0
for (s,j,a),D in cands[:14]:
    d=s+1-B; M=1<<d; mod=1<<(s+1); inv=pow(3,-j,mod)
    U=sorted(D["u"]); V=sorted(D["v"])
    Plo={};Phi={}
    for u in U:
        _,Cu=SC(u); P=(-inv*Cu)%mod; Plo[u]=P&((1<<B)-1); Phi[u]=P>>B
    Qlo={};Qhi={}
    for v in V:
        b,Cv=SC(v); rv=rz(len(v),b,Cv); Q=(inv*(1<<a)*rv)%mod
        Qlo[v]=Q&((1<<B)-1); Qhi[v]=Q>>B
    nm1=n0=nc1=0
    for u in U:
        for v in V:
            if ((Plo[u]+Qlo[v])>>B)==0: continue
            nc1+=1
            t=(Phi[u]+Qhi[v])%M
            if t==M-1: nm1+=1
            elif t==0: n0+=1
    diff=nm1-n0
    # independent FFT-free recomputation of 'carry' via the direct definition
    import cmath
    def e(x): return cmath.exp(2j*math.pi*x)
    car=0j
    for g in range(1,M):
        T=0j
        for u in U:
            for v in V:
                if ((Plo[u]+Qlo[v])>>B): T+=e(g*(Phi[u]+Qhi[v])/M)
        car+=(e(g/M)-1)*T
    car=(car/M).real
    ok=abs(car-diff)<1e-6
    bad+= (not ok)
    print(f"{s:>4} {j:>3} {d:>3} {nc1:>10,} {nm1:>8,} {n0:>8,} {diff:>7} {car:>11.4f}"
          f" {str(ok):>6} {abs(diff)/nc1:>11.6f}")
print(f"\nmismatches: {bad}")
print("=> the residual obligation is a bound on a DIFFERENCE OF TWO COUNTS over the carry set;")
print("   empirically |diff|/#c1 is of order 1e-4..1e-3 here, i.e. small, but unproved.")
