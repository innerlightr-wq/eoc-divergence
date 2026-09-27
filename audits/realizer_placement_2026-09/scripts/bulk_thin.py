#!/usr/bin/env python3
"""Recommended next task: separate thin/degenerate classes (bounded combinatorially) from
the bulk (where a weighted centered-energy estimate is attempted).

Per shell s, fixed split j, partition by intermediate total a:
  H_s(0) <= sum_a min{ L_a , (2L_a/q)(1 + sqrt(chi_U,a chi_V,a)) }
THIN classes: |U_a| = 1 or |V_a| = 1  -> use the trivial L_a, and bound its WEIGHT by the
  unconditional combinatorial estimate  L_a/L_s <= N*C(a-1,j-1)C(s-a-1,N-j-1)/C(s-1,N-1)
  (rotation bound, verified in verify_combinatorial.out).
BULK classes: report the weighted product  sum_bulk L_a sqrt(chi_U chi_V)  and its tau.
No size filter: every class is retained in the final count.
"""
import math
from math import comb
from collections import defaultdict
ALPHA=math.log2(3); I0=ALPHA-ALPHA*math.log2(ALPHA)+(ALPHA-1)*math.log2(ALPHA-1); SS=1-I0/ALPHA
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
print(f"sigma* = {SS:.9f};  crossover kappa for the a=j class: 1/(alpha-Delta) = "
      f"{1/(ALPHA-0.425485676):.6f}")
print(f"  max gain at that crossover = I0*(kappa-1/alpha) = "
      f"{I0*(1/(ALPHA-0.425485676)-1/ALPHA):.6f}  (vs 0.001513 at kappa=0.65)\n")
for (B,N,lab) in ((20,13,"kappa=0.65 PRIMARY"),(16,15,"kappa=0.94"),(20,18,"kappa=0.90 STRESS")):
    ws=words(N); j=max(2,N//2)
    print(f"{'='*78}\n{lab}: B={B} N={N}, balanced split j={j}\n{'='*78}")
    G=defaultdict(lambda:{"u":set(),"v":set(),"n":0})
    Ltot=defaultdict(int)
    for w in ws:
        s,_=SC(w); Ltot[s]+=1
        if s+1-B<1: continue
        a,_=SC(w[:j]); g=G[(s,a)]; g["u"].add(w[:j]); g["v"].add(w[j:]); g["n"]+=1
    print(f"  {'s':>4} {'d':>3} {'#cls':>5} {'thin':>5} {'L_thin':>10} {'L_thin*q/L_s':>13}"
          f" {'W_comb bound':>13} {'bulk tau':>9} {'C_shell':>8}")
    grand_bnd=0.0; grand_main=0.0
    for s in sorted(set(k[0] for k in G)):
        d=s+1-B; q=1<<d; Ls=Ltot[s]
        cls=[(a,D) for (ss,a),D in G.items() if ss==s]
        nthin=0; Lthin=0; Wcomb=0.0; bulkW=0.0; Lbulk=0; bnd=0.0
        for a,D in cls:
            U=sorted(D["u"]); V=sorted(D["v"]); L=len(U)*len(V)
            assert L==D["n"], "non-product class"
            mod=1<<(s+1); inv=pow(3,-j,mod)
            f=defaultdict(int); h=defaultdict(int)
            for u in U:
                _,Cu=SC(u); f[((-inv*Cu)%mod)>>B]+=1
            for v in V:
                b,Cv=SC(v); rv=rz(len(v),b,Cv); h[((inv*(1<<a)*rv)%mod)>>B]+=1
            xU=q*sum(c*c for c in f.values())/len(U)**2-1
            xV=q*sum(c*c for c in h.values())/len(V)**2-1
            prod=math.sqrt(max(xU,0)*max(xV,0))
            if len(U)==1 or len(V)==1:
                nthin+=1; Lthin+=L
                try: Wcomb += N*comb(a-1,j-1)*comb(s-a-1,N-j-1)/comb(s-1,N-1)
                except ValueError: pass
                bnd += min(L,(2*L/q)*(1+prod))
            else:
                Lbulk+=L; bulkW += L*prod
                bnd += min(L,(2*L/q)*(1+prod))
        tau = -math.log(bulkW/(q*Lbulk))/math.log(q) if bulkW>0 and Lbulk>0 and q>1 else float('nan')
        grand_bnd+=bnd; grand_main+=Ls/q
        print(f"  {s:>4} {d:>3} {len(cls):>5} {nthin:>5} {Lthin:>10,} {Lthin*q/Ls:>13.4f}"
              f" {Wcomb:>13.4f} {tau:>9.4f} {bnd/(Ls/q):>8.4f}")
    print(f"  TOTAL proved bound / cylinder main = C = {grand_bnd/grand_main:.4f}\n")
