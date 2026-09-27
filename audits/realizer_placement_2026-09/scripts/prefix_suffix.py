#!/usr/bin/env python3
"""Prefix-suffix factorization of the TOP BLOCK, with the cutoff restored.

DERIVED HERE, from the verified concatenation law r_{uv} = 3^{-j}(2^a r_v - C_u) mod 2^{s+1}:

Let s = S_w, d = s+1-B, and split w = uv with |u| = j, S_u = a, S_v = b, a+b = s.
Put P := (-3^{-j} C_u) mod 2^{s+1}  and  Q_v := (3^{-j} 2^a r_v) mod 2^{s+1}, so
r_w = (P + Q_v) mod 2^{s+1}.  Since 3^{-j} and r_v are odd, 2^a | Q_v.

*** CHOOSE THE SPLIT SO THAT a >= B. ***  Then 2^B | Q_v, so writing
   P = P_lo + 2^B P_hi  (P_lo < 2^B, P_hi < 2^d),   Q_v = 2^B q_v  (q_v < 2^d),
we get P + Q_v = P_lo + 2^B (P_hi + q_v) and hence, EXACTLY,

        r_w mod 2^B = P_lo            (prefix only)
        T_w := floor(r_w / 2^B) = ( P_hi(u) + q_v(v) ) mod 2^d .        (SPLIT)

So the top block is an ADDITIVE convolution of a prefix term and a suffix term, with NO
low-bit coupling: the cutoff is fully restored and the two halves still separate.
Consequences:
  V(g) := sum_w e(g T_w / 2^d) = A(g) * Bq(g),  A(g)=sum_u e(g P_hi/2^d), Bq(g)=sum_v e(g q_v/2^d)
  #{T_w = 0} = 2^{-d} sum_g A(g) Bq(g),  main term 2^{-d} #U #V,
  signed error  = 2^{-d} sum_{g != 0} A(g) Bq(g),
  |error| <= 2^{-d} sqrt(E_A) sqrt(E_B)  (Cauchy-Schwarz), where by Parseval
  E_A = 2^d sum_x n_A(x)^2 - (#U)^2,  E_B likewise (the excess additive energies).
Terras's bijection makes v -> r_v mod 2^{b+1} injective, hence q_v injective, hence
  E_B = #V (2^d - #V)   EXACTLY.
That reduces the whole cutoff-counting error to the PREFIX energy E_A alone.
"""
import math, cmath
from collections import defaultdict
from fractions import Fraction

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

def run(B,N,label):
    print(f"\n{'='*78}\n{label}:  B={B}, N={N}, X=2^{B}\n{'='*78}",flush=True)
    ws=words(N)
    # group by (s, j, a) where j is the MINIMAL index with S_j >= B
    groups=defaultdict(lambda: {"u":set(),"v":set(),"pairs":[]})
    nsplit=0
    for w in ws:
        S=0; j=None
        for i,a in enumerate(w,1):
            S+=a
            if S>=B: j=i; aa=S; break
        s,_=SC(w)
        if j is None or j>=N: continue      # no interior split with a>=B
        nsplit+=1
        u=w[:j]; v=w[j:]
        g=groups[(s,j,aa)]
        g["u"].add(u); g["v"].add(v); g["pairs"].append((u,v))
    print(f"  words of length N: {len(ws):,}   with an interior split at a>=B: {nsplit:,}"
          f"   (j,a,s) classes: {len(groups):,}",flush=True)
    bad_split=bad_prod=bad_inj=0; nclass=0
    tot_actual=0; tot_main=Fraction(0); tot_cs=0.0; tot_triv=0
    rows=[]
    for (s,j,aa),G in sorted(groups.items()):
        d=s+1-B
        U=sorted(G["u"]); V=sorted(G["v"])
        # product-set check
        if len(G["pairs"])!=len(U)*len(V): bad_prod+=1
        nclass+=1
        mod=1<<(s+1)
        inv=pow(3,-j,mod)
        Phi={}; 
        for u in U:
            a_,Cu=SC(u)
            P=(-inv*Cu)%mod
            Phi[u]=P>>B
        qv={}
        for v in V:
            b_,Cv=SC(v); rv=realizer_from(len(v),b_,Cv)
            Q=(inv*(1<<aa)*rv)%mod
            assert Q % (1<<B)==0, "Q_v not divisible by 2^B"
            qv[v]=Q>>B
        # (SPLIT) verification against the directly computed realizer
        for (u,v) in G["pairs"]:
            w=u+v; Sw,Cw=SC(w); rw=realizer_from(len(w),Sw,Cw)
            if (rw>>B) != ((Phi[u]+qv[v])%(1<<d)): bad_split+=1
            if (rw%(1<<B)) != ((-inv*SC(u)[1])%mod)%(1<<B): bad_split+=1
        # injectivity of q_v (Terras)
        if len(set(qv.values()))!=len(V): bad_inj+=1
        # exact counts
        actual=sum(1 for (u,v) in G["pairs"] if (Phi[u]+qv[v])%(1<<d)==0)
        main=Fraction(len(U)*len(V),1<<d)
        nA=defaultdict(int); 
        for u in U: nA[Phi[u]]+=1
        EA=(1<<d)*sum(c*c for c in nA.values())-(len(U))**2
        EB=len(V)*((1<<d)-len(V))
        cs=(2.0**(-d))*math.sqrt(max(EA,0))*math.sqrt(max(EB,0))
        tot_actual+=actual; tot_main+=main; tot_cs+=cs; tot_triv+=len(U)*len(V)
        rows.append((s,j,aa,d,len(U),len(V),actual,float(main),EA,EB,cs))
    print(f"  (SPLIT) violations: {bad_split}   non-product (j,a,s) classes: {bad_prod}"
          f"   q_v non-injective classes: {bad_inj}   [of {nclass} classes]",flush=True)
    print(f"  {'s':>4} {'j':>3} {'a':>4} {'d':>3} {'#U':>9} {'#V':>7} {'actual':>9} {'main':>11}"
          f" {'|actual-main|':>13} {'C-S bound':>11} {'trivial':>9}",flush=True)
    for (s,j,aa,d,nu,nv,ac,mn,EA,EB,cs) in rows[:14]:
        print(f"  {s:>4} {j:>3} {aa:>4} {d:>3} {nu:>9,} {nv:>7,} {ac:>9,} {mn:>11.3f}"
              f" {abs(ac-mn):>13.3f} {cs:>11.3f} {nu*nv:>9,}",flush=True)
    if len(rows)>14: print(f"  ... {len(rows)-14} more classes",flush=True)
    err=abs(tot_actual-float(tot_main))
    print(f"\n  TOTAL over split classes: actual={tot_actual:,}  main={float(tot_main):.3f}"
          f"  |signed error|={err:.3f}",flush=True)
    print(f"  Cauchy-Schwarz bound (sum of per-class): {tot_cs:.3f}",flush=True)
    print(f"  TRIVIAL bound (sum of #U*#V):            {tot_triv:,}",flush=True)
    if tot_cs>0:
        print(f"  saving of C-S over trivial: factor {tot_triv/tot_cs:.2f}"
              f"  = 2^{math.log2(tot_triv/tot_cs):.3f}",flush=True)
    return rows

run(20,13,"kappa = 0.65 (pre-registered default)")
run(20,18,"kappa = 0.90 (stress test recommended by the assessment)")
