#!/usr/bin/env python3
"""Verify the explicit thin-band lemma and the two corrections to my report."""
import math
from math import comb
from fractions import Fraction
ALPHA=math.log2(3); I0=ALPHA-ALPHA*math.log2(ALPHA)+(ALPHA-1)*math.log2(ALPHA-1); SS=1-I0/ALPHA
H2=lambda x:-x*math.log2(x)-(1-x)*math.log2(1-x)
F=lambda th: th*H2(1/th)
G=lambda z: (0.5+z)*H2(0.5/(0.5+z)) if z>0 else 0.0
Dd=lambda d,th: F(th)-G(d)-G(th-1-d)

print("="*78);print("S1. Sign-label correction to my report");print("="*78)
print("  My numbers were net = (alpha*kappa-1) - kappa*Delta; my PROSE wrote it as")
print("  'Delta*kappa - (alpha*kappa-1)', which is the negative. Numbers right, label wrong.")
D0=0.425485676
for k in (0.65,0.80,0.90):
    print(f"   kappa={k}: alpha*k-1-k*Delta = {ALPHA*k-1-k*D0:+.6f}   "
          f"k*Delta-(alpha*k-1) = {k*D0-(ALPHA*k-1):+.6f}")
print(f"  Delta_0(alpha) via the general formula = {Dd(1e-12,ALPHA):.9f}  (endpoint case, cf 0.425486)")

print();print("="*78);print("S2. The entropy gap and gamma");print("="*78)
print(f"  {'delta':>7} {'Delta_delta(alpha)':>19} {'kappa ceiling 1/(a-D)':>23} {'gamma(0.65,delta)':>18}")
for d in (1e-12,0.01,0.05,0.10):
    Dv=Dd(d,ALPHA); ceil=1/(ALPHA-Dv); g=1-0.65*(ALPHA-Dv)
    print(f"  {d:>7.2f} {Dv:>19.12f} {ceil:>23.6f} {g:>18.12f}")
print(f"  claimed: Delta_0.1(alpha)=0.130833546677096, gamma(0.65,0.1)=0.054816179871361")
print(f"  mine   : Delta_0.1(alpha)={Dd(0.10,ALPHA):.15f}, gamma={1-0.65*(ALPHA-Dd(0.10,ALPHA)):.15f}")

print();print("="*78);print("S3. Monotonicity: is theta = alpha the worst shell?");print("="*78)
print("  d/dtheta[theta-Delta_delta(theta)] = log2[ 2(theta-1)(theta-1/2-delta) / (theta(theta-1-delta)) ]")
print("  and numerator-denominator = (theta-1)^2 + delta(2-theta) > 0 on 1+delta<theta<=alpha.")
dd=0.10; bad=0
for i in range(1,400):
    th=1+dd+1e-9+(ALPHA-1-dd)*i/400
    num=2*(th-1)*(th-0.5-dd); den=th*(th-1-dd)
    if num-den <= 0: bad+=1
    if abs((num-den)-((th-1)**2+dd*(2-th)))>1e-9: bad+=1
print(f"  algebraic identity and positivity checked at 399 points: violations = {bad}")
vals=[(th, th-Dd(dd,th)) for th in [1+dd+0.01+(ALPHA-1-dd-0.01)*i/50 for i in range(51)]]
inc=all(vals[i+1][1]>vals[i+1-1][1] for i in range(len(vals)-1))
print(f"  theta - Delta_delta(theta) increasing on the range: {inc}"
      f"   (min {vals[0][1]:.6f} at theta={vals[0][0]:.4f}, max {vals[-1][1]:.6f} at theta={vals[-1][0]:.4f})")

print();print("="*78);print("S4. EXACT finite evaluation of bound (2): q*N*T_delta / C(s-1,N-1)");print("="*78)
def bound(B,kappa=Fraction(13,20),delta=Fraction(1,10)):
    N=math.ceil(kappa*B); j=N//2; cap=math.floor(delta*N)
    best=Fraction(0); arg=None
    for s in range(B, math.floor(ALPHA*N)+1):
        e=s-N
        if e<0: continue
        T=0
        for k in range(0,e+1):
            if min(k,e-k)>cap: continue
            a=j+k; b=(N-j)+(e-k)
            if a-1<j-1 or b-1<N-j-1: continue
            T+=comb(a-1,j-1)*comb(b-1,N-j-1)
        den=comb(s-1,N-1)
        if den==0: continue
        val=Fraction((1<<(s+1-B))*N*T, den)
        if val>best: best=val; arg=s
    return best,arg,N
print(f"  {'B':>5} {'N':>5} {'max bound over unresolved shells':>34} {'argmax s':>9} {'claimed':>14}")
claims={100:0.691826,200:0.0375106,320:0.000161790,640:1.72629e-9}
for B in (100,200,320,640):
    bb,ss,N=bound(B)
    print(f"  {B:>5} {N:>5} {float(bb):>34.6g} {ss:>9} {claims[B]:>14.6g}"
          f"   ratio {float(bb)/claims[B]:.6f}")

print();print("="*78);print("S5. Is the SUFFIX-side thin band empty for confined words at kappa=0.65?");print("="*78)
print("  prefix confinement a <= alpha*j forces (e-k)/N >= 1/kappa - (alpha+1)/2 for j=N/2.")
for k in (0.65,0.70,0.80,0.90):
    lb=1/k-(ALPHA+1)/2
    print(f"   kappa={k}: (e-k)/N >= {lb:+.6f}"
          f"   {'> delta=0.1 so suffix band EMPTY' if lb>0.1 else 'suffix band may be nonempty'}")
print("  => my 'symmetric extremes' claim was wrong for CONFINED words: the unrestricted")
print("     binomial envelope is symmetric, the confined family is not.  Corrected.")
