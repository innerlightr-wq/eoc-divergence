#!/usr/bin/env python3
"""Which split index j maximises the SHELL-AGGREGATE tau at the binding (largest-d) shell?
tau_shell(s) = -log_q( (sum_a R_a) / L_s ).  Need > sigma* = 0.949956, uniformly in B and s.
Reported per (B,N) for every j, with the trivial bound available per class."""
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
print(f"sigma* = {SS:.6f}\n")
for (B,N) in ((16,15),(20,18)):
    ws=words(N)
    smax=max(SC(w)[0] for w in ws)
    print(f"=== B={B} N={N};  binding shell s={smax}, d={smax+1-B}, q={1<<(smax+1-B)} ===")
    print(f"  {'j':>3} {'classes':>8} {'L_s':>12} {'sum R_a':>11} {'tau_shell':>10} {'C_total':>9} {'verdict':>9}")
    best=None
    for j in range(2,N-1):
        G=defaultdict(lambda:{"u":set(),"v":set(),"n":0})
        for w in ws:
            s,_=SC(w); d=s+1-B
            if d<1: continue
            a,_=SC(w[:j]); g=G[(s,a)]; g["u"].add(w[:j]); g["v"].add(w[j:]); g["n"]+=1
        ok=all(len(D["u"])*len(D["v"])==D["n"] for D in G.values())
        if not ok: continue
        # binding shell
        Ls=0; sR=0.0
        tot_bnd=0.0; tot_main=0.0
        for (s,a),D in G.items():
            d=s+1-B; q=1<<d; mod=1<<(s+1); inv=pow(3,-j,mod)
            U=sorted(D["u"]); V=sorted(D["v"]); L=len(U)*len(V)
            f=defaultdict(int); h=defaultdict(int)
            for u in U:
                _,Cu=SC(u); f[((-inv*Cu)%mod)>>B]+=1
            for v in V:
                b,Cv=SC(v); rv=rz(len(v),b,Cv); h[((inv*(1<<a)*rv)%mod)>>B]+=1
            EA=q*sum(c*c for c in f.values())-len(U)**2
            EB=q*sum(c*c for c in h.values())-len(V)**2
            R=math.sqrt(max(EA,0))*math.sqrt(max(EB,0))/q
            tot_main += L/q
            tot_bnd  += min(L, 2*L/q+2*R)
            if s==smax: Ls+=L; sR+=R
        q=1<<(smax+1-B)
        tau = -math.log(sR/Ls)/math.log(q) if sR>0 else 99
        C=tot_bnd/tot_main
        v = "PASS" if tau>SS else "FAIL"
        print(f"  {j:>3} {len(G):>8} {Ls:>12,} {sR:>11.2f} {tau:>10.4f} {C:>9.4f} {v:>9}")
        if best is None or tau>best[0]: best=(tau,j,C)
    print(f"  --> best j={best[1]}: tau_shell={best[0]:.4f}, total C={best[2]:.4f}\n")
