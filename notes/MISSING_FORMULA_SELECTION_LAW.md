# The finite-height selection law

**Research record, 2026-09-26. Not a revision of the synthesis paper, and not a claim
of progress toward (DE) or the Collatz conjecture.**

Nine routes were run against the missing pointwise tool — six mechanism imports and
three later routes (directional approximation-cost, phase-slip, selection-hazard). All
nine stopped, and all nine terminate at the same object: the placement of specific
integers inside a population whose size is already known. This note records what each
contributed, the exact statements worth preserving, and an isolation of the remaining
gap as a single ratio.

Reproduction: [`../audits/missing_formula_selection`](../audits/missing_formula_selection),
with the captured run in
[`repro.txt`](../audits/missing_formula_selection/repro.txt).

---

## 1. Nine-route convergence

| route | contributed | stopped at | why the same gap |
|---|---|---|---|
| **Rozier / abc** (arXiv:2306.15284v2) | exact cost calibrations; the dictionary `c_w = C_n`; abc applies to the one-defect stratum | `d ≥ 2` gives a ≥4-term relation, needing the `n`-conjecture, not abc | the one stratum it reaches is exited by a fixed seed in ≈3 steps, so it bounds `min N(j)` per `j`, never one orbit |
| **switch / `S`-unit** | the switch decomposition and the margin–switch tradeoff (§2) | the relation has `S`-unit *interior* terms but two free integer endpoints `m_0+σ_1`, `m_n+σ_ℓ` | fixing the seed removes one endpoint; `m_n+σ_ℓ` is the orbit value, whose factorisation is exactly what placement would control |
| **Sturmian / Liouville** | the square criterion transported to accelerated coordinates; the automatic height bound (§2.3) | confinement does not force long squares: confined near-critical words avoid squares of period ≥ 12 from band width 2 upward | the mechanism bites on square-rich words, already closed; entry is not forced |
| **imaginary hypotenuse** | the exact two-angle identity `m_n/m_0 = cot²(θ_D/2)·sec²(θ_C/2)` | `θ_D` is monotone in `H_n`, `θ_C` in `R_n`; the system is a skew product with no feedback | a reparameterisation of `(H_n, R_n)`; the descent boundary is the conclusion |
| **inherited membership** | the bit-loss law and minimal-automaton saturation (§2.4) | no finite-state membership is inheritance-stable; the only closed one (`m mod 3`) restricts nothing | the smallest closing state is the realizer cylinder, i.e. the placement datum itself |
| **micro / macro fibers** | cylinder conservation and the precision/multiplicity duality (§2.5–2.6) | the aggregate law closes, but its one free parameter is `Q` | `Q` is a monotone re-encoding of the frontier residual `Δ_N` |

The convergence is the content: six mechanisms with genuinely different inputs all
reduce to arithmetic selection among cylinders whose symbolic mass is already known.

Three later routes end in the same place, and are recorded here because they were
pursued independently of the six above:

| route | contributed | stopped at |
|---|---|---|
| **directional approximation-cost** | exact cost calibrations and the replenishment bookkeeping | the cost ledger is balanced by construction; what it cannot see is which cylinders are occupied below a height |
| **phase-slip / valuation-gap** | the corridor and self-financing statements | the corridor is automatic, so the temporal mechanisms are blocked and the residue is again placement |
| **selection-hazard** (§2.7) | the per-cylinder survival law and the exact `Q = 1` plateau | the one-step law is *proved* to be symbolic plus a height-truncation term, so there is no arithmetic tilt to find |

The selection-hazard route is the sharpest of the nine: it does not merely fail to
cross the gap, it shows why a one-step local mechanism cannot exist, and localises the
whole residual in a height-truncation discrepancy (§2.7, §5.1).

## 2. Exact results worth preserving

Statements and verification counts below; proofs and enumerations in the scripts.

### 2.1 Switch decomposition
For a `{1,2}`-word with runs `R_1…R_ℓ`, boundaries `0 = p_0 < ⋯ < p_ℓ = n`,
`σ_t = ±1` for letter `1`/`2`, and `B_t := 2^{S_{p_t}} 3^{n−p_t}`:
```
C_n = σ_1 B_0 + Σ_{t=1}^{ℓ−1} 2σ_{t+1} B_t − σ_ℓ B_ℓ,
```
with **exactly `r+2` terms** (`r` = number of switches), coefficients `±1` at the ends
and `±2` inside, all monomials distinct. *Verified: all 65,534 words of length ≤ 15;
0 mismatches in value, term count, or distinctness; coefficients `{−2,−1,+1,+2}` only.*
Refines the defect bound `2d+2`: `1^a2^b` has `d = Θ(n)` but `r = 1`.

### 2.2 Margin–switch tradeoff
With `κ := (α−1)(2−α) = 0.2427814…`, a `{1,2}`-word with `0 ≤ H_j ≤ W` for all `j`
satisfies
```
r + 1 ≥ 2κ·n/W − (α−1).
```
*Verified: all 34,125 zero-confined words of length ≤ 16; 0 violations.* Bounded switch
count and narrow confinement are incompatible.

### 2.3 Automatic confined-height bound
On any zero-confined word, `2^{S_i} ≤ 3^i` gives
```
C_n/3^n = Σ_{i<n} 2^{S_i}/3^{i+1} ≤ n/3,   hence   C_n ≤ (n/3)·max(2^{S_n}, 3^n),
```
with **no balance hypothesis**. *Verified: 34,125 words; 0 violations; max `C_n/3^n = 3.987`.*

### 2.4 Bit-loss law
If `m ≡ m′ (mod 2^K)` with common determined valuation `a`, then
`T(m) ≡ T(m′) (mod 2^{K−a})` and no finer, so retained precision obeys
```
K_{n+1} = K_n − a_n,   i.e.   K_n = K_0 − S_n.
```
*Verified: every odd class mod `2^K` splits under one step, `K = 6,8,10,12,14` —
fraction 1.0000 in each case.* Companion facts: the first `L` valuations are fixed by
`m mod 2^{S_L+1}` and no smaller modulus (70,000 pairs, 0 failures); and the quotient
of odd residues mod `2^N` by `L`-step futures saturates at the full `2^{N−1}` states.
**No nontrivial finite-state compression exists.**

### 2.5 Precision–multiplicity duality
With odd-Haar mass `μ(w) = 2^{−S_n}`, the child `wa` has `μ(wa)/μ(w) = 2^{−a}` and
`Σ_{a≥1} 2^{−a} = 1`. Hence
```
precision lost per step = a_n = log₂( 1 / relative child mass ).
```
*Verified: 255 words, 0 failures as exact truncated geometric sums.* Nothing is
destroyed: what the forward map consumes in resolution, the tree carries as mass
subdivision.

### 2.6 Cylinder conservation
`C(w) = r_w + 2^{S_n+1}ℤ`, and every `m ∈ C(w)` has a well-defined next valuation, so
```
C(w) = ⊔_{a≥1} C(wa),   hence   N_M(w) = Σ_{a≥1} N_M(wa)   for every height M.
```
*Verified: 728 tree nodes at `M = 10^4, 10^6`; 0 partition failures, tested by direct
partition with no truncation.*

### 2.7 Per-cylinder survival law

Take `M = 2^B − 1`, so `O_M = 2^{B−1}`.

**(a) The plateau is an identity, not an approximation.** If `S_N + 1 ≤ B` then
`|C(w) ∩ [1,M]| = 2^{B−S_N−1} = O_M·μ(w)` exactly. Summing over confined words,
`A_{N,M} = O_M p_N`, so
```
Q_{N,M} = 1    exactly,    for all N ≤ N*(B) := max{N : max_S(confined, N) + 1 ≤ B}.
```
*Verified: `N*(B)` equals the largest depth with `Q = 1` on exact rationals, 0
mismatches.*

| `B` | 8 | 10 | 12 | 14 | 16 | 18 | 20 |
|---|---|---|---|---|---|---|---|
| `N*(B)` | 5 | 6 | 7 | 8 | 10 | 11 | 12 |
| `(B−1)/α` | 4.42 | 5.68 | 6.94 | 8.20 | 9.46 | 10.73 | 11.99 |

Selection switches on precisely when the deepest cylinder modulus first exceeds the
height cutoff, at depth `N*(B) ≈ (B−1)/α`.

**(b) The per-cylinder survival count.** Parametrise the seeds of a cylinder as
`m₀ = r_w + 2^{S+1}t`, `t = 0…n_w − 1` over the admissible indices in `[1,M]`. From
`2^S m_N = 3^N m₀ + C_N`,
```
m_N = (3^N r_w + C_N)/2^S + 2·3^N·t,
```
and `3^N` is odd, so `m_N mod 2^k` is a **bijective affine function of `t mod 2^{k−1}`**.
Since `a_N = v₂(3m_N + 1)` is determined by `m_N mod 2^{a_N+1}`, the failures
`{a_N > K}` form a **single** residue class `t ≡ t*_w (mod 2^K)`, `K = K(N,S) =
max{a : 2^{S+a} ≤ 3^{N+1}}`. Hence exactly
```
surv_w = n_w − ⌊(n_w − 1 − t*_w)/2^K⌋ − 1     if t*_w <  n_w
surv_w = n_w                                   if t*_w ≥ n_w
A_{N+1,M} = Σ_w surv_w.
```
*Verified: 311,844 cylinders across `M = 2^12−1 … 2^20−1` and 397 depths; 0
survival-formula failures.* With the **exact converse**: `2^K | n_w` ⟺ the
per-cylinder hazard is exactly `1 − 2^{−K}` (4,403 of 4,403 divisible cylinders exact
at `B = 20`; 0 of 218,078 non-divisible ones exact).

So the one-step law is the **symbolic** hazard `1 − 2^{−K(N,S)}` plus a
**floor-function truncation at the height cutoff**. The deviation is a placement
discrepancy, never an arithmetic tilt.

**(c) The all-ones ray.** For `w = 1^N`, `C_N = 3^N − 2^N`, so
`r_w = (2^N − C_N)·3^{−N} mod 2^{N+1} = 2^{N+1} − 1`: the largest odd residue in its
shell, hence the last seed any height cutoff admits. *Verified: closed form and
forward valuation word, `N = 1…24`, 0 violations.*

**(d) No arithmetic signal beyond the barrier.** Conditioning on the barrier state
`R_N = (N,S_N)` and taking the expectation per cell, the barrier-only baseline is
already correct:

| | rows | observed | expected | `(obs−exp)/√exp` |
|---|---|---|---|---|
| `3x+1`, `M = 2^16−1` | 113,749 | 80,981 | 81,056.9 | **−0.267** |
| `3x+1`, `M = 2^20−1` | 1,825,739 | 1,301,451 | 1,301,576.3 | **−0.110** |
| `3x−1`, `M = 2^16−1` | 114,903 | 82,138 | 82,138.8 | **−0.003** |
| `3x−1`, `M = 2^20−1` | 1,833,329 | 1,309,044 | 1,309,104.5 | **−0.053** |

`m_N mod q` for `q = 3,5,7,9,11,13`, the previous valuation, and the height decile are
all null (every `χ²` at or below its dof; `max|z| ≤ 1.62` at `M = 2^20−1`). The one
marginal in-sample feature, `(a_{N−2},a_{N−1})`, **anti-transfers**: trained on
`M = 2^12,2^14,2^16` it makes held-out log-loss *worse* at `M = 2^18−1` (−2.13e−04)
and `M = 2^20−1` (−2.08e−04), in every regime including `10 ≤ A < 100`. The shuffled
label and shuffled history controls put the multiple-testing noise floor at
`|z| ≈ 2`, which bounds every feature above. **The `3x−1` control is
indistinguishable**: at `M = 2^20−1` it is *more* extreme than `3x+1` on four of the
nine features (`mod 9`, `mod 11`, `mod 13`, and the previous valuation at `|z| = 3.15`
against 1.62). The contrast a selection mechanism would need does not exist.

This is not a search limitation. Part (b) *forces* it: `a_N` is a bijective function
of `t mod 2^K` and of nothing else, so any 2-adic feature at that precision merely
re-encodes the label, and a feature is informative only insofar as it reveals
`t mod 2^K`.

> **Correction (scope of the last clause).** An earlier form of this paragraph asserted
> that *every* non-2-adic feature is exactly uninformative. That overclaims. For odd `u`
> with `gcd(u,6) = 1`, `m_N(t) = x_w + 2·3^N t` makes `m_N mod u` determine `t mod u`, so
> exact uninformativeness needs the lift sample to cover a complete period of the **joint**
> modulus `u·2^K` — not of `2^K`. Over a single `2^K` period there is exactly one failing
> `t`, so its residue mod `u` is determined and the feature *is* informative. Verified: the
> deviation is exactly 0 over a `u·2^K` period for `u = 3,5,7,9`, and 0.875 for `u = 5,7`
> over a `2^K` period. Concretely, for `w = (1)` and `M = 15` the seeds are `3,7,11,15`
> with next odd states `5,11,17,23` and following valuations `4,1,2,1`; at `K = 2` only
> the first fails, and `m_1 ≡ 0 (mod 5)` selects exactly it. The feature is informative
> only through the truncation, and reveals nothing beyond `t` itself. `u = 3` and `u = 9`
> are uninformative for a different and trivial reason: `2·3^N ≡ 0 (mod u)`, so `m_N mod u`
> is *constant* on the cylinder — consistent with §2.4's statement that `m mod 3`
> restricts nothing. **This does not affect the measurements of (d)**, which are
> barrier-conditioned and held-out; only the universal claim was wrong.

**(e) Where the drift lives.** With `ν` the barrier-state distribution of the integer
survivors and `h̄ = E_ν[1 − 2^{−K}]`, split
`g = log₂(h_int/h_sym) = log₂(h̄/h_sym) + log₂(h_int/h̄) = g_comp + g_arith`. At
`M = 2^20−1` the cumulative `Σg_comp` tracks `log₂Q` throughout (`N = 49`: −0.1389 vs
−0.1276; `N = 73`: −0.4999 vs −0.5089; `N = 104`: −0.9877 vs −0.9762) while
`Σg_arith` stays within ±0.041 for as long as `A_N ≥ 48`, and below ±0.34 until the
last handful of survivors, where a single survivor forces `h_int ∈ {0,1}`. Since
`ν(S) = A_{N,M}(S)/A_{N,M}`, **`ν` is the placement datum**: it is not computable from
symbolic depth-`≤N` data. The missing formula is a law for `ν`, not a selection law.

> **Verdict: no arithmetic signal beyond the barrier.** Four independent
> falsification conditions fired — everything vanishes under `R_N`; the one candidate
> fails held-out heights; `3x−1` fails to separate; the reconstructed `log₂Q` drifts
> to −3.1 by `N = 111` at `M = 2^20−1`.

**Retraction.** An earlier form of (b) claimed that divisibility of the *barrier-cell*
size by `2^K` implies an exact hazard. That is false — 7, 18, 21 and 33
counterexamples at `B = 12, 14, 16, 18` (reproduced in `per_cylinder_survival.py`
part 5). The divisibility argument applies to a single
**cylinder**, not to a barrier cell, which is a union of many cylinders with different
offsets `t*_w`. The per-cylinder statement above holds exactly, with an exact converse.

**Lineage.** The bijection between valuation words and residue classes is classical
(Terras 1976; Everett 1977; Lagarias 1985), as is the geometric law for the next
valuation. What is new here is only the **explicit truncated survival count** in (b) —
the `⌊·⌋` term and its converse — which is what converts the one-step question into a
discrepancy statement.

## 3. The finite-height count

```
A_{N,M} = #{ m odd, 1 ≤ m ≤ M : m is zero-confined for N steps }     (integer)
O_M     = #{ m odd, 1 ≤ m ≤ M } = ⌈M/2⌉
p_N     = Σ_{w confined, |w| = N} 2^{−S_N(w)}                        (exact rational)
```
and the **selection ratio**
```
Q_{N,M} := A_{N,M} / (O_M · p_N),        so        A_{N,M} = Q_{N,M} · O_M · p_N.
```

> **This is a definitional identity, not a theorem about the behaviour of `Q`.**

## 4. Interpretation

- `p_N` — the exact confined Haar/density mass. **Solved**: the rate
  `−(1/N)log₂ p_N → I₀ = α(1−H₂(1/α)) = 0.0793186…` is formalized
  (`Occupation.confined_mass_rate`), with the polynomial correction also proved.
- `O_M` — the finite archimedean population. **Trivial.**
- `Q_{N,M}` — the finite-height arithmetic selection/placement ratio. **Unexplained.**

`Q` is **not** an independent dynamical law. It is the target quantity whose
nontrivial behaviour remains unexplained, written in a form that isolates it from the
two factors that are understood.

Why the obvious bound fails: `N_M(w) ≤ 1 + M/2^{S_N+1}` summed over confined words
gives `A_{N,M} ≤ #W_N^{conf} + O_M p_N`. With `h := αH₂(1/α) = 1.5056439…` and the
identity `h + I₀ = α`, the count `#W_N^{conf} ≈ 2^{hN}` makes the union bound useless.
The `+1` per word is the obstruction: one must know *which* cylinders are occupied.

## 5. Relation to `Δ_N`

At `M = r_min(N,0)` we have `A_{N,M} = 1`, and `M` is odd so `O_M = (M+1)/2`. Hence
```
Q_{N,M} = 2 / ((M+1) p_N),
```
and with `Δ_N := log₂ r_min(N,0) − log₂(1/p_N)`,
```
Δ_N = 1 − log₂ Q_{N,M} − log₂(1 + 1/M).
```
*Both relations verified on exact rationals at `N = 4,8,…,36`: 0 mismatches, including
`A_{N,M} = 1` at each.* `Q` therefore **globalises** `Δ_N`, which is its specialisation
to the single frontier value of `M`.

> **Caution, and it matters.** `Q ≈ 1` is a statement about *large* finite-height
> ensembles. At the frontier specialisation `M = r_min(N,0)` the same `Q` **grows**:
> `0.352, 0.797, 1.370, 2.310, 3.710, 5.437, 8.160, 12.051, 16.722` at
> `N = 4,8,…,36`, because `r_min(N,0) = 27` is frozen while `log₂(1/p_N)` rises. The
> two regimes are the same object at different `M`, and neither licenses a claim about
> the other.

The practical advantage of the global form is conditioning: `Δ_N` is a min-statistic
driven by rare record replacements, whereas `Q_{N,M}` for large `M` averages over
thousands of surviving seeds.

### 5.1 Where `Q − 1` lives

**The realizer in closed form.** For a confined word `w` of length `N` with
`S = S_N(w)`, the cylinder modulus is `q_w = 2^{S+1}` and, requiring both that `2^S`
divide `3^N m₀ + C_N` and that the quotient `m_N` be odd,
```
r_w = ((2^S − C_N)·3^{−N}) mod 2^{S+1},        C₀ = 0,  C_{k+1} = 3C_k + 2^{S_k}.
```
*Verified by running the map forward from every recomputed realizer: exhaustively at
`N = 12` (8,045 words) and `N = 16` (312,455), and on a uniform 1-in-33 sample at
`N = 20` (408,251 of 13,472,296); 0 word mismatches.*

**The sawtooth.** Writing `M = k q_w + t` with `0 ≤ t < q_w`,
```
|C(w) ∩ [1,M]| = k + [ r_w ≤ t ].
```
`M` is odd and `q_w` even, so `t` is odd, and the odd residues in `[1,t]` number
`(t+1)/2` out of `q_w/2`. The **null favorable fraction is therefore**
```
u = (t+1)/q_w,        not 1/2.
```
This is the point: `Q ≈ 1` is a **frequency × magnitude balance**, not a 50/50 split.
`u` ranges over `2^{−1}, 2^{−2}, …` across the shells, and it is `u`, not `1/2`, that
an observed inclusion rate must be compared against.

**The exact identity.** Because `k_S + u_S = (M+1)/q_S = O_M 2^{−S}` exactly, grouping
words into shells by `S` and writing `f_S` for the observed favorable fraction gives
```
A_{N,M} − O_M p_N = Σ_S n_S D_{N,M,S},        D_{N,M,S} = f_S − u_S.
```
*Verified exactly on rationals for all nine pairs `N ∈ {12,16,20}`,
`M ∈ {2^12−1, 2^16−1, 2^20−1}`: 0 failures, with `A_{N,M}` cross-checked against
direct seed enumeration in every case.*

| `N` | `M` | `A_{N,M}` | `A − O_M p_N` | `Σ_S n_S D_S` | `Q_{N,M}` |
|---|---|---|---|---|---|
| 12 | `2^12−1` | 101 | −5.750000 | −5.750000 | 0.946136 |
| 12 | `2^16−1` | 1,676 | −32.000000 | −32.000000 | 0.981265 |
| 12 | `2^20−1` | 27,328 | +0.000000 | +0.000000 | **1.000000** |
| 16 | `2^12−1` | 60 | −3.316284 | −3.316284 | 0.947624 |
| 16 | `2^16−1` | 996 | −17.060547 | −17.060547 | 0.983159 |
| 16 | `2^20−1` | 16,220 | +11.031250 | +11.031250 | 1.000681 |
| 20 | `2^12−1` | 42 | +2.567967 | +2.567967 | 1.065124 |
| 20 | `2^16−1` | 633 | +2.087479 | +2.087479 | 1.003309 |
| 20 | `2^20−1` | 10,017 | −77.600342 | −77.600342 | 0.992313 |

The `N = 12`, `M = 2^20−1` row is the §2.7(a) plateau: `N*(20) = 12`, every `u_S = 1`,
every `D_S = 0`, and `Q = 1` on the nose.

**Per-shell structure**, `N = 20` at `M = 2^20−1` (`f/u` with the counting error bar
`(f/u)/√fav`; the `N = 12` and `N = 16` tables and the other heights are in
`repro.txt`):

| `S` | `n_S` | `k_S` | `u_S` | fav | `f_S` | `f/u` | `±` |
|---|---|---|---|---|---|---|---|
| 20 | 1 | 0 | 0.500000 | 0 | 0.000000 | 0.0000 | — |
| 21 | 19 | 0 | 0.250000 | 4 | 0.210526 | 0.8421 | 0.4211 |
| 22 | 187 | 0 | 0.125000 | 29 | 0.155080 | 1.2406 | 0.2304 |
| 23 | 1,265 | 0 | 0.062500 | 85 | 0.067194 | 1.0751 | 0.1166 |
| 24 | 6,608 | 0 | 0.031250 | 230 | 0.034806 | 1.1138 | 0.0734 |
| 25 | 28,333 | 0 | 0.015625 | 441 | 0.015565 | 0.9962 | 0.0474 |
| 26 | 103,078 | 0 | 0.007812 | 737 | 0.007150 | 0.9152 | 0.0337 |
| 27 | 325,398 | 0 | 0.003906 | 1,212 | 0.003725 | 0.9535 | 0.0274 |
| 28 | 898,798 | 0 | 0.001953 | 1,728 | 0.001923 | 0.9844 | 0.0237 |
| 29 | 2,135,733 | 0 | 0.000977 | 2,143 | 0.001003 | 1.0275 | 0.0222 |
| 30 | 4,036,203 | 0 | 0.000488 | 2,002 | 0.000496 | 1.0158 | 0.0227 |
| 31 | 5,936,673 | 0 | 0.000244 | 1,406 | 0.000237 | 0.9701 | 0.0259 |

**What reproduces.**

- **Populous shells sit at `f/u ≈ 1` within counting noise.** Of the 34 shells with
  `fav ≥ 100` across all nine `(N,M)` pairs, **2 fall outside two error bars** — about
  what chance gives at the 2σ level. The shells carrying the mass show no placement
  bias.
- **Once `N ≥ B−1` every shell has `k_S = 0`**, because `q_S = 2^{S+1} > M` for all
  `S ≥ N`. Then `D_S` reduces to *does shell `S` contain a realizer `≤ M`* — i.e.
  `r_min(N,0)` stratified by `S`, the Chain B / Chain A shell-offset object. The
  decomposition at that point has **no independent content** beyond the realizer-floor
  question it was meant to illuminate, and gives **no new leverage on the frontier**.

**What does *not* reproduce, and is corrected here.** The expectation was that the
structured deviation sits in the smallest shells `S = N, N+1, N+2`, with realizers
pushed near `2^{N+1}−1` by the all-1 ray. Testing the normalised realizer position
`r_w/q_S` against its null mean `1/2` (null sd `1/√(12 n_S)`):

- **no shell at all has `|z| > 3`**, at `N = 12, 16, 20`;
- the only genuinely structured shell is `S = N`, which contains **exactly one word** —
  the all-ones word, realizer exactly `2^{N+1}−1` by §2.7(c), hence `f/u = 0` at every
  height;
- shells `S = N+1` and `S = N+2` show **no realizer-position bias**: mean `r_w/q_S` is
  0.6211/0.5464 (`N = 12`), 0.4556/0.4918 (`N = 16`), 0.5702/0.5079 (`N = 20`) — within
  one to two null sd of `1/2`, and not consistently high. Their `f/u = 0` entries at
  smaller heights are small-count artefacts (`n_S = 11…187`, `fav = 0…29`), not
  structure.

Either way these shells are **high-slack**, far from the critical boundary, so they are
not where a frontier obstruction could live. The conclusion stands and is if anything
stronger: realizers are uniform in position to within counting noise in every shell
that has enough words to measure.

## 6. Extinction criterion — conditional mechanism only

`A_{N,M} ∈ ℤ_{≥0}`. Therefore any rigorous estimate giving
```
Q_{N,M} · O_M · p_N < 1        forces        A_{N,M} = 0.
```
Since `p_N ≍ N^{−3/2} 2^{−I₀N}`, a bound `Q_{N,M} ≤ poly(N)` uniform in `M` would give
`A_{N,M} = 0` for `N` large depending on `M`; as every positive odd integer lies below
some `M`, that is (DE).

> **Strength.** Such a bound **implies (DE)**. It is therefore at least as strong as
> (DE), and belongs with the exponential realizer floor and `Δ_N = O(1)` among
> sufficient statements — not among weaker intermediate targets. This note claims no
> route to it.

The integrality step is the only part doing real work, and it is why the integer count
`A_{N,M}` is the right object rather than a mass.

## 7. The `3x−1` control

`3x−1` shares `α`, the confined-word count and `p_N` with `3x+1`: the symbolic side is
identical. It differs in that `m = 1` is a zero-confined positive fixed point.
Measured at `M = 2^16 − 1`, `O_M = 32768`:

| `N` | `A(3x+1)` | `A(3x−1)` | `O_M·p_N` | `Q(3x+1)` | `Q(3x−1)` |
|---|---|---|---|---|---|
| 8 | 2936 | 2936 | 2.9360e3 | 1.000 | 1.000 |
| 24 | 436 | 425 | 4.3053e2 | 1.013 | 0.987 |
| 48 | 26 | 66 | 5.1089e1 | 0.509 | 1.292 |
| 80 | 2 | 4 | 4.5730e0 | 0.437 | 0.875 |
| 100 | **0** | 3 | 1.1310e0 | 0.000 | 2.653 |
| 140 | 0 | 3 | 7.9550e−2 | 0.000 | 37.712 |
| 180 | 0 | 3 | 6.4104e−3 | 0.000 | **467.992** |

`3x+1`: last `N` with `A > 0` is **84**; `A = 0` from `N = 85`. `3x−1`: still `A = 3` at
`N = 190`. Extinction depths for `3x+1` at smaller heights: `M = 2^8` at `N = 37`,
`2^{10}` at `51`, `2^{12}` at `51`, `2^{14}` at `66`, `2^{16}` at `85`.

For `3x+1`, `Q` is of order 1 across the tested pre-extinction regime
(`Q ∈ [0.92, 1.12]` for `M = 2^{16}…2^{22}`, `N = 8…48`) and the selected ensembles
eventually empty. For `3x−1` the positive anchor prevents extinction while the
symbolic mass shrinks identically, so `Q` grows strongly.

> **Any future useful bound on `Q` must be sign-sensitive and must fail on the `3x−1`
> positive anchor.** A bound blind to the sign of the anchor would falsely exclude
> `m = 1` under `3x−1`.

This is a constraint on proofs, not evidence that `Q` is a powerful coordinate: `Q`
separates the two maps because it is *defined from* `A_{N,M}`, which is the quantity
that differs. No values outside the tables above are claimed or extrapolated.

## 8. Epistemic status

**PROVED / EXACT**
- the switch decomposition (§2.1) and margin–switch tradeoff (§2.2);
- the automatic confined-height bound (§2.3);
- the bit-loss law `K_n = K_0 − S_n` and the precision budget (§2.4);
- the precision–multiplicity duality (§2.5);
- cylinder mass conservation (§2.6);
- **the `Q = 1` plateau `Q_{N,M} = 1` for `N ≤ N*(B)` (§2.7a)**;
- **the per-cylinder survival formula and its converse (§2.7b)**;
- **the all-ones realizer `r_{1^N} = 2^{N+1} − 1` (§2.7c)**;
- the definition `A_{N,M} = Q_{N,M} O_M p_N` (§3) and the exponent identity `h + I₀ = α`;
- the relation `Q = 2/((M+1)p_N)` and `Δ_N = 1 − log₂Q − log₂(1+1/M)` at `M = r_min(N,0)` (§5);
- **the closed-form realizer `r_w = ((2^S − C_N)3^{−N}) mod 2^{S+1}`, the sawtooth count
  `k + [r_w ≤ t]`, the null rate `u = (t+1)/q_w`, and the shell identity
  `A_{N,M} − O_M p_N = Σ_S n_S D_S` (§5.1)**.

**VERIFIED (finite range, exhaustive, exact arithmetic)**
- `Q ∈ [0.92, 1.12]` for `M = 2^{16}…2^{22}`, `N = 8…48`;
- the frontier-specialisation values of `Q` at `N = 4…36` (§5);
- extinction depths for `M = 2^8…2^{16}` (§7);
- the `3x+1` / `3x−1` control table (§7);
- **`N*(B)` for `B = 8…20`, and 311,844 cylinders over 397 depths with 0
  survival-formula failures (§2.7)**;
- **the barrier-conditioned nulls: `m_N mod q` for `q = 3,5,7,9,11,13`, previous
  valuation, valuation pairs, height decile, with shuffled-label and shuffled-history
  controls and the `3x−1` control, at `M = 2^16−1` and `2^20−1` (§2.7d)**;
- **held-out anti-transfer of the one marginal feature at `M = 2^18−1, 2^20−1` (§2.7d)**;
- **the shell identity for all nine `(N,M)` pairs, `N ∈ {12,16,20}`,
  `M ∈ {2^12−1, 2^16−1, 2^20−1}`, with `A_{N,M}` cross-checked by direct enumeration,
  and realizer positions uniform to `|z| ≤ 3` in every shell (§5.1)**.

**RETRACTED**
- that divisibility of a **barrier-cell** size by `2^K` forces an exact hazard: false,
  with 7/18/21/33 counterexamples at `B = 12/14/16/18`. The correct statement is
  per **cylinder** (§2.7b).
- that the smallest shells `S = N+1, N+2` carry a realizer-position bias: not
  reproduced; only `S = N`, a single word, is structured (§5.1).

**OPEN**
- boundedness of `Q_{N,M}`;
- polynomial or subexponential growth of `Q_{N,M}`, uniform in `M`;
- any pointwise exclusion following from either;
- **a discrepancy law for the cylinder offsets `t*_w` against the height cutoff —
  equivalently a law for `ν`, the height-truncated barrier-state measure. §2.7 shows
  this is the *whole* of what remains at the one-step level, and it is the same object
  as `Δ_N` and the realizer floor.**

No claim of progress toward the Collatz conjecture is made or implied. Nothing in this
note revises the synthesis paper.
