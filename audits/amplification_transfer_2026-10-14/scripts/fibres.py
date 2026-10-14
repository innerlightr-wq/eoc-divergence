"""Instantiate (AMP*) with the real down-shift transformation and measure its
index-set growth against its fibre growth.  Exact integer arithmetic.

Down-shift Phi:  index set
    I_N = { (P, e, e', t) : P||e'||t is 0-confined, e < e', both children of P }
    Phi(P,e,e',t) = P||e||t .
Decreasing a digit decreases every later partial sum, so Phi(I_N) ⊆ C_N always
(no defect at all -- verified, rate 1.0000).  (AMP*) would fire if
#I_N >= 2^{(g+delta)N} with all fibres <= 2^{o(N)}.
"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


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


print(f"{'N':>3} {'n_N':>8} {'#I_N':>10} {'I_N/n_N':>9} {'log2 n/N':>9} "
      f"{'log2 I/N':>9} {'delta':>7} {'maxfib':>8} {'log2 maxfib/N':>14} {'meanfib':>9}")
prev = None
for N in range(3, 15):
    W_ = confwords(N)
    S = set(W_)
    kids = {}
    for w in W_:
        for j in range(N):
            kids.setdefault(w[:j], set()).add(w[j])
    suf = {}
    for w in W_:
        for j in range(N):
            suf.setdefault((w[:j], w[j]), []).append(w[j+1:])
    fib = {}
    nI = 0
    for P, ds in kids.items():
        ds = sorted(ds)
        if len(ds) < 2:
            continue
        for a in range(len(ds)):
            for b in range(a+1, len(ds)):
                e, ep = ds[a], ds[b]
                for t in suf[(P, ep)]:
                    y = P + (e,) + t
                    assert y in S, "down-shift left the confined set"
                    nI += 1
                    fib[y] = fib.get(y, 0) + 1
    n = len(W_)
    mx = max(fib.values()) if fib else 0
    mean = nI / len(fib) if fib else float('nan')
    print(f"{N:>3} {n:>8} {nI:>10} {nI/n:>9.3f} {math.log2(n)/N:>9.5f} "
          f"{(math.log2(nI)/N if nI else 0):>9.5f} "
          f"{((math.log2(nI)-math.log2(n))/N if nI else 0):>7.5f} {mx:>8} "
          f"{(math.log2(mx)/N if mx else 0):>14.5f} {mean:>9.3f}")

print()
print("READ-OFF:  delta = (log2 #I_N - log2 n_N)/N  is the index-set surplus per step,")
print("and log2(maxfib)/N is the fibre cost per step.  (AMP*) needs the first")
print("positive and the second -> 0.  They are the SAME number here, identically:")
print("   #I_N = sum over y of fibre(y)  <=  n_N * maxfib ,  so  delta <= log2(maxfib)/N .")
print("That inequality is an identity of the counting, not a property of Collatz.")
