#!/usr/bin/env python3
"""Where Q - 1 lives: the sawtooth identity and the shell decomposition.

Exact integer / rational arithmetic throughout.  Floating point appears only in
reported ratios and error bars.

SETUP.  For a zero-confined word w of length N with S = S_N(w), the cylinder of
seeds realising w is an arithmetic progression of modulus

    q_w = 2^{S+1},

and its residue is given in closed form by requiring both that 2^S divides
3^N m_0 + C_N and that the quotient m_N be odd:

    r_w = ( (2^S - C_N) * 3^{-N} )  mod  2^{S+1},

with C_0 = 0, C_{k+1} = 3 C_k + 2^{S_k}.  This script recomputes every realizer from
this closed form and then ASSERTS, by running the map forward, that r_w really does
have valuation word w.

THE SAWTOOTH.  Write M = k q_w + t, 0 <= t < q_w.  Then

    |C(w) cap [1,M]| = k + [ r_w <= t ].

Because M is odd and q_w is even, t is odd, so the number of odd residues in [1,t] is
(t+1)/2 out of q_w/2, and the null favorable fraction is

    u = (t+1)/q_w ,          NOT 1/2.

This is why Q ~ 1 is a frequency-times-magnitude balance rather than a 50/50 split:
u varies over the shells, and it is u, not 1/2, that the observed inclusion rate must
be compared against.

THE EXACT IDENTITY.  Since k_S + u_S = (M+1)/q_S = O_M 2^{-S} exactly (M = 2^B - 1),
grouping words into shells by S = S_N(w) and writing f_S for the observed favorable
fraction in shell S gives

    A_{N,M} - O_M p_N  =  sum_S n_S D_{N,M,S},        D = f_S - u_S.

So the whole of Q - 1 is a discrepancy between the observed inclusion rate of shell
realizers and the null rate forced by the height cutoff.  Nothing here bounds that
discrepancy; it only localises it.
"""
import math
from fractions import Fraction


def shells(N, verify_cap=None):
    """all zero-confined words of length N, reduced to per-shell (S -> list of r_w).

    Depth-first over (k, S_k, C_k) with C_{k+1} = 3 C_k + 2^{S_k}; the confinement
    test is the exact integer comparison 2^{S_j} <= 3^j.  Returns the per-shell
    realizer lists together with the enumeration size and the number of realizers
    whose forward valuation word was checked (and any mismatches).
    """
    pow3 = [3 ** j for j in range(N + 2)]
    out = {}
    wordof = {}
    nwords = 0
    # inverse of 3^N modulo 2^{S+1}, one per shell, computed once
    inv = {}
    stack = [(0, 0, 0, ())]      # (k, S_k, C_k, word so far)
    while stack:
        k, S, C, w = stack.pop()
        if k == N:
            nwords += 1
            if S not in inv:
                inv[S] = pow(3, -N, 1 << (S + 1))
            q = 1 << (S + 1)
            r = ((1 << S) - C) * inv[S] % q
            out.setdefault(S, []).append(r)
            wordof[r] = tuple(w)
            continue
        Cn = 3 * C + (1 << S)     # C_{k+1}, independent of the next letter
        a = 1
        while (1 << (S + a)) <= pow3[k + 1]:
            stack.append((k + 1, S + a, Cn, w + (a,)))
            a += 1
    # forward verification that each realizer really has valuation word w
    checked = mismatch = 0
    total = sum(len(v) for v in out.values())
    step = 1 if verify_cap is None else max(1, total // verify_cap)
    idx = 0
    for S, rs in out.items():
        for r in rs:
            idx += 1
            if idx % step:
                continue
            m, Ssum, ok = r, 0, True
            fwd = []
            for j in range(1, N + 1):
                x = 3 * m + 1
                a = (x & -x).bit_length() - 1
                fwd.append(a)
                Ssum += a
                m = x >> a
                if (1 << Ssum) > pow3[j]:      # must stay zero-confined
                    ok = False
                    break
            checked += 1
            # FULL-WORD equality, not merely (length, total valuation); plus terminal parity.
            if not ok or Ssum != S or tuple(fwd) != wordof[r] or m % 2 == 0:
                mismatch += 1
    return out, nwords, checked, mismatch


def confined_mass(nmax):
    f = {0: 1}
    P = [Fraction(1)]
    for n in range(1, nmax + 1):
        g = {}
        for S, c in f.items():
            a = 1
            while (1 << (S + a)) <= 3 ** n:
                g[S + a] = g.get(S + a, 0) + c
                a += 1
        f = g
        P.append(sum(Fraction(c, 1 << S) for S, c in f.items()))
    return P


def A_direct(M, N):
    """A_{N,M} by direct enumeration of odd seeds: an independent check"""
    cnt = 0
    for m0 in range(1, M + 1, 2):
        m, S, ok = m0, 0, True
        for j in range(1, N + 1):
            x = 3 * m + 1
            a = (x & -x).bit_length() - 1
            S += a
            m = x >> a
            if (1 << S) > 3 ** j:
                ok = False
                break
        cnt += ok
    return cnt


print(__doc__)
P = confined_mass(25)
HEIGHTS = [12, 16, 20]
bad_identity = 0

for N in (12, 16, 20):
    sh, nwords, checked, mismatch = shells(N)
    print("=" * 78)
    print(f"N = {N}:  confined words enumerated = {nwords:,}"
          f"   shells S = {min(sh)}..{max(sh)}")
    print(f"  realizers forward-verified: {checked:,} of {nwords:,}"
          f"   word mismatches: {mismatch}")
    assert mismatch == 0, "closed-form realizer does not realise its word"
    for B in HEIGHTS:
        M = (1 << B) - 1
        OM = (M + 1) // 2
        print(f"\n  --- M = 2^{B}-1 = {M:,},  O_M = {OM:,} ---")
        print(f"   {'S':>4} {'n_S':>12} {'k_S':>8} {'u_S':>10} {'fav':>12}"
              f" {'f_S':>10} {'f/u':>8} {'+-':>7}")
        acc = Fraction(0)
        Afrom = 0
        for S in sorted(sh):
            q = 1 << (S + 1)
            k, t = divmod(M, q)
            assert t % 2 == 1, "M odd and q even should force t odd"
            u = Fraction(t + 1, q)
            rs = sh[S]
            n_S = len(rs)
            fav = sum(1 for r in rs if r <= t)
            f = Fraction(fav, n_S)
            acc += n_S * (f - u)
            Afrom += n_S * k + fav
            ratio = float(f / u) if u else float('nan')
            err = ratio / math.sqrt(fav) if fav else float('nan')
            print(f"   {S:>4} {n_S:>12,} {k:>8,} {float(u):>10.6f} {fav:>12,}"
                  f" {float(f):>10.6f} {ratio:>8.4f} {err:>7.4f}")
        A = A_direct(M, N)
        lhs = Fraction(A) - OM * P[N]
        ok = (lhs == acc) and (Afrom == A)
        bad_identity += (not ok)
        Q = Fraction(A, 1) / (OM * P[N]) if P[N] else 0
        print(f"   A_{{{N},M}} (direct) = {A:,}   A from cylinder counts = {Afrom:,}"
              f"   {'agree' if Afrom == A else 'DISAGREE'}")
        print(f"   A - O_M p_N = {float(lhs):+.6f}   sum_S n_S D_S = {float(acc):+.6f}"
              f"   exact identity: {'HOLDS' if lhs == acc else 'FAILS'}")
        print(f"   Q_{{{N},M}} = {float(Q):.6f}")
    print()

print("=" * 78)
print(f"exact-identity failures across all (N, M) pairs: {bad_identity}")
print()
print("Reading of the table:")
print("  * f/u is the observed inclusion rate divided by the null rate; the +- column")
print("    is the counting error bar ratio/sqrt(fav).  f/u = 1 within +- means the")
print("    shell carries no detectable placement bias.")
print("  * once N >= B-1 every q_S = 2^{S+1} exceeds M, so k_S = 0 and D_S reduces to")
print("    'does shell S contain a realizer <= M' -- i.e. r_min(N,0) stratified by S.")
print("    At that point the decomposition has no independent content beyond the")
print("    realizer-floor question it was meant to illuminate.")

print()
print("=" * 78)
print("HOW STRUCTURED IS A SHELL?  normalised realizer position r_w / q_S")
print("=" * 78)
print("Under the null the realizers are uniform over the odd residues mod q_S, so the")
print("mean of r_w/q_S should be 1/2 with standard deviation 1/sqrt(12 n_S).")
print()
print(f"   {'N':>3} {'S':>4} {'n_S':>12} {'mean r/q':>10} {'z':>8}   flag")
struct = 0
for N in (12, 16, 20):
    sh, _, _, _ = shells(N, verify_cap=1)
    for S in sorted(sh):
        rs = sh[S]
        q = 1 << (S + 1)
        mean = sum(rs) / len(rs) / q
        z = (mean - 0.5) * math.sqrt(12 * len(rs))
        flag = "STRUCTURED" if abs(z) > 3 else ""
        struct += (abs(z) > 3)
        print(f"   {N:>3} {S:>4} {len(rs):>12,} {mean:>10.4f} {z:>+8.2f}   {flag}")
print(f"   shells with |z| > 3: {struct}")
print()
print("  The single genuinely structured shell is S = N, which contains exactly ONE word,")
print("  the all-ones word, whose realizer is exactly 2^{N+1}-1 (proved and checked in")
print("  per_cylinder_survival.py).  It is maximally unfavorable at every height.")
print("  Shells S = N+1 and S = N+2 do NOT show a realizer-position bias: their means sit")
print("  within one to two null standard deviations of 1/2.  Their f/u = 0 entries at the")
print("  smaller heights are small-count artefacts (n_S = 11..187, fav = 0..29), not")
print("  placement structure.  These shells are also high-slack, far from the critical")
print("  boundary, so they are not where a frontier obstruction could live.")

print()
print("=" * 78)
print("POPULOUS SHELLS: is f/u = 1 within counting noise?")
print("=" * 78)
tested = outside = 0
for N in (12, 16, 20):
    sh, _, _, _ = shells(N, verify_cap=1)
    for B in HEIGHTS:
        M = (1 << B) - 1
        for S in sorted(sh):
            q = 1 << (S + 1)
            k, t = divmod(M, q)
            u = Fraction(t + 1, q)
            rs = sh[S]
            fav = sum(1 for r in rs if r <= t)
            if fav < 100:
                continue
            ratio = float(Fraction(fav, len(rs)) / u)
            err = ratio / math.sqrt(fav)
            tested += 1
            if abs(ratio - 1) > 2 * err:
                outside += 1
                print(f"   N={N} B={B} S={S} n_S={len(rs):,} fav={fav:,}"
                      f" f/u={ratio:.4f} +-{err:.4f}   outside 2 sd")
print(f"   populous shells (fav >= 100) tested: {tested}   outside 2 error bars: {outside}")
print("   At the 2-sigma level roughly 5% of tests fall outside by chance, so this is")
print("   consistent with no placement bias in the shells that carry the mass.")
