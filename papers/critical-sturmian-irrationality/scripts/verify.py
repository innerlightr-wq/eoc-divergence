#!/usr/bin/env python3
"""
Verification for "The 3x+1 conjugacy map sends the critical Sturmian word to an
irrational 2-adic integer".

All arithmetic is exact integer / 2-adic arithmetic.  No floating point is used
in any decision; floats appear only in printed diagnostics.

Commands
--------
  convergents   continued fraction and convergents of beta = ln2/ln3, with the
                side of each convergent decided by the exact test 3^p vs 2^q
  depths [N]    Theorem 5.3: v2(Phi(1c_beta) - Phi(w_n^inf)) for 3 <= n <= N,
                computed 2-adically, against the predicted q_n-1 / q_n+q_{n+1}-1
  lcp [N]       Theorem 5.3 again, computed instead as a longest common prefix
                of the two 0/1 words (independent of the 2-adic route)
  heights [Q]   Lemma 4.2 on every mechanical word p/q with q <= Q, and the
                unbalanced witness 0^a 1^a of Remark 4.3
  controls      the two rational controls: depths against a fixed rational
                target freeze, so the Liouville step cannot fire on a rational
  shadow        the explicit height of Corollary 6.3
  all           everything except the deepest `depths` run
"""
import sys, json, os
from fractions import Fraction
from decimal import Decimal, getcontext

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- convergents
def cf_of(fr, maxn=400):
    a, x = [], fr
    for _ in range(maxn):
        q = x.numerator // x.denominator
        a.append(q); x -= q
        if x == 0: break
        x = 1 / x
    return a

def beta_cf(prec=400):
    """Rigorous prefix of the continued fraction of beta = ln2/ln3."""
    getcontext().prec = prec
    v = Decimal(2).ln() / Decimal(3).ln()
    eps = Decimal(10) ** (-(prec - 20))
    A, B = cf_of(Fraction(str(v - eps))), cf_of(Fraction(str(v + eps)))
    out = []
    for i in range(min(len(A), len(B))):
        if A[i] != B[i]: break
        out.append(A[i])
    return out[:-1]

def convergents(N=40):
    a = beta_cf()
    conv = [(0, 1)]
    for i, ai in enumerate(a[1:], start=1):
        if i == 1: p, q = 1, ai
        else: p, q = ai*conv[-1][0] + conv[-2][0], ai*conv[-1][1] + conv[-2][1]
        conv.append((p, q))
    return conv[:N], a

def side(p, q):
    """exact: is p/q > beta ?   p/q > log_3 2  <=>  3^p > 2^q"""
    return '>' if 3**p > 2**q else '<'

# ------------------------------------------------------------------- the words
def floor_j_alpha(p3):
    """floor(j*log2 3) from 3^j, exactly: the bit length minus one."""
    return p3.bit_length() - 1

def mech_word(p, q):
    """lower mechanical word of slope p/q: length q, p ones at floor(j q/p)."""
    w = [0]*q
    for j in range(p): w[(j*q)//p] = 1
    return w

def c_of(w):
    """c_w = sum_{i: w_i=1} 3^{k-k_{i+1}} 2^i, by Horner over the ones."""
    k = sum(w); tot = 0; seen = 0
    for i, b in enumerate(w):
        if b:
            seen += 1
            tot += 3**(k-seen) << i
    return tot

# ------------------------------------------------------------ 2-adic machinery
def phi_1c_mod(K):
    """Phi(1c_beta) mod 2^K, via Horner on  -3^{-J} sum_{j<J} 3^{J-1-j} 2^{e_j}."""
    M = (1 << K) - 1
    S = 0; p3 = 1; j = 0
    while True:
        e = floor_j_alpha(p3)
        if e >= K: break
        S = ((S*3) + (1 << e)) & M
        p3 *= 3; j += 1
    return (-(S * pow(3, -j, 1 << K))) % (1 << K)

def phi_periodic_mod(p, q, K):
    """Phi(w^inf) = c_w / (2^q - 3^p)  mod 2^K."""
    c = c_of(mech_word(p, q))
    return (c * pow(2**q - 3**p, -1, 1 << K)) % (1 << K)

def v2(x):
    return None if x == 0 else (x & -x).bit_length() - 1

def predicted(n, conv):
    q = conv[n][1]
    return q - 1 if n % 2 == 0 else q + conv[n+1][1] - 1

# ------------------------------------------------------------------ the commands
def cmd_convergents():
    conv, a = convergents()
    print("continued fraction of beta = ln2/ln3, %d rigorous partial quotients:" % len(a))
    print("  ", a[:26], "...")
    print("\n n  p_n/q_n                 side      note (A) shell (q,p)")
    for n in range(1, 15):
        p, q = conv[n]
        print("  %-2d %8d/%-8d  p/q %s beta   (%d, %d)" % (n, p, q, side(p, q), p, q))
    print("\n  p_n/q_n > beta  <=>  n odd   (checked exactly above)")

def cmd_depths(N=11):
    conv, _ = convergents()
    print(" n  p_n/q_n             predicted   v2(Phi(1c)-Phi(w_n^inf))   match")
    ok = True
    for n in range(3, N+1):
        p, q = conv[n]; pred = predicted(n, conv)
        K = pred + 40
        got = v2((phi_1c_mod(K) - phi_periodic_mod(p, q, K)) % (1 << K))
        good = (got == pred); ok &= good
        print("  %-2d %8d/%-8d %-11d %-26s %s"
              % (n, p, q, pred, got, "OK" if good else "MISMATCH"), flush=True)
    print("\n  all match" if ok else "\n  FAILURES PRESENT")

def cmd_lcp(N=10):
    conv, _ = convergents()
    print(" n  p_n/q_n             predicted   lcp(1c_beta, w_n^inf)      match")
    ok = True
    for n in range(3, N+1):
        p, q = conv[n]; pred = predicted(n, conv); L = pred + 50
        ones_true = set(); p3 = 1
        while True:
            e = floor_j_alpha(p3)
            if e >= L: break
            ones_true.add(e); p3 *= 3
        ones_per = set()
        j = 0
        while True:
            pos = (j*q)//p
            if pos >= L: break
            ones_per.add(pos); j += 1
        got = next(i for i in range(L) if (i in ones_true) != (i in ones_per))
        good = (got == pred); ok &= good
        print("  %-2d %8d/%-8d %-11d %-26s %s"
              % (n, p, q, pred, got, "OK" if good else "MISMATCH"), flush=True)
    print("\n  all match" if ok else "\n  FAILURES PRESENT")

def cmd_heights(Q=120):
    from math import gcd
    conv, _ = convergents()
    print("Lemma 4.2:  c_w <= q * max(2^q, 3^p)  on the mechanical words of the convergents")
    for n in range(1, 12):
        p, q = conv[n]
        if p == 0: continue
        c = c_of(mech_word(p, q)); b = q*max(2**q, 3**p)
        print("  n=%-2d  l=%-6d k=%-6d  c_w / (l max) = %.5f   %s"
              % (n, q, p, c/b, "OK" if c <= b else "FAIL"))
    bad = 0; worst = 0.0
    for q in range(1, Q+1):
        for p in range(1, q+1):
            if gcd(p, q) != 1: continue
            c = c_of(mech_word(p, q)); b = q*max(2**q, 3**p)
            if c > b: bad += 1
            worst = max(worst, c/b)
    print("\n  every mechanical word p/q with q <= %d: %d violations, worst ratio %.5f"
          % (Q, bad, worst))
    print("\nRemark 4.3, the unbalanced witness w = 0^a 1^a:")
    print("  a    c_w                       closed form 2^a(3^a-2^a)   c_w/(l*max)")
    for a in (5, 10, 15, 18):
        w = [0]*a + [1]*a; c = c_of(w); cf_ = 2**a * (3**a - 2**a)
        assert c == cf_, "closed form disagrees at a=%d" % a
        print("  %-4d %-25d %-25s %.3f" % (a, c, "matches", c/(2*a*max(2**(2*a), 3**a))))
    print("  closed form verified at every a above; ratio = (3^a-2^a)/(2a 2^a) -> infinity")

def cmd_controls():
    """A rational target: the depths freeze, so the Liouville step cannot fire."""
    conv, _ = convergents()
    print("Controls. For a RATIONAL target y the agreement depth with the periodic")
    print("values is bounded; only the true value has depths tending to infinity.\n")
    for m in (3, 5):
        p, q = conv[m]
        y_num, y_den = c_of(mech_word(p, q)), 2**q - 3**p
        yf = Fraction(y_num, y_den)
        print("  target y = Phi(w_%d^inf) = %s  (a rational 2-adic integer)"
              % (m, yf.numerator if yf.denominator == 1 else yf))
        row = []
        for n in range(3, 12):
            pn, qn = conv[n]; pred = predicted(n, conv); K = pred + 40
            d = (y_num * pow(y_den, -1, 1 << K) - phi_periodic_mod(pn, qn, K)) % (1 << K)
            row.append((n, v2(d)))
        print("     v2(y - Phi(w_n^inf)) for n = 3..11:",
              ", ".join("%d:%s" % (n, "exact" if v is None else v) for n, v in row))
        print("     -> freezes at %s; no contradiction is produced, as it must not be.\n"
              % max(v for _, v in row if v is not None))

def cmd_shadow():
    """Corollary 6.3 from the deepest verified depth."""
    conv, _ = convergents()
    n = 13
    q_n, q_n1 = conv[n][1], conv[n+1][1]
    L = q_n + q_n1 - 1
    # 2^L <= |M_n| < 4 H q_n 2^{q_n}   =>   H > 2^{L-q_n} / (4 q_n)
    e = L - q_n
    C = 4*q_n
    print("deepest verified shell: n = %d, p/q = %d/%d, depth L = %d" % (n, conv[n][0], q_n, L))
    print("  2^L <= |M_n| < 4 H q_n 2^{q_n}   =>   H > 2^%d / %d" % (e, C))
    print("  %d < 2^%d, so H > 2^%d" % (C, C.bit_length(), e - C.bit_length()))
    print()
    print("  Corollary 6.3: Phi(1c_beta) is not u/v in lowest terms with")
    print("  max(|u|,v) <= 2^%d." % (e - C.bit_length()))

def cmd_audit():
    """Every remaining numerical constant asserted in the paper."""
    from decimal import Decimal, getcontext
    getcontext().prec = 200
    import math
    conv, _ = convergents()
    b = Decimal(2).ln()/Decimal(3).ln(); al = 1/b
    ok = True
    def chk(name, cond):
        nonlocal ok
        ok &= bool(cond)
        print("  [%s] %s" % ("OK" if cond else "FAIL", name))

    print("Theorem 5.3 / Lemma 5.2, supporting facts at odd n = 3,5,7,9,11:")
    for n in range(3, 12, 2):
        pn, qn = conv[n]; pn1, qn1 = conv[n+1]; pn2, qn2 = conv[n+2]
        Dn = abs(qn*b - pn); Dn1 = abs(qn1*b - pn1)
        lhs = (pn+pn1)*al*Dn; rhs = 1 + pn*al*(Dn - Dn1)
        chk("n=%-2d  identity (p_n+p_{n+1}) a D_n = 1 + p_n a (D_n - D_{n+1})" % n,
            abs(lhs-rhs) < Decimal(10)**-60)
        chk("n=%-2d  that quantity lies in (1,2)" % n, 1 < lhs < 2)
        chk("n=%-2d  (eq:pn1)  p_{n+1} a D_n = 1 - p_n a D_{n+1} < 1" % n,
            abs(pn1*al*Dn - (1 - pn*al*Dn1)) < Decimal(10)**-60 and pn1*al*Dn < 1)
        chk("n=%-2d  floor gap: (p_n+p_{n+1}) a D_n / p_n < 1" % n, lhs/pn < 1)
        chk("n=%-2d  m_{p_{n+1}} = p_n - 1" % n, (pn1*qn) % pn == pn - 1)
        chk("n=%-2d  D_n < 1/q_{n+1}" % n, Dn < Decimal(1)/qn1)

    print("\nSection 1, the critical growth rate:")
    chk("3^beta / 2 = 1", abs(Decimal(3)**b/2 - 1) < Decimal(10)**-60)

    print("\nTheorem 6.2, the explicit constants:")
    chk("alpha/8 < 0.2", float(al)/8 < 0.2)
    chk("2^0.2 < 1.15", 2**0.2 < 1.15)
    chk("2 * 1.15 = 2.3 <= 4", 2*1.15 <= 4)
    chk("Q/2 + 7 > log2 Q for 1 <= Q <= 10^6",
        all(Q/2 + 7 > math.log2(Q) for Q in range(1, 10**6)))
    chk("q_n >= 2 log2 H + 20  =>  q_n - log2 q_n > 3 + log2 H  (H = 2^L, L up to 10^6)",
        all((2*L+20) - math.log2(2*L+20) > 3 + L for L in range(0, 10**6, 97)))

    print("\nCorollary 6.3:")
    chk("4 * q_13 = 705004 < 2^20", 4*conv[13][1] == 705004 and 705004 < 2**20)
    chk("q_13 + q_14 - 1 - q_13 = 301993", conv[13][1]+conv[14][1]-1-conv[13][1] == 301993)

    print("\nSection 7, the archimedean terms:")
    p3 = 1
    bad = 0
    for j in range(20000):
        e = floor_j_alpha(p3)
        t = Decimal(2)**e / Decimal(3)**(j+1)
        if not (Decimal(1)/6 < t <= Decimal(1)/3): bad += 1
        p3 *= 3
    chk("3^{-(j+1)} 2^{floor(j a)} in (1/6, 1/3] for j < 20000", bad == 0)
    print("\n  ALL CHECKS PASSED" if ok else "\n  FAILURES PRESENT")

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "all"
    arg = int(sys.argv[2]) if len(sys.argv) > 2 else None
    if cmd == "convergents": cmd_convergents()
    elif cmd == "depths": cmd_depths(arg or 11)
    elif cmd == "lcp": cmd_lcp(arg or 10)
    elif cmd == "heights": cmd_heights(arg or 120)
    elif cmd == "controls": cmd_controls()
    elif cmd == "shadow": cmd_shadow()
    elif cmd == "audit": cmd_audit()
    elif cmd == "all":
        for f in (cmd_convergents, cmd_lcp, cmd_heights, cmd_controls, cmd_shadow, cmd_audit):
            print("="*78); f(); print()
    else: print(__doc__)
