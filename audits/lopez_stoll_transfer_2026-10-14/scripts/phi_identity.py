"""The exact relation between the REAL partial sums of Phi and the 2-adic value.

Lopez-Stoll write  Phi(2^{d_0}+2^{d_1}+...) = -sum_i 2^{d_i}/3^{i+1}  (LS2009 eq.(2)),
where d_0<d_1<... are the positions of the 1's in the parity vector v.
Phi_R(u) denotes that sum truncated to the 1's inside the prefix u.

CLAIM (master identity, exact over Q):  for every odd m_0 >= 1, every prefix
length l, with h = #1's in the first l parity bits of m_0,
        Phi_R(u^(l))  =  m_0  -  (2^l / 3^h) * T^l(m_0) ,
T(x) = x/2 for even x, (3x+1)/2 for odd x.  Hence  Phi(v) = m_0  while
        Phi_R(v) = m_0 - lim_l (2^l/3^h) T^l(m_0)
whenever that limit exists.  The two are DIFFERENT numbers.

All arithmetic exact (Fraction / int).  No floats in any decision.
"""
from fractions import Fraction as F


def parity_bits(m0, L):
    """First L ordinary parity bits of m0 and the ordinary trajectory."""
    bits, traj, x = [], [m0], m0
    for _ in range(L):
        b = x & 1
        bits.append(b)
        x = (3 * x + 1) // 2 if b else x // 2
        traj.append(x)
    return bits, traj


def phi_R_prefix(bits):
    """-sum_i 2^{d_i}/3^{i+1} over the 1-positions d_i inside the prefix."""
    s = F(0); i = 0
    for pos, b in enumerate(bits):
        if b:
            s -= F(2 ** pos, 3 ** (i + 1))
            i += 1
    return s


print("MASTER IDENTITY  Phi_R(u^(l)) = m_0 - (2^l/3^h) T^l(m_0)   [exact over Q]")
print()
bad = 0
for m0 in [1, 3, 5, 7, 9, 11, 27, 703, 10087]:
    bits, traj = parity_bits(m0, 60)
    worst = None
    for L in range(0, 61):
        h = sum(bits[:L])
        lhs = phi_R_prefix(bits[:L])
        rhs = F(m0) - F(2 ** L, 3 ** h) * F(traj[L])
        if lhs != rhs:
            bad += 1; worst = (L, lhs, rhs)
    print(f"  m0={m0:>6}: identity holds for all l = 0..60 : {worst is None}")
print(f"total violations: {bad}")

print()
print("CONSEQUENCE: Phi(v) = m_0 (2-adic), but the REAL limit is")
print("  Phi_R(v) = m_0 - lim (2^l/3^h) T^l(m_0),  which is a DIFFERENT number.")
print()
print("At accelerated endpoints l = S_N, h = N:  (2^{S_N}/3^N) m_N = 2^{-Delta_N} m_N")
print("and by the drift identity m_N = m_0 2^{Delta_N + E_N}, so")
print("  Phi_R(u^(S_N)) = m_0 (1 - 2^{E_N}),   E_N = sum_{j<N} log2(1+1/(3 m_j)) .")
print()
print(f"{'m0':>6} {'N':>3} {'S_N':>5} {'Delta_N':>10} {'2^-D m_N':>14} "
      f"{'m_0(1-2^E_N)':>16} {'Phi_R(u^(S_N))':>18}")
import math
for m0 in (27, 703):
    x = m0; S = 0; E = F(0); prod = F(1)
    bits, traj = parity_bits(m0, 400)
    for N in range(1, 9):
        t = 3 * x + 1
        d = (t & -t).bit_length() - 1
        prod *= (1 + F(1, 3 * x))        # exact 2^{E_N} as a rational product
        x = t >> d; S += d
        D = math.log2(3) * N - S
        h = sum(bits[:S])
        lhs = phi_R_prefix(bits[:S])
        tail = F(2 ** S, 3 ** N) * F(x)
        print(f"{m0:>6} {N:>3} {S:>5} {D:>10.6f} {float(tail):>14.9f} "
              f"{float(m0 * (1 - prod)):>16.9f} {float(lhs):>18.9f}")
    print()
