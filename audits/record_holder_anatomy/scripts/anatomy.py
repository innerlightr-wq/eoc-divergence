"""Exact measurement kit for the record-holder anatomy audit.

All arithmetic is exact (Python int / Fraction).  Floats appear only in printed
columns and never in a decision: every ceiling test is done on integers.

Coordinates
-----------
accelerated  T(m) = (3m+1)/2^{v2(3m+1)} on odd m; S_k the cumulative valuation;
             confinement after k steps is  S_k <= A[k] = floor(k log2 3).
standard     Tstd(x) = x/2 (x even), (3x+1)/2 (x odd); the parity word of x is
             v_i = Tstd^i(x) mod 2.  Phi is its inverse (paper Prop 2.2).
"""
from fractions import Fraction

# ---- exact A[k] = floor(k log2 3) ------------------------------------------
_A, _p = [0], 1
def A(k):
    """A[k] = floor(k log2 3) = bit_length(3^k) - 1.  Exact; no floating point."""
    global _p
    while len(_A) <= k:
        _p *= 3; _A.append(_p.bit_length() - 1)
    return _A[k]

# ---- accelerated orbit ------------------------------------------------------
def acc_orbit(m, cap=4000):
    """(depth, [(m_k, d_k, S_k)]) -- stops when confinement fails or cap is reached."""
    out, S, x = [], 0, m
    for k in range(1, cap + 1):
        y = 3 * x + 1
        if y == 0: break                      # m = -1/3 only; excluded
        d = (abs(y) & -abs(y)).bit_length() - 1
        S += d
        out.append((x, d, S))
        if S > A(k): return k - 1, out
        x = y // (1 << d)
        assert x * (1 << d) == y
    return len(out), out

def conf_depth(m, cap=4000):
    return acc_orbit(m, cap)[0]

# ---- standard-coordinate parity word ---------------------------------------
def parity_word(x, L):
    w = bytearray(L)
    for i in range(L):
        b = x & 1 if x >= 0 else x % 2
        w[i] = b
        x = (3 * x + 1) // 2 if b else x // 2
    return bytes(w)

# ---- periodic values --------------------------------------------------------
def c_of(w):
    """c_w = sum_{i: w_i=1} 3^{k-kappa_{i+1}} 2^i  (paper eq. 4.1)."""
    k = sum(w); tot = 0; seen = 0
    for i, b in enumerate(w):
        if b:
            seen += 1; tot += 3 ** (k - seen) << i
    return tot

def delta_of(w):
    return (1 << len(w)) - 3 ** sum(w)

# ---- word structure ---------------------------------------------------------
def rep_profile(w, pmax=None):
    """for each period p, the length of the maximal prefix with that period."""
    n = len(w); pmax = pmax or n // 2
    out = {}
    for p in range(1, min(pmax, n - 1) + 1):
        L = p
        while L < n and w[L] == w[L - p]:
            L += 1
        out[p] = L
    return out

def discrepancy(u):
    """max_j |k_j(u) - j*k/l| as an exact Fraction; u is balanced-with-slack-1 iff < 1."""
    l = len(u); k = sum(u)
    if l == 0: return Fraction(0)
    best, run = Fraction(0), 0
    for j in range(1, l + 1):
        run += u[j - 1]
        best = max(best, abs(Fraction(run) - Fraction(j * k, l)))
    return best

def v2(n):
    return None if n == 0 else (n & -n).bit_length() - 1

# ---- M1: the per-block ceiling ---------------------------------------------
LOG2_3_NUM, LOG2_3_DEN = None, None      # exact tests use integers only

def m1_row(m, u, word, horizon):
    """One initial square with block u (|u| = l) in the parity word of the integer m.

    Returns a dict with the exact quantities.  The ceiling test is done on
    integers:  2^{2l} <= |M|  and  |M| <= |m|(|delta| + c_u)  must both hold, and
    the derived inequality is  2l <= log2|m| + log2(|delta|+c_u).
    """
    l = len(u); k = sum(u)
    c = c_of(u); d = delta_of(u)
    M = m * d - c                                     # Phi(word) = m, v = 1
    per = (word[:horizon] == (bytes(u) * (horizon // l + 1))[:horizon])
    row = dict(l=l, k=k, dens=Fraction(k, l), disc=discrepancy(u),
               balanced=discrepancy(u) < 1, periodic=per, M=M, v2M=v2(M))
    if per or M == 0:
        row.update(lhs=None, rhs=None, slack=None); return row
    # exact bit-length form of  2l <= log2|m| + log2(|delta| + c_u)
    lhs = 2 * l
    rhs_int = abs(m) * (abs(d) + c)                   # exact integer
    rhs = rhs_int.bit_length()                        # >= log2 rhs_int
    row.update(lhs=lhs, rhs=rhs, slack=rhs - lhs,
               lower_ok=(abs(M) >= (1 << (2 * l))),
               upper_ok=(abs(M) <= rhs_int))
    return row

# ---- minimal realizer of a valuation word (the class construction) ----------
def minrep(word):
    """Least positive odd m whose accelerated valuation word starts with `word`.
    The odd m with a given word of total S form one class mod 2^{S+1}; this
    returns its least positive element, together with S and the orbit value."""
    r, S, k, mk = 1, 0, 0, 1
    for d in word:
        Ap = (3 * mk + 1) >> 1                        # A = 3 mk + 1 = 2 A'
        c = pow(3, k + 1, 1 << d)
        t = ((pow(c, -1, 1 << d) * ((1 << (d - 1)) - Ap)) % (1 << d)) if d >= 1 else 0
        r = r + t * (1 << (S + 1))
        mk = (3 * (mk + 2 * 3 ** k * t) + 1) >> d
        S += d; k += 1
    return r, S, mk
