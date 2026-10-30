import sys; sys.path.insert(0,'.')
import carry as K, random
random.seed(20261016)
def words(N,lo=1,hi=4,n=150,dmin=2):
    return [[random.randint(lo,hi) for _ in range(N)] for _ in range(n)]

print("="*96)
print("P3  S_N-PRESERVING SWAP: the only comparison with a common modulus")
print("="*96)
print("""  Bumping d_i changes S_N too, so r and r' live in DIFFERENT moduli and their difference
  is not intrinsic.  The matched comparison is the swap  d_i -> d_i+1, d_k -> d_k-1 (k>i,
  d_k>=2), which preserves S_N.  Then only S_j for i<j<=k change (each by +1), so
        Delta C_N = W_{i,k} := sum_{j=i+1}^{k} 3^{N-1-j} 2^{S_j} .""")
bad=0; tot=0
for d in words(11)+words(14,2,5):
    N=len(d)
    for i in range(N):
        for k in range(i+1,N):
            if d[k]<2: continue
            tot+=1
            if K.C(K.swap(d,i,k)) - K.C(d) != K.window(d,i,k): bad+=1
print(f"  Delta C_N = W_{{i,k}} verified exactly on {tot} swaps: {'OK' if bad==0 else f'{bad} FAIL'}")
print()
print("  Since S_j is STRICTLY increasing (d_j >= 1), the j=i+1 term has strictly least")
print("  2-valuation, so   v_2(W_{i,k}) = S_{i+1}   exactly.")
bad=0; tot=0
for d in words(11)+words(14,2,5):
    N=len(d); s=K.S(d)
    for i in range(N):
        for k in range(i+1,N):
            if d[k]<2: continue
            tot+=1
            if K.v2(K.window(d,i,k)) != s[i+1]: bad+=1
print(f"  v_2(W) = S_{{i+1}} verified exactly on {tot} swaps: {'OK' if bad==0 else f'{bad} FAIL'}")

print()
print("="*96)
print("P4  THE ODD PART -- and the representative trap the brief warns about")
print("="*96)
print("""  Delta r_N := r(d') - r(d) as integers in [0,2^{S_N}) is only defined mod 2^{S_N}.
  v_2 is well defined (since v_2 = S_{i+1} < S_N), but the ODD PART IS NOT: oddpart(x) and
  oddpart(x - 2^{S_N}) differ.  The intrinsic object is
        u := (Delta r_N / 2^{S_{i+1}})  mod  2^{S_N - S_{i+1}} ,   an odd residue.""")
# demonstrate the trap
d=[2,1,3,1,2,2,1,3]; i,k=1,5
if d[k]>=2:
    dd=K.swap(d,i,k); s=K.S(d); M=1<<s[len(d)]
    delta=K.r(dd)-K.r(d); s1=s[i+1]
    print(f"  example d={d}, i={i}, k={k}: Delta r_N = {delta}, v_2 = {K.v2(delta)} (= S_{{i+1}} = {s1})")
    print(f"     oddpart(Delta)          = {K.oddpart(delta)}")
    print(f"     oddpart(Delta - 2^S_N)  = {K.oddpart(delta-M)}   <- different integer, same class")
    print(f"     intrinsic u mod 2^(S_N-S_i+1) = {(delta>>s1) % (1<<(s[len(d)]-s1))}  (both agree) ")

print()
print("="*96)
print("P5  CANDIDATE LEMMA T:  the low bits of the odd part ARE determined by i alone")
print("="*96)
print("""  W = 2^{S_{i+1}} V,  V = 3^{N-2-i} + sum_{j=i+2}^{k} 3^{N-1-j} 2^{S_j - S_{i+1}} ,
  and the first omitted term has valuation S_{i+2}-S_{i+1} = d_{i+1}.  Since
  Delta r_N == -W 3^{-N} (mod 2^{S_N}),
        u == -3^{-(i+2)}   (mod 2^{d_{i+1}}) ,
  independent of N, S_N, k, and of every digit except d_{i+1}.""")
bad=0; tot=0; ex=[]
for d in words(11)+words(13,2,5)+words(9,1,6):
    N=len(d); s=K.S(d); M=1<<s[N]
    for i in range(N-1):
        for k in range(i+1,N):
            if d[k]<2: continue
            dd=K.swap(d,i,k)
            delta=(K.r(dd)-K.r(d)) % M
            s1=s[i+1]; w=s[N]-s1
            u=(delta>>s1) % (1<<w)
            m=1<<min(d[i+1], w)
            lhs=u % m
            rhs=(-pow(pow(3,i+2,m),-1,m)) % m if m>1 else 0
            tot+=1
            if lhs!=rhs:
                bad+=1
                if len(ex)<3: ex.append((d,i,k,lhs,rhs,m))
print(f"  u == -3^{{-(i+2)}} (mod 2^{{d_{{i+1}}}}) verified on {tot} swaps: "
      f"{'OK' if bad==0 else f'{bad} FAIL'}")
for e in ex: print("    counterexample:", e)
