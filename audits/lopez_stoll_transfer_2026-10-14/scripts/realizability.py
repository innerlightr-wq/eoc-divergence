"""Realizability controls: which confined symbolic words come from POSITIVE integers.

(1) The -1 warning control.  The accelerated word d_j = 1 for all j (= the
    ordinary parity word 111...) is 0-confined with Delta_N = (alpha-1)N -> infinity
    linearly.  Its unique 2-adic realizer is -1, a FIXED POINT of T, not a
    positive seed.  For a positive odd m_0 the all-ones prefix has length
    EXACTLY v_2(m_0+1):  d_j = 1 means m -> (3m+1)/2, whose solution is
    m_j = (m_0+1)(3/2)^j - 1.  Since 3 m_j + 1 = 2[(m_0+1)3^{j+1}/2^{j+1} - 1],
    d_{j+1} = 1 iff (m_0+1)3^{j+1}/2^{j+1} - 1 is odd, i.e. iff j+1 < v_2(m_0+1).
    So the number of leading letters d_j = 1 is EXACTLY v_2(m_0+1) - 1.

(2) Least-realizer congruence check: every confined word of length N is realized
    by exactly one odd residue mod 2^{S_N+1} (EOC/Realizer.lean
    leastRealizer_unique); we recompute it from the carry and verify by direct
    orbit iteration.  The residue exists for EVERY admissible word -- so a
    congruence check can never certify an INFINITE word as positive-integer
    realizable.  That is the gap, exhibited.
"""


def v2(n):
    return (n & -n).bit_length() - 1


def accel_word(m0, N):
    d, x = [], m0
    for _ in range(N):
        t = 3 * x + 1
        k = v2(t); d.append(k); x = t >> k
    return d, x


print("(1) all-ones prefix length vs v_2(m_0+1)")
print(f"{'m0':>10} {'v2(m0+1)-1':>11} {'#leading d_j=1':>15} {'equal':>6}")
bad = 0
for m0 in [1, 3, 5, 7, 15, 31, 63, 127, 255, 1023, 4095, 65535, 27, 703, 10087]:
    d, _ = accel_word(m0, 40)
    k = 0
    while k < len(d) and d[k] == 1: k += 1
    e = v2(m0 + 1) - 1
    bad += (k != e)
    print(f"{m0:>10} {e:>11} {k:>15} {str(k==e):>6}")
print(f"violations: {bad}")
print()
print("  So the INFINITE all-ones word -- 0-confined, Delta_N = (alpha-1)N -> infinity --")
print("  is realizable by NO positive integer: every positive m_0 leaves it after")
print("  v_2(m_0+1) - 1 steps.  Its only 2-adic realizer is -1 = 111..., with T(-1) = -1.")
print("  This is the brief's warning control: a 0-confined symbolic word with")
print("  arbitrarily large linear deficit need not come from a positive seed at all.")
print()

print("(2) least realizer from the carry, vs direct iteration")
print("    r = unique odd x < 2^{S_N+1} with 3^N x + q_N = 2^{S_N} (mod 2^{S_N+1})")


def carry(S):
    q = 0
    for s in S[:-1]:
        q = 3 * q + (1 << s)
    return q


print(f"{'word':>22} {'S_N':>4} {'least realizer':>15} {'reproduces word':>16}")
bad2 = 0
for d in [[1, 1, 1, 1], [1, 2, 1, 2], [2, 1, 2, 1], [1, 1, 2, 2], [2, 2, 1, 1],
          [1, 2, 2, 1, 2], [3, 1, 1, 1]]:
    S = [0]
    for dj in d: S.append(S[-1] + dj)
    N = len(d); SN = S[-1]; M = 1 << (SN + 1)
    q = carry(S)
    # solve 3^N x = 2^{S_N} - q  (mod 2^{S_N+1});  3^N is invertible mod 2^k
    inv = pow(3 ** N, -1, M)
    r = (inv * ((1 << SN) - q)) % M
    dd, _ = accel_word(r, N) if r % 2 == 1 else ([], 0)
    ok = (r % 2 == 1) and dd == d
    bad2 += (not ok)
    print(f"{str(d):>22} {SN:>4} {r:>15} {str(ok):>16}")
print(f"violations: {bad2}")
print()
print("  Every admissible word has such a residue, for every N.  A congruence check")
print("  therefore validates FINITE prefixes only and can never certify an infinite")
print("  word as coming from a positive integer: the residues r_N live in moduli")
print("  2^{S_N+1} that grow, and nothing forces a common positive representative.")
