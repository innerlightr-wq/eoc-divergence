# 06_FINAL_VERDICT.md

## Verdict: **D — No useful transfer**

The H10/ℚ machinery does not currently supply a new arithmetic constraint on the Collatz
pointwise realizer problem.  The conclusion is **independent of whether the H10 manuscript is
correct**: the obstruction is to the transfer, not to that proof.

## Why, precisely

H10 forces standard-from-nonstandard with three ingredients.  **The Collatz realizer problem has
none of them, and in two cases the analogue is provably false.**

| H10 ingredient | Collatz analogue | status |
|---|---|---|
| one fixed nonzero integer `δ` that every local obstruction divides to order `≥ K` | would be `m₀ − r_n` for a hypothetical integer realizer | **DISPROVED** — no nonzero integer is divisible by `2^{S_n}` for all `n` when `S_n → ∞`; and `m₀` is exactly what is in question (C5) |
| `h(s) ≤ H·M(s)^c`, `M(s)` a product of **many** varying contact primes | would need a second modulus coprime to `2` | **DISPROVED** — the realizer set `{r_N + k·2^{S_N}}` hits every class mod every odd `q` (C4), reconfirming the repository's §4b |
| canonical height `ĥ(nP) ≍ n²`, beating the linear bound | would need a positive-definite quadratic form on the realizer group | **absent** — the structure is the affine reduction `m₀ ↦ m₀ mod 2^{S_n}` on `(ℤ₂,+)`; every available comparison is linear in the exponent |

And there is a prior, independent reason: **H10's divisibility step is exactly the tool the EOC
programme has already proved vacuous on the confined sector.**  Its (2.24)→(2.25) is
"`M^K | δ`, `δ ≠ 0` ⟹ `M^K ≤ |δ|`" — verbatim Rev 8 §5.3's "a nonzero multiple of `2^m` has
absolute value at least `2^m`".  Revision 7 §5.3's meta-theorem then applies before any transfer
is attempted.  Quantitatively (**Lemma O, `[PROVED]`**): zero-confinement *is* `2^{S_n} ≤ 3^n`,
while the generic height is `H ≥ 3^N`, so `2^{S_N}/H − 1 ≤ 0` identically and `ρ_N ≥ 1`.  **The
hypothesis defining the interesting sector is exactly what voids the tool.**

The sharpest way to put it: on the aperiodic confined sector **both horns of the §5.3 dichotomy
fail at once** — there is no periodic collapse to pin `χ` to a rational (horn one), and the size
branch is vacuous (horn two).  Periodic words are decided by horn one, which is why they are not
the hard case.

## Classification of everything produced

| result | class |
|---|---|
| Proposition R (residue characterization, with hypotheses) | **PROVED**, but **ALREADY KNOWN** |
| Lemma O (`ρ_N ≥ 1` forced by confinement; size branch vacuous) | **PROVED**, substantially **ALREADY KNOWN** (Obs. 5.9) |
| no odd-prime constraint on the realizer (C4) | **DISPROVED** (the sought constraint does not exist) |
| fixed-`δ` sink (C5) | **DISPROVED** |
| prefix lower bound beating `r_N` (C6) | **DISPROVED** |
| `C_n` vs `2^{S_n}` inequality (C2), successive residues (C7) | **ALREADY KNOWN** |
| aggregate identity, stabilization on orbits, the Beatty gap, periodic collapse | **COMPUTATIONALLY VERIFIED** |
| transfer of any H10 mechanism | **DISPROVED** for C4/C5; **UNRESOLVED-but-structurally-blocked** for the quadratic height |
| `(DE)`, `(PosPC)`, Sharp EOC, Open Problem C | **UNRESOLVED**, unchanged |

**No conditional theorem is offered.**  Per the brief's §6, a conditional result requires an
additional hypothesis that is not already known and that connects to pointwise realization; every
hypothesis I could extract from H10 is either false here (C4, C5) or is the conclusion itself.

## What the comparison *is* worth

A sharper statement of the gap, which I think is a real if modest gain.  Before: "symbolic
admissibility and 2-adic compatibility do not give integer realizability."  After: *forcing
standard-from-nonstandard is achievable — H10 does it — given a fixed integer sink, a many-prime
height estimate, and a quadratic form; the Collatz realizer problem demonstrably has no sink and
no second prime, and no quadratic form is in sight.*  That converts an open gap into a list of
three specific missing objects, two of which are now known not to exist.

This is **C-grade understanding attached to a D-grade transfer**, and I am reporting it as D
because no theorem improved.

## Three highest-value next steps

Ranked by the brief's criterion — likelihood of a *provable* result rather than another
equivalent formulation.

1. **Find a second prime, or prove none exists.**  Everything upstream failed because the
   problem is supported at the single prime 2.  The precise question: *is there any
   word-measurable function whose value constrains the realizer at an odd prime?*  C4 shows the
   realizer congruence itself does not; §4b shows the 3-adic endpoint does not.  A **theorem
   that no such function exists** would be a genuine negative result, would close the
   multi-prime axis permanently, and looks reachable: it is a statement about the surjectivity
   of word ↦ residue maps, which is the kind of thing the existing machinery already computes.
2. **Attack the `S_n → ∞` hypothesis instead of the realizer.**  Proposition R needs
   `S_n → ∞`; the gap is entirely about the tail.  Rev 8's own strongest unconditional inputs
   (Garcia–Tal collision-free windows, Curry's quantitative form, summable reciprocals) are tail
   statements.  Rather than seek a new realizer constraint, ask whether the *existing* tail
   theorems bound `#{n : r_{n+1} ≠ r_n}` — the number of nonzero lift digits — for a divergent
   orbit.  That is a count, not a size, so Lemma O does not apply to it, which is the first
   genuine reason to expect a different answer.
3. **Formalize Lemma O and the §5.3 dichotomy in Lean.**  Not glamorous, but it converts a
   repeatedly rediscovered obstruction into a checked barrier, and would have saved this
   session's effort.  The `eoc-lean-verification` repo already has the aggregate identity
   formalized (Rev 8 §14), so this is incremental.  **It is also the only item here I would
   expect to complete with certainty.**

Explicitly *not* recommended: constructing an elliptic or Diophantine encoding of Collatz words.
Any such encoding faces C4 and C5 unchanged, and would be an analogy rather than a reduction.

## Safeguards honoured

No repository was modified; nothing was committed, pushed, published or deposited; no manuscript
was overwritten.  All work is in this scratch directory.  **No Lean build was run and no Lean
verification is claimed.**  The H10 manuscript was not accepted on authority — its proof was not
verified, and the verdict does not depend on it.  One claim of my own was retracted mid-session
and the correction is recorded in `05_COMPUTATIONAL_TESTS.md`.
