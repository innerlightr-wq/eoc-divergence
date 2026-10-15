# VERDICT.md

## Decision

**A nontrivial exponential least-realizer floor for the two-run family needs no
joint `×2,×3` input at all.** Theorem U gives exponent `log₆2 = 0.38685280723…`
unconditionally, as an elementary corollary of the already-published Theorem D.
Everything above that line does need such input, the required statement is
**pointwise** on a growing-modulus diagonal, corridor admissibility does **not**
weaken it, and the higher levels of the ladder do not close.

## The five answers

### 1. What is the floor, and what does it cost?

```
   r(1^u q 1^v) + 1  ≥  max( 2^{u+1} ,  2^{S}/3^{u+1} )  ≥  2^{(log₆2)·S}
```
for all `u ≥ 0`, `q ≥ 2`, `v ≥ 0`, `S = u+q+v`, with **no error term and no
hypothesis**. It costs two lines from Theorem D: `A*` is odd, and `3^{u+1}A* ≥ c`
because `0 < c < 2^{n+1}`. Verified on 2912 triples, 0 violations; worst observed
ratio `0.400000`.

### 2. Is this a new restricted least-realizer theorem?

**Modestly, yes** — as a statement about the two-run family with an explicit
constant. It is an **elementary corollary** of Theorem D of
[`episode_classification_2026-10-14`](../episode_classification_2026-10-14/), and
it is presented as such rather than as independent work. The content is that the
two bounds pull in opposite directions in `u`, so their maximum cannot be beaten
below `S/(1+log₂3)`.

### 3. Where is digit input actually needed, and in what form?

Only on the band `u+1 ≍ 0.39S`, `n ≍ 0.61S`, and only as a **pointwise** lower
bound on the least positive residue of `3^{−(u+1)}c` modulo `2^{n+1}` along the
diagonal `u, n → ∞`. The exponent follows as `ε = 1 − κ·log₂3` from
`A* ≥ 2^{n+1}3^{−κS−C}`, nontrivial exactly while `κ < log₃2 = 0.63093`;
step (ii) of Theorem U already supplies `κ = (u+1)/S`.

**Available `×2,×3` methods are the wrong shape.** Rigidity/disjointness results
need invariant measures or positive entropy; exceptional-set and Cantor-set
estimates bound the set of bad exponents. The application needs the value at the
*specific* `(u,n)` a word generates — one sequence, a null set for every
invariant measure and possibly inside any density-zero exceptional set.
**Population sparsity is not pointwise extremal placement**, and nothing is
promoted here. The two binding deficiencies are **pointwiseness** and the
**growing modulus** (a diagonal, not a fixed modulus).

### 4. Does corridor admissibility make it easier?

**No.** Confinement of the block at level `c` is the **single** inequality
`q ≤ c + α + (α−1)u`, exactly `2^{u+q} ≤ 2^c·3^{u+1}`, with **`v`
unrestricted** — verified against a per-index test, 0 violations. `q = 2`
satisfies it for every `u ≥ 0` already at `c = 1`, so every `b = (u+1)/S ∈ (0,1)`
is admissible, including the critical `b = 0.386853`. The admissible diagonal is
not thinner in the relevant direction.

### 5. What is the next target, and what would it *not* give?

> **TARGET.** There is `ζ(S) = o(S)` such that for all `u ≥ 0`, `q ≥ 2`, `v ≥ 0`
> with `q ≤ 1 + α + (α−1)u` and `S = u+q+v`,
> ```
>    A*(u,q,v)  ≥  2^{n+1}·3^{−ζ(S)} ,
> ```
> i.e. the least positive residue of `3^{−(u+1)}c` mod `2^{n+1}` is at least a
> `3^{−o(S)}` fraction of the modulus.
>
> * **quantifiers:** for all admissible `(u,q,v)`; **pointwise**, no exceptional
>   set; `c = 1 − 2^{q−1} + 2^n` explicit.
> * **consequence:** `r(1^u q 1^v) ≥ 2^{S−o(S)}` — Level A at exponent `1`.
> * **what it does not give:** Level B, C or D. See `DEPENDENCY_LADDER.md`.
> * **why it is not free:** it is exactly the pointwise statement that the
>   available `×2,×3` methods do not provide, and Observation P shows it must be
>   phrased relative to the modulus with `n` growing — never as an absolute floor
>   on `A*`.

## The three warnings worth carrying forward

1. **Never phrase a hypothesis as "`A*` is large".** For fixed `(q,v)`, `A*_u` is
   periodic with period `2^{n−1}` and dips to `O(1)` every period (verified at
   four `(q,v)`, `min A* = 5` each). Harmless for Theorem U, fatal to that
   phrasing.
2. **The bit count composes; the placement does not.** Theorem D makes the class
   modulus a product with no interaction term, so run decompositions determine
   the bit count completely and the placement not at all. Finer decompositions
   cannot bound least realizers.
3. **Level A is the smallest instance of the Level-B difficulty, not a route to
   it.** The moving anchor of Rev 8 Remark 5.8 is a global function of the carry;
   two-run placement is the fixed-anchor case.

## Scope

Nothing here proves, advances or conditionally establishes EOC, Open Problem
C/D, divergence exclusion, cycle exclusion, or the Collatz conjecture. Theorem U
is an elementary corollary of Theorem D. No external theorem is relied on, and no
claim is made about which named results exist for this exact diagonal. **No Lean
verification is claimed** — no `lake build` was run, and no formal theorem was
added.
