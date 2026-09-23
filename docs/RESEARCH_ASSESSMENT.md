# Research assessment: what this repository has established, and what to do next

*Written September 2026. No code, no Lean, and no paper was changed to produce it.*

Every claim below carries one of:

* **PROVED** — machine-checked or proved in this repository, with the file named;
* **CITED** — from the literature, with the source and, where it matters, the sentence;
* **VERIFIED** — an exact computation run *for this assessment* (integer or `Fraction`
  arithmetic; no floating-point value enters a decision). These are **not** repository
  artefacts; the parameters are given so each can be re-run;
* **HEURISTIC** — a judgement, an expectation, or a model;
* **OPEN** — not known.

**Scope statement, stated once and meant throughout.** Nothing in this document states or
implies progress toward the Collatz conjecture. The repository's headline theorem is an
*equivalence*, not an exclusion; `docs/PROGRAMME_ENDPOINT.md` and
`docs/EQUIVALENT_FORMS_OF_DE.md` already say so, and §6 below re-checks every asset against
that standard and finds nothing that changes it.

---

# 1. Inventory

## 1.1 The three formal libraries

### `Divergence` — the exact reduction

| | |
|---|---|
| **Proves** | `divergent_iff_zeroConfined : (∃ M, Odd M ∧ DivergentOrbit M) ↔ (∃ m, Odd m ∧ ZeroConfined m)` (`Divergence/Main.lean`), with **no hypotheses** and no axioms beyond `propext, Classical.choice, Quot.sound`. **PROVED.** |
| **Route** | `Basic` (aggregate identity `2^{Sₙ}mₙ = 3ⁿm₀ + Cₙ`) · `CycleDrift` (a repeat forces `3^L < 2^{S_cyc}`) · `RawMap` (Terras shift, Curry's contraction, the bridge) · `BinomialTail` + `WindowedSparsity` (Garcia–Tal's Fundamental Lemma in Curry's explicit form: a collision-free set meets `[a, a+2^N)` in `≤ 4(N+1)θ^N` points, `θ ≈ 1.9762 < 2`) · `Summable` (`Σ1/mₙ < ∞`) · `LastMaximum` (Prop. 4.10). 249 + 232 + … ≈ 1 650 lines. |
| **Deliberately does not** | exclude divergence. The `README` opens with that sentence. What it removes is the *hypothesis*: Curry's Theorem 2.3, carried as an external `Prop` in the companion repository, is **proved here**, which is what makes the equivalence unconditional. |

### `Occupation` — the confined-mass rate

| | |
|---|---|
| **Proves** | `confined_mass_rate : -(1/N)·log₂ p(N,c) → I₀ = α(1 − H₂(1/α)) ≈ 0.0793186`, `α = log₂3` (`Occupation/Rate.lean`). **PROVED.** Also `exists_rot_neg`, the Dvoretzky–Motzkin/Spitzer cycle lemma, stated generically (`Occupation/CyclicLemma.lean`). ≈ 1 430 lines. |
| **Deliberately does not** | connect to the headline theorem. `Divergence` does not import it. It is the *statistical* rate that Revision 7 §3.3 treated as a standard-technique expectation; it makes that a theorem and nothing more. |
| **Note** | purely combinatorial — no probability, no CLT, no tilting. Upper bound by unimodality of `C(s−1,N−1)2^{−s}`; lower bound by the cycle lemma at the integral anchor `s_N = Nat.log 2 (3^N)`. |

### `Descent` — the residue of a closed route

| | |
|---|---|
| **Proves** | **L1** backward-step inheritance, **L2** the chain law (`3^j(back^[j]x + 1) = 2^j(x+1)`; chain length exactly `v₃(x+1)`), **L4** `r_min(N) ≡ 3 or 7 (mod 12)`, **L7** the lockstep invariance. ≈ 430 lines, imports only `Divergence.Basic`. **PROVED.** |
| **Deliberately does not** | give a descent proof of (DE). The audit that produced it returned **STOP**; these four are the results worth keeping regardless. |

## 1.2 The audits

### `audits/descent` — verdict **STOP**

The question was whether inheritance plus well-ordering yields a descent proof of (DE). It
does not, and the audit names the reason twice over:

* **Classification (b), PROVED.** "Every `z ∈ Z` admits a descending round trip" is *equivalent*
  to (DE). Any statement of the form "every element of `Z` has a property that yields a
  contradiction" is equivalent to `Z = ∅` and carries no independent leverage. This is the
  generic trap, stated in the audit in those words.
* **L7, PROVED.** Under a forward step with `d = 1`, the 3-adic budget `v₃(m_k+1)` and the
  requirement `j_req(m_k)` each advance by exactly one, so the surplus `σ_k` is **invariant**;
  even `d` destroys the budget. The surplus starts at `σ₀ = −1` (by L4) and forward motion
  cannot raise it.
* **Phase 4, VERIFIED (in repo).** 67 ladder times over 16 record holders: **4** descending
  round trips observed against a geometric baseline of **6.86**. Fewer than chance. No forcing.
* **Controls.** `ℤ₂` fails at well-ordering (and `−1` is a backward fixed point with budget
  `v₃(0) = ∞`); the negative integers fail at the fixed point `−1 ∈ Z⁻`; `3x−1` fails at
  `p < m`, which holds iff `1 < m` there and iff `−1 < m` for `3x+1`. The sign of the `+1` is
  exactly what places the backward fixed point outside the positive integers.

**Left behind:** L2 (descent lives at the 3-adic place, and `v₃(x+1)` is its entire budget),
L4, L7.

### `audits/sturmian_irrationality` — Phases 0–3 and 1c-B

* **Phase 0** built and verified the critical-slope argument; **Phase 3** is the literature
  gate, closed with an explicitly limited wording ("no prior proof found across three indexes",
  *not* a priority claim).
* **Phase 1c, §1.3 — a correction that still governs everything downstream. PROVED.** The
  height bound `|c_w| ≤ ℓ·max(2^ℓ,3^k)` is **false for general `w`**: for `w = 0^a1^a`,
  `c_w = 2^a(3^a − 2^a)` and the ratio to `ℓ·max(2^ℓ,3^k)` is unbounded (2.83 at `a = 10`).
  It holds once `w` is **balanced**, with a factor 3 of slack. *Any argument that feeds an
  arbitrary periodic approximant into the Liouville step is unsound.* This is the single most
  load-bearing caveat in the whole Sturmian programme, and §2 below depends on it.
* **Phase 1c, scope correction.** The all-slope extension was correctly demoted from
  "corollary" to "target" — only the odd-indexed convergents are periodic-word values in
  López–Stoll's indexing.
* **Phase 1c-B (`phase1cB/REPORT.md`)** — the general-slope extension, now in PR #6. Its three
  findings: the depth law generalises with `n₀ = 3` **uniformly** in the slope (the expected
  slope-dependent threshold does not exist, because `α_γ ∈ (a₁, a₁+1)` and `q₂ = a₂a₁+1 > a₁`);
  every `β`-specific step is downstream of the single coincidence `α_β = 1/β = log₂3`; and the
  Liouville step survives uniformly with margin `c(γ) = 2 − max(1, γ log₂3) ≥ 2 − log₂3`.

## 1.3 The paper

`papers/critical-sturmian-irrationality`. v1 deposited on Zenodo; **v2 is open in PR #6, not
merged** (the author merges it in mid-October).

| | content |
|---|---|
| **v1, at `γ = β`** | `Φ(1c_β) ∉ ℚ`. Isometry (Prop. 2.2) · periodic values `c_w/(2^ℓ−3^k)` (Prop. 4.1) · height bound for mechanical words (Lemma 4.2) · depth law `q_n+q_{n+1}−1` at odd `n` (Thm 5.3) · the Liouville step (Thm 6.1). Effective: `Φ(1c_β)` is no `u/v` of height `≤ 2^{301973}` (Cor. 6.2). **PROVED.** |
| **v2 (PR #6), all slopes** | `Φ(1c_γ) ∉ ℚ` for every irrational `γ ∈ (0,1)`, one uniform inequality, `n₀ = 3` uniformly, contradiction at `q_n ≥ 5log₂H + 22`. **PROVED.** |
| **Credit map** | `γ < β`: an immediate corollary of **Monks–Yazinski**, *Discrete Math.* **275** (2004) 219–236, Thm 2.7(b) — refereed — a deduction drawn explicitly in **López–Stoll 2021**, p. 6. `γ > β`: the first half of **López–Stoll 2021**, Thm 1, archimedean, **arXiv:2101.12747v1, unpublished**. `γ = β`: new. **CITED.** |

## 1.4 The open problems, as the repository states them

* **(DE)** — no positive odd `m` has `2^{S_n(m)} ≤ 3^n` for every `n`. **OPEN.** Four equivalent
  forms are recorded in `EQUIVALENT_FORMS_OF_DE.md` precisely so that a reformulation into one
  of them is not mistaken for progress.
* **Open Problem C** — the pointwise realizer problem, on the occupation side. **OPEN.**
* **Cycle exclusion** — not a formalized target here; see §7.
* **Paper open problems (PR #6 wording):** general intercepts `ρ ≠ 0`; an irrationality
  measure; transcendence.

## 1.5 One fact that governs every direction below: **the density filter**

This is the most important thing in the inventory, and it is easy to miss.

> **CITED.** For an aperiodic word `v` with `lim inf kₙ(v)/n ≠ β`, `Φ(v) ∉ ℚ` is:
> * **known**, for `< β` — an immediate consequence of Monks–Yazinski 2004, Thm 2.7(b),
>   **refereed**, and the deduction is drawn explicitly in López–Stoll 2021, p. 6;
> * **claimed**, for `> β` — the first half of López–Stoll 2021, Thm 1, resting on that
>   preprint's own archimedean argument (their Lemmas 23–26). **arXiv:2101.12747v1, one
>   version, no journal reference: unrefereed. It is a claim, not a known theorem**, and this
>   document treats it as such throughout.

Both are *density* statements: they quantify over all aperiodic words, at every intercept, of
every complexity. **Therefore the novelty of any new irrationality criterion is confined to
words of lower density exactly `β`, plus whatever is added by putting the `> β` half on a
refereed footing**, plus effectivity. Sections 2 and 3 are ranked by that standard and not by
how much ground they appear to cover.

**The asymmetry matters and is easy to lose.** Below `β` a new proof adds only effectivity,
because the statement is already a theorem. Above `β` a new proof adds the statement itself in
publishable form, because at present it rests on an unrefereed preprint. The two are not the
same kind of contribution, and the per-region table in §2 keeps them apart.

---

# 2. Direction A — all Sturmian words, via initial repetitions

**Assessment: the strongest direction in this document. Recommended.**

## What would be proved

> `Φ(s) ∉ ℚ` for **every** Sturmian word `s`, at every irrational slope `γ ∈ (0,1)` and
> **every intercept** `ρ`, with an explicit height bound at every initial square.

That closes the paper's Open Problem 1 (general intercepts) outright, and it does so by an
argument strictly simpler than PR #6's.

## The literature input — **CITED, and verified against the source**

Berthé, Holton and Zamboni, *Initial powers of Sturmian sequences*, **Acta Arith. 122 (2006)
315–347**, p. 2, verbatim:

> "In [3] it is shown that each Sturmian sequence begins in infinitely many squares (see also
> [19]), and hence `ice(ω) ≥ 2` for all Sturmian sequences `ω`. We show that the value 2 is
> attainable…"

where `ice(ω)` is the *initial* critical exponent (the supremum of `p` with `u^p` a prefix for
arbitrarily long prefixes `u`), their [3] is **Allouche, Davison, Queffélec and Zamboni,
*Transcendence of Sturmian or morphic continued fractions*, J. Number Theory 91 (2001) 39–66**,
and [19] is Damanik–Killip–Lenz.

**Two cautions, both checked.** (i) The square fact is *attributed*, not proved, in BHZ — the
citation to chase is Allouche–Davison–Queffélec–Zamboni. (ii) BHZ's Theorem 1.1 shows
`ice(ω) = 2` is **attained** for suitable slopes, so no exponent above 2 is available in
general. The argument below therefore uses exponent exactly 2 and nothing more.

## The argument

Let `s` be Sturmian of slope `γ`, `θ = γ log₂3`. Suppose `Φ(s) = u/v` in lowest terms,
`H = max(|u|,v)`; `v` is odd. Take any prefix `u₀u₀` of `s` with `|u₀| = ℓ`, `k` ones.

* `u₀` is a factor of a Sturmian word of slope `γ`, hence **balanced**, hence `|k − ℓγ| < 1`.
* `lcp(s, u₀^∞) ≥ 2ℓ`, so by the isometry (Prop. 2.2) and `M = uδ − v c_{u₀}`, `δ = 2^ℓ − 3^k`
  odd, `|M| ≥ 2^{2ℓ}` — and `M ≠ 0` because `s` is aperiodic while `u₀^∞` is not.
* `|δ| < G := max(2^ℓ,3^k)` and `c_{u₀} ≤ 3ℓ·G` by the **balanced** height bound, so
  `|M| ≤ H(1+3ℓ)G`.
* `log₂G = max(ℓ, k log₂3) ≤ max(1,θ)ℓ + log₂3`.

Hence `(2 − max(1,θ))·ℓ ≤ log₂H + log₂(1+3ℓ) + log₂3`, and

> **`2 − max(1,θ) ≥ 2 − log₂3 = 0.41504… > 0` for every `γ ∈ (0,1)`.**

Since squares occur at unbounded `ℓ`, the left side is unbounded: contradiction.

**The margin is the same constant `c(γ)` as PR #6's Theorem 8.5.** That is not a coincidence:
at intercept 0 the depth law `q_n + q_{n+1} − 1` says the prefix is `w_n` repeated
`1 + q_{n+1}/q_n − 1/q_n ≥ 2 − 1/q_n` times, so the depth law *is* "begins in squares", made
exact. **The essential simplification:** the repetition argument needs only a *lower bound* on
the agreement depth, so it needs no continued-fraction theory, no alternation, no
three-distance lemma, and no exact depth law at all.

## VERIFIED (this assessment)

At the **critical slope** `β` with **nonzero intercept** — the case the paper leaves open —
using the word `1c_{β,ρ}(j) = ⌈(j+1)β+ρ⌉ − ⌈jβ+ρ⌉` over a 40 000-letter prefix, with `β`
bracketed to 250 decimal digits and every ceiling certified by requiring the two bracket ends
to agree:

| intercept `ρ` | largest initial square half-length `L` found | `k/L` | `log₂` of the forced height floor |
|---|---|---|---|
| `0` | 12 648 | 0.630930 | **10 525** (at `L = 10 540`) |
| `1/2` | 11 594 | 0.630930 | **11 578** (at `L = 11 594`) |
| `1/π` | 13 133 | 0.630930 | **13 117** (at `L = 13 133`) |

The square half-lengths at `ρ = 0` are `…, 7378, 8432, 9486, 10540, 11594, 12648` — an
arithmetic progression of step `1054 = q₉`, exactly the convergent structure. At `β`, `θ = 1`
exactly, so the margin is `2 − 1 = 1` and `log₂H₀ ≈ L − 15`.

## The one thing it needs that is not yet a lemma

**The balanced-word height bound.** The paper has it only as **Remark 4.3**, a sketch: "For an
arbitrary *balanced* `w` the proof of Lemma 4.2 goes through with the discrepancy bound
`|k_{i+1}(w) − (i+1)k/ℓ| < 1` in place of the exact count, at the cost of a factor 3." The
audit proved the *mechanical* case. Direction A needs the balanced case as a stated,
proved lemma, because the blocks `u₀` at a nonzero intercept are **conjugates** of mechanical
words, not mechanical words.

**VERIFIED (this assessment):** over **all 441 152 rotations** of every mechanical word
`w_{p,q}` with `q < 130`, the worst value of `c_w/(ℓ·max(2^ℓ,3^k))` is **0.451690**, attained
at `(p,q,r) = (53,84,65)` — note `53/84` is a convergent of `β`. So the bound holds on the
whole rotation class with constant **1**, and Remark 4.3's factor 3 is slack by 2.2×. For
contrast, the unbalanced `0^{10}1^{10}` gives 2.8333.

## Most likely failure point

Not the mathematics — the **citation chain**. The square fact must be taken from
Allouche–Davison–Queffélec–Zamboni (2001) and quoted in its own words, not from BHZ's summary
of it. If that paper's statement turns out to be about *some* Sturmian sequence rather than
*every* one, direction A weakens to the slopes and intercepts where squares are known. (BHZ's
phrasing — "each Sturmian sequence" — says otherwise, and the computation above exhibits them
at three intercepts, but the primary source is the thing to read.)

A second, smaller point: the argument needs `k ≥ 1` in `u₀` (so `2^ℓ ≠ 3^k` and Prop. 4.1
applies), which holds for `ℓ > 1/γ`.

## Novelty, honestly

| region | what direction A adds |
|---|---|
| `γ < β`, any `ρ` | nothing qualitative — Monks–Yazinski 2004. Effective height bounds are new. |
| `γ > β`, any `ρ` | **the statement, on a refereed footing.** Here it is only *claimed*, in an unrefereed preprint (López–Stoll 2021, archimedean); an elementary and effective proof would make it a theorem. |
| **`γ = β`, `ρ ≠ 0`** | **new.** This is the real content, and it is exactly the paper's Open Problem 1. |
| `γ = β`, `ρ = 0` | already PR #6 / v1. |

**Value: high** (closes a stated open problem; makes slope and intercept one theorem; and the
simpler proof is the better proof). **Effort: small** — the balanced height bound is a
half-page, the Liouville step is six lines, and the literature note is one paragraph.
**Risk: low.**

## Concrete first step, with a stop rule

> **Audit `phase1d`, bounded.** (1) Obtain Allouche–Davison–Queffélec–Zamboni (2001) and quote
> the square statement exactly; record whether it is "every Sturmian sequence" and whether it
> is proved there or attributed further back. (2) Write the balanced-word height bound as a
> lemma with a complete proof. (3) Write the six-line Liouville step. (4) Verify at ≥ 5
> (slope, intercept) pairs including `γ = β` with `ρ ∈ {1/2, 1/π}` and one slope above `β`.
> **STOP and report if** the square statement is not unconditional for every Sturmian sequence,
> or if the balanced height bound needs a constant growing with `ℓ`.

---

# 3. Direction B — a repetition criterion beyond Sturmian words

**Assessment: the criterion is real and easy; its novelty is almost entirely eaten by the
density filter. Rank low.**

## What would be proved

> **Criterion.** Let `v` be aperiodic with `lim inf kₙ(v)/n = d`, `θ = d log₂3`. If there are
> arbitrarily long prefixes `u` of `v` with `u^p` a prefix for some fixed `p > max(1,θ)`, and
> the blocks `u` have discrepancy bounded by a constant `D` (`|k(u) − |u|·d| ≤ D`), then
> `Φ(v) ∉ ℚ`, with an explicit height bound at each repetition.

This is a 2-adic analogue of the Adamczewski–Bugeaud repetition criterion, and the proof is
§2's, with `2` replaced by `p` and the factor 3 by a constant depending on `D`.

## Why the novelty is nearly empty — **the two obstructions**

**(i) The density filter (§1.5).** New ground is confined to `lim inf` density exactly `β`.

**(ii) `β` is transcendental, so the natural classes cannot sit there. PROVED (standard).**
`β = ln2/ln3` is irrational by unique factorisation; if it were algebraic and irrational then
`3^β = 2` would be transcendental by **Gelfond–Schneider**, so `β` is **transcendental**. But:

* letter frequencies of a **primitive morphic** word are entries of the normalised
  Perron–Frobenius eigenvector of the incidence matrix, hence **algebraic**;
* letter frequencies of a **`k`-automatic** word, when they exist, are **rational** (Cobham).

**Therefore no primitive morphic word and no automatic word has density `β`,** and the
morphic/automatic application of the criterion at the critical density is *empty*. This is the
decisive point and it is cheap to state.

**VERIFIED (this assessment), the Thue–Morse test case.** Over the first 65 536 letters,
Thue–Morse **never begins with a square** — the largest `L` with prefix `= uu` is **0** — and
its initial critical exponent is `5/3`, attained at periods `3·2^j` for `j = 0,…,10`. The
criterion does fire (`θ_TM = ½log₂3 = 0.7925 < 1`, so `max(1,θ) = 1 < 5/3`), but Thue–Morse has
density `½ < β` and is therefore **already covered by Monks–Yazinski**. It is a good sanity
test and no new mathematics. For contrast, the Fibonacci Sturmian word has initial exponents
`2.0, 2.4, 2.538, 2.588, 2.607, 2.614, 2.616, 2.617 …` at periods `2, 5, 13, 34, 89, 233, 610,
1597`, converging to `(3+√5)/2 = 2.618` — matching BHZ's own Fibonacci discussion.

## What survives

One narrow corollary, worth stating but **not new**:

> Any positive integer whose parity word is 0-confined and has initial repetitions of exponent
> `≥ 1+δ` with bounded-discrepancy blocks at unbounded lengths must be exponentially large in
> the repetition length.

Note (B), §8, Proposition 8.1 ("Windowed exponential floors at convergent scales") already
derives exactly this, in realizer form, from `s` consecutive copies of a convergent block.
**CITED.** And a hypothetical 0-confined word has no reason to have repetitions at all — see
§6.

**Value: low.** **Effort: small.** **Risk: low but the payoff is the issue, not the risk.**

## Concrete first step, with a stop rule

> Write the criterion as one lemma in the `phase1d` audit (it costs three extra lines over
> §2), record the Gelfond–Schneider/Perron–Frobenius obstruction in one paragraph, and
> **STOP**: do not look for applications until someone exhibits an explicit aperiodic word of
> density exactly `β` that is not Sturmian and has unbounded initial repetitions.

---

# 4. Direction C — an irrationality measure for `Φ(1c_β)`

**Assessment: high value, very high risk. The *rational-approximation* form is refuted unless
`β` is badly approximable; the *integer* form — the paper's actual Open Problem 3, and the one
the realizer floor needs — is untouched and remains **OPEN**. Rank low, and re-scope before
attempting.**

## What would be proved, and what it would buy

The paper's Open Problem 3: `∃ μ < ∞, C > 0` with `|Φ(1c_β) − y|₂ ≥ C|y|^{−μ}` for all
**integers** `y ≥ 1`. By note (B), **Theorem 5.2** (verbatim: "*Effective measure implies
exponential edge floor*"), any finite `μ` gives `r(D_N) ≥ (2C)^{1/μ}2^{S_N/μ}` — an
**exponential** lower bound on the least integer realizing the length-`N` prefix, "far beyond
the linear LCF scale on this edge". **CITED.**

## The obstruction, for the rational form — **PROVED**

If the same question is asked over **rationals** rather than integers, it is *false* unless
`β` is badly approximable. From the depth law, `|Φ(1c_β) − c_n/δ_n|₂ = 2^{−(q_n+q_{n+1}−1)}`
while the height of `c_n/δ_n` is `≈ 2^{q_n}`. So any rational-approximation exponent must
satisfy

> `μ ≥ 1 + q_{n+1}/q_n` for every odd `n`.

**VERIFIED (this assessment)**, using the repository's own rigorously determined continued
fraction of `β` (368 partial quotients, `scripts/verify.py convergents`): the largest partial
quotients are **2436** (the 331st), **964** (the 231st), **196** and **100**; the maximum of
`q_{n+1}/q_n` over `n < 367` is **2436.1**, at `n = 330`. So already `μ ≥ 2437`, and the bound
grows with every new record partial quotient. **HEURISTIC:** `β`'s partial quotients are
expected to be unbounded (as for almost every real), in which case **no finite rational
irrationality measure exists at all**. Whether `log₃2` is badly approximable is **OPEN** and
far out of reach.

> **The integer form is not touched by this, and it is the one that matters. OPEN.**
> The refutation above is of the *rational-approximation* analogue — `|Φ(1c_β) − p/q|₂` over all
> rationals — which is false unless `β` is badly approximable. The paper's Open Problem 3, and
> the only form note (B)'s Theorem 5.2 consumes, quantifies over **integers** `y ≥ 1`. Integers
> are not the approximants `c_n/δ_n`, so nothing above applies to them, and **the integer form
> remains open**. It is also the form the realizer floor needs: `|Φ(1c_β) − y|₂ ≥ C y^{−μ}`
> with `y` an integer is exactly what converts into `r(D_N) ≥ (2C)^{1/μ}2^{S_N/μ}`.
>
> What *is* established is that the repository's method has no purchase on it: every bound
> proved there comes from `Φ(w_n^∞)`, rationals with odd denominator, never integers. So the
> direction is not refuted — it is **unattacked**, and the rational-form refutation is only a
> warning against asking the question in the shape that is already false.

## Where it actually sits

`Φ(1c_β)`'s realizer frontier is not an incidental object. `1c_β` has
`k_ℓ = ⌈ℓβ⌉`, which is the **smallest** count compatible with 0-confinement at every length —
`1c_β` is the *extremal* 0-confined parity word. So Open Problem 3 asks for a growth rate of
least realizers of one specific 0-confined word, while (DE) asks for `r_min(N,0) → ∞`, the
minimum over **all** 0-confined words. **These do not imply one another** (a bound for one word
does not bound the minimum over the family), but they are the same genus of question, and
`PROGRAMME_ENDPOINT.md` already identifies that genus — *where specific integers sit inside a
population whose size is known* — as the common obstruction of both open problems.

**Value: high if achieved. Effort: large. Risk: very high.** The only sketched route is a
2-adic Mahler method (paper Open Problem 4; note (B) §7), which is speculative and which note
(B) itself says "would realistically deliver a finite `μ`, not the sharp law".

## Concrete first step, with a stop rule

> Before any attempt: a one-week audit that (1) records the rational-form obstruction above as
> a proposition in the paper's open-problems section, so the question is asked in the form that
> is not already refuted; (2) checks whether any 2-adic Mahler-method machinery exists at all
> in the literature for Hecke–Mahler values at the boundary point. **STOP if** no 2-adic
> analogue of the Mahler method is found — that is the whole route.

---

# 5. Direction D — Lean formalization of the irrationality theorem

**Assessment: feasible, and the right target is the repetition criterion, not the depth law.**

## What Mathlib provides

| available | file |
|---|---|
| `GenContFract.of v`, convergents, `convs_succ` | `Algebra/ContinuedFractions/…` |
| `determinant`: `Aₙ₊₁Bₙ − AₙBₙ₊₁ = (−1)^{n+1}` — i.e. `p_{n+1}q_n − p_nq_{n+1} = ±1` | `ContinuedFractions/Determinant.lean` |
| `abs_sub_convs_le`: `\|v − Aₙ/Bₙ\| ≤ 1/(BₙBₙ₊₁)` — i.e. `Dₙ ≤ 1/q_{n+1}` | `Computation/Approximations.lean` |
| `of_den_mono`, `succ_nth_fib_le_of_nth_den` (denominator growth), `of_convergence` | same |
| `TerminatesIffRat` — non-termination for irrationals | `Computation/TerminatesIffRat.lean` |
| `PadicInt ℤ_p`, units, completeness, `padicValInt` | `NumberTheory/Padics/` |

## What is missing

* the **alternation sign** (`p_n/q_n > γ ⟺ n odd`) as a named lemma;
* the exact identity `q_{n+1}Dₙ + q_nDₙ₊₁ = 1`;
* **all** Sturmian combinatorics: `⌊jα⌋` one-positions, mechanical words, balance, longest
  common prefix. Mathlib has none of it;
* **`Φ` itself** — the Bernstein–Lagarias conjugacy as a map `{0,1}^ℕ → ℤ₂` together with the
  isometry `v₂(Φ(v) − Φ(v')) = lcp(v,v')`. Constructible from the paper's Prop. 2.1 series
  (`Φ(v) = −Σ 3^{−k_{i+1}}2^i`, convergent in `ℤ₂` since `3` is a unit), which is the cheapest
  route.

## The strategic point

**Formalize direction A's criterion, not PR #6's depth law.** The criterion takes "the word has
arbitrarily long square prefixes with balanced periods" as a *hypothesis* and needs **zero**
continued-fraction theory. That removes the entire missing-Mathlib list above except `Φ`.

**HEURISTIC size estimate**, calibrated against this repository's own libraries (`Divergence`
≈ 1 650 lines for the full Garcia–Tal/Curry chain; `Occupation` ≈ 1 430 for the rate):

| target | estimate |
|---|---|
| `Φ`, the isometry, periodic values `c_w/(2^ℓ−3^k)`, balanced height bound, the Liouville step — i.e. **direction A's theorem, with the square hypothesis** | **≈ 1 200–1 800 lines** |
| adding the depth law (CF alternation, the `Dₙ` identities, the floor comparison of Lemma 5.2) | **+ 1 500–2 500 lines**, and the floor comparison is the hard part |
| adding "every Sturmian word begins in squares" | not advisable — a research-level combinatorics-on-words result |

**Value: moderate–high** — a fourth library, and the first machine-checked irrationality result
for a conjugacy value. **Effort: moderate** for the criterion version. **Risk: low**, since the
hypothesis-version can be stated and proved without ever resolving the combinatorics.

## Concrete first step, with a stop rule

> Milestone F1, bounded: define `Φ` in `ℤ₂` from the Prop. 2.1 series and prove the isometry
> and `Φ(w^∞) = c_w/(2^ℓ−3^k)`. Target ≈ 400 lines. **STOP and report if** the isometry needs
> more than 250 lines — that is the signal that `Φ` should be defined as an inverse limit
> instead of a series.

---

# 6. Direction F — does anything here pass the three-condition filter for (DE)?

**Assessment: nothing does. This confirms the default expectation.**

The filter, as stated in the brief (it is **not** recorded in the repository; this is the
author's formulation): a route to (DE) must (1) use 2-adic integrality at unbounded depth,
(2) use the sign or positivity of the integer, and (3) couple both along one orbit.

| asset | (1) integrality at unbounded depth | (2) sign / positivity | (3) coupled along one orbit | verdict |
|---|---|---|---|---|
| `divergent_iff_zeroConfined` | ✅ `2^{Sₙ} ≤ 3ⁿ` at every `n` | ✅ future-minimum, last-maximum | ✅ | **passes formally, and yields nothing** — it is an *equivalence*. `EQUIVALENT_FORMS_OF_DE.md` exists to make exactly this point: a reformulation is not progress. |
| `Descent` L1/L2/L4/L7 | ❌ the budget is **3-adic** (`v₃(x+1)`), and L7 proves it cannot accumulate | ✅ well-ordering, `p < m` | ✅ | **fails (1)**. Audit verdict STOP stands. |
| `Occupation.confined_mass_rate` | ✅ (confinement at every horizon) | ❌ statistical; no specific integer appears | ❌ | **fails (2), (3)** |
| the irrationality theorem (v1/PR #6) | ✅ `v₂(Mₙ) = qₙ+qₙ₊₁−1`, unbounded | ❌ uses only `Mₙ ≠ 0`, never a sign | ❌ one fixed word; the "orbit" is a shift orbit of a word, not of integers | **fails (2), (3)** |
| direction A's repetition criterion | ✅ | ❌ same | ❌ same | **fails (2), (3)** |

**Two further observations, both honest and both negative.**

* **The remaining target is already named in the literature.** A 0-confined orbit has parity
  word of lower density `≥ β` (`kℓ ≥ ℓβ` at the confinement times, and `n/S_{n+1} → β` between
  them), and López–Stoll 2021's Theorem 1 states that a divergent rational 2-adic integer has
  lower density **exactly** `β`. So the irrationality programme's remaining reach against (DE)
  is precisely the critical density — but that sharpening is **CITED**, not produced here, and
  it does not pass the filter either, being a density statement.
* **Why the repetition route cannot be pointed at (DE).** Direction A works because Sturmian
  words *have* long initial squares. A hypothetical 0-confined parity word has no reason to
  have any repetition at all, and the word-shadow cardinality barrier recorded in the
  programme notes says the 0-confined family is uncountable with generic members carrying no
  such structure. There is no mechanism to supply the hypothesis.

**Conclusion.** No asset in this repository, and nothing in directions A–E, G or H, bears on
(DE) or on the Collatz conjecture. The repository's own `README` sentence — "This repository
does not exclude divergent orbits" — remains exactly correct.

---

# 7. Direction G — the cycle side and Fernández–Ibáñez

**Assessment: a real and cheap bridge. Second recommendation.**

## The source — **CITED**

Carlos Fernández and Santiago Ibáñez, *Christoffel words as extremal structures in Collatz
dynamics*, **arXiv:2607.24844**, submitted 24 July 2026. From the abstract: they associate to a
finite orbit segment a binary word, introduce a functional `C(d)` "which provides an explicit
expression for the iterates and characterizes possible periodic cycles", define a rotation
action and the representative `C_min(d)`, and

> "prove that Christoffel words are, up to rotation, the unique maximizers of `C_min(d)` on
> `D_{N,r}`, the set of binary words of length `N` with exactly `r` ones",

obtaining "restrictions on the possible existence of nontrivial cycles" and "explicit bounds
for the minimum element of an orbit".

## The overlap with this repository

It is direct, and it is at the level of *the same formula*:

* the paper's **Prop. 4.1**, `Φ(w^∞) = c_w/(2^ℓ − 3^k)` with
  `c_w = Σ_{w_i=1} 3^{k−κ_{i+1}}2^i`, **is** the cycle value of the word `w`; `c_w` is the
  carry, and Fernández–Ibáñez's `C(d)` is — apparently — the same object;
* the paper's **Lemma 4.2** bounds `c_w ≤ ℓ·max(2^ℓ,3^k)` for **mechanical (= Christoffel)**
  words, and **Remark 4.3** shows the bound fails off the balanced class;
* `Occupation`'s `exists_rot_neg` is the cycle lemma on the same rotation classes.

**The concrete cross-import (OPEN, pending one verification).** If `C = c_w` up to
normalisation, then *their* maximality plus *this* repository's Lemma 4.2 combine to a bound on
`C_min` for **every** word of length `ℓ` with `k` ones — not only the balanced ones:

> `C_min(d) ≤ c_{Christoffel(ℓ,k)} ≤ ℓ·max(2^ℓ, 3^k)`.

**VERIFIED (this assessment):** the bound holds with constant **1** on all 441 152 rotations of
every mechanical word with `q < 130`, worst ratio **0.451690** at `(p,q,r) = (53,84,65)`.

**Likely failure point:** their `C` may be normalised differently (a factor `3^k`, or the
opposite orientation of the word), in which case "maximizer" and the repository's "upper bound"
sit on opposite sides and do not compose. That is a half-day check, not a research programme.

**Filter status:** this is the cycle side, not (DE). Cycle exclusion is a different open
problem and nothing here touches it either.

**Value: moderate. Effort: small. Risk: low (the downside is a null result in a day).**

## Concrete first step, with a stop rule

> A one-day audit `audits/cycle_words`: read Fernández–Ibáñez's definitions, decide whether
> `C(d) = c_w`, and test numerically over all words of length `≤ 20`. **STOP and report if**
> the normalisations do not match — then record the dictionary and nothing more.

---

# 8. Direction E — formalizing Scales 2–3 of *Three Scales of Confinement*

**Assessment: large effort, low value. Rank last.**

`Occupation` formalizes **Scale 1**, the exponential rate `I₀`. Scales 2 and 3 — the `Θ(N^{−3/2})`
polynomial persistence and the renewal phase — are **paper-proved** in the September 2026
*Three Scales of Confinement* note (they are theorems there, not conjectures).

**Why the value is low.** `PROGRAMME_ENDPOINT.md` says it in its own words: *"improving either
statistical estimate does not touch either open problem"*. Scales 2–3 are exactly a refinement
of the statistical estimate whose leading term is already formalized. They would strengthen a
companion library that the headline theorem does not import.

**Why the effort is large.** `N^{−3/2}` is a local-limit / ballot-type correction. In Lean it
needs Stirling with controlled error, a local central limit theorem or an exact ballot-problem
count, and the cycle lemma refined to count rather than merely exhibit rotations. Mathlib's
support here is thin. **HEURISTIC estimate: 2 500–4 000 lines**, more than `Occupation` itself.

**Concrete first step, if ever:** formalize only the *upper* bound `p(N,c) ≤ poly·2^{−I₀N}·N^{−3/2}`
via the exact `C(s−1,N−1)` count and Stirling, skipping the matching lower bound. **STOP if**
Stirling-with-error costs more than 600 lines.

---

# 9. Direction H — a synthesis paper for the programme

**Assessment: worth doing, and worth doing last.**

**What it would contain.** What the valuation boundary does and does not give; the three sides
(divergence, occupation, the Sturmian edge); the formal results with their axiom audits; and —
the part with the most long-run value — **the closed routes**, each with the reason it closes:
descent (STOP, with L7 as the mechanism), the word-shadow cardinality barrier, the transport
closed form, the four equivalent forms of (DE), and the density filter of §1.5.

**Why it matters.** Every one of those closures cost a bounded audit, and each is the kind of
thing that gets re-derived by the next person — including by the author. A paper that records
them is the single highest-leverage piece of scholarship available here. `PROGRAMME_ENDPOINT.md`
and `EQUIVALENT_FORMS_OF_DE.md` are already two-thirds of its skeleton.

**The one hard constraint.** It must claim no progress toward Collatz, and the natural
temptation of a synthesis paper is to let the accumulation of results imply momentum. The
honest framing is the `README`'s: an equivalence, a statistical rate, an irrationality theorem
at one density, and a list of routes that are closed.

**Value: moderate–high (scholarship, not new mathematics). Effort: moderate. Risk: low,
provided the framing constraint holds.**

**Why last.** It should be written after direction A, so that the Sturmian side is complete
(all slopes *and* all intercepts) rather than half-complete.

---

# 9b. Direction I — transcendence by a `p`-adic Roth/Ridout route

**Assessment: the arithmetic already in hand clears the Roth threshold, which makes this the
one direction that could answer an open problem of the paper outright. It is also the one most
likely to be already known, or to fail on a normalisation. Check the literature before touching
it.** **HEURISTIC throughout.**

## What would be proved

The paper's **Open Problem 4**: `Φ(1c_β)` is **transcendental** over `ℚ`. More generally
`Φ(1c_γ)` for suitable irrational `γ`.

## The mechanism, and the number it produces

This is the standard route to transcendence of automatic and Sturmian reals
(Adamczewski–Bugeaud), transplanted to the `2`-adic place. Repetitions give exceptionally good
rational approximations; a Roth-type theorem says an algebraic number cannot have them.

**The statement to use. CITED**, from Kalitzin and Murru, *Transcendence of `p`-adic continued
fractions and a quantitative `p`-adic Roth theorem*, **arXiv:2603.10561**, 11 March 2026, which
gives both Ridout's original (their Theorem 3) and a clean quantitative form:

> for `α ∈ ℚ_p` algebraic of degree `≥ 2` and `0 < ε ≤ 1/3`, the number of solutions of
> `|α − A/B|_p < |B|_∞^{−2−ε}` with `A, B ∈ ℤ`, `B > 0`, `gcd(A,B) = 1` and `|B|_∞ ≥ |A|_∞`
> is less than `exp(C₁ε^{−2})`, with `C₁` depending only on `α`.

**What the depth law supplies.** At an odd convergent, Theorem 5.3 and Lemma 4.2 give
```
|Φ(1c_β) − c_n/δ_n|₂ = 2^{−(q_n+q_{n+1}−1)} ,      log₂ max(c_n,|δ_n|) = q_n + log₂q_n + O(1) ,
```
so the approximation exponent is
```
E_n  =  (q_n + q_{n+1} − 1)/(q_n + log₂q_n + O(1))  →  1 + q_{n+1}/q_n .
```
**VERIFIED (this assessment), on the repository's own rigorously determined continued fraction
of `β`:** at `n = 13`, `q_n = 176 251`, `q_{n+1} = 301 994`, depth `478 244`, giving
`E₁₃ = 2.713`. The ratios `q_{n+1}/q_n` at the odd convergents run
`2.00, 2.67, 3.42, 5.77, 23.46, …`, so `E_n = 1 + q_{n+1}/q_n` runs
`3.00, 3.67, 4.42, 6.77, 24.46, …` — **every one above the Roth threshold of `2`, with room to
spare, and infinitely many of them.**

At a general irrational slope the same computation gives
`E_n = (1 + q_{n+1}/q_n)/max(1,θ)`, `θ = γ log₂3`, so the condition to beat is
`q_{n+1}/q_n > 2·max(1,θ) − 1`.

## Why this is not being claimed

Four reasons, in order of how likely each is to kill it.

1. **It would be too easy, and the machinery is standard.** Ridout is from 1958 and the
   Sturmian-transcendence argument is textbook. If the depth law plus Ridout really gave
   `Φ(1c_β)` transcendental in half a page, someone would very likely have done it — the more so
   since López–Stoll had the `2`-adic series with these exact exponents in 2009. **The first
   step is a literature search, not a proof attempt.**
2. **The height normalisation may not be the one Ridout wants.** The quoted form requires
   `|B|_∞ ≥ |A|_∞`, i.e. the height carried by the *denominator*. Our approximants have
   `c_n ≈ q_n·|δ_n|`, so `|A| > |B|` — by a factor `q_n`, which is polynomial in `log H` and so
   should be absorbable, but that has to be checked against the form actually proved rather than
   assumed.
3. **Ridout's Theorem 3 carries an archimedean factor.** Its product is
   `min(1,|α − A/B|_∞)·∏_i min(1,|α_i − A/B|_{p_i})`, over a real root and the `p`-adic roots of
   one polynomial. The clean `p`-adic-only form above is the quantitative theorem of
   arXiv:2603.10561, not Ridout's original; which one applies, and whether the archimedean
   factor can be dropped for a value that is a `2`-adic integer with no distinguished real
   conjugate, is the second thing to check.
4. **`c_n/δ_n` need not be in lowest terms.** Reduction only *lowers* the height and so *raises*
   `E_n`, so this direction is favourable — but the exponent must be computed after reduction
   for the statement to be exact.

## Value, effort, risk

**Value: the highest in this document if it survives** — it would settle the paper's Open
Problem 4, and transcendence implies irrationality, so it would subsume Theorem 6.1 and PR #6's
Theorem 8.5 at the slopes where it applies. It would also change **Direction C**: an
irrationality *measure* is a weaker and differently-shaped statement than transcendence, and a
Ridout argument gives qualitative transcendence without a measure. **Effort: small if it works**
(the approximations already exist and are machine-verified), **unbounded if the answer is that
it is known**. **Risk: high**, concentrated entirely in points 1–3 above.

**Filter status for (DE):** fails conditions (2) and (3) exactly as directions A–C do. It is
about one word; it uses `M ≠ 0` and heights, never a sign, and never couples along an orbit of
integers. **It does not bear on (DE) or on the Collatz conjecture.**

## Concrete first step, with a stop rule

> **A two-day literature audit, before any mathematics.** (1) Search for `p`-adic
> Roth/Ridout/Schlickewei applied to Bernstein–Lagarias conjugacy values, to `2`-adic Sturmian
> or Hecke–Mahler series, or to the López–Stoll series of Integers **9** (2009) #A13 —
> including the citing literature of Ridout and of Adamczewski–Bugeaud. (2) Obtain
> arXiv:2603.10561 in full and write down the exact hypotheses of the form to be used, in
> particular the height convention and whether an archimedean factor is required. (3) Only then
> compute `E_n` after reduction of `c_n/δ_n` to lowest terms, at `n = 3 … 13`, exactly.
> **STOP and report if** the statement is already in the literature — that is a complete and
> valuable answer — **or if** the applicable form of the theorem needs `|B| ≥ |A|` in a way the
> approximants cannot be made to satisfy.

---

# 10. Ranking and recommendation

| rank | direction | value | effort | risk | novelty after the density filter | filter status for (DE) |
|---|---|---|---|---|---|---|
| **1?** | **I. Transcendence by a `p`-adic Roth/Ridout route** | **highest if it survives** | small if it works | **high** — most likely already known, or a normalisation failure | would settle Open Problem 4 and subsume the irrationality theorems | fails (2),(3) |
| **1** | **A. All Sturmian words via initial repetitions** | **high** | **small** | **low** | `γ = β`, `ρ ≠ 0` — a stated open problem | fails (2),(3) — does not bear on (DE) |
| 2 | G. Fernández–Ibáñez cross-check | moderate | small | low | n/a (cycle side) | n/a — cycle side |
| 3 | D. Lean formalization (criterion version) | moderate–high | moderate | low | n/a (formalization) | fails (2),(3) |
| 4 | H. Synthesis paper | moderate–high | moderate | low | n/a | n/a |
| 5 | B. Repetition criterion beyond Sturmian | low | small | low | **essentially empty** — no morphic or automatic word has density `β` | fails (2),(3) |
| 6 | C. Irrationality measure | high *if* achieved | large | **very high** | n/a | fails (2),(3) |
| 7 | E. Scales 2–3 in `Occupation` | low | large | moderate | n/a | fails (2),(3) |
| — | F. (DE) itself | — | — | — | — | **nothing passes** |

## Recommendation: **direction A**, with one two-day check first

Pursue **A — all Sturmian words, at every slope and every intercept, via initial squares** —
as the next piece of work.

**But run direction I's literature audit first.** It costs two days, it is pure searching, and
its outcome changes what A is for: if a `p`-adic Roth route to transcendence is available, it
subsumes the irrationality statement at the slopes where it applies, and A becomes a sharper
and more elementary companion rather than the headline. If the audit finds the route already
taken, or the normalisation fatal, nothing is lost and A proceeds unchanged. **I is ranked
`1?` and not `1` precisely because its risk is concentrated in a question that two days of
searching answers.**

**Why, in four points.**

1. **It closes a problem the repository has itself declared open.** PR #6's Open Problem 1 is
   general intercepts; direction A answers it, and answers it at every slope at once.
2. **The hard input is already cited, and the margin is already proved.** The only literature
   input is "every Sturmian sequence begins in infinitely many squares"
   (Allouche–Davison–Queffélec–Zamboni 2001, via Berthé–Holton–Zamboni 2006). The margin
   `2 − max(1,θ) ≥ 2 − log₂3 = 0.41504 > 0` is PR #6's own Theorem 8.5 constant, already
   proved and already machine-verified in `make verify`.
3. **The proof is strictly simpler than the one it generalizes.** It needs only a *lower bound*
   on the agreement depth, so it discards the entire continued-fraction apparatus — the
   alternation, the `Dₙ` identities, Lemma 5.2's floor comparison. That also makes it the
   realistic Lean target (direction D), which is why A should precede D.
4. **The one missing lemma is half a page and already verified.** The balanced-word height
   bound is Remark 4.3's sketch; the computation above finds it holds with constant 1 across
   441 152 rotations.

**Sequencing.** Do not fold this into PR #6 — that PR is finished, green, and waiting on
Josefina López's comments. Run the `phase1d` audit of §2 against `main` after PR #6 merges in
mid-October, then decide whether the result is a v3 section or a short separate note.

**What this recommendation is not.** Direction A does not bear on (DE), on Open Problem C, on
cycle exclusion, or on the Collatz conjecture. It is a complete answer to a bounded question
about one family of words, and its value is that the family will then be finished.
