#!/usr/bin/env python3
"""Regression suite.  Runs from a clean process with no cached state.
Asserts the load-bearing facts of this package; exits nonzero on any failure."""
import os, sys, math, resource, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'scripts'))
resource.setrlimit(resource.RLIMIT_AS, (1 << 32, 1 << 32))
from fractions import Fraction as F
from eoc import *

fails = []
def chk(cond, msg):
    print(('PASS  ' if cond else 'FAIL  ') + msg)
    if not cond: fails.append(msg)

# 1. dictionary, one seed, all n
m0 = 285175
Hc, n_one = last_return_certified(m0, 1)
d, S, m = orbit(m0, Hc)
C, Cc = carries(S, Hc); z = zs(S, Hc); B = Bcal(m, z, Hc)
chk(C == Cc, "carry recurrence equals the closed form")
chk(all((1 << S[n]) * m[n] == 3**n * m0 + C[n] for n in range(Hc+1)),
    "Lemma 2.4: 2^{S_n} m_n = 3^n m_0 + C_n")
chk(all(B[n+1] - B[n] == z[n]/3 for n in range(Hc)),
    "Bcal_{n+1} - Bcal_n = z_n/3")
prod = F(1); ok = True
for n in range(Hc+1):
    if B[n] != m0 * prod: ok = False
    if n < Hc: prod *= 1 + F(1, 3*m[n])
chk(ok, "Bcal_n = m_0 * prod_{j<n}(1+1/(3 m_j))  (Lemma 2.2)")

# 2. Loeb benchmark
eps = episodes(S, Hc, 1)
lens = [b-a for (a,b,_) in eps]
L1 = max(N for N in range(Hc) if all(in_corridor(S,j,1) for j in range(N+1)))
t1 = min(n for n in range(1,Hc) if not in_corridor(S,n,1))
chk(sum(lens) == 98, f"O_1(285175) = 98  (got {sum(lens)})")
chk(L1 == 14 and t1 == 15, f"L_1 = 14, tau_1 = 15  (got {L1}, {t1})")
chk([(a,b) for (a,b,_) in eps] == [(0,15),(16,20),(21,27),(31,95),(98,99),
                                   (100,105),(108,111)], "the seven occupied runs")
chk(lens == [15,4,6,64,1,5,3], "episode lengths 15+4+6+64+1+5+3")
_, Sx, _ = orbit(m0, Hc + 40)          # extend past H for the certification check
chk(n_one == 138 and not any(in_corridor(Sx, n, 1) for n in range(Hc, Hc + 40)),
    "horizon certified by the fixed-point drift: no occupied index in [H,H+40)")

# 3. W_i, eta_i, the toll
ok_id = ok_eta = ok_toll = True
for (a,b,_) in eps:
    Wi = sum(z[n] for n in range(a,b))
    if Wi != 3*(B[b]-B[a]): ok_id = False
    if not (0 < Wi/(F(2)*(b-a)) <= 1): ok_eta = False
    if a > 0 and not (z[a] > F(2,3)*2): ok_toll = False
chk(ok_id, "W_i = 3(Bcal_{b_i} - Bcal_{a_i})")
chk(ok_eta, "0 < eta_i <= 1")
chk(ok_toll, "entry toll z_{a_i} > (2/3)2^c at every re-entry")

# 4. Proposition J, exact integral form, several cases
okJ = True; nre = 0
for (mm0, cc) in [(285175,1),(285175,2),(626331,1),(63728127,1)]:
    H2,_ = last_return_certified(mm0, cc)
    d2,S2,m2 = orbit(mm0,H2); z2 = zs(S2,H2); B2 = Bcal(m2,z2,H2)
    for (a,b,_) in episodes(S2,H2,cc):
        if a == 0: continue
        nre += 1
        r = F(1 << (2*cc)) * F(m2[a])**2 / (F(mm0) * B2[a])
        if not (1 <= r < F(9,4)*B2[a]/mm0): okJ = False
        if r != (B2[a]/mm0) * (F(1<<cc)/z2[a])**2: okJ = False
chk(okJ, f"Proposition J exact at all {nre} re-entries (incl. the 2^{{E_a}}2^{{2c_a}} identity)")

# 5. the gap-domination fact, and the direction of the pot
occW = sum(z[n] for n in range(Hc) if in_corridor(S,n,1))
gapW = sum(z[n] for n in range(Hc) if not in_corridor(S,n,1))
chk(occW + gapW == 3*(B[Hc]-m0), "occupied + gap = 3(Bcal_H - m_0) exactly")
chk(float(gapW/(occW+gapW)) > 0.99, f"pot is >99% gap weight (got {float(gapW/(occW+gapW)):.6f})")

# 6. single infinite-episode silence: P = 1 seeds pay zero toll
for s in (27, 703, 10087, 35655, 381727):
    H3,_ = last_return_certified(s, 1)
    d3,S3,m3 = orbit(s,H3)
    P = len(episodes(S3,H3,1))
    chk(P == 1, f"m_0 = {s}, c = 1 is a single episode (P = {P}), so the toll is 0")

print()
print(('REGRESSION: ALL PASS' if not fails else f'REGRESSION: {len(fails)} FAILURES'))
print(f"peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024:.1f} MiB")
sys.exit(1 if fails else 0)
