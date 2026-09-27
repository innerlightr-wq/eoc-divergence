# Carry-robust counting bound: audit, complete coverage, and what remains

Scratch `~/scratch/collatz-prefix-suffix-20260926-215500/`. No repository modified (heads
re-verified). Labels: **DERIVED HERE**, **COMPUTATIONALLY VERIFIED WITHIN STATED RANGE**,
**UNRESOLVED**.

## 0. Verdict up front

The assessment is **right on the main point**: the carry is **not** an independent obstruction for
an upper-counting target, and my previous framing of it as an unresolved cancellation problem was
the wrong reading. Two-class domination absorbs an arbitrary binary carry at a factor-2 cost, and
since `σ* < 1` the accompanying `L/q` term is harmless. **Corrected.**

What survives as the obstruction is exactly what the assessment named: **uniform, complete-shell
control of the marginal collision energies.** One new caveat is reported in §4: the only split
index that meets the threshold at `B = 16` is a degenerate one.

## 1. Task 1 — the bound, audited against exact definitions

Re-derived: `T = Z + c (mod q)` with `c ∈ {0,1}` gives `T = t ⟹ Z ∈ {t, t−1}`, hence
`H(t) ≤ H₀(t) + H₀(t−1)` with no independence or cancellation assumption. Fourier inversion on the
product set gives `H₀(t) = q^{−1}Σ_g e(−gt/q)A(g)B(g)`, and since `|e(−gt/q)| = 1`,
Cauchy–Schwarz gives `|H₀(t) − L/q| ≤ R := √(E_A E_B)/q` **uniformly in `t`**. Therefore
```
H(0) ≤ 2L/q + 2R ,      |D| = |H(0) − L/q| ≤ L/q + 2R
```
(the lower side using only `H(0) ≥ 0`). With `R ≤ C L q^{−τ}` this gives
`|D| ≤ (1+2C) L q^{−min(1,τ)}`, i.e. **`σ = min(1, τ)`**, so `τ > σ* = 0.949955527` suffices with
arbitrary carry. Confirmed symbolically.

**Audited on real Collatz data**, not abstract configurations, over **every** residue `t` and
**every** split index `j = 2…N−2`, at `B,N = (20,13)` and `(20,18)`:

| check | result |
|---|---|
| non-product `(s,a)` classes at fixed `j` | **0** |
| `H(t) ≤ H₀(t) + H₀(t−1)` violations | **0** |
| `|H₀(t) − L/q| ≤ R` violations | **0** |
| negative energies | **0** |
| exact integer form `E_A = qΣf² − |U|²` | consistent throughout |

**The Lean interface claim is confirmed.**
`ResidueDiscrepancy.exceptional_count_le_of_leastRealizerBound (U K) (hN) (A C : ℝ) (hC : 1 ≤ C)
(hNA : A*K ≤ N)` consumes
`#{w : K ≤ S_w ∧ r_w < 2^K} ≤ C·Σ_{w : K ≤ S_w} 2^K(1/2)^{S_w+1}` — an **upper** count against the
cylinder reference mass, with `C ≥ 1`, and **no** requirement of asymptotic equality. It does not
route through `WeylBound`; `exceptional_count_le_of_weyl` is a wrapper around it. So the direct
counting interface is available and the absolute-value Weyl hypothesis can be bypassed, exactly as
the assessment says.

## 2. Task 2 — complete-shell bounds, every class included

Partitioning each shell by the intermediate valuation `a` at a fixed `j` covers it exactly once
(verified: product property holds for all classes, 0 exceptions), and the trivial bound is used
where better: `H_s(0) ≤ Σ_a min{L_a, 2L_a/q + 2R_a}`.

**No `#U,#V ≥ 32` filter.** All classes, including singletons.

`κ = 0.90` (`B=20, N=18`, best split `j=2`), all 1,900,452 words with `d ≥ 1`
(the 18 words with `s < B` are complete cylinders, correctly outside the `K ≤ S_w` filter):

| `s` | `d` | `L_s` | true `H_s(0)` | `L_s/q` | `Σ_a R_a` | proved bound | `τ_shell` | trivial used |
|---|---|---|---|---|---|---|---|---|
| 20 | 1 | 150 | 80 | 75.00 | 4.00 | 150.00 | 5.229 | 2 |
| 22 | 3 | 4,265 | 566 | 533.12 | 71.95 | 1210.16 | 1.963 | 0 |
| 24 | 5 | 53,020 | 1,513 | 1656.88 | 278.39 | 3870.53 | 1.515 | 0 |
| 26 | 7 | 351,080 | 2,733 | 2742.81 | 706.08 | 6897.78 | 1.280 | 0 |
| 27 | 8 | 663,535 | 2,636 | 2591.93 | 1095.99 | 7375.84 | 1.155 | 0 |
| 28 | 9 | 663,535 | 1,313 | 1295.97 | 931.59 | 4455.11 | **1.053** | 0 |

Totals: `L = 1,900,452`, true `H(0) = 12,409`, cylinder main `= 12,452.95`, **true `C = 0.9965`**,
**proved `C = 2.5982`**. At `B = 16, N = 15`: proved `C = 3.2278`.

`κ = 0.65` (`B=20, N=13`): only `s = 20`, `d = 1` exists, where `2L/q = L` so the trivial bound
already gives `C = 2.0000`. **That is an artifact of `d_max = 1` at this `B`**, not evidence about
the target: `d_max ≈ (ακ−1)B = 0.0302B` grows, and at `B = 320` reaches 11, where the trivial
bound gives `2^d = 2048`, not a constant. Recorded as **not informative for κ = 0.65**.

## 3. Task 3 — the remaining uniform estimate, and which marginal binds

Writing `x_A := E_A/|U|² = qΣf²/|U|² − 1` and `x_B := E_B/|V|²` (exact integer collision counts),
`R = L√(x_A x_B)/q`, so per class `τ = 1 − log_q√(x_A x_B)`.

> **The uniform estimate that remains (UNRESOLVED).** For every `B`, every shell `s ≥ B`, and the
> chosen split `j`: `Σ_a R_a ≤ C·L_s·q^{−τ}` with `τ > σ* = 0.949955527` and `C` independent of `B`.
> Equivalently: uniform control of the marginal high-block collision counts `Σ_x f(x)²`,
> `Σ_x h(x)²`. This does **not** use the below-cutoff count as a premise.

Measured `τ_shell` at the binding (largest-`d`) shell, over all split indices:

| | best `j` | `τ_shell` at best `j` | splits passing `τ > σ*` |
|---|---|---|---|
| `B=16, N=15` (`d=8`) | 2 | **0.9836** | **2 of 12** (`j = 2,3` only) |
| `B=20, N=18` (`d=9`) | 2 | **1.0529** | 14 of 15 |

## 4. The caveat I have to report: the winning split is degenerate

At `j = 2` the prefix class is a **single word** (`|U| = 1` in every class — confirmed at both
`B`), so `x_A = q − 1`, its maximal value, `A(g)` has modulus 1 at every frequency, and the entire
saving comes from the suffix marginal `x_B ∈ [3.3·10⁻⁴, 3.4·10⁻³]`. With `|U| = 1` the count
reduces to `#{v : Q_hi(v) + c(v) ≡ −P_hi}` — **a single-marginal equidistribution statement for
words of length `N−2`**, i.e. the original shell question re-indexed, not a genuine factorization
gain.

The genuinely balanced splits are the informative ones, and **they fail at `B = 16`**: `j ≥ 4` gives
`τ_shell = 0.928, 0.914, 0.896, 0.883, 0.879, 0.835, 0.852, 0.830, 0.830, 0.859`, all below `σ*`.
They pass at `B = 20`, but two points are not a trend and I am not fitting one.

This also corrects a claim in my previous report. I wrote that "the prefix supplies the saving"
(from `E_A/E_A^{max} ≈ 0` at the `a ≥ B` split). At `j = 2` the opposite holds. **Which marginal is
equidistributed depends on the split point**, and the bound is limited by the worse one; a
singleton marginal contributes the maximal excess `q−1`. Neither statement is universal.

## 5. Status and next step

- **Carry**: no longer an obstruction for the upper-counting target. **Resolved** (§1).
- **Complete coverage**: achieved, all classes, trivial bound retained where better. **Done** (§2).
- **Proved constant**: `C = 2.60` (`B=20, κ=0.90`), `C = 3.23` (`B=16`) — at a degenerate split.
- **Uniformity in `B`**: **UNRESOLVED**, and the binding case is the largest-`d` shell, where the
  measured margin over `σ*` is `0.034` (`B=16`) and `0.103` (`B=20`).

If the measured `C ≈ 2.6` were uniform in `B` at `κ = 0.90`, `exceptional_count_le_of_leastRealizerBound`
would give exponent `1 − I₀·0.90 = 0.928613` against the unconditional baseline `0.949956` — a gain
of `0.021342`. That is the prize, and it now rests on exactly one statement (§3) rather than on a
carry-cancellation theorem.

**Next step:** attempt the §3 estimate for a *balanced* split, since the degenerate `j = 2` route is
a re-indexing. Concretely, bound `Σ_x h(x)²` for the suffix high-block map
`v ↦ ⌊(3^{−j}2^a r_v mod 2^{s+1})/2^B⌋` uniformly in `(B, s, a, j)`. Keep `κ = 0.65` as the primary
theorem target and `0.90` as the stress test; no larger scan is needed first.
