# Mark survey: does any candidate quantity survive limits **and** distinguish positive integers?

**Exploratory, and negative.** Nothing here is, or may be presented as, progress toward (DE) or the
Collatz conjecture. The repository's headline theorem is an equivalence, not an exclusion; see
`docs/PROGRAMME_ENDPOINT.md` and `docs/EQUIVALENT_FORMS_OF_DE.md`.

Labels: **PROVED** (proof written out in a cited source) · **CITED** (external result) ·
**VERIFIED** (exact computation over a stated range) · **HEURISTIC** · **OPEN**.

**No computation was run for this survey.** Phases 1 and 2 are reading and screening only; Phase 3
proposes tests and does not perform them.

---

## 0. The target property, as given

A candidate **MARK** is a quantity `G` computed along an orbit (or its valuation word, or its
normalized state) such that

- **(P1) Survival.** `G` has a well-defined limiting behaviour as the depth `N → ∞` — a constant, an
  asymptotic coefficient, a residue, an invariant — that is **not** erased by normalization
  (dividing by `N`, taking logs, fractional parts).
- **(P2) Sensitivity.** That limiting behaviour **differs** between positive-integer orbits and
  **all** controls: `−1` and `−5` under `3x+1`; the fixed point `+1` under `3x−1`; the critical
  Sturmian point `Φ(1c_β)`; 2-adic non-integer points of the zero-confined dust `K`.

### The screens

| | question | failure means |
|---|---|---|
| **S1** | Is `G` a function of the valuation word alone? | fails P2 by the word-shadow cardinality barrier (Rev. 7 Thm. 9.3) |
| **S2** | Does `G`'s limit survive normalization, or disappear? | fails P1 |
| **S3** | Would `−1`, `−5`, `3x−1`'s `+1`, or the Sturmian point give the same limiting `G`? | fails P2 |
| **S4** | As a premise, is "positive integers have `G`-behaviour `X`" equivalent to (DE), to "no divergent orbits", or to `r_min → ∞`? | a restatement, not a tool |
| **S5** | Is `G` already covered by earlier work? | not new |

S1 has an exact general form in the author's own methodological note (B07, Prop. 1; A15, Prop. 2):
a diagnostic that factors through a coarse coordinate `π` is constant on the fibres of `π`, so it
can decide membership in a set `S` only if `S` is a union of fibres. The word-shadow barrier is the
instance in which the fibre over a confined word contains `2^{ℵ₀}` points of `K` and at most one
positive integer.

---

## 1. The papers read

Group A in full; Group B as selected; Group D both; Group C sampled at four; Group E as
citations/controls only. Full bibliographic data, DOIs and the untracked-source policy are in
[`SOURCES.md`](SOURCES.md). Per-paper summaries and candidate extraction are in
[`phase1/S1_quarter_gamma.md`](phase1/S1_quarter_gamma.md),
[`phase1/A_integration.md`](phase1/A_integration.md) and
[`phase1/BCD_collatz.md`](phase1/BCD_collatz.md).

| tag | paper | date |
|---|---|---|
| **S1** | Shared quarter-gamma lattice and the limits of the Thales–Ramanujan analogy | Jun 2026 |
| A01 | Local algebraicity and graded global periods on the Thales partition manifold, Rev. 2 | Jul 2026 |
| A02 | Structural layers of the Thales semicircle | May 2026 |
| A03 | Parity-complementary mollifier operators | Apr 2026 |
| A04 | `√π` as a dimensional-reduction and transition-normalization constant | Apr 2026 |
| A05 | Boundary and interior record chronologies for the two-mode oscillator spectrum | Aug 2026 |
| A06 | Strain–vorticity interaction and rotational coherence (RVP) | Sep 2026 |
| A08 | Two complementary periods, modular self-duality, and a beat frequency | Jun 2026 |
| A09 | Archimedean compensation on the Thales semicircle, Rev. 3 | Feb 2026 |
| A10/A11 | The partition-intrinsic cubic (operator-balance; adversarial study) | Aug 2026 |
| A12 | The dual diagonal and reconstruction of orthogonal hyperrectangles | 2026 |
| A13 | The Minkowski interval as a Thales coupling diagnostic | Apr 2026 |
| A14 | Spectral coupling and structure-dependent relaxation, Rev. 2 | Aug 2026 |
| A15 | The compactness partition on the period dial, V2 | Aug 2026 |
| A16 | Compactness as a thermodynamic saturation coordinate, V2 | May 2026 |
| B01 | A global occupation conjecture for the accelerated `3x+1` map, Revision 7 | 2026 |
| B02 | Transport deficits and 2-adic survival budgets | Aug 2026 |
| B03 | Conditional obstructions and launch renormalization | Aug 2026 |
| B04 | Three scales of confinement, second revision | Sep 2026 |
| B05 | Inheritance-preserving differentiation in the Collatz survivor tower | Jul 2026 |
| B06 | Pointwise survivor discrepancy in a width-two Collatz system, v2 | 2026 |
| B07 | Representation sufficiency and licensed inference | Aug 2026 |
| C01 | A bit analyzer for the Collatz carry equation | Jun 2026 |
| C02 | The positive-entropy 2-adic carry law | Jun 2026 |
| C03 | Tail-tracking and the leading-block principle | Jun 2026 |
| C04 | Finite-field zero sums in the Collatz carry equation | Jun 2026 |
| D01 | A Sturmian complexity clock in accelerated Collatz words | Aug 2026 |
| D02 | Boundary-driven renewal structure in a Sturmian-modulated confined-word process | Aug 2026 |

Repository sources consulted for S4/S5: `papers/synthesis/main.tex`, `docs/PROGRAMME_ENDPOINT.md`,
`docs/EQUIVALENT_FORMS_OF_DE.md`, `audits/record_holder_anatomy/REPORT.md`,
`audits/sturmian_irrationality/REPORT.md`.

---

## 2. The primary candidate, re-posed and screened

### 2.1 Where the ghost is, and what it does

**One sentence.** In each individual quarter stratum a transcendental CM period appears —
`J(¼) = ⅓·K(1/√2) = Γ(¼)²/(12√π)`, with `J(¾)` proportional to its *reciprocal* — and that period
**disappears** under the reflection involution `s ↦ 1−s`, i.e. under multiplication by the conjugate
stratum, leaving only an algebraic residue: a rational times `cot(πs)`, hence `π/20` at the
self-complementary residue `s = ¼`. **PROVED** (S1, Prop. 1 and eqs. (11)–(15); the author's own
sentence, p. 4: *"the product identity (13) eliminates the period and returns `π/20`"*).

The erasure is therefore **not** a depth limit. It is an involution on the parameter, and `G1` does
not transfer to (P1) as stated. It is re-posed, as instructed:

> **G1, re-posed.** The Collatz analogue of "pairing with the complementary stratum" is the sign
> involution `n ↦ −n`, which is an exact valuation-by-valuation conjugacy between `3x+1` on the
> negatives and `3x−1` on the positives (synthesis note, Thm. 7.2 proof; **VERIFIED** on every odd
> `m < 4000` to depth 300, identical words and depths). `G1` is then any quantity attached to the
> *pair* `{m, −m}` — equivalently, to the two systems at one shared valuation word.

### 2.2 Does the paired object necessarily erase the sign? **Yes — provably, and for the same reason.**

The pairing map *is* the sign involution, so any quantity attached to the pair is by construction
invariant under `m ↦ −m`: it lies in the even sector of the grading. Concretely, the two periodicity
equations carry the **same** positive carry `C_L = Σ_{i<L} 3^{L−1−i}2^{S_i}`, differing only in
which side it lands on:

```
3x+1 :  m (2^S − 3^L) = C_L ,   confinement ⟹ 2^S − 3^L < 0 ⟹ m < 0
3x−1 :  m'(3^L − 2^S) = C_L ,   confinement ⟹ 3^L − 2^S > 0 ⟹ m' > 0
```

so `m' = −m`, and the paired quantities are
`m·m' = −C_L²/(2^S−3^L)²` (a square: the sign is gone, only the height remains) and `m/m' = −1`
(constant: no information at all). This is the exact structural twin of the quarter-gamma collapse:
there the pairing multiplies a period by its reciprocal and the **period** cancels, leaving a
rational multiple of `π`; here the pairing multiplies `m` by `−m` and the **sign** cancels, leaving
the height `|m|²`.

What survives the pairing is precisely `(valuation word, S_k, C_L, |m|)` — the aggregate identity,
the confinement condition, and the denominator's magnitude. Theorem 7.2 (the sign obstruction,
**PROVED**) says exactly that no argument using only those ingredients can separate the positive
integers from the rest of `K`, because the two systems agree on all of them and disagree on the
answer. The controls make it concrete: `−1` under `3x+1` and `+1` under `3x−1` are both zero-confined
fixed points with the **identical** valuation word `1^∞`, identical `S_k` and identical height `1`.
The paired object cannot tell them apart.

> **G1: FAILS S3**, via Theorem 7.2. It also fails S5 (the same content is `audits/record_holder_anatomy`
> P3 and its corollary). This is the outcome the brief anticipated, and the re-posing does not
> rescue it: the pairing that erases the period in the integration setting is *literally* the map
> whose invariants Theorem 7.2 proves insufficient.

There is no self-conjugate point to evaluate a residual diagnostic at, either: the partition
involution `a ↔ 1−a` has the apex `a = ½` as a fixed point, and the apex-selectivity diagnostic of
A03 fires exactly there, whereas `m ↦ −m` on `Z₂^×` has **no** fixed point. The apex mechanism has no
Collatz instance at all (**G8: FAILS**, vacuously).

### 2.3 Recorded observation (observation only, no claim attached)

Individual strata carry transcendental periods while paired objects are algebraic. This parallels
the situation on the Collatz side, where the individual, unpaired object carries the irrationality
and the paired/periodic object collapses to the rational level:

| | individual object | paired / periodic object |
|---|---|---|
| integration side | `J(¼) = ⅓K(1/√2)`, transcendental CM period of `Q(i)` | `J(s)J(1−s) ∈ Q·π·cot(πs)`; at `s=¼`, `π/20` |
| Collatz side | `Φ(1c_β) ∉ Q` (critical Sturmian point, **PROVED**) | eventually periodic points of `K`: negative **rationals** of small height (signed marker, **PROVED**; **VERIFIED** on all 1717 points of period ≤ 10) |

The parallel extends to the proof mechanism, which is why it is worth recording. The Sturmian
irrationality argument fires only on *unbounded growth* of the 2-adic agreement depth
`v₂(M_n) = p_n + p_{n+1} − 1` at lower convergents; at a rational point the same quantity **freezes**
at a constant `ℓ_m` (audit Task 5: frozen at 10, 83, 568 for `m = 2, 4, 6`), and no contradiction
arises. "The period cancels under pairing" and "the agreement depth freezes at a periodic point"
are the same phenomenon in the two settings: the object that individuates is annihilated exactly
when the object is paired with, or replaced by, its periodic counterpart.

This is an observation about structure. It is **not** evidence that a mark exists, and no claim of
progress is attached to it.

---

## 3. Phase 2 — the candidate table

`G` numbering follows the Phase-1 files. "word-level" in S1 means: determined by the valuation word
alone, hence shared by the `2^{ℵ₀}`-family of Rev. 7 Thm. 9.3, of which all but countably many have
no positive-integer realizer.

| # | `G`, in one line | S1 word-level? | S2 survives normalization? | S3 controls agree? | S4 restatement? | S5 already covered? | class |
|---|---|---|---|---|---|---|---|
| **G1** | the sign-conjugate paired object `{m,−m}` | no | yes | **yes** (`−1`/`+1` identical) | — | Thm. 7.2; audit P3 | **FAILS S3** |
| G2 | the algebraic residue surviving the pairing (height `|m|`, carry `C_L`) | no | yes | **yes** | Formulation (c) border-vs-height | synthesis §7(c) | **FAILS S3** |
| G3 | stratum/transcendence class of `Φ(v)` | **yes** | yes | Sturmian point is the interesting case, not integers | — | Thm. density, Thm. Sturmian | **FAILS S1** |
| G4 | normalized tilt ↔ valuation mean `S_N/N` | **yes** | survives but is `α` on every confined object | **yes** | — | valuation-mean classification | **FAILS S1, S3** |
| G5 | order at which the parameter response leaves `Q` | no | **no**: the only natural deformation `3x+v` preserves every `a_j` on the nose, so the response is identically zero | — | — | `prop:ladder` conjugacy | **FAILS S2** |
| G6 | Clausen-type defect: existence of a square-root factorization | **yes** (any generating function of the word) | — | — | — | — | **FAILS S1** |
| **G7** | the ghost / local / period layer classification, with a grading that predicts the class in advance | no | — | by construction an *odd*-sector quantity separates `m` from `−m`; the finding is that **every** observable in the programme is sign-**even** | yes: this is Criterion 7.1(ii) restated | Criterion 7.1 | **FAILS S4**, retained as a search heuristic (§4.3) |
| G8 | parity class at the involution's fixed point | — | — | — | — | — | **FAILS**: `m ↦ −m` has no fixed point in `Z₂^×` |
| G9 | moment sequence of the orbit's empirical measure | **yes** | yes | **yes** | — | the compactness/correspondence route | **FAILS S1, S3** |
| G10 | detuning from a self-dual fixed point / log-periodic modulation in `log` scale | **yes** (ensemble/word) | yes | **yes** | — | Thm. three scales `O(1)` phase | **FAILS S1** |
| **G11** | scaled record envelope `Δ₁(N) = log₂r_min(N,0) − log₂(1/p_N(0))`, *boundedness* | **no** — `r_min` is a least **positive integer**, a minimum over a family | yes: `Δ₁` is exactly the rate-subtracted envelope | **no**: `3x−1`'s ladder is degenerate (`r₁=1, r₂=5, r₃=17` for every `N`) | **yes**: `r_min(N,0) → ∞` **is** form (b) of (DE); `Δ₁` bounded is sharp EOC | audit Q5; Conj. sharp EOC | **FAILS S4** |
| **G11′** | the **shape** of the same envelope: where the record depths fall relative to the continued fraction of `α` | no | yes | no (degenerate for `3x−1`) | **no** — `r_min(N,0)` is defined for every finite `N` unconditionally, so a statement about its *shape* is not a statement about its divergence | **partly**: M2 tested Sturmian *word* proximity, not record *placement* | **SURVIVES SCREEN** (weak) |
| G12 | record-counting coefficient `lim #records(≤X)/log X` | no | yes | no (`3x−1` terminates at 3 records) | **yes** for `c>0` (= (DE)); the *value* of `c` is not | audit §2.2 | **FAILS S4** for the property; value ranked below G11′ |
| G13 | signed defect cycle along the record ladder | no | yes | — | — | **M3/Q4: measured.** Oscillates, no trend; absolute agreement `v₂ ∈ 5…17` while `log₂m` triples | **FAILS S5** |
| G14 | sufficiency of a finite family of aggregate invariants | — | — | — | — | — | not a mark: this is the barrier (dimension-count form of S1) |
| G15 | rate-versus-offset: individuality lives in the `O(1)` intercept | no | yes (an asymptotic coefficient) | **yes**: the intercept is `log₂|m₀| + O(1)`, identical for `m` and `−m` | Formulation (c) | synthesis §7(c) | **FAILS S3** |
| G16 | entropy-deficit coordinate `D(p‖½)/p`; `I₀ = 0.0793186…` | **yes** (ensemble) | yes | **yes**: every confined object sits at `ρ = log₃2` | — | `Occupation.confined_mass_rate` (formalized) | **FAILS S1, S3** |
| G17 | coupling/alignment rather than magnitude comparison | — | — | — | yes: Criterion 7.1(iii) | Criterion 7.1 | **FAILS S4**, retained as heuristic |
| G18 | degeneracy versus transversality of a constraint intersection | no | yes | **yes**: `2^S = 3^L` is impossible by unique factorisation, so the diagnostic is constant everywhere | — | cycle drift | **FAILS S3** |
| G19 | bounded–unbounded duality | **yes** | yes | **yes** | yes: it is confinement restated | — | **FAILS S1, S4** |
| G20 | departure from a no-selection null baseline | no | yes | — | — | **N0 null model**, audit §2.7 and Q5 | **FAILS S5** |
| **G21** | height amortization `ρ_N = log₂H/S_N` | **yes** — `(A,Λ)` are generated by the word | yes, and non-trivially: `→ 0` periodic, `≥ 1` generic | separates **periodic from aperiodic**, i.e. exactly the P1-marker level; does not separate positive integers from the dust | — | Rev. 7 §5.3, Obs. 5.9 | **FAILS S1** |
| G21b | bounded prefix realizers | **yes** | — | — | **yes**: characterizes realizability exactly | Rev. 7 Rem. 9.5 | **FAILS S4** |
| **G22** | matching precision `M_j` = zero-run of the **seed's binary expansion** at bit `S_j` | **no** — reads the integer's terminating tail | the limiting statement is `M_j → ∞` once `S_j` exceeds the bit length | no | **yes**: `M_j → ∞` for a confined seed is exactly form (d), "no zero-confined 2-adic integer has an expansion ending in `0^∞`" | Rev. 7 §9.2; transport-budget route | **FAILS S4** |
| G22a | cumulative regeneration budget | no | bounded by `⌊log₂m₀⌋+1` | — | — | Rev. 7 §9.2 | **FAILS S2** (the budget is finite, so no limiting behaviour) |
| G23 | terminal-repetition fraction, frontier `1 − log₃2` | **yes** | yes | **yes** | — | launch renormalization; the closing hypothesis is itself open | **FAILS S1** |
| G24 | `O(1)` renewal phase, Beatty jump sets of `β` | **yes** (ensemble) | yes — survives the `2^{−I₀N}N^{−3/2}` normalization exactly | **yes** | — | Thm. three scales | **FAILS S1, S3** |
| G25 | normalized branch asymmetry `χ_ℓ → ⅓` | — | the source proves **no autonomous scalar law** `χ_{ℓ+1}=F(χ_ℓ)` exists | — | — | B05 | **FAILS**: tower-level, no per-orbit instance |
| G26 | order–clock gate `ord_{2^ℓ}(A) > 32` | no | yes | **yes**: a function of `ℓ` only, identical for every orbit | — | B05 | **FAILS S3** |
| **G27** | signed survivor discrepancy `E₇ − E₃` (arithmetically **realized** counts, not formal word counts) | **no** — `E_c` counts which words positive integers attain | the limiting statement is the open positivity `E₇ > E₃` whenever `B₃ > 0` | **untested**; the model has no published sign control | **not established**: B06 names the obstruction as conditional anti-concentration of injected 2-adic frontier bits, not as (DE) | B06, open; verified to `ℓ = 27` | **UNCLEAR** |
| G28 | Sturmian global digit `ε_h`, count `K(h)` | **yes** — a function of the horizon, not of a seed | yes | **yes** | — | D01, which states the relation to `log₂m` is open | **FAILS S1** |
| G29 | phase-dependent entrance amplitude of the tilted process | **yes** (ensemble) | yes; provably boundary-generated | **yes** | — | D02 | **FAILS S1** |
| G30 | bit depth `ℓ(D) = v₂(Q(D) + Ξ_α)` | **yes** — `Q(D) = C_L(D)/(2^S−3^L)` is a function of `D` | freezes (saturation plateaus) | **yes**: the freeze is exactly the rational-point control of the Sturmian audit | — | C01/C03; audit Task 5 | **FAILS S1** |
| G31 | limiting residue measure `µ_ρ`; Haar iff `ρ = ½` | **yes** (shell ensemble) | yes | **yes**: every confined object has `ρ = log₃2` | — | C02 | **FAILS S1, S3** |
| G32 | odd-prime attainment layer / wall zero-sums | **yes** — `C_L` and `r(D)` are word-determined | — | — | — | C04 census: uniform density, no obstruction, "composite-wall incompatibility theorem" **withdrawn**; Rev. 7: the odd-prime support of `B_N` is unconstrained | **FAILS S1**, and a **VERIFIED** null |

**Tally: 32 candidates. 30 FAIL, 1 UNCLEAR (G27), 1 SURVIVES the screen weakly (G11′).**

### 3.1 The three structural reasons everything fails

Read down the table and the failures collapse into three modes, which is more informative than the
count.

1. **Word-level (S1), 14 candidates.** Every quantity built from the valuation word — the carry
   `C_L`, the projective coordinate `Q(D)`, the bit depth `ℓ(D)`, the entropy rate, the renewal
   phase, the residue measure, height amortization, the Sturmian clock digit — is shared by `2^{ℵ₀}`
   points of `K` and at most one integer per word. This is the fibre criterion of B07/A15 applied to
   the coarsening "integer ↦ its valuation word".
2. **Sign-even (S3), 8 candidates.** Every quantity that is not word-level turns out to be invariant
   under `m ↦ −m`: the paired object, the height, the `O(1)` intercept, the degeneracy indicator, the
   order–clock gate. This is Theorem 7.2 seen from the candidate side, and §2.2 shows the primary
   candidate `G1` fails here by construction rather than by accident.
3. **Restatement (S4), 5 candidates.** The candidates that *do* use positivity and *do* separate the
   controls turn out to be exactly the known equivalent forms: `r_min(N,0) → ∞` is form (b);
   `M_j → ∞` is form (d); bounded prefix realizers characterizes realizability; the record-counting
   coefficient being positive is (b) again. The survey therefore reproduces, from a completely
   different direction, the conclusion of `EQUIVALENT_FORMS_OF_DE.md`: a candidate that is sharp
   enough to see integrality is sharp enough only because it *is* the question.

There is a fourth, smaller mode worth naming because the integration corpus supplies it explicitly:
**refinement of the wrong target** (B07, Controlled Example II). A quantity may converge beautifully
and quickly to a limit that is not the one wanted, with a floor no further computation touches. G16
is the instance here: `I₀` is exact, formalized and completely insensitive, and A15's Correction 1
shows the inverse problem for it is not even single-valued.

---

## 4. Phase 3 — ranked shortlist, with the cheapest decisive test for each

Tests are **proposed and pre-registered, not run**. Each entry states the measurement, the controls
it must be run against, the outcome that kills it, and an honest prior.

### 4.1 Rank 1 — **G11′**, the placement of the record depths against the continued fraction of `α`

**Status: SURVIVES SCREEN (weakly).** It is the only candidate that is not word-level, is not
sign-even, and is not a restatement — because `r_min(N,0)` exists for every finite `N` whether or
not (DE) holds, so a statement about the *shape* of the record ladder is not a statement about its
divergence.

**Where it comes from.** A05 proves that the scaled record envelope `E(H) = H²·min_{h≤H}ε` is, for a
quadratic-irrational parameter, an *exactly log-periodic* function of `log H` with period `log λ`
(`λ` the fundamental unit), with exact `liminf = ¼` and `limsup = (57+40√2)/28`; that for rational
parameters the envelope instead collapses or the chronology terminates; and that for `e` and `π` the
records track continued-fraction convergents in arithmetic-progression runs, with run length
governed by the partial quotients (for `π`, the run toward `355/113` reflecting `a = 292`).

**The correct transplant, and the correction it forces.** `α = log₂3` is **transcendental**
(Gelfond–Schneider, **CITED**), not quadratic, so there is no fundamental unit and **no exact
log-period should be expected**. The `e`/`π` regime of A05 is the right analogue: the prediction is
that record *placement* is organized by the convergent denominators of `α`,
`q_n = 1, 1, 2, 5, 12, 41, 53, 306, 665, 15601, …`, and by the large partial quotients, not by a
period.

**The measurement (cheap; the data already exists).** From `audits/record_holder_anatomy`: the 24
distinct record holders certified over `N = 1…346`, each with the interval of `N` it holds.
Compute (i) the depths `N_j` at which the record holder changes, (ii) the gaps `N_{j+1} − N_j`, and
(iii) the scaled envelope `Δ₁(N) = log₂r_min(N,0) − log₂(1/p_N(0))` restricted to those depths.
Test whether the change depths or the local maxima of `Δ₁` concentrate near the `q_n`, or near
`p_n = ⌊q_nα⌉`, beyond what a uniform placement at the same rate predicts.

**Pre-registered controls (all four required).**
- **`3x−1` (the sign control).** Its ladder is degenerate — `r₁(N)=1, r₂(N)=5, r₃(N)=17` for every
  `N` up to the computed cap — so it must show **no** structure. A pattern that also appears here is
  not about the sign and is dead on arrival (record-holder audit, control C4).
- **The critical Sturmian realizers `r(D_N)`** (control C2). Their word *is* built from the
  convergents, so they must show the structure strongly; if they do not, the measurement is not
  measuring what it claims.
- **Random confined words and shuffled surrogates** (control C3), which must show nothing — and
  which is where the audit's selection-effect warning bites: the record holders are a minimum over a
  huge family, so any comparison against a single draw measures the size of the family, not a
  property of the extremes.
- **`3x+v`, `v` odd.** The map `m ↦ vm` sends `3x+1`-confined integers to `3x+v`-confined integers
  with identical words, so `r_min^{(v)}(N) ≤ v·r_min^{(1)}(N)`. If the placement structure is real it
  must survive this embedding; if it moves, it is an artefact of the specific `v = 1` arithmetic.

**Kill condition.** Any of: the effect appears in the shuffled surrogates; it appears in `3x−1`;
it disappears once the null is taken to be uniform placement at the measured rate
(`Occupation.confined_mass_rate` + the exact `p_N(0)` of Prop. `prop:density`) rather than a naive
uniform.

**Prior: low.** Three reasons, all from existing work. The record-holder audit's Q1 verdict is that
every pattern found in these 24 holders reduced to a proved lemma, to the last-maximum structure, or
to a selection effect; M2 already found the holders are **not** Sturmian-adjacent (1–3 shared
valuations at depths to 236); and the effective sample size is about 7, the holders being strongly
serially correlated (`ΔAICc = 0.29` between a drift and a bounded-residual model). The test is worth
running because it is nearly free and measures something M2 and Q5 did not — *placement* rather than
*word agreement* or *size* — not because it is likely to find anything.

**Even if it succeeds, what it would be.** A statement about the shape of a sequence that exists
unconditionally. It would bear on Conjecture (sharp EOC), not on (DE). Nothing in this route reaches
the open problem.

### 4.2 Rank 2 — **G27**, the signed survivor discrepancy `E₇ − E₃`

**Status: UNCLEAR.** It is the one candidate defined by *which words positive integers actually
attain* rather than by the words themselves, and B06 does not reduce it to (DE): the stated
obstruction is conditional anti-concentration of newly injected 2-adic frontier bits. It is
therefore not screened out — but it is also not screened *in*, because the one screen that matters
has never been applied to it.

**The cheapest decisive test: run the sign control.** Define the identical width-two model for
`3x−1` (`m ↦ (3m−1)/2^d`, `d ∈ {1,2}`, `d ≥ 3` leaves the model), with the same terminal cells and
the same two source classes, and compute `E₇ − E₃` over `ℓ ≤ 27` — the range already exactly
verified for `3x+1`. Exact integer arithmetic; the existing enumeration code should port with the
constant changed.

- **If `E₇ ≥ E₃` also holds for `3x−1`**, the discrepancy is sign-blind and G27 **fails S3**, joining
  the eight candidates of failure mode 2. Given Theorem 7.2 and the identical `S_k` combinatorics of
  the two systems, this is the expected outcome.
- **If the inequality reverses or fails for `3x−1`**, G27 is the first quantity in the corpus known
  to separate the two systems while not being a restatement of (DE) — at which point the next
  question, and only then, is whether the width-two truncation (`d ≥ 3` leaves the model) is doing
  the separating work rather than the arithmetic.

**Second control, if and only if the first is passed.** Recompute with the `d ≥ 3` escape replaced
by `d ≤ 3`, i.e. a width-three model. A separation that vanishes when the truncation widens is a
property of the model, not of `3x+1`.

**Prior: low, but the test is the cheapest in this report and its negative outcome is worth
recording.** B06's own framing — "the unresolved obstruction is conditional anti-concentration of
newly injected 2-adic frontier bits" — is the same anti-concentration wall that Observation
`obs:cycle` records on the cycle side, where the available machinery is ineffective.

### 4.3 Rank 3 — **G7**, the sign-parity enumeration (a heuristic, not a mark)

Not a candidate; it fails S4 as Criterion 7.1(ii) restated. It is retained because it converts that
criterion into a **finite, mechanical check** that costs nothing and has a recordable outcome either
way:

> Grade every observable the programme uses by its parity under `m ↦ −m`, and record the sector.

Predicted result, from the reading: **every one is even** — the valuation word, `S_k`, `R_k`, the
carry `C_L`, `p_N(c)`, `I₀`, `r_min`, `Δ₁`, `ρ_N`, `ℓ(D)`, `Q(D)`, `M_j`, the height `|m|`. That
would be Theorem 7.2 exhibited as a table rather than as an implication, and it makes the demand on
any future tool concrete and checkable in one line: *exhibit an odd-sector observable with a
non-vanishing normalized limit.* The value of the exercise is that it is falsifiable by a single
counterexample, and that a reader can apply it to a proposal in seconds.

### 4.4 Ranked below the line, and why they are not proposed

`G12` (record-counting coefficient): its qualitative form is (DE); its quantitative value is
determined by `G11′` and by sharp EOC, so it adds nothing the Rank-1 test does not already measure.
`G22` (matching precision): exactly form (d); no test is proposed because the statement to be tested
*is* the open problem. `G13`, `G20`: already measured, with null results recorded in
`audits/record_holder_anatomy` M3/Q4 and §2.7.

---

## 5. Verdict

**Of 32 candidate marks extracted from 29 papers, none satisfies both (P1) and (P2).** Thirty fail
outright, under three recurring modes — word-level, sign-even, restatement. One (`G27`) is genuinely
undecided and is decided by one cheap computation that has never been run. One (`G11′`) survives the
screen, but only as a statement about the shape of a sequence that exists whether or not (DE) holds,
and its prior is low for reasons the existing audits already established.

**The primary candidate, the `1/π` ghost, fails — and fails in an informative way.** Its erasure
mechanism is an involution, not a limit; the Collatz instance of that involution is the sign map;
and the invariants of the sign map are exactly the ingredients Theorem 7.2 proves insufficient. The
ghost does not merely fail to transfer. It transfers *precisely onto the known obstruction*.

That is a valid, recordable negative result, and it is the result. No claim of progress toward
(DE) or toward the Collatz conjecture is made or implied by anything in this report.
