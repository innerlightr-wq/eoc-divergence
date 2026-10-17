import sys; sys.path.insert(0,'.')
import lift as L
from collections import defaultdict
N=13; Wd=L.enum_confined(N)
print("="*98)
print(f"RESOLVING: why did mean J exceed the per-word null at N={N}?")
print("="*98)
obs=defaultdict(lambda:[0,0]); nul=defaultdict(float); cnt=defaultdict(int)
for d in Wd:
    b,l=L.blocks(d)
    for n in range(1,N):
        o=obs[n]; o[0]+=1; o[1]+=l[n]
        nul[n]+= 1-2.0**(-d[n]); cnt[n]+=1
print(f"  {'n':>3} {'#words':>8} {'obs P(lift)':>12} {'mean null':>11} {'diff':>8} {'mean d_n':>9}")
td=defaultdict(float)
for d in Wd:
    for n in range(1,N): td[n]+=d[n]
for n in range(1,N):
    c,s_=obs[n]
    print(f"  {n:>3} {c:>8} {s_/c:>12.4f} {nul[n]/cnt[n]:>11.4f} {s_/c-nul[n]/cnt[n]:>+8.4f} {td[n]/c:>9.4f}")
print()
print("  The excess is concentrated at SMALL n and fades with n.  Cause: at small n the")
print("  modulus 2^{S_n} is tiny, so r_n is forced into a very small range and the block b_n")
print("  is far from uniform -- the uniform-block null is simply a bad model there.")
print("  By n >= 6 the observed rate tracks the null closely.")
print()
print("  So the earlier headline 'lift density runs above the uniform null' is CORRECT as a")
print("  raw statement but MISLEADING as a finding: it is a small-n boundary effect, not a")
print("  confinement effect.  Corrected here.")
print()
print("="*98)
print("DOES THE EXCESS SURVIVE AT LARGE n?  tail-only comparison")
print("="*98)
for lo in (1,4,6,8):
    to=sum(obs[n][1] for n in range(lo,N)); tc=sum(obs[n][0] for n in range(lo,N))
    tn=sum(nul[n] for n in range(lo,N)); tcc=sum(cnt[n] for n in range(lo,N))
    print(f"  positions n >= {lo}: obs {to/tc:.4f}  null {tn/tcc:.4f}  diff {to/tc-tn/tcc:+.4f}")
