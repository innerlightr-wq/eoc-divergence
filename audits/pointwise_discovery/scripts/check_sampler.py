import os, sys, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from collections import Counter
from fractions import Fraction
from eoc import Map, T31, word_of, rare_depth
from words import Table, deficit, features

FAIL = []
def check(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + (("  " + detail) if detail else ""))
    if not cond: FAIL.append(name)

# S1: table normalisation reproduces num_N
for N, want in [(2, 3), (14, 168807)]:
    t = Table(T31, N)
    check(f"S1 num_{N} = {want}", t.num() == want, f"(got {t.num()})")

# S2: exact word frequencies at small n
rng = random.Random(20260925)
n = 6
t = Table(T31, n)
cnt = Counter(tuple(t.sample(rng)) for _ in range(200000))
# exact probabilities
from itertools import product
exact = {}
for w in product(range(1, 12), repeat=n):
    S = 0; ok = True
    for k, a in enumerate(w, 1):
        S += a
        if S > T31.A(k): ok = False; break
    if ok: exact[w] = Fraction(1, 1 << S)
Z = sum(exact.values())
check("S2a sampler support = exact confined-word set",
      set(cnt) <= set(exact), f"({len(cnt)} seen, {len(exact)} exist)")
worst = max(abs(cnt[w]/200000 - float(p/Z)) for w, p in exact.items())
check("S2b sampler frequencies match the exact dyadic law", worst < 0.004,
      f"(max |empirical-exact| = {worst:.5f} over {len(exact)} words)")
check("S2c normalisation Z = p_n", Z == t.p(), f"({Z} vs {t.p()})")

# S3: sampled words are realizable and the realizer reproduces the word
bad = 0
for _ in range(2000):
    w = t.sample(rng)
    r, S, d = deficit(T31, w)
    if word_of(T31, r, n) != w or not (0 < d <= S + 1): bad += 1
check("S3 every sampled word is realized by its r(w), delta in (0,S+1]",
      bad == 0, f"(2000 words; violations {bad})")

# S4: (*) the counting identity, brute force at small B
for B, n in [(12, 12), (14, 14), (13, 14)]:   # requires n >= B-1
    direct = sum(1 for m in range(1, 1 << B, 2) if rare_depth(T31, m, cap=n) >= n)
    tt = Table(T31, n)
    # enumerate all confined words of length n by DFS, count those with r < 2^B
    cnt2 = 0
    def dfs(k, S, w):
        global cnt2
        if k == n:
            if deficit(T31, w)[0] < (1 << B): cnt2 += 1
            return
        for d in range(1, T31.A(k+1) - S + 1):
            dfs(k+1, S+d, w+[d])
    dfs(0, 0, [])
    check(f"S4 count identity (*) at B={B}, n={n}", direct == cnt2,
          f"(direct {direct}, via r(w) {cnt2})")

# S5: upper-side table for 5x-1, truncation bound
mp = Map(5, -1)
t5 = Table(mp, 60)
tb = float(t5.truncation_bound())
p60 = float(t5.p())
check("S5 5x-1 upper-side truncation mass is negligible", tb / p60 < 1e-9,
      f"(omitted <= {tb:.2e}, relative {tb/p60:.2e}; p_60 = {p60:.6g})")
rng2 = random.Random(7)
bad = 0
for _ in range(500):
    w = t5.sample(rng2)
    r, S, d = deficit(mp, w)
    if word_of(mp, r, 60) != w: bad += 1
check("S5b 5x-1 sampled words realized exactly", bad == 0, f"(violations {bad})")

print()
print("FAILURES:", FAIL if FAIL else "none")
