#!/usr/bin/env python3
"""Phase B: exact Q_{N,M} = A_{N,M} / ((X/2) p_N) at N = ceil(kappa*B), M = 2^B - 1.

A_{N,M} = sum over zero-confined words w of |C(w) cap [1,M]|, C(w) = r_w + 2^(S_w+1) Z.
p_N     = sum_w 2^(-S_w)  (exact Fraction).
Everything exact; floats only for reported logs.  Cross-checked against direct odd-seed
enumeration for B <= 22.
"""
from fractions import Fraction
import math, sys
ALPHA=math.log2(3)

def enumerate_words(N):
    """yield (S, C) for every zero-confined word of length N, iteratively (no recursion limit)"""
    stack=[(0,0,0)]
    while stack:
        k,S,C=stack.pop()
        if k==N: yield (S,C); continue
        Cn=3*C+(1<<S); a=1
        while (1<<(S+a)) <= 3**(k+1):
            stack.append((k+1,S+a,Cn)); a+=1

def AN_pN(N,B):
    """exact A_{N,2^B-1} and p_N"""
    M=(1<<B)-1
    A=0; p=Fraction(0); inv={}
    for S,C in enumerate_words(N):
        p += Fraction(1,1<<S)
        q=1<<(S+1)
        if S not in inv: inv[S]=pow(3,-N,q)
        r=((1<<S)-C)*inv[S]%q
        if r==0: r=q
        if r<=M: A += (M-r)//q + 1
    return A,p

def A_direct(N,B):
    M=(1<<B)-1; cnt=0
    for m0 in range(1,M+1,2):
        m=m0;S=0;ok=True
        for j in range(1,N+1):
            x=3*m+1;a=(x&-x).bit_length()-1;S+=a;m=x>>a
            if (1<<S)>3**j: ok=False;break
        cnt+=ok
    return cnt

KAPPA=Fraction(13,20)
print(f"kappa = {KAPPA} = {float(KAPPA)};  eta ceiling I0*(kappa-1/alpha) = 0.001512625")
I0=ALPHA-ALPHA*math.log2(ALPHA)+(ALPHA-1)*math.log2(ALPHA-1)
print(f"baseline exponent 1-I0/alpha = {1-I0/ALPHA:.12f}")
print()
print(f"{'B':>4} {'N':>4} {'words':>12} {'A_{N,M}':>16} {'(X/2)p_N':>18} {'Q':>12} {'log2 Q':>9} {'direct A':>16} {'agree':>6}")
rows=[]
for B in (12,16,20,24,28):
    N=math.ceil(float(KAPPA)*B)
    nw=sum(1 for _ in enumerate_words(N))
    A,p=AN_pN(N,B)
    X=1<<B; denom=Fraction(X,2)*p
    Q=Fraction(A,1)/denom
    dA = A_direct(N,B) if B<=22 else None
    agree = ("yes" if dA==A else "NO") if dA is not None else "-"
    print(f"{B:>4} {N:>4} {nw:>12,} {A:>16,} {float(denom):>18.4f} {float(Q):>12.6f}"
          f" {math.log2(float(Q)):>9.5f} {str(dA) if dA is not None else 'skipped':>16} {agree:>6}",flush=True)
    rows.append((B,N,float(Q)))
print()
print("=== growth diagnostic: is log2 Q consistent with eta*B for eta>0? ===")
print(f"{'B':>4} {'log2 Q':>10} {'log2Q / B':>12} {'vs eta ceiling':>16}")
CEIL=0.001512625492
for B,N,Q in rows:
    l=math.log2(Q)
    print(f"{B:>4} {l:>10.5f} {l/B:>12.6f} {'EXCEEDS' if l/B>CEIL else 'within':>16}")
print()
print("A negative log2 Q means Q < 1, i.e. the count is BELOW the complete-cylinder main term;")
print("the target A <= C*(X/2)p_N then holds with C = 1 at that (B,N).")
