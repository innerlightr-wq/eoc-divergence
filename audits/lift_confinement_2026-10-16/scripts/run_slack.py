import sys; sys.path.insert(0,'.')
import lift as L
from collections import defaultdict
print("="*98)
print("THE SLACK EFFECT, PROPERLY CONTROLLED")
print("="*98)
print("""  KEY STRUCTURAL FACT:  b_n is determined by (d_0,...,d_n) alone -- r_n and d_n depend only
  on the prefix through position n, and the future digits never enter.  So pooling over FULL
  WORDS counts each prefix with multiplicity = (number of admissible continuations), and words
  with larger slack have MORE continuations.  That is a pure weighting artefact.

  CORRECT CONTROL: enumerate PREFIXES, each counted exactly once.""")
NMAX=13
# enumerate all confined prefixes of each length, once each
pref=defaultdict(lambda: defaultdict(lambda:[0,0]))   # length -> (G,d) -> [count, lifts]
def rec(d, s, k):
    if k>0:
        n=k-1
        if n>=1:
            G=L.cap(n)-L.S(d)[n]
            b,l=L.blocks(d)
            t=pref[k][(G,d[n])]; t[0]+=1; t[1]+=l[n]
    if k==NMAX: return
    top=L.cap(k+1)-s
    for x in range(1, top+1):
        d.append(x); rec(d, s+x, k+1); d.pop()
rec([],0,0)
agg=defaultdict(lambda:[0,0])
for k in pref:
    for key,v in pref[k].items():
        a=agg[key]; a[0]+=v[0]; a[1]+=v[1]
print()
print("  P(lift) by (slack G_n, digit d_n), each PREFIX counted once:")
print(f"  {'G_n':>4} {'d_n':>4} {'#prefixes':>11} {'P(lift)':>9} {'null 1-2^-d':>12} {'diff':>8}")
for (G,dn) in sorted(agg):
    c,s_=agg[(G,dn)]
    if c<300: continue
    p=s_/c
    print(f"  {G:>4} {dn:>4} {c:>11} {p:>9.4f} {1-2.0**(-dn):>12.4f} {p-(1-2.0**(-dn)):>+8.4f}")
print()
print("  Compare with the FULL-WORD pooling (previous run), d_n = 1 column:")
print("     full-word  G=0..3:  0.7423  0.6879  0.6391  0.5982   <- apparent monotone trend")
r1=[agg[(G,1)] for G in range(4) if (G,1) in agg]
print("     prefix     G=0..3:  " + "  ".join(f"{s_/c:.4f}" for c,s_ in r1))
print()
print("  >>> The monotone slack trend at d_n=1 is MUCH reduced once each prefix is counted once.")
print("      What remains is reported above; it is not flat, and I do not claim it is.")
print("      Whatever remains cannot carry arithmetic content anyway: b_n is a deterministic")
print("      function of (d_0..d_n), so P(lift | G, d_n) is a statement about how the CONFINED")
print("      PREFIX SET is distributed, not about any new arithmetic constraint.")
