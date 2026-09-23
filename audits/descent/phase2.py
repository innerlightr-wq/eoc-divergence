"""Phase 2 controls. Each MUST fail, and the failure point must be identifiable."""
from phase1 import v2, v3

# ---------- C1: 2-adic ----------
def c1(k=64):
    M = 1 << k
    inv3 = pow(3, -1, M)
    back = lambda x: ((2*x - 1) * inv3) % M
    # totality: defined for every residue
    total = all(isinstance(back(x), int) for x in range(0, 2000))
    # fixed point of the backward map
    fixed = [x for x in range(M-3, M) if back(x) == x]
    # -1 is the fixed point
    minus1 = M - 1
    return total, back(minus1) == minus1, fixed

# ---------- C2: negative integers ----------
def acc_step(m):
    t = 3*m + 1
    d = v2(abs(t)) if t != 0 else None
    return t >> d, d           # exact: t is divisible by 2^d

def conf_depth_signed(m, cap=200):
    S = 0; p3 = 1; x = m
    for j in range(1, cap+1):
        t = 3*x + 1
        if t == 0: return cap  # -1/3 never occurs for odd integers
        d = v2(abs(t)); S += d; p3 *= 3
        if (1 << S) > p3: return j - 1
        x = t >> d
    return cap

def c2():
    out = {}
    out['back(-1)'] = (2*(-1) - 1)//3
    out['depth(-1)'] = conf_depth_signed(-1)
    out['orbit(-5)'] = [(-5)] + [None]
    x = -5; orb = [x]
    for _ in range(6):
        t = 3*x + 1; d = v2(abs(t)); x = t >> d; orb.append(x)
    out['orbit(-5)'] = orb
    out['depth(-5)'] = conf_depth_signed(-5)
    out['depth(-7)'] = conf_depth_signed(-7)
    out['v3(-5+1)'] = v3(-4) if -4 % 3 != 0 else v3(abs(-4))
    out['-5 mod 3'] = (-5) % 3
    return out

# ---------- C3: 3x-1 on positive integers ----------
def Tm(m):
    t = 3*m - 1
    return t >> v2(t)

def conf_depth_minus(m, cap=200):
    S = 0; p3 = 1; x = m
    for j in range(1, cap+1):
        t = 3*x - 1
        d = v2(t); S += d; p3 *= 3
        if (1 << S) > p3: return j - 1
        x = t >> d
    return cap

def c3_chain(limit=2000001):
    """mirrored chain law: backward d=1 preimage p=(2m+1)/3, chain length = v3(x-1)"""
    bad = 0; tested = 0
    for x in range(3, limit, 2):
        if x % 3 != 1: continue     # need 3 | 2x+1
        tested += 1
        expected = v3(x - 1)
        y = x; steps = 0
        while y % 3 == 1 and y != 1:
            y = (2*y + 1)//3
            steps += 1
            if y % 2 != 1: bad += 1; break
            if steps > expected + 2: break
        if steps != expected: bad += 1; continue
        y = x
        for j in range(1, expected+1):
            y = (2*y + 1)//3
            if (y - 1) * 3**j != 2**j * (x - 1): bad += 1; break
    return tested, bad

if __name__ == "__main__":
    print("=== C1: 2-adic ===")
    total, fixok, fixed = c1()
    print(f"backward map total on Z/2^64: {total}")
    print(f"-1 (= 2^64-1) is a fixed point: {fixok}; fixed points near top: {fixed}")
    print("v3(x+1) at x = -1 is v3(0) = infinite  -> unlimited backward budget")

    print("\n=== C2: negative integers ===")
    for k, v in c2().items(): print(f"  {k} = {v}")

    print("\n=== C3: 3x-1 on positive integers ===")
    print(f"T'(1) = {Tm(1)}  (fixed point)")
    print(f"conf_depth_minus(1) = {conf_depth_minus(1)} (capped) -> 1 is zero-confined forever")
    print(f"backward preimage of 1: (2*1+1)/3 = {(2*1+1)//3}   -> p = m, NOT p < m")
    t,b = c3_chain(); print(f"mirrored chain law (x < 2e6, x = 1 mod 3): tested {t}, failures {b}")
    print(f"fixed point of y=(2x+1)/3 : x = 1  (positive!)   v3(1-1)=v3(0)= infinite")
    print(f"fixed point of y=(2x-1)/3 : x = -1 (not positive) v3(-1+1)=v3(0)= infinite")
