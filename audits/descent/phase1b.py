"""L5 (ladder inheritance, finite depth) and L6 numerics. Exact integers only."""
from phase1 import conf_depth, v2, v3, T

def orbit_data(m, N):
    """returns lists m_0..m_N and S_0..S_N"""
    ms = [m]; Ss = [0]; x = m; S = 0
    for _ in range(N):
        t = 3*x + 1; d = v2(t); S += d; x = t >> d
        ms.append(x); Ss.append(S)
    return ms, Ss

def is_conf(ms, Ss, k, upto):
    """restarted seed m_k zero-confined for `upto` steps (non-strict)"""
    for j in range(1, upto+1):
        if (1 << (Ss[k+j] - Ss[k])) > 3**j: return False
    return True

def strict_conf(ms, Ss, k, upto):
    """rho strictly decreasing after k: 2^{S_j(m_k)} < 3^j for 1<=j<=upto"""
    for j in range(1, upto+1):
        if (1 << (Ss[k+j] - Ss[k])) >= 3**j: return False
    return True

def check_future_min(m, N):
    """m in Z_N  =>  m < m_n for 1 <= n <= N"""
    ms, Ss = orbit_data(m, N)
    return all(m < ms[n] for n in range(1, N+1))

def ladder_times(m, N):
    """k in [0,N] with rho_k > rho_n for all k < n <= N (strict future max)"""
    ms, Ss = orbit_data(m, N)
    return [k for k in range(N+1) if strict_conf(ms, Ss, k, N-k)], ms, Ss

if __name__ == "__main__":
    records = [3,7,27,703,10087,35655,270271,362343,381727,626331,
               1027431,1126015,8088063,13421671,20638335,26716671,56924955,63728127]
    print("L5 / future-minimum checks on the r_min record holders")
    print(f"{'m':>12} {'N':>5} {'futmin':>7} {'#ladder':>8} {'ladder vals increasing':>23} {'restarts in Z':>14}")
    allok = True
    for m in records:
        N = conf_depth(m)
        fm = check_future_min(m, N)
        ks, ms, Ss = ladder_times(m, N)
        vals = [ms[k] for k in ks]
        inc = all(vals[i] < vals[i+1] for i in range(len(vals)-1))
        inZ = all(is_conf(ms, Ss, k, N-k) for k in ks)
        ok = fm and inc and inZ
        allok &= ok
        print(f"{m:12d} {N:5d} {str(fm):>7} {len(ks):8d} {str(inc):>23} {str(inZ):>14}")
    print(f"\nall checks pass: {allok}")

    # broader sweep
    bad = 0; tested = 0
    for m in range(3, 3000001, 2):
        N = conf_depth(m)
        if N < 3: continue
        tested += 1
        if not check_future_min(m, N): bad += 1
        ks, ms, Ss = ladder_times(m, N)
        vals = [ms[k] for k in ks]
        if not all(vals[i] < vals[i+1] for i in range(len(vals)-1)): bad += 1
        if not all(is_conf(ms, Ss, k, N-k) for k in ks): bad += 1
    print(f"sweep odd m < 3e6 with depth>=3: tested {tested}, failures {bad}")

    # L6: residues of every Z_N member found, and the 3 | (m+1) population
    cnt = {}; withv3 = 0; tot = 0
    for m in range(3, 3000001, 2):
        if conf_depth(m) >= 1:
            tot += 1
            cnt[m % 12] = cnt.get(m % 12, 0) + 1
            if (m+1) % 3 == 0: withv3 += 1
    print(f"\nZ_1 members < 3e6 by residue mod 12: {dict(sorted(cnt.items()))}")
    print(f"  of {tot}, {withv3} have 3 | (m+1)  (these are the ones with a backward chain)")
