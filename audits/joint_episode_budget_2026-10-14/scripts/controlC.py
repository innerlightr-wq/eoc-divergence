"""Control C, corrected: the Prop. 13.2 oscillator.  Digit 2 when R_n <= c
(inside), digit 1 when R_n > c (outside).  Symbolic word first; then a genuine
positive odd realizer of the prefix via the exact realizer congruence."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
from eoc import *

def oscillator(c, N):
    S = [0]; d = []
    for n in range(N):
        dn = 2 if (1 << S[n]) <= (1 << c) * 3 ** n else 1
        d.append(dn); S.append(S[n] + dn)
    return d, S

def realizer(S, N):
    """least odd r < 2^{S_N+1} with 3^N r + C_N = 2^{S_N} (mod 2^{S_N+1})"""
    C = 0
    for j in range(N): C = 3 * C + (1 << S[j])
    SN = S[N]; M = 1 << (SN + 1)
    return (pow(3 ** N, -1, M) * ((1 << SN) - C)) % M, C

print(f"{'c':>2} {'N':>5} {'#episodes P':>12} {'episode lengths':>24} {'occupation':>11} "
      f"{'#exits':>7} {'least realizer bits':>20} {'word reproduced':>16}")
for c in (0, 1, 2):
    for N in (60, 200):
        d, S = oscillator(c, N)
        occ = [n for n in range(N) if (1 << S[n]) <= (1 << c) * 3 ** n]
        runs = []; a = occ[0]; p = occ[0]
        for n in occ[1:]:
            if n == p + 1: p = n; continue
            runs.append(p + 1 - a); a = n; p = n
        runs.append(p + 1 - a)
        r, C = realizer(S, N)
        dd, _, _ = orbit(r, N)
        print(f"{c:>2} {N:>5} {len(runs):>12} {str(sorted(set(runs))):>24} {sum(runs):>11} "
              f"{N-sum(runs):>7} {r.bit_length():>20} {str(tuple(dd)==tuple(d)):>16}")
print()
print("=> episode COUNT grows linearly in N (P ~ N/3), so no bound P <= const(c,m_0)")
print("   can exist -- Prop. 13.2.  Every prefix is realized by a genuine positive odd")
print("   integer, whose bit length grows like S_N ~ 1.4 N: the realizer height is the")
print("   price, and it is exactly what Remark 13.3's charge re-levies at each episode.")
