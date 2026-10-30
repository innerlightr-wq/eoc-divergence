"""Exact accelerated-Collatz carry model and temporal perturbation calculus.

Conventions (EOC Rev 8 Lemma 2.4):
    word  d = (d_0,...,d_{N-1}),  d_j >= 1
    S_0 = 0,  S_j = sum_{i<j} d_i          (so S_N = sum of the whole word)
    C_N = sum_{j=0}^{N-1} 3^{N-1-j} 2^{S_j},   C_0 = 0,  C_{n+1} = 3 C_n + 2^{S_n}
    2^{S_N} m_N = 3^N m_0 + C_N
    r_N = (-C_N * 3^{-N}) mod 2^{S_N}
"""
def S(d):
    out=[0]
    for x in d: out.append(out[-1]+x)
    return out

def C(d):
    s=S(d); N=len(d)
    return sum(3**(N-1-j) * (1<<s[j]) for j in range(N))

def C_rec(d):
    "independent implementation via the recurrence, for cross-checking"
    s=S(d); c=0
    for n in range(len(d)): c = 3*c + (1<<s[n])
    return c

def r(d):
    s=S(d); N=len(d); M=1<<s[N]
    if M==1: return 0
    return (-C(d) * pow(pow(3,N,M), -1, M)) % M

def tail(d, i):
    "T_i = sum_{j>i} 3^{N-1-j} 2^{S_j}   (the carry mass strictly after position i)"
    s=S(d); N=len(d)
    return sum(3**(N-1-j) * (1<<s[j]) for j in range(i+1, N))

def window(d, i, k):
    "W_{i,k} = sum_{j=i+1}^{k} 3^{N-1-j} 2^{S_j}"
    s=S(d); N=len(d)
    return sum(3**(N-1-j) * (1<<s[j]) for j in range(i+1, k+1))

def bump(d, i, eps):
    "perturb d_i -> d_i + eps"
    e=list(d); e[i]+=eps; return e

def swap(d, i, k):
    "S_N-preserving: d_i -> d_i + 1, d_k -> d_k - 1   (requires d_k >= 2)"
    e=list(d); e[i]+=1; e[k]-=1; return e

def v2(x):
    if x==0: return None
    n=0
    while x%2==0: x//=2; n+=1
    return n

def oddpart(x):
    if x==0: return 0
    while x%2==0: x//=2
    return x
