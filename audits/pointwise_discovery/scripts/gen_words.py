"""D2 - generic rare-side words, sampled exactly from the dyadic law, with the
least realizer r(w), the realizer deficit delta(w), and the word features."""
import os, sys, os, random, math, csv, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eoc import Map, carry, realizer, word_of
from words import Table, features, slack_path


def log2_int(x):
    bl = x.bit_length()
    if bl <= 52:
        return math.log2(x)
    top = x >> (bl - 52)
    return (bl - 52) + math.log2(top)


def gen(mp, n, K, seed, out, verify=200):
    t = Table(mp, n)
    rng = random.Random(seed)
    rows = []
    for i in range(K):
        w = t.sample(rng)
        C, S = carry(mp, w)
        r = realizer(mp, w)
        d = (S + 1) - log2_int(r)
        f = features(mp, w)
        f["r_bits"] = r.bit_length()
        f["delta"] = d
        f["root"] = 1 if (r % 3 != 2) else 0        # 3 does not divide r+1
        f["v3r1"] = 0
        x = r + 1
        while x % 3 == 0: f["v3r1"] += 1; x //= 3
        f["r_mod8"] = r % 8; f["r_mod3"] = r % 3
        f["logC_minus_S"] = log2_int(C) - S
        rows.append(f)
    # independent verification on a subsample
    bad = 0
    rng2 = random.Random(seed ^ 0x5eed)
    for _ in range(verify):
        w = t.sample(rng2)
        r = realizer(mp, w)
        if word_of(mp, r, n) != w: bad += 1
    cols = sorted(rows[0].keys())
    with open(out, "w", newline="") as fh:
        wr = csv.DictWriter(fh, fieldnames=cols); wr.writeheader(); wr.writerows(rows)
    return bad, float(t.p())


if __name__ == "__main__":
    os.makedirs("results/words", exist_ok=True)
    jobs = []
    for n in [20, 40, 60]:                              # discovery
        jobs.append((Map(3, 1), n, 40000, 1000 + n))
    for n in [100, 150, 200, 300]:                      # holdout
        jobs.append((Map(3, 1), n, 20000, 1000 + n))
    for q, r in [(3, -1), (5, 1), (5, -1)]:             # controls
        for n in [20, 40, 60, 100, 150, 200]:
            jobs.append((Map(q, r), n, 20000, 2000 + n))
    for mp, n, K, sd in jobs:
        out = f"results/words/{mp.name}_n{n}.csv"
        t0 = time.time()
        bad, p = gen(mp, n, K, sd, out)
        print(f"{mp.name:6s} n={n:4d} K={K:6d}  p_n={p:.6g}  verify_fail={bad}  "
              f"{time.time()-t0:.1f}s", flush=True)
