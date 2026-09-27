#!/usr/bin/env python3
"""Verify the structural obstruction: LCP-rejection alone cannot beat capacity.

Setup: distinct odd transformed realizers y_v in [0, M), M = qH, H = 2^{B-a}, q = 2^{s+1-B}.
  n_z := #{v : y_v = z mod H}.  There are exactly q representatives of a fixed residue mod H
  in [0,qH), and the y_v are distinct, so n_z <= q.
  For distinct pairs, t < B-a  <=>  y_v != y_v' (mod H).   [t = v_2(y_v - y_v')]
  So the ordered candidate count surviving LCP rejection, with the diagonal, is
        P_LCP = n + n^2 - sum_z n_z^2 ,      and  sum_z n_z^2 <= q * n ,
  hence  P_LCP >= n(n + 1 - q).   Capacity gives  sum_x h(x)^2 <= n H / 2.
  Therefore  n + 1 > q + H/2   ==>   P_LCP > capacity, for ANY arrangement of low residues.
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
    return sum(v[:L])+min(v[L],vp[L])

B,N=20,18; j=N//2
G=defaultdict(lambda:{"v":set()})
for w in words(N):
    s,_=SC(w)
    if s+1-B<1: continue
    a,_=SC(w[:j])
    if a>=B: continue
    G[(s,a)]["v"].add(w[j:])
print(f"{'s':>4} {'a':>4} {'n=|V|':>8} {'q':>6} {'H':>6} {'n_z<=q':>7} {'t<B-a <=> y!=y mod H':>22}"
      f" {'P_LCP>=n(n+1-q)':>17} {'capacity nH/2':>14} {'ratio':>7} {'n+1>q+H/2':>10}")
badnz=badeq=0
for (s,a),D in sorted(G.items()):
    d=s+1-B; q=1<<d; Hh=1<<(B-a); V=sorted(D["v"])
    if len(V)<400: continue
    n=len(V); mod=1<<(s+1); inv=pow(3,-j,mod)
    ys={}
    for v in V:
        b,Cv=SC(v); ys[v]=(pow(3,-j,1<<(b+1))*rz(len(v),b,Cv))%(1<<(b+1))
    nz=defaultdict(int)
    for v in V: nz[ys[v]%Hh]+=1
    if max(nz.values())>q: badnz+=1
    # equivalence check on a sample of pairs
    Vs=V[:250]
    for i in range(len(Vs)):
        for k in range(i+1,len(Vs)):
            v,vp=Vs[i],Vs[k]
            if (lcp_t(v,vp) < B-a) != (ys[v]%Hh != ys[vp]%Hh): badeq+=1
    Plow=n*(n+1-q); cap=n*Hh//2
    print(f"{s:>4} {a:>4} {n:>8,} {q:>6} {Hh:>6} {str(max(nz.values())<=q):>7}"
          f" {'ok':>22} {Plow:>17,} {cap:>14,} {Plow/cap:>7.2f}"
          f" {str(n+1>q+Hh//2):>10}")
print(f"\n  n_z > q violations: {badnz}    't<B-a <=> y!=y mod H' violations: {badeq}")
print("\n  Representative class from the closing record (s=27, a=12):")
n,q,Hh=2258,256,256
print(f"    n={n} q={q} H={Hh}:  n+1-q={n+1-q}, P_LCP >= {n*(n+1-q):,}, capacity nH/2 = {n*Hh//2:,},"
      f" ratio {n*(n+1-q)/(n*Hh//2):.2f}")
print(f"    n+1 = {n+1} > q + H/2 = {q+Hh//2}  -> LCP-rejection PROVABLY cannot beat capacity here")
print(f"    n^2/q = {n*n/q:.6f}  (uniform reference collision mass)")
S2=21896
print(f"    chi_V (actual)   = {q*S2/n**2-1:.6f}")
print(f"    chi_V (capacity) = {q*(n*Hh//2)/n**2-1:.6f}   overshoot factor "
      f"{(q*(n*Hh//2)/n**2-1)/(q*S2/n**2-1):.2f}")
