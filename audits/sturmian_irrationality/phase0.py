"""Phase 0, Tasks 4 and 5. Exact integer / 2-adic arithmetic only; no floats anywhere."""
import sys, time

# ---------- exact continued fraction of log_2(3) ----------
def cf_log_ratio(n_terms):
    """CF of x = log(A/B)/log(C/D), starting from log(3)/log(2). All exact integers."""
    A, B, C, D = 3, 1, 2, 1
    out = []
    for _ in range(n_terms):
        k = 0
        Ck, Dk = C, D          # (C/D)^(k+1)
        while Ck * B <= A * Dk:
            k += 1
            Ck *= C; Dk *= D
        out.append(k)
        A, B, C, D = C, D, A * (D ** k), B * (C ** k)
    return out

def convergents(cf):
    """(q_n, p_n) with p_n/q_n -> alpha."""
    h0, h1 = 0, 1   # numerators p
    k0, k1 = 1, 0   # denominators q
    out = []
    for a in cf:
        h0, h1 = h1, a * h1 + h0
        k0, k1 = k1, a * k1 + k0
        out.append((k1, h1))
    return out

def is_upper(q, p):
    """R = p - q*alpha > 0  <=>  2^p > 3^q. Exact."""
    return (1 << p) > 3 ** q

# ---------- the constant, mod 2^K ----------
def xi_mod(K):
    """Xi_alpha = sum_j 3^{-(j+1)} 2^{floor(j*alpha)}  (mod 2^K), by Horner on the carry."""
    M = 1 << K
    A = 0          # A_J = sum_{j<J} 3^{J-1-j} 2^{s_j}
    P3 = 1         # 3^j, used only for s_j = bit_length-1
    J = 0
    while True:
        s = P3.bit_length() - 1      # s_j = floor(j*log2 3), exact
        if s >= K:
            break
        A = (3 * A + (1 << s)) % M
        P3 *= 3
        J += 1
    return (A * pow(pow(3, J, M), -1, M)) % M, J

# ---------- Christoffel block carry ----------
def carry_block(q, p, K):
    """C(X_n) mod 2^K for the lower mechanical block of shell (q,p): s_j = floor(j*p/q)."""
    M = 1 << K
    A = 0
    for j in range(q):
        A = (3 * A + (1 << ((j * p) // q))) % M
    return A

def v2_mod(z, K):
    """v2 of z mod 2^K; returns K if z == 0 mod 2^K (i.e. valuation >= K)."""
    z %= (1 << K)
    if z == 0:
        return K
    return (z & -z).bit_length() - 1

if __name__ == "__main__":
    NT = int(sys.argv[1]) if len(sys.argv) > 1 else 18
    cf = cf_log_ratio(NT)
    conv = convergents(cf)
    print("CF of log2(3):", cf)
    print("\nshells (q_n, p_n), n = 0..:")
    for n, (q, p) in enumerate(conv):
        print(f"  n={n:2d}  (q,p) = ({q:7d}, {p:7d})   {'upper' if is_upper(q,p) else 'lower'}")
