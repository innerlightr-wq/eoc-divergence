import sys; sys.path.insert(0,'.')
import carry as K, random
from collections import defaultdict
random.seed(20261016)
print("="*98)
print("P8-CORRECTED.  My first P8 asked whether the bit above the Lemma-T block is 'balanced'.")
print("It is not: measured P(bit=1) = 0.0000 at i=0 and 1.0000 at i=1, |z| = 152.8.  That")
print("printed conclusion ('balanced within noise') was WRONG and is retracted.  The bit is")
print("DETERMINED, and so is every bit below it -- which is the stronger true statement:")
print("="*98)
print("""
  LEMMA T+ (full closed form).  For the S_N-preserving swap (i,k), with
      V_{i,k} = sum_{j=i+1}^{k} 3^{N-1-j} 2^{S_j - S_{i+1}}      (odd, since the j=i+1 term is odd),
  one has, as residues mod 2^{S_N},
      Delta r_N == -2^{S_{i+1}} V_{i,k} 3^{-N} ,
  so the intrinsic odd part u = (Delta r_N / 2^{S_{i+1}}) mod 2^{S_N - S_{i+1}} satisfies
      u == -V_{i,k} 3^{-N}   (mod 2^{S_N - S_{i+1}}) ,   EXACTLY.
  There is no residual component: u is a closed form in (N, i, k, d_{i+1..k-1}).
  Lemma T is its first block: V == 3^{N-2-i} (mod 2^{d_{i+1}}).
""")
def words(N,lo,hi,n):
    return [[random.randint(lo,hi) for _ in range(N)] for _ in range(n)]
bad=0; tot=0; exa=[]
for d in words(11,1,4,300)+words(14,2,5,200)+words(9,1,6,200):
    N=len(d); s=K.S(d); M=1<<s[N]
    for i in range(N-1):
        for k in range(i+1,N):
            if d[k]<2: continue
            dd=K.swap(d,i,k)
            delta=(K.r(dd)-K.r(d)) % M
            s1=s[i+1]; w=s[N]-s1
            u=(delta>>s1) % (1<<w)
            V=sum(3**(N-1-j)*(1<<(s[j]-s1)) for j in range(i+1,k+1))
            mm=1<<w
            rhs=(-V*pow(pow(3,N,mm),-1,mm)) % mm
            tot+=1
            if u!=rhs:
                bad+=1
                if len(exa)<3: exa.append((d,i,k,u,rhs))
print(f"  u == -V_{{i,k}} 3^{{-N}} (mod 2^{{S_N-S_{{i+1}}}}) verified on {tot} swaps: "
      f"{'OK -- NO RESIDUAL' if bad==0 else f'{bad} FAIL'}")
for e in exa: print("   counterexample:", e)
print()
print("  >>> ANSWER TO THE PRIMARY QUESTION.  For the only comparison with a common modulus,")
print("      the difference of realizers has an exact closed form.  The 'residual odd")
print("      component beyond the 2-adic valuation' does not exist: once v_2 = S_{i+1} is")
print("      removed, what remains is -V 3^{-N}, an explicit function of the word.")
print("      Temporal position enters ONLY through which digits appear in V -- i.e. through")
print("      the index range of a sum, not through any new arithmetic.")
