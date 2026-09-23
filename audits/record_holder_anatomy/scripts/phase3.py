"""Phase 3 measurements M2, M3, M4.  Exact arithmetic throughout.

M2  Sturmian proximity: the drift deficit D_k = A[k] - S_k against the critical line,
    and the longest common prefix of an orbit's VALUATION word with the shifts of the
    critical Sturmian valuation word d_i = floor((i+1)a) - floor(i a), a = log2 3.
M3  Signed border: for every zero-confined periodic point x_w of K with period <= L
    (all negative, by P1), the 2-adic agreement v2(m - x_w) against log2 height(x_w).
M4  Approximation quality: the best (agreement depth)/(log2 height) over rationals of
    bounded height, for each point; this is the Markov-type exponent being ranked.
"""
import math
from fractions import Fraction
from anatomy import A, acc_orbit, minrep, c_of, v2
from controls import sturmian_valuations

# ------------------------------------------------------------------ M2
def drift_profile(m, cap=4000):
    dep, rows = acc_orbit(m, cap)
    return dep, [A(k + 1) - rows[k][2] for k in range(min(dep, len(rows)))]

def sturmian_lcp(word, stur, maxshift):
    """max over shifts j <= maxshift of the common-prefix length of `word` with
    the Sturmian valuation word starting at index j."""
    best, arg = 0, None
    for j in range(maxshift + 1):
        i = 0
        while i < len(word) and j + i < len(stur) and word[i] == stur[j + i]:
            i += 1
        if i > best: best, arg = i, j
    return best, arg

# ------------------------------------------------------------------ M3
def confined_periodic_points(Lmax):
    """All zero-confined purely periodic points of K with period <= Lmax, as exact
    negative Fractions, with their valuation words.  By P1 every one is negative."""
    out = {}
    def rec(word, S):
        k = len(word)
        if 1 <= k <= Lmax:
            # purely periodic point with this word repeated:
            #   m (2^S - 3^L) = C_L ,   C_L = sum_{i<L} 3^{L-1-i} 2^{S_i}
            C, Si = 0, 0
            for i in range(k):
                C += 3 ** (k - 1 - i) << Si
                Si += word[i]
            den = (1 << S) - 3 ** k
            x = Fraction(C, den)
            out.setdefault(x, (tuple(word), k, S))
        if k == Lmax: return
        for d in range(1, A(k + 1) - S + 1):
            word.append(d); rec(word, S + d); word.pop()
    rec([], 0)
    return out

def border(m, x):
    """v2(m - x) for integer m and Fraction x with odd denominator."""
    n, q = x.numerator, x.denominator
    assert q % 2 == 1
    return v2(m * q - n)

def height(x):
    return max(abs(x.numerator), x.denominator)

# ------------------------------------------------------------------ M4
def best_exponent(x_mod, K, Qmax, exact=None):
    """Markov-type exponent: max over rationals p/q (q odd) of
           v2(x - p/q) / log2 height(p/q) ,
    where x is known modulo 2^K.  `exact` is the true target when it is a rational
    (an integer here), used only to exclude p/q = x itself, which would give E = inf.  For each odd q and each t <= K the best p is the
    representative of x*q mod 2^t nearest zero; then v2(x*q - p) >= t and
    height = max(|p|, q).  Exact integers; the division is only in the reported ratio."""
    best = (0.0, None)
    for q in range(1, Qmax + 1, 2):
        xq = x_mod * q
        for t in range(2, K + 1):
            m2 = 1 << t
            r = xq % m2
            p = r if r <= m2 - r else r - m2
            h = max(abs(p), q)
            if h <= 1:
                continue
            if xq == p or (exact is not None and Fraction(p, q) == exact):
                continue           # p/q = x exactly: E is infinite, reported separately
            e = t / math.log2(h)
            if e > best[0]:
                best = (e, (p, q, t, h))
    return best
