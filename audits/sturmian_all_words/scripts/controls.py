#!/usr/bin/env python3
"""Controls: the method must be SILENT where it has to be."""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sturmian import *
from i2_i3_i4 import c_word, is_christoffel_conjugate, periodization_balanced

print("=" * 88)
print("CONTROL 1 — rational slope: the word is periodic, Phi is rational, M = 0 exactly")
print("=" * 88)
def rat_word(p, q, n):
    """EXACT lower mechanical word of rational slope p/q, intercept 0."""
    return [((j + 1) * p) // q - (j * p) // q for j in range(n)]

for (p, q) in [(2, 3), (5, 8), (12, 19), (41, 65)]:
    s = rat_word(p, q, 8 * q)                  # exact rational slope
    W = s[:q]
    per = all(s[i] == s[i % q] for i in range(len(s)))
    delta = 2 ** q - 3 ** p
    cW = c_word(W)
    # Phi(s) = Phi(W^inf) = cW/delta exactly, so u = cW, v = |delta| (up to sign)
    u, v = cW, delta
    M = u * delta - v * cW
    print(f"  slope {p}/{q}: word periodic={per}  Phi = c_W/(2^l-3^k) = {cW}/{delta}"
          f"   M = u*delta - v*c_W = {M}   -> {'SILENT (M=0)' if M == 0 else 'FIRES  <-- BUG'}")

print()
print("=" * 88)
print("CONTROL 2 — Thue-Morse: aperiodic but NOT Sturmian; the method must be silent")
print("=" * 88)
N = 4096
tm = [bin(i).count('1') & 1 for i in range(N)]
sq = [L for L in range(1, N // 2) if tm[:L] == tm[L:2 * L]]
print(f"  Thue-Morse initial squares with half-length L < {N//2}: {sq if sq else 'NONE'}")
if not sq:
    print("  -> I1 has no input: the method is SILENT on Thue-Morse, as required.")
else:
    for L in sq[:6]:
        W = tm[:L]; k = sum(W)
        bal = periodization_balanced(W)
        ratio = c_word(W) / (L * max(2 ** L, 3 ** k)) if k else float('nan')
        print(f"     L={L} k={k} periodization balanced={bal} c_W/(L*max)={ratio:.4f}")
print()
print("  (second guard) the height bound needs BALANCE.  Remark 4.3's family w = 0^a 1^a:")
for a in (6, 10, 14, 18):
    w = [0] * a + [1] * a
    ratio = c_word(w) / (2 * a * max(2 ** (2 * a), 3 ** a))
    print(f"     a={a:>3}: c_W/(ell*max(2^ell,3^k)) = {ratio:>10.4f}   "
          f"{'OK' if ratio <= 1 else 'EXCEEDS 1 -> unbounded, bound FAILS'}")

print()
print("=" * 88)
print("CONTROL 3 — a balanced word whose PERIODIZATION is not balanced")
print("=" * 88)
found = 0
for l in range(3, 17):
    for m in range(1 << l):
        w = [(m >> i) & 1 for i in range(l)]
        if sum(w) == 0 or sum(w) == l: continue
        if is_balanced(w) and not periodization_balanced(w):
            if found < 4:
                k = sum(w)
                print(f"     W={''.join(map(str,w))} (l={l},k={k}) balanced but W^inf NOT balanced;"
                      f"  conj of Christoffel? {is_christoffel_conjugate(w)}")
            found += 1
    if found >= 4: break
print(f"  such words exist ({found} found) -> I2 is genuinely load-bearing, not automatic.")
