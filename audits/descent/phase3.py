"""Phase 3: the exact round-trip criterion, evaluated at ladder times.
Exact integers only; the geometric baseline is the only heuristic number."""
from fractions import Fraction
from phase1 import conf_depth, v2, v3
from phase1b import orbit_data, strict_conf, is_conf

def required_j(mk, z):
    """least j with 2^j (mk+1) < 3^j (z+1); None if none <= 4000"""
    a, b = mk + 1, z + 1
    p2, p3 = 1, 1
    for j in range(0, 4001):
        if p2 * a < p3 * b: return j
        p2 *= 2; p3 *= 3
    return None

def analyse(z):
    N = conf_depth(z)
    ms, Ss = orbit_data(z, N)
    ks = [k for k in range(N+1) if strict_conf(ms, Ss, k, N-k)]
    rows = []
    for k in ks:
        mk = ms[k]
        need = required_j(mk, z)
        have = v3(mk + 1)
        rows.append((k, mk, Ss[k], have, need, have >= need if need is not None else False))
    return N, rows

if __name__ == "__main__":
    records = [27,703,10087,35655,270271,362343,381727,626331,
               1027431,1126015,8088063,13421671,20638335,26716671,56924955,63728127]
    print(f"{'z':>10} {'N':>4} {'k':>4} {'m_k':>14} {'S_k':>5} {'v3(m_k+1)':>10} {'j needed':>9} {'ok':>4}")
    total_expected = 0.0
    total_success = 0
    total_rows = 0
    for z in records:
        N, rows = analyse(z)
        for (k, mk, Sk, have, need, ok) in rows:
            if k == 0: continue          # trivial: m_0 = z itself
            total_rows += 1
            if ok: total_success += 1
            if need is not None: total_expected += 3.0 ** (-need)
            print(f"{z:10d} {N:4d} {k:4d} {mk:14d} {Sk:5d} {have:10d} {need:9d} {str(ok):>4}")
    print()
    print(f"ladder times examined (k>=1): {total_rows}")
    print(f"successful round trips observed: {total_success}")
    print(f"HEURISTIC baseline E[#successes] = sum 3^(-j_needed) = {total_expected:.6g}")
