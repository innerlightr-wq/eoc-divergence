# Baseline and scope

Scratch: `~/scratch/collatz-partial-counting-20260926-205246/`. Recorded before any change.

## Repository state (verified, not assumed)

| repo | branch | HEAD | tracked mods | untracked | remote tip |
|---|---|---|---|---|---|
| `eoc-divergence` | `missing-formula-selection-law` | `9a1748a5414b0d0ca6b4b2fff18153f3bf92f64f` | 0 | 14 | `origin/missing-formula-selection-law = 9a1748a` (**identical**) |
| `eoc-lean-verification` | `research-sparse-visits-2026-09-16` | `14dea46ae5af816754cf3883475fa73dea598130` | 3 (`EOC.lean`, `docs/LITERATURE_CONTEXT.md`, `docs/RESEARCH_STATUS.md`) | 50 | `origin/main = 1c4d670` |

`origin/main` of `eoc-divergence` is `b7e4241`. Local and remote agree on the
missing-formula branch, so the base is unambiguous: **`9a1748a`**.

**Pre-existing worktrees left untouched**: `eoc-divergence` has `sturmian-v2-copy` (detached
`3407b1b`); `eoc-lean-verification` has `eoc-harmonic-8-9`, `eoc-main-integration`, and 27
worktrees under another session's scratchpad (marked *prunable*). None were pruned or modified.

**Toolchains differ and were not changed**: `eoc-divergence` `leanprover/lean4:v4.34.0`;
`eoc-lean-verification` `leanprover/lean4:v4.34.0-rc1`, mathlib `rev = v4.34.0-rc1`. Results
from the two repositories are therefore **not** combined. No `lake build` was run in this task
(see REPRODUCIBILITY.md); no Lean file was added or edited.

**No `AGENTS.md` or `CLAUDE.md` exists in either repository.** `README.md` (162 / 797 lines) was
read; it documents build procedure and scope but imposes no additional agent rules.

**New work**: branch `research/harden-missing-formula-audit`, isolated worktree, one local
commit `b57b15243d440540c7e13e07e0be32ea512a4bb4`. Nothing pushed, no PR, no DOI, no manuscript
edit.

## Definitions, verified against source

| item | verified value | source |
|---|---|---|
| `α` | `Real.logb 2 3` | `EOC/Confinement.lean:9` |
| `I₀` | `α − α log₂α + (α−1)log₂(α−1)` = `0.07931861277485547` | `EOC/TaoLike/PersistenceModel.lean:422` |
| `Confined U d N` | `∀ j ≤ N, R d j ≤ U` where `R = S_j − jα` | `EOC/Confinement.lean:15` |
| **zero confinement** | the case `U = 0`; exact integer form `2^{S_j} ≤ 3^j` | derived; used by the divergence audit |
| `A_{N,M}` | `#{m odd, 1 ≤ m ≤ M : zero-confined for N steps}` — cutoff **INCLUSIVE** `[1,M]` | `notes/MISSING_FORMULA_SELECTION_LAW.md` §3 |
| `O_M` | `⌈M/2⌉`; at `M = 2^B−1` equals `2^{B−1} = X/2` | ibid. |
| `p_N` | `Σ_{w confined, |w|=N} 2^{−S_N(w)}`, exact rational | ibid. |
| `Q_{N,M}` | `A_{N,M}/((X/2) p_N)` — **confirmed**, matches the brief | ibid. §3 |
| exact-realizer modulus | `q_w = 2^{S_w+1}`. The `+1` is **terminal parity**: it forces `m_N` odd. Verified: `x_w = (3^N r_w + C_w)/2^{S_w}` is an odd integer on 12,447 confined words, 0 exceptions | `repro/a1.out` |
| `E_U` | `{μ odd : ∀ M, Confined U (a∘orbit μ) M}` — permanently `U`-confined seeds, **not** all divergent seeds | `ExceptionalPowerBound.lean:248` |
| baseline exponent | `1 − I₀/α = H₂(1/α) = 0.9499555271883305` | `exceptional_count_le_rpow`, `one_sub_I0_div_alpha_eq` |
| logarithms | `log₂` throughout (`Real.logb 2`); `I₀` is a **bit** rate | `PersistenceModel.lean:449-453` |

### `p_N` normalization — the key interface identity (DERIVED HERE)

`geom2 k = (1/2)^k` for `k ≥ 1`, `0` otherwise (`TaoLike/TaoInterface.lean:307`), and
`iidGeom2VectorProb n {a} = ∏ᵢ geom2 (a i)` (`:399`). `geomPersistenceEvent α c n` is
`∀ j, 1 ≤ j ≤ n → centeredSum α n a j ≤ c`, i.e. `R_j ≤ c` (`PersistenceModel.lean:33`).
Hence, on words with all letters `≥ 1`,
```
iidGeom2VectorProb N (geomPersistenceEvent collatzAlpha U N) = Σ_{w : R_j ≤ U ∀ j} 2^{−S_N(w)} = p_N^{(U)}
```
**exactly**, with `U = 0` giving the divergence-side `p_N`. Therefore the first-moment
hypothesis of `exceptional_count_le_of_firstMoment` is **literally `Q_{N,M} ≤ C`**.

### `exceptional_count_le_of_firstMoment` — actual signature

```
(U : ℕ) {X N : ℕ} (hN : 1 ≤ N) (hX : 1 ≤ X) (A C : ℝ) (hC : 0 ≤ C)
(hNA : A * Real.logb 2 X ≤ N)
(hyp : #{μ ∈ range X | Odd μ ∧ Confined U (a∘orbit μ) N}
         ≤ C * (X/2 * iidGeom2VectorProb N (geomPersistenceEvent collatzAlpha U N)))
⊢ #{μ ∈ range X | Odd μ ∧ ∀ M, Confined U (a∘orbit μ) M} ≤ C * exp(lambdaStar*U)/2 * X^(1 − I₀*A)
```
Note `range X` is `[0,X)`, i.e. an **exclusive** upper cutoff on the Lean side, while the
divergence-side `A_{N,M}` uses inclusive `[1,M]` with `M = X−1`. These agree: odd
`μ ∈ [0,X) ⟺ μ ∈ [1,X−1]`. `C` is an arbitrary real parameter and may depend on `X`.

### Persistence rate: exact `I₀`, no loss (LEAN VERIFIED)

`geometric_persistence_upper_bound_bits (c : ℝ) (n : ℕ) (hn : 1 ≤ n)` gives
`iidGeom2VectorProb n (geomPersistenceEvent collatzAlpha c n) ≤ exp(λ* c) · 2^{−I₀ n}`
(`PersistenceModel.lean:451`). The **exact** rate `I₀` is used, with a multiplicative constant
`exp(λ* c)`; there is no substitution of a rate `γ < I₀`. This answers the brief's question
directly.

### `WeylBound` — actual quantifiers

`WeylBound U N K C := ∀ s, K ≤ s → Σ_{g ≠ 0} ‖shellWeyl U N K s g‖ ≤ (C−1)·#shell(U,N,s)`
(`ShellWeyl.lean:202`). Only shells with `s ≥ K` are constrained; shells with `s < K` are
complete cylinders handled exactly.

## Interface map

**A. Unconditional and proved (LEAN VERIFIED).** `exceptional_count_le_rpow`:
`#(E_U ∩ [0,X)) ≤ C_U X^{1−I₀/α}` for `X ≥ 4`. `survivor_count_le_rpow` at
`Nstar X = ⌊log₂X/α⌋`. `geometric_persistence_upper_bound_bits` (exact `I₀`).
`one_sub_I0_div_alpha_eq`. `card_filter_lt_eq_fourier` (exact Fourier identity).
`leastRealizer_eq_prefix_add`, `topBlock_eq_suffix`, `dyadicPhase_eq_prefix`. Zero `axiom`,
`sorry`, `admit` in `EOC/*.lean` (checked repo-wide: count 0).

**B. Conditional on an external hypothesis.** `exceptional_count_le_of_firstMoment` (needs
`Q_{N,M} ≤ C`). `leastRealizerBound_of_weyl`, `exceptional_count_le_of_weyl`,
`shell_count_le` (need `WeylBound`). `weylBound_of_pointwise` (needs a pointwise power saving
`2^{−n}`).

**C. Exact identity or definition, supplying no estimate.** `A_{N,M} = Q_{N,M}·O_M·p_N` (§3 of
the note — definitional). The plateau `Q_{N,M} = 1` for `N ≤ N*(B)` (exact, but exactly the
pre-fresh-bit regime). `Δ_N = 1 − log₂Q − log₂(1+1/M)`. The cylinder decomposition
`A_{N,M} − (X/2)p_N = Σ_{q_w>X}(1_{r_w<X} − X/q_w)` (verified here).

**D. Computational evidence only.** `Q ∈ [0.92,1.12]` for `M = 2^16…2^22`, `N = 8…48`; the
shell tables of §5.1; the `Q` ladder measured here; realizer-position uniformity `|z| ≤ 3`.

**E. Merely proposed.** `WeylBound` with constant `C`; square-root cancellation of shell
discrepancies; any `η > 0` first-moment bound beyond the plateau.

**Distinctions kept explicit.** Permanently zero-confined seeds (`E_0`) ⊊ permanently
`U`-confined (`E_U`, `U>0`) ⊊ all divergent seeds; finite surviving words (`A_{N,M}`) are a
depth-`N` truncation of none of these; arbitrary symbolic sequences are not realizable at all.
Single-window (`Confined U · N`) versus multi-window (`∀ M, Confined U · M`) is the
`hsub` step inside `exceptional_count_le_of_firstMoment` and is the only place the two meet.
