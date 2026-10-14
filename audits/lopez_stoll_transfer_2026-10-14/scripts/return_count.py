"""THEOREM R, verified: a return-count bound from the carry identity.

Identity (PRIOR, = the carry closed form):
    sum_{i<N} 2^{-Delta_i} = 3 ( (2^{S_N}/3^N) m_N - m_0 ) = 3 m_0 (2^{E_N} - 1),
with 2^{-Delta_i} the EXACT rational 2^{S_i}/3^i.

Repo input (PRIOR, EOC/HarmonicPacking.lean sum_inv_orbit_le): if m_0 is odd and
m_0,...,m_{N-1} are pairwise distinct then  sum_{k<N} 1/m_k <= 7/3 + (1/3) log N.
Hence E_N = sum log2(1+1/(3 m_k)) <= (1/(3 ln2))(7/3 + (1/3) log N)
          = 7/(9 ln 2) + (1/(9 ln 2)) log N,   so  2^{E_N} <= e^{7/9} N^{1/9}.

THEOREM R (new corollary).  For every w >= 0,
    #{ i < N : Delta_i <= w }  <=  2^w sum_{i<N} 2^{-Delta_i}
                               =  3 m_0 2^w (2^{E_N} - 1)
                               <=  3 e^{7/9} m_0 2^w N^{1/9}.
Putting the count equal to N and w = B log2 N + C recovers EXACTLY the repo's
LogCorridor.logFloor_window_bound' :  N^{8/9 - B} <= 3 e^{7/9} 2^C m_0.
So Theorem R is a COUNTING GENERALISATION of that theorem, same mechanism and
same constant, with "every prefix" weakened to "the returning indices".
"""
from fractions import Fraction as F
import math

E79 = math.exp(7 / 9)
print(f"3 e^(7/9) = {3*E79:.6f}   (the repo's constant in logFloor_window_bound')")
print()


def accel(m0, N):
    S, m, x = [0], [m0], m0
    for _ in range(N):
        t = 3 * x + 1
        v = (t & -t).bit_length() - 1
        x = t >> v; S.append(S[-1] + v); m.append(x)
    return S, m


def inj_len(m0, cap):
    """Largest N with m_0..m_{N-1} pairwise distinct."""
    seen, x = set(), m0
    n = 0
    while n < cap:
        if x in seen: return n
        seen.add(x); n += 1
        t = 3 * x + 1
        x = t >> ((t & -t).bit_length() - 1)
    return cap


print(f"{'m0':>8} {'Ninj':>5} {'N':>5} {'sum 2^-D_i':>13} {'3m0(2^E_N-1)':>14} "
      f"{'3e^(7/9)m0 N^(1/9)':>20} {'ok':>4} | {'#D<=0':>6} {'#D<=1':>6} "
      f"{'#D<=2':>6} {'bound w=2':>11} {'ok':>4}")
bad = 0
for m0 in [3, 7, 27, 31, 703, 10087, 35655, 381727, 626331]:
    Ninj = inj_len(m0, 400)
    N = max(1, Ninj - 1)
    S, m = accel(m0, N)
    tot = sum(F(1 << S[i], 3 ** i) for i in range(N))
    prod = F(1)
    for j in range(N): prod *= 1 + F(1, 3 * m[j])
    alt = 3 * m0 * (prod - 1)
    bound = 3 * E79 * m0 * (N ** (1 / 9))
    ok1 = (tot == alt) and (float(tot) <= bound)
    # exact return counts: Delta_i <= w  <=>  2^{S_i} >= 3^i / 2^w  <=>  2^{S_i+w} >= 3^i
    cnt = {}
    for w in (0, 1, 2):
        cnt[w] = sum(1 for i in range(N) if (1 << (S[i] + w)) >= 3 ** i)
    b2 = 4 * float(tot)
    ok2 = cnt[2] <= b2
    bad += (not ok1) + (not ok2)
    print(f"{m0:>8} {Ninj:>5} {N:>5} {float(tot):>13.6f} {float(alt):>14.6f} "
          f"{bound:>20.2f} {str(ok1):>4} | {cnt[0]:>6} {cnt[1]:>6} {cnt[2]:>6} "
          f"{b2:>11.2f} {str(ok2):>4}")
print(f"\nviolations: {bad}")

print()
print("CONTROL: drop the injectivity hypothesis and the bound must fail.")
for m0 in (27, 703):
    Ninj = inj_len(m0, 400)
    for N in (Ninj - 1, Ninj + 20, Ninj + 40):
        S, m = accel(m0, N)
        tot = float(sum(F(1 << S[i], 3 ** i) for i in range(N)))
        bound = 3 * E79 * m0 * (N ** (1 / 9))
        print(f"  m0={m0:>5} N={N:>4} (injective through {Ninj}) sum={tot:>14.2f} "
              f"bound={bound:>9.2f}  holds={tot<=bound}")
