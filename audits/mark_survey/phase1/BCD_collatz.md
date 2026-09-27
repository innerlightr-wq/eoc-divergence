# Phase 1 — Groups B, C, D: the Collatz side

Reading only. Page/section references are to the PDFs listed in `SOURCES.md`.

---

# Group B — EOC programme core

## B01. *A global occupation conjecture for the accelerated 3x+1 map*, Revision 7 (2026)

Reorganizes the programme around four axes (occupation, residue, time, divergence) and the exact
bridges between them: the least-realizer frontier `r_min(N,c)` is the inverse function of the
single-window lifetime `L_c(m)`, so every pointwise lifetime bound transfers to a realizer floor.
Retains Garcia–Tal/Curry as the unconditional divergence input, and records what the audits closed:
finite cylinders cannot decide infinite realization; several apparently independent coordinates are
invertible reparameterizations; the known word shadows do not characterize positive realization.

**Candidates.**
- **G21 (height amortization).** `ρ_N = log₂H/S_N` with `H = max(|A|,|Λ|)` for the realizer
  condition `2^{S_N} | A + χΛ` (§5.3, Obs. 5.9). Periodic and eventually periodic words have
  `ρ_N → 0` (a fixed height amortized over unboundedly many periods); arbitrary confined words give
  only `(C_N, 3^N)`, so `ρ_N ≥ 1` and the Liouville branch is vacuous. The note states the separating
  invariant is height amortization, **not** symbolic complexity: the Sturmian word, of minimal
  aperiodic complexity `p(n)=n+1`, already has `ρ_N > 1` at every depth examined while its periodic
  approximants sit near `0.26`.
- **G21a (coordinate list, already screened).** Normalized carry, lift digits, terminal zero gap
  `g(D) = ⌈E(D)⌉`, transport depths `F, M, H` — §9.2 records each as an invertible reparameterization
  of the exact realizer, and `B_N = C_N + 3^Nχ` as the single identity whose Archimedean size and
  2-adic valuation are complementary factors, `log₂|B_N| − v₂(B_N) = log₂ m_N`, not two independent
  constraints.
- **G21b (bounded prefix realizers).** Rem. 9.5: the one word-level invariant sharp enough to decide
  realizability exactly — and therefore a restatement of realizability, not a handle on it.

## B02. *Transport deficits and 2-adic survival budgets* (Aug 2026)

Isolates the chain `past–future 2-adic matching precision → perfect-transport lifetime → first-
failure severity`. `M_j = v₂(T_j − A_{j,∞})` exactly determines the length of perfect transport
(`δ_{j+1}=⋯=δ_{j+m}=0 ⟺ M_j ≥ D_m`), depletes exactly by the valuation discharged
(`M_{j+m} = M_j − D_m`), and at first failure forces `δ_fail ≥ log₂(1+2^{F+M})`: transport is either
exactly maximal or loses an amount comparable to the depth.

**Candidates.**
- **G22 (matching precision).** `M_j`. This is the one quantity in the corpus that reads the
  *integer* directly: on a genuine orbit (B01 §9.2) `M_j` is the length of the zero-run of the
  **seed's binary expansion** beginning at bit `S_j`. It therefore sees the terminating tail, which
  Observation `obs:integer` of the synthesis note names as one of only two integer-specific features.
- **G22a (cumulative regeneration).** The total excess regeneration over all failures is at most
  `⌊log₂m₀⌋+1`, the bit intervals at distinct failures being disjoint.

## B03. *Conditional obstructions and launch renormalization* (Aug 2026)

Proves the launch-state collapse `T_j = −m*_j·3^{−j}`, so that letters after a stabilized index are
exactly the accelerated word of the orbit of a smaller integer. A word with anomalously small
realizer therefore decomposes into a short free prefix and a long forced suffix. For the periodic
branch: terminal-repetition fraction bound `1 − (1−ε)log₃2 + o(1)`, frontier limit `1 − log₃2 ≈
0.36907`. For the irregular branch the inherited corridor **grows linearly** in the original word
length, so renormalization preserves the form of the problem without fixing the corridor.

**Candidates.**
- **G23 (terminal-repetition fraction).** The limiting fraction of a forced suffix that must be
  terminal repetition, with frontier value `1 − log₃2`.
- **G23a (corridor-uniform lifetime hypothesis).** Named in the note as the hypothesis that would
  close the residual branch, and labelled open.

## B04. *Three scales of confinement*, second revision (Sept 2026)

Exponential rate `h_conf = αH₂(log₃2)` from the cycle lemma; the polynomial correction is exactly
`N^{−3/2}`, two-sided, for both the unweighted count and the dyadic survival probability; and the
`O(1)` phase is an explicit geometrically weighted renewal sum whose jump sets are **the Beatty
sequences of `β = α−1`** — a genuine arithmetic manifestation of the irrationality of `α`. Every
statement is an ensemble statement about finite words, stated as such.

**Candidates.**
- **G24 (renewal phase).** The bounded `O(1)` phase coefficient and its Beatty jump sets: a limit
  object that survives the `2^{−I₀N}N^{−3/2}` normalization exactly, and whose structure is
  arithmetic rather than statistical.

## B05. *Inheritance-preserving differentiation in the Collatz survivor tower* (July 2026)

Hereditary refinement embeds an ancestral branch subspace in the intersection of two refined
descendant subspaces. A registered level-10 test chose level-doubling over constant increments,
with branch-rank increments in exact ratio `2:1`; under sustained `2:1` the normalized branch
asymmetry is driven to `χ* = 1/3`, i.e. rapidity `ξ* = ½ln2`. A **negative** result is central: the
same `χ = 0` persists through several refinement steps and then jumps, so no autonomous scalar law
`χ_{ℓ+1} = F(χ_ℓ)` can describe the tower — the state needs level or regime information as well.

**Candidates.**
- **G25 (normalized branch asymmetry).** `χ_ℓ → 1/3`, a normalized invariant with an exact limit.
- **G26 (order–clock gate).** Full-band activation at `ℓ → ℓ+1` occurs exactly when the
  multiplicative order of the multiplier outruns the clock modulus, `ord_{2^ℓ}(A) > 32`.

## B06. *Pointwise survivor discrepancy in a width-two Collatz system*, v2

In the width-two model (`d ∈ {1,2}`, `d ≥ 3` leaves the model) with the exact mechanical barrier
`S_k ≤ ⌊k log₂3⌋`, words are grouped into terminal cells and source classes `c ∈ {7,3}`. The formal
word count `B_c` is distinguished from the **arithmetically realized** count `E_c`, with the exact
decomposition `2(E₇−E₃) = (B₇−B₃) − (Σ₇−Σ₃)`. The corrected conjecture `B₃(ℓ,n,h)>0 ⟹
E₇(ℓ,n,h) > E₃(ℓ,n,h)` and the weak `E₇ ≥ E₃` remain open, exactly verified through `ℓ = 27`; the
unresolved obstruction is conditional anti-concentration of newly injected 2-adic frontier bits.

**Candidates.**
- **G27 (signed survivor discrepancy).** `E₇ − E₃`: the difference between two *realized* counts,
  i.e. a quantity defined by which words positive integers actually attain, not by the words
  themselves. The formal/realized gap is exactly the arithmetic-versus-word distinction the survey
  is looking for.

## B07. *Representation sufficiency and licensed inference* (Aug 2026)

A target-relative audit: provenance gate; exact sufficiency `Q = Q̃∘π` with the fibre criterion;
quantitative resolution by target fibre diameter `Δ_Q(y)` with optimal reconstruction radius
`r_Q = ½Δ_Q`; a minimal no-go; monotonicity under coarsening; stability; transport compatibility.
Calibrated on five controlled examples. **Controlled Example II** is "excellent refinement of the
wrong target": a detuned Ramanujan kernel converges fast to a limit that is not `1/π`, with a floor
no further computation touches. **Controlled Example III** is exactly the quarter-gamma case: the
beta family is *exactly* sufficient for the lemniscatic-period target (`Δ_Q ≡ 0`) and *provably*
insufficient for the modular mechanism, by the Clausen parameter arithmetic.

**Not a candidate mark — this note supplies the screen.** Its fibre criterion is the general form of
S1, and its `E_solver → 0` while `E_representation > 0` decomposition is the general form of S2.

---

# Group C — carry-equation family (4 of 29 sampled)

## C01. *A bit analyzer for the Collatz carry equation* (June 2026) · C03. *Tail-tracking and the leading-block principle* (June 2026)

Both are built on one diagnostic: `ℓ(D) = v₂(Q(D) + Ξ_α)`, the first-disagreement depth between a
word's periodization and the characteristic Sturmian word, read off the 2-adic bits of the carry
quotient. C01 certifies saturation plateaus for grouped tower families (`ℓ = 83, 64, 568, …`) and
recycles residues across two-parameter families; C03 removes the adjacency hypothesis with a
two-channel Horizon Lemma and the depth formula `ℓ = min(ℓ_tail, ℓ_ceil)`, matching 1324/1324
predicted members with the 20 boundary cases explained by Christoffel identities. Both state
explicitly that the analyzer pins 2-adic candidates only and that the odd-prime layer is independent.

**Candidates.**
- **G30 (bit depth).** `ℓ(D) = v₂(Q(D)+Ξ_α)`. `Q(D) = C_L(D)/(2^S−3^L)` is a function of the
  valuation word `D` alone, so `ℓ` is too. The saturation plateaus are the same freezing phenomenon
  the Sturmian audit's Task-5 control exhibits at a rational point.

## C02. *The positive-entropy 2-adic carry law* (June 2026)

The projective carry coordinate `Q(D) = C_L(D)/(2^S−3^L) ∈ Z₂` satisfies the Bridge congruence
`r(D) ≡ Q(D) (mod 2^S)`, so its low-depth law *is* the law of the least-realizer residue. On the
uniform shell the prefix bits are hypergeometric; as `L,S → ∞` with `L/S → ρ` the residue law
converges to the pushforward of iid Bernoulli(ρ) bits, and the projective limit `µ_ρ` on `Z₂^×` is
Haar **iff** `ρ = ½`. At the critical Collatz density it is not.

**Candidates.**
- **G31 (limiting residue measure).** `µ_ρ` and its multifractal/dimension data: a limit object that
  survives normalization and is non-Haar exactly because the critical density is `log₃2 ≠ ½`.

## C04. *Finite-field zero sums in the Collatz carry equation* (June 2026)

Two positive results: contact modulo any odd wall prime is a vanishing `L`-term exponential sum,
reducible to powers of 2 whenever `3 ∈ ⟨2⟩`; and the wall relation forces `3 ∈ ⟨2⟩` whenever
`gcd(L,p−1)=1`. Two nulls: across three shells (~5.3 M residents, six prime layers) per-prime
zero-sum counts track uniform density and layers intersect essentially freely — nonsingularity at
composite walls is a near-uniform sieve, not an arithmetic obstruction, and the contemplated
"composite-wall incompatibility theorem" is **withdrawn**; and zero-sum exponent sets are
geometrically generic. One anomaly survives as an open question (layers 71 and 14303 of shell
`(17,27)` co-vanish 34 times against an expectation of 5.2).

**Candidates.**
- **G32 (odd-prime layer).** The odd-prime divisibility structure of the carry / the wall zero-sum
  event, offered as the layer independent of the 2-adic one.

---

# Group D — Sturmian side

## D01. *A Sturmian complexity clock in accelerated Collatz words* (Aug 2026)

For a fixed confinement window, the exact pruning threshold governing the decision tree is
`d*(S_fin, j, h) = ⌊2α+hβ⌋+3+j−S_fin`, so the whole horizon dependence collapses to a single global
digit `ε_h ∈ {0,1}` generated by the irrational rotation `h ↦ {hβ}` — a mechanical word of slope
`β`. Proved: the collapse, a sharp discrepancy estimate for `ε_h`'s frequency, and invariance of the
branch-count profile on the zero digit. The note states explicitly that the relation, if any,
between these resolution-rate quantities and the bit length `log₂m` of a genuine integer seed is
**open**.

**Candidates.**
- **G28 (Sturmian global digit).** `ε_h` and the cumulative count `K(h)`, with the mode
  `j*(h) = K(h)−1`: a limit-stable arithmetic quantity — of the *horizon*, not of a seed.

## D02. *Boundary-driven renewal structure in a Sturmian-modulated confined-word process* (Aug 2026)

After critical tilting the confined-word recursion is exactly a random walk with geometric downward
increments and a deterministic Sturmian ceiling, killed on exit from `[0,∞)`. Proved: exactly zero
average drift after averaging over the Sturmian phase frequencies (falsifying an earlier
negative-drift reading); the correct state space is the skew product (headroom, phase) with no
Doeblin minorization in the phase coordinate; and a localization chain showing any phase dependence
of the entrance amplitude cannot be generated by the translation-invariant far-field equation, so it
is localized at the boundary-truncated dynamics near `Y = 0`, with exact killing probability
`(1−ρ)^{y+ε(θ)}`.

**Candidates.**
- **G29 (phase-dependent entrance amplitude).** The `O(1)` amplitude of the harmonic profile, whose
  phase dependence survives every bulk normalization and is provably boundary-generated.
