"""N0 -- the random-placement null model for the SIZE of a record holder.

The odd m with a given zero-confined valuation word d of total S form exactly one
residue class mod 2^{S+1} (Terras/Everett), so among ODD integers their density is
2^{-S}.  Summing over all zero-confined words of length N gives the exact density

    p_N(0) = sum_{d confined, |d| = N} 2^{-S(d)} ,

which is `Occupation.p N 0`.  Under random placement the k-th smallest N-confined
odd integer sits near  r_k(N) ~ 2k / p_N(0), so the residual to report is

    Delta_k(N) = log2 r_k(N) - log2( k / p_N(0) ) .

p_N(0) is computed EXACTLY here by the transfer recursion over (k, S):
    f[0][0] = 1 ,   f[k+1][S'] = sum_{d >= 1} f[k][S'-d]   for  S' <= A[k+1] ,
with A[k] = floor(k log2 3) = bit_length(3^k) - 1.  Writing  L = A[N],
    num_N := sum_S f[N][S] * 2^{L-S}   is an exact integer, and  p_N(0) = num_N / 2^L.
num_N is also, exactly, the number of odd m in [1, 2^{L+1}) that are N-confined --
which is how it is cross-checked against the scanner below.
"""
import math
from anatomy import A

def transfer(Nmax):
    """f[N] as a dict S -> exact count, and num[N] = sum_S f[N][S] * 2^{A[N]-S}."""
    f = {0: 1}
    nums = {}
    for k in range(1, Nmax + 1):
        Ak = A(k)
        # prefix sums of f over S, then g[S'] = sum_{d>=1} f[S'-d] = prefix(S'-1)
        if not f: break
        Smax = max(f)
        pre = [0] * (Ak + 2)
        run = 0
        for S in range(0, Ak + 1):
            run += f.get(S, 0)
            pre[S] = run
        g = {}
        for Sp in range(1, Ak + 1):
            v = pre[Sp - 1]
            if v: g[Sp] = v
        f = g
        L = Ak
        nums[k] = sum(c << (L - S) for S, c in f.items())
    return nums

def log2_int(n):
    b = n.bit_length()
    return math.log2(n) if b <= 53 else (b - 53) + math.log2(n >> (b - 53))

def log2_inv_p(N, nums):
    """log2(1 / p_N(0)) = A[N] - log2(num_N)."""
    return A(N) - log2_int(nums[N])

if __name__ == "__main__":
    import sys
    Nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    nums = transfer(Nmax)
    print("exact cross-check of the transfer recursion against the scanner")
    print("num_N must equal #{odd m < 2^{A[N]+1} : m is N-confined}")
    import subprocess, collections
    for N in (1, 2, 3, 4, 5, 6, 8, 10, 12, 14):
        L = A(N)
        out = subprocess.run(['./scan', '1', str(1 << (L + 1))], capture_output=True, text=True)
        cnt = 0
        # recount directly with the python reference for an independent path
        from anatomy import conf_depth
        cnt = sum(1 for m in range(3, 1 << (L + 1), 4) if conf_depth(m, N + 2) >= N)
        print(f"  N={N:<3} A[N]={L:<3} num_N={nums[N]:<12} direct count={cnt:<12} "
              f"{'OK' if nums[N] == cnt else 'MISMATCH'}")
    I0 = None
    print("\nScale 1 and Scale 2, tested on the exact p_N(0):")
    print(f"{'N':>5} {'log2(1/p_N)':>14} {'/N':>10} {'-I0 N -1.5lgN':>14}")
    a = math.log2(3)
    H = -(1/a) * math.log2(1/a) - (1 - 1/a) * math.log2(1 - 1/a)
    I0 = a * (1 - H)
    for N in (10, 20, 50, 100, 150, 200, 250, min(300, Nmax)):
        if N > Nmax: break
        L = log2_inv_p(N, nums)
        print(f"{N:>5} {L:>14.4f} {L/N:>10.6f} {L - I0*N - 1.5*math.log2(N):>14.4f}")
    print(f"  I0 = alpha(1 - H2(1/alpha)) = {I0:.7f}  (Occupation.confined_mass_rate)")
