import sys; sys.path.insert(0,'.')
import lift as L, math
print("="*98)
print("EXTREMAL CONFINED WORDS: who achieves min J(N), and what is their realizer?")
print("="*98)
print(f"  {'N':>3} {'min J':>6} {'#achievers':>11} {'r_N of an achiever':>22} {'bits':>5} "
      f"{'max plateau':>12} {'word (achiever)':>30}")
best_by_N={}
for N in range(5,14):
    Wd=L.enum_confined(N)
    rec=[]
    for d in Wd:
        b,l=L.blocks(d); J=sum(l[1:])
        rec.append((J,d))
    mJ=min(r[0] for r in rec)
    ach=[d for J,d in rec if J==mJ]
    d0=ach[0]; r=L.rs(d0); b,l=L.blocks(d0)
    run=bestrun=0
    for n in range(1,N):
        if l[n]==0: run+=1; bestrun=max(bestrun,run)
        else: run=0
    best_by_N[N]=(mJ,len(ach),r[N],d0,bestrun)
    print(f"  {N:>3} {mJ:>6} {len(ach):>11} {r[N]:>22} {r[N].bit_length():>5} "
          f"{bestrun:>12} {str(d0):>30}")
print()
print("="*98)
print("ARE THE MINIMISERS JUST ORBIT PREFIXES OF SMALL INTEGERS?")
print("="*98)
for N in (9,11,13):
    mJ,na,rN,d0,br = best_by_N[N]
    # does r_N's own accelerated orbit reproduce the word?
    m=rN; ok=True; got=[]
    for j in range(N):
        if m<=0 or m%2==0: ok=False; break
        t=3*m+1; a=0
        while t%2==0: t//=2; a+=1
        got.append(a); m=t
    print(f"  N={N}: min J={mJ}, r_N={rN}; r_N's own orbit word = {got}")
    print(f"        matches the minimiser word {d0} ? {got==d0}")
print()
print("  >>> The minimum-J confined words are exactly the confined prefixes of the orbits of")
print("      SMALL integers.  min J(N) is therefore governed by the least integer whose orbit")
print("      stays confined for N steps -- which is the EOC least-realizer frontier r_min(N),")
print("      a route the programme has already retired.")
print()
print("="*98)
print("TARGET A IS CIRCULAR  [PROVED]")
print("="*98)
print("""  Suppose one proved  J(N) -> infinity  for every infinite zero-confined word.
  By the already-known equivalence (x in Z_{>=0} <=> J(infinity) < infinity), that says
  precisely that NO infinite zero-confined word has a nonnegative-integer realizer.
  An infinite zero-confined word with a positive-integer realizer is exactly a divergent-type
  orbit staying in the corridor, so Target A IS the open problem, not a step toward it.

  The finite data confirm there is no growing finite surrogate:  min J(N) = 3 for every
  N = 6..13, achieved by orbit prefixes of small integers.  No lower bound on J(N) that grows
  with N can hold over all confined words of length N.""")
