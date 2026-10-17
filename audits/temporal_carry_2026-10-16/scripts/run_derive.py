import sys; sys.path.insert(0,'.')
import carry as K, random, itertools
random.seed(20261016)
def words(N, lo=1, hi=4, n=200):
    return [[random.randint(lo,hi) for _ in range(N)] for _ in range(n)]

print("="*94); print("P0  model self-check: two independent implementations of C_N, and the identity"); print("="*94)
ok=all(K.C(d)==K.C_rec(d) for d in words(9)+words(14))
print(f"  C_N closed form == recurrence : {'OK' if ok else 'FAIL'}")
# identity on genuine orbits
def orbit(m0,N):
    m=m0; d=[]
    for _ in range(N):
        t=3*m+1; a=0
        while t%2==0: t//=2; a+=1
        d.append(a); m=t
    return d,m
ok2=True
for m0 in [7,27,703,159487]:
    d,mN=orbit(m0,25); s=K.S(d)
    if (1<<s[25])*mN != 3**25*m0 + K.C(d): ok2=False
print(f"  2^{{S_N}} m_N = 3^N m_0 + C_N   : {'OK' if ok2 else 'FAIL'}")

print()
print("="*94); print("P1  SINGLE PERTURBATION    d_i -> d_i + eps"); print("="*94)
print("     C_N = sum_{j<=i} 3^{N-1-j}2^{S_j}  +  sum_{j>i} 3^{N-1-j}2^{S_j}")
print("     bumping d_i multiplies every S_j with j>i by 2^eps, so")
print("         Delta_i C_N = (2^eps - 1) * T_i ,      T_i = sum_{j>i} 3^{N-1-j} 2^{S_j}.")
bad=0; tot=0
for d in words(10)+words(15,1,5):
    for i in range(len(d)):
        for eps in (1,2,3):
            tot+=1
            if K.C(K.bump(d,i,eps)) - K.C(d) != ((1<<eps)-1)*K.tail(d,i): bad+=1
print(f"  verified exactly on {tot} (word,i,eps) triples: {'OK' if bad==0 else f'{bad} FAIL'}")

print()
print("="*94); print("P2  SECOND DIFFERENCE  (the 'nonlinear interaction')"); print("="*94)
print("     With A = sum_{j<=i}, B = sum_{i<j<=k}, D = sum_{j>k}:")
print("         C_N(e_i,e_k) = A + 2^{e_i} B + 2^{e_i+e_k} D ,  so")
print("         Delta_i Delta_k C_N = (2^{e_i}-1)(2^{e_k}-1) * T_k .")
bad=0; tot=0
for d in words(10)+words(12,1,5):
    N=len(d)
    for i in range(N):
        for k in range(i+1,N):
            for ei,ek in ((1,1),(1,2),(3,2)):
                tot+=1
                c00=K.C(d); c10=K.C(K.bump(d,i,ei)); c01=K.C(K.bump(d,k,ek))
                c11=K.C(K.bump(K.bump(d,i,ei),k,ek))
                lhs=c11-c10-c01+c00
                if lhs != ((1<<ei)-1)*((1<<ek)-1)*K.tail(d,k): bad+=1
print(f"  verified exactly on {tot} (word,i,k,eps) tuples: {'OK' if bad==0 else f'{bad} FAIL'}")
print()
print("  CONSEQUENCE (exact, no asymptotics):")
print("      Delta_i Delta_k C_N  =  Delta_i C_N * Delta_k C_N / T_i .")
bad=0; tot=0
for d in words(9):
    N=len(d)
    for i in range(N):
        for k in range(i+1,N):
            tot+=1
            di=K.C(K.bump(d,i,1))-K.C(d); dk=K.C(K.bump(d,k,1))-K.C(d)
            dd=K.C(K.bump(K.bump(d,i,1),k,1))-K.C(K.bump(d,i,1))-K.C(K.bump(d,k,1))+K.C(d)
            if dd*K.tail(d,i) != di*dk: bad+=1
print(f"  verified exactly on {tot} (word,i,k) pairs: {'OK' if bad==0 else f'{bad} FAIL'}")
print()
print("  >>> The interaction term is NONZERO but MULTIPLICATIVELY SEPARABLE.  It is the")
print("      identity 2^{a+b} = 2^a 2^b and nothing more.  The second difference is a")
print("      FUNCTION of the two first differences and the tail T_i; it carries no")
print("      information absent from them.")
