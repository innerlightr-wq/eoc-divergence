# THEOREM_LEDGER.md — proved / source-backed / computational / conditional

Every statement in this package, with its domain, quantifiers, assumptions, and
whether it is pointwise or average. `alpha = log_2 3`, `I_0 = 0.079318612775`,
`g = alpha - I_0 = 1.505643887946`, `Q_N = 2^{sN(N)+1}`, `n_N` = number of
`0`-confined words of length `N`, `mu` = normalized counting measure on odd
residues mod `Q_N`.

---

## 1. Proved here, unconditionally

| # | statement | domain / quantifiers | uniform in | pointwise or average | where |
|---|---|---|---|---|---|
| **Lemma T** | persistent seed `<=>` `r_min(N,0)` bounded `<=>` `exists X_0 forall N: W(N,X_0) >= 1` | all positive odd seeds; `forall N` | — | equivalence of a pointwise statement with a counting one | `EOC_DIVERGENCE_TARGET.md` §2 |
| **Theorem B** | `mu(C_N) = p(N,0)` **exactly**, and `#C_N = Σ_{d} 2^{sN-S_N(d)}` with classes of distinct words disjoint | every `N >= 1`; `c`-version for `c + sN(N) + 1 <= log_2 Q_N` | exact, no `N`-dependence | average (a measure identity) | §4 |
| **Proposition W** | `p(N,c) = P[S_j <= alpha j + c, j <= N]`, `d_i` i.i.d. Geometric(1/2) | every `N, c` | exact | average; **no pointwise content** | §6 |
| **Proposition A1** | if `B_N ⊆ C_N` with `mu(B_N) >= c 2^{-eps N}`, `eps < I_0`, along an infinite set of `N`, then `confined_mass_rate` fails | `eps` fixed `< I_0`, `c > 0` fixed | — | average | `AMPLIFICATION_CRITERION.md` §1 |
| **Theorem 1** | **no** such `B_N` exists, for any `m`, persistent or not | `forall eps < I_0`, `forall c > 0` | — | average | §2 |
| **Corollary 1a** | every family of distinct confined classes has measure `<= 2^{-I_0N+o(N)}`; of distinct confined words, cardinality `<= 2^{gN+o(N)}` | every `N` | — | average | §2 |
| **(AMP\*)** | `#I_N >= 2^{(g+delta)N}` + fibres `<= C N^B` + `Phi_N : I_N -> C_N` `=>` contradiction | `delta > 0` fixed | — | average | §4 |
| **Theorem 3** | word `->` least-realizer class is a bijection; every fibre is one point | every `N`; all `0`-confined words | — | exact | `JOINT_INVERSE_ATTEMPT.md` §2 |
| **Theorem 4** | down-shift fibres are `<= (alpha-1)N(N+1)/2`, hence `#I_N <= O(N^2) n_N` and `delta_N = O(log N/N) -> 0` | every `N`; the specific `Phi` | absolute constants | counting | §6 |
| **Theorem 5** | `#I_N <= n_N · max fibre` for **any** `Phi_N : I_N -> C_N` | all maps, all `N` | — | counting | §7 |
| **Proposition S** | every kernel on a **finite** set with row and column sums `1` has `\|\|K\|\|_{l^2} = 1`, so `H = 0` | all finite `O`, all such `K` | — | operator-theoretic | `ASYMPTOTIC_BUDGET.md` §4 |
| **Proposition D** | `-(1/N)log_2 p(N,floor(theta N)) -> J(alpha+theta)` for `0<=theta<2-alpha`, `-> 0` for `theta >= 2-alpha`; `J(a)=a(1-H_2(1/a))` | `theta >= 0` fixed | not uniform in `theta` | average | §6 |

**Proof status of Proposition D.** Upper bound fully proved (drop all but the
terminal constraint; `J` decreasing on `[1,2]`). Lower bound given as a sketch
(restrict to straight-line words) — the straight-line family's admissibility is
immediate but the `O(log N)` bookkeeping is not written out. **Labelled a
sketch, not a theorem**, and the statement is confirmed numerically at three
depths and eight values of `theta`.

## 2. Source-backed (repository sources read; nothing compiled here)

| statement | source | note |
|---|---|---|
| `confined_mass_rate (c) : Tendsto (fun N => -(1/N) logb 2 (p N c)) atTop (𝓝 I₀)` | `eoc-divergence@938dcc0` `Occupation/Rate.lean:478` | `c` bound **outside** the limit; **no uniformity in `c`** |
| `I₀ = alpha * (1 - binEntropy (1/alpha) / log 2)`, `alpha = logb 2 3` | same file, ll. 32–35 | `I_0 = 0.079318612775` |
| `p N c = Σ_{d ∈ confWords N c} (2:ℝ)⁻¹ ^ psum d N` | `Occupation/Compositions.lean:217` | the dyadic mass |
| `Confined c d ↔ ∀ j ≤ N, 2^{psum d j} ≤ 2^c * 3^j` | `Occupation/Compositions.lean` | **integral** form; used throughout |
| `realizerCongruence`, `leastRealizer_unique`, `residue_pinning` | `eoc-lean-verification@6057a0d` `EOC/Realizer.lean` ll. 286, 478, 543 | modulus `2^{S_N+1}`, uniqueness, pinning |
| `le_p` / `p_le`: `tt(N,sN)/N <= p <= (sN+1) tt(N,sN)` | `Occupation/Rate.lean` ll. 219, 255 | validated here, 0 violations |
| one-step drift of `S_j - alpha j` under past-only confinement `= +0.4149 ≈ 2-alpha` | `eoc-lean-verification` `scratch/center_audit_2026-09-14/REPORT.md` §4.2 | a measurement in that audit, flagged there as such |
| Theorem D (branch-node decomposition, `v_2(beta) = sigma-1`) and Theorem E (power-law barrier, exponent `2alpha-g-I_0 = alpha`) | `the growing-scale-pairs round (local scratch, not published)ARITHMETIC_PROOF_ATTEMPT.md` §§5–6 | recovered, not reconstructed |

> **No claim of Lean verification is made anywhere in this package.** No `lake
> build` was run, no Lean toolchain was invoked, and no dependency chain was
> audited in this session. The `Occupation` files declare no `sorry`, `admit`,
> `axiom` or `opaque` in their headers and
> `eoc-divergence/scripts/OccupationAxioms.lean` exists to print the axioms of
> `confined_mass_rate`, but that script was **not executed here**.

## 3. Computational, this session (exact integer / rational arithmetic only)

| check | range | result | script |
|---|---|---|---|
| Lean sandwich `tt/N <= p <= (sN+1)tt` against an independent DP | `N = 4,8,…,96` | **0 violations** | `rate_checks.py` (1) |
| Proposition W by independent transfer matrix | 27 pairs, `N <= 30`, `c ∈ {0,1,3}` | **0 mismatches**, exact rational equality | `rate_checks.py` (2) |
| Proposition D vs `J(alpha+theta)` | `N = 60,120,200`; 8 values of `theta` | monotone convergence toward prediction in every column | `rate_checks.py` (3) |
| Theorem B by brute force over all odd residues mod `Q_N` | `N = 1..14` (up to `Q_14 = 8388608`) | **0 violations**; e.g. `#C_14 = 168807 = 2^{22} p(14,0)` | `bridge.py` |
| Theorem 3: max fibre of word `->` realizer class | `N = 1..14` | **max fibre `= 1` at every `N`**, 0 violations | `bridge.py` |
| down-shift survival rate | `N = 3..12`, every node and suffix | **exactly `1.0000`** (total, defect-free) | `recombine.py` |
| up-shift survival rate and budget defect | `N = 3..12` | rate `0.40–0.69`; max defect `1,1,2,2,3,4,4,5,5,6` | `recombine.py` |
| `#I_N`, `n_N`, every fibre of the down-shift | `N = 3..14` | `delta_N` plateau is an artifact; fibres `27,40,55` at `N=10,12,14` vs Theorem 4's `32.2,45.6,61.4` | `fibres.py`, `check_thm4.py` |
| `W(N,X)` vs fair value `X p(N,0)/2`, all odd `m < 2^17` | `N = 1..24` | bulk agreement to within **`1.6%`** | `placement.py` |
| `rho(N)/r_min(N)` on the record ladder; depths by direct iteration | `N = 4..80`, seeds to `381727` | peaks at **`17.34`**, then drops below `1`; bounded band | `tail_ratio.py` |

All confinement decisions are `2^{S_j} <= 2^c · 3^j` on Python integers.
**No floating-point logarithm decides confinement anywhere.** Floats appear only
in printed diagnostics.

## 4. Conditional — and nothing new was introduced

**This package introduces no conditional hypothesis.** Every negative result
above is unconditional given the source-backed rate. For completeness, the
conditional chain inherited from the previous round is unchanged and *not* used
here:

```
   SUM-PAIR at h_N  =>  …  =>  log_2 r_min(N,0) <= 0.8321405567 N + o(N) ,
```
an **upper**-localization statement, consistent with a persistent seed, which
says nothing about divergence exclusion.

## 5. Open, and explicitly not claimed

| item | status |
|---|---|
| **(LEFT-TAIL)** `r_min(N,0) >= C^{-1} N^{-B}/p(N,0)` | open; **sufficient** for the target (`POINTWISE_INVARIANT_ATTEMPT.md` §4); measured true with `B=0, C≈17` to `N=108` |
| pointwise divergence exclusion (statement `C`) | open; untouched by this package |
| a centred / killed / weighted operator with a genuine contraction and a justified link to integer realizability | not constructed; not claimed |
| the lower bound in Proposition D | sketch only |
| whether `(AMP*)` can be driven by an index set built independently of `C_N` | open; no such construction is known to this package, and none is suggested |
| Collatz | untouched. Nothing here bears on it, and no claim is made |
