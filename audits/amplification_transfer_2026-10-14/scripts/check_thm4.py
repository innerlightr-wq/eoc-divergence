"""Audit the claimed fibre bound of Theorem 4 against the exact fibres."""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
alpha = math.log2(3)

def sNj(j): return (3 ** j).bit_length() - 1

def confwords(N):
    out = []
    def rec(w, S, j):
        if j == N:
            out.append(tuple(w)); return
        p3 = 3 ** (j + 1)
        d = 1
        while (1 << (S + d)) <= p3:
            w.append(d); rec(w, S + d, j + 1); w.pop()
            d += 1
    rec([], 0, 0)
    return out

for N in (10, 12, 14):
    W_ = confwords(N); S = set(W_)
    fib = {}
    for y in W_:
        c = 0
        for j in range(N):                       # 0-indexed position
            P = y[:j]; t = y[j+1:]
            # admissible e' > y[j] with P||e'||t 0-confined
            e = y[j]
            ep = e + 1
            while True:
                cand = P + (ep,) + t
                # the local constraint alone caps ep: 2^{S_j + ep} <= 3^{j+1}
                if sum(P) + ep > sNj(j+1):
                    break
                if cand in S:
                    c += 1
                ep += 1
        fib[y] = c
    mx = max(fib.values()); arg = max(fib, key=fib.get)
    # the two candidate bounds
    loc = sum(sNj(j+1) - sum(arg[:j+1]) for j in range(N))        # local constraint only
    thm = (alpha - 1) * N * (N + 1) / 2
    print(f"N={N}: measured max fibre = {mx}  (argmax {arg})")
    print(f"        sum_j (sN(j+1) - S_j) at the argmax, local constraint only = {loc}")
    print(f"        claimed (alpha-1)N(N+1)/2 = {thm:.2f}")
    print(f"        max over all y of the local sum = "
          f"{max(sum(sNj(j+1)-sum(y[:j+1]) for j in range(N)) for y in W_)}")
    print()
