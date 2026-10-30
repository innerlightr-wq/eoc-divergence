import sys; sys.path.insert(0,'.')
import eoc, math, random
from fractions import Fraction as F
random.seed(20261016)
alpha=math.log2(3)
print("="*94)
print("CORRECTED: the dichotomy has TWO branches and periodic words are caught by the FIRST")
print("="*94)
print("""  Rev 8 Sec 5.3 dichotomy:   either  A + chi*Lambda = 0  (chi pinned to the rational -A/Lambda)
                             or      |chi| >= 2^{S_N}/H - 1 ,  H = max(|A|,|Lambda|).

  GENERIC word: (A, Lambda) = (C_N, 3^N).  Then H >= 3^N >= 2^{S_N} on any confined word,
  so the size branch is vacuous -- for EVERY word, periodic ones included.""")
print()
print("  Generic representation, rho_N = log2(max(C_N,3^N))/S_N :")
def rho_gen(ds,ns):
    rh=eoc.rho(ds); return " ".join(f"{rh[n-1]:>7.4f}" for n in ns if n-1<len(rh))
NS=(10,20,40,60)
rows=[("orbit m0=27", eoc.orbit_word(27,70)[0]),
      ("Beatty word", [int((j+1)*alpha)-int(j*alpha) for j in range(70)]),
      ("periodic [1,2]", ([1,2]*40)[:70]),
      ("periodic [2,1,1,2]", ([2,1,1,2]*20)[:70])]
for nm,ds in rows:
    print(f"    {nm:<22} {rho_gen(ds,NS)}")
print("    -> all >= 1 asymptotically.  The generic size branch is vacuous everywhere.")
print()
print("  PERIODIC COLLAPSE (the first branch).  For a purely periodic word of period p with")
print("  per-period valuation sum sigma, a realizer must satisfy m_{Np} = m_0, so")
print("      m_0 (2^{N sigma} - 3^{Np}) = C_{Np}   =>   m_0 = C_{Np}/(2^{N sigma} - 3^{Np}),")
print("  a FIXED rational independent of N.  That is branch one: chi is pinned outright.")
for p in [[1,2],[2,1,1,2],[1,1,3]]:
    sig=sum(p); vals=[]
    for N in (2,4,8,16):
        ds=(p*N)
        S,C = eoc.SC(ds)
        num=C[len(ds)]; den=(1<<S[len(ds)]) - 3**len(ds)
        vals.append(F(num,den) if den!=0 else None)
    same = all(v==vals[0] for v in vals)
    print(f"    period {str(p):<12} sigma={sig}  m_0 = {str(vals[0]):>14}  "
          f"independent of N: {same}  integer: {vals[0].denominator==1 if vals[0] else '-'}")
print()
print("  So periodic words never needed the size branch: they are pinned to a single rational,")
print("  and one checks directly whether it is a positive integer.  The hard sector is exactly")
print("  the APERIODIC confined words, where branch one is unavailable (no collapse) and")
print("  branch two is vacuous (rho_N >= 1).  BOTH horns fail there simultaneously.")
print()
print("="*94)
print("WHY rho_N >= 1 IS FORCED, not measured   [PROVED]")
print("="*94)
print("  Zero-confinement is the statement 2^{S_n} <= 3^n for all applicable n.  The generic")
print("  height is H = max(C_N, 3^N) >= 3^N >= 2^{S_N}.  Hence")
print("        2^{S_N}/H - 1 <= 0        identically on the confined sector,")
print("  i.e. log2 H >= S_N, i.e. rho_N >= 1, with NO arithmetic input beyond confinement.")
print("  The defining hypothesis of the sector is exactly what voids the tool.")
ok=True
for nm,ds in rows[1:2]+rows[2:3]:
    S,C=eoc.SC(ds)
    for n in range(1,len(S)):
        if (1<<S[n])<=3**n and not (max(C[n],3**n) >= (1<<S[n])): ok=False
print(f"  machine check of the inequality on the words above: {'OK' if ok else 'FAIL'}")
