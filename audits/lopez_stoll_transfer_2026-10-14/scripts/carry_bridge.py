"""The exact bridge:  Lopez-Stoll's real partial sums ARE the EOC carry.

CLAIM 1 (exact, integers).  With S_i the accelerated partial valuation sums and
q_N the EOC carry (q_0 = 0, q_{j+1} = 3 q_j + 2^{S_j}):
        q_N = sum_{i=0}^{N-1} 3^{N-1-i} 2^{S_i} ,
and therefore the Lopez-Stoll real partial sum at ordinary length l = S_N is
        Phi_R(u^(S_N)) = - sum_{i<N} 2^{S_i}/3^{i+1} = - q_N / 3^N .

CLAIM 2 (exact).  The carry identity 2^{S_N} m_N = 3^N m_0 + q_N gives
        q_N / 3^N = (2^{S_N}/3^N) m_N - m_0 = 2^{-Delta_N} m_N - m_0 ,
hence
        sum_{i<N} 2^{-Delta_i}  =  3 ( 2^{-Delta_N} m_N - m_0 ) ,
with 2^{-Delta_N} meaning the EXACT rational 2^{S_N}/3^N.

CLAIM 3.  Phi_R(v) = -lim q_N/3^N exists  <=>  sum_i 2^{-Delta_i} < infinity
       <=>  sum_j 1/m_j < infinity  <=>  E_N = sum log2(1+1/(3m_j)) bounded.

All integer / exact-rational arithmetic.
"""
from fractions import Fraction as F


def accel(m0, N):
    """d_j, S_j, m_j for the accelerated odd map, j = 0..N."""
    d, S, m = [], [0], [m0]
    x = m0
    for _ in range(N):
        t = 3 * x + 1
        v = (t & -t).bit_length() - 1
        d.append(v); x = t >> v
        S.append(S[-1] + v); m.append(x)
    return d, S, m


def carry(S, N):
    """q_N by the recurrence, and by the closed form -- both exact ints."""
    q = 0
    for j in range(N):
        q = 3 * q + (1 << S[j])
    closed = sum(3 ** (N - 1 - i) * (1 << S[i]) for i in range(N))
    return q, closed


def phiR_at(S, N):
    return -sum(F(1 << S[i], 3 ** (i + 1)) for i in range(N))


print("CLAIM 1+2: q_N recurrence = closed form;  Phi_R(u^(S_N)) = -q_N/3^N;")
print("           2^{S_N} m_N = 3^N m_0 + q_N;  sum_{i<N} 2^{-D_i} = 3(2^{-D_N}m_N - m_0)")
print()
bad = 0
for m0 in [3, 7, 27, 31, 703, 10087, 35655, 381727]:
    d, S, m = accel(m0, 40)
    ok = True
    for N in range(1, 41):
        q, closed = carry(S, N)
        if q != closed: ok = False; bad += 1
        if phiR_at(S, N) != F(-q, 3 ** N): ok = False; bad += 1
        if (1 << S[N]) * m[N] != 3 ** N * m0 + q: ok = False; bad += 1
        lhs = sum(F(1 << S[i], 3 ** i) for i in range(N))
        rhs = 3 * (F(1 << S[N], 3 ** N) * m[N] - m0)
        if lhs != rhs: ok = False; bad += 1
    print(f"  m0 = {m0:>7}: all four identities hold for N = 1..40 : {ok}")
print(f"total violations: {bad}")

print()
print("CLAIM 3, numerically: the four equivalent quantities along real orbits")
print(f"{'m0':>8} {'N':>4} {'sum 2^-D_i':>14} {'3(2^-D_N m_N - m_0)':>21} "
      f"{'m_0(2^{E_N}-1)*3':>18} {'max D_i':>9}")
import math
for m0 in (27, 703, 10087, 35655, 381727):
    d, S, m = accel(m0, 60)
    prod = F(1)
    for N in (10, 30, 60):
        prod = F(1)
        for j in range(N):
            prod *= 1 + F(1, 3 * m[j])
        lhs = sum(F(1 << S[i], 3 ** i) for i in range(N))
        rhs = 3 * (F(1 << S[N], 3 ** N) * m[N] - m0)
        third = 3 * m0 * (prod - 1)
        maxD = max(math.log2(3) * i - S[i] for i in range(N + 1))
        print(f"{m0:>8} {N:>4} {float(lhs):>14.8f} {float(rhs):>21.8f} "
              f"{float(third):>18.8f} {maxD:>9.4f}")
