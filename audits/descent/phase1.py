"""Phase 1: exact verification of the inheritance lemmas L1-L4.
All arithmetic is exact integer arithmetic; no floats enter any decision."""
import sys
from math import gcd

def v2(n):
    c = 0
    while n % 2 == 0:
        n //= 2; c += 1
    return c

def v3(n):
    if n == 0: return None  # infinite
    c = 0
    while n % 3 == 0:
        n //= 3; c += 1
    return c

def T(m):
    x = 3*m + 1
    return x >> v2(x)

def conf_depth(m, cap=200):
    """max N with 2^{S_j} <= 3^j for all 1<=j<=N (0 if it fails at j=1)."""
    S = 0; p3 = 1; x = m
    for j in range(1, cap+1):
        t = 3*x + 1
        d = v2(t)
        S += d; p3 *= 3
        if (1 << S) > p3:
            return j - 1
        x = t >> d
    return cap

# ---------- L1 ----------
def check_L1(limit):
    bad = 0; tested = 0
    for m in range(3, limit, 2):
        if m % 3 != 2: continue
        N = conf_depth(m)
        if N == 0: continue
        tested += 1
        p = (2*m - 1)//3
        assert (2*m - 1) % 3 == 0
        if p % 2 != 1: bad += 1; continue
        if not (p < m): bad += 1; continue
        t = 3*p + 1
        if v2(t) != 1 or (t >> 1) != m: bad += 1; continue
        if conf_depth(p) < N + 1: bad += 1; continue
    return tested, bad

# ---------- L2 ----------
def check_L2(limit):
    bad = 0; tested = 0
    for x in range(3, limit, 2):
        if x % 3 != 2: continue
        tested += 1
        expected = v3(x + 1)
        # walk the backward d=1 chain
        y = x; steps = 0
        while y % 3 == 2:
            y = (2*y - 1)//3
            steps += 1
            if y % 2 != 1: bad += 1; break
        if steps != expected: bad += 1; continue
        # closed form after j steps
        y = x
        for j in range(1, expected+1):
            y = (2*y - 1)//3
            if (y + 1) * 3**j != 2**j * (x + 1): bad += 1; break
    return tested, bad

# ---------- L3 ----------
def check_L3(limit, dmax=12):
    bad = 0; tested = 0
    for m in range(3, limit, 2):
        for d in range(2, dmax+1):
            num = (1 << d) * m - 1
            if num % 3 != 0: continue
            p = num // 3
            if p % 2 != 1 or p <= 0: continue
            tested += 1
            t = 3*p + 1
            if v2(t) != d or (t >> d) != m:
                bad += 1; continue
            # d>=2 must break confinement at the first step
            if conf_depth(p) != 0: bad += 1
    return tested, bad

# ---------- L4 ----------
def rmin_table(limit, cap=200):
    best = {}
    for m in range(1, limit, 2):
        N = conf_depth(m, cap)
        for k in range(1, N+1):
            if k not in best:
                best[k] = m
    return best

if __name__ == "__main__":
    L = int(sys.argv[1]) if len(sys.argv) > 1 else 200001
    print(f"# range: odd m < {L}")
    t,b = check_L1(L);  print(f"L1: tested {t}, failures {b}")
    t,b = check_L2(L);  print(f"L2: tested {t}, failures {b}")
    t,b = check_L3(min(L, 20001)); print(f"L3: tested {t}, failures {b}")
