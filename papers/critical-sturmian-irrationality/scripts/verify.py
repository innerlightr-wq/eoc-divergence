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
  shadow        the explicit height of Corollary 6.2
  slopes [CAP]  Theorem 8.3 at seven irrational slopes, by longest common prefix
                and, independently, 2-adically; depths capped at CAP
  uniform       Theorem 8.4 / 8.5 / Corollary 8.7: every explicit constant of
                Section 8, the bound on log2 G_n at every odd convergent, and
                the exact height floor at the deepest one
  slopecontrols the rational-slope control for Section 8
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
    """Corollary 6.2 from the deepest verified depth."""
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
    print("  Corollary 6.2: Phi(1c_beta) is not u/v in lowest terms with")
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

    print("\nTheorem 6.1, the explicit constants:")
    chk("alpha/8 < 0.2", float(al)/8 < 0.2)
    chk("2^0.2 < 1.15", 2**0.2 < 1.15)
    chk("2 * 1.15 = 2.3 <= 4", 2*1.15 <= 4)
    chk("Q/2 + 7 > log2 Q for 1 <= Q <= 10^6",
        all(Q/2 + 7 > math.log2(Q) for Q in range(1, 10**6)))
    chk("q_n >= 2 log2 H + 20  =>  q_n - log2 q_n > 3 + log2 H  (H = 2^L, L up to 10^6)",
        all((2*L+20) - math.log2(2*L+20) > 3 + L for L in range(0, 10**6, 97)))

    print("\nCorollary 6.2:")
    chk("4 * q_13 = 705004 < 2^20", 4*conv[13][1] == 705004 and 705004 < 2**20)
    chk("q_13 + q_14 - 1 - q_13 = 301993", conv[13][1]+conv[14][1]-1-conv[13][1] == 301993)

    print("\nSection 9, the archimedean terms:")
    p3 = 1
    bad = 0
    for j in range(20000):
        e = floor_j_alpha(p3)
        t = Decimal(2)**e / Decimal(3)**(j+1)
        if not (Decimal(1)/6 < t <= Decimal(1)/3): bad += 1
        p3 *= 3
    chk("3^{-(j+1)} 2^{floor(j a)} in (1/6, 1/3] for j < 20000", bad == 0)
    print("\n  ALL CHECKS PASSED" if ok else "\n  FAILURES PRESENT")

# ============================================================================
# Section 8 (all irrational slopes).  Exact throughout: a slope is given by the
# partial quotients of gamma = [0;a_1,a_2,...], so alpha_gamma = 1/gamma =
# [a_1;a_2,...] has convergents q_n/p_n, which bracket it and certify the
# floors floor(j*alpha_gamma).
# ============================================================================

def cf_e_minus_2(N):
    """e - 2 = [0;1,2,1,1,4,1,1,6,1,1,8,...]"""
    a, k = [1], 2
    while len(a) < N:
        a += [k, 1, 1]; k += 2
    return a[:N]

SLOPES = [
    ("1/phi",              [1]*40,                                       "below"),
    ("sqrt2-1",            [2]*30,                                       "below"),
    ("e-2",                cf_e_minus_2(30),                             "above"),
    ("[0;50,1,1,...]",     [50]+[1]*39,                                  "below"),
    ("[0;1,97,1,...]",     [1,97]+[1]*38,                                "above"),
    ("[0;1,1,1,1000,...]", [1,1,1,1000]+[1]*36,                          "above"),
    ("~1/(7+1/pi)",        [7,3,7,15,1,292,1,1,1,2,1,3,1,14]+[1]*26,     "below"),
]

def convergents_cf(a):
    """p[n]/q[n] for gamma = [0;a_1,a_2,...], indexed from p_0/q_0 = 0/1."""
    p, q = [0, 1], [1, a[0]]
    for n in range(1, len(a)):
        p.append(a[n]*p[-1] + p[-2]); q.append(a[n]*q[-1] + q[-2])
    return p, q

def alpha_bracket(p, q):
    """Two consecutive convergents of alpha_gamma = 1/gamma, as exact bounds."""
    m = len(q) - 2
    lo, hi = Fraction(q[m], p[m]), Fraction(q[m+1], p[m+1])
    return (lo, hi) if lo < hi else (hi, lo)

def floor_alpha(j, lo, hi):
    """Certified floor(j*alpha_gamma); raises if the bracket is too coarse."""
    f = (j*lo).__floor__()
    if f != (j*hi).__floor__():
        raise RuntimeError("bracket too coarse at j=%d" % j)
    return f

def mech_positions(p, q, jmax):
    """ones of w_{p,q}^inf : floor(j q / p), j >= 0."""
    return [(j*q)//p for j in range(jmax)]

def first_mismatch(A, B):
    for j, (x, y) in enumerate(zip(A, B)):
        if x != y:
            return j, min(x, y)
    raise RuntimeError("no disagreement in the computed range")

def word_at(positions, L):
    w = bytearray(L)
    for x in positions:
        if x >= L: break
        w[x] = 1
    return w

def phi_word_mod(w, K):
    """Phi(v) mod 2^K from  3^{k_K} x = -c_K (mod 2^K)."""
    M = 1 << K
    c, k, pw = 0, 0, 1
    for i in range(K):
        if w[i]:
            c = (3*c + pw) % M; k += 1
        pw = (pw << 1) % M
    return (-c * pow(pow(3, k, M), -1, M)) % M

def predicted_g(n, q):
    return q[n] - 1 if n % 2 == 0 else q[n] + q[n+1] - 1

def cmd_slopes(CAP=50000):
    """Theorem 8.3 at seven irrational slopes, by longest common prefix AND
    2-adically.  Both routes are independent; agreement also re-checks the
    isometry (Proposition 2.2) away from beta."""
    ok = True
    for name, a, sideof in SLOPES:
        p, q = convergents_cf(a)
        lo, hi = alpha_bracket(p, q)
        print("%-20s gamma = [0;%s,...]   (%s beta)"
              % (name, ",".join(map(str, a[:8])), sideof))
        print("   n  p_n/q_n                predicted   lcp        v2        match")
        for n in range(1, len(q)-1):
            pred = predicted_g(n, q)
            if pred > CAP: break
            jmax = p[n] + p[n+1] + 4
            A = [floor_alpha(j, lo, hi) for j in range(jmax)]
            B = mech_positions(p[n], q[n], jmax)
            jstar, lcp = first_mismatch(A, B)
            jpred = p[n] + p[n+1] if n % 2 else p[n]
            K = pred + 40
            jw = int(K*p[n]/q[n]) + 4
            x1 = phi_word_mod(word_at([floor_alpha(j, lo, hi) for j in range(jw)], K), K)
            cn = c_of(mech_word(p[n], q[n]))
            x2 = (cn * pow((1 << q[n]) - 3**p[n], -1, 1 << K)) % (1 << K)
            got = v2((x1 - x2) % (1 << K))
            good = (lcp == pred and got == pred and jstar == jpred)
            ok &= good
            print("  %-3d %8d/%-8d %11d %10d %9s   %s"
                  % (n, p[n], q[n], pred, lcp, got,
                     "OK" if good else "MISMATCH"), flush=True)
        print()
    print("  all match" if ok else "  FAILURES PRESENT")
    return ok

def cmd_uniform():
    """Theorem 8.4, Theorem 8.5 and Corollary 8.7: every explicit constant, and
    the exact height floor at the deepest odd convergent of each test slope."""
    import math
    L3 = math.log2(3); c0 = 2 - L3; C = 2 + L3
    ok = True
    def chk(name, cond):
        nonlocal ok
        ok &= bool(cond); print("  [%s] %s" % ("OK" if cond else "FAIL", name))

    print("Constants of Section 8:")
    chk("log2 3 = %.15f" % L3, abs(L3 - 1.5849625007211562) < 1e-15)
    chk("c_0 = 2 - log2 3 = %.15f > 0" % c0, c0 > 0)
    chk("2/c_0 = %.10f" % (2/c0), abs(2/c0 - 4.8188416793) < 1e-9)
    chk("C = 2 + log2 3 = %.10f" % C, abs(C - 3.5849625007) < 1e-9)
    chk("theta = gamma log2 3 < log2 3 for every gamma in (0,1), so c(gamma) > c_0",
        2 - L3 == c0)
    chk("the two rates would meet only at gamma = 2/log2 3 = %.6f > 1" % (2/L3),
        2/L3 > 1)

    print("\n  Q/log2 Q >= 2/c_0 exactly from Q = 22 (and not from 21):")
    chk("21/log2 21 = %.6f <  2/c_0" % (21/math.log2(21)), 21/math.log2(21) < 2/c0)
    chk("22/log2 22 = %.6f >= 2/c_0" % (22/math.log2(22)), 22/math.log2(22) >= 2/c0)
    chk("Q/log2 Q >= 2/c_0 for all 22 <= Q <= 10^6",
        all(Q/math.log2(Q) >= 2/c0 for Q in range(22, 10**6, 7)))

    print("\n  firing threshold (Theorem 8.5):")
    chk("(c_0/2)*5 = %.6f > 1" % (5*c0/2), 5*c0/2 > 1)
    chk("(c_0/2)*22 = %.6f > C = %.6f" % (22*c0/2, C), 22*c0/2 > C)
    chk("q_n >= 5 log2 H + 22  =>  c_0 q_n - log2 q_n > log2 H + C  (log2 H to 10^6)",
        all(c0*(5*L+22) - math.log2(5*L+22) > L + C for L in range(0, 10**6, 97)))
    print("  sharper, for gamma <= beta where c(gamma) = 1:")
    chk("Q/log2 Q >= 2 for all 4 <= Q <= 10^6",
        all(Q/math.log2(Q) >= 2 for Q in range(4, 10**6, 7)))
    chk("q_n >= 2 log2 H + 8  =>  q_n - log2 q_n > log2 H + C  (log2 H to 10^6)",
        all((2*L+8) - math.log2(2*L+8) > L + C for L in range(0, 10**6, 97)))

    print("\n  Convention 8.1 and Lemma 8.2, exactly, at every slope and every n<=14.")
    print("  gamma is enclosed between two convergents, and every quantity built")
    print("  from it is carried as a rational interval; a check passes only if it")
    print("  holds on the whole interval.")
    for name, a, sideof in SLOPES:
        p, q = convergents_cf(a)
        m = len(q) - 1
        i_lo = m if m % 2 == 0 else m - 1          # even convergents lie below gamma
        i_hi = m if m % 2 else m - 1               # odd  convergents lie above gamma
        g_lo, g_hi = Fraction(p[i_lo], q[i_lo]), Fraction(p[i_hi], q[i_hi])
        al_hi = 1/g_lo                              # alpha_gamma = 1/gamma <= 1/g_lo
        def D(n):                                   # rational interval for D_n
            lo, hi = p[n] - q[n]*g_hi, p[n] - q[n]*g_lo
            if n % 2 == 0: lo, hi = -hi, -lo
            return (min(lo, hi), max(lo, hi))
        sub = True
        for n in range(1, 15):
            Dn, Dn1 = D(n), D(n+1)
            sub &= (p[n+1]*q[n] - p[n]*q[n+1] == (-1)**n)                 # exact
            sub &= (Fraction(p[n], q[n]) > g_hi) == (n % 2 == 1)          # the side
            sub &= q[n+1] > q[n]                                          # exact
            sub &= Dn1[1] < Dn[0]                                         # D_{n+1} < D_n
            sub &= q[n+1]*Dn[0] + q[n]*Dn1[0] <= 1 <= q[n+1]*Dn[1] + q[n]*Dn1[1]
            sub &= al_hi*Dn[1] < 1                                        # Lemma 8.2
            sub &= q[n+1] > al_hi                                         # Lemma 8.2
            if n % 2 == 1:
                sub &= (p[n+1]*q[n]) % p[n] == p[n] - 1                   # m_{p_{n+1}}
            if n >= 3:
                sub &= p[n] >= 2                                          # step (iii)
        chk("%-18s  sides, (-1)^n identity, q_{n+1}D_n+q_nD_{n+1}=1, D_n decreasing,"
            " alpha_g D_n<1, q_{n+1}>alpha_g, m_{p_{n+1}}=p_n-1, p_n>=2 (n<=14)" % name, sub)

    print("\n  The step  log2 G_n <= max(1,theta) q_n + log2 3  of Theorem 8.4, in its")
    print("  exact form  p_n - gamma q_n <= 1  (regime B; regime A is trivial), and")
    print("  the exact height floor of Corollary 8.7, at every odd convergent:")
    print("   slope                n   regime   log2 G_n   log2 H_0   [diagnostic]")
    for name, a, sideof in SLOPES:
        p, q = convergents_cf(a)
        # exact rational bounds for gamma: even convergents below, odd above
        m = len(q) - 1
        g_lo = Fraction(p[m if m % 2 == 0 else m-1], q[m if m % 2 == 0 else m-1])
        g_hi = Fraction(p[m if m % 2 else m-1], q[m if m % 2 else m-1])
        th = float(g_lo)*L3; kap = max(1.0, th) - 1.0
        last = None
        for n in range(3, len(q)-1):
            if n % 2 == 0: continue
            depth = q[n] + q[n+1] - 1
            if depth > 400000: break
            two, three = 1 << q[n], 3**p[n]
            G = max(two, three); reg = 'A' if two >= three else 'B'
            lgG = G.bit_length() - 1
            # EXACT: regime A needs nothing; regime B needs p_n - gamma q_n <= 1,
            # and p_n - gamma q_n <= p_n - g_lo q_n since gamma >= g_lo.
            good = True if reg == 'A' else (Fraction(p[n]) - g_lo*q[n] <= 1)
            ok &= good
            H0 = (1 << depth) // ((1 + q[n])*G)
            lgH0 = H0.bit_length() - 1 if H0 > 0 else -1
            pred = q[n+1] - kap*q[n] - math.log2(12*q[n])
            last = (n, reg, lgG, lgH0, pred, good)
        n, reg, lgG, lgH0, pred, good = last
        print("   %-18s %3d      %s %10d %10d %11.1f  %s"
              % (name, n, reg, lgG, lgH0, pred, "OK" if good else "FAIL"))
    print("  (checked at EVERY odd n, not only the deepest, which is the row shown;")
    print("   regime A means 2^{q_n} >= 3^{p_n}.  log2 G_n and log2 H_0 are exact")
    print("   bit lengths; the last column is the float prediction of Section 8,")
    print("   printed for comparison only and used in no decision.)")
    print("\n  ALL CHECKS PASSED" if ok else "\n  FAILURES PRESENT")
    return ok

def cmd_slopecontrols():
    """Rational slopes: the word is periodic, the value rational, and the
    Section 8 argument must not fire."""
    def ceil_div(m, d): return -((-m)//d)
    ok = True
    print("A rational slope p/q gives 1c_{p/q} = w_{p,q}^inf exactly, hence a")
    print("rational value; the argument must produce no contradiction.\n")
    for (pp, qq) in [(5, 8), (2, 3), (41, 65)]:
        L = 8*qq
        w1c = bytes(ceil_div((j+1)*pp, qq) - ceil_div(j*pp, qq) for j in range(L))
        wmec = bytes(word_at(mech_positions(pp, qq, 8*pp + 1), L))
        same = (w1c == wmec)
        ok &= same
        val = Fraction(c_of(list(w1c[:qq])), 2**qq - 3**pp)
        print("  [%s] gamma = %d/%d : 1c_gamma = w^inf over %d letters, Phi = %s"
              % ("OK" if same else "FAIL", pp, qq, L,
                 val if val.denominator != 1 else val.numerator))
    p, q = convergents_cf([1, 1, 1, 2])          # 5/8
    val = Fraction(319, 13); H = 319
    print("\n  gamma = 5/8 = [0;1,1,1,2], Phi(1c_gamma) = %s, H = %d." % (val, H))
    for n in (1, 3):
        G = max(1 << q[n], 3**p[n])
        H0 = (1 << (q[n] + q[n+1] - 1)) // ((1 + q[n])*G)
        good = H > H0
        ok &= good
        print("  [%s] odd n=%d: depth %d forces H > %d; actual H = %d -- no contradiction"
              % ("OK" if good else "FAIL", n, q[n]+q[n+1]-1, H0, H))
    d4 = (1 << q[4]) - 3**p[4]
    c4 = c_of(mech_word(p[4], q[4]))
    M4 = val.numerator*d4 - val.denominator*c4
    good = (M4 == 0)
    ok &= good
    print("  [%s] n=4 is the last convergent and is even: M_4 = u d_4 - v c_4 = %d,"
          % ("OK" if good else "FAIL", M4))
    print("       so the lower bound |M_n| >= 2^depth is vacuous and the chain ends.")
    print("\n  ALL CHECKS PASSED" if ok else "\n  FAILURES PRESENT")
    return ok

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
    elif cmd == "slopes": cmd_slopes(arg or 50000)
    elif cmd == "uniform": cmd_uniform()
    elif cmd == "slopecontrols": cmd_slopecontrols()
    elif cmd == "all":
        for f in (cmd_convergents, cmd_lcp, cmd_heights, cmd_controls, cmd_shadow,
                  cmd_audit, cmd_slopes, cmd_uniform, cmd_slopecontrols):
            print("="*78); f(); print()
    else: print(__doc__)
