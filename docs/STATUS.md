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

---

# `Occupation` (companion library)

A **separate** Lean library holding one occupation-side result: the exponential rate of
confined-word mass. It is **not** part of the headline equivalence, and `Divergence.lean` does
not import it. It has its own axiom audit (`scripts/OccupationAxioms.lean`), enforced in CI
under the same permitted set.

`Occupation` imports nothing from `Divergence`: `Confined` here is a condition on abstract
words, not on orbits, so the library is fully self-contained.

## O1 — compositions and the cycle lemma: **complete**

| Theorem | Statement |
|---|---|
| `card_comps` | stars and bars: `#comps N s = C(s-1, N-1)` for `1 ≤ N ≤ s` |
| `confComps_eq_empty` | confinement caps the total: empty once `2N + c ≤ s` |
| `p_eq_sum` | the mass, organised by total |
| `p_pos` | the all-ones word is `0`-confined, so `p N c > 0` |
| `two_pow_lt_three_pow_iff` | the one integral/real bridge: `2^S < 3^j ↔ S < j·log₂3` |
| `sum_range_rot` | a rotation permutes a full period |
| `exists_rot_neg` | **the cycle lemma** (Dvoretzky–Motzkin; Spitzer), generic |
| `exists_rot_confined` | `2^s < 3^N` ⟹ some rotation is `0`-confined |
| `card_comps_le_mul` | rotation is at most `N`-to-1: `#comps ≤ N · #confComps` |

Axiom audit for all nine: `[propext, Classical.choice, Quot.sound]`.

## Deviations and notes

1. `confComps_eq_empty` carries `1 ≤ N`. It is **false at `N = 0`**: with `c = 0, s = 0` the
   hypothesis `2·0 + 0 ≤ 0` holds, yet the empty word is vacuously positive and confined
   (`2^0 ≤ 2^0·3^0`). The step `2^c·3^N < 2^{c+2N}` needs `3^N < 4^N`, strict only for `N ≥ 1`.
2. Consequently **`p 0 c` is not the true empty-word mass**. Nothing downstream uses `N = 0`;
   every statement about the rate carries `1 ≤ N`.
3. `card_comps` needs both `1 ≤ N` and `N ≤ s`. At `s = 0, N = 1` the count is `0` while
   `(0-1).choose 0 = 1` in ℕ-truncated subtraction, so the unguarded form is false.
4. The cycle lemma is indexed by `ℕ` with an explicit `% N`, not by `Fin N` with its group
   structure. This Mathlib has **no `NatCast (Fin N)` instance**, even with `NeZero N`, so
   `(i : Fin N)` does not elaborate; the `ℕ` form also keeps every index manipulation inside
   `omega`'s reach. `rot` therefore takes `r : ℕ`.
5. `rot_zero_mod` does not need `0 < N` (it was dropped as unused).

## O2 — the entropy estimate: **complete**

Ported from `eoc-lean-verification`'s `EOC/BinomialEntropy.lean` (`one_le_succ_mul_choose_mul`,
the max-term argument), trimmed to what O3 consumes. Entropy is in **nats**
(`Real.binEntropy`); O3 divides by `Real.log 2` where bits are wanted.

| Theorem | Statement |
|---|---|
| `sum_term_eq_one` | `Σ_j C(n,j) p^j q^{n-j} = 1` for `p + q = 1` |
| `choose_mul_le_one` | one term is at most the sum |
| `term_le_term_max` | the terms peak at `j = k` when `p = k/n` (interior) |
| `one_le_succ_mul_choose_mul` | `1 ≤ (n+1)·C(n,k)·p^k·q^{n-k}` |
| `weight_eq_one`, `weight_pos` | the weight at the endpoints, and its positivity |
| `log_weight_eq` | `p^k q^{n-k} = exp(−n·H(k/n))`, in log form |
| `log_choose_le` | `log C(n,k) ≤ n·H(k/n)` — no `log(n+1)` loss |
| `abs_log_choose_sub_le` | `\|log C(n,k) − n·H(k/n)\| ≤ log(n+1)` |

Axiom audit for all nine: `[propext, Classical.choice, Quot.sound]`.

### Deviations

6. `choose_mul_le_one` drops `0 < n` (unused) and takes `p, q` explicitly with `0 ≤ p`,
   `0 ≤ q`, `p + q = 1` — those *are* needed and were implicit in the brief.
7. `term_le_term_max` keeps the **interior** hypotheses `0 < k` and `k < n` of the original
   port, rather than the proposed `k ≤ n`. At the endpoints the maximum statement is still
   true but needs a different argument, and its only consumer
   (`one_le_succ_mul_choose_mul`) handles `k = 0` and `k = n` directly, where the bound is
   the trivial `1 ≤ n+1`.
8. `log_choose_le` is exported alongside `abs_log_choose_sub_le`: on the upper side the truth
   is `log C(n,k) − n·H(k/n) ≤ 0`, strictly better than `≤ log(n+1)`. O3 uses the sharp form
   for the upper bound and the absolute form for the lower.
9. The endpoint identity in `log_weight_eq` holds **only** because Lean's `0^0 = 1` and
   `log 0 = 0` line up: at `k = 0` the weight is `0^0 · 1^n = 1` and `binEntropy 0 = 0`.
   Both endpoints are split out explicitly, since `Real.log_mul` needs each factor nonzero
   and the interior argument assumes `0 < p < 1`.

## O3 — the rate: **complete**

| Theorem | Statement |
|---|---|
| `sN`, `two_pow_sN_le`, `lt_two_pow_sN_succ` | the anchor `s_N = Nat.log 2 (3^N)` |
| `two_pow_sN_lt` | `2^{s_N} < 3^N`, **strict by parity** |
| `le_sN` | `N ≤ s_N` |
| `sN_div_tendsto` | `s_N / N → α` |
| `choose_step`, `two_mul_choose_le`, `tt_le_top` | unimodality of `C(s-1,N-1)·2^{-s}` |
| `p_le` | upper bound: the largest confined total dominates |
| `le_p` | lower bound: the cycle lemma at the anchor |
| `rate_core` | the rate along any anchor with `f N / N → α` |
| **`confined_mass_rate`** | **`-(1/N)·log₂ p(N,c) → I₀`** |

Axiom audit: `[propext, Classical.choice, Quot.sound]` (`choose_step` uses only
`[propext, Quot.sound]`).

### Deviations and notes

10. `le_sN` needs **no** hypothesis — `Nat.log 2 (3^0) = 0`, so `N ≤ s_N` holds at `N = 0` too.
    I had proposed `1 ≤ N`.
11. `confComps_eq_empty_of_gt` dropped an unused `1 ≤ N`.
12. `p_le` is stated as `p N c ≤ ((c:ℝ) + s_N + 1) · tt N (c + s_N)` with
    `tt N s = C(s-1,N-1)·2^{-s}` a named definition, rather than spelled out. Same content.
13. `hbig : c + s_N + 2 ≤ 2N` holds eventually, supplied inside `confined_mass_rate` from
    `s_N ≤ Nα` and `α < 2`. It is *false* for small `N`, as expected.
14. **The real-`c` corollary was skipped**, as agreed: `p` is defined over a `ℕ`-valued corridor,
    and a real corridor would need a second `Confined` predicate plus the transfer lemmas
    between them. The `ℕ` version is the theorem.
15. No logarithm is evaluated numerically anywhere: `α` and `I₀` are defined symbolically, the
    anchor is `Nat.log`, and the single integral/real bridge is `two_pow_lt_three_pow_iff`
    (with its non-strict companion `two_pow_le_three_pow_iff`).

**The `Occupation` companion library is complete.**

---

# `Descent` (audit library)

A third **separate** library holding the results retained by
[`audits/descent/DESCENT_AUDIT.md`](../audits/descent/DESCENT_AUDIT.md), whose verdict on a
descent proof of (DE) was **STOP**. It imports **only** `Divergence.Basic`, modifies nothing in
`Divergence/` or `Occupation/`, and has its own axiom audit
(`scripts/DescentAxioms.lean`) enforced in CI.

| Theorem | Content |
|---|---|
| `back_confinedUpTo`, `back_step_zeroConfined` | **L1** — the backward `d = 1` step inherits confinement, with one horizon to spare |
| `three_pow_mul_back_iterate`, `back_chain_length` | **L2** — the chain law; the chain has length exactly `v₃(x+1)` |
| `least_confined_mod12` | **L4** — a least confined integer is `≡ 3 or 7 (mod 12)` |
| `v3_T_succ`, `rt_shift`, `not_three_dvd_T_succ`, `three_dvd_T_succ` | **L7** — the lockstep invariance |

Axiom audit for all 25: `[propext, Classical.choice, Quot.sound]`.

## Notes

16. `Divergence.ZeroConfined` lives in `Divergence.CycleDrift`, which the "import only
    `Divergence.Basic`" rule excludes. The infinite-horizon statements are therefore written in
    the **unfolded** form `∀ n, 2 ^ S m n ≤ 3 ^ n`, which *is* `Divergence.ZeroConfined m` by
    definition, so `back_step_zeroConfined` applies to it directly without the import.
    `forall_confinedUpTo_iff` records the bridge to the finite horizons.
17. L1 is split into named lemmas rather than the proposed single bundled conjunction with a
    `let`: the bundled form is awkward to consume, and `orbit_back` / `S_back` are wanted
    separately in any case. Same content.
18. L2's closed form is stated division-free as `3^j · (back^[j] x + 1) = 2^j · (x+1)`, so no
    `ℕ`-division appears downstream. Every hypothesis supplies `m ≥ 1`, making the subtraction
    in `back m = (2m−1)/3` exact; `three_mul_back` states that explicitly and is used in place of
    the division throughout.
19. L4 uses `IsLeast`, and **uses** `confinedUpTo_mono` rather than assuming it: L1 delivers
    horizon `N+1` and the set asks for `N`.
20. `not_three_dvd_T_succ` **drops** the proposed `2 ≤ a m`: for odd `m`, `a_pos` gives
    `a m ≥ 1`, so `a m % 2 = 0` already forces `a m ≥ 2`.
21. `three_dvd_T_succ` is stated for **all** odd `a m`, including `a m = 1`, where it is
    consistent with `v3_T_succ` (budget `≥ 1`). The proposed `a m ≥ 3` is unnecessary.
