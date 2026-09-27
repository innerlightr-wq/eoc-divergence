#!/usr/bin/env python3
"""Task 3: which marginal limits sum_a R_a, and how does it scale?

Normalised collision excess (exact integers, no FFT):
   xA := q*sum_x f(x)^2 / |U|^2 - 1 = E_A/|U|^2,   xB := E_B/|V|^2.
Then R = |U||V| sqrt(xA xB)/q = L sqrt(xA xB)/q, so
   tau_eff (per class) = -log_q( sqrt(xA xB)/q ) = 1 - log_q sqrt(xA xB).
Perfect equidistribution of a marginal gives x = 0; a singleton gives x = q-1.
"""
import math
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
print(f"sigma* = {SS:.6f}")
for (B,N) in ((16,15),(20,18)):
    print(f"\n=== B={B}, N={N}, j=2 (best split found) ===")
    ws=words(N); j=2
    G=defaultdict(lambda:{"u":set(),"v":set()})
    for w in ws:
        s,_=SC(w); d=s+1-B
        if d<1: continue
        a,_=SC(w[:j]); g=G[(s,a)]; g["u"].add(w[:j]); g["v"].add(w[j:])
    print(f"  {'s':>4} {'d':>3} {'a':>4} {'|U|':>5} {'|V|':>10} {'xA':>10} {'xB':>10}"
          f" {'|V|/q':>9} {'tau_cls':>8}")
    worst=99
    for (s,a),D in sorted(G.items()):
        d=s+1-B; q=1<<d; mod=1<<(s+1); inv=pow(3,-j,mod)
        U=sorted(D["u"]); V=sorted(D["v"])
        f=defaultdict(int); h=defaultdict(int)
        for u in U:
            _,Cu=SC(u); f[((-inv*Cu)%mod)>>B]+=1
        for v in V:
            b,Cv=SC(v); rv=rz(len(v),b,Cv); h[((inv*(1<<a)*rv)%mod)>>B]+=1
        xA=q*sum(c*c for c in f.values())/len(U)**2-1
        xB=q*sum(c*c for c in h.values())/len(V)**2-1
        tau = 1-math.log(math.sqrt(max(xA,1e-300)*max(xB,1e-300)))/math.log(q) if q>1 and xA>0 and xB>0 else 99
        worst=min(worst,tau)
        if d>=max(1,0):
            print(f"  {s:>4} {d:>3} {a:>4} {len(U):>5} {len(V):>10,} {xA:>10.4f} {xB:>10.6f}"
                  f" {len(V)/q:>9.1f} {tau:>8.4f}")
    print(f"  worst per-class tau = {worst:.4f}   (need > {SS:.4f})")
