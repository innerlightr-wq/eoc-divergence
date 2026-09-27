#!/usr/bin/env python3
"""The sign-alignment criterion, checked on every map in the brief.

For T(x) = (qx + r)/2^{v2(qx+r)} on odd positive x, the aggregate identity is

    2^{S_n} m_n = q^n m_0 + r C_n ,   C_n = sum_{i<n} q^{n-1-i} 2^{S_i} > 0  (n >= 1).

At a period: m (2^S - q^L) = r C_L, so for m > 0,  sign(S/L - log2 q) = sign(r).
The RARE side (the one against the drift of R_n = S_n - n log2 q, whose mean
increment is 2 - log2 q) is:  S/L <= log2 q  if q < 4,  S/L >= log2 q  if q > 4.
Hence a positive cycle shelters on the rare side iff sign(r) = sign(q - 4).

All arithmetic is exact integers.
"""
from math import log2

MAPS = [("A  3x+1", 3, 1), ("B  3x-1", 3, -1), ("C  5x+1", 5, 1), ("D  5x-1", 5, -1),
        ("   3x+5", 3, 5), ("   7x+1", 7, 1), ("   7x-1", 7, -1)]


def v2(n):
    return (n & -n).bit_length() - 1


def step(x, q, r):
    y = q * x + r
    return y >> v2(y), v2(y)


def find_cycles(q, r, limit):
    """All cycles met by orbits of odd x <= limit that stay below a guard."""
    seen, cycles = {}, []
    GUARD = 1 << 200
    for x0 in range(1, limit + 1, 2):
        path, pos = [], {}
        x = x0
        while x not in pos and x not in seen and x < GUARD and x > 0:
            pos[x] = len(path)
            path.append(x)
            x, _ = step(x, q, r)
        if x in pos:                                  # new cycle found
            cyc = path[pos[x]:]
            key = min(cyc)
            if key not in [min(c) for c in cycles]:
                cycles.append(cyc)
        for y in path:
            seen[y] = True
    return cycles


print(f"{'map':10s} {'q':>2s} {'r':>3s}  log2 q      rare side   "
      f"cycles (min element, L, S, S/L)                     shelter?")
print("-" * 118)
for name, q, r in MAPS:
    a = log2(q)
    rare = "S/L <= a" if q < 4 else "S/L >= a"
    cys = find_cycles(q, r, 20001)
    desc, shelter_any = [], False
    for c in sorted(cys, key=min):
        w = [v2(q * x + r) for x in c]
        S, L = sum(w), len(w)
        on_rare = (S / L < a) if q < 4 else (S / L > a)
        shelter_any = shelter_any or on_rare
        desc.append(f"({min(c)},{L},{S},{S/L:.4f}{'*' if on_rare else ''})")
    pred = (r > 0) == (q > 4)
    print(f"{name:10s} {q:2d} {r:+3d}  {a:.6f}  {rare:9s}  {' '.join(desc)[:52]:52s}  "
          f"predicted {str(pred):5s} observed {str(shelter_any):5s}  "
          f"{'OK' if pred == shelter_any else 'MISMATCH'}")
print()
print("* marks a cycle on the rare side.  'shelter' = some positive cycle sits on the rare side,")
print("predicted by sign(r) = sign(q-4).  Cycle search over odd seeds <= 20001.")
