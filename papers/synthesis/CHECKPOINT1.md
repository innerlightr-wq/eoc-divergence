# Checkpoint 1 — synthesis note: outline, statements, claim ledger, title

**Nothing has been drafted beyond this file.** The note itself awaits approval of what follows.

---

## 0. Title

**Proposed (recommended):**

> **After the reduction: proved statistics, excluded structure, and the missing pointwise tool
> in the accelerated `3x+1` problem**

The brief's working title is accurate but front-loads the object rather than the thesis;
moving "after the reduction" to the front makes the one-line claim of the note its first four
words. Three alternatives, in case:

| | title | comment |
|---|---|---|
| **A** | *After the reduction: proved statistics, excluded structure, and the missing pointwise tool in the accelerated `3x+1` problem* | recommended |
| B | *Statistics without placement: the accelerated `3x+1` problem after an exact reduction* | shortest; "placement" is the programme's own word and carries the thesis |
| C | *The accelerated `3x+1` problem after reduction: proved statistics, excluded structure, and the missing pointwise tool* | the brief's, unchanged |
| D | *What is proved, what is excluded, and what is missing: a status report on the accelerated `3x+1` problem* | most neutral; reads as a survey rather than a research note |

Author line: Elias De Jesús, Independent Researcher, ORCID 0009-0007-0190-9143,
dejesuselias10@gmail.com. `amsart`, 11pt, `reqno`. MSC 2020: Primary 11B83; Secondary 11J72,
11K31, 37P05, 68R15, 03B35.

---

## 1. Outline, with target lengths

| § | content | pp. |
|---|---|---|
| 1 | Introduction: the map, the thesis in one paragraph, explicit non-claims, how to read the labels | 1.5 |
| 2 | The valuation boundary `log₂3`: the drift identity, the three orbit types, why the two open halves sit on opposite sides | 2 |
| 3 | The exact reduction: `divergent_iff_zeroConfined`, the equivalent forms, the dust `K` and its rational points | 2 |
| 4 | The statistics: sparsity, the rate `I₀`, the three scales, the record-holder data, the Sharp EOC conjecture, clustering | 3 |
| 5 | The structured sectors, excluded: a map by *kind* of structure | 3 |
| 6 | Closed routes, one table, each with its reason | 1.5 |
| 7 | **What is needed** — (a) the three-condition checklist and its controls; (b) the sign theorem; (c) border versus height; (d) the `√n` formulation; (e) the only integer-specific features; (f) the signed ladder; (g) the cycle side | 4.5 |
| 8 | Open problems, numbered and precise | 1 |
| 9 | Formal and computational resources; reproducibility | 0.75 |
| — | AI-assistance declaration; references | 0.75 |
| | **total** | **≈ 20** |

---

## 2. Every theorem, proposition and conjecture the note will state — exact wording

Numbering is the note's. Nothing below is new mathematics; every item is a restatement of
something already proved or recorded, and the source column of §3 gives the provenance of each.

### §2 — the valuation boundary

> **Proposition 2.1 (drift identity).** For odd `m₀ > 1`, with `d_k = ν₂(3m_k+1)`,
> `S_N = Σ_{k<N} d_k` and `E_N = Σ_{k<N} log₂(1 + 1/(3m_k))`,
> `log₂(m_N/m₀) = N·log₂3 + E_N − S_N`, and `0 < E_N ≤ N·log₂(1 + 1/3)`.
> **PROVED (paper).**

> **Theorem 2.2 (valuation-mean classification).** Let `M` be a bound below which the `3x+1`
> conjecture is verified and `τ_M = log₂(3 + 1/M)`. Every orbit of an odd `m₀ > 1` falls into
> exactly one of three cases, with disjoint asymptotic valuation means `D̄_N = S_N/N`:
> terminating, `lim D̄_N = 2`; cyclic, `lim D̄_N = S/L ∈ (log₂3, τ_M]`; injective,
> `lim sup D̄_N ≤ log₂3`. Equivalently `lim sup D̄_N > τ_M` if and only if the orbit reaches `1`.
> **PROVED (paper)** — *Valuation-Mean Classification*, conditional only through `M`.

> **Remark 2.3.** The boundary `log₂3` separating injective from cyclic behaviour is exact; the
> convergence criterion sits at the near-critical `τ_M`, and `log₂3 < τ_M < 2`. The two open
> halves of the problem therefore lie on **opposite sides** of one line: cycles strictly above
> it, divergence at or below it. No argument that controls only the time-average of `d_k` can
> address both.

### §3 — the exact reduction

> **Definition 3.1.** For odd `m`, `m` is **zero-confined** if `2^{S_n(m)} ≤ 3^n` for every `n`;
> equivalently `R_n = S_n − n·log₂3 ≤ 0` for every `n`. `K` denotes the set of zero-confined
> elements of `ℤ₂^×`.

> **Theorem 3.2 (exact reduction).** There is an odd `M ∈ ℕ` whose accelerated orbit diverges
> if and only if there is an odd `m ∈ ℕ` that is zero-confined:
> `(∃ M, Odd M ∧ DivergentOrbit M) ↔ (∃ m, Odd m ∧ ZeroConfined m)`.
> **PROVED (LEAN)**, `Divergence.divergent_iff_zeroConfined`, no hypotheses, axioms
> `propext, Classical.choice, Quot.sound`.

> **Definition 3.3 (DE).** *Universal drift exit* is the assertion that the right-hand side of
> Theorem 3.2 is false. **OPEN.**

> **Proposition 3.4 (equivalent forms).** (a) DE as stated; (b) `r_min(N,0) → ∞`; (c) escape at
> one corridor width is escape at all of them; (d) no zero-confined `2`-adic integer has an
> expansion ending in `0^∞`. (a) is **PROVED (LEAN)**; (b), (c), (d) are **PROVED (paper)** and
> are equivalent restatements, not routes.

> **Theorem 3.5 (signed marker).** Every eventually periodic point of `K` is a **negative**
> rational. Explicitly, a purely periodic zero-confined point of period `L` and total `S`
> satisfies `m = C_L/(2^S − 3^L)` with `C_L = Σ_{i<L} 3^{L−1−i}2^{S_i} ≥ 3^{L−1} > 0` and
> `2^S − 3^L < 0`. **PROVED (paper).**

### §4 — the statistics

> **Theorem 4.1 (windowed sparsity).** There is `θ` with `1 ≤ θ < 2` such that every
> collision-free `A ⊆ ℕ` satisfies `#(A ∩ [a, a+2^N)) ≤ 4(N+1)θ^N` for all `N` and all `a ≥ 1`.
> **PROVED (LEAN)**, `Divergence.exists_window_sparsity`; `θ ≈ 1.9762`. After Garcia–Tal, in
> Curry's explicit form. **CITED** for the original.

> **Theorem 4.2 (reciprocal summability).** A divergent accelerated orbit satisfies
> `Σ_n 1/m_n < ∞`. **PROVED (LEAN)**, `Divergence.summable_inv_orbit`.

> **Theorem 4.3 (cycle drift).** A repeated orbit value at times `i < j` forces
> `3^{j−i} < 2^{S(m_i, j−i)}`. **PROVED (LEAN)**, `Divergence.cycle_drift`; hence no periodic
> orbit is zero-confined.

> **Theorem 4.4 (confined-mass rate).** With `p_N(c) = Σ 2^{−S_N(d)}` over the `c`-confined
> valuation words `d` of length `N`, `−(1/N)·log₂ p_N(c) → I₀ = α(1 − H₂(1/α))`, `α = log₂3`,
> `I₀ = 0.0793186…`. **PROVED (LEAN)**, `Occupation.confined_mass_rate`.

> **Theorem 4.5 (three scales).** The polynomial correction to the rate of Theorem 4.4 is
> exactly `N^{−3/2}`, two-sided, for both the unweighted count and the dyadic survival
> probability, and the `O(1)` phase is an explicit geometrically weighted renewal sum whose
> jump sets are the Beatty sequences of `β = α − 1`. **PROVED (paper)**, *Three Scales of
> Confinement*; **not** formalized. Its two-sided local ballot input is derived from classical
> fluctuation theory (**CITED**: Caravenna 2005; Alili–Doney 1999).

> **Proposition 4.6 (the density, exactly).** `p_N(0)` is computed in integer arithmetic by the
> transfer recursion `f[0][0] = 1`, `f[k+1][S′] = Σ_{d≥1} f[k][S′−d]` for `S′ ≤ A[k]`,
> `A[k] = ⌊k log₂3⌋`; `num_N = Σ_S f[N][S]2^{A[N]−S}` is also the exact number of odd
> `m ∈ [1, 2^{A[N]+1})` that are `N`-confined. Over `N = 100 … 300`,
> `log₂(1/p_N(0)) − I₀N − (3/2)log₂N = −3.28 ± 0.05`. **VERIFIED.**

> **Conjecture 4.7 (sharp EOC).** `log₂ r_min(N,0) = I₀·N + (3/2)·log₂N + O(1)`.
> **CONJECTURE.** Supporting data: `r_min(N,0)` certified for `N = 1…346` by an exact scan of
> every odd `m ≡ 3 (mod 4)` below `10^12`, 24 distinct record holders, largest
> `r_min(345) = 898 696 369 947`; empirical growth exponent `0.0737` with block-bootstrap 95 %
> CI `[0.061, 0.087]`, containing `I₀` and bounded away from `0`. **VERIFIED.**

> **Proposition 4.8 (clustering).** The confined integers are not a Poisson process at the
> extreme: `Δ₁(N) = log₂r_min(N,0) − log₂(1/p_N(0)) > 0` at all 24 record holders, while the
> direct count `#{odd m ≤ 2^j : N-confined}` exceeds `2^{j−1}p_N(0)` immediately above
> `r_min(N,0)` and nowhere else. The cause is the backward chains of Theorem 5.6.
> **VERIFIED** (the two measurements); **HEURISTIC** (the attribution).

### §5 — the structured sectors, excluded

> **Theorem 5.1 (Bernstein–Lagarias).** The parity-vector map is a bijection onto `{0,1}^ℕ`,
> and a `2`-adic isometry. **CITED.**

> **Theorem 5.2 (critical Sturmian irrationality).** `Φ(1c_β) ∉ ℚ`, `β = ln2/ln3`.
> **PROVED (paper)**, Zenodo `10.5281/zenodo.22920056`. Effective: `Φ(1c_β)` is no `u/v` in
> lowest terms with `max(|u|,v) ≤ 2^{301973}`.

> **Theorem 5.3 (all irrational slopes; in preparation).** `Φ(1c_γ) ∉ ℚ` for every irrational
> `γ ∈ (0,1)`, with `n₀ = 3` uniformly and an explicit height bound; the margin is
> `c(γ) = 2 − max(1, γ log₂3) ≥ 2 − log₂3 > 0`. **PROVED (paper), in preparation.**
> Credit, stated in the note: below `β` this is an immediate consequence of **Monks–Yazinski
> (2004), Thm 2.7(b)** (**CITED**, refereed); above `β` it is *claimed* in **López–Stoll (2021),
> Thm 1** (**CITED, unrefereed preprint**); only at `γ = β` is the statement new.

> **Proposition 5.4 (balanced-square criterion).** If an aperiodic parity word has arbitrarily
> long prefixes `WW` whose block `W` is balanced, with `θ_W = (k/ℓ)log₂3`, then `Φ(v) ∉ ℚ`, by
> `(2 − max(1,θ_W))·ℓ ≤ log₂H + O(log ℓ)`. **The balance hypothesis cannot be dropped**: for
> `W = 0^a1^a`, `c_W/(ℓ·max(2^ℓ,3^k))` is unbounded. **PROVED (paper).**

> **Theorem 5.5 (density exclusions).** An aperiodic word whose lower ones-density is `< β` has
> `Φ(v) ∉ ℚ` (**CITED**, Monks–Yazinski 2004, Thm 2.7(b), refereed); the same for density `> β`
> is **claimed** in López–Stoll 2021, Thm 1 (**CITED, unrefereed**). Hence a hypothetical
> zero-confined integer orbit has parity word of lower density **exactly** `β`.

> **Theorem 5.6 (descent lemmas).** L1: a zero-confined `m ≡ 2 (mod 3)` has backward image
> `p = (2m−1)/3 < m` with one horizon to spare. L2: the backward `d = 1` chain from `x` has
> length exactly `ν₃(x+1)`, with `3^j(back^j x + 1) = 2^j(x+1)`. L4: `r_min(N,0) ≡ 3` or
> `7 (mod 12)`. L7: under a forward `d = 1` step both `ν₃(m_k+1)` and the round-trip requirement
> advance by exactly one, so the surplus is invariant; an even `d` destroys the budget.
> **PROVED (LEAN)**, the `Descent` library.

> **Proposition 5.7 (L4′).** For `i ≥ 2`, if `r_i(N) ≡ 2 (mod 3)` then `(2r_i(N)−1)/3` is one of
> `r_1(N), …, r_{i−1}(N)`; and `r_1(N) ≢ 2 (mod 3)`, which is L4. **PROVED (paper).**

### §6 — closed routes

No new statements; one table (§4 of this checkpoint lists its rows).

### §7 — what is needed

> **Criterion 7.1 (the three conditions).** A tool capable of deciding DE must (i) use `2`-adic
> integrality at unboundedly many depths; (ii) use the sign or the size of the integer; and
> (iii) couple (i) and (ii) along a single orbit. **HEURISTIC** — this is a checklist distilled
> from the closed routes, not a theorem.

> **Theorem 7.2 (the sign obstruction).** No argument that uses only the aggregate identity, the
> confinement condition and the sign of the denominator can separate the positive integers from
> the rest of `K`. Concretely, `m ↦ −m` is an exact conjugacy from `3x−1` on `ℤ_{>0}` to `3x+1`
> on `ℤ_{<0}`, valuation by valuation; for `3x−1` the argument of Theorem 3.5 yields
> `m = C′_L/(3^L − 2^S) > 0`, and `+1` is a zero-confined positive fixed point. The two systems
> agree on all three inputs and disagree on the answer. **PROVED (paper).**

> **Proposition 7.3 (the signed ladder).** `(LPC) ⟹ (PosPC) ⟹ (DE)`, where **(PosPC)** is
> "`K` contains no positive rational". The second implication is strict as far as anything
> known. Moreover (PosPC) holds **iff** for every odd `v ≥ 1` no positive odd integer has a
> zero-confined orbit under `n ↦ (3n+v)/2^{ν₂(3n+v)}` — an exact, valuation-by-valuation
> conjugacy. **PROVED (paper).** (LPC) is Lagarias's Periodicity Conjecture (**CITED**).

> **Formulation 7.4 (border versus height).** Every exclusion in §5 has the shape: an agreement
> depth of `R` with a rational of height `H` costs `R ≤ c·log₂H + O(log R)`. DE asserts that a
> **finite** height cannot buy an **infinite** border inside `K`. **HEURISTIC** as a programme
> statement. The note will say why descriptive complexity is not a substitute for height: the
> Liouville step consumes `log₂H` and nothing weaker, and the word-shadow barrier shows the
> word side alone is uncountable.

> **Formulation 7.5 (the `√n` form).** At the critical density — forced by Theorem 5.5 — a
> divergent orbit's drift `R_n` is a zero-mean lattice walk that is one-sided forever, against
> the law of the iterated logarithm for such walks. **This is a reformulation of DE, not
> progress**: the walk is deterministic and no independence is available. **HEURISTIC.**

> **Observation 7.6 (the integer-specific features).** The only features an integer has that a
> general element of `ℤ₂` does not are its finite bit length (equivalently, a terminating
> `0^∞` tail) and its archimedean size. Every attempt recorded here to read either through the
> dynamics has collapsed into a restatement of DE. A genuinely new ingredient would have to be
> a quantitative law for how the zero tail propagates into the parity digits. **OPEN.**

> **Observation 7.7 (the cycle side).** Cycle exclusion is an anti-concentration statement
> modulo `2^S − 3^L`. Fixed-prime digit counting does not reach it; the closest available
> machinery is the `p`-adic Subspace/Ridout family, which is ineffective (**CITED**: Mahler
> 1957; Ridout 1958; and the repository's own audit of its limits). **OPEN.**

### §8 — open problems

Numbered restatements only; see §5 of this checkpoint.

---

## 3. Claim ledger — every claim, its label, and its source

| # | claim | label | source |
|---|---|---|---|
| 1 | drift identity; `E_N` bounds | PROVED (paper) | *Valuation-Mean Classification* §1, Zenodo `10.5281/zenodo.22143078` |
| 2 | three orbit types, disjoint means, boundary `log₂3` | PROVED (paper) | *Valuation-Mean Classification*, Zenodo `10.5281/zenodo.22143078` |
| 3 | `divergent_iff_zeroConfined` | PROVED (LEAN) | `Divergence/Main.lean`; `docs/STATUS.md` |
| 4 | four equivalent forms of DE | (a) LEAN, (b–d) paper | `docs/EQUIVALENT_FORMS_OF_DE.md` |
| 5 | signed marker: periodic points of `K` are negative rationals | PROVED (paper) | `audits/record_holder_anatomy/REPORT.md` P1 |
| 6 | P1 verified on 1 717 periodic points of period ≤ 10 | VERIFIED | same, §3.2 |
| 7 | windowed sparsity, `θ ≈ 1.9762` | PROVED (LEAN) | `Divergence/WindowedSparsity.lean` |
| 8 | Garcia–Tal original; Curry's explicit form | CITED | Acta Arith. **90** (1999) 245–250; Zenodo `10.5281/zenodo.22087163` |
| 9 | `Σ 1/m_n < ∞` | PROVED (LEAN) | `Divergence/Summable.lean` |
| 10 | cycle drift | PROVED (LEAN) | `Divergence/CycleDrift.lean` |
| 11 | `I₀` rate | PROVED (LEAN) | `Occupation/Rate.lean` |
| 12 | `N^{−3/2}` two-sided; renewal phase; Beatty jump sets; no priority claim vs Banderier–Wallner | PROVED (paper) | *Three Scales of Confinement*, **v3** (second revision), Zenodo `10.5281/zenodo.22663600` |
| 13 | ballot/fluctuation input to (12) | CITED | Caravenna 2005; Alili–Doney 1999 (as cited in that note) |
| 14 | exact `p_N(0)`; `−3.28 ± 0.05` over `N = 100…300` | VERIFIED | `audits/record_holder_anatomy/scripts/nullmodel.py`; REPORT §2.7 |
| 15 | `r_min(N,0)` for `N ≤ 346`; 24 holders; `r_min(345)` | VERIFIED | `scripts/scan.c`; REPORT §2.2 |
| 16 | growth exponent `0.0737`, CI `[0.061, 0.087]` | VERIFIED | `scripts/q5fit.py`, `run_q5c.py`; REPORT §5.3 |
| 17 | Sharp EOC | CONJECTURE | `docs/PROGRAMME_ENDPOINT.md` |
| 18 | clustering: `Δ₁ > 0`; count excess above `r_min` | VERIFIED / HEURISTIC | REPORT §5.3, §5.6 |
| 19 | Bernstein–Lagarias conjugacy and isometry | CITED | Canad. J. Math. **48** (1996) 1154–1169 |
| 20 | `Φ(1c_β) ∉ ℚ`; height `2^{301973}` | PROVED (paper) | Zenodo `10.5281/zenodo.22920056`; `papers/critical-sturmian-irrationality` |
| 21 | all irrational slopes; margin `2 − log₂3` | PROVED (paper), in preparation | `audits/sturmian_irrationality/phase1cB/REPORT.md`; PR #6 |
| 22 | density `< β` ⟹ irrational | CITED (refereed) | Monks–Yazinski, Discrete Math. **275** (2004) 219–236, Thm 2.7(b) |
| 23 | density `> β` ⟹ irrational | **CITED (unrefereed)** | López–Stoll, arXiv:2101.12747v1, Thm 1, first half |
| 24 | balanced-square criterion; balance cannot be dropped | PROVED (paper) | `docs/RESEARCH_ASSESSMENT.md` §2; audit §1.3 |
| 25 | L1, L2, L4, L7 | PROVED (LEAN) | `Descent/*.lean` |
| 26 | L4′ | PROVED (paper) | `audits/record_holder_anatomy/REPORT.md` §2.6 |
| 27 | descent audit verdict STOP; round-trip ⟺ DE | PROVED (paper) | `audits/descent/DESCENT_AUDIT.md` |
| 28 | the three conditions | HEURISTIC | this programme; distilled from §6 |
| 29 | sign obstruction; `3x−1` mirror conjugacy | PROVED (paper) | `audits/record_holder_anatomy/REPORT.md` P3 + §2.4 |
| 30 | `(LPC) ⟹ (PosPC) ⟹ (DE)`; `(PosPC) ⟺` all `3x+v` | PROVED (paper) | same, P2; `docs/PROGRAMME_ENDPOINT.md` |
| 31 | Lagarias's Periodicity Conjecture | CITED | Amer. Math. Monthly **92** (1985) 3–23, §2 |
| 32 | word-shadow cardinality barrier | PROVED (paper) | programme notes; `docs/PROGRAMME_ENDPOINT.md` closed routes |
| 33 | `√n` / LIL reformulation | HEURISTIC | this note |
| 34 | triangle/decay programme: `ShapeTail` unconditional; pressure open | PROVED (LEAN) / OPEN | `eoc-lean-verification` `docs/RESEARCH_STATUS.md` |
| 35 | `PowerOfTwoDangerousWindowSparsity ⟹ LowFreqDecay`; the hypothesis itself open; `λ = 1` unavoidable | PROVED (LEAN) / OPEN | `docs/ARITHMETIC_FRONTIER.md` §§1–3 |
| 36 | Tao's uniform decay does not transfer to the critical confined law | PROVED (MATH) + COMPUTATIONAL | `docs/LITERATURE_SUBSPACE_TRIANGLES.md` §4 |
| 37 | Tao 2022 | CITED | Forum of Math. Pi **10** (2022) e12 |
| 38 | Mahler 1957; Ridout 1958; Subspace ineffectivity | CITED | `docs/LITERATURE_SUBSPACE_TRIANGLES.md` §§1–2 |
| 39 | Terras/Everett prefix correspondence | CITED | Acta Arith. **30** (1976) 241–252; **32** (1977) 25–30 |
| 40 | Dvoretzky–Motzkin cycle lemma | CITED | Duke Math. J. **14** (1947) 305–313 |
| 41 | transcendence of `Φ(1c_β)` via `p`-adic Roth | HEURISTIC / OPEN | `docs/RESEARCH_ASSESSMENT.md` direction I |

---

## 4. §6's table of closed routes — the rows

| route | why it fails | label |
|---|---|---|
| descent by inheritance + well-ordering | round-trip criterion is *equivalent* to DE; **L7** shows the `3`-adic budget cannot be accumulated by forward motion | PROVED (paper) |
| transport budgets | bookkeeping collapse: the budget identity is the aggregate identity again | PROVED (paper) |
| time-axis / word-level arguments | the `−1` control (a zero-confined `2`-adic fixed point) and the word-shadow cardinality barrier (uncountably many unrealizable confined words) | PROVED (paper) |
| fixed-depth Fourier / triangle methods | reach only low frequencies; `λ = 1` is unavoidable and the pressure hypothesis is open | PROVED (LEAN) for the implication; hypothesis OPEN |
| parity-type counting on the cycle side | fixed-prime digit counting gives `o(L)` information only | PROVED (MATH) |
| record-holder anatomy | the extremes are generic: every pattern reduces to L4/L4′/L1/L2, to a control artefact, or to a selection effect | PROVED (paper) + VERIFIED |

---

## 5. §8's open problems — the list

1. **(DE)** universal drift exit. **OPEN.**
2. **Open Problem C**, integer form: a finite irrationality measure for `Φ(1c_β)` over the
   **integers**. The rational-approximation analogue is false unless `β` is badly approximable;
   the integer form is untouched. **OPEN.**
3. **Sharp EOC** (Conjecture 4.7). **OPEN.**
4. **(PosPC)**: `K` contains no positive rational. Strictly between DE and (LPC). **OPEN.**
5. **Sturmian words at general intercept** `ρ ≠ 0`. **OPEN**, with the precise obstruction named.
6. **Transcendence** of `Φ(1c_β)`. **HEURISTIC**, pending a literature check on `p`-adic
   Roth/Ridout.
7. **Cycle-side anti-concentration** modulo `2^S − 3^L`. **OPEN.**
8. **`PowerOfTwoDangerousWindowSparsity`** for every shift and logarithmic `K`. **OPEN.**

---

## 6. DOIs — resolved

**Citations the note will use.**

* De Jesús, Elias (2026). *Three Scales of Confinement in Accelerated Collatz Words: Entropy,
  Ballot Persistence, and an Irrational Renewal Phase*. Technical note, second revision
  (Zenodo **version v3**, 8 September 2026).
  [doi:10.5281/zenodo.22663600](https://doi.org/10.5281/zenodo.22663600)
* De Jesús, Elias (2026). *Valuation-Mean Classification for the Accelerated Collatz Map: A
  Conditional Lyapunov Criterion, the Critical Boundary `log₂3`, and the Cycle Window*. Zenodo.
  [doi:10.5281/zenodo.22143078](https://doi.org/10.5281/zenodo.22143078)

**The version discrepancy is closed.** `10.5281/zenodo.22663600` is **v3**, which *is* the
second revision — the one carrying the irrational renewal phase, the renewal functions `U, Û`,
and the Beatty jump sets. The record's *metadata title* still shows the **v1** wording
("… and Sturmian Phase"), which is a stale field the author is correcting, not a different
document. Earlier versions, for completeness: v1 `10.5281/zenodo.22257070` (2 Sep 2026),
v2 `10.5281/zenodo.22658728` (8 Sep 2026).

Consequences for the note:

* **Theorem 4.5 is cited whole** to `10.5281/zenodo.22663600`, with the document's own title
  and an explicit "version v3, second revision" in the reference. Ledger row 12 is re-merged;
  the "version to confirm" flag is removed.
* The reference will carry the version qualifier **even after the metadata is fixed**, because
  the `N^{−3/2}` result and the renewal phase belong to specific revisions and a bare concept
  DOI would not pin them.
* The **no-priority-claim** caveat of that note's §12.2 (Banderier–Wallner, *Lattice paths below
  a line of irrational slope*, announced as work in preparation, no posted version located) is
  carried wherever Scale 3 is mentioned.

## 7. Still open from Checkpoint 1 — one item

**The title.** A, B, C or D from §0; I recommend **A**. Nothing else blocks drafting, and no
drafting has begun.

For confirmation, not blocking: the Sturmian paper is cited as **v1 only**
(`10.5281/zenodo.22920056`), the all-slopes extension is described as *in preparation*, and the
`> β` density exclusion is described as **claimed in an unrefereed preprint** at every
appearance, never as known.
