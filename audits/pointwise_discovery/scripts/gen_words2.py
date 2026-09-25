import os, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eoc import Map
from gen_words import gen
import time
for n in [120, 140, 160, 180, 250]:
    out = f"results/words/3x+1_n{n}.csv"
    t0 = time.time(); bad, p = gen(Map(3,1), n, 20000, 1000+n, out)
    print(f"3x+1 n={n} p={p:.6g} fail={bad} {time.time()-t0:.1f}s", flush=True)
for q, r in [(3,-1), (5,-1)]:
    for n in [120, 140]:
        out = f"results/words/{Map(q,r).name}_n{n}.csv"
        t0 = time.time(); bad, p = gen(Map(q,r), n, 20000, 3000+n, out)
        print(f"{Map(q,r).name} n={n} p={p:.6g} fail={bad} {time.time()-t0:.1f}s", flush=True)
