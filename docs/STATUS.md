# Status

**Complete — all five milestones.** `main` builds; CI enforces `lake build`, the
forbidden-construct scan, and the axiom audit on every push.

The headline theorem

```lean
theorem divergent_iff_zeroConfined :
    (∃ M, Odd M ∧ DivergentOrbit M) ↔ (∃ m, Odd m ∧ ZeroConfined m)
```

takes **no hypotheses** and depends on `[propext, Classical.choice, Quot.sound]` and nothing else.
It does **not** exclude divergent orbits; it reduces that question to universal drift exit, which
is open.

## Proved

| Theorem | Statement | Paper |
|---|---|---|
| `aggregate_identity` | `2^{Sₙ}·mₙ = 3ⁿ·m₀ + Cₙ` | Lemma 2.4 |
| `cycle_drift` | a repeat forces `3^L < 2^{S_cyc}` | Lemma 4.2 |
| `not_zeroConfined_of_repeat` | a periodic orbit is not zero-confined | Lemma 4.2 |
| `injective_iff_divergent` | injective orbit ⟺ divergent orbit | — |
| `divergent_of_zeroConfined` | **the `←` direction of the headline theorem** | Thm 6.14 (half) |
| `U_iter_shift` | shift invariant for every `j ≤ N` | Terras; Garcia–Tal Lemma 1 |
| `U_iter_shift_endpoint` | the endpoint form, as a corollary | Garcia–Tal Lemma 1 |
| `oddCount_shift` | the parity prefix is shift-invariant | — |
| `modEq_of_parity_prefix` | equal parity prefixes ⟹ `n ≡ n' [MOD 2^N]` | prefix injectivity |
| `raw_aggregate_identity` | `2^N·U^N n = 3^m·n + E N n` | — |
| `E_lt`, `contraction` | `2^N·U^N n < 3^m·(n + 2^N)` | Curry Lemma 2.2 |
| `bridge` | `orbit M n = U^[S M n] M` for odd `M` | — |
| `raw_injective_of_divergent` | divergent ⟹ raw orbit injective and collision-free | M4 interface |
| `tail_mul_le` | the sum-to-one weighted tail bound | — |
| `card_subsets_card_ge` | `#{T ⊆ range N : k ≤ #T} = tail N k` | M4 heavy case |
| `entropy_certificate` | `50^50 < 2^50·31^31·19^19`, i.e. `H(31/50) < 1` | — |
| `light_certificate` | `3^31 < 2^50`, i.e. `(31/50)·log₂3 < 1` | — |
| `heavy_tail_pow` | `tail^50 · (31^31·19^19)^N ≤ (50^50)^N` | — |
| `exists_window_base` | **one** `θ < 2` bounding both branches | M4 interface |
| `ncard_window_eq` | `Set.ncard` of a window = `Finset.card` | — |
| `window_card_le_shifts` | two shifts cover a window; no pigeonhole | Garcia–Tal split |
| `Bset_card_eq_sum_fibres` | fibring by `oddCount` over `{0,…,N}` | — |
| `fibre_card_le_choose` | heavy fibre `≤ C(N,m)`, for **every** `m` | prefix injectivity |
| `light_fibre_card_le` | light fibre `≤ 2·3^m`, for **every** `m` | contraction + collision-freeness |
| `exists_window_sparsity` | `#(A ∩ [a, a+2^N)) ≤ 4(N+1)·θ^N`, `θ < 2` | Garcia–Tal; Curry Thm 2.3 |
| `summable_inv_orbit` | `Σ 1/m_n < ∞` for a divergent orbit | Curry Prop 3.1 / Prop 4.9 |
| `rho_mul_orbit` | `ρ_n·m_n = m_0·Q_n` | Eliahou–Rozier |
| `rho_tendsto_zero` | `ρ_n → 0` | — |
| `exists_last_max` | generic strict last maximum | — |
| `exists_zeroConfined_of_divergent` | divergent ⟹ a zero-confined seed | Prop 4.10 |
| **`divergent_iff_zeroConfined`** | **the headline theorem, no hypotheses** | **Thm 6.14** |

Axiom audit for all of the above: `[propext, Classical.choice, Quot.sound]`
(`U_iter_two_pow_mul` uses only `[propext, Quot.sound]`).

## Open hypotheses

**None.** No `Prop`-valued external input was ever introduced, in any milestone. Curry's
Theorem 2.3 — the one input the companion repository carried as an unformalized external
hypothesis — is proved here as `exists_window_sparsity`.

## What remains open is mathematics, not formalization

`divergent_iff_zeroConfined` converts the divergence question into an exactly equivalent one:
does some positive odd `m` satisfy `2^{S_n(m)} ≤ 3^n` for every `n`? That is universal drift
exit, and it is open. Nothing in this repository bears on it.

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

### M2

No approved statement was changed, and no hypothesis was added or removed.

6. `oddCount` is *defined* as `(parityPrefix N n).card` rather than as an inline `filter` count,
   so that `oddCount_eq_card` is `rfl`. Same definition, factored the way M4 will want it.
7. The sharp bound `E ≤ 3^{m-1}(2^N − 1)` was skipped, as agreed: `E_lt` is what `contraction`
   consumes. `E_eq_zero` records the `m = 0` case separately, with no truncated subtraction.
8. Supporting lemmas added beyond the approved list, none of them load-bearing on their own:
   `U_of_even`, `U_of_odd`, `two_mul_U_of_even`, `two_mul_U_of_odd`, `oddCount_eq_sum`,
   `oddCount_succ`, `oddCount_le`, `E_succ`, `E_succ_even`, `E_succ_odd`.

### M3

9. `tail_mul_le` — stated **without** `hk : k ≤ N`. The hypothesis is unused: summing over
   `Icc k N` already forces `j ≤ N` at every term, and for `k > N` the tail is empty and the
   bound is `0 ≤ (a+b)^N`. `heavy_tail_pow` still case-splits on `k ≤ N`, because its weight
   identity `19N = 50(N-k) + (50k - 31N)` does need it.
10. `light_pow_le : 50m ≤ 31N → 3^m ≤ 2^N` is kept but **not** exported as the light interface.
    It carries no geometric saving, so M5's dyadic sum would not converge through it; the light
    branch of `exists_window_base` supplies the saving instead.
11. `exists_window_base` exports a **single** `θ ≈ 1.9762` for both branches — the max of the
    heavy base `(50^50/(31^31·19^19))^{1/50} ≈ 1.9427` and the light base `3^{31/50} ≈ 1.9762` —
    so M5 sums one ratio `θ/2`. `rpow` appears only inside this theorem and `le_base_pow`.

### M4

**No statement was changed, and no hypothesis was added or removed.**

12. Both fibre bounds hold for **every** `m`, with no heavy/light hypothesis. The split enters
    once, in `exists_window_sparsity`, only to choose which bound to feed to
    `exists_window_base`. This keeps the two counting lemmas independently reusable.
13. Window length is exactly `2^N`, so `[1, 2^N]` carries exactly one element per residue class
    mod `2^N` and the heavy fibre costs `C(N,m)` with no factor of two. Only the light branch
    contributes the `2` in the final constant `4(N+1)`.
14. Classical decidability is scoped to `windowFinset` and `Bset` via `open Classical in`, not
    opened file-wide, so `Finset.filter` lemmas elsewhere keep their own instances. Note the
    `open ... in` must precede the docstring, not sit between it and the declaration.

### M5

**No statement was changed beyond the correction agreed before building.**

15. `rho_succ` and `rho_mul_orbit` carry `Odd M`. Without it they are false at `M = 0`: there
    `orbit 0 0 = 0`, and `1 + 1/(3·0) = 1` in Lean, so the step identity reads `1/3 = 0`. The
    identity `(3m+1)/3 = m(1 + 1/(3m))` needs `m ≠ 0`, and `T m ≥ 1` always, so `orbit 0 0` is
    the only zero that can occur in any orbit.
16. No logarithm appears anywhere in M5: the drift is carried by `ρ n = 2^{S_n}/3^n`, and
    `R_n → −∞` is `ρ n → 0`. `Real.exp` is used once, in `Q_le_exp`, and never inverted.
17. `exists_last_max` is stated for an arbitrary positive real sequence tending to `0`, with no
    Collatz content, so it can be reused or replaced independently.
