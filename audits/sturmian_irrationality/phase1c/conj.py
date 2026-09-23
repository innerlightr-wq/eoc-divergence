"""Phase 1c, Task 1: the 3x+1 conjugacy map Phi on parity vectors.
Exact 2-adic arithmetic; every check is an exact integer comparison."""

def T_mod(x, K):
    """one step of T on Z/2^K -> Z/2^{K-1}; returns (parity, next x, new K)."""
    v = x & 1
    if v == 0:
        return 0, (x >> 1), K - 1
    return 1, ((3 * x + 1) >> 1), K - 1

def Phi_mod(bits, K):
    """Phi(v) mod 2^K from the closed form  Phi(v) = -sum_{i: v_i=1} 3^{-k_{i+1}} 2^i."""
    M = 1 << K
    inv3 = pow(3, -1, M)
    S = 0; p = 1
    for i in range(K):
        if bits(i):
            p = (p * inv3) % M
            S = (S + p * (1 << i)) % M
    return (-S) % M

def parity_vector(x, K):
    """the first K parities of the T-orbit of x (x given mod 2^K)."""
    out = []; k = K
    for _ in range(K):
        v, x, k = T_mod(x, k)
        out.append(v)
    return out

def mech(s_num, s_den):
    """characteristic mechanical word of slope s = s_num/s_den, intercept 0:
       v_j = floor((j+1)s) - floor(js).  Exact integer arithmetic."""
    return lambda j: ((j + 1) * s_num) // s_den - (j * s_num) // s_den

def c_w_and_den(w):
    """periodic word w^inf: Phi(w^inf) = c_w / (2^l - 3^k), exact integers."""
    l = len(w); k = sum(w)
    c = 0; kappa = 0
    for r in range(l):
        if w[r]:
            kappa += 1
            c += 3 ** (k - kappa) * (1 << r)
    return c, (1 << l) - 3 ** k, l, k

if __name__ == "__main__":
    K = 400
    # --- 1.2 check: v = 1^inf gives -1 ---
    x = Phi_mod(lambda i: 1, K)
    print(f"Phi(1^inf) mod 2^{K} == -1 mod 2^{K} : {x == ((-1) % (1 << K))}")
    print(f"Phi(0^inf) == 0 : {Phi_mod(lambda i: 0, K) == 0}")

    # --- 1.2 check: the closed form really produces that parity vector ---
    import random
    random.seed(11)
    ok = True
    for trial in range(200):
        bits = [random.randint(0, 1) for _ in range(K)]
        x = Phi_mod(lambda i: bits[i], K)
        pv = parity_vector(x, K // 2)
        ok &= (pv == bits[:K // 2])
    print(f"closed form reproduces the parity vector (200 random words, {K//2} steps): {ok}")

    # --- 1.3 check: periodic words ---
    ok = True
    for trial in range(300):
        l = random.randint(1, 14)
        w = [random.randint(0, 1) for _ in range(l)]
        if sum(w) == 0: continue
        c, den, l, k = c_w_and_den(w)
        if den == 0: continue           # 2^l = 3^k impossible for l,k>=1 but guard
        lhs = Phi_mod(lambda i: w[i % l], K)
        rhs = (c * pow(den, -1, 1 << K)) % (1 << K)
        ok &= (lhs == rhs)
    print(f"Phi(w^inf) = c_w/(2^l - 3^k) (300 random periods): {ok}")

    # --- 1.1 smoke test: isometry / lcp ---
    ok = True
    for trial in range(200):
        a = [random.randint(0, 1) for _ in range(K)]
        b = a[:]
        L = random.randint(0, K - 60)
        b[L] ^= 1
        for i in range(L + 1, K):
            b[i] = random.randint(0, 1)
        xa = Phi_mod(lambda i: a[i], K); xb = Phi_mod(lambda i: b[i], K)
        d = (xa - xb) % (1 << K)
        v2 = (d & -d).bit_length() - 1
        ok &= (v2 == L)
    print(f"v2(Phi(a) - Phi(b)) = lcp(a,b) (200 random pairs): {ok}")
