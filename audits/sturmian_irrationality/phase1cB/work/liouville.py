"""Task 2/3: the uniform Liouville step at a general irrational slope.

Exact integer arithmetic throughout.  For odd n,

    |M_n| >= 2^{q_n + q_{n+1} - 1}        (depth law, Theorem 1')
    |M_n| <= H (1 + q_n) G_n,  G_n = max(2^{q_n}, 3^{p_n})

so any rational Phi(1c_gamma) = u/v in lowest terms has

    H = max(|u|,v) > 2^{q_n+q_{n+1}-1} / ((1+q_n) G_n).
"""
from fractions import Fraction
from math import log2
from slopes import *

LOG2_3 = 1.5849625007211562          # only ever used for reporting, never for a decision

def regime_and_G(pn, qn):
    """Exact: returns ('A'|'B', G_n) with G_n = max(2^{q_n}, 3^{p_n}) as an integer."""
    A, B = 1 << qn, 3 ** pn
    return ('A', A) if A >= B else ('B', B)

def height_floor(pn, qn, qn1):
    """Exact integer H0 with: Phi(1c_gamma) = u/v in lowest terms => max(|u|,v) > H0."""
    reg, G = regime_and_G(pn, qn)
    num = 1 << (qn + qn1 - 1)
    den = (1 + qn) * G
    return reg, num // den            # floor; H > num/den  =>  H >= H0 + 1

# ---------- 2-adic side: Phi(v) mod 2^K ----------

def phi_mod(word_bits, K):
    """Phi(v) mod 2^K for a word given as an indexable of 0/1 of length >= K.
    Uses  3^{k_K} x = -c_K (mod 2^K)  with  c_{i+1} = 3^{v_i} c_i + v_i 2^i."""
    M = 1 << K
    c, k, pw = 0, 0, 1
    for i in range(K):
        if word_bits[i]:
            c = (3 * c + pw) % M
            k += 1
        pw = (pw << 1) % M
    return (-c * pow(pow(3, k, M), -1, M)) % M


def word_from_positions(pos, L):
    """binary word of length L whose ones sit at the given increasing positions."""
    w = bytearray(L)
    for p in pos:
        if p >= L:
            break
        w[p] = 1
    return w

def v2_diff_mod(a, b, K):
    d = (a - b) % (1 << K)
    if d == 0:
        return None                   # agree to at least K; inconclusive
    return (d & -d).bit_length() - 1

# ---------- periodic values as exact rationals ----------

def c_word(w):
    """c_w = sum_{i<l, w_i=1} 3^{k - k_{i+1}} 2^i  (exact integer)."""
    k = sum(w)
    c, pw, kk = 0, 1, 0
    for i, b in enumerate(w):
        if b:
            kk += 1
            c += 3 ** (k - kk) * pw
        pw <<= 1
    return c

def phi_periodic(w):
    l, k = len(w), sum(w)
    return Fraction(c_word(w), (1 << l) - 3 ** k)

def v2_rational(x):
    n, d = x.numerator, x.denominator
    assert d % 2 == 1, "denominator must be odd"
    if n == 0:
        return None
    return (n & -n).bit_length() - 1
