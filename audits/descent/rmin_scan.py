import sys, time
from phase1 import conf_depth, v3

LIM = int(sys.argv[1])
t0 = time.time()
best = {}
recs = []
m = 3
while m < LIM:
    N = conf_depth(m)
    if N >= 1:
        if N not in best or m < best[N]:
            pass
        newly = [k for k in range(1, N+1) if k not in best]
        if newly:
            for k in newly: best[k] = m
            recs.append((m, N))
    m += 2
print(f"scan to {LIM}: {time.time()-t0:.1f}s, max N = {max(best)}")
print("\ndistinct r_min values (record holders):")
print(f"{'m':>12} {'depth':>6} {'covers N':>12} {'m%12':>5} {'v3(m+1)':>8}")
bad = 0
for m, N in recs:
    ks = [k for k in sorted(best) if best[k] == m]
    if m % 12 not in (3, 7): bad += 1
    print(f"{m:12d} {N:6d} {min(ks):5d}-{max(ks):<6d} {m%12:5d} {v3(m+1):8d}")
print(f"\nL4 check: r_min(N) mod 12 in {{3,7}} for all N=1..{max(best)}: "
      f"{'PASS' if bad==0 else f'FAIL ({bad})'}")
print(f"L4 monotone: r_min non-decreasing: "
      f"{'PASS' if all(best[k] <= best[k+1] for k in range(1, max(best))) else 'FAIL'}")
