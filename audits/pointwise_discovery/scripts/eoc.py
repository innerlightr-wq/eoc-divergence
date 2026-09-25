"""Exact-arithmetic core for the accelerated q x + r maps.

Everything here is integer/rational.  Floating point appears only in the
convenience wrappers whose names end in `_f`, and never in a decision.

Conventions (fixed once, matching eoc-divergence):

    T(m) = (q m + r) / 2^{a(m)},   a(m) = v2(q m + r),   q odd >= 3, r odd
    m_k  = T^k(m_0),  a_k = a(m_k),  S_n = sum_{k<n} a_k
    alpha_q = log2 q,  R_n = S_n - n alpha_q

    aggregate identity:  2^{S_n} m_n = q^n m_0 + r C_n,
                         C_n = sum_{i<n} q^{n-1-i} 2^{S_i},  C_{n+1} = q C_n + 2^{S_n}

    A[k] = floor(k log2 q) = bitlength(q^k) - 1

    rare side (the side an orbit must fight to stay on):
        q < 4 :  2^{S_n} <= q^n     <=>  S_n <= A[n]          ("confinement")
        q > 4 :  2^{S_n} >= q^n     <=>  S_n >= A[n] + 1      ("anti-confinement")
"""

from fractions import Fraction
from math import log2


# ---------------------------------------------------------------- the map ---

class Map:
    def __init__(self, q, r):
        assert q % 2 == 1 and q >= 3 and r % 2 == 1
        self.q, self.r = q, r
        self.upper = q > 4                 # rare side is the upper one
        self.name = f"{q}x{'+' if r > 0 else '-'}{abs(r)}"
        self._A = [0]
        self._qk = [1]

    def A(self, k):
        """A[k] = floor(k log2 q), exactly, from bitlength(q^k)."""
        while len(self._A) <= k:
            self._qk.append(self._qk[-1] * self.q)
            self._A.append(self._qk[-1].bit_length() - 1)
        return self._A[k]

    def qpow(self, k):
        self.A(k)
        return self._qk[k]

    def step(self, m):
        y = self.q * m + self.r
        a = (y & -y).bit_length() - 1      # v2(y)
        return y >> a, a

    def rare_ok(self, n, S):
        """Is the orbit still on the rare side at depth n with total S?"""
        return S >= self.A(n) + 1 if self.upper else S <= self.A(n)


T31 = Map(3, 1)


# -------------------------------------------------------------- the orbit ---

def orbit(mp, m0, nmax, stop_off_rare=False):
    """Exact orbit record.  Returns dict of lists indexed by depth."""
    m, S, C = m0, 0, 0
    ms, aa, Ss, Cs = [m0], [], [0], [0]
    for k in range(nmax):
        C = mp.q * C + (1 << S)
        m, a = mp.step(m)
        S += a
        ms.append(m); aa.append(a); Ss.append(S); Cs.append(C)
        if stop_off_rare and not mp.rare_ok(k + 1, S):
            break
    return {"m": ms, "a": aa, "S": Ss, "C": Cs}


def rare_depth(mp, m0, cap=100000, guard_bits=4096):
    """Largest n with the orbit on the rare side at every 1..n.  Exact."""
    m, S = m0, 0
    for k in range(1, cap + 1):
        m, a = mp.step(m)
        S += a
        if not mp.rare_ok(k, S):
            return k - 1
        if m.bit_length() > guard_bits:
            raise OverflowError("guard")
    return cap


def word_of(mp, m0, n):
    """The length-n valuation word of m0."""
    m, w = m0, []
    for _ in range(n):
        m, a = mp.step(m)
        w.append(a)
    return w


# ----------------------------------------------- words, carries, realizers ---

def carry(mp, w):
    """C_n and S_n for a word w, exactly."""
    C, S = 0, 0
    for a in w:
        C = mp.q * C + (1 << S)
        S += a
    return C, S


def realizer(mp, w):
    """Least positive odd m whose length-|w| word is exactly w  (Terras-Everett).

    Solves  q^n m + r C_n = 2^{S_n}  (mod 2^{S_n+1}); the quotient is then odd.
    """
    n = len(w)
    C, S = carry(mp, w)
    mod = 1 << (S + 1)
    qn_inv = pow(mp.qpow(n) % mod, -1, mod)
    m = (qn_inv * ((1 << S) - mp.r * C)) % mod
    if m == 0:
        m = mod                            # cannot happen for odd classes
    return m


def realizer_deficit(mp, w):
    """delta(w) = S_n + 1 - log2 r(w)  in exact-log form; returns (r, S, delta_f)."""
    C, S = carry(mp, w)
    r = realizer(mp, w)
    return r, S, (S + 1) - log2(r)


def confined_word(mp, w):
    """Is w on the rare side at every prefix length?"""
    S = 0
    for k, a in enumerate(w, 1):
        S += a
        if not mp.rare_ok(k, S):
            return False
    return True


# ------------------------------------------------- exact word mass p_N(c) ---

def transfer(mp, N):
    """f[k][S] = number of rare-side words of length k with total S.

    Returns (f, Smax) with f a list of dicts.  Exact integers.
    For the lower side the totals are capped by A[k]; for the upper side they
    are floored by A[k]+1 and capped by 2k... no: the upper side has no cap, so
    we cap at A[k]+1 + WINDOW and carry the tail separately.  See `p_mass`.
    """
    raise NotImplementedError


def p_mass_lower(mp, N):
    """Exact dyadic mass p_n(0) of the lower-confined words, n = 0..N.

    p_n = sum over words with S_k <= A[k] for all k<=n of 2^{-S_k}.
    Returned as a list of Fractions.
    """
    assert not mp.upper
    Amax = mp.A(N)
    f = [0] * (Amax + 1)
    f[0] = 1                                # k = 0, S = 0
    out = [Fraction(1)]
    for k in range(1, N + 1):
        Ak = mp.A(k)
        g = [0] * (Ak + 1)
        # g[S'] = sum_{d>=1} f[S'-d] = prefix sums of f
        run = 0
        for S in range(0, Ak + 1):
            if 1 <= S <= len(f):
                run += f[S - 1]
            g[S] = run
        f = g
        tot = sum(f[S] * (1 << (Ak - S)) for S in range(Ak + 1))
        out.append(Fraction(tot, 1 << Ak))
    return out


def p_mass_upper(mp, N, slack):
    """Exact dyadic mass of the upper-rare words, n = 0..N, with totals tracked
    in the window [A[k]+1, A[k]+1+slack] and everything above folded in exactly.

    For the upper side the constraint is S_k >= A[k]+1.  Mass above the window
    is handled by noting that once S_k - (A[k]+1) = t is large the future is
    unconstrained for the next floor(t/(2-alpha))... we instead track the
    *excess* e_k = S_k - (A[k]+1) exactly up to `slack` and treat e > slack as
    absorbing with the exact unconstrained mass 1 minus the escape probability.
    That approximation is NOT exact, so this routine returns a two-sided bracket.
    """
    raise NotImplementedError


# ------------------------------------------------------------- utilities ----

def bitlen(m):
    return m.bit_length()


def drift_R(mp, n, S):
    """R_n = S_n - n log2 q as an exact comparison surrogate: returns the
    integer deficit D_n = A[n] - S_n (>= 0 iff confined, for the lower side)."""
    return mp.A(n) - S
