#!/usr/bin/env python3
"""Does a BALANCED split (both #U,#V large) give sigma > sigma* = 0.949956?

Exact identity (DERIVED HERE): with e(x)=exp(2 pi i x),
  V(g) = A(g) Bq(g) + (e(g/2^d)-1) * T(g),   T(g) = sum_{pairs with c=1} e(g(P_hi+Q_hi)/2^d)
so the FACTORED term is exact and the whole coupling sits in the carry term T, damped by
|e(g/2^d)-1| = 2|sin(pi g/2^d)|.
Reported: the exact error, its factored and carry parts, and the Cauchy-Schwarz sigma for the
factored part alone (E_A, E_B now both from large sets).
"""
import math, cmath
from collections import defaultdict
ALPHA=math.log2(3); I0=ALPHA-ALPHA*math.log2(ALPHA)+(ALPHA-1)*math.log2(ALPHA-1)
SS=1-I0/ALPHA
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
def e(x): return cmath.exp(2j*math.pi*x)

B,N=20,18
ws=words(N)
print(f"B={B} N={N} (kappa=0.90), sigma* = {SS:.6f}")
# group by (s, j, a) for every j, then keep the most balanced classes
G=defaultdict(lambda:{"u":set(),"v":set(),"p":[]})
for w in ws:
    s,_=SC(w); d=s+1-B
    if d<3 or d>7: continue
    for j in range(4,N-3):
        a,_=SC(w[:j])
        g=G[(s,j,a)]; g["u"].add(w[:j]); g["v"].add(w[j:]); g["p"].append((w[:j],w[j:]))
cands=[(k,v) for k,v in G.items() if len(v["u"])>=32 and len(v["v"])>=32
       and len(v["p"])==len(v["u"])*len(v["v"])]
cands.sort(key=lambda kv: -min(len(kv[1]["u"]),len(kv[1]["v"])))
print(f"product-set classes with #U,#V >= 32: {len(cands)}")
print(f"{'s':>4} {'j':>3} {'a':>4} {'d':>3} {'#U':>7} {'#V':>7} {'L':>10} {'err':>9} {'factored':>10}"
      f" {'carry':>9} {'C-S(fact)':>10} {'sig_CS':>8} {'sig_true':>9}")
shown=0
for (s,j,a),D in cands[:12]:
    d=s+1-B; mod=1<<(s+1); inv=pow(3,-j,mod)
    U=sorted(D["u"]); V=sorted(D["v"]); L=len(U)*len(V); M=1<<d
    Plo={};Phi={}
    for u in U:
        _,Cu=SC(u); P=(-inv*Cu)%mod; Plo[u]=P&((1<<B)-1); Phi[u]=P>>B
    Qlo={};Qhi={}
    for v in V:
        b,Cv=SC(v); rv=rz(len(v),b,Cv); Q=(inv*(1<<a)*rv)%mod
        Qlo[v]=Q&((1<<B)-1); Qhi[v]=Q>>B
    actual=0; c1=[]
    for u in U:
        for v in V:
            c=(Plo[u]+Qlo[v])>>B
            if c: c1.append((u,v))
            if (Phi[u]+Qhi[v]+c)%M==0: actual+=1
    main=L/M; err=actual-main
    # factored and carry parts of the exact Fourier error
    fact=0j; car=0j
    for g in range(1,M):
        A=sum(e(g*Phi[u]/M) for u in U); Bq=sum(e(g*Qhi[v]/M) for v in V)
        T=sum(e(g*(Phi[u]+Qhi[v])/M) for (u,v) in c1)
        fact += A*Bq; car += (e(g/M)-1)*T
    fact=(fact/M).real; car=(car/M).real
    nA=defaultdict(int); nB=defaultdict(int)
    for u in U: nA[Phi[u]]+=1
    for v in V: nB[Qhi[v]]+=1
    EA=M*sum(c*c for c in nA.values())-len(U)**2
    EB=M*sum(c*c for c in nB.values())-len(V)**2
    cs=math.sqrt(max(EA,0))*math.sqrt(max(EB,0))/M
    sc=-math.log2(cs/L)/d if cs>0 else 99
    st=-math.log2(abs(err)/L)/d if err!=0 else 99
    print(f"{s:>4} {j:>3} {a:>4} {d:>3} {len(U):>7,} {len(V):>7,} {L:>10,} {err:>9.3f} {fact:>10.3f}"
          f" {car:>9.3f} {cs:>10.3f} {sc:>8.4f} {st:>9.4f}")
    shown+=1
print()
print("  'factored'+'carry' must reproduce 'err' exactly (identity check).")
print(f"  sig_CS is the PROVED Cauchy-Schwarz exponent for the factored term; need > {SS:.4f}.")
