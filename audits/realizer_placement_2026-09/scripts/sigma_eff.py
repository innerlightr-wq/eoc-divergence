#!/usr/bin/env python3
"""What saving exponent sigma does the PROVED factorization+Terras+Cauchy-Schwarz deliver?

Per split class (s,j,a) with d = s+1-B, L = #U*#V:
    proved bound   |actual - main| <= 2^{-d} sqrt(E_A) sqrt(E_B),   E_B = #V(2^d - #V) exactly
    target form    |actual - main| <= L * 2^{-sigma d}
    =>  sigma_eff = -log2( bound / L ) / d       (need sigma_eff > 1 - I0/alpha = 0.949956)
Also reports the ORACLE sigma (from the actually observed error) to show the C-S loss.
"""
import math
from collections import defaultdict
ALPHA=math.log2(3); I0=ALPHA-ALPHA*math.log2(ALPHA)+(ALPHA-1)*math.log2(ALPHA-1)
SIGMA_STAR=1-I0/ALPHA
def SC(word):
    S=0;C=0
    for a in word: C=3*C+(1<<S); S+=a
    return S,C
def realizer_from(n,S,C):
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
print(f"sigma* = 1 - I0/alpha = {SIGMA_STAR:.9f}   (need sigma_eff > sigma*)")
for (B,N,lab) in ((16,15,"kappa~0.94"),(20,18,"kappa=0.90")):
    ws=words(N); groups=defaultdict(lambda:{"u":set(),"v":set(),"pairs":[]})
    for w in ws:
        S=0;j=None
        for i,a in enumerate(w,1):
            S+=a
            if S>=B: j=i;aa=S;break
        if j is None or j>=N: continue
        s,_=SC(w); G=groups[(s,j,aa)]
        G["u"].add(w[:j]); G["v"].add(w[j:]); G["pairs"].append((w[:j],w[j:]))
    print(f"\n=== {lab}: B={B}, N={N}; split classes={len(groups)} ===")
    print(f"  {'s':>4} {'d':>3} {'L=#U#V':>10} {'|err|':>9} {'C-S bnd':>11} {'sig_CS':>8} {'sig_oracle':>11} {'EA/EA_max':>10}")
    worst_cs=9.9; worst_or=9.9; tl=0; te=0.0; tcs=0.0
    for (s,j,aa),G in sorted(groups.items()):
        d=s+1-B; mod=1<<(s+1); inv=pow(3,-j,mod)
        U=sorted(G["u"]); V=sorted(G["v"]); L=len(U)*len(V)
        Phi={u:((-inv*SC(u)[1])%mod)>>B for u in U}
        qv={}
        for v in V:
            b_,Cv=SC(v); rv=realizer_from(len(v),b_,Cv)
            qv[v]=((inv*(1<<aa)*rv)%mod)>>B
        actual=sum(1 for (u,v) in G["pairs"] if (Phi[u]+qv[v])%(1<<d)==0)
        main=L/(1<<d); err=abs(actual-main)
        nA=defaultdict(int)
        for u in U: nA[Phi[u]]+=1
        EA=(1<<d)*sum(c*c for c in nA.values())-len(U)**2
        EAmax=(1<<d)*len(U)-len(U)**2          # E_A if Phi were injective
        EB=len(V)*((1<<d)-len(V))
        cs=(2.0**(-d))*math.sqrt(max(EA,0))*math.sqrt(max(EB,0))
        sc = -math.log2(cs/L)/d if cs>0 else 99
        so = -math.log2(err/L)/d if err>0 else 99
        worst_cs=min(worst_cs,sc); worst_or=min(worst_or,so)
        tl+=L; te+=err; tcs+=cs
        if d>=max(2,(s+1-B)) and L>1000 and d>=4:
            print(f"  {s:>4} {d:>3} {L:>10,} {err:>9.2f} {cs:>11.2f} {sc:>8.4f} {so:>11.4f}"
                  f" {(EA/EAmax if EAmax>0 else 0):>10.4f}")
    print(f"  --- worst-case sigma over classes:  C-S {worst_cs:.4f}   oracle {worst_or:.4f}"
          f"   (need > {SIGMA_STAR:.4f})")
    print(f"  --- totals: L={tl:,}  observed err={te:.2f}  C-S={tcs:.2f}"
          f"   C-S/observed = {tcs/te if te>0 else 0:.1f}x loss")
