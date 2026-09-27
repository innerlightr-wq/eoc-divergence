#!/usr/bin/env python3
"""Phase C: verify the exact cylinder decomposition and size the unresolved signed error.

Claim (brief, verified here):  with X = 2^B, M = X-1, q_w = 2^(S_w+1), r_w odd,
    q_w <= X  ->  |C(w) cap [1,M]| = X/q_w   EXACTLY
    q_w >  X  ->  |C(w) cap [1,M]| = 1_{r_w < X}
so           A_{N,M} - (X/2) p_N = sum_{w : q_w > X} ( 1_{r_w < X} - X/q_w ).
Grouped by shell s = S_w (so d = s+1-B is constant on a shell) and writing
T_w = floor(r_w / 2^B) in [0, 2^d):
    = sum_{s >= B} ( #{w in shell s : T_w = 0} - #shell(s) * 2^(-d) ).
Everything exact (Fraction); floats only for display.
"""
from fractions import Fraction
import math
def enumerate_words(N):
    stack=[(0,0,0)]
    while stack:
        k,S,C=stack.pop()
        if k==N: yield (S,C); continue
        Cn=3*C+(1<<S); a=1
        while (1<<(S+a)) <= 3**(k+1):
            stack.append((k+1,S+a,Cn)); a+=1

print(f"{'B':>4} {'N':>4} {'shells s>=B':>12} {'words q>X':>12} {'exact err':>16} {'(X/2)p_N':>16} {'Q-1':>11} {'id ok':>6}")
for B in (12,16,20,24,28):
    N=math.ceil(0.65*B); X=1<<B; M=X-1
    p=Fraction(0); A=0; err=Fraction(0); inv={}
    shells={}
    nbig=0
    for S,C in enumerate_words(N):
        p+=Fraction(1,1<<S)
        q=1<<(S+1)
        if S not in inv: inv[S]=pow(3,-N,q)
        r=((1<<S)-C)*inv[S]%q
        if r==0: r=q
        assert r%2==1, "realizer must be odd"
        cnt = (M-r)//q+1 if r<=M else 0
        A+=cnt
        if q<=X:
            assert cnt==X//q, f"complete-cylinder contribution wrong: {cnt} vs {X//q}"
        else:
            nbig+=1
            d=S+1-B
            T=r>>B
            assert 0<=T<(1<<d)
            assert cnt==(1 if r<X else 0), "post-fresh-bit contribution wrong"
            err += Fraction(1 if r<X else 0) - Fraction(X,q)
            sh=shells.setdefault(S,[0,0,d]); sh[0]+=1; sh[1]+= (1 if T==0 else 0)
    denom=Fraction(X,2)*p
    lhs=Fraction(A)-denom
    ok = (lhs==err)
    # shell-grouped form
    err2=sum(Fraction(v[1])-Fraction(v[0],1<<v[2]) for v in shells.values())
    ok2 = (err2==err)
    print(f"{B:>4} {N:>4} {len(shells):>12} {nbig:>12,} {float(err):>16.6f} {float(denom):>16.2f}"
          f" {float(lhs/denom):>11.6f} {str(ok and ok2):>6}",flush=True)

print()
print("=== shell-resolved signed discrepancy at B=24, N=16 ===")
B=24;N=16;X=1<<B;M=X-1;inv={}
rows=[]
for S,C in enumerate_words(N):
    q=1<<(S+1)
    if q<=X: continue
    if S not in inv: inv[S]=pow(3,-N,q)
    r=((1<<S)-C)*inv[S]%q
    if r==0: r=q
    d=S+1-B; T=r>>B
    while len(rows)<=S: rows.append([0,0,0])
    rows[S][0]+=1; rows[S][1]+= (1 if T==0 else 0); rows[S][2]=d
print(f"  {'s':>4} {'d':>3} {'#shell':>12} {'#T=0':>10} {'main #shell/2^d':>16} {'signed D_s':>12} {'D_s/sqrt(#)':>12}")
tot=Fraction(0)
for s,(n,z,d) in enumerate(rows):
    if n==0: continue
    main=Fraction(n,1<<d); D=Fraction(z)-main; tot+=D
    print(f"  {s:>4} {d:>3} {n:>12,} {z:>10,} {float(main):>16.4f} {float(D):>12.4f}"
          f" {float(D)/math.sqrt(n):>12.4f}")
print(f"  total signed error = {float(tot):.6f}")
print()
print("  What a lemma must deliver: |sum_s D_s| <= eta-budget * (X/2) p_N with")
print("  log2(1 + |sum D_s|/((X/2)p_N)) <= eta*B,  eta < 0.001512625 at kappa=0.65.")
