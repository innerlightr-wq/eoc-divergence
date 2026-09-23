"""Check Lopez-Stoll 2009 Theorem 1 against Xi_alpha, 2-adically, at the critical slope."""
import sys
sys.path.insert(0, '..')
K = 4000; M = 1 << K

# convergents of alpha_LS = ln2/ln3 = 1/log2(3): reciprocals of the log2(3) convergents
def convergents_LS(n):
    # CF of log2 3 = [1;1,1,2,2,3,1,5,2,23,...]; alpha_LS = [0;1,1,1,2,2,3,1,5,2,23,...]
    cf = [0,1,1,1,2,2,3,1,5,2,23,2,2,1,1]
    h0,h1,k0,k1 = 0,1,1,0
    out=[]
    for a in cf[:n]:
        h0,h1 = h1, a*h1+h0
        k0,k1 = k1, a*k1+k0
        out.append((h1,k1))          # (p_j, q_j)
    return out

cv = convergents_LS(13)
print("Lopez-Stoll convergents p_j/q_j of alpha = ln2/ln3:")
for j,(p,q) in enumerate(cv): print(f"  j={j:2d}  {p:6d}/{q:6d}")

# Xi_alpha mod 2^K  (note A), and Phi(1c) = -Xi
A=0; P3=1; J=0
while True:
    s = P3.bit_length()-1
    if s >= K: break
    A = (3*A + (1<<s)) % M; P3 *= 3; J += 1
XI = (A * pow(pow(3,J,M),-1,M)) % M
PHI = (-XI) % M

# Lopez-Stoll Theorem 1
tot = (-pow(3,-1,M)) % M
terms = []
for j in range(len(cv)-1):
    p0,q0 = cv[j]; p1,q1 = cv[j+1]
    if q1 + q0 - 1 >= K: break
    num = (1 << (q1 + q0 - 1)) % M
    den = (3 * (pow(3,p1,M) - pow(2,q1,M)) * (pow(3,p0,M) - pow(2,q0,M))) % M
    t = (num * pow(den,-1,M)) % M
    sgn = -1 if (j+1) % 2 else 1          # (-1)^{j+1}
    tot = (tot - sgn*t) % M
    terms.append((j, q1+q0-1, (tot - PHI) % M))
print(f"\nTheorem 1 partial sums vs Phi(1c_alpha):  v2 of the残 error")
print(f"{'j':>3} {'q_{j+1}+q_j-1':>14} {'v2(partial - Phi)':>18}")
for j, e, d in terms:
    v = K if d == 0 else (d & -d).bit_length()-1
    print(f"{j:3d} {e:14d} {v:18d}")
