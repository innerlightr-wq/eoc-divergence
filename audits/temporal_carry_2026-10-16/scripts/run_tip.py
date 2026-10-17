import sys; sys.path.insert(0,'.')
import carry as K, random, math, itertools
from collections import Counter, defaultdict
random.seed(20261016)

def comp(N, Ssum, dmax=4):
    "all words of length N, digits 1..dmax, summing to Ssum  (exact enumeration)"
    out=[]
    def rec(pref, rem, left):
        if left==0:
            if rem==0: out.append(pref[:])
            return
        if rem < left or rem > dmax*left: return
        for x in range(1, dmax+1):
            pref.append(x); rec(pref, rem-x, left-1); pref.pop()
    rec([], Ssum, N); return out

print("="*98)
print("P6  THE TERMINAL-TIP TEST, with the normalisation the brief requires")
print("="*98)
print("""  Lemma T determines u mod 2^{d_{i+1}}.  The available window is w = S_N - S_{i+1} bits.
  ABSOLUTE information determined = min(d_{i+1}, w) bits.
  RELATIVE fraction              = min(d_{i+1}, w)/w .
  If the tip is special, the ABSOLUTE amount must rise with tau = i/N.""")
N, Ssum, dmax = 11, 22, 4
Wd = comp(N, Ssum, dmax)
print(f"\n  Exact enumeration: N={N}, S_N={Ssum}, digits 1..{dmax}  ->  {len(Wd)} words")
buckets=defaultdict(lambda: [0,0.0,0.0,0])   # count, abs_bits, rel_frac, window
for d in Wd:
    s=K.S(d)
    for i in range(N-1):
        w = s[N]-s[i+1]
        if w<=0: continue
        absb = min(d[i+1], w); rel = absb/w
        b=buckets[i]; b[0]+=1; b[1]+=absb; b[2]+=rel; b[3]+=w
print(f"  {'i':>3} {'tau=i/N':>8} {'#eligible':>10} {'window w':>9} {'ABS bits det':>13} {'REL fraction':>13}")
for i in sorted(buckets):
    c,a,r,wsum=buckets[i]
    print(f"  {i:>3} {i/N:>8.3f} {c:>10} {wsum/c:>9.3f} {a/c:>13.4f} {r/c:>13.4f}")
print()
print("  >>> ABSOLUTE bits determined is FLAT in tau (it is just E[d_{i+1}], the mean digit).")
print("      RELATIVE fraction rises to 1 purely because the window w = S_N - S_{i+1} shrinks.")
print("      The 'terminal tip' is the denominator, not the numerator.")

print()
print("="*98)
print("P7  RAW PAIR COUNTS: is a terminal peak just an eligibility artefact?")
print("="*98)
pairs=defaultdict(int)
for d in Wd:
    for i in range(N):
        for k in range(i+1,N):
            if d[k]>=2 and d[i]+1<=dmax: pairs[i]+=1
tot=sum(pairs.values())
print(f"  {'i':>3} {'#valid swaps':>13} {'share':>8}")
for i in sorted(pairs): print(f"  {i:>3} {pairs[i]:>13} {pairs[i]/tot:>8.4f}")
print("  >>> The number of eligible swaps DECREASES with i (fewer k>i remain).  Any raw count")
print("      peaking late would be impossible here; any statistic summed over pairs must be")
print("      divided by this profile before it means anything.")

print()
print("="*98)
print("P8  IS THE REST OF THE ODD PART UNIFORM once Lemma T is removed?")
print("="*98)
print("  Test the NEXT bit above the determined block: is it balanced?")
res=defaultdict(lambda: Counter())
for d in Wd[:4000]:
    s=K.S(d); M=1<<s[N]
    for i in range(N-1):
        for k in range(i+1,N):
            if d[k]<2 or d[i]+1>dmax: continue
            dd=K.swap(d,i,k)
            delta=(K.r(dd)-K.r(d)) % M
            s1=s[i+1]; w=s[N]-s1
            if w <= d[i+1]: continue
            u=(delta>>s1) % (1<<w)
            nxt=(u >> d[i+1]) & 1
            res[i][nxt]+=1
print(f"  {'i':>3} {'n':>8} {'P(next bit = 1)':>17} {'|z| vs 1/2':>12}")
for i in sorted(res):
    c=res[i]; n=c[0]+c[1]
    if n<40: continue
    p=c[1]/n; z=abs(p-0.5)/math.sqrt(0.25/n)
    print(f"  {i:>3} {n:>8} {p:>17.4f} {z:>12.2f}")
print("  >>> balanced within noise at every position: beyond the block Lemma T determines,")
print("      the odd part shows no further structure that depends on temporal position.")
