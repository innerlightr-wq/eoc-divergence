#!/usr/bin/env python3
"""GENERALIZED SPLIT (DERIVED HERE): the a >= B restriction is unnecessary.

With P := (-3^{-j}C_u) mod 2^{s+1} = P_lo + 2^B P_hi  and
     Q := (3^{-j} 2^a r_v) mod 2^{s+1} = Q_lo + 2^B Q_hi   (P_lo,Q_lo < 2^B),
r_w = (P+Q) mod 2^{s+1} gives, for ANY split point j,

    r_w mod 2^B = (P_lo + Q_lo) mod 2^B
    T_w = floor(r_w/2^B) = ( P_hi(u) + Q_hi(v) + c(u,v) ) mod 2^d,
    c(u,v) = floor( (P_lo + Q_lo) / 2^B )  in  {0,1}.

So the top block is a prefix term plus a suffix term plus ONE carry bit. When a >= B we have
Q_lo = 0 and c = 0, recovering the earlier clean split.  The carry is the entire coupling.
"""
import math
from collections import defaultdict
def SC(word):
    S=0;C=0
    for a in word: C=3*C+(1<<S); S+=a
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

print("=== verification of the generalized split, over ALL interior split points ===")
print(f"  {'B':>4} {'N':>4} {'words':>10} {'(w,j) checks':>13} {'T_w violations':>15}"
      f" {'low-bit violations':>19} {'c=1 fraction':>13} {'a<B fraction':>13}")
for (B,N) in ((12,8),(16,11),(20,13),(16,15),(20,18)):
    ws=words(N); nchk=0; badT=0; badL=0; nc1=0; naB=0
    for w in ws:
        Sw,Cw=SC(w); rw=rz(N,Sw,Cw); s=Sw; d=s+1-B
        if d<1: continue
        mod=1<<(s+1)
        for j in range(1,N):
            u=w[:j]; v=w[j:]
            a,Cu=SC(u); b,Cv=SC(v); rv=rz(len(v),b,Cv)
            inv=pow(3,-j,mod)
            P=(-inv*Cu)%mod; Q=(inv*(1<<a)*rv)%mod
            Plo=P&((1<<B)-1); Phi=P>>B
            Qlo=Q&((1<<B)-1); Qhi=Q>>B
            c=(Plo+Qlo)>>B
            nchk+=1; nc1+=c; naB+= (1 if a<B else 0)
            if (rw>>B) != ((Phi+Qhi+c)%(1<<d)): badT+=1
            if (rw&((1<<B)-1)) != ((Plo+Qlo)&((1<<B)-1)): badL+=1
    if nchk==0: print(f"  {B:>4} {N:>4} {len(ws):>10,} {0:>13}  (no shell with d>=1)"); continue
    print(f"  {B:>4} {N:>4} {len(ws):>10,} {nchk:>13,} {badT:>15} {badL:>19}"
          f" {nc1/nchk:>13.4f} {naB/nchk:>13.4f}",flush=True)
print()
print("  0 violations at every split point, including all a < B, confirms that the ONLY")
print("  prefix/suffix coupling in the top block is the single carry bit c in {0,1}.")
print()
print("=== consequence: a two-term factorization of the shell Weyl sum ===")
print("  V(g) = sum_{u,v} e(g(P_hi+Q_hi+c)/2^d)")
print("       = sum_{c0 in {0,1}} e(g c0/2^d) * sum_{(u,v): c(u,v)=c0} e(g P_hi/2^d) e(g Q_hi/2^d)")
print("  The inner sum is a product ONLY on the set {c = c0}, which is a threshold condition")
print("  P_lo + Q_lo >= 2^B.  So the coupling is now a single low-bit threshold, not a general")
print("  correlation: exactly the object an off-diagonal estimate would have to handle.")
