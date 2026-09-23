"""The lockstep invariance: forward d=1 steps move budget and requirement equally."""
from phase1 import v2, v3, conf_depth
from phase3 import required_j
from phase1b import orbit_data

def check_lockstep(zs, limit_orbit=300):
    bad = 0; tested = 0
    detail = []
    for z in zs:
        N = min(conf_depth(z), limit_orbit)
        ms, Ss = orbit_data(z, N)
        for k in range(N):
            d = Ss[k+1] - Ss[k]
            if d != 1: continue
            tested += 1
            hv, hv1 = v3(ms[k]+1), v3(ms[k+1]+1)
            rq, rq1 = required_j(ms[k], z), required_j(ms[k+1], z)
            if hv1 != hv + 1: bad += 1
            if rq1 != rq + 1:  bad += 1
            if (hv1 - rq1) != (hv - rq): bad += 1
    return tested, bad

def surplus_profile(z):
    N = conf_depth(z)
    ms, Ss = orbit_data(z, N)
    out = []
    for k in range(N+1):
        d = (Ss[k] - Ss[k-1]) if k >= 1 else None
        out.append((k, d, v3(ms[k]+1) - required_j(ms[k], z)))
    return out

if __name__ == "__main__":
    records = [27,703,10087,35655,270271,362343,381727,626331,
               1027431,1126015,8088063,13421671,20638335,26716671,56924955,63728127]
    t, b = check_lockstep(records)
    print(f"lockstep under forward d=1 steps: tested {t} steps, failures {b}")

    # what d>=2 does to the 3-adic budget
    from collections import Counter
    cnt = Counter()
    for z in records:
        N = conf_depth(z); ms, Ss = orbit_data(z, N)
        for k in range(N):
            d = Ss[k+1] - Ss[k]
            if d >= 2:
                cnt[(d % 2 == 0, v3(ms[k+1]+1) == 0)] += 1
    print(f"\nd>=2 steps: (d even, budget destroyed) counts = {dict(cnt)}")
    print("  d even  => 2^d - 2 = 2 (mod 3) => v3(m_{k+1}+1) = 0 : budget destroyed")
    print("  d odd   => 2^d - 2 = 0 (mod 3) => budget may survive")

    # surplus never turns positive except where already observed
    print(f"\n{'z':>10} {'max surplus over orbit':>24} {'at k':>6} {'d there':>8}")
    for z in records:
        prof = surplus_profile(z)
        k, d, s = max(prof[1:], key=lambda r: r[2])
        print(f"{z:10d} {s:24d} {k:6d} {str(d):>8}")
