# VERDICT.md — what was actually learned

## The five required answers

### 1. Did the percolation amplification method yield a genuine new arithmetic mechanism applicable to EOC?

**No.** And the reason is specific rather than atmospheric: **Lemma 4.8 exists
to delete an inverse multiplicity, and EOC has no inverse multiplicity to
delete.**

Lemma 4.8's achievement, in the paper's own words, is that "joint undoing is
injective *without retaining either code*. This stronger assertion removes the
factor `W^{2k}` from this class." That factor is there because the percolation
splice is non-injective: many input bit tuples produce the same output field, so
the inverse must be *coded* (selected indices plus seam gaps), and the code count
`W^k ≈ (C M^s log M)^k` is the multiplicity.

In EOC the corresponding correspondence is a **bijection**. By
`leastRealizer_unique` and `residue_pinning` (`EOC/Realizer.lean` ll. 478, 543),
each `0`-confined word of length `N` is realized by exactly one odd residue class
mod `2^{S_N+1}`, and the class determines the word. Verified by brute force at
`N = 1..14`: **maximum fibre `= 1` at every depth, 0 violations.** The inverse is
a division, the code is empty, the multiplicity is `1 = 2^0`. The technique
solves a problem we do not have.

Three further obstructions are independent of that one and of each other:

* **No spectral seed.** Proposition 4.3 needs `H = log(1/‖K‖) > 1`, obtained in
  Lemma 4.4 from `ρ < 1`, i.e. from **nonamenability**. Every kernel with row
  and column sums `1` on a **finite** set has `‖K‖_{ℓ²} = 1` exactly
  (Proposition S), and the EOC state space at depth `N` must be the finite
  residue space mod `Q_N` for `p(N,c)` to mean what `confined_mass_rate` says.
* **No independent second field.** The splice requires a distinguished field `D`
  and fresh i.i.d. fields `E_1,…,E_k`, exchanged on masks that preserve the total
  number of open bits so that input and output have *exactly* equal probability.
  There is one arithmetic world; the sibling suffixes are coordinates of the
  branch node, and their realizers are already counted in `C_N`.
* **The architecture is aggregate-to-aggregate.** Hypothesis (4.1) is about a
  measure and the contradiction is against that same measure. The paper never
  passes from an aggregate to an individual. The EOC target is one fixed integer.

**What did transfer** is the *shape* of the argument, as the criterion `(AMP*)`
of `AMPLIFICATION_CRITERION.md` §4 — count an index set against `C_N` through a
map with controlled fibres. That reframing is the genuine borrowing, and it is
what made answers 2–4 provable rather than speculative.

### 2. Can a single permanently confined positive odd integer be proved to generate additional distinct confined realizers?

**It can generate them, and the generation is provably worthless.**

Generation is easy and better than expected. The **down-shift** at a branch node
— replace a digit `d_j` by a smaller admissible `e` and keep the suffix — is
**total and defect-free**: lowering a digit lowers every later partial sum, so
`2^{S_i} ≤ 3^i` is inherited automatically. Measured survival rate exactly
`1.0000` at every branch node and every suffix for `N = 3..12`. It also
preserves **positive-integer realizability**, not merely symbolic admissibility:
the output is `r_{P‖e} + 2^{σ}c'`, an honest odd integer with the recombined
orbit word.

It is worthless for two independent proved reasons.

* **Theorem 1 (the hard cap).** Any family of pairwise distinct `0`-confined
  residue classes has `mu(B_N) ≤ mu(C_N) = 2^{-I_0N+o(N)}`. So **no injection
  into the confined population can amplify its mass** — not permutations, not
  lifts, not any map whatsoever. The brief asked whether the mechanism creates
  mass or merely rearranges residues; the answer is that *nothing* can create
  it, because `confined_mass_rate` is the accounting of a conserved budget and
  anything one seed generates is a subpopulation of its own parent.
* **Theorem 4 (the surplus is polynomial).** Instantiating `(AMP*)` with the
  down-shift gives an index set `I_N` with every fibre
  `≤ (α−1)N(N+1)/2`, hence `#I_N ≤ O(N²)·n_N`. `(AMP*)` needs
  `#I_N ≥ 2^{(g+δ)N}` with `δ > 0` fixed. **Short by an exponential.**

### 3. Does the growth defeat the known exponential confinement-mass rate, or is it absorbed by multiplicity and height costs?

**Neither, and the distinction matters.** It is not "absorbed" by a competing
cost that one might hope to optimise down: **the growth and the cost are the
same number.**

> **Theorem 5.** For *any* map `Φ_N : I_N → C_N`,
> `#I_N = Σ_y #Φ_N^{-1}(y) ≤ n_N · max fibre`, hence
> `δ_N ≤ (log_2 max fibre)/N` identically.

So `(AMP*)`'s two hypotheses — large domain, small fibres — are upper and lower
bounds on one quantity, separated only by `n_N = 2^{gN+o(N)}`. In percolation,
gain and cost are both linear in `k` and the *ratio* contracts by a fixed factor
`c_ξ < 1`, which is the whole engine; here the ratio is identically `1` and
there is no admissible region at all.

This session also caught itself being fooled on exactly this point, and the
correction is the most useful computational result in the package. The measured
index surplus `δ_N` reads `0.2125, 0.2084, 0.2115, 0.1985` at `N = 8,10,12,14`
and looks like a stable positive constant. It is not: `#I_N/n_N` grows
**linearly** in `N`, and `log_2(N/2)/N` equals `0.2005` at `N = 14`, `0.0564` at
`N = 100`, `0.0090` at `N = 1000`. A plateau across seven consecutive even
depths was a slowly varying logarithm. Theorem 4 settles it by proof.

In the paper's own currency the gap is one line. Financing requires
`π ≥ n^{-β}` with `β < 1/2` (forced by `β + s < 1`, `s = 1/2 + ε`). Matching
`n ↔ 2^N`: the **whole confined population** has `β_eff = I_0 = 0.0793 < 1/2`
and *would* finance the construction; **one seed's cylinder** has
`β_eff = alpha = 1.5850` and does not, short by `n^{1.085} = 2^{1.085N}`. That
pair of numbers is the aggregate/pointwise gap of the EOC program expressed in
the percolation paper's variables, and it is the single most useful quantity
this investigation produced. Closing it would mean recovering the *entire*
confined population from one seed — simultaneously the maximum conceivable and,
by Theorem 1, still insufficient.

### 4. Did we obtain a new unconditional theorem, a restricted theorem, a conditional reduction, or only a useful obstruction?

**Unconditional theorems — all of them negative or structural — plus two exact
positive identities. No conditional reduction, and no new hypothesis was
introduced.**

New and unconditional:

* **Theorem 1 / Corollary 1a** — the proposed mass criterion is **vacuous**: its
  hypothesis is unconditionally false, so the implication is logically
  equivalent to the target and decomposes nothing. It asks for more confined
  classes than exist.
* **Theorem 3** — the word ↔ realizer-class correspondence is a bijection;
  multiplicity exactly `1`.
* **Theorem 4** — the down-shift's fibres are `O(N^2)`; its index surplus is
  `O(log N/N) → 0`.
* **Theorem 5** — index surplus and fibre cost are the same quantity, for every
  map into `C_N`.
* **Proposition S** — no doubly stochastic kernel on a finite set contracts.
* **Proposition D** — the exact price of a drifting confinement budget:
  rate `J(alpha+θ)` for `0 ≤ θ < 2-alpha`, and `0` beyond
  `2 - alpha = 0.4150375`. (Upper bound proved; lower bound a sketch, labelled
  as such.) **A linear defect makes the target strictly harder, not easier** —
  the only escape from Theorem 1's fixed-`c` scope is closed in the direction
  that would have helped.

Exact positive identities, both verified by brute force with zero violations:

* **Theorem B** — `mu(C_N) = p(N,0)` *exactly*, for every `N`. The bridge from
  the repository's symbolic dyadic mass to residue density is an identity, not
  an asymptotic. (`N = 1..14`, all odd residues mod `Q_N` enumerated.)
* **Proposition W** — `p(N,c) = P[S_j ≤ alpha j + c, ∀ j ≤ N]` for i.i.d.
  Geometric(1/2) letters. The dyadic mass *is* that probability; this is why
  `I_0 = J(alpha)` and why `2 - alpha` is the budget that kills the rate. It has
  **no pointwise content**, and is never applied to a particular orbit.

Also delivered: **a useful obstruction catalogue** (`OBSTRUCTIONS.md`), with
three of my own claims refuted on exact examples and recorded as refuted rather
than redefined — including one, the `δ ≈ 0.21` plateau, where numerics alone
would have produced a false positive.

The second route (§9 of the brief) produced **no new invariant**: the candidate
— `m` is simultaneously the unique least realizer of its own word at every depth
— is equivalent to `r_min(N,0)` being bounded, i.e. to the target itself, and is
reported as a restatement.

### 5. What is the single smallest missing lemma that would genuinely advance pointwise divergence exclusion?

> **(LEFT-TAIL).** There exist `C ≥ 1`, `B ≥ 0` such that for every `N`,
> ```
>    #{ m odd, m < X : 2^{S_j(m)} ≤ 3^j for all j ≤ N }  =  0
>        whenever    X  ≤  C^{-1} N^{-B} / p(N,0) ,
> ```
> equivalently `r_min(N,0) ≥ C^{-1} N^{-B}/p(N,0)`.

**Why this one.**

* **It suffices.** `1/p(N,0) = 2^{I_0N-o(N)}` by `confined_mass_rate`, so
  (LEFT-TAIL) forces `r_min(N,0) → ∞`, and by Lemma T that is exactly the
  pointwise target `C`. It is not a restatement: Lemma T's equivalence is with
  `r_min` *bounded*, and (LEFT-TAIL) supplies a quantitative lower bound that no
  counting statement can.
* **Its content is precisely the absence of an additive term.** The same bound
  with `+ C N^B` on the right is useless — at a fixed `X_0` the additive term
  alone permits a confined seed at every depth. This independently reproduces,
  from a new direction, the repository's recorded position that placement is
  Open Problem C and that the obstruction is the additive term.
* **It asks for very little.** Any `C`, any polynomial `N^B`. It asks only that
  the record seed's advantage over the equidistribution mean stay
  **subexponential** — not bounded, not small, just `2^{o(N)}`.
* **It is where the difficulty provably is.** Measured here: the bulk of the
  confined population obeys equidistribution to within **`1.6%`** at every depth
  up to `24`; and `rho(N)/r_min(N)` climbs to `17.34` and then falls *below* `1`
  at each record transition, oscillating in a bounded band over `N = 4..108`.
  **The aggregate statistics are correct, and that is exactly why they say
  nothing: the whole problem is one atypical integer per range, beating the mean
  by a bounded factor — invisible to every exponential-rate argument,
  `confined_mass_rate` included.**

## Scope, stated plainly

* Nothing here proves, advances, weakens, or conditionally establishes the
  **Collatz conjecture**, and nothing here is a proof of EOC's pointwise
  divergence exclusion.
* The percolation paper is **not** claimed to prove anything about Collatz. It
  was read for its mechanism; its theorem concerns Bernoulli bond percolation on
  nonamenable quasi-transitive graphs.
* `confined_mass_rate` is **source-backed**, not Lean-verified here: **no `lake
  build` was run and no dependency chain was audited in this session.**
* All closures above apply to their precise formulations. None is an
  impossibility claim about Fourier, combinatorial or probabilistic methods in
  general. Theorems 1, 3, 4, 5 close *amplification against the confinement mass
  rate*; they say nothing about a contradiction derived against some different
  proved quantity.
* The transfer **does not work**, and this is reported as a carefully proved
  negative rather than dressed up as a conditional reduction whose hypothesis
  would have been the original conjecture in new notation.
