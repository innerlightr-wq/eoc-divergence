"""Task 4: verify v2(x_n + Xi_alpha) against the law. Exact 2-adic arithmetic."""
import sys, time
from cf import convergents, lt_alpha

def xi_mod(K):
    """Xi = sum_{j>=0} 3^{-(j+1)} 2^{floor(j*alpha)} mod 2^K, via the carry recursion."""
    M = 1 << K
    A = 0; P3 = 1; J = 0
    while True:
        s = P3.bit_length() - 1          # = floor(j*log2 3), exact
        if s >= K: break
        A = (3 * A + (1 << s)) % M
        P3 *= 3; J += 1
    return (A * pow(pow(3, J, M), -1, M)) % M

def carry_block(q, p, K):
    """C(X_n) mod 2^K, s_j = floor(j*p/q)."""
    M = 1 << K
    A = 0
    for j in range(q):
        A = (3 * A + (1 << ((j * p) // q))) % M
    return A

def v2_mod(z, K):
    z %= (1 << K)
    return K if z == 0 else (z & -z).bit_length() - 1

if __name__ == "__main__":
    K = int(sys.argv[1]); MAXN = int(sys.argv[2])
    cv = convergents(300000)
    t0 = time.time(); XI = xi_mod(K); print(f"Xi mod 2^{K} computed in {time.time()-t0:.1f}s")
    print(f"  Xi mod 2^64 = {XI % (1<<64)}")
    print(f"\n{'n':>3} {'q_n':>8} {'p_n':>8} {'side':>6} {'law':>9} {'observed':>9} {'match':>6}")
    ok = True
    for n in range(2, MAXN + 1):
        q, p = cv[n]
        upper = not lt_alpha(q, p)
        law = (p - 1) if upper else (p + cv[n+1][1] - 1)
        if law >= K:
            print(f"{n:3d} {q:8d} {p:8d} {'upper' if upper else 'lower':>6} {law:9d} {'--':>9}  (K too small)")
            continue
        C = carry_block(q, p, K)
        d = (pow(3, q, 1 << K) - pow(2, p, 1 << K)) % (1 << K)
        x = (-C * pow(d, -1, 1 << K)) % (1 << K)
        obs = v2_mod(x + XI, K)
        good = (obs == law)
        ok &= good
        print(f"{n:3d} {q:8d} {p:8d} {'upper' if upper else 'lower':>6} {law:9d} {obs:9d} {str(good):>6}")
    print(f"\nTask 4: {'ALL MATCH' if ok else 'MISMATCH'}")
