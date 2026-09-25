"""Task 1 validation: the odd-n depth law  q_n + q_{n+1} - 1  (and the even-n law
q_n - 1) for the mechanical convergent words of a general irrational slope."""
import math
from slopes import *

CAP = 400000     # largest depth we are willing to compute

def run(name, a, nmax=40):
    p, q = convergents(a)
    N = len(q) - 1
    alpha = Alpha(p, q, N - 1)
    rows = []
    for n in range(1, min(nmax, N - 1) + 1):
        if p[n] < 1:
            continue
        pred = q[n] + q[n + 1] - 1 if n % 2 == 1 else q[n] - 1
        if pred > CAP:
            break
        jmax = p[n] + p[n + 1] + 4
        A = [alpha.floor(j) for j in range(jmax)]
        B = mech_ones(p[n], q[n], jmax)
        j_star, lcp = lcp_from_positions(A, B)
        j_pred = p[n] + p[n + 1] if n % 2 == 1 else p[n]
        rows.append((n, p[n], q[n], q[n+1], pred, lcp, j_pred, j_star,
                     pred == lcp and j_pred == j_star))
    print(f"\n=== {name}   gamma = [0;{','.join(map(str,a[:9]))},...]   "
          f"alpha=1/gamma in ({float(alpha.lo):.6f},{float(alpha.hi):.6f})")
    print(f"{'n':>3} {'p_n':>8} {'q_n':>8} {'q_n+1':>8} {'pred':>9} {'lcp':>9} "
          f"{'j*pred':>8} {'j*':>8}  ok")
    bad = []
    for r in rows:
        print(f"{r[0]:>3} {r[1]:>8} {r[2]:>8} {r[3]:>8} {r[4]:>9} {r[5]:>9} "
              f"{r[6]:>8} {r[7]:>8}  {'OK' if r[8] else 'FAIL'}")
        if not r[8]:
            bad.append(r[0])
    return bad

SLOPES = [
    ("1/phi = (sqrt5-1)/2", cf_golden(40)),
    ("sqrt2 - 1",           cf_sqrt2m1(30)),
    ("e - 2",               cf_e_minus_2(30)),
    ("large a_1: [0;50,1,1,...]",  cf_from_quotients([50,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],40)),
    ("large early a_2: [0;1,97,1,...]", cf_from_quotients([1,97]+[1]*38,40)),
    ("huge a_4: [0;1,1,1,1000,1,...]", cf_from_quotients([1,1,1,1000]+[1]*36,40)),
    ("small gamma [0;7,3,7,15,1,292,...] ~ 1/(7+1/pi)", cf_from_quotients([7,3,7,15,1,292,1,1,1,2,1,3,1,14]+[1]*26,40)),
]

allbad = {}
for name, a in SLOPES:
    b = run(name, a)
    if b:
        allbad[name] = b
print("\nFAILURES:", allbad if allbad else "none")
