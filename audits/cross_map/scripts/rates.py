#!/usr/bin/env python3
"""Item 2 -- the rare-side exponential rate for each map.

Under Haar the accelerated letters are i.i.d. geometric(1/2); equivalently the
parity word is i.i.d. Bernoulli(1/2).  Confinement is a constraint on the
ones-density of the parity word at the critical value

        beta = 1/alpha = log_q 2 ,        alpha = log2 q,

so Sanov/Cramer gives a rate D(beta || 1/2) = 1 - H2(beta) bits PER PARITY SYMBOL.
A word of N accelerated steps has S_N ~ alpha*N parity symbols, so per accelerated
step the rate is

        I(q) = alpha * D(beta || 1/2) = D(beta || 1/2) / beta = alpha (1 - H2(1/alpha)).

The rate depends on q only -- not on r, and not on which side is rare, because the
rare side is always the one away from density 1/2.

The exact dyadic mass is computed by the integer prefix-sum transfer recursion
(A[k] = bitlen(q^k) - 1, exact), and the measured local slope is compared with I(q)
after removing the 3/2*log2 N correction.
"""
import math
from fractions import Fraction


def H2(x):
    return -x * math.log2(x) - (1 - x) * math.log2(1 - x)


def Afloor(q, N):
    out = [0] * (N + 1)
    p = 1
    for k in range(1, N + 1):
        p *= q
        out[k] = p.bit_length() - 1
    return out


def survival(q, N, side, slack=None):
    """side='lower': S_k <= A[k] for all k;  side='upper': S_k >= A[k]+1 for all k."""
    A = Afloor(q, N)
    if slack is None:
        slack = int(max(0.0, 2 - math.log2(q)) * N) + 300
    hi = A[N] + (0 if side == "lower" else slack)
    w = [0] * (hi + 2)
    w[0] = 1
    res = []
    for k in range(1, N + 1):
        pre = [0] * (hi + 2)
        acc = 0
        for S in range(hi + 1):
            acc += w[S]
            pre[S] = acc
        nw = [0] * (hi + 2)
        lo, cap = (1, A[k]) if side == "lower" else (A[k] + 1, hi)
        for S2 in range(lo, cap + 1):
            nw[S2] = pre[S2 - 1]
        w = nw
        res.append(sum(Fraction(c, 1 << S) for S, c in enumerate(w) if c))
    return res


def log2_frac(fr):
    return math.log2(fr.numerator) - math.log2(fr.denominator)


print("=" * 92)
print("The rate, in closed form")
print("=" * 92)
print(f"{'q':>3s}  {'alpha=log2 q':>14s}  {'beta=1/alpha':>13s}  {'H2(beta)':>10s}  "
      f"{'D(beta||1/2)':>13s}  {'I(q)=D/beta':>13s}   rare side")
for q in (3, 5, 7):
    a = math.log2(q)
    b = 1 / a
    D = 1 - H2(b)
    print(f"{q:3d}  {a:14.10f}  {b:13.10f}  {H2(b):10.7f}  {D:13.10f}  {D/b:13.10f}   "
          f"{'lower (below the line)' if q < 4 else 'upper (above the line)'}")
print()
print("I(3) = 0.0793186128 is Occupation.confined_mass_rate (formalized).")
print("The rate is a function of q alone: r does not appear, so A and B share it,")
print("and C and D share it.")
print()

N = 500
print("=" * 92)
print("Exact transfer recursion, and the measured rate")
print("=" * 92)
print(f"{'q':>3s} {'side':>6s}   {'N':>5s}   {'p_N':>14s}   {'-log2 p_N':>12s}   "
      f"{'local slope':>12s}   {'slope - 1.5 dlog2N/dN':>21s}")
for q, side in ((3, "lower"), (5, "upper"), (7, "upper")):
    res = survival(q, N, side)
    prev = None
    for N0 in (100, 200, 300, 400, 500):
        L = -log2_frac(res[N0 - 1])
        line = f"{q:3d} {side:>6s}   {N0:5d}   {float(res[N0-1]):14.6e}   {L:12.6f}"
        if prev:
            n1, L1 = prev
            sl = (L - L1) / (N0 - n1)
            corr = 1.5 * (math.log2(N0) - math.log2(n1)) / (N0 - n1)
            line += f"   {sl:12.8f}   {sl - corr:21.8f}"
        print(line)
        prev = (N0, L)
    a = math.log2(q)
    print(f"{'':3s} {'':6s}   reference I(q) = {a*(1-H2(1/a)):.10f}")
    print()
