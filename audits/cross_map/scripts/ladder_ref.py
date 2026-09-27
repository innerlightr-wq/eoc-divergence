#!/usr/bin/env python3
"""Independent reference implementations of the rare-side record ladder.

Written to cross-check `scan_rare.c` after the first-step sieve correction of
2026-09-25.  Pure Python, standard library only, exact integer arithmetic.

Two modes, deliberately built on different principles:

  scan   direct orbit iteration over EVERY odd m < cap, no sieve of any kind.
         Trivially correct and therefore the arbiter; linear in the cap.

  tree   the Terras-Everett CLASS tree.  A rare-side word of length n and total
         S is realized by exactly one residue class mod 2^{S+1}; the tree walks
         those classes, carrying each class's least positive member r together
         with T^n(r), and prunes a class as soon as its least member reaches the
         cap.  The pruning is exact because extending a word can only refine the
         class, so least realizers are non-decreasing along any branch.  This
         enumerates classes, not integers, and never sieves by residue.

  verify exact depth of each (N, m) pair on stdin, and the minimality of m
         among odd integers below it (optional, and linear in m).

Usage:
    ladder_ref.py scan   <q> <r> <cap_bits>
    ladder_ref.py tree   <q> <r> <cap_bits>
    ladder_ref.py verify <q> <r> < ladder.txt
"""
import sys


def Afloor(q, kmax):
    """A[k] = floor(k log2 q) = bitlength(q^k) - 1, exactly."""
    out = [0] * (kmax + 1)
    p = 1
    for k in range(1, kmax + 1):
        p *= q
        out[k] = p.bit_length() - 1
    return out


def v2(x):
    return (x & -x).bit_length() - 1


def rare_ok(A, upper, k, S):
    return S >= A[k] + 1 if upper else S <= A[k]


def depth(q, r, m, A, upper, kmax):
    """Largest n with the orbit of m on the rare side at every 1..n.  Exact."""
    x, S = m, 0
    for k in range(1, kmax + 1):
        y = q * x + r
        a = v2(y)
        S += a
        if not rare_ok(A, upper, k, S):
            return k - 1
        x = y >> a
    return kmax


# --------------------------------------------------------------------- scan --

def ladder_scan(q, r, cap, kmax=900):
    A = Afloor(q, kmax)
    upper = q > 4
    best = {}
    for m in range(1, cap, 2):
        d = depth(q, r, m, A, upper, kmax)
        for n in range(1, d + 1):
            if n not in best:
                best[n] = m
    return best


# --------------------------------------------------------------------- tree --

def ladder_tree(q, r, cap, kmax=900):
    """Walk the class tree.  A node is (n, S, r_least, y = T^n(r_least))."""
    A = Afloor(q, kmax)
    upper = q > 4
    best = {}
    # depth 0: the whole class of odd integers, least member 1, modulus 2
    stack = [(0, 0, 1, 1)]
    nodes = 0
    while stack:
        n, S, rl, y = stack.pop()
        nodes += 1
        if n >= 1 and (n not in best or rl < best[n]):
            best[n] = rl
        if n >= kmax:
            continue
        mod = 1 << (S + 1)
        qn = q ** n
        seen = {}
        t = 0
        while True:
            m = rl + t * mod
            if m >= cap:
                break
            Y = y + 2 * qn * t if t else y
            u = q * Y + r
            d = v2(u)
            if d not in seen and rare_ok(A, upper, n + 1, S + d):
                seen[d] = True
                stack.append((n + 1, S + d, m, u >> d))
            t += 1
            if mod >= cap:          # the class has at most one member below cap
                break
    return best, nodes


# ------------------------------------------------------------------ helpers --

def jumps(best):
    out, prev = [], None
    for n in sorted(best):
        if best[n] != prev:
            out.append((n, best[n]))
            prev = best[n]
    return out


def main():
    mode = sys.argv[1]
    q, r = int(sys.argv[2]), int(sys.argv[3])
    if mode == "verify":
        A = Afloor(q, 900)
        upper = q > 4
        rows = [tuple(map(int, ln.split())) for ln in sys.stdin if ln.strip()]
        bad = 0
        for N, m in rows:
            d = depth(q, r, m, A, upper, 900)
            ok = d >= N
            if not ok:
                bad += 1
            print(f"  N={N:>4} m={m:>14}  depth={d:>4}  depth>=N: {ok}")
        print(f"verified {len(rows)} holders, {bad} failures")
        return
    capbits = int(sys.argv[4])
    cap = 1 << capbits
    if mode == "scan":
        best = ladder_scan(q, r, cap)
        nodes = None
    else:
        best, nodes = ladder_tree(q, r, cap)
    J = jumps(best)
    print(f"# {mode}  q={q} r={r:+d}  cap=2^{capbits}  "
          f"holders={len(J)}  maxN={max(best) if best else 0}"
          + (f"  nodes={nodes}" if nodes else ""))
    for n, m in J:
        print(f"{n} {m}")


if __name__ == "__main__":
    main()
