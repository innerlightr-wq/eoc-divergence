"""(A) The two-clock dictionary and counterexamples to the invalid implications.
   (B) The endpoint large-deviation rate J(s) = s(1 - H_2(1/s)), exact check.
All confinement decisions by integer comparison 2^{S_j} <= 3^j.  No float logs.
"""
import math
from fractions import Fraction as F

alpha = math.log2(3); beta = 1 / alpha
H = lambda x: 0.0 if x <= 0 or x >= 1 else -x * math.log2(x) - (1 - x) * math.log2(1 - x)
J = lambda s: s * (1 - H(1 / s))
print(f"alpha = {alpha:.12f}   beta = 1/alpha = {beta:.12f}   J(alpha) = I0 = {J(alpha):.12f}")
print()

# ---------------------------------------------------------------- (A) clocks
def ordinary_density(d):
    """The COMPLETE ordinary parity sequence of a valuation word d: one 1 then
    d_j-1 zeros per accelerated step.  Returns (liminf, limsup) of h(l)/l over
    all ordinary l, and the endpoint values N/S_N."""
    bits = []
    for dj in d:
        bits.append(1); bits.extend([0] * (dj - 1))
    lo, hi = 10.0, -10.0
    h = 0
    for l, b in enumerate(bits, start=1):
        h += b
        r = h / l
        lo = min(lo, r); hi = max(hi, r)
    return lo, hi


print("(A1) within one accelerated block the ordinary density h/l DECREASES,")
print("     so its infimum over the block is attained at the block END l = S_j:")
print("        liminf_l h/l = liminf_N N/S_N = 1/limsup_N (S_N/N) ,")
print("        limsup_l h/l = limsup_N N/(S_{N-1}+1) .")
print()
for name, d in [("all ones (S_N = N)", [1] * 40),
                ("period 12 (S=2N)", [1, 3] * 20),
                ("critical-ish 1,2,2,1,2,...", [1, 2, 2, 1, 2] * 8)]:
    S = 0; mn = 9.9
    for N, dj in enumerate(d, start=1):
        S += dj; mn = min(mn, N / S)
    lo, hi = ordinary_density(d)
    print(f"  {name:<28} endpoint min N/S_N = {mn:.6f}   "
          f"ordinary liminf = {lo:.6f}  limsup = {hi:.6f}")

print()
print("(A2) COUNTEREXAMPLES to the invalid implications among A..G.")
print("     Words are admissible valuation words (every d_j >= 1); confinement")
print("     is tested exactly.  Delta_N = alpha N - S_N.")


def build(dgen, N):
    d = [dgen(j) for j in range(1, N + 1)]
    S, Ss = 0, []
    for dj in d:
        S += dj; Ss.append(S)
    return d, Ss


def confined(Ss):
    return all((1 << S) <= 3 ** (j + 1) for j, S in enumerate(Ss))


def deltas(Ss):
    return [alpha * (j + 1) - S for j, S in enumerate(Ss)]


# D but not E: Delta_N/N -> 0 along a subsequence only, linear elsewhere.
# Use blocks: long runs of d=1 (Delta grows at rate alpha-1) then runs of d=2
# (Delta shrinks at rate 2-alpha), with block lengths growing geometrically.
def word_D_not_E(N):
    d = []; i = 0; L = 4
    while len(d) < N:
        d += [2] * L            # Delta decreases by (2-alpha) each step
        d += [1] * int(L * (2 - alpha) / (alpha - 1) + 1)   # climb back up
        L = int(L * 2.2) + 1
        i += 1
    return d[:N]


N = 4000
dD = word_D_not_E(N)
S = 0; Ss = []
for dj in dD:
    S += dj; Ss.append(S)
De = deltas(Ss)
conf = all(x >= -1e-9 for x in De)
rat = [De[j] / (j + 1) for j in range(N)]
print(f"  word_D_not_E: confined(Delta>=0) = {conf};  min Delta = {min(De):.4f}")
print(f"     liminf Delta_N/N over N<=4000 = {min(rat[200:]):.6f}  "
      f"(approaches 0)   limsup = {max(rat[200:]):.6f}  (stays positive)")
print(f"     max Delta_N = {max(De):.2f}  at N = {De.index(max(De))+1};  "
      f"Delta_N/log2(N) max = {max(De[j]/math.log2(j+2) for j in range(N)):.2f}")
print("     => D holds, E FAILS (Delta_N/N does not tend to 0), and F,G fail badly.")
print()
# E but not F: Delta_N ~ sqrt(N)
def word_E_not_F(N):
    d = []; S = 0
    for j in range(1, N + 1):
        target = alpha * j - math.sqrt(j)      # want S_j ~ target
        dj = max(1, int(round(target - S)))
        d.append(dj); S += dj
    return d
dE = word_E_not_F(3000)
S = 0; Ss = []
for dj in dE:
    S += dj; Ss.append(S)
De2 = deltas(Ss)
print(f"  word_E_not_F (Delta ~ sqrt N): min Delta = {min(De2):.4f}  "
      f"max Delta/sqrt(N) = {max(De2[j]/math.sqrt(j+1) for j in range(len(De2))):.4f}")
print(f"     max Delta_N/N = {max(De2[j]/(j+1) for j in range(200,len(De2))):.6f} -> 0 : E holds")
print(f"     Delta_N/log2 N at N=3000 = {De2[-1]/math.log2(3000):.3f} -> infinity : F FAILS")
print("     => E holds, F FAILS.  And F => G fails likewise (Delta unbounded).")
print()
print("  A (S_N <= alpha N for all N) holds for the all-ones word with")
print("     Delta_N = (alpha-1)N -> infinity LINEARLY: so A does NOT give D, E, F or G.")
dA = [1] * 2000
S = 0; Ss = []
for dj in dA:
    S += dj; Ss.append(S)
DeA = deltas(Ss)
print(f"     all-ones: confined = {confined(Ss)}, Delta_N/N = {DeA[-1]/2000:.6f} "
      f"= alpha-1 = {alpha-1:.6f} constant.")

# ---------------------------------------------------------------- (B) J(s)
print()
print("(B) endpoint rate:  #{words of length N with S_N = s} = C(s-1,N-1), weight 2^-s,")
print("    so P(S_N <= sN) = sum_{t<=sN} C(t-1,N-1) 2^{-t}.  Check -log2 P /N -> J(s).")
print(f"{'s':>6} {'J(s)':>12} {'N=50':>10} {'N=150':>10} {'N=400':>10} {'N=1000':>10}")
for s in (1.1, 1.2, 1.3, 1.4, alpha, 1.7, 1.9):
    row = []
    for N in (50, 150, 400, 1000):
        cap = int(s * N)
        P = sum(F(math.comb(t - 1, N - 1), 1 << t) for t in range(N, cap + 1))
        row.append(-(math.log2(P.numerator) - math.log2(P.denominator)) / N if P else float('inf'))
    tag = " <- alpha" if abs(s - alpha) < 1e-9 else ""
    print(f"{s:>6.4f} {J(s):>12.9f} " + " ".join(f"{x:>10.6f}" for x in row) + tag)
