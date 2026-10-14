# VERDICT.md

## The six required answers

### 1. Does the exact confined-mass law genuinely strengthen the López–Stoll critical-density analysis, or only re-express an existing large-deviation estimate?

**Neither, in the direction asked — it turns out to *contain* the López–Stoll
real-analytic object exactly, which is a strictly more useful outcome.**

The mass law's own content is a re-expression: `p(N,c) = P[S_j ≤ αj + c ∀j ≤ N]`
for i.i.d. Geometric(1/2) letters is an identity, and `I₀ = J(α)` with
`J(s) = s(1 − H₂(1/s))` is the ordinary Cramér rate. Nothing there strengthens a
density analysis, because López–Stoll's statements are about `liminf h/ℓ`, a
pathwise quantity, while the mass law is about a measure.

What *does* happen is an exact identification. From `Φ(2^{d_0}+2^{d_1}+…) =
−Σ_i 2^{d_i}/3^{i+1}` with the `1`-positions at `d_i = S_i`:

```
   Φ_R(v) = −(1/3) Σ_{i≥0} 2^{−Δ_i} ,        Φ_R(u^{(S_N)}) = − q_N / 3^N ,
```

where `q_N` is the EOC carry. **López–Stoll's real partial sums are the
normalized EOC carry**, and their devil's-staircase object is the carry's limit.
Combined with the carry identity `2^{S_N}m_N = 3^N m_0 + q_N` this gives the
master identity, verified exactly with 0 violations:

```
   Φ_R(u^{(ℓ)}) = m_0 − (2^ℓ/3^h) T^ℓ(m_0) ,
   Σ_{i<N} 2^{−Δ_i} = 3(2^{−Δ_N} m_N − m_0) = 3 m_0 (2^{E_N} − 1) ,
```

so `Φ_R(v)` converges ⟺ `q_N/3^N` converges ⟺ `Σ 2^{−Δ_i} < ∞` ⟺ `Σ 1/m_k < ∞`.
The two frameworks are the same object in different coordinates. That is the
bridge the brief was looking for; it is a dictionary, not a strengthening.

### 2. What does the 2021 argument actually establish about rational 2-adic conjugacy values, after its real-to-2-adic reasoning is audited?

**Securely: only the `liminf < β` branch, which is Monks–Yazinski (2004) and
Lagarias, not new. The `> β` branch — where the preprint's content lies — does
not survive.**

Four findings, in order of severity:

* **The real→2-adic step is invalid.** The paper argues `Φ_R(v)` irrational ⟹
  `Φ(v)` aperiodic "because the irrational `Φ_R(v)` does not admit an eventually
  periodic 2-adic expansion". Equations (15)–(16) only say the 2-adic digits of
  `Φ(v)` are read off from the partial sums — true regardless of whether the real
  series converges, since the partial sums are the *same rationals*. The sentence
  conflates the real number with the 2-adic one. **The discrepancy is explicit
  and verified:** for a positive odd seed, `Φ(v) = m_0` while
  `Φ_R(v) = m_0(1 − 2^{E_∞})`; for `m_0 = 27` at `N = 8` the real partial sum is
  `−1.405426002` against the 2-adic value `27`. So `Φ_R(v) ∉ Q_odd` is perfectly
  consistent with `Φ(v) = m_0 ∈ Q_odd`, and branch 1's conclusion does not follow.
* **Lemma 24 shares the conflation** in its `ζ ∈ Q_odd` sub-case ("`v` is the
  aperiodic parity vector of `ζ`" presupposes `Φ_R(v) = Φ(v)`).
* **The trichotomy presupposes that `lim h/ℓ` exists.** Nothing forces it. What
  steps 1–2 support, with no existence assumption, is `liminf(h/ℓ) = β`, with
  `limsup` unconstrained. Theorem 1's unqualified "`lim = β`" overstates it.
* **The repaired branch 1 is already a theorem.** Stated in `R` only, it says a
  near-critically-confined orbit has `Σ 2^{−Δ_i} < ∞`, i.e. `Σ 1/m_k < ∞` — which
  is Curry (2026) Proposition 3.1 for divergent orbits. So the repair adds
  nothing, and the unrepaired conclusion is unavailable.

Theorem 1 is therefore recorded as an **unaudited / incomplete dependency** and
nothing in this package rests on it. The 2009 paper is refereed and sound; its
abstract itself says only that its examples *"suggest"* full complexity, and it
contains no density theorem.

**Consequence for EOC:** after the audit, López–Stoll adds **no** restriction on
a hypothetical permanently zero-confined positive integer beyond asymptotic
confinement — which zero confinement already gives. Neither `Δ_N = o(N)` nor
`liminf Δ_N/N = 0` is available.

### 3. What is the strongest rigorous statement about the near-critical return behavior of a hypothetical permanently confined positive integer?

Two statements, the second conditional on an external theorem.

> **Theorem R [P].** If `m_0` is odd and `m_0,…,m_{N−1}` are pairwise distinct,
> then for every `w ≥ 0`
> ```
>   #{ i < N : Δ_i ≤ w } ≤ 3 m_0 2^w (2^{E_N} − 1) ≤ 3 e^{7/9} m_0 2^w N^{1/9} ,
> ```
> `3e^{7/9} = 6.529890`. Unconditional; verified on 9 seeds with 0 violations,
> and the injectivity hypothesis shown load-bearing by a control that fails by
> five orders of magnitude past the injective depth.

> **Corollary R1 [P + Curry, external].** Along a divergent orbit,
> `#{ i : Δ_i ≤ w } < ∞` for every fixed `w`. **A divergent positive-integer
> orbit enters any fixed-width near-critical band only finitely often.**

So constant-width returns are excluded; and up to depth `N` there are at most
`O_w(m_0 N^{1/9})` of them, a density of `O(N^{−8/9})`.

**What remains open is the regime the mass concentration points at.** Under the
conditioned measure the typical deficit is `o(N)` (Theorem M4), and
log-width, sublinear-width (`√N`), and `liminf Δ_N/N = 0` returns are all open —
with every tool in this package vacuous there, because `2^{w(N)}` with `w`
superlogarithmic swamps `N^{1/9}`.

### 4. Can the EOC carry or realizer congruence convert the mass concentration theorem into a deterministic restriction not already implied by bounded drift, finite-prefix packing, or Curry?

**It converts the *carry identity* — not the mass concentration — into one; and
the result is a counting generalization of an existing repository theorem, with
the same mechanism and the same constant. Honestly: a sibling, not an orphan.**

Setting the return count equal to `N` and `w = B log₂N + C`, Theorem R becomes
`N^{8/9−B} ≤ 3e^{7/9}·2^C·m_0`, which is **verbatim**
`LogCorridor.logFloor_window_bound'`, constant included. What is new is only the
hypothesis: the existing theorem needs a drift floor at **every** prefix;
Theorem R needs nothing and bounds the **number** of returning indices. That is
exactly the "returns versus floors" distinction the brief asked about, and it is
the entire advance.

**The mass concentration itself converts into nothing**, and for a structural
reason: it is a statement about a measure on words, and witness **W1**
(`d_j = 1` for all `j`) is a `0`-confined word sitting in the
exponentially-penalized region at every `N`. Statistical scarcity caps no
individual — the same wall as in the previous session's package.

**No new logarithmic obstruction is claimed.** `Σ 2^{−Δ_i} < ∞` fails exactly at
`Δ_i ≤ log₂ i`, so Corollary R1 re-derives the **harmonic** barrier `B = 1`,
weaker than the repository's unconditional `8/9` and Curry's `1.0358567`. Three
independent routes — conditioned measure, harmonic packing, carry identity — all
stop at `Δ ~ log N`, because all three are driven by a `Σ1/k` budget.

### 5. Did we establish a genuinely new theorem, a meaningful restricted result, a conditional reduction, or only another precise obstruction?

**A dictionary, one restricted theorem, and a refutation of a published proof
step. No conditional reduction, and no new hypothesis was introduced.**

* **New and exact [P]:** the identification `Φ_R(u^{(S_N)}) = −q_N/3^N` and the
  master identity (B1–B3); the four-way equivalence
  `Φ_R` converges ⟺ `q_N/3^N` converges ⟺ `Σ2^{−Δ_i}<∞` ⟺ `Σ1/m_k<∞`; the
  two-clock lemmas C1–C3 with the complete ordinary sequence handled; the full
  implication lattice `A..G` with four exact `0`-confined witnesses; `J(s)` and
  the conditional estimate M4; the explicit moving band U2–U3 with
  `κ = 0.438032659`; Theorem R; Theorem S; and X1 (`v₂(m_0+1)−1`), X2.
* **Restricted theorem [P]:** **Theorem S** — no divergent positive-integer orbit
  has `(w,G)`-regular near-critical returns for fixed `w, G`; explicitly,
  `N^{8/9} ≤ 3e^{7/9} m_0 2^w G`. Verified, 14 rows, 0 violations. Narrow, and
  labelled as a counting wrapper on a known theorem.
* **Refutation [R]:** the real→2-adic step of [2021] Theorem 1, with the exact
  discrepancy exhibited. The theorem may still be true; its proof as written does
  not establish it.
* **Obstructions [R]:** Diophantine leverage from integrality of `q_N` (blocked,
  `3^N L − q_N → ∞`); Theorem R past the log barrier (blocked); iterating
  Theorem R (blocked).
* **Three of my own errors**, caught by exact checks and corrected rather than
  rescued: a non-confined first draft of the `D`-not-`E` witness; `X1` off by one
  (`v₂(m_0+1)` → `v₂(m_0+1)−1`); and `κ = 1.3195` → `0.438032659` via the closed
  form `J′(s) = 1 + log₂((s−1)/s)`.

### 6. What is the smallest independently motivated arithmetic lemma that could actually move the pointwise problem forward?

> **(SUBLINEAR-RETURN).** There exist `C ≥ 1`, `θ ∈ (0,1)` and `B ≥ 0` such that
> for every odd `m_0` with pairwise distinct states through `N`,
> ```
>   #{ i < N : Δ_i ≤ N^θ }  ≤  C m_0 N^{B} ,      with  B < 1 .
> ```

**Why this one.**

* **It is the exact next step of Theorem R.** Theorem R proves the case
  `w` constant with `B = 1/9`; the open content is replacing the factor `2^w` —
  which is `2^{N^θ}` and ruinous — by a polynomial. Nothing else in the chain
  needs to change.
* **It is independently motivated, not a restatement.** It is a statement about
  how often distinct integer states can crowd near the critical line, in the same
  currency as `sum_inv_orbit_le` — the repository's own pigeonhole — and not about
  divergence.
* **It would reach past every barrier here.** With `B < 1` it excludes
  `(N^θ, G)`-regular returns for every fixed `G`, hence by Theorem S's argument
  caps the injective depth, hence excludes the sublinear-width regime that
  `PRIOR_DETERMINISTIC_BARRIERS.md` §5 identifies as the frontier — the one place
  where bounded drift, finite-prefix packing, Curry, and Theorem R are all
  vacuous.
* **It is where the obstruction provably is.** Theorem R's proof loses exactly
  the factor `2^w` and nothing else; the harmonic budget `7/3 + (1/3)log N` is
  used optimally. So the whole gap is the conversion of a `2^w` penalty into a
  polynomial one.

## Scope, stated plainly

* **Nothing here proves, advances, weakens, or conditionally establishes the
  Collatz conjecture, or EOC's pointwise divergence exclusion.** Theorem S
  excludes one regularity pattern, not divergence.
* **No conditional hypothesis equivalent to divergence exclusion was
  introduced.** Corollary R1's only external input is Curry's reciprocal
  summability, a published theorem about divergent orbits, source-reported and
  not read here.
* **No Lean verification is claimed.** No `lake build` was run; every Lean entry
  is source-backed by reading the file.
* **Attribution.** The geometric model, the conjugacy formula `Φ`, the carry and
  drift identities, the Cramér rate `J`, and the harmonic packing bound are all
  **prior**; the 2009 López–Stoll continued-fraction expansion is refereed and is
  theirs; the 2021 preprint's claims are distinguished from it throughout.
* **Every closure above applies to its precise formulation**, and none is an
  impossibility claim about real-analytic, Fourier, combinatorial, or
  probabilistic methods in general.
