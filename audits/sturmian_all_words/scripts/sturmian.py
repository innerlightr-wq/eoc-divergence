#!/usr/bin/env python3
"""Certified mechanical/Sturmian words, initial powers, and Christoffel tests.

Exactness.  gamma and rho are carried as integers over a common denominator
2^P.  Every floor is an integer shift.  The computation is certified by
`safety_margin`: it reports the minimum distance of j*gamma + rho to Z, in
units of 2^-P, over the range used.  Since the representation error of gamma
after j steps is at most j units, a margin above j proves every floor correct.
"""
P = 512
ONE = 1 << P


def from_cf(a, P=P):
    """Value of [a0; a1, a2, ...] as an integer over 2^P (truncated CF, exact)."""
    from fractions import Fraction
    x = Fraction(a[-1])
    for ai in reversed(a[:-1]):
        x = ai + 1 / x
    return (x.numerator << P) // x.denominator


def log3_2(P=P):
    """floor(2^P * log_3 2) from a high-precision Decimal.  Certified downstream
    by `safety_margin`, which bounds how close any j*gamma+rho comes to Z."""
    from decimal import Decimal, getcontext
    getcontext().prec = P // 3 + 80
    return int((Decimal(2).ln() / Decimal(3).ln()) * (1 << P))


def sqrt_int(n, P=P):
    """floor(2^P * sqrt(n))."""
    from math import isqrt
    return isqrt(n << (2 * P))


def word(gnum, rnum, n, upper=False):
    """mechanical word of slope gnum/2^P, intercept rnum/2^P, length n."""
    if upper:
        f = lambda t: -((-t) >> P)          # ceil(t / 2^P)
    else:
        f = lambda t: t >> P                # floor(t / 2^P)
    prev = f(rnum)
    out = []
    for j in range(1, n + 1):
        cur = f(j * gnum + rnum)
        out.append(cur - prev)
        prev = cur
    return out


def safety_margin(gnum, rnum, n):
    """min over 0<=j<=n of distance of j*gamma+rho to Z, in units of 2^-P."""
    m = ONE
    for j in range(1, n + 1):          # j = 0 is exact (r = rnum), no error yet
        r = (j * gnum + rnum) % ONE
        m = min(m, r, ONE - r)
    return m


def initial_period_run(s, L):
    """m(L) = max{ m : s[j] == s[j+L] for all j < m }."""
    m = 0
    while m + L < len(s) and s[m] == s[m + L]:
        m += 1
    return m


def initial_powers(s, maxL=None):
    """for each period L, the initial exponent e(L) = (L + m(L))/L."""
    n = len(s)
    maxL = maxL or n // 2
    out = []
    for L in range(1, maxL + 1):
        m = initial_period_run(s, L)
        out.append((L, m, (L + m) / L))
    return out


def is_square_prefix(s, L):
    return 2 * L <= len(s) and s[:L] == s[L:2 * L]


def christoffel(p, q):
    """lower Christoffel word of slope p/q: ones at floor(j*q/p)? -- use the
    standard cutting-sequence definition d_i = floor((i+1)p/q) - floor(i*p/q)."""
    return [((i + 1) * p) // q - (i * p) // q for i in range(q)]


def conjugates(w):
    return [tuple(w[i:] + w[:i]) for i in range(len(w))]


def is_balanced(w):
    """is the finite word balanced? (|k(u) - k(v)| <= 1 for factors of equal length)"""
    n = len(w)
    for L in range(1, n + 1):
        cnt = [sum(w[i:i + L]) for i in range(n - L + 1)]
        if cnt and max(cnt) - min(cnt) > 1:
            return False
    return True
