"""Exact accelerated-map arithmetic.  Integers and Fractions only.

Rev 8 conventions (authoritative copy: eoc-lean-verification branch eoc-revision8
= b2dcae2, paper/eoc_rev8.pdf sha256 07c6610d...):
   m_{n+1} = (3 m_n + 1)/2^{d_n},  d_n = v2(3 m_n + 1),  S_0 = 0,
   R_n = S_n - alpha n,  alpha = log2 3.
Occupied means R_n <= c, decided EXACTLY as 2^{S_n} <= 2^c * 3^n (integer c).
"""
from fractions import Fraction as F


def v2(n):
    return (n & -n).bit_length() - 1


def orbit(m0, H):
    d, S, m = [], [0], [m0]
    x = m0
    for _ in range(H):
        t = 3 * x + 1
        k = v2(t)
        d.append(k); x = t >> k
        S.append(S[-1] + k); m.append(x)
    return d, S, m


def occupied(S, n, c):
    return (1 << S[n]) <= (1 << c) * 3 ** n


def episodes(S, H, c):
    occ = [n for n in range(H) if occupied(S, n, c)]
    if not occ:
        return []
    out = []; a = occ[0]; p = occ[0]
    for n in occ[1:]:
        if n == p + 1:
            p = n; continue
        out.append((a, p + 1)); a = n; p = n
    out.append((a, p + 1))
    return [(a, b, b == H) for (a, b) in out]


def direction(d):
    """s_n = 0 if d_n == 1 else 1."""
    return [0 if x == 1 else 1 for x in d]


def changes(sym):
    return sum(1 for i in range(len(sym) - 1) if sym[i] != sym[i + 1])


def runs(sym):
    """Maximal constant runs as (symbol, length)."""
    if not sym:
        return []
    out = []; s = sym[0]; n = 1
    for x in sym[1:]:
        if x == s:
            n += 1
        else:
            out.append((s, n)); s = x; n = 1
    out.append((s, n))
    return out


def carry(S, t):
    """C(D) = sum_{j<t} 3^{t-1-j} 2^{S_j}, relative to S_0 = 0."""
    return sum(3 ** (t - 1 - j) * (1 << S[j]) for j in range(t))


def least_realizer(d):
    """The unique odd r < 2^{S+1} with 3^t r + C = 2^S (mod 2^{S+1})."""
    t = len(d); S = [0]
    for x in d:
        S.append(S[-1] + x)
    C = carry(S, t); SN = S[t]; M = 1 << (SN + 1)
    return (pow(3 ** t, -1, M) * ((1 << SN) - C)) % M, C, SN
