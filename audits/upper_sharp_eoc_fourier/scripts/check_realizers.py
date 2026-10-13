#!/usr/bin/env python3
"""check_realizers.py  --  [V] exact realizer arithmetic on the terminal shell.

Status label: [V]  (verified by exact integer computation, for the stated finite range only)

What is checked, all in exact integer arithmetic:

  (1) the realizer congruence  3^N r + q_N == 2^S  (mod 2^(S+1))  holds for the
      residue produced by inverting 3^N, for every word of the terminal shell, N <= 16;
  (2) the shell map  D |-> r(D)  is injective (distinct residues), N <= 16;
  (3) every shell realizer is == 3 (mod 4)  -- forced by d_0 = 1;
      Lean input in this repository: Descent.a_eq_one_of_confined and
      Descent.mod_four_of_confined (Descent/ResidueLaw.lean), both proved there;
  (4) every shell realizer is re-verified by *direct accelerated-orbit iteration*:
      its actual valuation word equals D, it is 0-confined for N steps, it is odd;
  (5) true r_min(N,0) by direct seed scan, N <= 14, against the terminal-shell
      minimum -- showing the shell minimum is an UPPER BOUND only;
  (6) the mixed-shell weighting identity
          sum_S |W(N,S)| * 2^(A[N]-S)  ==  #{odd m < 2^(A[N]+1) : 0-confined for N steps}
      at N = 8, 10, 12, 14.

Exits non-zero on any failed assertion.  Writes nothing; prints to stdout only.

Usage:  python3 check_realizers.py [--quick]
"""

import sys

# ---------------------------------------------------------------- primitives

def A(k):
    return (3 ** k).bit_length() - 1


def v2(n):
    """2-adic valuation of n >= 1."""
    return (n & -n).bit_length() - 1


def shell_words(N):
    """All 0-confined positive words of length N with terminal sum exactly A[N]."""
    S = A(N)
    out = []
    w = [0] * N

    def rec(j, s):
        if j == N:
            if s == S:
                out.append(tuple(w))
            return
        for d in range(1, A(j + 1) - s + 1):
            w[j] = d
            rec(j + 1, s + d)

    rec(0, 0)
    return out, S


def carry(d):
    """q_0 = 0, q_{j+1} = 3 q_j + 2^{s_j}.  Returns (q_N, s_N).

    This is Divergence.C / Divergence.C_succ of this repository, evaluated on a
    prescribed word instead of an orbit.
    """
    q = 0
    s = 0
    for dj in d:
        q = 3 * q + 2 ** s
        s += dj
    return q, s


def carry_closed_form(d):
    """q_N = sum_{j<N} 3^{N-1-j} 2^{s_j}."""
    N = len(d)
    s = [0] * (N + 1)
    for j in range(N):
        s[j + 1] = s[j] + d[j]
    return sum(3 ** (N - 1 - j) * 2 ** s[j] for j in range(N))


def least_realizer(d):
    """The unique r < 2^(S+1) with 3^N r + q_N == 2^S (mod 2^(S+1))."""
    N = len(d)
    q, S = carry(d)
    Q = 2 ** (S + 1)
    return ((2 ** S - q) * pow(pow(3, N, Q), -1, Q)) % Q, q, S, Q


def orbit_word(m, N, pow3):
    """Actual accelerated-orbit valuation word of m, with exact 0-confinement.

    a(m) = v2(3m+1), T(m) = (3m+1)/2^{a(m)} -- Divergence.a / Divergence.T.
    Returns (word, confined_for_N_steps).
    """
    d = []
    s = 0
    for j in range(N):
        x = 3 * m + 1
        a = v2(x)
        d.append(a)
        m = x >> a
        s += a
        if 2 ** s > pow3[j + 1]:
            return tuple(d), False
    return tuple(d), True


def capped_depth(m, cap, pow3):
    """Largest j <= cap with 2^{s_i} <= 3^i for every i <= j."""
    s = 0
    for j in range(cap):
        x = 3 * m + 1
        a = v2(x)
        m = x >> a
        s += a
        if 2 ** s > pow3[j + 1]:
            return j
    return cap


def shell_table(N):
    f = {0: 1}
    for j in range(N):
        g = {}
        cap = A(j + 1)
        for s, c in f.items():
            for d in range(1, cap - s + 1):
                g[s + d] = g.get(s + d, 0) + c
        f = g
    return f


# ---------------------------------------------------------------- the checks

EXPECTED_RMIN = {1: 3, 2: 7, 3: 7, 4: 27, 5: 27, 6: 27, 7: 27, 8: 27,
                 9: 27, 10: 27, 11: 27, 12: 27, 13: 27, 14: 27}

EXPECTED_WEIGHTED = {8: 367, 10: 2114, 12: 27328, 14: 168807}


def main(quick=False):
    fail = []
    nmax_shell = 14 if quick else 16
    nmax_scan = 12 if quick else 14
    pow3 = [3 ** j for j in range(nmax_shell + 2)]

    print("=" * 78)
    print("check_realizers.py  --  [V] exact realizer arithmetic, terminal shell")
    print("=" * 78)

    # ---- 1-4. per-shell exact checks ------------------------------------
    print("\n[1-4] terminal shell S = A[N]: congruence, injectivity, mod 4, orbit replay")
    print("    %3s %4s %9s %14s %14s %9s %11s %9s"
          % ("N", "S", "M_N", "min r", "max r", "distinct", "all=3 mod4", "orbit-ok"))
    shell_min = {}
    for N in range(5, nmax_shell + 1):
        ws, S = shell_words(N)
        Q = 2 ** (S + 1)
        rs = []
        for d in ws:
            r, q, S2, Q2 = least_realizer(d)
            assert S2 == S and Q2 == Q, (N, d)
            # (1) the congruence, exactly
            assert (pow(3, N, Q) * r + q) % Q == (2 ** S) % Q, (N, d, r)
            # carry recursion == carry closed form, exactly
            assert q == carry_closed_form(d), (N, d)
            # r is the LEAST such residue: it is the unique one below the modulus
            assert 0 <= r < Q, (N, d, r)
            rs.append(r)
        distinct = len(set(rs)) == len(rs)                      # (2)
        mod4 = all(r % 4 == 3 for r in rs)                      # (3)
        orbit_ok = True                                          # (4)
        for d, r in zip(ws, rs):
            wd, conf = orbit_word(r, N, pow3)
            if not (wd == d and conf and r % 2 == 1):
                orbit_ok = False
                fail.append("orbit replay N=%d word=%s r=%d" % (N, d, r))
                break
        if not distinct:
            fail.append("not injective on shell N=%d" % N)
        if not mod4:
            fail.append("some shell realizer != 3 mod 4 at N=%d" % N)
        shell_min[N] = min(rs)
        print("    %3d %4d %9d %14d %14d %9s %11s %9s"
              % (N, S, len(rs), min(rs), max(rs), distinct, mod4, orbit_ok))

    # ---- 5. true r_min by direct seed scan ------------------------------
    print("\n[5] true r_min(N,0) = least odd m that is 0-confined for N steps (direct scan)")
    limit = 2 ** (A(nmax_scan) + 1)
    print("    one scan of every odd m < 2^%d = %d" % (A(nmax_scan) + 1, limit))
    depths = bytearray((limit // 2) + 1)
    for i in range(limit // 2):
        depths[i] = capped_depth(2 * i + 1, nmax_scan, pow3)
    # smallest N whose scan window 2^(A[N]+1) can contain a given bit length
    nmin_for_bl = {}
    for bl in range(1, A(nmax_scan) + 2):
        nmin_for_bl[bl] = next(N for N in range(1, nmax_scan + 1) if A(N) + 1 >= bl)
    cnt = [0] * (nmax_scan + 1)
    rmin = [None] * (nmax_scan + 1)
    for i in range(limit // 2):
        dep = depths[i]
        if dep == 0:
            continue
        m = 2 * i + 1
        lo = nmin_for_bl.get(m.bit_length())
        if lo is None:
            continue
        for N in range(lo, dep + 1):
            cnt[N] += 1
            if rmin[N] is None:
                rmin[N] = m
    print("    %3s %16s %10s %19s %15s %12s"
          % ("N", "r_min(N,0)", "expected", "shell-min (S=A[N])", "shell/r_min", "#confined"))
    for N in range(1, nmax_scan + 1):
        exp = EXPECTED_RMIN.get(N)
        got = rmin[N]
        ok = (exp is None) or (got == exp)
        if not ok:
            fail.append("r_min N=%d computed=%s reference=%s" % (N, got, exp))
        sm = shell_min.get(N)
        ratio = "%.3f" % (sm / got) if (sm and got) else "-"
        print("    %3d %16s %10s %19s %15s %12d  %s"
              % (N, got, exp, sm, ratio, cnt[N], "ok" if ok else "MISMATCH"))
    worst = max((shell_min[N] / rmin[N] for N in shell_min if N <= nmax_scan), default=0.0)
    print("    worst shell-min / r_min overestimate on this range: %.2fx" % worst)
    print("    => the terminal-shell minimum is an UPPER BOUND on r_min, not r_min.")

    # ---- 6. mixed-shell weighting identity ------------------------------
    print("\n[6] mixed-shell weighting: sum_S |W(N,S)| * 2^(A[N]-S) == brute scan count")
    print("    (a word of terminal sum S has 2^(A[N]-S) lifts mod 2^(A[N]+1);")
    print("     one least realizer per word is NOT the uniform measure on survivors)")
    print("    %3s %14s %14s" % ("N", "weighted sum", "brute count"))
    for N in sorted(EXPECTED_WEIGHTED):
        if N > nmax_scan:
            continue
        AN = A(N)
        weighted = sum(c * 2 ** (AN - S) for S, c in shell_table(N).items())
        brute = cnt[N]
        exp = EXPECTED_WEIGHTED[N]
        ok = weighted == brute == exp
        if not ok:
            fail.append("weighting N=%d weighted=%d brute=%d reference=%d"
                        % (N, weighted, brute, exp))
        print("    %3d %14d %14d  reference=%d  %s"
              % (N, weighted, brute, exp, "ok" if ok else "MISMATCH"))

    print("\n" + "=" * 78)
    if fail:
        print("FAILED (%d):" % len(fail))
        for f in fail:
            print("  - " + f)
        return 1
    print("all exact checks passed   [V] for the finite ranges printed above")
    return 0


if __name__ == "__main__":
    sys.exit(main(quick="--quick" in sys.argv))
