#!/usr/bin/env python3
"""Item 5 (L4 analogue) -- residue laws of the rare-side record holders.

For A = 3x+1 the least N-confined integer satisfies r_min(N) = 3 or 7 (mod 12),
never 11 (Descent.ResidueLaw, formalized).  This script reads a ladder and reports
the residue census modulo small moduli, for whichever map produced it.
"""
import sys
from collections import Counter


def jumps(path_list):
    best = {}
    for p in path_list:
        for line in open(p):
            n, m = line.split()
            n, m = int(n), int(m)
            if n not in best or m < best[n]:
                best[n] = m
    out, prev = [], None
    for n in sorted(best):
        if best[n] != prev:
            out.append((n, best[n]))
            prev = best[n]
    return out, best


def main(tag, paths):
    J, best = jumps(paths)
    holders = [m for _, m in J]
    print(f"{tag}: {len(holders)} distinct record holders, deepest depth {max(best)}")
    print(f"  holders: {holders[:12]}{' ...' if len(holders) > 12 else ''}")
    for mod in (4, 8, 16, 32, 3, 5, 12, 15, 20, 24, 40):
        c = Counter(m % mod for m in holders)
        occupied = sorted(c)
        print(f"  mod {mod:3d}: {len(occupied):2d}/{mod:2d} classes occupied  "
              f"{dict(sorted(c.items()))}")
    # all N (not only jump points), as the A law is stated for every N
    allh = [best[n] for n in sorted(best)]
    for mod in (8, 16, 40):
        c = Counter(m % mod for m in allh)
        print(f"  over every N (mod {mod}): {dict(sorted(c.items()))}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
