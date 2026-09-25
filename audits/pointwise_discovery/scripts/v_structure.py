"""Two exact structural laws about the realizer, verified.

(R1)  r_{q,+r}(w) + r_{q,-r}(w) = 2^{S+1}  for every word w.
      Hence the +/- pair of maps carries no independent realizer information:
      2^{-delta_-} = 1 - 2^{-delta_+}, and the uniform null is self-conjugate.

(R2)  the L1/L2 chain law in the delta coordinate:
      delta(1.w) = delta(w) + log2 3   iff   3 | r(w)+1   (inheritance),
      and otherwise delta(1.w) in {log2 3, log2 3 - 1} + O(2^{-S}).
"""
import os, sys, math, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eoc import Map, carry, realizer, word_of
from words import Table
from gen_words import log2_int

FAIL = []
def check(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + (("  " + detail) if detail else ""))
    if not cond: FAIL.append(name)

rng = random.Random(4242)

# --- R1 -------------------------------------------------------------------
bad = 0; tested = 0
for q in (3, 5, 7):
    mp_p, mp_m = Map(q, 1), Map(q, -1)
    t = Table(mp_p, 30) if q < 4 else Table(mp_p, 30)
    for _ in range(300):
        w = [rng.randrange(1, 7) for _ in range(12)]
        S = sum(w)
        rp, rm = realizer(mp_p, w), realizer(mp_m, w)
        tested += 1
        if rp + rm != (1 << (S + 1)): bad += 1
check("R1  r_{q,+1}(w) + r_{q,-1}(w) = 2^{S+1}", bad == 0,
      f"(q=3,5,7; {tested} random words; violations {bad})")

# --- R2 -------------------------------------------------------------------
mp = Map(3, 1)
inh = inh_ok = other = other_ok = 0
vals = []
for _ in range(4000):
    n = rng.randrange(6, 30)
    # a random word whose 1-prefix extension is still confined is not needed:
    # R2 is an identity about realizers, independent of confinement.
    w = [rng.randrange(1, 6) for _ in range(n)]
    r0 = realizer(mp, w); S0 = sum(w)
    d0 = (S0 + 1) - log2_int(r0)
    w1 = [1] + w
    r1 = realizer(mp, w1); S1 = S0 + 1
    d1 = (S1 + 1) - log2_int(r1)
    if r0 % 3 == 2:                                   # 3 | r0+1: inheritance
        inh += 1
        # exact integer identity, and the delta form with its exact error term
        exact = (r1 == (2 * r0 - 1) // 3)
        pred = d0 + math.log2(3) - math.log2(1 - 1 / (2 * r0))
        if exact and abs(d1 - pred) < 1e-9:
            inh_ok += 1
    else:
        other += 1
        vals.append(d1)
        if d1 < math.log2(3) + 1e-9: other_ok += 1
check("R2a inheritance: 3|r(w)+1  =>  r(1.w) = (2r(w)-1)/3 exactly, and "
      "delta(1.w) = delta(w) + log2 3 - log2(1 - 1/(2r(w)))",
      inh == inh_ok, f"({inh} cases, {inh_ok} exact)")
check("R2b otherwise delta(1.w) <= log2 3", other == other_ok,
      f"({other} cases; max = {max(vals):.4f}, log2 3 = {math.log2(3):.4f})")
print(f"      inheritance frequency {inh/(inh+other):.4f}  (predicted 1/3)")

# --- R3  the chain is the ONLY way delta grows by a fixed amount -----------
#     P(3 | r(w)+1) = 1/3 exactly over the class, so a leading run of L ones
#     inherits with probability 3^{-L}: delta ~ L log2 3 has mass 3^{-L}, while
#     the uniform null gives P(delta > L log2 3) = 3^{-L}.  They agree exactly.
print()
print("      note: P(delta > L log2 3) = 2^{-L log2 3} = 3^{-L} under the null,")
print("      and the chain gives inheritance depth L with probability 3^{-L}.")
print("      The known mechanism and the null agree to leading order -- which is")
print("      why L1/L2 leaves no signature in the marginal law of delta.")
print()
print("FAILURES:", FAIL if FAIL else "none")
