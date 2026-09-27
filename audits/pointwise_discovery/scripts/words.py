"""Exact transfer table, exact conditional sampling, word features, and the
realizer deficit  delta(w) = S+1 - log2 r(w).

The table is the one of `audits/record_holder_anatomy` §2.7 rescaled so that the
top row is the integer `num_n`:

    g_n(S) = 2^{Smax - S}                      for admissible S
    g_k(S) = sum_{d>=1, (k+1,S+d) admissible} g_{k+1}(S+d)
    p_n    = g_0(0) / 2^{Smax}

Admissibility is the rare-side condition of the map:
    lower side (q<4):  S_k <= A[k]
    upper side (q>4):  A[k]+1 <= S_k <= Smax     (Smax a stated truncation)
"""
import random
from math import log2
from fractions import Fraction
from eoc import Map, carry, realizer


class Table:
    def __init__(self, mp, n, smax=None):
        self.mp, self.n = mp, n
        if mp.upper:
            self.smax = smax if smax is not None else 3 * n + 40
        else:
            self.smax = mp.A(n)
        self.g = self._build()

    def lo(self, k):
        if k == 0:
            return 0                       # the rare-side condition starts at k=1
        return self.mp.A(k) + 1 if self.mp.upper else 0

    def hi(self, k):
        if k == 0:
            return 0
        return self.smax if self.mp.upper else min(self.mp.A(k), self.smax)

    def _build(self):
        """Store, for each k, the suffix sums  suf[k][S] = sum_{S' >= S} g[k][S'].

        Sampling then costs one binary search per letter instead of a scan.
        """
        n, smax = self.n, self.smax
        row = [0] * (smax + 1)
        for S in range(self.lo(n), self.hi(n) + 1):
            row[S] = 1 << (smax - S)
        sufs = [None] * (n + 1)
        suf = [0] * (smax + 2)
        for S in range(smax, -1, -1):
            suf[S] = suf[S + 1] + row[S]
        sufs[n] = suf
        for k in range(n - 1, -1, -1):
            nxt = sufs[k + 1]
            lo1, hi1 = self.lo(k + 1), self.hi(k + 1)
            row = [0] * (smax + 1)
            for S in range(self.lo(k), self.hi(k) + 1):
                a = max(S + 1, lo1)
                if a <= hi1:
                    row[S] = nxt[a] - nxt[hi1 + 1]
            suf = [0] * (smax + 2)
            for S in range(smax, -1, -1):
                suf[S] = suf[S + 1] + row[S]
            sufs[k] = suf
        return sufs

    def gval(self, k, S):
        return self.g[k][S] - self.g[k][S + 1]

    def num(self):
        return self.gval(0, 0)

    def p(self):
        return Fraction(self.num(), 1 << self.smax)

    def truncation_bound(self):
        """Exact upper bound on the dyadic mass omitted by the Smax cutoff.

        Only the upper side truncates; the bound is  sum_{S>Smax} C(S-1,n-1)2^{-S},
        the mass of *all* words of length n with total above Smax.
        """
        if not self.mp.upper:
            return Fraction(0)
        from math import comb
        n, smax = self.n, self.smax
        tot = Fraction(0)
        S = smax + 1
        while S < smax + 400:
            tot += Fraction(comb(S - 1, n - 1), 1 << S)
            S += 1
        return tot

    def sample(self, rng):
        """One word, exactly from the law  2^{-S(w)} / p_n  on rare-side words."""
        w, S = [], 0
        for k in range(self.n):
            nxt = self.g[k + 1]
            lo1, hi1 = self.lo(k + 1), self.hi(k + 1)
            a = max(S + 1, lo1)
            base = nxt[a]; tail = nxt[hi1 + 1]
            tot = base - tail
            x = rng.randrange(tot)
            # least j in [a, hi1] with  base - nxt[j+1] > x
            target = base - x           # want nxt[j+1] < target
            lo, hi = a, hi1
            while lo < hi:
                mid = (lo + hi) // 2
                if nxt[mid + 1] < target: hi = mid
                else: lo = mid + 1
            w.append(lo - S); S = lo
        return w


# --------------------------------------------------------------- features ---

def slack_path(mp, w):
    """D_k >= 0: the integer distance to the rare-side boundary at each k."""
    D, S = [], 0
    for k, a in enumerate(w, 1):
        S += a
        D.append(S - (mp.A(k) + 1) if mp.upper else mp.A(k) - S)
    return D


def features(mp, w):
    n = len(w)
    S = sum(w)
    D = slack_path(mp, w)
    f = {}
    f["n"] = n
    f["S"] = S
    f["mean_a"] = S / n
    for v in (1, 2, 3, 4):
        f[f"n_a{v}"] = w.count(v)
    f["n_a5p"] = sum(1 for a in w if a >= 5)
    # longest run of a == 1
    best = run = 0
    for a in w:
        run = run + 1 if a == 1 else 0
        best = max(best, run)
    f["run1_max"] = best
    f["D_max"] = max(D)
    f["D_end"] = D[-1]
    f["D_mean"] = sum(D) / n
    f["contacts0"] = sum(1 for d in D if d == 0)
    f["contacts1"] = sum(1 for d in D if d <= 1)
    f["argmax_D"] = D.index(max(D)) / n
    f["first0"] = (D.index(0) / n) if 0 in D else 1.0
    f["last0"] = (max(i for i, d in enumerate(D) if d == 0) / n) if 0 in D else 0.0
    # carry area Z = sum 2^{-D_k}  (order-sensitive; = 3 G_n up to frac parts)
    f["logZ"] = log2(sum(2.0 ** (-d) for d in D) + 2.0 ** -30)
    for W in (8, 16, 32):
        if n > W:
            f[f"slope{W}"] = (S - sum(w[:n - W])) / W      # terminal slope
            f[f"slope{W}_0"] = sum(w[:W]) / W              # initial slope
    f["t11"] = sum(1 for i in range(n - 1) if w[i] == 1 and w[i + 1] == 1)
    f["a0"] = w[0]
    f["lead1"] = next((i for i, a in enumerate(w) if a != 1), n)   # leading 1-run
    return f


def deficit(mp, w):
    """(r, S, delta) with delta = S+1 - log2 r, exact r."""
    C, S = carry(mp, w)
    r = realizer(mp, w)
    return r, S, (S + 1) - log2(r)


def exact_delta_bits(S, r):
    """S + 1 - log2 r, computed without float error in the integer part."""
    return (S + 1) - (r.bit_length() - 1) - log2(r / (1 << (r.bit_length() - 1)))
