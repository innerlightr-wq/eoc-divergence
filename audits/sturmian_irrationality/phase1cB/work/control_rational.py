"""Control 1 (corrected): a rational slope.  The word is periodic, the value is
rational, and we locate exactly where the argument stops."""
from fractions import Fraction
from slopes import *
from liouville import *

def ceil_div(m, d):  return -((-m) // d)

def one_c_rational(num, den, L):
    """1c_{p/q}(j) = ceil((j+1)p/q) - ceil(j p/q)."""
    return bytes(ceil_div((j + 1) * num, den) - ceil_div(j * num, den) for j in range(L))

for (num, den) in [(5, 8), (2, 3), (41, 65)]:
    L = 8 * den
    w1c = one_c_rational(num, den, L)
    wmec = bytes(word_from_positions(mech_ones(num, den, 8 * num + 1), L))
    print(f"\ngamma = {num}/{den}")
    print(f"  1c_gamma == w_({num},{den})^infty over {L} letters : {w1c == wmec}")
    val = phi_periodic(list(w1c[:den]))
    print(f"  Phi(1c_gamma) = {val}   H = {max(abs(val.numerator), val.denominator)}")

# where the argument stops, quantitatively, for gamma = 5/8 = [0;1,1,1,2]
a = [1, 1, 1, 2]
p, q = convergents(a)
print(f"\ngamma = 5/8 = [0;1,1,1,2] : convergents "
      f"{[f'{p[i]}/{q[i]}' for i in range(len(q))]}")
val = Fraction(319, 13); H = 319
print(f"  Phi(1c_(5/8)) = {val}, H = {H}, log2 H = {H.bit_length()-1}.x")
for n in (1, 3):
    reg, H0 = height_floor(p[n], q[n], q[n + 1])
    print(f"  odd n={n}: p/q={p[n]}/{q[n]}, depth q_n+q_(n+1)-1={q[n]+q[n+1]-1}, "
          f"regime {reg}, forced H > {H0}  -> actual H={H}: "
          f"{'consistent (no contradiction)' if H > H0 else 'VIOLATED'}")
print("  n=4 is the LAST convergent and is even; there is no odd n>=5.")
print("  At n=4 the word 1c_(5/8) equals w_4^infty, so the lcp is infinite,")
print("  M_4 = u*delta_4 - v*c_4 = 0, and the lower bound |M_n| >= 2^depth is vacuous.")
d4 = (1 << q[4]) - 3 ** p[4]
c4 = c_word(list(word_from_positions(mech_ones(p[4], q[4], p[4] + 1), q[4])))
print(f"  check: u*delta_4 - v*c_4 = {val.numerator}*{d4} - {val.denominator}*{c4} "
      f"= {val.numerator * d4 - val.denominator * c4}")
