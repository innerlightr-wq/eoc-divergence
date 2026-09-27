#!/usr/bin/env python3
"""Tasks 1-3: audit the carry-robust bound, then complete-shell coverage with ALL classes.

Bound under audit (assessment, re-derived here):
  T = Z + c (mod q), c in {0,1}  =>  T=t  =>  Z in {t, t-1}  =>  H(t) <= H0(t) + H0(t-1)
  |H0(t) - L/q| <= R := sqrt(E_A E_B)/q   uniformly in t   (Fourier inversion + Cauchy-Schwarz)
  E_A = q*sum_x f(x)^2 - |U|^2,  E_B = q*sum_x h(x)^2 - |V|^2   (exact integer collision counts)
  => H(t) <= 2L/q + 2R  and  |D| = |H(0)-L/q| <= L/q + 2R   (lower side from H(0) >= 0).
Target interface (ResidueDiscrepancy.exceptional_count_le_of_leastRealizerBound, hC : 1 <= C):
  sum_{s>=B} H_s(0) <= C * sum_{s>=B} L_s * 2^{-d_s}.
"""
import math
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

def analyse(B,N,j,verbose=True):
    ws=words(N)
    # partition the whole shell family by (s, a) at the FIXED split index j
    G=defaultdict(lambda:{"u":set(),"v":set(),"p":[]})
    for w in ws:
        s,_=SC(w); d=s+1-B
        if d<1: continue
        a,_=SC(w[:j])
        g=G[(s,a)]; g["u"].add(w[:j]); g["v"].add(w[j:]); g["p"].append((w[:j],w[j:]))
    out={}
    bad_prod=bad_dom=bad_R=bad_E=0; nclass=0; ncov=0
    per_shell=defaultdict(lambda:[0,0,0.0,0.0,0.0,0])  # L, Htrue, sumR, bnd_plain, bnd_min, ntriv
    for (s,a),D in sorted(G.items()):
        d=s+1-B; q=1<<d; mod=1<<(s+1); inv=pow(3,-j,mod)
        U=sorted(D["u"]); V=sorted(D["v"]); L=len(U)*len(V); nclass+=1; ncov+=len(D["p"])
        isprod = (len(D["p"])==L)
        if not isprod: bad_prod+=1; continue
        Plo={};Phi={}
        for u in U:
            _,Cu=SC(u); P=(-inv*Cu)%mod; Plo[u]=P&((1<<B)-1); Phi[u]=P>>B
        Qlo={};Qhi={}
        for v in V:
            b,Cv=SC(v); rv=rz(len(v),b,Cv); Q=(inv*(1<<a)*rv)%mod
            Qlo[v]=Q&((1<<B)-1); Qhi[v]=Q>>B
        f=defaultdict(int); h=defaultdict(int)
        for u in U: f[Phi[u]]+=1
        for v in V: h[Qhi[v]]+=1
        EA=q*sum(c*c for c in f.values())-len(U)**2
        EB=q*sum(c*c for c in h.values())-len(V)**2
        if EA<0 or EB<0: bad_E+=1
        R=math.sqrt(max(EA,0))*math.sqrt(max(EB,0))/q
        # exact H0 and H over all residues
        H0=defaultdict(int); H=defaultdict(int)
        for u in U:
            for v in V:
                z=(Phi[u]+Qhi[v])%q; H0[z]+=1
                c=(Plo[u]+Qlo[v])>>B
                H[(z+c)%q]+=1
        for t in range(q):
            if H[t] > H0[t]+H0[(t-1)%q]: bad_dom+=1
            if abs(H0[t]-L/q) > R+1e-9: bad_R+=1
        ps=per_shell[s]
        ps[0]+=L; ps[1]+=H[0]; ps[2]+=R
        ps[3]+= 2*L/q + 2*R
        bmin=min(L, 2*L/q+2*R); ps[4]+=bmin
        if bmin==L: ps[5]+=1
    if verbose:
        print(f"  j={j}: classes={nclass}  words covered={ncov:,}  non-product={bad_prod}"
              f"  domination violations={bad_dom}  R violations={bad_R}  negative energy={bad_E}")
    return per_shell, (nclass,bad_prod,bad_dom,bad_R)

for (B,N,lab) in ((20,13,"kappa=0.65 (primary)"),(20,18,"kappa=0.90 (stress)")):
    print(f"\n{'='*78}\n{lab}: B={B}, N={N}\n{'='*78}")
    best=None
    for j in range(2,N-1):
        ps,(nc,bp,bd,br)=analyse(B,N,j)
        if bp or bd or br: continue
        Ls=sum(v[0] for v in ps.values()); Ht=sum(v[1] for v in ps.values())
        main=sum(v[0]/(1<<(s+1-B)) for s,v in ps.items())
        bnd=sum(v[4] for v in ps.values())
        sumR=sum(v[2] for v in ps.values())
        C_eff = bnd/main if main>0 else float('inf')
        if best is None or C_eff<best[0]: best=(C_eff,j,Ls,Ht,main,bnd,sumR,ps)
    if best is None: print("  no valid j"); continue
    C_eff,j,Ls,Ht,main,bnd,sumR,ps=best
    print(f"\n  BEST split j={j}:  L_total={Ls:,}  true H(0)={Ht:,}  cylinder main={main:.2f}")
    print(f"     true C (=H/main)          : {Ht/main:.4f}")
    print(f"     PROVED bound / main = C   : {C_eff:.4f}   <- the constant delivered")
    print(f"     sum_a R_a                 : {sumR:.2f}")
    print(f"  {'s':>4} {'d':>3} {'L_s':>12} {'H_s(0)':>9} {'L_s/q':>11} {'sum R_a':>10}"
          f" {'bound':>11} {'tau_eff':>8} {'#triv used':>11}")
    for s,v in sorted(ps.items()):
        d=s+1-B; q=1<<d
        tau = -math.log(v[2]/v[0])/math.log(q) if v[2]>0 and v[0]>0 and q>1 else float('nan')
        print(f"  {s:>4} {d:>3} {v[0]:>12,} {v[1]:>9,} {v[0]/q:>11.2f} {v[2]:>10.2f}"
              f" {v[4]:>11.2f} {tau:>8.4f} {v[5]:>11}")
    print(f"\n  sigma* = {SS:.6f}.  tau_eff > sigma* is what the aggregate energy estimate must give.")
