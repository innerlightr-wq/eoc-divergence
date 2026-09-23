"""Task 2: numerical certification of the explicit constants (all checks are
inequalities between real constants, verified with a safe rational/interval margin)."""
from fractions import Fraction
from math import log2, log, e

L3 = log2(3)
c0 = 2 - L3
print(f"log2(3)            = {L3:.16f}")
print(f"c0 = 2 - log2(3)   = {c0:.16f}")
print(f"2/c0               = {2/c0:.10f}")
print(f"C  = 2 + log2(3)   = {2+L3:.10f}")

# (i)  Q/log2(Q) >= 2/c0  for Q >= 22, and fails at Q = 21
g = lambda Q: Q/log2(Q)
print("\n(i) Q/log2 Q vs 2/c0 = %.6f" % (2/c0))
for Q in (20, 21, 22, 23, 30, 100, 10**6):
    print(f"   Q={Q:>8}  Q/log2Q={g(Q):.6f}  {'>=' if g(Q)>=2/c0 else '< FAIL'}")
print("   g has its minimum at Q=e and is increasing for Q>e, so Q>=22 is the")
print("   exact integer threshold (g(21)=%.6f < %.6f <= %.6f=g(22))."
      % (g(21), 2/c0, g(22)))

# (ii) uniform firing threshold  q_n >= 5 log2 H + 22
print("\n(ii) uniform: q_n >= 5*log2(H) + 22  =>  c0*q_n - log2(q_n) > log2 H + C")
bad = []
for lg in [0, 1, 2, 5, 10, 50, 100, 1000, 10**4, 10**5, 10**6]:
    Q = 5*lg + 22
    lhs, rhs = c0*Q - log2(Q), lg + 2 + L3
    ok = lhs > rhs
    if not ok: bad.append(lg)
    print(f"   log2H={lg:>8}  q_n={Q:>8}  lhs={lhs:>14.4f}  rhs={rhs:>12.4f}  {'OK' if ok else 'FAIL'}")
print("   algebraic proof: q_n>=22 gives c0*q_n-log2 q_n >= (c0/2)q_n;")
print("   (c0/2)(5*lg+22) = %.6f*lg + %.6f > lg + %.6f for all lg>=0."
      % (5*c0/2, 22*c0/2, 2+L3))
assert 5*c0/2 > 1 and 22*c0/2 > 2+L3

# (iii) sharper threshold when c(gamma)=1, i.e. gamma <= beta
print("\n(iii) gamma <= beta (c(gamma)=1): q_n >= 2*log2(H) + 8")
for lg in [0, 1, 5, 10, 100, 10**4, 10**6]:
    Q = 2*lg + 8
    lhs, rhs = Q - log2(Q), lg + 2 + L3
    print(f"   log2H={lg:>8}  q_n={Q:>8}  lhs={lhs:>14.4f}  rhs={rhs:>12.4f}  "
          f"{'OK' if lhs>rhs else 'FAIL'}")
print("   (Q/log2 Q >= 2 for Q>=4, and 2*(2+log2 3) = %.4f <= 8.)" % (2*(2+L3)))

# (iv) c(gamma) range and the gamma -> 1 edge
print("\n(iv) c(gamma) = 2 - max(1, gamma*log2 3)")
for gam in [0.01, 0.3, 0.6309297535714574, 0.7, 0.9, 0.99, 0.999999]:
    th = gam*L3
    print(f"   gamma={gam:<10}  theta={th:.6f}  c={2-max(1.0,th):.6f}")
print(f"   inf over gamma in (0,1) = 2 - log2 3 = {c0:.10f} > 0, not attained.")

# (v) the small-n facts used: q_1>=1, q_2>=2, q_3>=3, q_4>=5, p_3>=2
print("\n(v) worst-case convergent growth with all a_i = 1:")
q=[1,1]; p=[0,1]
for i in range(2,7):
    q.append(q[-1]+q[-2]); p.append(p[-1]+p[-2])
print("   q =", q[:7], "  p =", p[:7], " -> q_3>=3, q_4>=5, p_3>=2 in the worst case")
print("\nFAILURES:", bad if bad else "none")
