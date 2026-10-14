"""Step 1: verify the accounting dictionary exactly.  Preparation, not advance."""
import os, sys, resource
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
resource.setrlimit(resource.RLIMIT_AS, (1 << 32, 1 << 32))
from fractions import Fraction as F
from eoc import *

SEEDS = [3, 7, 27, 31, 703, 10087, 285175, 35655, 381727]
H = 60
bad = 0
print("identity checks over all seeds and all n <= 60 (exact):")
checks = {k: 0 for k in [
    "C recurrence = closed form", "z_n = 2^{S_n}/3^n",
    "Bcal_n = m_n z_n = m_0 + C_n/3^n", "Bcal_{n+1} - Bcal_n = z_n/3",
    "2^{S_n} m_n = 3^n m_0 + C_n", "Bcal_n = m_0 2^{E_n} (as a product)",
    "block: (Bcal_b,z_b) = [[1,u],[0,v]](Bcal_a,z_a)", "block: m_b = (m_a+u)/v",
    "block: 2^s m_b = 3^t m_a + C_[a,b)", "block composition u,v",
    "terminal oddness mod 2^{s+1}"]}
for m0 in SEEDS:
    d, S, m = orbit(m0, H)
    C, Cc = carries(S, H)
    z = zs(S, H); B = Bcal(m, z, H)
    prod = F(1)
    for n in range(H + 1):
        if C[n] != Cc[n]: checks["C recurrence = closed form"] += 1
        if z[n] != F(1 << S[n], 3 ** n): checks["z_n = 2^{S_n}/3^n"] += 1
        if B[n] != F(m[n]) * z[n] or B[n] != m0 + F(C[n], 3 ** n):
            checks["Bcal_n = m_n z_n = m_0 + C_n/3^n"] += 1
        if (1 << S[n]) * m[n] != 3 ** n * m0 + C[n]:
            checks["2^{S_n} m_n = 3^n m_0 + C_n"] += 1
        if B[n] != m0 * prod: checks["Bcal_n = m_0 2^{E_n} (as a product)"] += 1
        if n < H:
            if B[n + 1] - B[n] != z[n] / 3:
                checks["Bcal_{n+1} - Bcal_n = z_n/3"] += 1
            prod *= 1 + F(1, 3 * m[n])
    # blocks
    for (a, b) in [(0, 5), (3, 11), (7, 7), (10, 25), (25, 60), (0, 60)]:
        if b < a or b > H: continue
        u, v, Cab, s, t = block(S, m, a, b)
        if t == 0:
            if u != 0 or v != 1: checks["block composition u,v"] += 1
            continue
        if B[b] != B[a] + u * z[a] or z[b] != v * z[a]:
            checks["block: (Bcal_b,z_b) = [[1,u],[0,v]](Bcal_a,z_a)"] += 1
        if F(m[b]) != (F(m[a]) + u) / v: checks["block: m_b = (m_a+u)/v"] += 1
        if (1 << s) * m[b] != 3 ** t * m[a] + Cab:
            checks["block: 2^s m_b = 3^t m_a + C_[a,b)"] += 1
        if ((3 ** t * m[a] + Cab) - (1 << s)) % (1 << (s + 1)) != 0:
            checks["terminal oddness mod 2^{s+1}"] += 1
    # composition on consecutive blocks
    for (a, mid, b) in [(0, 7, 18), (5, 20, 44), (10, 11, 30)]:
        u1, v1, _, _, _ = block(S, m, a, mid)
        u2, v2, _, _, _ = block(S, m, mid, b)
        ut, vt, _, _, _ = block(S, m, a, b)
        if ut != u1 + v1 * u2 or vt != v1 * v2:
            checks["block composition u,v"] += 1
for k, n in checks.items():
    print(f"  {'OK  ' if n == 0 else 'FAIL'} {k}  (violations {n})")
    bad += n
print(f"\ntotal violations: {bad}")
print(f"peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024:.1f} MiB")
sys.exit(1 if bad else 0)
