"""Task 3 - verification and controls for the general-slope argument.

(a) depth law, 2-adically (independent of the lcp check in depthcheck.py)
(b) Liouville side: exact height floor H0 at the deepest odd n per slope
(c) regime (A: 2^{q_n} wins, B: 3^{p_n} wins) at every odd convergent
(d) controls: a rational slope, and a fixed periodic target
"""
from math import log2
from fractions import Fraction
from slopes import *
from liouville import *

LOG2_3 = 1.5849625007211562

SLOPES = [
    ("1/phi",            cf_golden(40)),
    ("sqrt2-1",          cf_sqrt2m1(30)),
    ("e-2",              cf_e_minus_2(30)),
    ("[0;50,1,1,...]",   cf_from_quotients([50]+[1]*39, 40)),
    ("[0;1,97,1,...]",   cf_from_quotients([1,97]+[1]*38, 40)),
    ("[0;1,1,1,1000,..]",cf_from_quotients([1,1,1,1000]+[1]*36, 40)),
    ("1/(7+1/pi)",       cf_from_quotients([7,3,7,15,1,292,1,1,1,2,1,3,1,14]+[1]*26, 40)),
]

DEPTH_CAP   = 400000     # lcp / height arithmetic
PADIC_CAP   = 60000      # 2-adic cross-check (O(K) bigint steps)

def gamma_float(p, q, n):  return p[n] / q[n]

print("=" * 100)
print("(c)+(b)  REGIME AND EXACT HEIGHT FLOOR AT EVERY ODD CONVERGENT")
print("=" * 100)
summary = []
for name, a in SLOPES:
    p, q = convergents(a)
    g = gamma_float(p, q, len(q) - 1)
    theta = g * LOG2_3
    kappa = max(1.0, theta) - 1.0
    cgam  = 2.0 - max(1.0, theta)
    print(f"\n--- {name}   gamma~{g:.9f}   theta=gamma*log2(3)~{theta:.6f}   "
          f"c(gamma)=2-max(1,theta)~{cgam:.6f}")
    print(f"{'n':>3} {'p_n':>8} {'q_n':>8} {'q_n+1':>8} {'reg':>4} "
          f"{'depth':>9} {'log2 G_n':>11} {'log2 H0':>10} {'predicted':>11}")
    last = None
    for n in range(3, len(q) - 1):
        if n % 2 == 0:
            continue
        depth = q[n] + q[n + 1] - 1
        if depth > DEPTH_CAP:
            break
        reg, H0 = height_floor(p[n], q[n], q[n + 1])
        _, G = regime_and_G(p[n], q[n])
        lg = G.bit_length() - 1
        lgH0 = H0.bit_length() - 1 if H0 > 0 else None
        pred = q[n + 1] - kappa * q[n] - log2(12 * q[n])   # section 6 prediction
        print(f"{n:>3} {p[n]:>8} {q[n]:>8} {q[n+1]:>8} {reg:>4} "
              f"{depth:>9} {lg:>11} {lgH0 if lgH0 is not None else '-':>10} {pred:>11.1f}")
        last = (n, p[n], q[n], q[n+1], reg, depth, lgH0, pred)
    summary.append((name, g, theta, cgam, last))

print("\n" + "=" * 100)
print("(a)  DEPTH LAW, CHECKED 2-ADICALLY (independent of the lcp computation)")
print("=" * 100)
print(f"{'slope':>18} {'n':>3} {'predicted depth':>16} {'v2 computed':>12} {'K':>8}  ok")
padic_fail = []
for name, a in SLOPES:
    p, q = convergents(a)
    N = len(q) - 1
    alpha = Alpha(p, q, N - 1)
    for n in range(3, len(q) - 1):
        if n % 2 == 0:
            continue
        depth = q[n] + q[n + 1] - 1
        if depth + 40 > PADIC_CAP:
            break
        K = depth + 40
        jmax = alpha_jmax = int(K / (q[n] / p[n])) + 4
        ones = [alpha.floor(j) for j in range(int(K * p[n] / q[n]) + 4)]
        w1c = word_from_positions(ones, K)
        wn  = word_from_positions(mech_ones(p[n], q[n], int(K * p[n] / q[n]) + 4), K)
        x1  = phi_mod(w1c, K)
        # periodic value c_n/delta_n mod 2^K, delta_n odd
        wfin = word_from_positions(mech_ones(p[n], q[n], p[n] + 1), q[n])
        cn   = c_word(list(wfin))
        dn   = (1 << q[n]) - 3 ** p[n]
        x2   = (cn * pow(dn % (1 << K), -1, 1 << K)) % (1 << K)
        got  = v2_diff_mod(x1, x2, K)
        ok   = (got == depth)
        if not ok:
            padic_fail.append((name, n, depth, got))
        print(f"{name:>18} {n:>3} {depth:>16} {str(got):>12} {K:>8}  {'OK' if ok else 'FAIL'}")

print("\n" + "=" * 100)
print("(d)  CONTROLS")
print("=" * 100)

# Control 1: rational slope -- the word is periodic, the value is rational,
# and the argument must stop.  gamma = 5/8 (a convergent of beta).
print("\nControl 1: rational slope gamma = 5/8.")
pr, qr = 5, 8
ones_r = [(j * qr) // pr for j in range(400)]
w_rat  = word_from_positions(ones_r, 320)
# 1c_{5/8} built from the ceiling definition, compared with w_{5,8}^infty
from fractions import Fraction as F
g = F(5, 8)
w_ceil = bytearray(320)
for j in range(320):
    w_ceil[j] = int(-((-(j + 1) * g.numerator) // g.denominator)
                    - (-((-j) * g.numerator) // g.denominator))
same = (bytes(w_ceil) == bytes(w_rat))
print(f"  1c_(5/8) equals w_(5,8)^infty over 320 letters : {same}")
val = phi_periodic(list(w_rat[:8]))
print(f"  Phi(1c_(5/8)) = {val}  (rational, as it must be)")
print(f"  M_n = u*delta_n - v*c_n = 0 at n = this level, so v2 = infinity and the")
print(f"  lower bound |M_n| >= 2^depth is vacuous: the argument stops exactly here.")
print(f"  Continued fraction of 5/8 = [0;1,1,1,2] is finite: there is no infinite")
print(f"  sequence of odd n, so 'q_n -> infinity along odd n' fails as well.")

# Control 2: fixed periodic target -- depths must freeze.
print("\nControl 2: fixed periodic target, slope 1/phi, target Phi(w_5^infty).")
a = cf_golden(40); p, q = convergents(a)
m = 5
wm = word_from_positions(mech_ones(p[m], q[m], p[m] + 1), q[m])
target = phi_periodic(list(wm))
print(f"  target Phi(w_{m}^inf) = {target}  (rational)")
print(f"  {'n':>3} {'q_n+q_n+1-1':>13} {'v2(target - Phi(w_n^inf))':>27}")
frozen = q[m] + q[m + 1] - 1
for n in range(3, 16):
    wn = word_from_positions(mech_ones(p[n], q[n], p[n] + 1), q[n])
    d  = target - phi_periodic(list(wn))
    v  = v2_rational(d)
    print(f"  {n:>3} {q[n]+q[n+1]-1:>13} {str(v):>27}")
print(f"  frozen value predicted = q_{m}+q_{m+1}-1 = {frozen}")

print("\n2-adic depth failures:", padic_fail if padic_fail else "none")
