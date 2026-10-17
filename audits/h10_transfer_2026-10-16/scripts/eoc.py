"""Accelerated 3x+1 machinery, exact integers only.

Rev 8 Lemma 2.4 (aggregate identity):   2^{S_n} m_n = 3^n m_0 + C_n ,
    C_n = sum_{j<n} 3^{n-1-j} 2^{S_j},   C_0 = 0,  C_{n+1} = 3 C_n + 2^{S_n}.
Realizer congruence:  m_0 == -C_n 3^{-n}  (mod 2^{S_n}).
Canonical residue:    r_n = (-C_n * inv(3^n, 2^{S_n})) mod 2^{S_n}  in [0, 2^{S_n}).
"""
def v2(x):
    k=0
    while x%2==0: x//=2; k+=1
    return k

def accel_step(m):
    "T(m) = (3m+1)/2^a, a = v2(3m+1);  m odd positive"
    t=3*m+1; a=v2(t); return t>>a, a

def orbit_word(m0, N):
    "first N accelerated exponents d_j and the iterates"
    m=m0; ds=[]; ms=[m0]
    for _ in range(N):
        m,a = accel_step(m); ds.append(a); ms.append(m)
    return ds, ms

def SC(ds):
    "partial sums S_n and carries C_n for n = 0..len(ds)"
    S=[0]; C=[0]
    for j,d in enumerate(ds):
        C.append(3*C[-1] + (1<<S[-1]))
        S.append(S[-1]+d)
    return S, C

def residues(ds):
    "canonical residues r_n for n = 0..len(ds)"
    S,C = SC(ds); out=[]
    for n in range(len(S)):
        M = 1<<S[n]
        if M==1: out.append(0); continue
        inv3n = pow(pow(3,n,M), -1, M)
        out.append((-C[n]*inv3n) % M)
    return out, S, C

def check_identity(m0, N):
    ds, ms = orbit_word(m0, N); S,C = SC(ds)
    return all((1<<S[n])*ms[n] == 3**n*m0 + C[n] for n in range(len(S)))

def rho(ds):
    "rho_N = log2 H / S_N,  H = max(|C_N|, 3^N)   (Rev 8 Obs. 5.9)"
    import math
    S,C = SC(ds); out=[]
    for n in range(1,len(S)):
        H = max(C[n], 3**n)
        out.append(math.log2(H)/S[n] if S[n]>0 else float('inf'))
    return out

def confined(ds):
    "zero-confined: 2^{S_n} <= 3^n at every n>=1"
    S,_ = SC(ds)
    return all((1<<S[n]) <= 3**n for n in range(1,len(S)))
