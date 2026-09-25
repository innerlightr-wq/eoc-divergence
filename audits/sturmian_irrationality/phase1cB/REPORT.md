# Phase 1c-B — irrationality of Φ(1c_γ) at every irrational slope

**Status: Tasks 0, 1, 2, 3, 4 complete. Verdict: PROVED at every irrational slope.**
Proposed v2 section drafted at `v2-section-all-irrational-slopes.tex` (the paper
itself is untouched).
Date 2026-09-23. All arithmetic below is exact (Python `int`/`Fraction`); no
floating-point value enters any decision.

Labels: **PROVED** (proved here), **VERIFIED** (exact computation), **CITED**
(taken from the literature, quoted), **OPEN**.

---

## 0. Executive verdict

1. **Task 0 changes the novelty framing, and it changes it a lot.**
   For **every** irrational γ < β the statement Φ(1c_γ) ∉ ℚ is an *immediate*
   consequence of a refereed 2004 theorem (Monks–Yazinski, Discrete Math. 275),
   and the deduction is not even latent: López–Stoll 2021 writes it out on their
   p. 6 and reuses it inside the proof of their Theorem 1. **CONFIRMED, not
   refuted.** See §1.
2. The half γ > β is claimed only in **López–Stoll, arXiv:2101.12747 (v1, 29 Jan
   2021, 51 pp., no journal reference, no v2)** — unrefereed — and it rests on
   *their own* archimedean machinery (Lemmas 23–26, "the orbit of Φ_ℝ(v) has
   accumulation points"), not on anything refereed. See §2.
3. γ = β is the *single* slope excluded by both halves, by their own account
   ("Hence lim(h/ℓ) = ln2/ln3 is the only remaining possibility"). That is
   exactly the paper's theorem. **The paper's novelty claim survives Task 0
   intact.**
4. **Task 1: the generalisation is much cleaner than expected.** Lemmas 3.1,
   4.2, the alternation, Lemma 5.2 and Theorem 5.3 all go through for every
   irrational γ ∈ (0,1) with **n₀(γ) = 3, uniformly in γ** — there is no
   γ-dependent threshold at all. The one candidate threshold (`α_γ D_n < 1`) is
   automatic from n ≥ 1 because `q₂ > α_γ` always. PROVED in §4, VERIFIED at
   seven slopes in §5.
5. The β-specific steps are **not** in the depth law. They are all in
   Theorem 6.1, and they are all instances of one coincidence:
   **`α_β = 1/β = log₂3`, so that `3^{p_n}` and `2^{q_n}` are the same size to
   within a factor `2^{α D_n} < 2^{0.2}`.** At general γ these two scales part
   exponentially. See §4.4.
6. **Task 2: the Liouville step survives that parting, uniformly.** With
   `θ := γ log₂3` and `c(γ) := 2 − max(1,θ)`, every odd n ≥ 3 forces
   `c(γ)·q_n − log₂q_n < log₂H + 2 + log₂3`, and
   `c(γ) ≥ 2 − log₂3 = 0.41504… > 0` for **every** γ ∈ (0,1). The contradiction
   fires at the first odd n with `q_n ≥ 5log₂H + 22`. **PROVED**, §6.
   **Φ(1c_γ) ∉ ℚ for every irrational γ ∈ (0,1)**, by one proof, with
   `n₀ = 3` uniformly and no input about γ beyond `q_n → ∞`.
7. Tasks 3 and 4 done: depth law re-verified 2-adically (independent of the lcp
   run), exact height floors computed at every odd convergent of all seven test
   slopes, both controls behave as they must, corollaries generalise verbatim.
   §7, §8.

**Net effect on the v2 framing.** A general-slope theorem would be: the first
proof at γ = β (new); the first *refereed-grade* proof at γ > β (currently an
unrefereed preprint); an independent, effective, 2-adic reproof at γ < β (known
since 2004). Honest, and still worth writing — but the headline can no longer be
"all irrational slopes are new".

---

## 1. Task 0.1 — Monks–Yazinski 2004, Theorem 2.7

**Source obtained.** K. G. Monks and J. Yazinski, *The autoconjugacy of the
3x + 1 function*, Discrete Mathematics **275** (2004) 219–236. Author's PDF
`https://monks.scranton.edu/files/pubs/AutoConjV13.pdf`, saved as
`sources/MonksYazinski2004_AutoConjV13.pdf` (172 339 bytes), text in
`sources/my.txt`. This is the PDF linked from López–Stoll 2021's reference [8].

**Their notation** (§2, p. 5): `Q_odd` is the set of rationals with odd
denominator in reduced form, i.e. `ℚ ∩ ℤ₂`; `Φ⁻¹(x) = y₀y₁y₂…` with
`y_k = T^k(x) mod 2` is the parity vector, so **their Φ is our Φ**;
`κ_n(x) = Σ_{i<n} (T^i(x) mod 2)` is the number of ones in the first n digits of
the parity vector. Their "`lim`" with an underbar is `lim inf` (so named in the
text preceding Lemma 4.1). "Divergent" is *defined* (p. 1, §1) as the negation of
eventually cyclic: "The f-orbit of x, x itself, and O_f(x) are all said to be
eventually cyclic if O_f(x) is finite and **divergent otherwise**" — so divergent
means *the orbit set is infinite*, not that it tends to ±∞. López–Stoll restate
it the same way ("that is, if the orbit is an infinite set").

**Theorem 2.7, quoted exactly** (p. 6):

> **Theorem 2.7.** Let x ∈ Q_odd.
> (a) If the orbit of x is eventually cyclic then lim_{n→∞} κ_n(x)/n exists and
>  ln2/(ln3 + 1/m) ≤ lim_{n→∞} κ_n(x)/n ≤ ln2/(ln3 + 1/M)
> where m, M are the least and greatest cyclic elements in O(x).
> (b) If the orbit of x is divergent then
>  ln2/ln3 ≤ lim‾inf κ_n(x)/n .

The proof (§4.1, pp. 9–11) is complete and unconditional: Lemma 4.1 (lim inf is
shift-invariant), Lemma 4.2 (strictly positive orbits, via Eliahou-type
majorisation), Lemma 4.3 (strictly negative orbits, `−1 ≥ T^n(x₀) ≥ 3^κ/2^n · x₀`
and take logs), then the three cases strictly positive / mixed / strictly
negative. No positivity, no integrality, no extra hypothesis survives into the
statement.

### 1.1 Does it imply Φ(1c_γ) ∉ ℚ for every γ < β?  **YES — CONFIRMED.**

**Corollary (CITED; one-line deduction).** *Let v ∈ {0,1}^ℕ be aperiodic with
lim inf κ_n(v)/n < ln2/ln3. Then Φ(v) ∉ ℚ.*

*Proof.* Suppose x = Φ(v) ∈ ℚ. Since Φ(v) ∈ ℤ₂ and ℚ ∩ ℤ₂ = Q_odd, x ∈ Q_odd.
The parity vector of x is v, which is aperiodic; by the standard dictionary
(Monks–Yazinski p. 4: "the parity vector of x is rational if and only if x is
eventually cyclic for T") x is not eventually cyclic, i.e. O(x) is infinite,
i.e. the orbit is divergent in their sense. Theorem 2.7(b) then gives
lim inf κ_n(x)/n ≥ ln2/ln3, contradicting the hypothesis. ∎

For v = 1c_γ with γ irrational, `k_n(1c_γ) = ⌈nγ⌉` (Lemma 3.1 of the paper,
general slope — §3.1 below), so `lim κ_n/n = γ` exists and equals γ; and 1c_γ is
aperiodic because γ is irrational. Hence:

> **For every irrational γ ∈ (0, β), Φ(1c_γ) ∉ ℚ is a refereed consequence of
> Monks–Yazinski (2004).**

Note the deduction needs *no* Sturmian input beyond "density γ, aperiodic". It
applies to every aperiodic word of lower density < β, an uncountable family.

### 1.2 It is not even a latent consequence — López–Stoll state it

López–Stoll 2021, p. 6 (verbatim, `sources/ls.txt` lines 288–299):

> "In 2004 it was proved that the same constraint holds for rational 2-adic
> integers as well (Monks, Yazinski [8], Theorem 2.7 b): if the trajectory of
> ζ ∈ Q_odd is divergent (that is, if the orbit is an infinite set), then it
> holds (12). The contrapositive of this statement tells us that
>   lim‾inf h/ℓ < ln(2)/ln(3)  (13)
> implies ζ ∉ Q_odd, or O(ζ) is finite. However, if Φ(v) = ζ for an aperiodic
> word v, then O(ζ) is an infinite set. Thus (13) implies ζ ∉ Q_odd."

That is exactly the corollary above, in print, in 2021. **So the γ < β half of
Phase 1c-B is not new, and was not new in 2021 either.** Any v2 section must say
so in these words.

---

## 2. Task 0.2 — López–Stoll 2021, Theorem 1, and which half is theirs

**Publication status (checked 2026-09-23).** arXiv:2101.12747, *The 3x+1
Periodicity Conjeture in ℝ* [sic], J. López and P. Stoll, submitted 29 Jan 2021,
**v1 only**, 51 pages, 18 figures, MSC 11A41/11B50/11A07, **no journal
reference, no DOI other than the arXiv DOI**. Unrefereed. (Stoll died in 2019;
the paper is unlikely ever to be revised.)

**Theorem 1, quoted exactly** (p. 6):

> **Theorem 1** If the trajectory of some ζ ∈ Q_odd is divergent (that is, if the
> orbit is an infinite set), then it holds that
>   lim‾inf h/ℓ = ln(2)/ln(3),  (14)
> where h is the number of 1's in the first ℓ digits of the parity vector v of ζ.

**Its proof (p. 29–30, verbatim) splits into exactly the two halves:**

> "Proof of Theorem 1. The word v is aperiodic.
> If lim‾inf (h/ℓ) > ln(2)/ln(3), then limit Φ_ℝ(v) exists by Lemma 23, and the
> orbit of Φ_ℝ(v) has accumulation points by Lemma 26, which implies
> Φ_ℝ(v) ∉ Q_odd. From (15) and (16) it follows that the 2-adic Φ(v) is
> aperiodic.
> If lim‾inf (h/ℓ) < ln(2)/ln(3), then Φ(v) ∉ Q_odd, because a divergent
> trajectory of an Φ(v) ∈ Q_odd implies lim‾inf (h/ℓ) ≥ ln(2)/ln(3) (Monks,
> Yazinski [8], Theorem 2.7 b). Thus Φ(v) is aperiodic.
> Hence lim‾inf (h/ℓ) = ln(2)/ln(3) is the only remaining possibility."

So, **explicitly by their own bookkeeping**:

* **γ > β half: theirs, unrefereed.** It rests on Lemma 23 (convergence of the
  *real* series Φ_ℝ(v) when lim inf h/ℓ > ln2/ln3), Lemma 24, Lemma 25 (the
  sandwich Φ_ℝ(0c_α) ≤ Φ_ℝ(s') ≤ Φ_ℝ(1c_α)) and Lemma 26 (the real orbit has an
  accumulation point, hence is not an orbit of a rational, by Monks–Yazinski
  Lemma 3.2 / Cor. 3.3). It is archimedean throughout, and it is the part of
  their Theorem 1 that is not a citation.
* **γ < β half: not theirs.** One sentence, and the sentence is a citation of
  Monks–Yazinski Theorem 2.7 (b).
* **γ = β: neither half applies**, by their own closing line.

---

## 3. Task 0.3 — the novelty map

| slope γ ∈ (0,1) irrational | Φ(1c_γ) ∉ ℚ | status of the best existing argument |
|---|---|---|
| γ < β | **known** | Immediate corollary of Monks–Yazinski 2004 Thm 2.7(b) (**refereed**, Discrete Math. 275). Written out in López–Stoll 2021 p. 6. Covers *all* aperiodic words of lower density < β, not just Sturmian ones. |
| γ = β | **ours** | No prior proof. Stated open in López–Stoll 2009; identified as "the only remaining possibility" in López–Stoll 2021. |
| γ > β | **claimed** | López–Stoll, arXiv:2101.12747 v1 (2021), Theorem 1, first half, via their Lemmas 23–26. **Unrefereed preprint, archimedean, no journal version.** Also covers all aperiodic words of lower density > β. |

Three consequences for how a "All irrational slopes" section must be framed.

1. It cannot be sold as new mathematics below β. At most: *an independent,
   2-adic, effective proof of a known statement* — with the genuine added value
   that the 2-adic route is quantitative (Corollary 7.4-style explicit height
   bounds), where Monks–Yazinski's is a pure non-effective density argument.
2. Above β it *is* worth having: it would replace an unrefereed archimedean
   argument with a short elementary 2-adic one, in the same framework as the
   γ = β theorem, and again effectively.
3. **The one thing no existing argument touches remains γ = β.** Both halves of
   López–Stoll's Theorem 1 are density arguments and both are vacuous at the
   critical density. Nothing in Task 0 erodes the paper as it stands.

**Stop rule check.** The rule "STOP if Task 0 shows the whole statement is
already known in refereed form" is *not* triggered: only the γ < β third is, and
γ = β — the paper's actual theorem — is untouched. Reporting at the Task 1
checkpoint as instructed.

---

## 4. Task 1 — generalising each ingredient

Throughout: γ ∈ (0,1) irrational, α = α_γ = 1/γ > 1, γ = [0; a₁, a₂, …] with
convergents p_n/q_n (p₀/q₀ = 0/1, p₁/q₁ = 1/a₁, p_n = a_n p_{n−1} + p_{n−2},
q_n = a_n q_{n−1} + q_{n−2}), D_n = |q_n γ − p_n|, w_n = w_{p_n,q_n} the
mechanical word of slope p_n/q_n, α_n = q_n/p_n.

Standing facts used, all classical and slope-independent:
`D_n < 1/q_{n+1}`; `q_{n+1} D_n + q_n D_{n+1} = 1`; `p_{n+1}q_n − p_n q_{n+1} =
(−1)^n`; `D_n` strictly decreasing; `q_{n+1} > q_n` for n ≥ 1;
`p_n = γq_n + (−1)^{n+1} D_n`.

### 4.1 Task 1.1 — Lemma 3.1 analogue. **PROVED, fully general.**

*Claim.* `k_n(1c_γ) = ⌈nγ⌉` for n ≥ 0, and for j ≥ 0 the (j+1)-st one of 1c_γ
occupies position ⌊jα⌋.

*Proof.* Identical to the paper's Lemma 3.1 with β ↦ γ. The first claim
telescopes from `1c_γ(j) = ⌈(j+1)γ⌉ − ⌈jγ⌉`. For the second: position i carries
the (j+1)-st one iff `⌈iγ⌉ ≤ j` and `⌈(i+1)γ⌉ ≥ j+1`. For j ≥ 1 the first reads
`iγ ≤ j`, i.e. `i ≤ jα`, i.e. `i ≤ ⌊jα⌋` (using jα ∉ ℤ, which holds because α is
irrational); the second reads `(i+1)γ > j`, i.e. `i ≥ ⌊jα⌋`. Hence `i = ⌊jα⌋`.
For j = 0 both force i = 0 = ⌊0·α⌋. ∎

**The proof uses only: γ ∈ (0,1), γ irrational. No β-specific input.** (It does
*not* use α > 1, though that is true and is used later.)

### 4.2 Task 1.2 — alternation. **PROVED (classical), fully general.**

*Claim.* For γ ∈ (0,1) irrational with the above indexing,
`p_n/q_n > γ ⟺ n odd`; equivalently `sign(γ − p_n/q_n) = (−1)^n`, equivalently
`p_n = γ q_n + (−1)^{n+1} D_n`.

*Proof.* Standard: `γ − p_n/q_n = (−1)^n |γ − p_n/q_n|` for the convergents of a
simple continued fraction with `p₀/q₀ = a₀ = 0`. Anchor: `p₀/q₀ = 0 < γ` (n = 0,
even, below) and `p₁/q₁ = 1/a₁ > γ` since `a₁ = ⌊1/γ⌋ < 1/γ` (n = 1, odd,
above). The alternation then propagates by the classical identity
`p_{n+1}/q_{n+1} − p_n/q_n = (−1)^n/(q_n q_{n+1})`. ∎

Consequences used below, both general: for n odd, `η_n := α_n − α < 0`
(approach from above in slope ⇒ from below in α); for n even, `η_n > 0`. In both
cases `|η_n| = D_n/(p_n γ) = α D_n / p_n`.

This is the **only** place the "side" enters, and it is a statement about γ's
continued fraction alone. In particular the *long* depth `q_n + q_{n+1} − 1`
occurs at odd n for **every** slope, above or below β. Nothing here knows about
2 or 3.

### 4.3 Task 1.3 — Lemma 4.2 (height) is already general. **CONFIRMED.**

The paper's Lemma 4.2 is stated for "coprime 1 ≤ p ≤ q" and `w = w_{p,q}`, with
no reference to β; its proof uses only `k_{i+1}(w) = #{0 ≤ j < p : j < (i+1)p/q}
≥ (i+1)p/q` and the monotonicity of `i ↦ ρ^{q−1−i}2^i`, ρ = 3^{p/q}. So
`0 < c_{w_n} ≤ q_n · max(2^{q_n}, 3^{p_n})` holds for every slope and every
n ≥ 1 (p_n ≥ 1 requires n ≥ 1). **No change needed.** VERIFIED in the existing
`scripts/verify.py heights` run over all p/q with q ≤ 120 — which is already a
general-slope check, since it ranges over all mechanical words, not only β's
convergents.

Likewise Propositions 2.1–2.3 (closed form, isometry, shift) and Proposition 4.1
(periodic value `c_w/(2^ℓ − 3^k)`) contain no slope at all, and Remark 4.3
(unbalanced counterexample) is slope-free.

### 4.4 Task 1.4 — **every β-specific step, and its replacement**

I went through Lemma 5.2 (floor comparison) and Theorem 5.3 (depth law) line by
line. Result: **the depth law is not β-specific anywhere.** The three candidates
named in the brief resolve as follows.

| # | Step (paper) | Uses | Verdict at general γ | Replacement |
|---|---|---|---|---|
| S1 | L5.2, case n even, "the two floor sequences differ by at most one, since `j\|η_n\| ≤ p_n\|η_n\| = αD_n < α/q_{n+1} < 1`" | `α/q_{n+1} < 1`, i.e. `q_{n+1} > α` | **β-specific as written** (α = 1.585 makes it free) | threshold **(T1) `q_{n+1} > α_γ`** — and (T1) is *automatic for n ≥ 1*, see Lemma A below |
| S2 | L5.2, even, `j α D_n < p_n α D_n < p_n α / q_{n+1} ≤ 1` via `p_n α < q_n < q_{n+1}` | `p_n α < q_n` ⟸ n even ⟹ p_n/q_n < γ | general | none |
| S3 | L5.2, even, depths: `p_n α = q_n − αD_n`, `0 < αD_n < 1` | (T1) | as S1 | (T1) |
| S4 | L5.2, odd, (5.3) `m_{p_{n+1}} = p_n − 1`, `p_{n+1}α_n = q_{n+1} − 1/p_n` | `p_{n+1}q_n − p_n q_{n+1} = (−1)^n = −1`, `gcd(p_n,q_n)=1` | general | none |
| S5 | L5.2, odd, (5.4) `(p_n+p_{n+1})αD_n = 1 + p_n α(D_n − D_{n+1})` | `p_m = γq_m + (−1)^{m+1}D_m`, `q_{n+1}D_n + q_nD_{n+1} = 1` | general (β ↦ γ verbatim) | none |
| S6 | L5.2, odd, `0 < p_nα(D_n−D_{n+1}) < (q_n+1)D_n ≤ (q_n+1)/q_{n+1} ≤ 1`, giving LHS of (5.4) ∈ (1,2) | `p_nα = q_n + αD_n < q_n + 1` needs `αD_n < 1`; `q_{n+1} ≥ q_n + 1` | **(T1)** + general | (T1) |
| S7 | L5.2, odd, (5.5) `p_{n+1}αD_n = 1 − p_nαD_{n+1} < 1` | S5 and `D_{n+1} > 0` | general | none |
| S8 | L5.2, odd, `j\|η_n\| ≤ (p_n+p_{n+1})αD_n/p_n < 2/p_n ≤ 1`, "since **p_n ≥ 2** for n ≥ 3" | `p_n ≥ 2` | **general**: p₁ = 1, p₂ = a₂, p₃ = a₃a₂ + 1 ≥ 2, p_n ↑ for n ≥ 2, so **p_n ≥ 2 for all n ≥ 3, every γ** | none (keep n ≥ 3) |
| S9 | L5.2, odd, no `j ≤ p_{n+1}` satisfies (5.2); the range `j = p_{n+1}+i`, `1 ≤ i ≤ p_n−1`, has `m_j ≤ p_n − 2` | `gcd(p_n,q_n)=1`, S6, S7 | general | none |
| S10 | L5.2, odd, `⌊j*α_n⌋ = q_n + q_{n+1} − 1/p_n` ⇒ `= q_n+q_{n+1}−1` | `p_n ≥ 2` | general for n ≥ 3 (S8) | none |
| S11 | L5.2, odd, `⌊j*α⌋ = q_n+q_{n+1}` via `0 < α(D_n−D_{n+1}) < αD_n < α/q_{n+1} < 1` | **(T1)** | as S1 | (T1) |
| S12 | Thm 5.3, "both position sequences are strictly increasing" | `α > 1` (true: α = 1/γ, γ<1) and `α_n = q_n/p_n > 1` (true for n ≥ 2) | general | none |
| **S13** | **Thm 6.1**, "Since n is odd, `3^{p_n} > 2^{q_n}`, so `δ_n < 0` and `\|δ_n\| < 3^{p_n} = max(2^{q_n},3^{p_n})`" | **`p_n/q_n > β`**, which for n odd follows from `p_n/q_n > γ` only when **γ ≥ β** | **β-specific, essentially** | keep `\|δ_n\| < max(2^{q_n},3^{p_n})` — true always, no sign claim |
| **S14** | **Thm 6.1**, `c_n ≤ q_n 3^{p_n}` | same specialisation of L4.2 | **β-specific** | `c_n ≤ q_n max(2^{q_n},3^{p_n})` |
| **S15** | **Thm 6.1**, `3^{p_n} = 2^{p_n α}` and `p_n α − q_n = α(p_n − q_nβ) = αD_n` | **`α = log₂3` ⟺ `γ = β`** — the coincidence `α_β = 1/β = log₂3` | **the one real β-specific step** | none: at general γ, `p_n log₂3 = θ q_n ± D_n log₂3` with **θ := γ log₂3 ≠ 1**; the two scales part exponentially. This is Task 2. |
| S16 | Thm 6.1, `αD_n < α/q_{n+1} ≤ α/8 < 0.2` "because n ≥ 3 forces `q_{n+1} ≥ 8`" | `q₄ = 8` **for β** | **β-specific numeric** | (T1) gives `αD_n < α/q_{n+1} < 1` for n ≥ 1, hence `3^{p_n} < 2^{q_n+1}` uniformly; the sharper 0.2 is not needed |
| S17 | Thm 6.1, `\|M_n\| < 2.3Hq_n2^{q_n} ≤ 4Hq_n2^{q_n}`, and the final numeric `q_n ≥ 2log₂H + 20` | S16's constant | **β-specific numerics** | recompute from the uniform constants; see §6 |

**Lemma A (PROVED).** *For every irrational γ ∈ (0,1) and every n ≥ 1,
`q_{n+1} > α_γ`; hence `α_γ D_n < α_γ/q_{n+1} < 1`.*

*Proof.* `γ = [0;a₁,a₂,…]` gives `α_γ = 1/γ = [a₁;a₂,a₃,…]`, so
`a₁ < α_γ < a₁ + 1`. Now `q₁ = a₁` and `q₂ = a₂q₁ + q₀ = a₂a₁ + 1 ≥ a₁ + 1 >
α_γ`. Since `q_{n+1} ≥ q₂` for n ≥ 1 and `(q_m)_{m≥1}` is strictly increasing,
`q_{n+1} > α_γ` for all n ≥ 1. The second claim is `D_n < 1/q_{n+1}`. ∎

This is the step I expected to produce a genuine γ-dependent threshold `n₀(γ)`
(the brief anticipated "fails for small n when α_γ = 1/γ is large"). It does not:
a large `α_γ` forces a correspondingly large `a₁ = q₁`, and `q₂ > a₁`. The
stress-test slope `γ ≈ 1/(7 + 1/π)` (α_γ = 7.318…, a₁ = 7, q₂ = 22) is in the
table of §5 and behaves exactly like the others.

### 4.5 The generalised depth law

> **Theorem 1′ (depth law at every irrational slope). PROVED.**
> Let γ ∈ (0,1) be irrational, α = 1/γ, and let p_n/q_n, w_n be as above. Then
> for every n ≥ 3,
>
>  v₂( Φ(1c_γ) − Φ(w_nᐩ) ) = lcp(1c_γ, w_nᐩ) = q_n + q_{n+1} − 1 (n odd),
>   = q_n − 1 (n even),
>
> where wᐩ denotes w^∞. The first mismatch of one-positions occurs at
> j* = p_n + p_{n+1} (n odd), j* = p_n (n even).
>
> **n₀(γ) = 3, uniformly in γ. There is no γ-dependent threshold.**

*Proof.* Verbatim the proofs of Lemma 5.2 and Theorem 5.3 with β ↦ γ,
α ↦ α_γ = 1/γ, using: §4.2 for the sign of η_n; Lemma A for every occurrence of
`αD_n < 1` (steps S1, S3, S6, S11); `p_n ≥ 2 for n ≥ 3` (step S8, general as
shown); and §4.1 for the one-positions. Every remaining step (S2, S4, S5, S7,
S9, S10, S12) is a classical continued-fraction identity with no slope-specific
content. ∎

*Remark (a small simplification, not needed).* The bound `j|η_n| < 1` of S8/S1 is
used to call (5.2) an equivalence. It is not required: for `t ≥ 0`,
`⌊x+t⌋ ≥ ⌊x⌋+1 ⟺ {x}+t ≥ 1` unconditionally. Keeping S8 costs nothing, so I did
not disturb the proof.

---

## 5. VERIFIED — the depth law at seven general slopes

`work/slopes.py`, `work/depthcheck.py` (exact `Fraction` arithmetic; `⌊jα⌋` is
certified by bracketing α between two consecutive convergents `q_m/p_m`,
`q_{m+1}/p_{m+1}` and requiring the two floors to agree — a `RuntimeError` is
raised otherwise, and none was). Depths computed as the true longest common
prefix of the two one-position sequences. Predicted vs. computed, plus the
predicted vs. computed first-mismatch index j*.

| slope γ | CF | levels n checked | max depth reached | mismatches |
|---|---|---|---|---|
| 1/φ = (√5−1)/2 | [0;1,1,1,…] | 1 … 26 | 317 810 | none |
| √2 − 1 | [0;2,2,2,…] | 1 … 14 | 275 806 | none |
| e − 2 | [0;1,2,1,1,4,1,1,6,…] | 1 … 14 | 208 523 | none |
| [0;50,1,1,…] (large a₁, α_γ = 50.618) | [0;50,1,1,…] | 1 … 18 | 211 633 | none |
| [0;1,97,1,1,…] (large early a₂) | [0;1,97,1,…] | 1 … 18 | 254 828 | none |
| [0;1,1,1,1000,1,…] (huge a₄) | [0;1,1,1,1000,1,…] | 1 … 12 | 165 211 | none |
| γ ≈ 1/(7 + 1/π), α_γ = 7.3183 | [0;7,3,7,15,1,292,…] | 1 … 4 | 2 597 | none |

**Every value agrees, at every level, including j\*.** Sample (1/φ): n = 9 gives
q₉ + q₁₀ − 1 = 55 + 89 − 1 = 143, computed 143, j* = p₉ + p₁₀ = 34 + 55 = 89,
computed 89; n = 10 gives q₁₀ − 1 = 88, computed 88, j* = p₁₀ = 55, computed 55.

**Small-n behaviour.** Theorem 1′ is stated for n ≥ 3 (to get p_n ≥ 2). The
computation shows it in fact holds from **n = 1** at all seven slopes, because
when p_n = 1 the quantity `q_n + q_{n+1} − 1/p_n` is already the integer
`q_n + q_{n+1} − 1`, so step S10 survives. I have not proved the n ∈ {1,2} case
and see no reason to: n ≥ 3 loses nothing.

**No small-n failures, and no γ-dependent n₀, were observed at any slope —
including the two designed to stress `n₀` (α_γ = 50.6 and α_γ = 7.32).**

---


## 6. Task 2 — the uniform Liouville step. **PROVED**

### 6.1 Set-up and the two regimes

γ ∈ (0,1) irrational, α = 1/γ, convergents p_n/q_n, D_n = |q_nγ − p_n|,
w_n = w_{p_n,q_n}, `δ_n = 2^{q_n} − 3^{p_n}`, `c_n = c_{w_n}`,
`Φ(w_nᐩ) = c_n/δ_n` (Prop. 4.1). Put

  **G_n := max(2^{q_n}, 3^{p_n}), Λ_n := log₂G_n = max(q_n, p_n·log₂3),
  θ := γ·log₂3, κ := max(1,θ) − 1, c(γ) := 2 − max(1,θ) = 1 − κ.**

*Regimes.* **A** = `2^{q_n} ≥ 3^{p_n}` ⟺ `p_n/q_n ≤ β`, so `Λ_n = q_n`;
**B** = otherwise, `Λ_n = p_n log₂3`. Since n is odd, `p_n/q_n > γ`, so:

* γ > β ⟹ every odd convergent is in **B** (and `Λ_n ≈ θq_n > q_n`);
* γ = β ⟹ every odd convergent is in **B**, but only just: `Λ_n = q_n + αD_n`,
  `αD_n < 0.2` — this is the paper's step S13/S15;
* γ < β ⟹ odd convergents are **eventually in A**, but may **start in B**, since
  `p_n/q_n > γ` does not yet mean `p_n/q_n < β` at small n. Verified: for
  γ = 1/φ = 0.6180… < β the odd convergents run B (n = 3, p/q = 2/3 = 0.667 > β),
  then A from n = 5 on (5/8 = 0.625 < β) — §7.3.

So a general-slope proof must **not** branch on γ. It branches on nothing: the
bound below is uniform in n and γ.

### 6.2 The inequality

> **Theorem 2′ (uniform Liouville step). PROVED.**
> Let γ ∈ (0,1) be irrational and suppose `Φ(1c_γ) = u/v` with `u ∈ ℤ`, `v ≥ 1`,
> `gcd(u,v) = 1`; put `H = max(|u|,v)`. Then every odd n ≥ 3 satisfies
>
>  **(K)  q_{n+1} − κ·q_n < log₂H + log₂q_n + 2 + log₂3**
>
> and consequently
>
>  **(L)  c(γ)·q_n − log₂q_n < log₂H + 2 + log₂3.**

*Proof.* `Φ(1c_γ) ∈ ℤ₂`, so v is odd. Set `M_n = u δ_n − v c_n ∈ ℤ`, so that
`Φ(1c_γ) − Φ(w_nᐩ) = M_n/(v δ_n)`.

*Lower bound.* `δ_n` is odd (2^{q_n} − 3^{p_n} with q_n, p_n ≥ 1) and v is odd,
so `v₂(M_n) = v₂(Φ(1c_γ) − Φ(w_nᐩ)) = q_n + q_{n+1} − 1` by Theorem 1′ (n odd,
n ≥ 3). The valuation is finite, hence `M_n ≠ 0` and

  `|M_n| ≥ 2^{q_n + q_{n+1} − 1}`.  (L1)

*Upper bound.* `|δ_n| = |2^{q_n} − 3^{p_n}| < G_n` (the two powers are distinct
and positive), and `c_n ≤ q_n G_n` by Lemma 4.2 — **used in its general form**,
with no assumption on which of the two powers is larger. Hence

  `|M_n| ≤ |u||δ_n| + v c_n < H G_n + H q_n G_n = H(1+q_n)G_n ≤ 2 H q_n 2^{Λ_n}`. (L2)

*Bounding Λ_n.* For n odd, `p_n = γ q_n + D_n` with `0 < D_n < 1/q_{n+1} ≤ 1`, so

  `p_n log₂3 = θ q_n + D_n log₂3 ≤ θ q_n + log₂3`,

and trivially `q_n ≤ max(1,θ) q_n`. Therefore

  `Λ_n = max(q_n, p_n log₂3) ≤ max(1,θ)·q_n + log₂3 = (1+κ)q_n + log₂3`. (L3)

*Comparison.* (L1) with (L2) gives `2^{q_n+q_{n+1}−1} < 2Hq_n 2^{Λ_n}`, i.e.

  `q_n + q_{n+1} − 1 < 1 + log₂H + log₂q_n + Λ_n`,

and substituting (L3) and cancelling `q_n` against `(1+κ)q_n` yields (K).
Finally `q_{n+1} > q_n` for n ≥ 1, so `q_{n+1} − κq_n > (1−κ)q_n = c(γ)q_n`,
which turns (K) into (L). ∎

*Remark (sharper constant).* For n ≥ 3 one has `q_{n+1} ≥ q_4 ≥ 5` in the worst
case a_i ≡ 1 (§7 item (v)), so `D_n log₂3 < (log₂3)/5 < 0.317` and the constant
`2 + log₂3 = 3.5850` in (K), (L) improves to `2.317`. Nothing below needs it.

### 6.3 The coefficient, and the γ → 1 edge

`θ = γ log₂3` is strictly increasing in γ with `θ(β) = β log₂3 = 1`. Hence

  `c(γ) = 2 − max(1, γ log₂3) = 1` for `γ ≤ β`, and `= 2 − γ log₂3` for `γ > β`,

so c is continuous, non-increasing, equal to 1 on (0, β] and decreasing on
[β, 1) to the limit

  **`c(1⁻) = 2 − log₂3 = 0.4150374992788439… > 0`, not attained.**

*This is the γ → 1 edge, and it is harmless.* Because γ is irrational and
γ < 1 strictly, `c(γ) > 2 − log₂3` always; and even the infimum is positive. The
mechanism: Regime B costs the argument a factor `2^{(θ−1)q_n}` of archimedean
size, while the depth law pays `2^{q_{n+1}} ≥ 2^{q_n}`; the proof survives
precisely because `θ − 1 < log₂3 − 1 = 0.5850 < 1 ≤ q_{n+1}/q_n`. There is no
slope in (0,1) at which the two rates meet. They would meet only at
`θ = 2`, i.e. `γ = 2/log₂3 = 1.2618… > 1` — outside the range of a slope.
**The margin is therefore structural, not numerical.**

### 6.4 The first n at which the contradiction fires

> **Corollary 2′ (effective form). PROVED.** With H as above, **every odd n ≥ 3
> satisfies `q_n < 5·log₂H + 22`.** Since `q_n → ∞` along odd n, no such u/v
> exists: `Φ(1c_γ) ∉ ℚ`.

*Proof.* Put `c₀ = 2 − log₂3 = 0.41504…`, so `c(γ) > c₀` for every γ ∈ (0,1).
Suppose some odd n ≥ 3 had `q_n ≥ 5log₂H + 22`. Then `q_n ≥ 22`, and for
`Q ≥ 22` one has `Q/log₂Q ≥ 22/log₂22 = 4.9334 > 4.8189 = 2/c₀` (the function
`Q/log₂Q` has its minimum at `Q = e` and increases thereafter; `Q = 21` gives
4.7811 < 2/c₀, so 22 is the exact integer threshold). Hence
`log₂q_n ≤ (c₀/2)q_n` and

  `c(γ)q_n − log₂q_n ≥ c₀q_n − (c₀/2)q_n = (c₀/2)q_n ≥ (c₀/2)(5log₂H + 22)
   = 1.03759·log₂H + 4.56541 > log₂H + 2 + log₂3`,

contradicting (L). ∎

*Sharper, at γ ≤ β* (where `c(γ) = 1`): the same computation with `2/c = 2` and
the threshold `Q ≥ 4` gives **`q_n < 2·log₂H + 8`** for every odd n ≥ 3.
(The published Theorem 6.1 states `q_n < 2log₂H + 20` at γ = β; the improvement
is bookkeeping, not a new idea.) All of these are certified in
`work/task2_constants.py`.

**`n₀ = 3` is uniform in γ** (Lemma A and `p_n ≥ 2` for n ≥ 3, §4.4); no step of
Theorem 2′ adds a threshold.

### 6.5 Consistency with the published theorem

At γ = β: `θ = β log₂3 = 1`, so `κ = 0`, `c(β) = 1`, and (K) reads
`q_{n+1} < log₂H + log₂q_n + 3.585` against the paper's
`q_{n+1} ≤ 3 + log₂H + log₂q_n`. The published constant is the sharper one
because the paper uses `αD_n < α/q_{n+1} ≤ α/8 < 0.2` (step S16), available only
because it knows `q_4 = 8` for β. **Theorem 2′ therefore reproves Theorem 6.1
with a marginally worse constant and no knowledge of β's continued fraction.**

> **Theorem 3′ (main, general slope). PROVED.**
> `Φ(1c_γ) ∉ ℚ` for every irrational γ ∈ (0,1).

---

## 7. Task 3 — verification and controls. **VERIFIED**

Scripts: `work/slopes.py`, `work/depthcheck.py` (§5), `work/liouville.py`,
`work/task3.py`, `work/control_rational.py`, `work/task2_constants.py`. Exact
integer / `Fraction` arithmetic; floats appear only in printed columns, never in
a decision. Test slopes: 1/φ, √2−1, e−2, [0;50,1,1,…] (α_γ = 50.618),
[0;1,97,1,…] (γ = 0.98986, large early partial quotient), [0;1,1,1,1000,…]
(huge a₄), and γ ≈ 1/(7 + 1/π) = 0.136644 (α_γ = 7.3183). Three are below β,
three above, none at β.

### 7.1 Depth law, re-checked 2-adically — **36/36 agree**

Independently of the lcp computation of §5, `v₂(Φ(1c_γ) − c_n/δ_n)` was computed
modulo `2^{L+40}` (L the predicted depth), with `Φ(1c_γ) mod 2^K` obtained from
`3^{k_K}x ≡ −c_K (mod 2^K)` and `c_n/δ_n` from the odd inverse of δ_n. **Every
one of the 36 values equals `q_n + q_{n+1} − 1`**, across all seven slopes, odd
n from 3 up to 21 (1/φ), deepest modulus `2^{46407}`. Agreement with §5's lcp
values also re-confirms Prop. 3.2 (the isometry) at general slope.

### 7.2 Liouville side — exact height floors

At every odd convergent, the exact integer
`H₀(n) = ⌊2^{q_n+q_{n+1}−1} / ((1+q_n)·G_n)⌋` was computed with `G_n` the exact
`max(2^{q_n}, 3^{p_n})`; Theorem 2′'s bounds say `Φ(1c_γ)` is not any u/v in
lowest terms with `max(|u|,v) ≤ H₀(n)`. Deepest level per slope:

| slope | γ | side of β | deepest odd n | q_n | q_{n+1} | regime | **log₂H₀** | §6 prediction `q_{n+1}−κq_n−log₂(12q_n)` |
|---|---|---|---|---|---|---|---|---|
| 1/φ | 0.618034 | below | 25 | 121 393 | 196 418 | A | **196 400** | 196 397.5 |
| √2−1 | 0.414214 | below | 13 | 80 782 | 195 025 | A | **195 007** | 195 005.1 |
| e−2 | 0.718282 | above | 13 | 18 089 | 190 435 | B | **187 915** | 187 912.9 |
| [0;50,1,1,…] | 0.019756 | below | 17 | 80 837 | 130 797 | A | **130 779** | 130 777.1 |
| [0;1,97,1,…] | 0.989860 | above | 17 | 97 336 | 157 493 | B | **102 101** | 102 099.3 |
| [0;1,1,1,1000,…] | 0.666556 | above | 11 | 63 081 | 102 131 | B | **98 552** | 98 549.6 |
| 1/(7+1/π) | 0.136644 | below | 3 | 161 | 2 437 | A | **2 428** | 2 426.1 |

The prediction tracks the exact floor to within 2–3 bits at every one of the 48
computed levels (the gap is exactly the slack in `D_n log₂3 ≤ log₂3` of (L3)).
**The Regime B slopes visibly pay the `κq_n` toll** — [0;1,97,1,…] (γ = 0.9899,
κ = 0.5689) yields log₂H₀ = 102 101 where a Regime A slope with the same q's
would yield ≈ 157 480 — **and still clears it by a wide margin**, exactly as
c(γ) = 0.4311 > 0 predicts.

### 7.3 Regimes, observed

Every odd convergent of every test slope was classified by the exact integer
comparison `2^{q_n}` vs `3^{p_n}`:

* γ > β (e−2, [0;1,97,…], [0;1,1,1,1000,…]): **regime B at every odd n**, as
  predicted.
* γ < β: **regime A from some point on, but not from the start.** 1/φ is the
  witness — n = 3 gives p/q = 2/3 = 0.6667 > β, **regime B**; n ≥ 5 gives
  5/8 = 0.625, 13/21 = 0.6190, … < β, **regime A**. √2−1, [0;50,…] and
  1/(7+1/π) are in A already at n = 3 (their odd convergents fall below β at
  once). **This is the regime switch near β, observed.** Theorem 2′ never
  branches, so the switch costs nothing.

### 7.4 Controls

**Control 1 — rational slope (`work/control_rational.py`).** For γ = p/q
rational, `1c_γ = w_{p,q}^∞` exactly — verified over 8q letters for
γ = 5/8, 2/3, 41/65 — so `Φ(1c_γ) ∈ ℚ` and no contradiction may be derivable.
Taking γ = 5/8 = [0;1,1,1,2], `Φ(1c_{5/8}) = 319/13`, H = 319. The argument
stops in **two** independent ways, both exhibited:

* the odd levels that exist give a *satisfied* bound, not a violated one:
  n = 1 forces H > 0 and n = 3 forces **H > 28**, and indeed H = 319 > 28;
* there is no deeper odd level. n = 4 is the **last** convergent (5/8 is the
  slope itself) and is even; at it the two words coincide, so the lcp is
  infinite and `M_4 = u δ_4 − v c_4 = 319·13 − 13·319 = 0` **exactly** — the
  lower bound `|M_n| ≥ 2^{depth}` is vacuous. Equivalently, `q_n → ∞` along odd
  n fails because the continued fraction of 5/8 is finite.

For comparison, γ = 2/3 gives `Φ(1c_{2/3}) = −5`, matching the paper's control.

**Control 2 — fixed periodic target (`work/task3.py`).** With γ = 1/φ and target
`Φ(w₅^∞) = 319/13` (rational), the depths `v₂(target − Φ(w_nᐩ))` are

  n = 3: 7 · n = 4: 4 · n = 5: ∞ (difference is 0) · n = 6: 12 · n = 7 … 15: **20, 20, 20, 20, 20, 20, 20, 20, 20**

— **frozen at 20 = q₅ + q₆ − 1**, while `q_n + q_{n+1} − 1` runs 54, 88, 143, …,
2583. The agreement depth is bounded while the archimedean height of the
approximants grows linearly, so the comparison of §6 yields nothing against a
rational target, exactly as it must not.

---

## 8. Task 4 — corollaries at general slope. **PROVED**

All four corollaries of §7 of the paper are slope-free once Theorem 3′ is
available; each proof goes through verbatim with β ↦ γ. The two facts they use
about the word are general:

* `1c_γ` begins with `1` (its first letter is `⌈γ⌉ = 1`, as γ ∈ (0,1)), and
  `0c_γ` begins with `0` (`⌊γ⌋ = 0`);
* `σ(1c_γ) = σ(0c_γ) = c_γ`, because for j ≥ 1 and γ irrational
  `⌈(j+1)γ⌉ − ⌈jγ⌉ = (⌊(j+1)γ⌋+1) − (⌊jγ⌋+1) = ⌊(j+1)γ⌋ − ⌊jγ⌋`.

> **Corollary 4′.a** (= Cor. 7.1). `Φ(c_γ)` and `Φ(0c_γ)` are irrational, for
> every irrational γ ∈ (0,1).
> *Proof.* `Φ(c_γ) = T(Φ(1c_γ)) = (3Φ(1c_γ)+1)/2` and
> `Φ(c_γ) = T(Φ(0c_γ)) = Φ(0c_γ)/2`; both relations are ℚ-affine and invertible,
> so the three values are rational or irrational together. ∎

> **Corollary 4′.b** (= Cor. 7.2). `Φ(σ^k 1c_γ)` is irrational for every k ≥ 0
> and every irrational γ ∈ (0,1).
> *Proof.* `Φ(σ^k 1c_γ) = T^k(Φ(1c_γ))`, and `T(x) ∈ ℚ ⟺ x ∈ ℚ` on ℤ₂ (the two
> T-preimages of y are 2y and (2y−1)/3, both rational when y is). ∎

> **Corollary 4′.c** (= Cor. 7.3). Let q ≥ 1 be odd, `T_q(n) = n/2` for n even,
> `(3n+q)/2` for n odd. For no irrational γ ∈ (0,1) is there an `n₀ ∈ ℤ` whose
> `T_q`-orbit has parity word `1c_γ`, or any shift `σ^k 1c_γ`.
> *Proof.* Verbatim the paper's: `x_j = n_j/q` satisfies `x_{j+1} = T(x_j)` with
> the same parity word, so such an `n₀` would give `Φ(1c_γ) ∈ ℚ`. ∎

> **Corollary 4′.d** (effective, = Cor. 6.2 generalised). For every irrational
> γ ∈ (0,1) and every odd n ≥ 3, `Φ(1c_γ)` is not equal to any `u/v` in lowest
> terms with
>  `max(|u|,v) ≤ 2^{q_n+q_{n+1}−1} / ((1+q_n)·max(2^{q_n},3^{p_n}))`.
> *Proof.* (L1) and (L2). ∎ The table of §7.2 instantiates this at seven slopes;
> e.g. at γ = 1/φ and n = 25 it excludes every height up to `2^{196400}`.

> **Corollary 4′.e** (new, worth stating). The map `γ ↦ Φ(1c_γ)` sends the
> irrationals of (0,1) into `ℤ₂ ∖ ℚ`; in particular there are uncountably many
> explicit aperiodic parity vectors with irrational Φ-value, each with an
> effective height bound. (Below β this is qualitatively Monks–Yazinski 2004;
> above β it is López–Stoll 2021's claim; the effectivity is new at every γ.)

**Not generalised, and still open:** the intercept. Everything above is at
intercept 0. For `1c_{γ,ρ}(j) = ⌈(j+1)γ+ρ⌉ − ⌈jγ+ρ⌉`, the one-positions become
`⌊(j−ρ)α⌋`-like and Lemma 5.2's exact identities (S4, S5, S9) break; that is the
paper's Open Problem 2 and it survives Phase 1c-B untouched.

---

## 9. Files

```
audits/sturmian_irrationality/phase1cB/
  REPORT.md                                   this file
  v2-section-all-irrational-slopes.tex        proposed v2 section (NOT in the paper)
  sources/SOURCES.md                          where each third-party paper came
                                              from; the PDFs and their text
                                              extractions are git-ignored, this
                                              repository being public
  work/slopes.py            exact CF / certified-floor machinery
  work/depthcheck.py        Task 1 validation: depth law by lcp, 7 slopes  (§5)
  work/liouville.py         periodic values, c_w, Phi mod 2^K, height floors
  work/task3.py             regimes, height floors, 2-adic depths, control 2  (§7)
  work/control_rational.py  control 1, rational slope                        (§7.4)
  work/task2_constants.py   certification of every explicit constant in §6
```

**Build check.** The draft section was compiled against an untouched copy of
`papers/critical-sturmian-irrationality/main.tex` in a scratch directory
(inserted as the new Section 8, before "Why the 2-adic place"):
`pdflatex`/`bibtex`/`pdflatex`x2 with **no errors and no undefined references or
citations**, 14 pages. `MonksYazinski2004` is **already present in `refs.bib`**
and currently uncited, so no bibliography entry has to be added — the draft
cites it and it appears as reference [12]. The paper's own files were not
modified.

## 10. Verdict

* **Task 0 CONFIRMED.** γ < β is a refereed 2004 consequence (Monks–Yazinski
  Thm 2.7(b)), stated as such in López–Stoll 2021 p. 6. γ > β is claimed only in
  an unrefereed preprint. γ = β — the published theorem — is untouched. Stop
  rule not triggered.
* **Task 1 PROVED.** Every ingredient generalises; `n₀ = 3` uniformly in γ; the
  expected γ-dependent threshold does not exist (Lemma A).
* **Task 2 PROVED.** One uniform inequality, coefficient `c(γ) ≥ 2 − log₂3 > 0`
  for all γ ∈ (0,1), contradiction at `q_n ≥ 5log₂H + 22`. The γ → 1 edge is
  structural, not numerical.
* **Task 3 VERIFIED.** 36/36 2-adic depths, 48 exact height floors, both
  controls correct, regime switch observed at 1/φ.
* **Task 4 PROVED.** All corollaries generalise; intercept ρ ≠ 0 stays open.
* **Result: `Φ(1c_γ) ∉ ℚ` for every irrational γ ∈ (0,1)**, by one elementary,
  effective, 2-adic proof.
* **No obstruction, no stop-rule trigger.**
* **Integrated** into `papers/critical-sturmian-irrationality/main.tex` on branch
  `paper/v2-all-slopes` as Section 8, with the abstract, Credit, Scope, Open
  problems and Appendix A updated and `scripts/verify.py` extended; see that
  branch's commit. The draft in this folder is kept as the audit record and is
  superseded by the paper.
