#!/usr/bin/env python3
"""Verify every constant against the repository's OWN definitions.

Lean (EOC/TaoLike/PersistenceModel.lean:422):
    I0 = alpha - alpha*logb 2 alpha + (alpha-1)*logb 2 (alpha-1)
Lean (EOC/Confinement.lean:9):  alpha = logb 2 3
Lean (ExceptionalPowerBound.lean:124): 1 - I0/alpha = binEntropy(1/alpha)/log 2
"""
from decimal import Decimal, getcontext
getcontext().prec = 40
import math
mp.dps = 40
L2 = log(2)
def lg(x): return log(x)/L2
alpha = lg(3)
I0 = alpha - alpha*lg(alpha) + (alpha-1)*lg(alpha-1)
inv_a = 1/alpha
H2 = lambda x: -x*lg(x) - (1-x)*lg(1-x)
print(f"alpha        = {alpha}")
print(f"1/alpha      = {inv_a}")
print(f"I0 (Lean def)= {I0}")
print(f"alpha*(1-H2(1/alpha)) = {alpha*(1-H2(inv_a))}   [alternative form]")
print(f"  agree to {abs(I0-alpha*(1-H2(inv_a)))}")
print()
print(f"H2(1/alpha)  = {H2(inv_a)}")
print(f"1 - I0/alpha = {1-I0/alpha}")
print(f"  agree to {abs(H2(inv_a)-(1-I0/alpha))}   [Lean one_sub_I0_div_alpha_eq]")
print()
print("=== brief's proposed constants, checked ===")
for name, claimed, actual in (("I0", mpf("0.0793186128"), I0),
                              ("H2(1/alpha)", mpf("0.949955527"), H2(inv_a)),
                              ("1-I0*0.65", mpf("0.948442902"), 1-I0*mpf("0.65"))):
    print(f"  {name:>12}: claimed {claimed}  actual {actual}  diff {abs(claimed-actual)}")
print()
print("=== THE GAIN at kappa, max possible (eta -> 0) ===")
print(f"   baseline exponent (unconditional, Lean) = 1 - I0/alpha = {1-I0/alpha}")
print(f"   {'kappa':>8} {'1-I0*kappa':>18} {'max gain I0*(kappa-1/alpha)':>28}")
for k in ("0.65","0.70","0.80","0.90","1.00","1.20","1.50"):
    kk=mpf(k)
    print(f"   {k:>8} {1-I0*kk!s:>18.12} {I0*(kk-inv_a)!s:>28.12}")
print()
eta=mpf("0.001"); k=mpf("0.65")
print(f"   illustrative eta=0.001 at kappa=0.65: exponent 1-I0*kappa+eta = {1-I0*k+eta}")
print(f"   brief claims 0.949442902; diff = {abs(mpf('0.949442902')-(1-I0*k+eta))}")
print(f"   net gain vs baseline = {(1-I0/alpha)-(1-I0*k+eta)}")
print(f"   eta must satisfy eta < I0*(kappa-1/alpha) = {I0*(k-inv_a)}")
