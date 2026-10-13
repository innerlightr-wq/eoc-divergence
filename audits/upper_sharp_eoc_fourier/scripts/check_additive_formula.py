#!/usr/bin/env python3
"""check_additive_formula.py  --  the additive realizer formula (PRIOR ART) and its
Hensel-truncation reformulation.

Status labels:
  the FORMULA itself                 [P]  PRIOR ART -- cited, not new (see below)
  the finite verification here       [V]  exact integer arithmetic, stated range only
  the constant-term simplification   [V]  exact
  the Hensel zero-run reformulation  [P]  cited (Prop. 7.1) + [V] for the bit identity
  the (1,2)/(2,1) block carries      [V]  reproduced from the carry recursion

=============================================================================
THE FORMULA IS NOT NEW.  It is prior art of this programme, in two places:

  * "The Sturmian-Mahler Edge of the Accelerated Collatz Realizer Problem"
    (De Jesus, June 2026), **Lemma 2.1** (Terras-Everett class): the odd m whose
    word begins with D form the single residue class
        { m : 3^N m + C_N(D) == 2^{S_N}  (mod 2^{S_N+1}) },
    stated there equivalently as  m == 3^{-N}( 2^{S_N} - C_N(D) )  (mod 2^{S_N+1}),
    with **Definition 2.2** r(D) = the least positive element of that class.  The
    summand-by-summand form used here is the identity
        3^{-N} C_N  =  sum_{i<N} 3^{-i-1} 2^{S_i},
    which is what drives the proof of that note's **Theorem 4.1** (where
    Xi_{alpha,beta} = -(1/3) sum_i 3^{-i} 2^{S_i} = - sum_i 3^{-i-1} 2^{S_i}).
    Local copy, in this repository:
    `audits/sturmian_irrationality/sources/B_Sturmian_Mahler_Edge.pdf`
    (source [B] of `audits/sturmian_irrationality/SOURCES.md`).

  * EOC **Revision 8**, **Proposition 5.2**, DOI 10.5281/zenodo.23146031 -- the same
    statement, to which the form used here is equivalent because
        3^{-N} 2^S  ==  2^S   (mod 2^{S+1})
    (3^{-N} is odd, so 3^{-N} = 1 + 2k and 3^{-N} 2^S = 2^S + 2^{S+1} k).
    That simplification is itself checked exactly in section [4] below.

THE ONLY NEW CONTENT of this round is the *use* of the formula: because the j-th
summand depends on the path only through the pair (j, s_j), the twisted sum
sum_D exp(2 pi i h r(D)/Q) factorizes through a forward DP on that state, and
confinement bounds s_j by A[j], so the state space has size O(N^2) rather than
O(2^{1.5N}).  That is what made depths N = 40, 50 reachable without enumerating any
word set.  The DP is implemented and validated in fourier_diagnostics.py.
=============================================================================

Derivation, for completeness (one line, from the two cited inputs): the realizer
congruence 3^N r + q_N == 2^S (mod 2^(S+1)) together with the carry closed form
q_N = sum_{j<N} 3^(N-1-j) 2^(s_j); 3 is odd so 3^N is a unit mod 2^(S+1); multiply
through by 3^(-N).  In THIS repository the carry recursion is `Divergence.C_succ`
and the precursor of the congruence is `Divergence.aggregate_identity`; the
congruence and the closed form themselves are not formalized here.

Exits non-zero on any failed assertion.  Writes nothing; prints to stdout only.

Usage:  python3 check_additive_formula.py [--quick]
"""

import sys


def A(k):
    return (3 ** k).bit_length() - 1


def shell_words(N):
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
    """Divergence.C evaluated on a prescribed word:  q_0=0, q_{j+1}=3q_j+2^{s_j}."""
    q = 0
    s = 0
    for dj in d:
        q = 3 * q + 2 ** s
        s += dj
    return q, s


def least_realizer(d):
    N = len(d)
    q, S = carry(d)
    Q = 2 ** (S + 1)
    return ((2 ** S - q) * pow(pow(3, N, Q), -1, Q)) % Q


def additive_formula(d, reduced=False):
    """r via the additive representation, in exact integer arithmetic.

    reduced=False : constant term 3^(-N) 2^S   (Sturmian-Mahler Edge Lemma 2.1 form)
    reduced=True  : constant term 2^S          (EOC Rev 8 Prop. 5.2 form)
    """
    N = len(d)
    _, S = carry(d)
    Q = 2 ** (S + 1)
    inv3 = pow(3, -1, Q)
    acc = pow(2, S, Q) if reduced else (pow(3, -N, Q) * pow(2, S, Q)) % Q
    s = 0
    for j in range(N):
        acc = (acc - pow(inv3, j + 1, Q) * pow(2, s, Q)) % Q
        s += d[j]
    return acc


def main(quick=False):
    fail = []
    print("=" * 78)
    print("check_additive_formula.py  --  additive realizer formula [P] (PRIOR ART)")
    print("=" * 78)
    print("\n  cited: Sturmian-Mahler Edge note, Lemma 2.1 + Definition 2.2 (local copy at")
    print("         audits/sturmian_irrationality/sources/B_Sturmian_Mahler_Edge.pdf);")
    print("         EOC Revision 8, Proposition 5.2, DOI 10.5281/zenodo.23146031.")
    print("  new here: only its use as an O(N^2)-state DP over the confined ensemble.")

    targets = [5, 8, 11] if quick else [5, 8, 11, 13]

    # ---- 1. the formula, every word of the terminal shell ----------------
    print("\n[1] additive formula vs least realizer, every terminal-shell word, exactly")
    print("    r(D) == 3^(-N) 2^S - sum_{j<N} 3^(-(j+1)) 2^(s_j)   (mod 2^(S+1))")
    print("    %3s %10s %12s" % ("N", "words", "mismatches"))
    for N in targets:
        ws, S = shell_words(N)
        bad = sum(1 for d in ws if additive_formula(d) != least_realizer(d))
        if bad:
            fail.append("additive formula N=%d mismatches=%d" % (N, bad))
        print("    %3d %10d %12d  %s" % (N, len(ws), bad, "ok" if bad == 0 else "MISMATCH"))
    if quick:
        print("    (--quick: N=13 skipped)")

    # ---- 2. carry recursion == carry closed form -------------------------
    print("\n[2] carry recursion (Divergence.C_succ) == closed form sum 3^(N-1-j) 2^(s_j)")
    for N in targets:
        ws, _ = shell_words(N)
        for d in ws:
            q, _ = carry(d)
            s = [0] * (N + 1)
            for j in range(N):
                s[j + 1] = s[j] + d[j]
            assert q == sum(3 ** (N - 1 - j) * 2 ** s[j] for j in range(N)), (N, d)
    print("    agreement on every terminal-shell word for N in %s" % targets)

    # ---- 3. the (1,2) / (2,1) blocks -------------------------------------
    print("\n[3] the (1,2) and (2,1) valuation blocks, from the carry recursion")
    print("    %8s %10s %8s %22s" % ("word", "total S", "carry", "prefix sums s_0,s_1,s_2"))
    seen = {}
    for d in [(1, 2), (2, 1)]:
        q, S = carry(d)
        s = (0, d[0], d[0] + d[1])
        seen[d] = (S, q)
        print("    %8s %10d %8d %22s" % (str(d), S, q, str(s)))
    ok_tot = seen[(1, 2)][0] == seen[(2, 1)][0] == 3
    ok_car = (seen[(1, 2)][1], seen[(2, 1)][1]) == (5, 7)
    if not ok_tot:
        fail.append("(1,2)/(2,1) totals not both 3: %s" % seen)
    if not ok_car:
        fail.append("(1,2)/(2,1) carries not (5,7): %s" % seen)
    print("    equal total valuation S = 3 : %s" % ok_tot)
    print("    carries 5 and 7             : %s" % ok_car)
    print("    => same total valuation, DIFFERENT carries, hence different modular")
    print("       phases.  [V] for the two carries and the equal total.  That different")
    print("       phases can FORCE cancellation when both blocks carry comparable weight")
    print("       is [D] -- reported from discussion, not re-checked here.")

    # ---- 4. the constant-term simplification -----------------------------
    print("\n[4] the two cited forms agree:  3^(-N) 2^S == 2^S  (mod 2^(S+1))")
    print("    (3^(-N) is odd, so 3^(-N) = 1+2k and 3^(-N) 2^S = 2^S + 2^(S+1) k)")
    print("    %3s %10s %36s %14s" % ("N", "words", "3^(-N)2^S == 2^S mod 2^(S+1)", "mismatches"))
    for N in targets:
        ws, S = shell_words(N)
        Q = 2 ** (S + 1)
        idok = (pow(3, -N, Q) * pow(2, S, Q)) % Q == pow(2, S, Q)
        bad = sum(1 for d in ws if additive_formula(d, reduced=True) != least_realizer(d))
        if not idok:
            fail.append("constant simplification fails at N=%d" % N)
        if bad:
            fail.append("reduced additive formula N=%d mismatches=%d" % (N, bad))
        print("    %3d %10d %36s %14d  %s"
              % (N, len(ws), idok, bad, "ok" if (idok and bad == 0) else "MISMATCH"))

    # ---- 5. the Hensel-truncation / zero-run reformulation ---------------
    print("\n[5] Hensel-truncation reformulation")
    print("    CITED [P]: Sturmian-Mahler Edge note, Proposition 7.1 (\"Realizers are")
    print("    Hensel truncations\"): r(D_N) = sum_{j<=S_N} eps_j 2^j, the integer formed")
    print("    by the first S_N+1 Hensel bits of the word's 2-adic point; it is odd")
    print("    (eps_0 = 1); and if 2^k <= r(D_N) < 2^(k+1) then eps_{k+1} = ... = eps_{S_N}")
    print("    = 0, a zero-run of length S_N - k below depth S_N + 1.  (The note states")
    print("    it for the mechanical/Sturmian point Xi_{alpha,beta}; its proof uses only")
    print("    the congruence and leastness, so the truncation statement is not special")
    print("    to that case.  Stated here as cited, for the mechanical case.)")
    print("\n    CONSEQUENCE, the restatement of the target:  r_min(N,0) <= 2^(cN) holds")
    print("    exactly when some 0-confined word of length N has r(D) with Hensel bits")
    print("    zero from position about cN up to S -- a zero-run of length about")
    print("    (alpha - c) N.  Checked here [V] as the elementary bit identity")
    print("        r < 2^k  <=>  bit_j(r) = 0 for every j in [k, S].")
    print("\n    %3s %4s %8s %6s %6s %10s %10s %26s"
          % ("N", "S", "M_N", "c", "k", "#r<2^k", "max run", "bit identity holds"))
    for N in ([14, 15] if quick else [14, 15, 16]):
        ws, S = shell_words(N)
        rs = [least_realizer(d) for d in ws]
        for c in (0.90, 0.95):
            k = int(c * N)                       # floor(cN)
            nlt = 0
            idok = True
            for r in rs:
                lt = r < 2 ** k
                bits0 = all(((r >> j) & 1) == 0 for j in range(k, S + 1))
                if lt != bits0:
                    idok = False
                if lt:
                    nlt += 1
            if not idok:
                fail.append("bit identity fails at N=%d c=%.2f" % (N, c))
            # longest zero-run below depth S+1, over the shell
            runs = [S - max(0, r.bit_length() - 1) for r in rs]
            print("    %3d %4d %8d %6.2f %6d %10d %10d %26s"
                  % (N, S, len(rs), c, k, nlt, max(runs), idok))
    print("    (max run = S - floor(log2 r) for the smallest realizer in the shell;")
    print("     needed for c is about (alpha - c) N, e.g. 0.685*16 ~ 11 at N=16, c=0.90)")

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
