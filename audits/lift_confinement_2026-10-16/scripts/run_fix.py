import sys; sys.path.insert(0,'.')
import lift as L, itertools
print("="*96)
print("RETRACTION of L3, and the CORRECTED statement")
print("="*96)
print("""  WRONG (mine, above): "r_n is the least residue, so 2^{S_n} exactly divides 3^n r_n + C_n,
  hence m_n is odd."  Being least mod 2^{S_n} says nothing about divisibility by 2^{S_n+1}.
  m_n is frequently EVEN.  Minimal counterexample, by exhaustive search:""")
found=None
for N in range(1,7):
    for d in itertools.product(range(1,4), repeat=N):
        m=L.mvals(list(d))
        for n in range(N):
            if m[n]%2==0:
                found=(list(d),n,m[n],L.rs(list(d))[n]); break
        if found: break
    if found: break
d,n,mn,rn = found
print(f"    word d={d}, n={n}: r_n={rn}, m_n={mn} (EVEN)")
print(f"    then 3m_n+1={3*mn+1} is odd, v_2=0 < d_n={d[n]}, so b_n != 0 by L2.")
b,l=L.blocks(d); print(f"    check: b_{n} = {b[n]} != 0  -> {b[n]!=0}")
print()
print("  CORRECTED L3'.  [PROVED, verified below]")
print("     (i)  m_n even        =>  v_2(3m_n+1) = 0 < d_n  =>  b_n != 0  (for every d_n >= 1).")
print("     (ii) m_n odd, d_n=1  =>  v_2(3m_n+1) >= 1 = d_n =>  b_n = 0.")
print("     So the lift indicator is   l_n = [m_n even]  OR  [m_n odd AND v_2(3m_n+1) < d_n].")
import random; random.seed(7)
def words(N,hi,n): return [[random.randint(1,hi) for _ in range(N)] for _ in range(n)]
bad1=bad2=tot=0
pool = words(12,3,300)+words(16,2,300)+L.enum_confined(10)[:3000]
for d in pool:
    m=L.mvals(d); b,_=L.blocks(d)
    for n in range(len(d)):
        tot+=1
        if m[n]%2==0 and b[n]==0: bad1+=1
        if m[n]%2==1 and d[n]==1 and b[n]!=0: bad2+=1
print(f"    (i)  on {tot} positions: {'OK' if bad1==0 else f'{bad1} FAIL'}")
print(f"    (ii) on {tot} positions: {'OK' if bad2==0 else f'{bad2} FAIL'}")
print()
print("  CONSEQUENCE for the intended Theorem A' (J(N) <= S_N - N):  WITHDRAWN.")
print("  It rested on L3.  With L3' the d_n=1 positions only force b_n=0 when m_n is ODD,")
print("  and m_n is even about half the time, so no such upper bound follows.")
