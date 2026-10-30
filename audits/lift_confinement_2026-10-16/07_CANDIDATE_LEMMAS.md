# 07_CANDIDATE_LEMMAS.md

## Proved

**L1 (base-2 reading).** `x = −Σ_{j≥0}3^{−(j+1)}2^{S_j} ∈ ℤ₂` and `b_n = (x >> S_n) mod 2^{d_n}`.
Status: **PROVED**, and **ALREADY KNOWN in substance** — it makes Proposition R a triviality.

**L2 (lift criterion).** `b_n = 0 ⟺ 2^{d_n} | 3m_n+1`, and `b_n ≡ −(3m_n+1)3^{−(n+1)} (mod 2^{d_n})`,
where `m_n = (3^n r_n + C_n)/2^{S_n}`.  **PROVED**; 7 100 positions, 0 failures.
*Assessment:* correct, exact, and the most clarifying statement here — but it follows in three
lines from the carry recurrence, so by the brief's own standard it is a **definition made
explicit**, not a new theorem.

**L3′ (parity control).** `m_n` even ⟹ `b_n ≠ 0`; `m_n` odd and `d_n = 1` ⟹ `b_n = 0`.
**PROVED**; 18 010 positions, 0 failures.

**L4 (both extremes are confined).** `min J(N) = 3` for `N = 6..13` (realizer `71`) and
`max J(N) = N−1` (all-ones word, `x = −1`), on complete enumerations.
**PROVED as a finite statement**; it is the counterexample to every density bound below.

## Disproved

**L3 (withdrawn).** "`m_n` is always odd, hence `d_n = 1 ⟹ b_n = 0`, hence `J(N) ≤ S_N − N`."
**FALSE.**  `m_n` even at 4 914/8 480 positions; minimal counterexample `d=[1]`, `n=0`,
`r_0=0`, `m_0=0`, `b_0=1`.  All three statements withdrawn.

**Slack effect.** `P(lift)` depends on `G_n` only through continuation-count weighting; after
the correct control it matches `1−2^{−d_n}` to `±0.021`.  **DISPROVED as an effect.**

## Targets A–D

**Target A — confined lift-density lower bound.  VERDICT E (obstructed), and circular.**

*Obstructed:* `min J(N) = 3` for every `N = 6..13` on complete enumerations, so no lower bound
growing with `N` holds over confined words of length `N`.

*Circular:* suppose one proved `J(∞) = ∞` for every infinite zero-confined word.  By
Proposition R that says exactly that **no infinite zero-confined word has a nonnegative-integer
realizer** — which, since infinite confinement forces `m_n > m_0` for all `n`, is precisely the
statement that no positive integer has a zero-confined divergent-type orbit.  **Target A is the
open problem, not a step toward it.**

**Target B — plateau obstruction.  VERDICT E.**  The all-ones word has plateau 0 but never
stabilises; the `71`-words have plateau `N−5` and do stabilise.  Plateau length and
realizability are not related in the direction needed, and confinement bounds neither.

**Target C — episode–lift connection.  NOT REACHED.**  `06_...` records why: with `J`
unconstrained by confinement in either direction, there is no lift-side quantity for an episode
inequality to bound.  I did not construct one and do not claim one is impossible — only that
nothing here motivates it.

**Target D — pointwise conditional theorem.  NOT OBTAINED.**  Every hypothesis I could form
about the lift sequence is either a consequence of the carry recurrence (L1, L2, L3′) or is
Target A in disguise.

## Honest summary of what is new

Three exact statements (L1, L2, L3′) that make the realizer dynamics explicit and, in L2's case,
genuinely easier to think about; one finite counterexample pair (L4) that **forecloses the entire
lift-density programme**; and a proof that Target A is circular.  **No new inequality, and no new
arithmetic restriction.**
