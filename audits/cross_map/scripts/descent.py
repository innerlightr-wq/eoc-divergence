#!/usr/bin/env python3
"""Item 5 -- the Descent lemmas across the four maps.

For T(x) = (qx+r)/2^{v2(qx+r)} the backward step with letter a is
        p = (2^a m - r)/q ,      defined when q | 2^a m - r.

L2 analogue (the a=1 backward chain).  Seek c with  p + c = (2/q)(m + c):
        (2m - r)/q + c = (2m + 2c)/q  <=>  c(q-2) = r  <=>  c = r/(q-2),
so with the integral normalisation

        q^j * ( (q-2) * back^j(m) + r )  =  2^j * ( (q-2) m + r ) ,

and the a=1 backward chain from m has length exactly v_q( (q-2)m + r ).

    A (3,+1): v_3(m+1)      B (3,-1): v_3(m-1)
    C (5,+1): v_5(3m+1)     D (5,-1): v_5(3m-1)

L1 analogue (does the persistence-preserving backward step decrease the seed?).
Prepending a letter a to the word replaces S_k by a + S_{k-1}.  On the LOWER side
(q<4) the constraint is S_k <= A[k], and a = 1 always works, giving p = (2m-r)/q < m.
On the UPPER side (q>4) the constraint is S_k >= A[k]+1, and a letter a works iff
a >= max_k (A[k] - A[k-1]) = ceil(alpha); then p = (2^a m - r)/q > m because
2^{ceil(alpha)} > q.  So the direction reverses.
"""
from math import log2, ceil


def v(n, p):
    n = abs(n)
    k = 0
    while n and n % p == 0:
        n //= p
        k += 1
    return k


def back1(m, q, r):
    num = 2 * m - r
    return num // q if num % q == 0 else None


MAPS = [("A 3x+1", 3, 1), ("B 3x-1", 3, -1), ("C 5x+1", 5, 1), ("D 5x-1", 5, -1)]

print("=" * 88)
print("L2 analogue: the a=1 backward chain length equals v_q((q-2)m + r)")
print("=" * 88)
for name, q, r in MAPS:
    bad = 0
    tested = 0
    worst = 0
    degenerate = []
    for m in range(1, 200001, 2):
        if (q - 2) * m + r == 0:        # backward fixed point: the chain never terminates
            degenerate.append(m)
            continue
        pred = v((q - 2) * m + r, q)
        j, x = 0, m
        while True:
            nx = back1(x, q, r)
            if nx is None or nx <= 0 or nx % 2 == 0:
                break
            x = nx
            j += 1
            if j > 60:
                break
        tested += 1
        worst = max(worst, j)
        if j != pred:
            bad += 1
            if bad <= 3:
                print(f"    mismatch {name} m={m}: chain {j}, v_q((q-2)m+r) = {pred}")
    print(f"  {name}: invariant v_{q}(({q-2})m {r:+d});  odd m < 2*10^5 tested: {tested}, "
          f"mismatches {bad}, longest chain {worst}")
    print(f"      backward fixed point (q-2)m + r = 0 at m = {-r}/{q-2}"
          f"{' -- the positive integer ' + str(degenerate) if degenerate else ' -- not a positive integer'}")
print()

print("=" * 88)
print("L1 analogue: which backward letters preserve rare-side persistence, and the direction")
print("=" * 88)
for name, q, r in MAPS:
    a = log2(q)
    lower = q < 4
    A = [0]
    p = 1
    for k in range(1, 40):
        p *= q
        A.append(p.bit_length() - 1)
    inc = max(A[k] - A[k - 1] for k in range(1, 40))
    if lower:
        amin, ratio = 1, 2 / q
        rule = "a = 1 always works (prepending the smallest letter relaxes an upper bound)"
    else:
        amin, ratio = ceil(a), 2 ** ceil(a) / q
        rule = f"needs a >= max_k (A[k]-A[k-1]) = {inc} (prepending must beat a lower bound)"
    print(f"  {name}: rare side {'lower' if lower else 'upper'};  {rule}")
    print(f"      minimal admissible backward letter a = {amin}; "
          f"p/m -> 2^a/q = {ratio:.6f}  =>  the step {'DECREASES' if ratio < 1 else 'INCREASES'} the seed")
print()
print("  So the well-ordering descent of L1 exists only on the lower side (q < 4).")
print("  For q > 4 the persistence-preserving backward move increases the integer,")
print("  and it is also NOT the move carrying the q-adic chain of L2 (that one is a = 1),")
print("  so for C and D the two halves of the descent machinery decouple.")
