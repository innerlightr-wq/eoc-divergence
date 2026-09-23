# Status

Milestone **M1 of 5** complete. `main` builds; CI enforces `lake build`, the forbidden-construct
scan, and the axiom audit on every push.

## Proved

| Theorem | Statement | Paper |
|---|---|---|
| `aggregate_identity` | `2^{Sₙ}·mₙ = 3ⁿ·m₀ + Cₙ` | Lemma 2.4 |
| `cycle_drift` | a repeat forces `3^L < 2^{S_cyc}` | Lemma 4.2 |
| `not_zeroConfined_of_repeat` | a periodic orbit is not zero-confined | Lemma 4.2 |
| `injective_iff_divergent` | injective orbit ⟺ divergent orbit | — |
| `divergent_of_zeroConfined` | **the `←` direction of the headline theorem** | Thm 6.14 (half) |

Axiom audit for all of the above: `[propext, Classical.choice, Quot.sound]`.

## Open hypotheses

**None.** No `Prop`-valued external input has been introduced. If a later milestone cannot avoid
one, it will appear here as a named hypothesis on the theorems that use it, never as an `axiom`.

## Remaining

M2 `RawMap` · M3 `BinomialTail` · M4 `WindowedSparsity` · M5 `Summable` + `LastMaximum` + `Main`.

The `→` direction is the substantial half: it needs the Garcia–Tal / Curry windowed sparsity
theorem formalized, which is what makes the headline equivalence unconditional.

## Deviations from the approved statement list

Recorded so the plan and the code never drift apart.

1. `two_pow_a_mul_T`, `aggregate_identity` — stated without `Odd m` (approved; hypothesis unused).
2. `odd_T` — also stated without `Odd m`. `(3m+1)/2^{ν₂(3m+1)}` is odd for **every** `m`, so the
   hypothesis was unused. `odd_orbit` still needs `Odd m`, for the base case `n = 0`.
3. `divergent_of_injective`, `injective_of_divergent`, `injective_iff_divergent` — stated without
   `Odd M` (approved; unused).
4. `pow_succ_mul_le` — stated without `1 ≤ B`. The inequality `B^t(B+t) ≤ (B+1)^t·B` holds at
   `B = 0` as well (both sides are `0` for `t ≥ 1`, and `0` at `t = 0`), so the hypothesis was
   unused. `1 ≤ B` is still established at the call site, where it *is* needed.
5. `cycle_drift` and `orbit_pos` keep `Odd m`: positivity of the cycle value is genuinely used.
