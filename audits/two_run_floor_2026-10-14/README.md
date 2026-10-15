# An unconditional two-run least-realizer floor — 2026-10-14

**Question.** How much joint `×2, ×3` ("powers of 3 modulo powers of 2") input is
actually needed to obtain a nontrivial exponential lower bound on the least
realizer of a two-run valuation word `1^u q 1^v`?

**Answer: none.** Theorem D of
[`episode_classification_2026-10-14`](../episode_classification_2026-10-14/RUN_ARITHMETIC.md)
gives the realizing set exactly; combining its two elementary consequences —
`A* ≥ 1` and `3^{u+1}A* ≥ c` — already yields

```
   r(1^u q 1^v) + 1  ≥  2^{(log₆2)·S} ,       S = u+q+v ,
   log₆2 = 1/log₂6 = 0.38685280723… ,
```

with **no error term and no digit hypothesis**. Verified on 2912 triples with 0
violations; worst observed `log₂(r+1)/S = 0.400000`.

Digit input is needed **only** to push the exponent above `log₆2`, and **only**
on the band `u+1 ≍ 0.39·S`, `n ≍ 0.61·S`. `TWO_RUN_FLOOR.md` locates that band
exactly and `DEPENDENCY_LADDER.md` says what each stronger conclusion would
additionally need.

---

## Contents

| file | contents |
|---|---|
| [`TWO_RUN_FLOOR.md`](TWO_RUN_FLOOR.md) | Theorem U with every constant audited; where the exponent is binding; the periodicity quantifier trap; the corridor-admissible cone |
| [`DEPENDENCY_LADDER.md`](DEPENDENCY_LADDER.md) | two-run floor → all confined words → divergence exclusion → full EOC, with every missing bridge named |
| [`VERDICT.md`](VERDICT.md) | the decision and the next target |
| [`PROVENANCE.md`](PROVENANCE.md) | sources, resources, scope |

## The three headline facts

1. **Level A is unconditional.** `ε = log₆2 = 0.38685`, no hypotheses. The two
   bounds that give it pull in opposite directions in `u`, so their maximum is
   minimised at `b = (u+1)/S = 1/(1+log₂3)` — which is where the exponent comes
   from.
2. **Corridor admissibility does not lower the bar.** Confinement of `1^u q 1^v`
   at level `c` is the **single** inequality `q ≤ c + α + (α−1)u` (exactly
   `2^{u+q} ≤ 2^c·3^{u+1}`) with **`v` unrestricted**. Taking `q = 2` satisfies it
   for every `u ≥ 0` already at `c = 1`, so the critical band is fully
   admissible and the required input is exactly as strong on the admissible
   diagonal as off it.
3. **A hypothesis must never be an absolute floor on `A*`.** For fixed `(q,v)`,
   `A*_u` is periodic in `u` with period `2^{n−1}` and dips to `O(1)` within
   every period (verified at four `(q,v)`; `min A* = 5` in each). That is
   harmless for Theorem U — for fixed `n`, `log₂(r+1) ≥ u+1 = S−n+1` gives ratio
   `→ 1` — but it kills any statement of the form "`A*` is large", and it means
   `n` must be allowed to grow with `u`.

## Limits

Nothing here proves, advances or conditionally establishes EOC, Open Problem C/D,
divergence exclusion, or the Collatz conjecture. Theorem U is an **elementary
corollary** of the already-published Theorem D and is presented as such.
`DEPENDENCY_LADDER.md` is explicit that Level A is *not* a stepping stone to the
higher levels — it is the smallest instance of the same difficulty. **No Lean
verification is claimed** and no external theorem is relied on.

## Reproduction

CPython standard library only. All congruence, divisibility, confinement and
minimality decisions are exact `int`; floats are printed diagnostics only.

```bash
python3 scripts/floor.py     # the class, Theorem U, periodicity, the cone   ~40 s
```
