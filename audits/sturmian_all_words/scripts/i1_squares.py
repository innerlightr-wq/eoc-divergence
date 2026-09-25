#!/usr/bin/env python3
"""I1 — do ALL Sturmian words begin in squares of unbounded length?

For each (slope, intercept) we list the half-lengths L for which the prefix of
length 2L is a square, and the best initial exponent e(L) = (L + m(L))/L.
The Liouville step of I4 needs e(L) > max(1, gamma*log2 3) for infinitely many L.
"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sturmian import *
from decimal import Decimal, getcontext

getcontext().prec = 250
LOG2_3 = Decimal(3).ln() / Decimal(2).ln()

SLOPES = {
    "log_3 2  = 0.6309 (critical beta)": log3_2(),
    "1/phi    = 0.6180": from_cf([0] + [1] * 400),
    "sqrt2-1  = 0.4142": from_cf([0] + [2] * 300),
    "[0;1,97,1,1,...] = 0.9899": from_cf([0, 1, 97] + [1] * 300),
}

N = 6000          # word length
LMAX = N // 2

def report(name, g, rho_label, r):
    s = word(g, r, N)
    marg = safety_margin(g, r, N)
    sq = [L for L in range(1, LMAX + 1) if is_square_prefix(s, L)]
    gamma = Decimal(g) / (1 << P)
    thr = float(max(Decimal(1), gamma * LOG2_3))
    # best exponent in each dyadic window of L
    best = []
    for lo in (1, 16, 64, 256, 1024):
        hi = min(lo * 4, LMAX)
        cand = [(L + initial_period_run(s, L)) / L for L in range(lo, hi + 1)]
        best.append((lo, hi, max(cand) if cand else 0.0))
    print(f"  intercept {rho_label:<22} margin {marg.bit_length():>4}b   "
          f"squares at L = {sq[:9]}{' ...' if len(sq) > 9 else ''}")
    print(f"      threshold max(1, gamma*log2 3) = {thr:.4f};  best e(L) per window: "
          + "  ".join(f"[{lo}-{hi}]:{b:.3f}" for lo, hi, b in best))
    return sq, thr, best

for name, g in SLOPES.items():
    print("=" * 96)
    print(f"SLOPE {name}")
    print("=" * 96)
    rng = random.Random(20260925)
    intercepts = [("0 (characteristic)", 0),
                  ("{3*gamma}", (3 * g) % ONE),
                  ("1/2", ONE // 2),
                  ("1/pi-ish", int(Decimal("0.3183098861837907") * (1 << P))),
                  ("random A", rng.randrange(ONE)),
                  ("random B", rng.randrange(ONE))]
    for lab, r in intercepts:
        report(name, g, lab, r)
    print()
