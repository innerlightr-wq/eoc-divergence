#!/usr/bin/env python3
"""O2 -- confinement mass, exact integer arithmetic, prefix-sum transfer recursion.

Letters i.i.d. geometric(1/2) under Haar (Phase 0, F1).  With w_k[S] = number of
words of length k and total S obeying the constraint at every prefix,

    w_{k+1}[S'] = sum_{S < S'} w_k[S]          (letters d >= 1)

restricted to the admissible S' at step k+1.  All counts are exact integers;
A[k] = bitlen(q^k) - 1 = floor(k log2 q) exactly, so no floating point enters a
decision.  p_N = sum_S w_N[S] 2^{-S}, reported as log2 p_N in exact arithmetic.
"""
import math
from fractions import Fraction

def Afloor(q, N):
    out = [0] * (N + 1); p = 1
    for k in range(1, N + 1):
        p *= q; out[k] = p.bit_length() - 1
    return out

def log2_frac(fr):
    return math.log2(fr.numerator) - math.log2(fr.denominator)

def survival(q, N, side, slack=None):
    """side='lower': S_k <= A[k] for all k.  side='upper': S_k >= A[k]+1 for all k."""
    A = Afloor(q, N)
    if slack is None:
        slack = int(max(0.0, 2 - math.log2(q)) * N) + 300
    hi = A[N] + (0 if side == "lower" else slack)
    w = [0] * (hi + 2); w[0] = 1
    lo_prev = 0
    res = []
    for k in range(1, N + 1):
        pre = [0] * (hi + 2)
        acc = 0
        for S in range(0, hi + 1):
            acc += w[S]; pre[S] = acc          # pre[S] = sum_{j<=S} w[j]
        nw = [0] * (hi + 2)
        if side == "lower":
            lo, cap = 1, A[k]
        else:
            lo, cap = A[k] + 1, hi
        for S2 in range(lo, cap + 1):
            nw[S2] = pre[S2 - 1]
        w = nw
        p = Fraction(0)
        for S in range(0, hi + 1):
            if w[S]:
                p += Fraction(w[S], 1 << S)
        res.append(p)
    return res

def H2(x):
    return -x * math.log2(x) - (1 - x) * math.log2(1 - x)

def show(tag, q, side, N, res):
    a = math.log2(q)
    I = a * (1 - H2(1 / a))
    print(f"-- {tag}: q={q}, alpha={a:.10f}, {side} side; reference rate "
          f"I(alpha)=alpha(1-H2(1/alpha))={I:.10f}")
    print("      N        p_N            -log2 p_N     -log2p/N     "
          "local slope     slope - 1.5*dlog2N/dN")
    prev = None
    for N0 in (25, 50, 100, 200, 300, 400, 500):
        if N0 > N: break
        L = -log2_frac(res[N0 - 1])
        line = f"  {N0:5d}   {float(res[N0-1]):.6e}   {L:12.6f}   {L/N0:.8f}"
        if prev:
            n1, L1 = prev
            sl = (L - L1) / (N0 - n1)
            corr = 1.5 * (math.log2(N0) - math.log2(n1)) / (N0 - n1)
            line += f"   {sl:.8f}     {sl - corr:.8f}"
        print(line)
        prev = (N0, L)
    print()

if __name__ == "__main__":
    N = 500
    print("=" * 96)
    print("A and B (3x+1, 3x-1) -- identical by F2.  Confinement R_k<=0 is the LARGE DEVIATION.")
    print("=" * 96)
    show("A/B lower (zero-confinement)", 3, "lower", N, survival(3, N, "lower"))
    show("A/B upper (anti-confinement)", 3, "upper", N, survival(3, N, "upper"))
    print("=" * 96)
    print("C (5x+1) -- the mirror: confinement is TYPICAL, anti-confinement is the large deviation.")
    print("=" * 96)
    show("C lower (zero-confinement)", 5, "lower", N, survival(5, N, "lower"))
    show("C upper (anti-confinement)", 5, "upper", N, survival(5, N, "upper"))
