#!/usr/bin/env python3
"""The cycles of each map, their valuation words, and which side of the line they sit on.

For a cycle of length L with valuation total S, the aggregate identity at the period gives
   A/C (shift +1): m (2^S - q^L) = C_L > 0  =>  2^S > q^L  =>  S/L > log2 q
   B   (shift -1): m (q^L - 2^S) = C_L > 0  =>  q^L > 2^S  =>  S/L < log2 q
for POSITIVE m.  So the sign of the shift decides which side of log2 q a positive
cycle must lie on.  This is the cycle-drift theorem (formalized for A as
Divergence.cycle_drift) together with the signed marker.
"""
from math import log2

def v2(n):
    return (n & -n).bit_length() - 1

def orbit_cycle(x, q, r):
    seen, seq = {}, []
    while x not in seen:
        seen[x] = len(seq)
        seq.append(x)
        y = q * x + r
        x = y >> v2(y)
    i = seen[x]
    return seq[i:]

def word(cy, q, r):
    return [v2(q * x + r) for x in cy]

MAPS = {"A (3x+1)": (3, 1, [1]),
        "B (3x-1)": (3, -1, [1, 5, 17]),
        "C (5x+1)": (5, 1, [1, 13, 17])}

for name, (q, r, seeds) in MAPS.items():
    a = log2(q)
    print(f"{name}   log2 q = {a:.10f}   (rare side is "
          f"{'BELOW' if a < 2 else 'ABOVE'} the line, since E[a]=2)")
    for s in seeds:
        cy = orbit_cycle(s, q, r)
        w = word(cy, q, r)
        S, L = sum(w), len(w)
        side = "ABOVE" if S / L > a else "BELOW"
        rare = (a < 2 and side == "BELOW") or (a > 2 and side == "ABOVE")
        print(f"   cycle {str(cy):<44} word {str(w):<24} L={L} S={S}  S/L={S/L:.6f}  "
              f"{side} log2 q   {'<== ON THE RARE SIDE' if rare else ''}")
    print()
print("Consequence: a permanently 'rare-side' positive seed exists for B and for C as an")
print("explicit cycle element, and cannot exist for A unless (DE) fails -- which is exactly")
print("why the record ladder of A is non-degenerate and those of B and C are not.")
