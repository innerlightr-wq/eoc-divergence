"""Verify Xi_alpha = -Phi(1 c_{ln2/ln3}) exactly, and identify the word."""
from conj import Phi_mod

K = 3000
M = 1 << K

def floor_j_alpha(j):
    """floor(j*log2 3) = bitlen(3^j) - 1, exact."""
    return (3 ** j).bit_length() - 1

# the raw parity vector of the accelerated characteristic word:
# ones exactly at the cumulative valuations s_j = floor(j*alpha)
beatty = set()
j = 0
while True:
    s = floor_j_alpha(j)
    if s >= K: break
    beatty.add(s); j += 1
v = [1 if i in beatty else 0 for i in range(K)]

# Xi_alpha mod 2^K by its own definition
A = 0; P3 = 1; J = 0
while True:
    s = P3.bit_length() - 1
    if s >= K: break
    A = (3 * A + (1 << s)) % M; P3 *= 3; J += 1
XI = (A * pow(pow(3, J, M), -1, M)) % M

PHI = Phi_mod(lambda i: v[i], K)
print(f"Xi_alpha  mod 2^{K} == -Phi(v) : {XI == (-PHI) % M}")
print(f"  Xi mod 2^64  = {XI % (1<<64)}")
print(f"  -Phi mod 2^64 = {(-PHI) % M % (1<<64)}")

# identify v: ones-density and comparison with characteristic words of slope s = 1/alpha
ones = sum(v)
print(f"\nones in first {K} digits: {ones}   density = {ones/K:.6f}   ln2/ln3 = {0.6309297535714574:.6f}")
print(f"first 40 digits of v : {''.join(map(str,v[:40]))}")

# characteristic word c_s, s = log_3 2, two common indexings
def c_lower(n):   # floor((n+1)s) - floor(n s),  n >= 0
    return (3 ** (n + 1)).bit_length() - (3 ** n).bit_length()
def c_from1(n):   # same, indexed from n = 1
    return c_lower(n)
w_from0 = [c_lower(n) for n in range(40)]
w_from1 = [c_lower(n) for n in range(1, 41)]
print(f"c_s indexed n>=0    : {''.join(map(str,w_from0))}")
print(f"1 + c_s indexed n>=1: 1{''.join(map(str,w_from1[:39]))}")
print(f"\nv == '1' + c_s(n>=1) ?  {v[:40] == [1] + w_from1[:39]}")
print(f"v == c_s(n>=0) ?        {v[:40] == w_from0}")
# full-length check of the winning identification
full1 = [1] + [c_lower(n) for n in range(1, K)]
print(f"full-length (K={K}) v == '1' + c_s(n>=1): {v == full1}")
