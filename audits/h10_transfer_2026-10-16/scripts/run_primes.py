import sys; sys.path.insert(0,'.')
import eoc, math
alpha=math.log2(3)
print("="*92)
print("H10's ENGINE NEEDS MANY PRIMES.  Does a Collatz word constrain any prime but 2?")
print("="*92)
print("""  In H10 the height estimate is  h(s) <= H * M(s)^c ,  M(s) = product of the CONTACT PRIMES
  (nonexceptional primes where one of five fixed linear forms has odd valuation).  M(s) varies
  with s and can be large; that is exactly what converts divisibility into a height bound.

  In Collatz the realizer condition is a single congruence modulo 2^{S_N}.  The realizers are
      { r_N + k*2^{S_N} : k >= 0 } ,
  so for any odd modulus q the realizers hit EVERY residue class mod q (gcd(2,q)=1, CRT).
  The word therefore imposes NO condition at any prime other than 2.""")
print()
ds=[int((j+1)*alpha)-int(j*alpha) for j in range(40)]
r,S,C=eoc.residues(ds); N=40; M=1<<S[N]
print(f"  Beatty confined word, N={N}, modulus 2^{S[N]}.  Residue classes hit by r_N + k*2^S:")
print(f"  {'q':>7} {'classes hit':>12} {'q itself':>9} {'all?':>6}")
for q in [3,9,27,81,5,7,11,13,3**5]:
    hit={(r[N]+k*M)%q for k in range(4*q)}
    print(f"  {q:>7} {len(hit):>12} {q:>9} {'YES' if len(hit)==q else 'no':>6}")
print()
print("  => M(s) has no Collatz analogue.  There is one prime, one modulus, and the odd part")
print("     of the problem is completely unconstrained.  This is the repo's own Sec 4b finding")
print("     ('a code imposes no 3-adic condition on its start'), reproved here in one line.")
print()
print("="*92)
print("AND THE SECOND INGREDIENT: H10 closes with a QUADRATIC height.  Collatz has none.")
print("="*92)
print("""  H10's endgame:   h(x(eta(a_j) P)) <<_f B      (linear, from the contact-prime bound)
                   h^(nP) ~ c n^2                (quadratic, canonical height on E)
                   => B^2 <<_f B  => B = O(1)   => nonstandard forced to standard.

  The quadratic comes from the Neron-Tate canonical height, a positive-definite QUADRATIC
  FORM on a finitely generated abelian group.  The Collatz realizer structure is the affine
  map m_0 |-> (m_0 mod 2^{S_n}); the only group in sight is Z_2 under addition, which carries
  no positive-definite quadratic form with respect to which the residues grow.  Every
  comparison available (S_n vs n log2 3, log m_0 vs S_n) is LINEAR in the exponent.

  Without a quadratic-vs-linear squeeze there is no forcing step, and the H10 architecture
  has no endgame in this setting.""")
