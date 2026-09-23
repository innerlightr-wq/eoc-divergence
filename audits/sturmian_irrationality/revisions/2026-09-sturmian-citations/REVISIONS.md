# Citation-and-provenance revision — notes (A) and (B)

**Date:** 23 September 2026
**Scope:** add the López–Stoll citations, qualify the affected claims, fix one typo in (A), and
pin the range of (A)'s Theorem 7.1. **No theorem statement, proof or numerical result is
changed**, with the single exception of the typo listed as **A-6**.

**Originals:** not touched. Neither note has a LaTeX source on this machine (searched `~/GitHub`,
`~/Documents`, `~/Downloads`, and all of `~`; the only `.tex` mentioning "Sturmian" is
`~/Downloads/EOC_Rev6.tex`, an unrelated manuscript). Per the brief, **no LaTeX was reconstructed
from the PDFs**. This file is therefore the authoritative patch list, and the two addenda
(`A_addendum.pdf`, `B_addendum.pdf`) are the publishable form of it.

**Prohibition observed:** no claim about irrationality of `Ξ_α` appears anywhere below, and the
forthcoming note is not cited. Where a pointer to it would belong, the addendum sources carry
`% TODO(Elias): add pointer to irrationality note once posted`.

**Sources of record.**

| | file | sha256 (prefix) | pages |
|---|---|---|---|
| (A) | `sources/A_2adic_Sturmian_Carry_Constant.pdf` | — | 8 |
| (B) | `sources/B_Sturmian_Mahler_Edge.pdf` | — | 11 |
| LS09 | `sources/LopezStoll_2009_Integers9_A13.pdf` | `e6901bbe7b84af72…` | 22 |
| LS21 | `sources/LopezStoll_2021_2101.12747.pdf` | `e4c5bccec262d8fd…` | 51 |

Page anchors below are PDF pages of the archived files; section and theorem numbers are the
notes' own.

---

## 0. What López–Stoll actually contain

Stated once here, used by both patch lists.

**LS09** — J. López and P. Stoll, *The 3x+1 conjugacy map over a Sturmian word*,
Integers **9** (2009), #A13, 141–162, `doi:10.1515/integ.2009.014` (MR 2506145).

* **Theorem 1** (in `ℤ₂`). For irrational `α = [0;a₁,a₂,…] ∈ (0,1)` with convergents `p_k/q_k`
  and `1c_α(j) = ⌈(j+1)α⌉ − ⌈jα⌉`,
  ```
  Φ(1c_α) = −1/3 − Σ_{j≥0} (−1)^{j+1} · 2^{q_{j+1}+q_j−1}
                            / [ 3 (3^{p_{j+1}} − 2^{q_{j+1}}) (3^{p_j} − 2^{q_j}) ] .
  ```
  The denominators are the walls of the two consecutive convergent shells; the term exponents are
  `q_{j+1} + q_j − 1`.
* **Corollary 2.** A generalized continued fraction for `−1/Φ(1c_α)`, convergent in `ℤ₂`.
* **§4.** Real-valued study. `Φ_R(m_α)` is proved **irrational** on `ℚ ∩ (ln2/ln3, 1]`, with a
  dual construction `F*` for `0 < α < ln2/ln3`. The domain restriction is forced:
  `Σ 2^{nq}/3^{np}` converges in `ℝ` **iff** `ln2/ln3 < p/q ≤ 1`.
* **Where it stops.** In their own words: "*`F` diverges at `x = ln(2)/ln(3)`, the odd
  approximations in Theorem 1 approach `−∞` and the even `+∞`*". On the 2-adic question they
  claim nothing: the abstract says the examples "**suggest**" that `Φ` maps Sturmian words to
  words of full complexity, and §4 says "*It seems that `F` additionally maps irrationals to
  transcendental numbers. **We have no proof.***"

**LS21** — J. López and P. Stoll, *The 3x+1 periodicity conjecture in ℝ*, `arXiv:2101.12747`.

* **Theorem 1.** If the trajectory of some `ζ ∈ ℚ_odd` is divergent then `lim h/ℓ = ln2/ln3`
  exactly — the critical density is the only place a rational divergent trajectory can live.
* Their aperiodicity theorem requires `lim(h/ℓ) > ln2/ln3` **strictly**.
* At `α = ln2/ln3` the real series diverges; §7 Lemma 27 names it "the divergent series
  `−Φ_R(1c_α)`", and §10 Lemma 41's terms `t_i = 2^{⌊(i−1)/α⌋}/3^i ∈ (1/6, 1/3]` are literally
  the summands of `Ξ_α`. §§7, 10, 11 study the critical word without an irrationality statement
  for it.

**Neither paper proves, or claims, anything about the 2-adic value at the critical slope.**

---

## 1. The dictionary — verified against each note's own definitions

Signs were checked term by term against (A) Definition 4.1 and (B) Theorem 4.1, and the identity
was verified numerically modulo `2^3000`.

| | note (A) | note (B) | López–Stoll |
|---|---|---|---|
| slope | `α = log₂3 ≈ 1.58496` | `α = log₂3` | `α_LS = ln2/ln3 = log₃2 ≈ 0.630930` |
| relation | — | — | `α_LS = 1/α` |
| word | `c_α`, `s_j(c_α) = ⌊jα⌋` | `S_i = ⌊iα+β⌋`, here `β = 0` | `1c_{α_LS}(j) = ⌈(j+1)α_LS⌉ − ⌈jα_LS⌉` |
| constant | `Ξ_α = Σ_{j≥0} 3^{−(j+1)}2^{⌊jα⌋}` | `Ξ_{α,0} = −Σ_{i≥0} 3^{−(i+1)}2^{⌊iα⌋}` | `Φ(1c_{α_LS})` |
| **identity** | **`Ξ_α = −Φ(1c_{ln2/ln3})`** | **`Ξ_{α,0} = +Φ(1c_{ln2/ln3})`** | — |
| shell | `(q_n, p_n)` = (length, discharge) | — | `(p_k, q_k)` = (numerator, denominator) |
| **relation** | **`(q_n, p_n) = (p_k, q_k)`** — LS's numerator is (A)'s length | | |
| approximant | `x_n = Q_n = −C_n/δ_n` | `Q_n` | `F(p_k/q_k) = ϕ(m_{p/q})/(2^{q}−3^{p})` |

*Sign check.* `Ξ_{α,β} = −Ξ(w_β)` term by term, and `s_j(c_α) = j + ⌊j(α−1)⌋ = ⌊jα⌋`, so
`c_α = w_0` and `Ξ_{α,0} = −Ξ_α`. Anchor: (B) Remark 4.2 evaluates `(1,2)^∞` to `−5`; (A) §9
records the same shell `(2,3)` as `Q = −5` with `Ξ((1,2)^∞) = C/δ = 5/1 = 5`. Consistent.

*Partial correspondence of the approximants.* LS Definition 26 sets `F(p/q) = ϕ(m_{p/q})/(2^q−3^p)`,
which **is** the periodic cycle value `Φ(m_{p/q}^∞)`. But their Lemma 27 shows
`−P_{2k+1}/Q_{2k+1} = F(p_{2k+1}/q_{2k+1})` while `−P_{2k}/Q_{2k} = F(p_{2k}/q_{2k}) + g(p_{2k}/q_{2k})`.
**Only the odd-indexed continued-fraction convergents are periodic cycle values**; the even ones
carry the extra gap term `g`. Any statement that "their convergents are the cycle values" must
carry this qualification.

*Depth correspondence.* In (A)'s coordinates the term exponents `q_{j+1}+q_j−1` of LS Theorem 1
read `p_n + p_{n+1} − 1`. Verified: the partial sums of their series have error valuations
`2, 4, 10, 26, 83, 148, 568, 1538, …`, i.e. `p_n + p_{n+1} − 1` for `n = 1, 2, 3, …` in (A)'s
§10 numbering. **(A)'s lower-convergent constants `10, 83, 568` are exactly the odd-indexed
members of that sequence.** (A)'s upper-convergent constants `p_n − 1` (`7, 64, 484`) do **not**
appear in LS's series: their alternating series exposes the depth of its own tail, not the
individual valuation `v₂(x_n + Ξ_α)` shell by shell. This is the precise sense in which (A)'s
Theorem 7.1 is sharper, and the precise sense in which it is not first.

---

## 2. Bibliography additions

Keys are Better-BibTeX style and match `references.bib` in this folder.

| key | entry | add to |
|---|---|---|
| `lopez2009conjugacy` | J. López and P. Stoll, *The 3x+1 conjugacy map over a Sturmian word*, Integers **9** (2009), #A13, 141–162. `doi:10.1515/integ.2009.014` | **(A)** and **(B)** — required |
| `lopez2021periodicity` | J. López and P. Stoll, *The 3x+1 periodicity conjecture in ℝ*, `arXiv:2101.12747` (2021) | **(B)** — required; (A) optional |
| `bernstein1996conjugacy` | D. J. Bernstein and J. C. Lagarias, *The 3x+1 conjugacy map*, Canad. J. Math. **48** (1996), 1154–1169. `doi:10.4153/CJM-1996-060-x` | **(A)** and **(B)** — needed to name `Φ` in the dictionary |
| `bernstein1994noniterative` | D. J. Bernstein, *A noniterative 2-adic statement of the 3N+1 conjecture*, Proc. AMS **121** (1994), 405–408 | both — optional |
| `lopez2012adic` | J. López and P. Stoll, *The 2-adic, binary and decimal periods of 1/3^k approach full complexity for increasing k*, Integers **12** (2012) | both — optional, related only |

In (A) the new entries continue the existing numbering from `[9]`; in (B) from `[20]`. The
addenda use author–year keys and do not depend on the notes' numbering.

---

## 3. Note (A) — patch list

### A-1 · Abstract (p. 1)

**Original (quoted):**

> For the lower Christoffel blocks `X_n` of the convergent shells `(q_n, p_n)` of `α`, the
> rotated-lever residues `x_n = −C_n(3^{q_n} − 2^{p_n})^{−1}` converge to `−Ξ_α` in `ℤ₂`, with
> the exact valuation law `v₂(x_n + Ξ_α) = p_n − 1` for upper convergents and
> `v₂(x_n + Ξ_α) = p_n + p_{n+1} − 1` for lower convergents.

**Replacement:** keep the sentence unchanged and append:

> The approximants and their 2-adic approximation depths are not new: López and Stoll
> [`lopez2009conjugacy`] expand the conjugacy value of the characteristic Sturmian word as an
> alternating series over consecutive convergent shells whose term exponents are, in the present
> coordinates, `p_n + p_{n+1} − 1`. The law stated here is an independent derivation, and is
> sharper in giving the upper and lower cases separately with exact constants.

### A-2 · §1 Introduction, second paragraph (p. 1) — **priority claim**

**Original (quoted):**

> This note begins the study of the tower itself, and presents its first theorem-grade structural
> result.

**Replacement:**

> This note begins the study of the tower itself, and presents a theorem-grade structural result
> for it. The result is not the first 2-adic theorem about this object. For every irrational
> slope, López and Stoll [`lopez2009conjugacy`, Thm. 1] give a closed 2-adic series for the
> Bernstein–Lagarias conjugacy value [`bernstein1996conjugacy`] of the characteristic Sturmian
> word, indexed by consecutive pairs of continued-fraction convergents; in the coordinates of
> this note its term exponents are `p_n + p_{n+1} − 1`, the lower-convergent depths of
> Theorem 7.1. What follows is an independent derivation, sharper in one respect: it separates
> the upper and lower convergent cases and pins each constant exactly, shell by shell.

*Rationale: "first theorem-grade structural result" is the only priority claim in the note, and
it is not sustainable as written.*

### A-3 · §3, after the display of convergent shells (p. 2) — **new remark**

**Insert** (new Remark 3.1, renumbering the section's later items if any):

> **Remark (relation to the López–Stoll normalization).** The constant `Ξ_α` is, up to sign, the
> Bernstein–Lagarias conjugacy value [`bernstein1996conjugacy`] of the Sturmian parity word
> studied by López and Stoll [`lopez2009conjugacy`]: `Ξ_α = −Φ(1c_{ln2/ln3})`, where their slope
> is the ones-density `α_LS = ln2/ln3 = 1/α` and `1c_{α_LS}(j) = ⌈(j+1)α_LS⌉ − ⌈jα_LS⌉`. Their
> convergent `p_k/q_k` is this note's shell `(q_n, p_n)` with the roles of numerator and
> denominator exchanged: their numerator is the word length, their denominator the discharge.
> The identity was verified modulo `2^3000`.

### A-4 · §5 Remark 5.2 (p. 4)

**Original (quoted):**

> The lemma is consistent with the classical fact that the periodic approximant of a one-sided
> best rational approximation agrees with the characteristic word for `q_n + q_{n+1} − O(1)`
> letters [6, 7]; the proof above is self-contained and pins the constants and both partial-sum
> depths exactly, which the valuation law requires.

**Replacement:** keep, and append after the semicolon clause:

> The 2-adic consequence of that agreement — that the periodic values of the convergent blocks
> approximate the conjugacy value of the characteristic word, with depths governed by consecutive
> convergent pairs — is Theorem 1 of [`lopez2009conjugacy`].

### A-5 · §7 Theorem 7.1 (p. 5) — **range**

**Original (quoted):**

> **Theorem 7.1** (Sturmian carry convergence law). Let `X_n` be the lower Christoffel block of
> the convergent shell `(q_n, p_n)` of `α = log₂3`, and `x_n = −C_n δ_n^{−1} ∈ ℤ₂`. Then
> `x_n → −Ξ_α` in `ℤ₂`, and, exactly, `v₂(x_n + Ξ_α) = p_n − 1` (`R_n > 0`, upper) /
> `= p_n + p_{n+1} − 1` (`R_n < 0`, lower).

**Replacement:** insert the range into the hypothesis —

> Let `n ≥ 3`, let `X_n` be the lower Christoffel block …

and add immediately after the statement:

> **Remark (range).** The proof of Lemma 5.1 uses `q_n ≥ 2` (the index range `1 ≤ i ≤ q_n − 1`
> must be non-empty) and `q_{n+1} > q_n`. In the numbering of §§9–10, where `(q_1,p_1) = (1,1)`,
> both hold from the shell `(2,3)` onward, i.e. for `n ≥ 3`; the two initial shells `(1,1)` and
> `(1,2)` have `q_n = 1` and lie outside the proof's scope. The stated formula nevertheless
> returns the correct valuations there — `2` and `1` respectively — as verified by direct
> computation. That is an observation, not an extension of the theorem, and nothing in this note
> uses the two excluded shells.
>
> **Remark (attribution).** The lower-convergent half of the law is the leading 2-adic behaviour
> already visible in [`lopez2009conjugacy`, Thm. 1], whose term exponents are `p_n + p_{n+1} − 1`
> in these coordinates. The upper-convergent constant `p_n − 1` is not exposed by that series,
> which gives the valuation of its own tail rather than `v₂(x_n + Ξ_α)` shell by shell. The proof
> here is independent of theirs.

> ⚠ **Indexing caution for the author.** §§9–10 number the shells from `n = 1` (`(q_1,p_1)=(1,1)`,
> Conjecture 8.3 reads "`n ≥ 4`", Remark 8.2 calls `(5,8)` level 4). The audit's Phase 0 §2.3
> states the same range as "`n ≥ 2`" under **0-based** indexing. **`n ≥ 3` is the correct form in
> the note's own numbering.** If a future revision renumbers the shells from `0`, the hypothesis
> must be restated as `n ≥ 2`.

### A-6 · §5, proof of Lemma 5.1, lower case (p. 4) — **the typo; the only mathematical edit**

**Original (quoted):**

> At `j* = q_n + q_{n+1}` the mismatch occurs: `m_{j*} = m_{q_{n+1}} = q_n − 1` and
> `m_{j*} + j*|R_n| = q_n + q_n|R_n| − |R_{n+1}| > q_n`.

**Replacement:**

> At `j* = q_n + q_{n+1}` the mismatch occurs: `m_{j*} = m_{q_{n+1}} = q_n − 1` and
> `m_{j*} + j*|R_n| = q_n + q_n|R_n| − q_n|R_{n+1}| > q_n`.

**Derivation of the corrected line.** With `m_{j*} = q_n − 1` and `j* = q_n + q_{n+1}`,

```
m_{j*} + j*|R_n| = (q_n − 1) + q_n|R_n| + q_{n+1}|R_n|
                 = (q_n − 1) + q_n|R_n| + (1 − q_n|R_{n+1}|)        [by (1)]
                 =  q_n + q_n|R_n| − q_n|R_{n+1}| .
```

The factor `q_n` on the last term was dropped in the printed line.

**Consequence: none.** The inequality `> q_n` follows from `|R_n| > |R_{n+1}|`, which is classical
and holds; with the misprinted term it would follow from `q_n|R_n| > |R_{n+1}|`, which is also
true. The conclusion of Lemma 5.1, Theorem 7.1, and every numerical value in §10 are unaffected.

### A-7 · §11 Next targets, item (1) (p. 7) — TODO only

**Original (quoted):**

> (1) attack Conjecture 8.3 through the window criterion, which now requires only an effective
> non-integrality statement for the truncations of `Ξ_α`;

**Action:** leave the text exactly as written; place
`% TODO(Elias): add pointer to irrationality note once posted` in the source at this point.

### A-8 · References (p. 7–8)

Append `[10]`–`[12]` (or renumber as convenient):

```
[10] J. López and P. Stoll, The 3x+1 conjugacy map over a Sturmian word,
     Integers 9 (2009), #A13, 141–162. doi:10.1515/integ.2009.014
[11] D. J. Bernstein and J. C. Lagarias, The 3x+1 conjugacy map,
     Canad. J. Math. 48 (1996), no. 6, 1154–1169. doi:10.4153/CJM-1996-060-x
[12] J. López and P. Stoll, The 3x+1 periodicity conjecture in R,
     arXiv:2101.12747 (2021).                                    [optional in (A)]
```

---

## 4. Note (B) — patch list

### B-1 · Abstract (p. 1)

**Original (quoted):**

> We position `Ξ_{α,β}` against the theorems of Mahler, Loxton–van der Poorten, Bugeaud–Laurent,
> Luca–Ouaknine–Worrell, and Masser, stating in each case the hypothesis that excludes our point,
> and consolidate the route into a single open problem…

**Replacement:**

> We position `Ξ_{α,β}` against the theorems of Mahler, Loxton–van der Poorten, Bugeaud–Laurent,
> Luca–Ouaknine–Worrell, Masser, and López–Stoll, stating in each case the hypothesis that
> excludes our point, and consolidate the route into a single open problem…

### B-2 · §4, after Theorem 4.1 (p. 3) — **new remark**

**Insert** (new Remark 4.2, renumbering the existing Remark 4.2 "Periodic sanity checks" to 4.3):

> **Remark (the object is the Bernstein–Lagarias conjugacy value; prior 2-adic work).** In
> parity-vector coordinates `Ξ_{α,β}` is a value of the 3x+1 conjugacy map `Φ` of Bernstein and
> Lagarias [`bernstein1996conjugacy`, `bernstein1994noniterative`] on a Sturmian parity word: at
> `β = 0`, `Ξ_{α,0} = Φ(1c_{ln2/ln3})`, where López and Stoll's slope is the ones-density
> `ln2/ln3 = 1/α`. That value has been studied 2-adically before. López and Stoll
> [`lopez2009conjugacy`, Thm. 1] give, for every irrational slope, a closed alternating series
> for `Φ(1c_α)` indexed by consecutive convergent pairs, together with a generalized continued
> fraction for `−1/Φ(1c_α)` convergent in `ℤ₂` (their Cor. 2). Their §4 then leaves `ℤ₂` and
> studies the real function `Φ_R`; the arithmetic conclusions of that section are archimedean
> (see §9 and Open Problem 1). The identity `Ξ_{α,0} = Φ(1c_{ln2/ln3})` was verified modulo
> `2^3000`.

### B-3 · §9 Positioning: the literature gate (pp. 7–8) — **new bullet**

**Insert** as a fifth bullet, after Masser and before Remark 9.1:

> * **López–Stoll 2009 [`lopez2009conjugacy`]; López–Stoll 2021 [`lopez2021periodicity`].** The
>   closest prior work on this exact object. The 2009 paper gives the 2-adic series and
>   continued-fraction expansion of `Φ(1c_α)` for every irrational slope — the approximants and
>   approximation depths of the present edge — and then proves irrationality of the **real**
>   values `Φ_R(m_α)`, on the domain `ℚ ∩ (ln2/ln3, 1]`, with a dual construction below
>   `ln2/ln3`. The 2021 paper proves aperiodicity for ones-density **strictly** above `ln2/ln3`,
>   and shows (its Theorem 1) that the critical density is the only place a rational divergent
>   trajectory could live. **Excluded by the domain hypothesis at both places.** The real series
>   `Σ 2^{nq}/3^{np}` converges exactly when `ln2/ln3 < p/q ≤ 1`, and the staircase `F` diverges
>   at `x = ln2/ln3` — their own §7 Lemma 27 calls it "the divergent series `−Φ_R(1c_α)`". Our
>   slope is that single excluded point, and it is excluded from the dual construction as well.
>   On the 2-adic question the 2009 paper claims nothing: its abstract says the examples
>   "suggest" full complexity, and its §4 says of the transcendence analogue, "We have no proof."
>   The exclusion mechanism is the same resonance as in Theorem 6.5(ii), reached independently by
>   the authors of the closest prior work.

### B-4 · §11 Remark 11.1 (p. 9) — **qualification**

**Original (quoted):**

> **Remark 11.1** (Not automatic). Irrationality does not follow from Sturmian aperiodicity:
> "rational 2-adic ⇒ eventually periodic valuation word" is the open periodicity conjecture [3],
> not a theorem.

**Replacement:**

> **Remark 11.1** (Not automatic). Irrationality does not follow from Sturmian aperiodicity:
> "rational 2-adic ⇒ eventually periodic valuation word" is the periodicity conjecture [3], which
> is open at our slope. It is not open everywhere: López and Stoll [`lopez2021periodicity`] prove
> it for parity words of ones-density **strictly** greater than `ln2/ln3`, and their Theorem 1
> shows that a rational divergent trajectory would have to have density exactly `ln2/ln3`. The
> critical density — the density of the mechanical words of slope `α = log₂3` studied here — is
> precisely the case their method does not reach.

*Rationale: "the open periodicity conjecture" is correct at our slope and overstated as a blanket
statement, now that the settled range is known.*

### B-5 · §11 Open Problem 1 (p. 9)

**Original (quoted):**

> **Open Problem 1** (Irrationality). Prove `Ξ_{α,β} ∉ ℚ`.

**Replacement:** keep the statement verbatim and append a sentence:

> The archimedean analogue is a theorem off the critical slope: López and Stoll
> [`lopez2009conjugacy`, §4] prove irrationality of the real values `Φ_R(m_α)` for
> `α ∈ ℚ ∩ (ln2/ln3, 1]`, and of the dual limit point below `ln2/ln3`. Neither covers
> `α = ln2/ln3`, where the real series diverges, so the 2-adic problem above is not a corollary
> of their results.

**Action:** place `% TODO(Elias): add pointer to irrationality note once posted` in the source
immediately after Open Problem 1.

### B-6 · Bibliographic note (p. 10)

**Original (quoted):**

> References [7, 8, 13, 14, 9, 10, 11, 16] were verified against primary or publisher sources;
> [12, 15] are cited from standard secondary use.

**Replacement:** extend the verified list to include the new entries, e.g.

> References [7, 8, 13, 14, 9, 10, 11, 16] and the López–Stoll and Bernstein–Lagarias entries
> were verified against primary or publisher sources; [12, 15] are cited from standard secondary
> use.

### B-7 · References (pp. 10–11)

Append `[21]`–`[23]`:

```
[21] J. López and P. Stoll, The 3x+1 conjugacy map over a Sturmian word,
     Integers 9 (2009), #A13, 141–162. doi:10.1515/integ.2009.014
[22] J. López and P. Stoll, The 3x+1 periodicity conjecture in R,
     arXiv:2101.12747 (2021).
[23] D. J. Bernstein and J. C. Lagarias, The 3x+1 conjugacy map,
     Canad. J. Math. 48 (1996), no. 6, 1154–1169. doi:10.4153/CJM-1996-060-x
```

---

## 5. Bibliographic verification — resolved; note (B) was correct

An earlier draft of this file flagged two page ranges in (B)'s bibliography as disagreeing with
`references.bib`. **Re-checked against the publisher DOI records, note (B) is right and this
audit's `references.bib` was wrong.**

| (B) reference | as printed in (B) | Crossref | OpenAlex | verdict |
|---|---|---|---|---|
| [9] Bugeaud–Laurent, `10.4064/aa220323-18-1` | Acta Arith. **209** (2023), 59–90 | 209, 59–90 | 209, 59–90 | **(B) correct** |
| [10] Luca–Ouaknine–Worrell, `10.1112/blms.70033` | Bull. LMS **57** (2025), 1360–1368 | 57(5), 1360–1368 | 57(5), 1360–1368 | **(B) correct** |

Queried 23 September 2026: `api.crossref.org/works/<doi>` and `api.openalex.org/works/doi:<doi>`,
two independent records, in agreement.

**Action taken:** `references.bib` corrected in both copies (it had 59–75 and 1360–1374), the
Bull. LMS issue number `5` added, and the works-to-add table in `REPORT.md` corrected, with the
error recorded there. **No change is proposed to note (B)** on either entry, and no
"bibliographic corrections" section was added to `B_addendum` — there is nothing to correct.
Publishing one would have introduced two errors into a record that is currently right.

The one cosmetic item in (B)'s bibliography stands as previously noted and is still not proposed
as a patch: reference [20] runs its DOI URL into the preceding text without a space
("Zenodo (2026).https://doi.org/…").

## 6. Step 5 — other notes carrying the same citation debt (report only)

Every PDF in `~/Downloads` was scanned for `Christoffel · Sturmian · mechanical word ·
convergent shell`, then the hits were checked for use of the carry constant `Ξ_α` and the
first-disagreement depth `v₂(Q(D) + Ξ_α)`. **None of them cites López or Stoll.**

### Tier 1 — same debt as (A); they consume the approximant law directly

| note | evidence | what it needs |
|---|---|---|
| **A Bit Analyzer for the Collatz Carry Equation: Saturation Laws and Window Recycling Across the Sturmian Tower** (June 2026) | its central diagnostic **is** `ℓ(D) = v₂(Q(D) + Ξ_α)`; 16 occurrences of `Ξ`; reads "the first-disagreement partial-sum depth between the periodization `D^∞` and the characteristic Sturmian word `c_α`" | the full A-1/A-2 treatment: cite LS09 as the first source of the approximants and depths, inherited through (A) |
| **Adjacent Tower Products in the Collatz Carry Equation: A General Saturation Taxonomy** (June 2026) | bit-depth taxonomy for `X_n^a X_{n+1}^b` attached to the convergents of `α`; cites (A)'s Theorem 7.1 explicitly; 10 occurrences of `Ξ` | one sentence in the preliminaries: the `n`-shell depths originate in LS09, via (A) |
| **Finite Christoffel Products in the Collatz Carry Equation: A Recursive Horizon Algorithm for Bit Depths** (June 2026) | finite products `X_{i₁}^{a₁}···X_{i_k}^{a_k}` of standard Christoffel blocks; 7 occurrences of `Ξ`; uses `Q(D)` and `v₂(Q + Ξ)` | same one-sentence attribution |

These three also inherit **A-5**: any statement of the per-shell depth they quote from (A) carries
the `n ≥ 3` range.

### Tier 2 — mention the edge, do not use the approximants; a pointer suffices once (B) is revised

| note | why it is only tier 2 |
|---|---|
| **Boundary-Driven Renewal Structure in a Sturmian-Modulated Confined-Word Process** (Aug 2026) | refers to `Ξ_{α,β}` only in its related-work paragraph on (B); its own object is a renewal process, not the 2-adic value |
| **From Sturmian Capacity to Entropy-Deficit Survival** (Sept 2026) | uses the mechanical staircase combinatorially (Beatty/Sturmian lattice paths); no 2-adic constant |
| **Symbolic Complexity is a Bounded Lever for 2-adic Carry Anti-Concentration** (June 27, 2026) | 2-adic anti-concentration, but no `Ξ_α` and no convergent-shell approximants |
| **EOC Rev 7** | four passing mentions of "Sturmian"; no use of the approximants |

### Tier 3 — no action

**The (22,34) Shell in the Collatz Carry Equation** — a finite shell census, no 2-adic constant,
no Sturmian machinery beyond the word "Christoffel" appearing once.

### Caveat

This survey covers `~/Downloads` only, which is where the note corpus lives on this machine. Notes
held elsewhere were not scanned. The scan is keyword-driven and was confirmed by reading each
hit's abstract; it is a triage, not an audit of those notes.
