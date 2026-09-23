"""Exact machinery for Sturmian words of an arbitrary irrational slope gamma in (0,1).

Everything is integer / Fraction arithmetic.  A slope is given by the partial
quotients of its continued fraction  gamma = [0; a_1, a_2, ...]  so that
alpha = 1/gamma = [a_1; a_2, a_3, ...].  If p_n/q_n are the convergents of gamma
(p_0/q_0 = 0/1, p_1/q_1 = 1/a_1) then q_n/p_n (n >= 1) are the convergents of
alpha, which gives certified rational brackets for alpha and hence exact floors.
"""
from fractions import Fraction

# ---------- continued fractions of the test slopes ----------

def cf_golden(N):            # 1/phi = [0;1,1,1,...]
    return [1] * N

def cf_sqrt2m1(N):           # sqrt(2)-1 = [0;2,2,2,...]
    return [2] * N

def cf_e_minus_2(N):         # e-2 = [0;1,2,1,1,4,1,1,6,1,1,8,...]
    a, k = [1], 2
    while len(a) < N:
        a += [k, 1, 1]
        k += 2
    return a[:N]

def cf_from_quotients(qs, N):
    out = list(qs)
    while len(out) < N:
        out.append(1)
    return out[:N]

# ---------- convergents ----------

def convergents(a):
    """a = [a_1, a_2, ...].  Returns p[0..N], q[0..N] for gamma = [0;a_1,a_2,...]."""
    p = [0, 1]
    q = [1, a[0]]
    for n in range(1, len(a)):
        p.append(a[n] * p[-1] + p[-2])
        q.append(a[n] * q[-1] + q[-2])
    return p, q          # p[n]/q[n] is the n-th convergent, p[0]/q[0] = 0/1

# ---------- certified floors of j*alpha ----------

class Alpha:
    """alpha = 1/gamma, bracketed by two consecutive convergents q_m/p_m."""
    def __init__(self, p, q, m):
        lo = Fraction(q[m], p[m])
        hi = Fraction(q[m + 1], p[m + 1])
        self.lo, self.hi = (lo, hi) if lo < hi else (hi, lo)

    def floor(self, j):
        f1 = (j * self.lo).__floor__()
        f2 = (j * self.hi).__floor__()
        if f1 != f2:
            raise RuntimeError(f"bracket too coarse at j={j}")
        return f1

def ones_positions(alpha_floor, jmax):
    return [alpha_floor(j) for j in range(jmax)]

def mech_ones(pn, qn, jmax):
    """ones of w_{p,q}^infty : positions floor(j*q/p), j >= 0."""
    return [(j * qn) // pn for j in range(jmax)]

def lcp_from_positions(A, B):
    """A, B strictly increasing one-position lists of two binary words.
    Returns (j_star, lcp) where j_star is the first index of disagreement."""
    for j, (x, y) in enumerate(zip(A, B)):
        if x != y:
            return j, min(x, y)
    raise RuntimeError("no disagreement inside the computed range")
