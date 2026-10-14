"""The symbolic-mass <-> residue-density bridge, verified by brute force.

Claim (B).  Let Q_N = 2^{sN(N)+1}, sN(N) = floor(N log2 3).  Then
   #{ m odd, m < Q_N : 2^{S_j(m)} <= 3^j for all j <= N }  =  2^{sN(N)} * p(N,0),
i.e. the density of 0-confined seeds among odd residues mod Q_N is EXACTLY the
symbolic dyadic mass p(N,0) of Occupation/Compositions.lean.

Claim (I).  word -> least realizer residue is injective with multiplicity ONE:
each 0-confined word d of length N is realized by exactly one odd residue class
mod 2^{S_N(d)+1}, which splits into 2^{sN-S_N} classes mod Q_N.  Hence
   #confined odd residues mod Q_N  =  sum_d 2^{sN - S_N(d)} ,
and no residue is counted twice.  (Lean: EOC/Realizer.lean leastRealizer_unique,
residue_pinning.)

All integer arithmetic.  No floating-point logarithm decides confinement.
"""
import os, sys
from fractions import Fraction as Q
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mass import counts, mass, sN


def word_of(m: int, N: int):
    """The first N valuation letters of the accelerated odd orbit of m, and the
    partial sums.  T(m) = (3m+1)/2^{v2(3m+1)}."""
    d = []
    x = m
    for _ in range(N):
        t = 3 * x + 1
        v = (t & -t).bit_length() - 1
        d.append(v)
        x = t >> v
    return d


def confined(d) -> bool:
    S = 0
    for j, dj in enumerate(d, start=1):
        S += dj
        if (1 << S) > 3 ** j:
            return False
    return True


print("=" * 86)
print("(B) density of 0-confined odd residues mod Q_N = 2^{sN+1}  ==  p(N,0)")
print("=" * 86)
print(f"{'N':>3} {'sN':>4} {'Q_N':>12} {'#conf odd res':>14} {'2^sN * p(N,0)':>22} {'equal':>6}"
      f" {'#words':>9} {'sum 2^(sN-S)':>14}")
bad = 0
for N in range(1, 15):
    s = sN(N); QN = 1 << (s + 1)
    cnt = 0
    for m in range(1, QN, 2):
        if confined(word_of(m, N)):
            cnt += 1
    p = mass(N, 0)
    target = Q(1 << s) * p
    A = counts(N, 0)
    nw = sum(A.values())
    splitsum = sum(a * (1 << (s - S)) for S, a in A.items())
    eq = (Q(cnt) == target) and (cnt == splitsum)
    bad += not eq
    print(f"{N:>3} {s:>4} {QN:>12} {cnt:>14} {str(target):>22} {str(eq):>6}"
          f" {nw:>9} {splitsum:>14}")
print(f"violations: {bad}")

print()
print("=" * 86)
print("(I) multiplicity: each confined word has EXACTLY ONE realizer class mod 2^{S_N+1}")
print("=" * 86)
hdr = f"{'N':>3} {'#words':>9} {'#distinct (S_N, r mod 2^(S_N+1))':>33} {'max fibre':>10} {'injective':>10}"
print(hdr)
bad2 = 0
for N in range(1, 15):
    s = sN(N); QN = 1 << (s + 1)
    # collect, for every confined odd residue, its word; group by word
    byword = {}
    for m in range(1, QN, 2):
        d = word_of(m, N)
        if confined(d):
            S = sum(d)
            byword.setdefault(tuple(d), set()).add(m % (1 << (S + 1)))
    nw = len(byword)
    fib = max(len(v) for v in byword.values()) if byword else 0
    nres = sum(len(v) for v in byword.values())
    ok = (fib == 1) and (nres == nw) and (nw == sum(counts(N, 0).values()))
    bad2 += not ok
    print(f"{N:>3} {nw:>9} {nres:>33} {fib:>10} {str(ok):>10}")
print(f"violations: {bad2}")
