"""Are Lopez-Stoll's convergents the periodic cycle values Phi(m_{p/q}^inf)?
Compare v2(Phi(1c_alpha) - Phi(m_{p_k/q_k}^inf)) with note (A)'s valuation law."""
from conj import Phi_mod
K = 4000; M = 1 << K

def ceil_div_word(p, q):
    """their upper mechanical word m_{p/q}: w_j = ceil((j+1)p/q) - ceil(j p/q), j=0..q-1"""
    c = lambda n: -((-n * p) // q)          # ceil(n*p/q), exact
    return [c(j + 1) - c(j) for j in range(q)]

# Phi(1c_alpha), alpha = ln2/ln3  (== -Xi_alpha)
A = 0; P3 = 1; J = 0
while True:
    s = P3.bit_length() - 1
    if s >= K: break
    A = (3 * A + (1 << s)) % M; P3 *= 3; J += 1
XI = (A * pow(pow(3, J, M), -1, M)) % M
PHI = (-XI) % M

cf = [0,1,1,1,2,2,3,1,5,2,23]
h0,h1,k0,k1 = 0,1,1,0
conv=[]
for a in cf:
    h0,h1 = h1, a*h1+h0
    k0,k1 = k1, a*k1+k0
    conv.append((h1,k1))

print(f"{'k':>3} {'p_k/q_k':>14} {'noteA shell (q,p)':>19} {'v2(Phi(1c)-Phi(per))':>21} {'noteA law':>10} {'side':>6}")
# note (A) shells are (q_n,p_n) = (p_k, q_k) of Lopez-Stoll
for k,(p,q) in enumerate(conv):
    if q == 1 and p == 0: continue
    if q + (conv[k+1][1] if k+1 < len(conv) else 0) >= K: break
    w = ceil_div_word(p, q)
    per = Phi_mod(lambda i: w[i % q], K)
    d = (PHI - per) % M
    v = K if d == 0 else (d & -d).bit_length() - 1
    # note (A): shell (q_n,p_n) = (p, q); upper iff 2^{q} > 3^{p}
    upper = (1 << q) > 3 ** p
    law = (q - 1) if upper else (q + conv[k+1][1] - 1)
    print(f"{k:3d} {f'{p}/{q}':>14} {f'({p},{q})':>19} {v:21d} {law:10d} {'upper' if upper else 'lower':>6}")
