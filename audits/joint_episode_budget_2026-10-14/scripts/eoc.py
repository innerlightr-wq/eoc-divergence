"""Exact EOC accounting dictionary.  Integers and Fractions only.

Rev 8 conventions (manuscript sha256 07c6610d..., repo branch eoc-revision8
b2dcae2): m_{n+1} = (3 m_n + 1)/2^{d_n}, d_n = v2(3 m_n + 1), S_0 = 0,
R_n = S_n - alpha n, alpha = log2 3.  Occupation is the ONE-SIDED corridor
R_n <= c, decided exactly as  2^{S_n} <= 2^c * 3^n  (integer c).  Time zero
counts.  The full forward orbit continues past m = 1 (d = 2, R rises by
2 - alpha each step).
"""
from fractions import Fraction as F


def v2(n):
    return (n & -n).bit_length() - 1


def orbit(m0, H):
    """d, S, m arrays with S[0]=0, m[0]=m0, for n = 0..H."""
    d, S, m = [], [0], [m0]
    x = m0
    for _ in range(H):
        t = 3 * x + 1
        k = v2(t)
        d.append(k); x = t >> k
        S.append(S[-1] + k); m.append(x)
    return d, S, m


def in_corridor(S, n, c):
    """R_n <= c  <=>  2^{S_n} <= 2^c 3^n.  Exact integers, no logarithms."""
    return (1 << S[n]) <= (1 << c) * 3 ** n


def carries(S, H):
    """C_0 = 0, C_{n+1} = 3 C_n + 2^{S_n}; also the closed form."""
    C = [0]
    for n in range(H):
        C.append(3 * C[n] + (1 << S[n]))
    closed = [sum(3 ** (n - 1 - j) * (1 << S[j]) for j in range(n)) for n in range(H + 1)]
    return C, closed


def zs(S, H):
    """z_n = 2^{S_n}/3^n = 2^{R_n}, exact rational."""
    return [F(1 << S[n], 3 ** n) for n in range(H + 1)]


def Bcal(m, z, H):
    """Bcal_n = m_n z_n."""
    return [F(m[n]) * z[n] for n in range(H + 1)]


def episodes(S, H, c):
    """Maximal occupied integer intervals [a,b) inside [0,H), with a flag for
    the final truncated episode (one that is still occupied at H-1)."""
    occ = [n for n in range(H) if in_corridor(S, n, c)]
    out = []
    if not occ:
        return out
    a = occ[0]; prev = occ[0]
    for n in occ[1:]:
        if n == prev + 1:
            prev = n; continue
        out.append((a, prev + 1)); a = n; prev = n
    out.append((a, prev + 1))
    return [(a, b, b == H) for (a, b) in out]


def block(S, m, a, b):
    """u, v, C_[a,b), s, t for the block [a,b)."""
    t = b - a
    s = S[b] - S[a]
    Cab = sum(3 ** (b - 1 - j) * (1 << (S[j] - S[a])) for j in range(a, b))
    return F(Cab, 3 ** t), F(1 << s, 3 ** t), Cab, s, t


def last_return_certified(m0, c, cap=20000):
    """Return (H_cert, n_one) where n_one is the first index with m_n = 1 and
    H_cert is a horizon provably containing every occupied time.

    Certification, not a scan cutoff: for n >= n_one the orbit sits at the fixed
    point (d = 2) so R_{n+1} = R_n + 2 - alpha is strictly increasing; hence once
    n >= n_one and R_n > c, no later index is occupied.  Exactly:
    R_n > c  <=>  2^{S_n} > 2^c 3^n, and S_n = S_{n_one} + 2(n - n_one).
    """
    d, S, m = orbit(m0, cap)
    n_one = next((n for n in range(cap + 1) if m[n] == 1), None)
    if n_one is None:
        return None, None
    n = n_one
    while n < cap and in_corridor(S, n, c):
        n += 1
    # from n onwards R strictly increases, so n-1 is the last occupied index >= n_one
    return n, n_one
