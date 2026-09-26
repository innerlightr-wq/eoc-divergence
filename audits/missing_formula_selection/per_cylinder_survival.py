#!/usr/bin/env python3
"""The per-cylinder survival law, and the exact Q = 1 plateau.

Every identity here is checked in exact integer arithmetic.  Floating point is
used only to report hazards and logarithms.

Repository conventions: T(m) = (3m+1)/2^{v_2(3m+1)} on odd m; word a = (a_1..a_N),
S_j = a_1+..+a_j; zero-confinement is the exact integer test 2^{S_j} <= 3^j.
M = 2^B - 1, so O_M = ceil(M/2) = 2^{B-1}.

Three statements:

(1) PLATEAU.  A confined word w of length N has cylinder C(w) = r_w + 2^{S_N+1} Z.
    If S_N + 1 <= B then |C(w) cap [1,M]| = 2^{B-S_N-1} = O_M * mu(w) exactly, so
    summing over w gives A_{N,M} = O_M p_N, i.e. Q_{N,M} = 1 EXACTLY, for every
    N <= N*(B) := max{ N : max_S(confined,N) + 1 <= B }.

(2) PER-CYLINDER SURVIVAL.  Parametrise m_0 = r_w + 2^{S+1} t, t = 0..n_w-1 over the
    admissible indices in [1,M].  Since 2^{S} m_N = 3^N m_0 + C_N,

        m_N = (3^N r_w + C_N)/2^S + 2 * 3^N * t,

    and 3^N is odd, so m_N mod 2^k is a bijective affine function of t mod 2^{k-1}.
    As a_N = v_2(3 m_N + 1) is determined by m_N mod 2^{a_N+1}, the failures
    {a_N > K} form ONE residue class t = t*_w (mod 2^K), K = K(N,S).  Hence exactly

        surv_w = n_w - floor((n_w - 1 - t*_w)/2^K) - 1     if t*_w <  n_w
        surv_w = n_w                                        if t*_w >= n_w

    and A_{N+1,M} = sum_w surv_w.

(3) CONVERSE.  2^K | n_w  <=>  the per-cylinder hazard is exactly 1 - 2^{-K}.

The content is that the one-step law is symbolic (1 - 2^{-K(N,S)}) plus a
floor-function truncation at the height cutoff -- a placement/discrepancy term, not
an arithmetic tilt.  Lineage: the bijection between valuation words and residue
classes is classical (Terras 1976; Everett 1977; Lagarias 1985).  The new part is
the explicit truncated survival count above.
"""
from collections import defaultdict
from fractions import Fraction


def confined_mass(nmax):
    """exact p_n and the (N, S) shell-weight tables for confined words"""
    f = {0: 1}
    P = [Fraction(1)]
    tables = [dict(f)]
    for n in range(1, nmax + 1):
        g = {}
        for S, c in f.items():
            a = 1
            while (1 << (S + a)) <= 3 ** n:
                g[S + a] = g.get(S + a, 0) + c
                a += 1
        f = g
        P.append(sum(Fraction(c, 1 << S) for S, c in f.items()))
        tables.append(dict(f))
    return P, tables


def Kcap(N, S):
    """largest a with 2^{S+a} <= 3^{N+1}: the admissible next valuation cap"""
    a = 0
    while (1 << (S + a + 1)) <= 3 ** (N + 1):
        a += 1
    return a


def survivors(M, nmax, q=1):
    """records (m0, m_n, S_n) for odd m0 <= M still zero-confined at each depth"""
    pop = [(m, m, 0) for m in range(1, M + 1, 2)]
    out = [pop]
    for n in range(1, nmax + 1):
        nxt, p3 = [], 3 ** n
        for m0, m, S in pop:
            x = 3 * m + q
            a = (x & -x).bit_length() - 1
            S2 = S + a
            if (1 << S2) <= p3:
                nxt.append((m0, x >> a, S2))
        pop = nxt
        out.append(pop)
        if not pop:
            break
    return out


print(__doc__)

print("=" * 78)
print("(1) THE PLATEAU IS AN IDENTITY:  Q_{N,M} = 1 exactly for N <= N*(B)")
print("=" * 78)
P, tables = confined_mass(40)
print(f"  {'B':>3} {'N*(B)':>6} {'largest N with Q=1':>20} {'match':>7} {'(B-1)/alpha':>12}")
import math
ALPHA = math.log2(3)
bad_plateau = 0
for B in (8, 10, 12, 14, 16, 18, 20):
    M = (1 << B) - 1
    OM = (M + 1) // 2
    Nstar = max(N for N in range(len(tables)) if max(tables[N]) + 1 <= B)
    A = [len(s) for s in survivors(M, 30)]
    lastone = -1
    for N in range(min(len(A), 31)):
        if Fraction(A[N]) == OM * P[N]:
            lastone = N
        else:
            break
    ok = (Nstar == lastone)
    bad_plateau += (not ok)
    print(f"  {B:>3} {Nstar:>6} {lastone:>20} {'yes' if ok else 'NO':>7} {(B-1)/ALPHA:>12.2f}")
print(f"  plateau mismatches: {bad_plateau}")

print()
print("=" * 78)
print("(2)+(3) PER-CYLINDER EXACTNESS, THE CONVERSE, AND THE SURVIVAL FORMULA")
print("=" * 78)
print(f"  {'M':>9} {'cylinders':>10} {'2^K | n_w':>10} {'of those exact':>15}"
      f" {'not div':>9} {'of those exact':>15} {'formula fails':>14}")
tot_cyl = tot_form = 0
for B in (12, 14, 16, 18, 20):
    M = (1 << B) - 1
    S = survivors(M, 200)
    ncyl = ndiv = ndiv_ex = nnd = nnd_ex = nform = 0
    depths = 0
    for N in range(0, len(S) - 1):
        if not S[N] or not S[N + 1]:
            break
        depths += 1
        alive = {r[0] for r in S[N + 1]}
        cyl = defaultdict(list)
        for m0, mN, Sc in S[N]:
            cyl[(Sc, m0 & ((1 << (Sc + 1)) - 1))].append(m0)
        for (Sc, r), lst in cyl.items():
            K = Kcap(N, Sc)
            mod = 1 << (Sc + 1)
            lst.sort()
            n = len(lst)
            # the admissible indices t must be contiguous 0..n-1
            t0 = lst[0] // mod
            assert [m // mod - t0 for m in lst] == list(range(n)), "t not contiguous"
            fails = [i for i, m in enumerate(lst) if m not in alive]
            ncyl += 1
            exact = (Fraction(n - len(fails), n) == 1 - Fraction(1, 1 << K))
            if n % (1 << K) == 0:
                ndiv += 1
                ndiv_ex += exact
            else:
                nnd += 1
                nnd_ex += exact
            # the closed-form survival count
            if fails:
                cls = {t % (1 << K) for t in fails}
                assert len(cls) == 1, f"failures not one class mod 2^K: {sorted(cls)}"
                ts = cls.pop()
                pred = n - ((n - 1 - ts) // (1 << K) + 1) if ts < n else n
            else:
                pred = n
            if pred != n - len(fails):
                nform += 1
    tot_cyl += ncyl
    tot_form += nform
    print(f"  2^{B}-1 {ncyl:>12,} {ndiv:>10,} {ndiv_ex:>15,} {nnd:>9,} {nnd_ex:>15}"
          f" {nform:>14}   ({depths} depths)")
print()
print(f"  TOTAL cylinders checked: {tot_cyl:,}   survival-formula failures: {tot_form}")
print("  'of those exact' in the divisible column should equal the divisible count,")
print("  and in the non-divisible column should be 0: divisibility is exactly the")
print("  condition for the symbolic hazard to hold on the nose.")

print()
print("=" * 78)
print("(4) THE ALL-ONES RAY: an exact realizer, maximally unfavorable")
print("=" * 78)
print("  For w = 1^N: C_N = 3^N - 2^N, so r_w = (2^N - C_N) 3^{-N} mod 2^{N+1} = 2^{N+1} - 1,")
print("  the LARGEST odd residue mod 2^{N+1}.  The all-1 ray therefore sits at the top of")
print("  its shell and is the last to be included by any height cutoff.")
bad = 0
for N in range(1, 25):
    C = 3 ** N - 2 ** N
    q = 1 << (N + 1)
    r = ((1 << N) - C) * pow(3, -N, q) % q
    if r != q - 1:
        bad += 1
    m, w = r, []
    for _ in range(N):
        x = 3 * m + 1
        a = (x & -x).bit_length() - 1
        w.append(a)
        m = x >> a
    if w != [1] * N:
        bad += 1
print(f"  checked N = 1..24 (closed form r_w = 2^{{N+1}}-1 and forward word = 1^N):"
      f" violations = {bad}")

print()
print("=" * 78)
print("(5) THE RETRACTION: why the argument must be made PER CYLINDER")
print("=" * 78)
print("  An earlier form of (2) claimed that divisibility of a BARRIER-CELL size by 2^K")
print("  forces an exact hazard.  A barrier cell (N,S) is a union of many cylinders with")
print("  different offsets t*_w, so the argument does not survive the union.  Counting the")
print("  cells where 2^K divides the cell size but the hazard is NOT exactly 1 - 2^{-K}:")
print()
print(f"  {'M':>9} {'cells':>8} {'2^K | size':>11} {'of those exact':>15} {'COUNTEREXAMPLES':>16}")
for B in (12, 14, 16, 18):
    M = (1 << B) - 1
    S = survivors(M, 200)
    ncell = ndiv = ndivex = 0
    for N in range(0, len(S) - 1):
        if not S[N] or not S[N + 1]:
            break
        alive = {r[0] for r in S[N + 1]}
        cells = defaultdict(lambda: [0, 0])
        for m0, mN, Sc in S[N]:
            c = cells[Sc]
            c[0] += 1
            c[1] += 1 if m0 in alive else 0
        for Sc, (n, o) in cells.items():
            K = Kcap(N, Sc)
            ncell += 1
            if n % (1 << K) == 0:
                ndiv += 1
                ndivex += (Fraction(o, n) == 1 - Fraction(1, 1 << K))
    print(f"  2^{B}-1 {ncell:>11,} {ndiv:>11,} {ndivex:>15,} {ndiv - ndivex:>16,}")
print()
print("  Non-zero counterexample counts are the retraction: the divisibility criterion is")
print("  valid per cylinder (section 3 above, exact with an exact converse) and invalid")
print("  per barrier cell.")
