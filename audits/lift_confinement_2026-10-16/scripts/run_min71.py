import sys; sys.path.insert(0,'.')
import lift as L
print("="*98)
print("CORRECTION: why r_N = 71 for every minimiser, and why some minimisers are NOT orbit words")
print("="*98)
print("""  The congruence r_n ≡ -C_n 3^{-n} only forces  2^{d_j} | 3 m_j + 1, i.e. v_2 >= d_j.
  Equality is NOT forced.  When v_2(3 m_j+1) > d_j the next iterate m_{j+1} is EVEN and the
  word is a CONGRUENCE word, not an ORBIT word.  So 'least congruence realizer' and 'orbit
  prefix' are different notions, and my earlier sentence conflated them.  Retracted.""")
print()
print("  71's accelerated orbit and its confinement:")
m=71; w=[]; 
print(f"  {'j':>3} {'m_j':>10} {'d_j':>4} {'S_{j+1}':>8} {'2^S <= 3^(j+1)?':>16}")
S_=0
for j in range(14):
    t=3*m+1; a=0
    while t%2==0: t//=2; a+=1
    S_+=a; w.append(a)
    print(f"  {j:>3} {m:>10} {a:>4} {S_:>8} {str((1<<S_) <= 3**(j+1)):>16}")
    m=t
print(f"  71's word (14 steps): {w}")
print()
print("  Minimisers at each N, with whether each is an ORBIT word of its own r_N:")
print(f"  {'N':>3} {'#min':>5} {'r_N':>6} {'orbit word?':>12} {'all m_j odd?':>13}")
for N in range(7,14):
    Wd=L.enum_confined(N)
    rec=[(sum(L.blocks(d)[1][1:]), d) for d in Wd]
    mJ=min(x[0] for x in rec); ach=[d for J,d in rec if J==mJ]
    norb=0; nodd=0
    for d in ach:
        mv=L.mvals(d)
        if all(x%2==1 for x in mv[1:]): nodd+=1
        m0=L.rs(d)[N]; mm=m0; okw=True
        for j in range(N):
            if mm<=0 or mm%2==0: okw=False; break
            t=3*mm+1; a=0
            while t%2==0: t//=2; a+=1
            if a!=d[j]: okw=False; break
            mm=t
        if okw: norb+=1
    print(f"  {N:>3} {len(ach):>5} {L.rs(ach[0])[N]:>6} {f'{norb}/{len(ach)}':>12} {f'{nodd}/{len(ach)}':>13}")
print()
print("  CORRECTED STATEMENT.  All minimisers share r_N = 71; only SOME are orbit words of 71.")
print("  The rest are congruence words that undershoot a valuation (some m_j is even).")
print("  What is actually true, and is the point:  min J(N) is pinned by the SMALLEST integer")
print("  admitting a length-N confined congruence word, and that integer does not grow over the")
print("  enumerable range -- it is 71 from N=7 to N=13.")
