#!/usr/bin/env python3
"""A2 (full-word verification), A3 (scope of the uninformativeness claim), A4 (singleton shell)."""
import math, sys
sys.setrecursionlimit(10000)
ALPHA = math.log2(3)

def Kcap(N,S):
    a=0
    while (1<<(S+a+1)) <= 3**(N+1): a+=1
    return a
def words(N):
    out=[]
    def rec(k,S,C,w):
        if k==N: out.append((tuple(w),S,C)); return
        Cn=3*C+(1<<S); a=1
        while (1<<(S+a)) <= 3**(k+1):
            w.append(a); rec(k+1,S+a,Cn,w); w.pop(); a+=1
    rec(0,0,0,[]); return out
def realizer(N,S,C):
    q=1<<(S+1); r=((1<<S)-C)*pow(3,-N,q)%q
    return q if r==0 else r
def acc_word(m,n):
    w=[];S=0
    for _ in range(n):
        x=3*m+1;a=(x&-x).bit_length()-1;w.append(a);S+=a;m=x>>a
    return tuple(w),S,m

print("="*78); print("A2. FULL-WORD verification (exhaustive, not sampled)"); print("="*78)
print(f"  {'N':>3} {'words':>10} {'word mismatch':>14} {'S-only would pass':>18} {'brute-force xcheck':>19}")
for N in (8,12,16):
    ws=words(N); bad=0; sonly=0
    # brute force: for N<=12 find the least positive seed realising each word directly
    brute_ok = "n/a"
    if N<=12:
        M=1<<(max(S for _,S,_ in ws)+1)
        first={}
        for m in range(1,M+1,2):
            w,S,mN=acc_word(m,N)
            if w not in first: first[w]=m
        bb=0
        for w,S,C in ws:
            if first.get(w)!=realizer(N,S,C): bb+=1
        brute_ok=f"{bb} mismatch"
    for w,S,C in ws:
        r=realizer(N,S,C); ww,SS,mN=acc_word(r,N)
        if ww!=w: bad+=1
        if ww!=w and SS==S: sonly+=1     # caught by full word, MISSED by the S-only test
    print(f"  {N:>3} {len(ws):>10,} {bad:>14} {sonly:>18} {brute_ok:>19}")
print("  'S-only would pass' counts words where the total valuation matches but the WORD")
print("  differs; 0 means the weaker test happens to agree here, not that it is equivalent.")

print(); print("="*78)
print("A3. The brief's finite example, and the exact scope of uninformativeness")
print("="*78)
N=1; ws=words(1); w,S,C=[x for x in ws if x[0]==(1,)][0]
q=1<<(S+1); r=realizer(N,S,C); K=Kcap(N,S); M=15
seeds=[r+q*t for t in range((M-r)//q+1)]
print(f"  w=(1): S={S} C={C} q_w={q} r_w={r} K={K}  seeds<=15: {seeds}")
m1=[acc_word(m,1)[2] for m in seeds]
a2=[(lambda x:(x&-x).bit_length()-1)(3*v+1) for v in m1]
print(f"  next odd states m_1: {m1}")
print(f"  following valuations a_2: {a2}   cap K={K}  -> failures at t = "
      f"{[t for t,a in enumerate(a2) if a>K]}")
print(f"  m_1 mod 5: {[v%5 for v in m1]}   -> 'm_1 = 0 mod 5' selects t = "
      f"{[t for t,v in enumerate(m1) if v%5==0]}")
print("  => the example is CORRECT: an odd-modulus feature identifies the failure here.")
print()
print("  WHY, and what the correct general statement is:")
print("  m_N(t) = x_w + 2*3^N*t, so for odd u, m_N mod u determines t mod u (2*3^N invertible).")
print(f"  Here u=5 and the lift interval has only n={len(seeds)} < 5 points, so t mod 5 = t,")
print("  which determines t mod 2^K.  The feature is informative ONLY through the truncation.")
print("  Over a COMPLETE cylinder (n a multiple of 2^K) CRT makes t mod u independent of")
print("  t mod 2^K, so the feature is exactly uninformative.  Verified:")
for u in (3,5,7):
    worst=0
    for N in range(1,9):
        for w,S,C in words(N):
            K=Kcap(N,S); q=1<<(S+1); r=realizer(N,S,C); n=1<<K   # exactly one full period
            num=3**N*r+C; x=num>>S
            tab={}
            for t in range(n):
                mN=x+2*3**N*t
                xx=3*mN+1; fail=((xx&-xx).bit_length()-1)>K
                tab.setdefault(mN%u,[0,0]); tab[mN%u][0]+=1; tab[mN%u][1]+=fail
            base=sum(v[1] for v in tab.values())/n
            for cls,(cnt,f) in tab.items():
                worst=max(worst,abs(f/cnt-base))
    print(f"     complete cylinders, feature m_N mod {u}: max |P(fail|class) - P(fail)| = {worst:.3e}")

print(); print("="*78)
print("A4. The singleton shell s=N in ShellWeyl's normalization")
print("="*78)
print("  WeylBound U N K C  :=  forall s, K <= s -> sum_{g!=0} ||shellWeyl s g|| <= (C-1)*#shell(s)")
print(f"  {'N':>4} {'#shell(s=N)':>12} {'r_w(1^N)':>12} {'=2^(N+1)-1?':>12}")
for N in (4,8,12,16,20):
    ws=[x for x in words(N) if x[1]==N]
    r=realizer(N,N,3**N-2**N)
    print(f"  {N:>4} {len(ws):>12} {r:>12,} {str(r==(1<<(N+1))-1):>12}")
print()
print("  Singleton => |shellWeyl(g)|=1 for every g, so sum_{g!=0} = 2^n - 1 with n=s+1-K=N+1-K.")
print("  WeylBound then forces (C-1) >= 2^n - 1, i.e. C >= 2^n = 2^d with d = N+1-K.")
print(f"  {'kappa':>7} {'N=ceil(kB), B=100':>18} {'K=B':>5} {'s=N >= K?':>10} {'d=N+1-K':>8} {'C >= 2^d':>12}")
for k in (0.65,0.80,0.95,1.00,1.05,1.20):
    B=100; N=math.ceil(k*B); inscope = (N>=B)
    d=N+1-B
    print(f"  {k:>7.2f} {N:>18} {B:>5} {str(inscope):>10} {d:>8} {('2^%d'%d) if inscope else 'n/a':>12}")
print()
print("  Also: r_w(1^N) = 2^(N+1)-1 < 2^K iff N+1 <= K, i.e. d <= 0.  So whenever the shell IS")
print("  in scope (d >= 1) the true below-cutoff count is 0 while the main term is #shell/2^n =")
print("  2^-d > 0: the exact signed discrepancy is -2^-d, FAVOURABLE, and destroyed by | . |.")
print("  CONCLUSION: the obstruction is correct mathematics, but it bites only for kappa >= 1.")
print("  At the Phase B target kappa=0.65 the shell s=N has s < K and is out of scope, i.e.")
print("  already fully resolved as a complete cylinder.")
