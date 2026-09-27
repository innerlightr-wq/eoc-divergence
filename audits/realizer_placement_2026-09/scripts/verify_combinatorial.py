#!/usr/bin/env python3
"""Verify the assessment's new combinatorial claims."""
import math
from math import comb
from collections import defaultdict
ALPHA=math.log2(3); I0=ALPHA-ALPHA*math.log2(ALPHA)+(ALPHA-1)*math.log2(ALPHA-1); SS=1-I0/ALPHA
H2=lambda x:-x*math.log2(x)-(1-x)*math.log2(1-x)

print("="*78);print("C1. The rotation (cycle-lemma) bound  L_s >= C(s-1,N-1)/N");print("="*78)
print("  Proof checked: with e_i = d_i - s/N (sum 0), rotate just after a maximiser m of the")
print("  partial sums T_k. Then every new partial sum is T_. - T_m <= 0, so S'_k <= (s/N)k <= alpha k")
print("  because s <= alpha N. Each rotation class has <= N members and contributes >= 1 confined word.")
def confined_by_shell(N):
    cnt=defaultdict(int)
    def rec(k,S,w):
        if k==N: cnt[S]+=1; return
        a=1
        while (1<<(S+a))<=3**(k+1):
            rec(k+1,S+a,w); a+=1
    rec(0,0,None); return cnt
bad=0; tot=0
print(f"  {'N':>3} {'s':>4} {'L_s (exact)':>13} {'C(s-1,N-1)/N':>15} {'ratio':>8} {'holds':>6}")
for N in (6,8,10,12,14):
    cs=confined_by_shell(N)
    for s in sorted(cs):
        lb=comb(s-1,N-1)/N; tot+=1
        ok=cs[s]>=lb-1e-9
        bad+= (not ok)
        if N in (10,14) and s in (N, N+2, int(ALPHA*N)-1, int(ALPHA*N)):
            print(f"  {N:>3} {s:>4} {cs[s]:>13,} {lb:>15.2f} {cs[s]/lb:>8.3f} {str(ok):>6}")
print(f"  shells checked: {tot}   violations: {bad}")

print();print("="*78);print("C2. Delta for the singleton-prefix class a=j, j=N/2, s=alpha N");print("="*78)
d1=ALPHA*H2(1/ALPHA); d2=(ALPHA-0.5)*H2(0.5/(ALPHA-0.5)); D=d1-d2
print(f"  alpha*H2(1/alpha)                      = {d1:.9f}   (= h)")
print(f"  (alpha-1/2)*H2((1/2)/(alpha-1/2))      = {d2:.9f}")
print(f"  Delta                                  = {D:.9f}   (claimed 0.425486)")
print(f"  |diff| = {abs(D-0.425486):.2e}")
print(f"\n  {'kappa':>7} {'Delta*kappa (suppression/B)':>27} {'d/B = alpha*kappa-1':>21} {'net exponent/B':>16} {'harmless?':>10}")
for k in (0.65,0.70,0.80,0.90,1.00):
    sup=D*k; dd=ALPHA*k-1; net=dd-sup
    print(f"  {k:>7.2f} {sup:>27.6f} {dd:>21.6f} {net:>16.6f} {'YES' if net<0 else 'NO':>10}")
print("  => at kappa=0.65 the a=j singleton-prefix class is asymptotically harmless by pure")
print("     combinatorics (net -0.246340/B); at kappa=0.90 it is not (net +0.043529/B).")

print();print("="*78);print("C3. The suffix pair-counting form and the capacity bound");print("="*78)
print("  Claim: for a < B, with M_v = 2^{b+1}, H = 2^{B-a}, y_v = 3^{-j} r_v mod M_v,")
print("         Q_hi(v) = floor(y_v / H)  and  q = M_v/H = 2^{s+1-B}.")
print("  Also sum_x h(x)^2 = #{(v,v') : floor(y_v/H) = floor(y_v'/H)} <= (H/2) * |V|,")
print("  since the y_v are distinct odd residues and each interval holds <= H/2 odd values.")
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
B,N=16,15; badQ=badcap=badodd=nc=0
for j in (4,6,8):
    G=defaultdict(lambda:{"v":set()})
    for w in words(N):
        s,_=SC(w)
        if s+1-B<1: continue
        a,_=SC(w[:j])
        if a>=B: continue
        G[(s,a)]["v"].add(w[j:])
    for (s,a),D_ in G.items():
        d=s+1-B; q=1<<d; mod=1<<(s+1); inv=pow(3,-j,mod); nc+=1
        Mv=None; Hh=1<<(B-a); h=defaultdict(int); ys=[]
        for v in D_["v"]:
            b,Cv=SC(v); rv=rz(len(v),b,Cv); Mv=1<<(b+1)
            direct=((inv*(1<<a)*rv)%mod)>>B
            y=(pow(3,-j,Mv)*rv)%Mv
            if direct != y//Hh: badQ+=1
            if y%2==0: badodd+=1
            ys.append(y); h[direct]+=1
        if Mv//Hh != q: badQ+=1
        S2=sum(c*c for c in h.values())
        if S2 > Hh//2*len(D_["v"]): badcap+=1
print(f"  classes checked: {nc}   Q_hi/q-form violations: {badQ}   y_v even: {badodd}"
      f"   capacity-bound violations: {badcap}")
print();print(f"  Required: delta_U + delta_V < 2(1-sigma*) = {2*(1-SS):.9f}")
print(f"  and delta_U + delta_V = 2(1 - tau_eff), so this is the SAME condition as tau_eff > sigma*.")
print(f"  Interpretation correction: a finite tau_eff below sigma* is compatible with a uniform")
print(f"  exponent tau at constant cost C >= q^(tau - tau_eff); e.g. q=256, tau=0.96, tau_eff=0.830")
print(f"  gives C >= {2**(8*(0.96-0.830)):.3f}.")
