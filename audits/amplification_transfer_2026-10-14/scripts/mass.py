"""Exact confined-word counts and dyadic mass.  INTEGER arithmetic only:
confinement is tested as 2^{S_j} <= 2^c * 3^j, never with a float logarithm.

Definitions are taken verbatim from eoc-divergence/Occupation/Compositions.lean:
   Confined c d  <->  forall j <= N, 2^{psum d j} <= 2^c * 3^j
   p N c         =   sum over c-confined words d of length N of 2^{-psum d N}
A word is a tuple of N letters, each >= 1 (a positive composition of S_N).
"""
from fractions import Fraction as Q
import sys


def sN(N: int) -> int:
    """floor(N log2 3), as (3^N).bit_length()-1 -- the repo's Occupation.sN."""
    return (3 ** N).bit_length() - 1


def ok(S: int, j: int, c: int) -> bool:
    """2^S <= 2^c 3^j, exactly."""
    return (1 << S) <= (1 << c) * 3 ** j


def counts(N: int, c: int = 0):
    """A[j][S] = number of c-confined words of length j with psum = S.
    Returns A[N] as a dict.  Exact integers."""
    A = {0: 1}
    for j in range(1, N + 1):
        Smax = c + sN(j)
        B = {}
        for S, a in A.items():
            # d >= 1, new partial sum S+d must satisfy confinement at step j
            for d in range(1, Smax - S + 1):
                T = S + d
                if ok(T, j, c):
                    B[T] = B.get(T, 0) + a
        A = B
    return A


def mass(N: int, c: int = 0) -> Q:
    """p(N,c) as an exact rational."""
    return sum((Q(a, 1 << S) for S, a in counts(N, c).items()), Q(0))


def nwords(N: int, c: int = 0) -> int:
    return sum(counts(N, c).values())


if __name__ == '__main__':
    import math
    alpha = math.log2(3)
    H = lambda x: 0.0 if x in (0.0, 1.0) else -x * math.log2(x) - (1 - x) * math.log2(1 - x)
    I0 = alpha * (1 - H(1 / alpha))
    g = alpha - I0
    print(f"alpha = {alpha:.12f}   I0 = {I0:.12f}   g = alpha - I0 = {g:.12f}")
    print()
    print(f"{'N':>4} {'sN':>5} {'n_N = #confined':>22} {'log2(n_N)/N':>13} "
          f"{'p(N,0)':>14} {'-log2 p/N':>11}")
    for N in [4, 8, 12, 16, 20, 24, 28, 32, 40, 48, 56, 64, 80, 96, 128, 160, 200]:
        A = counts(N, 0)
        n = sum(A.values())
        p = sum((Q(a, 1 << S) for S, a in A.items()), Q(0))
        lp = -(math.log2(p.numerator) - math.log2(p.denominator)) if p else float('inf')
        print(f"{N:>4} {sN(N):>5} {n:>22} {math.log2(n)/N:>13.9f} "
              f"{float(p):>14.6e} {lp/N:>11.9f}")
