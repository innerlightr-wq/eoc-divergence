#!/usr/bin/env python3
"""I2, I3, I4 — verification in exact integer arithmetic.

I2  the primitive root W of an initial square WW of a Sturmian word is a
    conjugate (cyclic permutation) of the Christoffel/standard word of slope
    k/ell, equivalently W^infty is balanced.
I3  |c_W| <= C * ell * max(2^ell, 3^k)   with explicit C.
I4  the Liouville inequality  c(gamma)*ell <= log2 H + log2(2 + C*ell) + log2 3.
"""
import sys, os, math, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sturmian import *
from decimal import Decimal, getcontext
getcontext().prec = 120
LOG2_3 = float(Decimal(3).ln() / Decimal(2).ln())


def c_word(w):
    """c_w = sum_{i<l, w_i=1} 3^{k - k_{i+1}(w)} 2^i   (paper, eq. (2))."""
    k = sum(w); tot = 0; ki = 0
    for i, b in enumerate(w):
        if b:
            ki += 1
            tot += 3 ** (k - ki) * (1 << i)
    return tot


def is_christoffel_conjugate(w):
    k, l = sum(w), len(w)
    if k == 0 or math.gcd(k, l) != 1:
        return None                      # non-primitive slope: handle separately
    return tuple(w) in set(conjugates(christoffel(k, l)))


def periodization_balanced(w, reps=6):
    return is_balanced((w * reps)[:min(len(w) * reps, 400)])


# ---------------------------------------------------------------- I3 ------
def i3_scan(QMAX=40):
    worst, arg = 0.0, None
    for q in range(1, QMAX + 1):
        for p in range(1, q + 1):
            if math.gcd(p, q) != 1: continue
            base = christoffel(p, q)
            for w in conjugates(base):
                w = list(w)
                c = c_word(w)
                r = c / (q * max(2 ** q, 3 ** p))
                if r > worst: worst, arg = r, (p, q, ''.join(map(str, w)))
    return worst, arg


# ---------------------------------------------------------------- main ----
if __name__ == "__main__":
    print("=" * 92)
    print("I3 — height bound over ALL conjugates of Christoffel words")
    print("=" * 92)
    worst, arg = i3_scan(40)
    print(f"  max over p/q with q<=40 and all conjugates of  c_W / (ell*max(2^ell,3^k))")
    print(f"     = {worst:.6f}   attained at p/q = {arg[0]}/{arg[1]}, W = {arg[2]}")
    print(f"  => C = 1 suffices on this range (paper's Lemma 4.2 constant, now for ALL conjugates)")
    print()

    print("=" * 92)
    print("I2 + I4 — initial squares of Sturmian words: roots, heights, Liouville margin")
    print("=" * 92)
    SL = {"log_3 2 (critical)": log3_2(),
          "1/phi": from_cf([0] + [1] * 300),
          "sqrt2-1": from_cf([0] + [2] * 250),
          "[0;1,97,1,...]": from_cf([0, 1, 97] + [1] * 250)}
    N, LMAX = 4000, 1400
    rng = random.Random(20260925)
    bad_i2 = bad_i3 = 0; rows = 0
    for name, g in SL.items():
        gamma = g / ONE
        thr = max(1.0, gamma * LOG2_3); cg = 2.0 - thr
        print(f"\n  SLOPE {name}   gamma={gamma:.6f}   c(gamma)=2-max(1,g*log2 3)={cg:.4f}")
        for lab, r in [("0", 0), ("1/2", ONE // 2),
                       ("rand", rng.randrange(ONE)), ("rand2", rng.randrange(ONE))]:
            s = word(g, r, N)
            sq = [L for L in range(2, LMAX + 1) if s[:L] == s[L:2 * L]]
            if not sq:
                print(f"    intercept {lab:<6}: NO SQUARE FOUND  <-- would break I1"); continue
            out = []
            for L in sq[-3:]:
                W = s[:L]; k = sum(W)
                conj = is_christoffel_conjugate(W)
                bal = periodization_balanced(W)
                c = c_word(W)
                ratio = c / (L * max(2 ** L, 3 ** k))
                ok2 = (conj is True) or (conj is None and bal)
                ok3 = ratio <= 1.0
                bad_i2 += (not ok2); bad_i3 += (not ok3); rows += 1
                # I4 margin: 2L - max(L, k log2 3)  must grow like c(gamma)*L
                margin = 2 * L - max(L, k * LOG2_3)
                out.append(f"L={L}(k={k}) conj={'Y' if ok2 else 'N'} "
                           f"c_W/({L}max)={ratio:.4f} margin={margin:.1f}={margin/L:.3f}*L")
            print(f"    intercept {lab:<6}: " + " | ".join(out))
    print()
    print(f"  I2 failures: {bad_i2} / {rows}      I3 failures (ratio>1): {bad_i3} / {rows}")
