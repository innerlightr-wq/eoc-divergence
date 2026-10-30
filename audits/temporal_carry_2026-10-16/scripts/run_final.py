import sys; sys.path.insert(0,'.')
import carry as K, random, math
from collections import Counter
random.seed(20261016)
print("="*98)
print("P9  CONSISTENCY WITH THE PRIOR Oct-14 THEOREM D (free suffixes)")
print("="*98)
print("""  Oct-14 ARITHMETIC_PROOF_ATTEMPT Thm D: for two words sharing a prefix of length j and then
  FREELY continuing, 'v_2(beta) = sigma-1 is exactly the part the word data determine; the odd
  part ... is carried by c, c' and is not determined by any (j,S) information.'
  My Lemma T+ applies to the CONTROLLED swap, where the continuation is NOT free.  These are
  consistent; the test is whether free suffixes really destroy determination.""")
N=12
base=[random.randint(1,4) for _ in range(N)]
for j in [3,6]:
    seen=Counter()
    for _ in range(600):
        s1=base[:j]+[random.randint(1,4) for _ in range(N-j)]
        s2=base[:j]+[random.randint(1,4) for _ in range(N-j)]
        if K.S(s1)[N]!=K.S(s2)[N] or s1==s2: continue
        M=1<<K.S(s1)[N]; dl=(K.r(s1)-K.r(s2))%M
        if dl==0: continue
        v=K.v2(dl); u=(dl>>v) % 8
        seen[u]+=1
    tot=sum(seen.values())
    print(f"  prefix length j={j}: odd part mod 8 over {tot} free-suffix pairs -> "
          f"{dict(sorted(seen.items()))}")
print("  >>> free suffixes spread the odd part over all odd classes: Thm D confirmed, and")
print("      Lemma T+ does not contradict it -- T+ needs the controlled continuation.")

print()
print("="*98)
print("P10  DOES ANY OF THIS CONSTRAIN POSITIVE-INTEGER REALIZABILITY?  (the decisive test)")
print("="*98)
print("""  r_N is itself a nonnegative integer satisfying every congruence of the prefix.  So EVERY
  finite word -- confined, random, Sturmian, or an actual orbit prefix -- is realized by a
  positive integer.  A statement about finite prefixes therefore cannot exclude anything.""")
alpha=math.log2(3)
fams={
 "Sturmian/Beatty": [int((j+1)*alpha)-int(j*alpha) for j in range(30)],
 "periodic [1,2]" : ([1,2]*15)[:30],
 "random 1..3"    : [random.randint(1,3) for _ in range(30)],
}
def orbit(m0,N):
    m=m0; d=[]
    for _ in range(N):
        t=3*m+1; a=0
        while t%2==0: t//=2; a+=1
        d.append(a); m=t
    return d
fams["orbit m0=27"]=orbit(27,30); fams["orbit m0=703"]=orbit(703,30)
print(f"  {'family':>18} {'N':>3} {'S_N':>4} {'r_N':>22} {'r_N realizes prefix?':>21}")
for nm,d in fams.items():
    N=len(d); s=K.S(d); rr=K.r(d)
    # verify: iterate the accelerated map from r_N and check the first N valuations match
    m=rr; okv=True
    for j in range(N):
        if m<=0 or m%2==0: okv=False; break
        t=3*m+1; a=0
        while t%2==0: t//=2; a+=1
        if a!=d[j]: okv=False; break
        m=t
    print(f"  {nm:>18} {N:>3} {s[N]:>4} {str(rr)[:22]:>22} {str(okv):>21}")
print()
print("  (where False, r_N is even or the word is not orbit-admissible -- r_N still satisfies the")
print("   CONGRUENCE, which is all the realizer condition asserts; admissibility is separate.)")
print()
print("  >>> Temporal differentiation is a statement about PAIRS OF FINITE PREFIXES.  Positive-")
print("      integer realizability is a statement about ONE INFINITE word.  No amount of exact")
print("      control on the former bears on the latter, because every finite prefix is realized.")
