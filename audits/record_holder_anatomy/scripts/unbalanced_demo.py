"""Correction 2, examined: what actually fails for an UNBALANCED initial square.

The least positive integer realizing a parity word w of length L is
    x = (-c_L * 3^{-k_L}) mod 2^L                (paper Prop. 2.2's computation),
where c_L, k_L are as in eq. (2.1).  Taking w = (1 0^a 1^a)^2 gives an initial square
whose block is badly unbalanced, and the ceiling l <= (log2 m + O(log l))/(2 - theta_W)
-- which is proved only for balanced blocks -- loses its input.

The honest finding, stated up front: the INPUT fails (c_W exceeds 3l*max(2^l,3^k) by a
growing factor), while the CONCLUSION happens to survive on these words, because their
least realizers are of size ~2^L and the ceiling is then satisfied for trivial reasons.
Correction 2 is therefore about the derivation being unproved off the balanced class,
not about an observed violation.  No violation, balanced or unbalanced, was found.
"""
from fractions import Fraction
from anatomy import c_of, delta_of, discrepancy, parity_word, v2

def least_realizer_of_parity_word(w):
    L = len(w); k = sum(w)
    c = 0
    for i, b in enumerate(w):                      # c_L = sum_{i<L, w_i=1} 3^{k_L-k_{i+1}} 2^i
        pass
    c = c_of(w)                                    # same formula
    M = 1 << L
    return (-c * pow(pow(3, k, M), -1, M)) % M

print(f"{'a':>3} {'l=|W|':>6} {'k':>4} {'disc(W)':>9} {'bal':>5} {'c_W/(3l*max)':>13} "
      f"{'log2 m':>7} {'R':>4} {'ceiling':>8} {'holds?':>7} {'v2(M)=R':>8}")
import math
for a in (2, 4, 6, 8, 10, 12, 16, 20, 24):
    W = bytes([1] + [0]*a + [1]*a)
    w = W + W
    m = least_realizer_of_parity_word(w)
    if m % 2 == 0: m += 1 << len(w)                 # must be odd; w starts with 1 so it is
    got = parity_word(m, len(w))
    assert got == w, "realizer does not reproduce the word"
    l = len(W); k = sum(W)
    c = c_of(W); d = delta_of(W)
    M = m * d - c
    # R = agreement length of the word of m with W^inf
    long = parity_word(m, 8*l)
    R = l
    while R < len(long) and long[R] == long[R-l]: R += 1
    th = float(Fraction(k, l)) * math.log2(3)
    ceil = (math.log2(m) + math.log2(1+3*l) + math.log2(3)) / (2 - max(1.0, th))
    ratio = Fraction(c, 3*l*max(1 << l, 3**k))
    print(f"{a:>3} {l:>6} {k:>4} {str(discrepancy(W))[:9]:>9} {str(discrepancy(W)<1):>5} "
          f"{float(ratio):>13.3f} {m.bit_length()-1:>7} {R:>4} {ceil:>8.2f} "
          f"{str(R <= ceil):>7} {str(v2(M) == R):>8}")
print("\nc_W/(3l*max(2^l,3^k)) passes 1 at a = 12 and keeps growing: the balanced height")
print("bound -- the INPUT to the ceiling -- is false for these blocks, unboundedly so.")
print("The ceiling's CONCLUSION nevertheless holds on every row, because the least")
print("realizer of a length-L word is of size ~2^L and R <= L.  So an unbalanced block")
print("could only break the ceiling if it also had an anomalously small realizer; none")
print("was found here or anywhere in Phase 2.  Correction 2 stands as a statement about")
print("what is proved, not about what was observed.")
