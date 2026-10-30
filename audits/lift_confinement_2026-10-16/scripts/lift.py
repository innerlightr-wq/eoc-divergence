"""Lift-block theory for the accelerated 3x+1 map.  Exact integers only.

S_0=0, S_n = sum_{j<n} d_j ;  C_0=0, C_{n+1} = 3 C_n + 2^{S_n} ;  2^{S_n} m_n = 3^n m_0 + C_n
r_n = (-C_n 3^{-n}) mod 2^{S_n} ;  r_{n+1} = r_n + b_n 2^{S_n},  0 <= b_n < 2^{d_n}
"""
from math import log2, floor

def S(d):
    o=[0]
    for x in d: o.append(o[-1]+x)
    return o

def Cs(d):
    c=[0]; s=S(d)
    for n in range(len(d)): c.append(3*c[-1] + (1<<s[n]))
    return c

def rs(d):
    "canonical residues r_0..r_N"
    s=S(d); c=Cs(d); out=[]
    for n in range(len(d)+1):
        M=1<<s[n]
        out.append(0 if M==1 else (-c[n]*pow(pow(3,n,M),-1,M)) % M)
    return out

def blocks(d):
    "lift blocks b_0..b_{N-1} and indicators l_n"
    s=S(d); r=rs(d)
    b=[(r[n+1]-r[n])>>s[n] for n in range(len(d))]
    return b, [1 if x else 0 for x in b]

def mvals(d):
    "m_n for the prefix realizer: m_n = (3^n r_n + C_n)/2^{S_n}"
    s=S(d); c=Cs(d); r=rs(d)
    out=[]
    for n in range(len(d)+1):
        num=3**n*r[n]+c[n]
        assert num % (1<<s[n]) == 0
        out.append(num >> s[n])
    return out

def v2(x):
    if x==0: return None
    k=0
    while x%2==0: x//=2; k+=1
    return k

def confined(d):
    "2^{S_k} <= 3^k for EVERY k<=N, exact integer comparison"
    s=S(d)
    return all((1<<s[k]) <= 3**k for k in range(1,len(d)+1))

def cap(k):
    "largest S_k allowed by zero confinement: max S with 2^S <= 3^k"
    S_=0
    while (1<<(S_+1)) <= 3**k: S_+=1
    return S_

def enum_confined(N, dmax=None):
    "ALL zero-confined words of length N (d_j>=1, 2^{S_k}<=3^k for all k<=N)"
    out=[]; caps=[cap(k) for k in range(N+1)]
    def rec(pref, s, k):
        if k==N: out.append(pref[:]); return
        top = caps[k+1]-s if dmax is None else min(caps[k+1]-s, dmax)
        for x in range(1, top+1):
            pref.append(x); rec(pref, s+x, k+1); pref.pop()
    rec([],0,0); return out

def orbit_word(m0,N):
    m=m0; d=[]
    for _ in range(N):
        t=3*m+1; a=0
        while t%2==0: t//=2; a+=1
        d.append(a); m=t
    return d
