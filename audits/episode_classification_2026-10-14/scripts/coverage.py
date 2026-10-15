"""How much of the real population does F_k with small k actually cover?"""
import os, sys, math, resource
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
resource.setrlimit(resource.RLIMIT_AS, (1 << 32, 1 << 32))
from eoc import *
alpha = math.log2(3)
print("direction changes k inside COMPLETE episodes, over all odd 3 <= m_0 < 60001, c = 1")
print("(each episode counted once; blocks are boundary-inclusive)")
import collections
by_len = collections.defaultdict(list)
tot = 0
for m0 in range(3, 60001, 2):
    d, S, m = orbit(m0, 400)
    try: H = next(n for n in range(len(m)) if m[n] == 1)
    except StopIteration: continue
    for (a, b, trunc) in episodes(S, H, 1):
        if trunc: continue
        k = changes(direction(d[a:b])); by_len[b - a].append(k); tot += 1
print(f"  complete episodes found: {tot}")
print(f"  {'l':>4} {'count':>8} {'min k':>6} {'median k':>9} {'max k':>6} {'mean k/l':>9}")
for L in sorted(by_len):
    if L > 40 and L % 8: continue
    ks = sorted(by_len[L])
    if len(ks) < 3 and L > 12: continue
    print(f"  {L:>4} {len(ks):>8} {ks[0]:>6} {ks[len(ks)//2]:>9} {ks[-1]:>6} "
          f"{sum(ks)/len(ks)/L:>9.4f}")
print()
allk = [(L, k) for L, ks in by_len.items() for k in ks]
big = [(L, k) for (L, k) in allk if L >= 10]
print(f"  episodes with l >= 10: {len(big)};  of those, k <= 2: "
      f"{sum(1 for (L,k) in big if k <= 2)};  k <= 4: {sum(1 for (L,k) in big if k <= 4)}")
print(f"  mean k/l over l >= 10: {sum(k/L for (L,k) in big)/len(big):.4f}")
print(f"  max l with k <= 2: {max([L for (L,k) in allk if k <= 2], default=0)}")
print(f"  max l with k <= 4: {max([L for (L,k) in allk if k <= 4], default=0)}")
print()
print("  READ-OFF: among complete episodes of length >= 10, k is essentially linear in l")
print("  (mean k/l about 0.4), and small-k classes contain only SHORT episodes. So the")
print("  F_k hierarchy at fixed k covers a bounded-length sliver of the real population,")
print("  and the baseline bound alpha^{ceil((k+1)/2)} is astronomically vacuous where")
print("  the population actually lives.")
print(f"peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024:.1f} MiB")
