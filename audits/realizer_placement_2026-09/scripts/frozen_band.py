#!/usr/bin/env python3
"""(i) Is my numeric 'thin' set contained in the frozen band?  (ii) Recompute with the FROZEN band."""
import math
from math import comb, floor
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
DELTA=0.10
for (B,N,lab) in ((20,13,"kappa=0.65 PRIMARY"),(20,18,"kappa=0.90 STRESS")):
    j=N//2; cap=floor(DELTA*N)
    print(f"\n{'='*78}\n{lab}: B={B} N={N} j={j}, frozen band min(k,e-k) <= floor({DELTA}*N) = {cap}\n{'='*78}")
    G=defaultdict(lambda:{"u":set(),"v":set(),"n":0}); Ltot=defaultdict(int)
    for w in words(N):
        s,_=SC(w); Ltot[s]+=1
        if s+1-B<1: continue
        a,_=SC(w[:j]); g=G[(s,a)]; g["u"].add(w[:j]); g["v"].add(w[j:]); g["n"]+=1
    # (i) containment
    notcontained=[]; nthin_old=0
    for (s,a),D in G.items():
        e=s-N; k=a-j
        inband = min(k,e-k)<=cap
        old_thin = (len(D["u"])==1 or len(D["v"])==1)
        if old_thin: nthin_old+=1
        if old_thin and not inband: notcontained.append((s,a,k,e-k,len(D["u"]),len(D["v"])))
    print(f"  my old numeric thin classes (|U|=1 or |V|=1): {nthin_old}")
    print(f"  of those NOT in the frozen band: {len(notcontained)}")
    for t in notcontained[:8]:
        print(f"     s={t[0]} a={t[1]} k={t[2]} e-k={t[3]} |U|={t[4]} |V|={t[5]}")
    # (ii) frozen-band accounting
    print(f"  {'s':>4} {'d':>3} {'#cls':>5} {'band':>5} {'L_thin':>10} {'thin*q/L_s':>11}"
          f" {'comb bnd':>10} {'bulk tau':>9} {'C_shell':>8}")
    gb=0.0; gm=0.0
    for s in sorted(set(kk[0] for kk in G)):
        d=s+1-B; q=1<<d; Ls=Ltot[s]; e=s-N
        nb=0; Lthin=0; bulkW=0.0; Lbulk=0; bnd=0.0
        for (ss,a),D in G.items():
            if ss!=s: continue
            k=a-j; U=sorted(D["u"]); V=sorted(D["v"]); L=len(U)*len(V)
            mod=1<<(s+1); inv=pow(3,-j,mod)
            f=defaultdict(int); h=defaultdict(int)
            for u in U:
                _,Cu=SC(u); f[((-inv*Cu)%mod)>>B]+=1
            for v in V:
                b,Cv=SC(v); rv=rz(len(v),b,Cv); h[((inv*(1<<a)*rv)%mod)>>B]+=1
            xU=q*sum(c*c for c in f.values())/len(U)**2-1
            xV=q*sum(c*c for c in h.values())/len(V)**2-1
            pr=math.sqrt(max(xU,0)*max(xV,0))
            if min(k,e-k)<=cap:
                nb+=1; Lthin+=L; bnd+=L                       # trivial bound on the band
            else:
                Lbulk+=L; bulkW+=L*pr; bnd+=min(L,(2*L/q)*(1+pr))
        T=0
        for k in range(0,e+1):
            if min(k,e-k)>cap: continue
            a=j+k; b=(N-j)+(e-k)
            if a-1>=j-1 and b-1>=N-j-1: T+=comb(a-1,j-1)*comb(b-1,N-j-1)
        cb=q*N*T/comb(s-1,N-1) if comb(s-1,N-1) else float('nan')
        tau=-math.log(bulkW/(q*Lbulk))/math.log(q) if bulkW>0 and Lbulk>0 and q>1 else float('nan')
        gb+=bnd; gm+=Ls/q
        print(f"  {s:>4} {d:>3} {len([1 for kk in G if kk[0]==s]):>5} {nb:>5} {Lthin:>10,}"
              f" {Lthin*q/Ls:>11.4f} {cb:>10.4f} {tau:>9.4f} {bnd/(Ls/q):>8.4f}")
    print(f"  TOTAL proved bound / cylinder main = C = {gb/gm:.4f}")
