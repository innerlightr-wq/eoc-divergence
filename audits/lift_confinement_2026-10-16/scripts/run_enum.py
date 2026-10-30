import sys; sys.path.insert(0,'.')
import lift as L, math
from collections import Counter
print("="*98)
print("GENUINELY ZERO-CONFINED ENUMERATION   (2^{S_k} <= 3^k for EVERY k<=N, exact integers)")
print("="*98)
print(f"  {'N':>3} {'cap S_N':>8} {'#confined words':>16} {'S_N range':>12} {'d_0 forced':>11}")
for N in range(1,15):
    Wd=L.enum_confined(N)
    if not Wd: print(f"  {N:>3} {L.cap(N):>8} {0:>16}"); continue
    sums=[L.S(d)[N] for d in Wd]
    d0=set(d[0] for d in Wd)
    print(f"  {N:>3} {L.cap(N):>8} {len(Wd):>16} {f'{min(sums)}..{max(sums)}':>12} {str(sorted(d0)):>11}")
print("  (d_0 = 1 is forced: 2^{d_0} <= 3 and d_0 >= 1.)")
print()
print("="*98)
print("LIFT STATISTICS on the FULL confined enumeration,  J(N) = sum_{n=1}^{N-1} l_n")
print("="*98)
print(f"  {'N':>3} {'#words':>9} {'mean J':>8} {'J/N':>7} {'J/S_N':>7} {'max plateau':>12} "
      f"{'min J':>6} {'max J':>6} {'null E[J]':>10}")
rows=[]
for N in range(4,14):
    Wd=L.enum_confined(N)
    if len(Wd)>400000: Wd=Wd[:400000]
    tj=0; tp=0; mn=10**9; mx=-1; tjn=0; tjs=0; nullE=0.0
    for d in Wd:
        b,l=L.blocks(d); s=L.S(d)
        J=sum(l[1:])
        # longest run of zero lifts within n=1..N-1
        run=best=0
        for n in range(1,N):
            if l[n]==0: run+=1; best=max(best,run)
            else: run=0
        tj+=J; tp+=best; mn=min(mn,J); mx=max(mx,J)
        tjn+=J/(N-1); tjs+=J/s[N]
        nullE += sum(1-2.0**(-d[n]) for n in range(1,N))
    k=len(Wd)
    rows.append((N,k,tj/k,tjn/k,tjs/k,tp/k,mn,mx,nullE/k))
    print(f"  {N:>3} {k:>9} {tj/k:>8.3f} {tjn/k:>7.3f} {tjs/k:>7.3f} {tp/k:>12.3f} "
          f"{mn:>6} {mx:>6} {nullE/k:>10.3f}")
print()
print("  'null E[J]' = sum_{n=1}^{N-1} (1 - 2^{-d_n}), i.e. the prediction if each block b_n were")
print("  UNIFORM on [0,2^{d_n}).  Agreement with mean J tests whether confinement adds anything.")
