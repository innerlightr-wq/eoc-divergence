"""Task 1.3: test the claimed height bound |c_w| <= l * max(2^l, 3^k)."""
from conj import c_w_and_den, mech
import random, math

def ratio(w):
    c, den, l, k = c_w_and_den(w)
    return abs(c) / (l * max(1 << l, 3 ** k)), c, l, k

print("=== explicit candidate counterexample  w = 0^10 1^10 ===")
w = [0]*10 + [1]*10
r, c, l, k = ratio(w)
print(f"  c_w = {c},  l*max(2^l,3^k) = {l*max(1<<l,3**k)},  ratio = {r:.3f}  -> "
      f"{'BOUND HOLDS' if r <= 1 else 'BOUND FAILS'}")

print("\n=== worst ratio over all words of each length (exhaustive, l <= 18) ===")
print(f"{'l':>3} {'worst ratio':>12} {'witness':>20}")
for l in range(1, 19):
    worst = 0.0; wit = None
    for mask in range(1, 1 << l):
        w = [(mask >> i) & 1 for i in range(l)]
        r, *_ = ratio(w)
        if r > worst: worst, wit = r, ''.join(map(str, w))
    print(f"{l:3d} {worst:12.3f} {wit:>20}")

print("\n=== mechanical (characteristic) words: ratio for many slopes p/q ===")
worst = 0.0; wit = None
for q in range(2, 400):
    for p in range(1, q):
        if math.gcd(p, q) != 1: continue
        f = mech(p, q)
        w = [f(j) for j in range(q)]
        r, c, l, k = ratio(w)
        if r > worst: worst, wit = r, (p, q, r)
print(f"  worst ratio over all Christoffel words with q < 400: {worst:.4f}   at (p,q)={wit[:2]}")
print(f"  -> bound {'HOLDS' if worst <= 1 else 'FAILS'} on mechanical words in this range")
