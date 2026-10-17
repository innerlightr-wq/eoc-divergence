import sys; sys.path.insert(0,'.')
import lift as L, random
random.seed(20261016)
print("="*96)
print("THEOREM L1  the lift block is the binary block of the 2-adic realizer")
print("="*96)
print("""  x := lim r_n = - sum_{j>=0} 3^{-(j+1)} 2^{S_j}  in Z_2 (converges since S_j -> inf),
  and b_n = (x >> S_n) mod 2^{d_n}: the lift sequence IS the base-2 expansion of x read in
  windows cut by the partial sums S_n.""")

print()
print("="*96)
print("THEOREM L2  b_n = 0  <=>  v_2(3 m_n + 1) >= d_n   [PROVED]")
print("="*96)
print("""  3^{n+1} r_n + C_{n+1} = 3(3^n r_n + C_n) + 2^{S_n} = 2^{S_n}(3 m_n + 1),  m_n = (3^n r_n+C_n)/2^{S_n}.
  r_{n+1} = r_n  <=>  2^{S_{n+1}} | 3^{n+1} r_n + C_{n+1}  <=>  2^{d_n} | 3 m_n + 1.
  More precisely  b_n == -(3 m_n + 1) 3^{-(n+1)}  (mod 2^{d_n}),
  so v_2(b_n) = v_2(3 m_n + 1) whenever that is < d_n, and b_n = 0 otherwise.""")
def words(N,hi,n):
    return [[random.randint(1,hi) for _ in range(N)] for _ in range(n)]
bad=0; tot=0; badv=0
for d in words(12,3,250)+words(16,2,250)+[L.orbit_word(m,20) for m in (7,27,703,159487,270271)]:
    b,l=L.blocks(d); m=L.mvals(d); N=len(d)
    for n in range(N):
        tot+=1
        lhs=(b[n]==0); rhs=((3*m[n]+1) % (1<<d[n]) == 0)
        if lhs!=rhs: bad+=1
        mm=1<<d[n]
        if b[n] % mm != (-(3*m[n]+1)*pow(pow(3,n+1,mm),-1,mm)) % mm: badv+=1
print(f"  b_n = 0 <=> 2^{{d_n}} | 3m_n+1   on {tot} positions: {'OK' if bad==0 else f'{bad} FAIL'}")
print(f"  b_n == -(3m_n+1)3^{{-(n+1)}} mod 2^{{d_n}} : {'OK' if badv==0 else f'{badv} FAIL'}")

print()
print("="*96)
print("THEOREM L3  m_n is ODD for every prefix realizer  =>  d_n = 1 FORCES b_n = 0  [PROVED]")
print("="*96)
print("""  r_n is the LEAST residue, so 2^{S_n} exactly divides 3^n r_n + C_n (else r_n - 2^{S_{n-1}}...
  would also satisfy the congruence at a smaller value).  Hence m_n is odd, 3m_n+1 is even,
  v_2(3 m_n + 1) >= 1 = d_n, and by L2  b_n = 0.""")
oddbad=0; onebad=0; tot=0
for d in words(12,3,300)+words(16,2,300)+[L.orbit_word(m,20) for m in (7,27,703,159487)]:
    m=L.mvals(d); b,l=L.blocks(d)
    for n in range(len(d)):
        tot+=1
        if m[n] % 2 == 0: oddbad+=1
        if d[n]==1 and b[n]!=0: onebad+=1
print(f"  m_n odd on {tot} positions                : {'OK' if oddbad==0 else f'{oddbad} FAIL'}")
print(f"  d_n = 1  =>  b_n = 0                      : {'OK' if onebad==0 else f'{onebad} FAIL'}")
