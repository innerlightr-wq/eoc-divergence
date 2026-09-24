#!/usr/bin/env python3
"""Item 4 -- the signed marker as one statement across the four maps.

A purely periodic point of T(x) = (qx+r)/2^{v2(qx+r)} with word W of length L and
total S is the rational
        m = r * C_L / (2^S - q^L),     C_L = sum_{i<L} q^{L-1-i} 2^{S_i} > 0.
On the RARE side:
   q < 4 : S/L <= alpha  =>  2^S < q^L  =>  sign(m) = -sign(r)
   q > 4 : S/L >= alpha  =>  2^S > q^L  =>  sign(m) = +sign(r)
i.e. sign(m) = sign(r) * sign(q-4).  Rare-side periodic points are NEGATIVE exactly
when sign(r) != sign(q-4) -- exactly the maps with no shelter, A and D.

Since S_L - L*alpha has the rare-side sign strictly, the prefix condition for the
infinite periodic word reduces to the first period, so the enumeration below is
complete for each period length.
"""
from fractions import Fraction
from itertools import product
from math import log2

MAPS = [("A 3x+1", 3, 1), ("B 3x-1", 3, -1), ("C 5x+1", 5, 1), ("D 5x-1", 5, -1)]


def v2(n):
    n = abs(n)
    return (n & -n).bit_length() - 1 if n else 10 ** 9


def Afloor(q, N):
    out = [0] * (N + 1)
    p = 1
    for k in range(1, N + 1):
        p *= q
        out[k] = p.bit_length() - 1
    return out


print("=" * 90)
print("Conjugacies:  A(-x) = -B(x)   and   D(-x) = -C(x),  checked on every odd |x| < 2^14")
print("=" * 90)
for (n1, q1, r1), (n2, q2, r2) in (((None, 3, 1), (None, 3, -1)), ((None, 5, -1), (None, 5, 1))):
    bad = 0
    for x in range(1, 1 << 14, 2):
        y1 = q1 * (-x) + r1
        y2 = q2 * x + r2
        if v2(y1) != v2(y2) or (y1 >> v2(y1)) != -(y2 >> v2(y2)):
            bad += 1
    print(f"  ({q1}x{r1:+d})(-x) = -({q2}x{r2:+d})(x):  violations = {bad}")
print()

print("=" * 90)
print("Rare-side purely periodic points: enumeration by period, with signs")
print("=" * 90)
LMAX = 10
SLACK = 5          # for q > 4 the rare side bounds S from BELOW only, so the set of
                   # rare-side periodic words of a given length is infinite; the
                   # enumeration is capped at S <= A[L] + SLACK and says so.
HEIGHT_UPTO = 6    # reduced heights are computed exactly for period <= this

for name, q, r in MAPS:
    A = Afloor(q, LMAX + 1)
    upper = q > 4
    tot = neg = pos = 0
    heights = []
    for L in range(1, LMAX + 1):
        cap = A[L] + SLACK
        stack = [(0, 0, 0, 0)]        # (k, S_k, C_k, unused)
        # DFS carrying C incrementally: C_{k+1} = q*C_k + 2^{S_k}
        def dfs(k, Sk, C):
            global tot, neg, pos
            if k == L:
                den = (1 << Sk) - q ** L
                if den == 0:
                    return
                sgn = (1 if r > 0 else -1) * (1 if den > 0 else -1)
                tot += 1
                if sgn < 0:
                    neg += 1
                else:
                    pos += 1
                if L <= HEIGHT_UPTO:
                    m = Fraction(r * C, den)
                    heights.append(max(abs(m.numerator), m.denominator))
                return
            hi = cap - Sk - (L - k - 1)
            C2 = q * C + (1 << Sk)
            for a in range(1, hi + 1):
                S2 = Sk + a
                if upper:
                    if S2 < A[k + 1] + 1:
                        continue
                else:
                    if S2 > A[k + 1]:
                        break
                dfs(k + 1, S2, C2)

        dfs(0, 0, 0)
    sgn = "negative" if (r > 0) != (q > 4) else "positive"
    print(f"  {name}: rare-side purely periodic points with period <= {LMAX}: {tot} "
          f"({neg} negative, {pos} positive)")
    print(f"      predicted sign: {sgn};  observed: "
          f"{'all negative' if pos == 0 and neg else ('all positive' if neg == 0 and pos else 'MIXED')}"
          f";  reduced heights (period <= {HEIGHT_UPTO}) up to {max(heights) if heights else 0}")
