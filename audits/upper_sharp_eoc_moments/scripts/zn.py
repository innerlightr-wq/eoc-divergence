#!/usr/bin/env python3
"""zn.py  --  shared module: the seed set Z_N, exact all-shift window statistics, Fourier DP.

Conventions (sources in this repository; see ../PREREGISTRATION.md section 0):
  s_j = d_0 + ... + d_{j-1},  S = s_N            Occupation/Compositions.lean:37  psum
  zero confinement: 2^{s_j} <= 3^j, j <= N       Occupation/Compositions.lean:62  Confined 0
                                                 Descent/Basic.lean:29            ConfinedUpTo
                                                 Divergence/CycleDrift.lean:30    ZeroConfined
  carry q_0 = 0, q_{j+1} = 3 q_j + 2^{s_j}       Divergence/Basic.lean:52,57      C / C_succ
  A[k] = (3**k).bit_length() - 1                 Occupation/Rate.lean:71          sN

The object (PREREGISTRATION section 0b):

  Q   = 2^{A[N]+1}
  Z_N = { m < Q : m odd, m zero-confined through N steps },   M = |Z_N|

built from WORDS, not by scanning integers: a zero-confined word D of length N with terminal sum S
contributes the 2^{A[N]-S} lifts of its least realizer r(D) to the common modulus Q.  No single
terminal shell is used for anything.

Realizer, additive form (prior art: Sturmian-Mahler Edge Lemma 2.1 / Def 2.2; EOC Rev 8 Prop 5.2):

  r(D) == 2^S - sum_{j<N} 3^{-(j+1)} 2^{s_j}   (mod 2^{S+1})

Exact integer arithmetic throughout this module except F_batch (complex128, labelled [F]).
"""

import numpy as np
from fractions import Fraction

# ------------------------------------------------------------------ primitives

def A(k):
    """A[k] = floor(k log2 3), as the exact integer (3**k).bit_length() - 1  (Occupation.sN)."""
    return (3 ** k).bit_length() - 1


def v2(n):
    """2-adic valuation of n >= 1."""
    return (n & -n).bit_length() - 1


def shell_table(N):
    """{S: #(zero-confined words of length N with terminal sum S)}, exact integers."""
    dp = {0: 1}
    for j in range(N):
        cap = A(j + 1)
        nd = {}
        for s, c in dp.items():
            for d in range(1, cap - s + 1):
                nd[s + d] = nd.get(s + d, 0) + c
        dp = nd
    return dp


def M_from_words(N):
    """M = sum_S |W(N,S)| * 2^{A[N]-S}, exact."""
    AN = A(N)
    return sum(c * 2 ** (AN - S) for S, c in shell_table(N).items())


# ------------------------------------------------------------------ Z_N, from words

def build_Z(N):
    """Z_N as a sorted numpy int64 array, built from words + lift weights.

    Returns (Z, Q, A[N]).  Exact: every element is an integer residue; the DFS accumulates
    sum_j 3^{-(j+1)} 2^{s_j} modulo Q with exact integer arithmetic, and reduction mod 2^{S+1}
    commutes with it, so (2^S - acc) mod 2^{S+1} is exactly r(D).
    """
    AN = A(N)
    Q = 1 << (AN + 1)
    inv3 = [pow(pow(3, j, Q), -1, Q) for j in range(N + 2)]
    pow2 = [1 << i for i in range(AN + 2)]
    caps = [A(j) for j in range(N + 1)]

    tab = shell_table(N)
    M = sum(c * 2 ** (AN - S) for S, c in tab.items())

    # residues are written straight into preallocated per-S int64 arrays: no Python int lists
    res = {S: np.empty(c, dtype=np.int64) for S, c in tab.items()}
    fill = {S: 0 for S in tab}
    stack = [(0, 0, 0)]
    # iterative DFS to avoid recursion limits at larger N
    while stack:
        j, s, acc = stack.pop()
        if j == N:
            mod = 1 << (s + 1)
            res[s][fill[s]] = (pow2[s] - acc) % mod
            fill[s] += 1
            continue
        term = (acc + inv3[j + 1] * pow2[s]) % Q
        cap = caps[j + 1]
        for d in range(1, cap - s + 1):
            stack.append((j + 1, s + d, term))
    for S in tab:
        assert fill[S] == tab[S], "word count mismatch at S=%d" % S

    # lifts written in place, one strided block per lift index: no large temporaries
    Z = np.empty(M, dtype=np.int64)
    off = 0
    for S in sorted(tab):
        R = res[S]
        n = R.size
        step = 1 << (S + 1)
        for t in range(1 << (AN - S)):
            Z[off:off + n] = R
            if t:
                Z[off:off + n] += step * t
            off += n
        res[S] = None
    assert off == M, "lift expansion filled %d of %d" % (off, M)
    Z.sort()
    return Z, Q, AN


# ------------------------------------------------------------------ brute force, for validation

def brute_Z(N):
    """Independent brute scan: every odd m < 2^{A[N]+1}, actual accelerated orbit.

    a(m) = v2(3m+1), T(m) = (3m+1)/2^{a(m)}  (Divergence.a / Divergence.T);
    zero-confined through N steps iff 2^{s_j} <= 3^j for every j <= N.
    """
    AN = A(N)
    Q = 1 << (AN + 1)
    pow3 = [3 ** j for j in range(N + 1)]
    out = []
    for m in range(1, Q, 2):
        x = m
        s = 0
        ok = True
        for j in range(N):
            y = 3 * x + 1
            a = v2(y)
            x = y >> a
            s += a
            if (1 << s) > pow3[j + 1]:
                ok = False
                break
        if ok:
            out.append(m)
    return np.array(out, dtype=np.int64), Q


def count_confined_below(N, limit):
    """#{odd m < limit : m zero-confined through N steps}, by direct accelerated-orbit scan.

    Independent of the word construction: this uses the actual map a(m) = v2(3m+1),
    T(m) = (3m+1)/2^{a(m)} (Divergence.a / Divergence.T).  Exact integers, O(limit*N) time and
    O(1) memory -- which is how the extension depths are reached without building Z_N at all.
    """
    pow3 = [3 ** j for j in range(N + 1)]
    cnt = 0
    for m in range(1, limit, 2):
        x, s = m, 0
        for j in range(N):
            y = 3 * x + 1
            a = v2(y)
            x = y >> a
            s += a
            if (1 << s) > pow3[j + 1]:
                break
        else:
            cnt += 1
    return cnt


def rmin_direct(N, cap=None):
    """r_min(N,0) by direct orbit scan over odd m, ascending.  Exact."""
    pow3 = [3 ** j for j in range(N + 1)]
    limit = cap if cap is not None else (1 << (A(N) + 1))
    m = 1
    while m < limit:
        x = m
        s = 0
        ok = True
        for j in range(N):
            y = 3 * x + 1
            a = v2(y)
            x = y >> a
            s += a
            if (1 << s) > pow3[j + 1]:
                ok = False
                break
        if ok:
            return m
        m += 2
    return None


# ------------------------------------------------------------------ exact all-shift window law

def window_hist(Z, Q, H):
    """Exact histogram of X_y = #(Z in [y, y+H) mod Q) over ALL y mod Q.

    X_{y+1} - X_y = [ (y+H) mod Q in Z ] - [ y mod Q in Z ], so X is piecewise constant in y with
    at most 2M breakpoints.  Returns (values, counts) as int64 arrays with sum(counts) == Q and
    sum(values*counts) == M*H.  Cost O(M log M), independent of Q.  Exact integers.

    Memory: the breakpoints are carried in ONE int64 array of length 2M, holding the key
    2*position + tag (tag 1 = an element enters at y+H, tag 0 = an element leaves at y), sorted
    in place -- an argsort, or assembling per-segment start/end/value arrays, would cost several
    more arrays of that length.  Buffers are released as soon as they are consumed, and the
    histogram is assembled from DIFFERENCES of the breakpoint positions.
    """
    M = Z.size
    assert H <= Q // 2, "window_hist assumes H <= Q/2"
    X0 = int(np.searchsorted(Z, H, side='left'))          # window [0,H), no wrap

    keys = np.empty(2 * M, dtype=np.int64)
    keys[:M] = Z
    keys[:M] <<= 1                                        # tag 0 -> delta -1
    keys[M:] = Z
    keys[M:] -= H
    np.add(keys[M:], Q, out=keys[M:], where=keys[M:] < 0)  # (Z - H) mod Q
    keys[M:] <<= 1
    keys[M:] += 1                                         # tag 1 -> delta +1
    keys.sort()

    pos = keys >> 1
    keys &= 1
    keys <<= 1
    keys -= 1                                             # keys is now the delta array
    first = np.empty(pos.size, dtype=bool)
    first[0] = True
    np.not_equal(pos[1:], pos[:-1], out=first[1:])
    idx = np.flatnonzero(first)
    del first
    upos = pos[idx]                                       # distinct breakpoint positions
    del pos
    g = np.add.reduceat(keys, idx)                        # aggregated delta per position
    del keys, idx
    np.cumsum(g, out=g)
    assert int(g[-1]) == 0, "total delta over a full cycle must vanish"

    n = upos.size
    first_pos = int(upos[0])
    last_pos = int(upos[-1])
    # X = X0 on [0, upos[0]+1) and again on [upos[-1]+1, Q) (since the deltas sum to zero);
    # on [upos[i]+1, upos[i+1]+1) it is X0 + cumsum(g)[i].
    wrap = (first_pos + 1) + (Q - 1 - last_pos)
    if n > 1:
        seglen = np.diff(upos)
        segval = g[:-1]
        segval += X0
        assert int(segval.min()) >= 0, "window count went negative"
        counts = np.bincount(segval, weights=seglen,
                             minlength=int(segval.max()) + 1)
        del seglen, segval
    else:
        counts = np.zeros(X0 + 1, dtype=np.float64)
    if counts.size <= X0:
        counts = np.concatenate([counts, np.zeros(X0 + 1 - counts.size)])
    counts[X0] += wrap
    # every weight is an integer below 2^53, so the float64 accumulation above is exact
    counts = np.rint(counts).astype(np.int64)
    values = np.flatnonzero(counts)
    counts = counts[values]
    assert int(counts.sum()) == Q, "segment lengths must sum to Q"
    assert int((values * counts).sum()) == M * H, "sum_y X_y must equal M*H"
    return values.astype(np.int64), counts


def central_moments(values, counts, M, H, Q, ks=(2, 4, 6)):
    """Exact central moments mu_k = (1/Q) sum_y (X_y - E)^k, E = M*H/Q, as Fractions."""
    E = Fraction(M * H, Q)
    out = {}
    for k in ks:
        tot = Fraction(0)
        for v, c in zip(values.tolist(), counts.tolist()):
            tot += c * (Fraction(v) - E) ** k
        out[k] = tot / Q
    return E, out


# ------------------------------------------------------------------ exact pair statistics

def pair_stats(Z, Q, H, chunk=1 << 20):
    """Exact (P_ordered, weighted) where

      P_ordered = #{(m,m') in Z^2 : m != m', circular |m-m'| < H}
      weighted  = sum_{m != m'} (H - d(m,m'))_+        [ = sum_y X_y^2 - M*H ]

    Valid for H <= Q/2: each unordered pair is seen once in the forward direction, so the ordered
    count is twice the forward count.  Exact integers.

    Streams over Z in chunks: the only full-length array held is the prefix-sum table, so peak
    memory is O(M) once plus O(chunk), not O(M) a dozen times over.
    """
    M = Z.size
    assert H <= Q // 2, "pair_stats assumes H <= Q/2"
    csum = np.empty(M + 1, dtype=np.int64)
    csum[0] = 0
    np.cumsum(Z, out=csum[1:])

    fwd = 0
    wtot = 0
    for a in range(0, M, chunk):
        z = Z[a:min(a + chunk, M)]
        right = z + H
        lo = np.searchsorted(Z, z + 1, side='left')
        hi = np.searchsorted(Z, np.minimum(right, Q), side='left')
        cnt = hi - lo
        ssum = csum[hi] - csum[lo]                    # sum of the m' in (m, m+H), no wrap
        fwd += int(cnt.sum())
        wtot += int((H * cnt - (ssum - cnt * z)).sum())
        over = right > Q
        if over.any():
            zo = z[over]
            wh = np.searchsorted(Z, np.maximum(right[over] - Q, 0), side='left')
            fwd += int(wh.sum())
            # wrapped m' lie in [0, m+H-Q), at circular distance m' + Q - m
            wtot += int((H * wh - (csum[wh] + (Q - zo) * wh)).sum())
    return 2 * fwd, 2 * wtot


# ------------------------------------------------------------------ Fourier, word-level DP  [F]

def F_batch(N, hs, M=None):
    """F(h) = (1/M) sum_{m in Z_N} e(h m / Q), by word-level DP with lift weights.  [F] complex128.

    Structure used (and verified against brute force in check_zn.py):  the 2^{A-S} lifts of one
    word of terminal sum S contribute

        sum_{t < 2^{A-S}} e(h (r + t 2^{S+1}) / Q) = e(h r / Q) * 2^{A-S} * [ 2^{A-S} | h ],

    a geometric sum that VANISHES unless 2^{A-S} | h; and when 2^{A-S} | h, writing
    h = 2^{A-S} h' gives e(h r / Q) = e(h' r / 2^{S+1}).  Hence

        F(h) = (1/M) sum_{S >= A[N]-v2(h)} 2^{A[N]-S} T_S(h / 2^{A[N]-S}),
        T_S(u) = sum_{D : s_N(D)=S} e(u r(D)/2^{S+1}).

    In particular for odd h only the terminal shell S = A[N] contributes, with h' = h.
    """
    AN = A(N)
    Q = 1 << (AN + 1)
    if M is None:
        M = M_from_words(N)
    hs = np.asarray(hs, dtype=np.int64)
    out = np.zeros(hs.size, dtype=np.complex128)
    tv = np.array([v2(int(h)) for h in hs], dtype=np.int64)
    caps = [A(j) for j in range(N + 1)]
    tab = shell_table(N)

    for S in sorted(tab):
        need = AN - S                      # v2(h) >= need
        sel = np.flatnonzero(tv >= need)
        if sel.size == 0:
            continue
        hsel = hs[sel] >> need          # the reduced frequency h' = h / 2^{A-S}
        mS = 1 << (S + 1)
        inv3 = [pow(pow(3, j, mS), -1, mS) for j in range(N + 2)]
        # dp[s] = complex array over hsel
        dp = {0: np.ones(hsel.size, dtype=np.complex128)}
        for j in range(N):
            ndp = {}
            rem = N - 1 - j                # letters still to place, each >= 1
            cap = caps[j + 1]
            for s, arr in dp.items():
                coef = (inv3[j + 1] * (1 << s)) % mS
                ph = (-(hsel % mS) * coef) % mS
                cur = arr * np.exp(2j * np.pi * (ph.astype(np.float64) / mS))
                hi = min(cap, S - rem)
                for sp in range(s + 1, hi + 1):
                    if sp in ndp:
                        ndp[sp] += cur
                    else:
                        ndp[sp] = cur.copy()
            dp = ndp
            if not dp:
                break
        if S in dp:
            sign = np.where(hsel % 2 == 0, 1.0, -1.0)      # e(h 2^S / 2^{S+1}) = (-1)^h
            out[sel] += (1 << (AN - S)) * dp[S] * sign
    return out / M


def F_brute(Z, Q, hs):
    """Direct exponential sums over Z_N.  [F] complex128.  For validation only."""
    hs = np.asarray(hs, dtype=np.int64)
    out = np.empty(hs.size, dtype=np.complex128)
    Zf = Z.astype(np.float64)
    for i, h in enumerate(hs.tolist()):
        ph = (Z * h) % Q
        out[i] = np.exp(2j * np.pi * (ph.astype(np.float64) / Q)).sum()
    return out / Z.size


# ------------------------------------------------------------------ uniform word sampling

def completion_counts(N, S=None):
    """cnt[j][s] = #completions from (j, s) to a zero-confined word of length N.

    If S is given, completions must have terminal sum exactly S; else any terminal sum.
    Exact integers.
    """
    caps = [A(j) for j in range(N + 1)]
    cnt = [dict() for _ in range(N + 1)]
    if S is None:
        for s in range(caps[N] + 1):
            cnt[N][s] = 1
    else:
        cnt[N][S] = 1
    for j in range(N - 1, -1, -1):
        cap = caps[j + 1]
        for s in range(caps[j] + 1):
            tot = 0
            for sp in range(s + 1, cap + 1):
                tot += cnt[j + 1].get(sp, 0)
            if tot:
                cnt[j][s] = tot
    return cnt


def sample_word(N, cnt, rng):
    """One uniform sample from the ensemble counted by cnt (exact rational choice)."""
    caps = [A(j) for j in range(N + 1)]
    s = 0
    word = []
    for j in range(N):
        tot = cnt[j][s]
        r = rng.randrange(tot)
        acc = 0
        cap = caps[j + 1]
        for sp in range(s + 1, cap + 1):
            c = cnt[j + 1].get(sp, 0)
            if c == 0:
                continue
            acc += c
            if r < acc:
                word.append(sp - s)
                s = sp
                break
        else:
            raise AssertionError("sampling fell through")
    return tuple(word), s
