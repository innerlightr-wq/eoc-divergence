"""Controls C1-C4 for the record-holder anatomy audit.  Exact arithmetic.

C1  the negative zero-confined cycles of 3x+1 and their small preimages
C2  the critical Sturmian point: the valuation word d_i = floor((i+1)a) - floor(ia),
    a = log2 3, and the least realizers of its prefixes
C3  least realizers of RANDOM zero-confined words, and of shuffled surrogates of
    the record holders' own words (same multiset of valuations, hence same density
    and same total drift)
C4  the 3x-1 system.  PROVED: m -> -m is an exact conjugacy from 3x-1 on the
    positive integers to 3x+1 on the negative integers, valuation by valuation --
    v2(3(-m)+1) = v2(1-3m) = v2(3m-1) and T(-m) = -T'(m) -- so the two systems
    have identical S_k and identical confinement.
"""
import random
from fractions import Fraction
from anatomy import A, acc_orbit, minrep, parity_word, c_of, delta_of, v2

# ---------------- C2: the critical Sturmian valuation word -------------------
def sturmian_valuations(N):
    """d_i = floor((i+1) log2 3) - floor(i log2 3), i = 0..N-1.  Exact: floor(i*a)
    is the bit length of 3^i minus one."""
    f = [ (3 ** i).bit_length() - 1 for i in range(N + 1) ]
    return [f[i + 1] - f[i] for i in range(N)]

def sturmian_realizers(Ns):
    d = sturmian_valuations(max(Ns))
    return {N: minrep(d[:N]) for N in Ns}

# ---------------- C3: random and shuffled zero-confined words ----------------
def random_confined_word(N, rng):
    """Uniform over the ALLOWED LETTER at each step (not uniform over words --
    documented, and the surrogate below is the density-matched control)."""
    w, S = [], 0
    for k in range(1, N + 1):
        hi = A(k) - S
        if hi < 1: return None
        d = rng.randint(1, hi)
        w.append(d); S += d
    return w

def shuffled_surrogate(word, rng, tries=20000):
    """A permutation of `word` that is still zero-confined: same multiset of
    valuations, hence the same density and the same endpoint drift."""
    w = list(word)
    for _ in range(tries):
        rng.shuffle(w)
        S = 0; ok = True
        for k, d in enumerate(w, 1):
            S += d
            if S > A(k): ok = False; break
        if ok: return list(w)
    return None

# ---------------- C4: the 3x-1 system ---------------------------------------
def acc_orbit_minus(m, cap=4000):
    out, S, x = [], 0, m
    for k in range(1, cap + 1):
        y = 3 * x - 1
        if y == 0: break
        d = (abs(y) & -abs(y)).bit_length() - 1
        S += d
        out.append((x, d, S))
        if S > A(k): return k - 1, out
        x = y // (1 << d)
    return len(out), out

def parity_word_minus(x, L):
    w = bytearray(L)
    for i in range(L):
        b = x % 2
        w[i] = b
        x = (3 * x - 1) // 2 if b else x // 2
    return bytes(w)

def M_minus(m, u):
    """Phi'(v) = -Phi(v), so Phi'(u^inf) = c_u/(3^k - 2^l) and M' = m(3^k-2^l) - c_u."""
    return m * (3 ** sum(u) - (1 << len(u))) - c_of(u)
