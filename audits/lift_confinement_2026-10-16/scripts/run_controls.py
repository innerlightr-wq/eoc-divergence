import sys; sys.path.insert(0,'.')
import lift as L, math
from collections import defaultdict
print("="*98)
print("NEGATIVE CONTROL: the all-ones word  d_n = 1  (the 2-adic fixed point -1)")
print("="*98)
print("""  d = (1,1,1,...):  S_n = n, and C_n = sum_{j<n} 3^{n-1-j} 2^j = 3^n - 2^n.
  So r_n == -(3^n-2^n)3^{-n} == -1 + 2^n 3^{-n} == -1 (mod 2^n), i.e. r_n = 2^n - 1,
  b_n = 1 for every n, J(N) = N-1, and x = -1: NOT a nonnegative integer.
  It is zero-confined (2^n <= 3^n for all n).""")
d=[1]*20; r=L.rs(d); b,l=L.blocks(d)
print(f"  confined: {L.confined(d)}   r_n = 2^n-1 ? {all(r[n]==(1<<n)-1 for n in range(21))}")
print(f"  b_n all 1 ? {all(x==1 for x in b)}   J(20) = {sum(l[1:])} = N-1 = {len(d)-1}")
print()
print("="*98)
print("THE TWO EXTREMES ARE BOTH CONFINED  ->  confinement constrains J in NEITHER direction")
print("="*98)
print(f"  {'N':>3} {'min J over confined':>20} {'max J over confined':>20} {'N-1':>5}")
for N in range(7,14):
    Wd=L.enum_confined(N); Js=[sum(L.blocks(d)[1][1:]) for d in Wd]
    print(f"  {N:>3} {min(Js):>20} {max(Js):>20} {N-1:>5}")
print("  min stays at 3 (realizer 71); max equals N-1 (all-ones word).  The full range is")
print("  occupied at every N.  NO lift-density bound of any kind follows from confinement.")
print()
print("="*98)
print("CONFINEMENT SLACK  g_n = n log2(3) - S_n :  does it predict lifts?")
print("="*98)
print("  Exact integer slack:  G_n = cap(n) - S_n  (cap(n) = max S with 2^S <= 3^n).")
N=12; Wd=L.enum_confined(N)
tab=defaultdict(lambda:[0,0])
for d in Wd:
    s=L.S(d); b,l=L.blocks(d)
    for n in range(1,N):
        G=L.cap(n)-s[n]
        t=tab[(G,d[n])]; t[0]+=1; t[1]+=l[n]
print(f"  N={N}, all {len(Wd)} confined words.  P(lift) by (slack G_n, current digit d_n):")
print(f"  {'G_n':>4} {'d_n':>4} {'count':>9} {'P(lift)':>9} {'null 1-2^-d':>12}")
for (G,dn) in sorted(tab):
    c,s_=tab[(G,dn)]
    if c<200: continue
    print(f"  {G:>4} {dn:>4} {c:>9} {s_/c:>9.4f} {1-2.0**(-dn):>12.4f}")
print()
print("  >>> P(lift) depends on d_n and is essentially FLAT in the slack G_n at fixed d_n.")
print("      The apparent slack dependence is the digit composition, not the boundary.")
