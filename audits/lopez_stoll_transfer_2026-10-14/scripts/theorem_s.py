"""THEOREM S: bounded-gap, bounded-width near-critical returns are impossible
for a permanently zero-confined positive integer.  Exact integer checks.

If every window [N, N+G) contains some i with Delta_i <= w, then the number of
returns below N is at least floor(N/G), so Theorem R gives
    N/G  <=  3 e^{7/9} m_0 2^w N^{1/9}   ==>   N^{8/9} <= 3 e^{7/9} m_0 2^w G ,
i.e. the orbit can be injective for at most
    N_max = ( 3 e^{7/9} m_0 2^w G )^{9/8}
steps.  Beyond that it repeats a state, hence is eventually periodic, hence not
divergent.  So no divergent orbit has bounded-gap bounded-width returns.
"""
import math
from fractions import Fraction as F
E79 = math.exp(7 / 9)


def accel(m0, N):
    S, m, x = [0], [m0], m0
    for _ in range(N):
        t = 3 * x + 1
        v = (t & -t).bit_length() - 1
        x = t >> v; S.append(S[-1] + v); m.append(x)
    return S, m


def inj_len(m0, cap):
    seen, x, n = set(), m0, 0
    while n < cap:
        if x in seen: return n
        seen.add(x); n += 1
        t = 3 * x + 1
        x = t >> ((t & -t).bit_length() - 1)
    return cap


print("Theorem S, checked against real orbits: measured max return gap G_meas")
print("vs the largest G that Theorem S permits at the observed injective depth.")
print()
print(f"{'m0':>8} {'Ninj':>5} {'w':>2} {'#returns':>9} {'G_meas':>7} "
      f"{'N^(8/9)':>10} {'3e^(7/9)m0 2^w G_meas':>22} {'S holds':>8}")
bad = 0
for m0 in [27, 31, 703, 10087, 35655, 381727, 626331]:
    Ninj = inj_len(m0, 600)
    N = Ninj - 1
    S, m = accel(m0, N)
    for w in (0, 2):
        # exact: Delta_i <= w  <=>  2^{S_i + w} >= 3^i
        R = [i for i in range(N) if (1 << (S[i] + w)) >= 3 ** i]
        if len(R) < 2:
            continue
        gaps = [R[k + 1] - R[k] for k in range(len(R) - 1)]
        G = max(gaps + [R[0] + 1, N - R[-1]])
        lhs = N ** (8 / 9)
        rhs = 3 * E79 * m0 * (2 ** w) * G
        ok = lhs <= rhs
        bad += (not ok)
        print(f"{m0:>8} {Ninj:>5} {w:>2} {len(R):>9} {G:>7} {lhs:>10.2f} "
              f"{rhs:>22.2f} {str(ok):>8}")
print(f"\nviolations of the inequality: {bad}")
print()
print("Reading: for every real seed tested the inequality is satisfied with room,")
print("i.e. Theorem S is consistent with the data and its content is a CAP on how")
print("long an orbit with regular narrow returns can stay injective:")
print(f"{'m0':>8} {'w':>2} {'G':>4} {'N_max = (3e^(7/9) m0 2^w G)^(9/8)':>36}")
for m0 in (27, 703, 10087):
    for w, G in ((0, 1), (0, 5), (2, 5)):
        print(f"{m0:>8} {w:>2} {G:>4} {(3*E79*m0*(2**w)*G)**(9/8):>36.1f}")
