#!/usr/bin/env python3
"""BOUNDED PROOF ATTEMPT: arithmetic input beyond capacity for the suffix collision count.

DERIVED HERE.  Within a bulk class all v in V share the total b, so the exact realizers r_v are
distinct ODD residues mod 2^{b+1}.  Let L = lcp(v,v') and t := S_L(v) + min(v_{L+1}, v'_{L+1}).
  (i)  v_2(r_v - r_{v'}) = t                                   [accelerated lcp law]
  (ii) y_v := 3^{-j} r_v mod 2^{b+1}, so v_2(y_v - y_{v'}) = t  [3^{-j} is a unit]
  (iii) a COLLISION floor(y_v/H) = floor(y_{v'}/H), H = 2^{B-a}, forces |y_v - y_{v'}| < H as
        integers; since the difference is a nonzero multiple of 2^t, |diff| >= 2^t, hence
                              t < B - a.
So colliding pairs must have a common prefix of SMALL total valuation.  This is genuine
arithmetic information beyond distinctness/capacity.  The question is whether it is enough.
"""
import math
from collections import defaultdict
ALPHA=math.log2(3)
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
def lcp_t(v,vp):
    L=0
    while L<len(v) and L<len(vp) and v[L]==vp[L]: L+=1
    S=sum(v[:L])
    return S+min(v[L],vp[L])

print("=== step (i)+(ii): verify the accelerated lcp law for suffix realizers ===")
bad=0; tot=0
for N in (8,10,12):
    byb=defaultdict(list)
    for w in words(N):
        b,C=SC(w); byb[b].append((w,rz(N,b,C)))
    for b,lst in byb.items():
        mod=1<<(b+1)
        for i in range(min(len(lst),60)):
            for k in range(i+1,min(len(lst),60)):
                v,r=lst[i]; vp,rp=lst[k]
                t=lcp_t(v,vp); d=(r-rp)%mod
                tot+=1
                if d==0: bad+=1; continue
                if (d & -d).bit_length()-1 != t: bad+=1
print(f"  pairs checked: {tot:,}   violations of v_2(r_v - r_v') = S_L + min: {bad}")

print("\n=== step (iii) + usefulness: collision => t < B-a, and what it buys ===")
B,N=20,18; j=N//2; ws=words(N)
G=defaultdict(lambda:{"u":set(),"v":set()})
for w in ws:
    s,_=SC(w)
    if s+1-B<1: continue
    a,_=SC(w[:j]); g=G[(s,a)]; g["u"].add(w[:j]); g["v"].add(w[j:])
print(f"  {'s':>4} {'a':>4} {'d':>3} {'|V|':>8} {'B-a':>5} {'sum h^2':>10} {'capacity':>11}"
       f" {'lcp-restr':>11} {'viol':>5} {'excl frac':>10}")
badiii=0
for (s,a),D in sorted(G.items()):
    d=s+1-B
    V=sorted(D["v"])
    if len(V)<200 or d<5: continue
    q=1<<d; mod=1<<(s+1); inv=pow(3,-j,mod); Hh=1<<(B-a)
    ys={}; bs=None
    for v in V:
        b,Cv=SC(v); bs=b; ys[v]=(pow(3,-j,1<<(b+1))*rz(len(v),b,Cv))%(1<<(b+1))
    h=defaultdict(int)
    for v in V: h[ys[v]//Hh]+=1
    S2=sum(c*c for c in h.values())
    # lcp-restricted pair count and violation check
    npair=0; nrestr=0
    Vs=V[:400]
    for i in range(len(Vs)):
        for k in range(len(Vs)):
            if i==k: continue
            v,vp=Vs[i],Vs[k]; t=lcp_t(v,vp); npair+=1
            same = (ys[v]//Hh)==(ys[vp]//Hh)
            if same and not (t < B-a): badiii+=1
            if t < B-a: nrestr+=1
    cap=Hh//2*len(V)
    scale=(len(V)/len(Vs))**2
    print(f"  {s:>4} {a:>4} {d:>3} {len(V):>8,} {B-a:>5} {S2:>10,} {cap:>11,}"
          f" {len(V)+int(nrestr*scale):>11,} {badiii:>5} {1-nrestr/npair:>10.6f}")
print(f"  violations of 'collision => t < B-a': {badiii}")
print()
print("  READING: the constraint is VALID but WEAK here -- the excluded fraction of pairs is")
print("  ~1e-2 or less, because short common prefixes are typical, so the lcp-restricted bound")
print("  is barely below the trivial |V|^2 and far above the true sum h^2.  The lemma supplies")
print("  real arithmetic information (it kills exactly the long-shared-prefix pairs) but does")
print("  NOT by itself deliver (*): it removes a vanishing fraction of the pair count, whereas")
print("  (*) needs sum h^2 near |V|^2/q.  Recorded as a precise negative.")
