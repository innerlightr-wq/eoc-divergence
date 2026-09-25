# Checkpoint 2 — self-audit of `main.tex`

Draft: `papers/synthesis/main.tex`, **19 pp.**, compiles with **0 errors, 0 undefined
references, 0 undefined citations, 0 font warnings, 0 overfull boxes**. Title A, as approved.

*Revised after Checkpoint 2: §7(a) and §7(c) expanded and the AI declaration made specific.
§8 below re-audits only what changed; §§1–7 above stand.*

## 1. Claim labels

Declared set used, and only that set: `proved (lean)` 10, `proved (paper)` 19, `cited` 16,
`verified` 9, `heuristic` 6, `conjecture` 2, `open` 13.

**All 25 numbered statements carry a label.** (`thm:signobstruction` carries its label after
the proof block rather than before it; checked by hand.)

**One label corrected during drafting.** Equation (1), the aggregate identity, was first
labelled `proved (lean)` without qualification. Lean proves it over `ℕ`; Theorem 3.5 (the signed
marker) and Theorem 7.2 (the sign obstruction) need it over `ℤ₂^×`, where it is paper-level.
The note now says exactly that: *"`proved (lean)` over `ℕ` … the same induction over `ℤ₂^×`,
which is what Theorem 3.5 needs, is `proved (paper)`."*

## 2. Sources for every claim

Every numbered statement traces to the Checkpoint-1 ledger. Spot-checks of all thirteen
distinct numerical figures against their source files:

| figure | in the note | source |
|---|---|---|
| `r_min(345) = 898 696 369 947` | Conj. 4.7 | `audits/record_holder_anatomy/REPORT.md` §2.2 |
| `N = 1 … 346`, 24 holders | Conj. 4.7, Thm 5.6 | same |
| exponent `0.0737`, CI `[0.061, 0.087]` | Conj. 4.7 | same, §5.3 |
| `ΔAICc = 0.29`, `n_eff ≈ 7` | Conj. 4.7 | same |
| `Δ₁` offset 1.9–2.5 bits | Prop. 4.8 | same, §5.3–5.4 |
| `1.78` at `N=200`; `5.45` at `N=300`; 12 vs 2.2 | Prop. 4.8 | same, §5.6 |
| `−3.28 ± 0.05` over `N = 100…300` | Prop. 4.6 | same, §2.7 |
| 1 717 periodic points, period ≤ 10 | Thm. 3.5 | same, §3.2 |
| L4 census 218 / 128 / 0 | Thm. 5.6 | same, §2.2 |
| `2436` (331st partial quotient) | §8, item 2 | `docs/RESEARCH_ASSESSMENT.md` §4 |
| `2^301973` | Thm. 5.2 | `papers/critical-sturmian-irrationality`, Cor. 6.2 |
| `I₀ = 0.0793186` | Thm. 4.4 | `Occupation/Rate.lean`; `docs/STATUS.md` |
| `θ ≈ 1.9762` | Thm. 4.1 | `Divergence/WindowedSparsity.lean`; `docs/STATUS.md` |

Every figure was found in its source. The two written with LaTeX thin spaces
(`898\,696\,369\,947`, `1\,717`) were checked in the rendered PDF.

Lean identifiers quoted in the note (`divergent_iff_zeroConfined`,
`exists_window_sparsity`, `summable_inv_orbit`, `cycle_drift`, `confined_mass_rate`,
`aggregate_identity`) were each checked to exist, in namespace `Divergence` or `Occupation`.

## 3. Non-claims

Present in **three** places, not one: the abstract's closing sentence; the Introduction's
dedicated *Explicit non-claims* paragraph; and the closing line of §8. A sweep for phrasing
that could read as progress (`we prove/show/establish that no…`, `resolves`, `settles the…`)
returned nothing.

Additional caution, applied throughout rather than once: the density exclusion **above** `β`
is described as **claimed in an unrefereed preprint** at all three of its appearances
(Remark 5.3, Theorem 5.5, Formulation 7.5) and never as known.

## 4. Citations

All 30 bibliography entries are cited; none is unused. Four entries inherited from the Sturmian
paper's bibliography that this note does not use (Bugeaud–Laurent, Luca–Ouaknine–Worrell ×2,
Stephan) were **removed** rather than left dangling.

Entries with a DOI were Crossref-verified when the Sturmian paper was prepared, or are the
author's own Zenodo records. Two points of care:

* **`GarciaTal1999`** — the author *initials* are not recorded in either repository and were
  not re-verified for this note; the entry says so in its `note` field, and the note cites the
  result through Curry's explicit form, which is what is actually formalized.
* **`DeJesusScales`** — cited as **version v3** (the second revision), because the `N^{−3/2}`
  result and the renewal phase belong to specific revisions; v1 and v2 DOIs are recorded in the
  entry. The record's metadata title is currently the v1 wording and is being corrected; the
  note uses the document's own title.
* **`Caravenna2005`** and **`BanderierWallner`** are cited *through* `DeJesusScales`, and both
  entries say so. The no-priority-claim caveat regarding Banderier–Wallner is carried in the
  text at Theorem 4.5.

## 5. Credits required by the brief

Terras \& Everett (§4, the prefix/residue-class correspondence) · Garcia–Tal and Curry (Thm 4.1)
· Lagarias (§5, the Periodicity Conjecture) · Bernstein–Lagarias (§5, the conjugacy and
isometry) · Monks–Yazinski (Rem. 5.3, Thm 5.5) · López–Stoll 2009 (Thm 5.2, the depth
exponents) and 2021 (flagged unrefereed) · Tao and his stated limits (§6, closing paragraph) ·
Mahler and Ridout (Obs. 7.7) · Dvoretzky–Motzkin (Thm 4.4) · Eliahou (Obs. 7.7) ·
Adamczewski–Bugeaud, ADQZ, Berthé–Holton–Zamboni (Prop. 5.4) · Lothaire (§5) · the author's own
notes (Thms 2.1, 2.2, 4.5, 5.2, and §7(c)). **All present.**

## 6. Two judgement calls, flagged rather than buried

1. **Formulation 7.5** (the `√n` / law-of-the-iterated-logarithm form) carries its disclaimer
   *inside* the numbered item — "this is a reformulation of (DE), not progress toward it" —
   rather than in surrounding prose, because that section is the one most likely to be read as
   a probabilistic argument.
2. **Criterion 7.1** is labelled `heuristic` and explicitly called "a checklist distilled from
   the closed routes, not a theorem", and §7(a) then applies it to a concrete proposal so that
   its negative use is visible.

## 7. Length

14 pp. against a target of ≈15–20. The outline is covered in full; the shortfall is density,
not omission. Two genuine gaps found and filled during drafting — the aggregate identity was
used throughout but never displayed, and the accelerated↔parity dictionary was implicit — and
I would rather stop here than pad. Say the word if you want §5 or §7 expanded.


---

# 8. Re-audit of the sections changed after Checkpoint 2

## 8.1 §7(c) — the exchange-rate table (new)

Added: a five-family table giving, for each exclusion, the border depth achieved, the surplus
over the approximant's own size `Λ`, and why it wins; closing with the **generic sector** row.
Every entry traces to a statement already in the note:

| row | border | surplus | from |
|---|---|---|---|
| periodic | infinite | — | Thm. 3.5 — wins on **sign**, not height |
| convergent approximants | `q_n+q_{n+1}−1` | `q_{n+1}−1` | Thm. 5.1 (depth law) |
| balanced squares | `≥ 2ℓ` | `≥ (2−log₂3)ℓ` | Prop. 5.4 |
| density | — | — | Thm. 5.3 — **different mechanism** |
| descent | — | — | Thm. 5.5 — **different mechanism** |
| **generic sector** | **infinite required** | **none available** | the residue of the five |

**A point the table forced into the open, and worth stating plainly:** only *three* of the five
families trade border against height at all, and of those three the periodic one wins on sign
rather than on height. The prose after the table now says so. That is a more honest description
of the programme than "every exclusion is a border/height statement", which is how §7(c) read
before.

## 8.2 §7(a) — the worked checklist

**Provenance, as asked.** Both instances are generic and publicly describable, and the note now
says so in its first sentence: *"Both instances below are generic: the first is constructed for
this note as the obvious thing to try, the second is a route that was actually pursued and
closed, and whose full record is public."* **Neither is drawn from correspondence of any kind.**

* *First* — a counting argument at the level of valuation words (drift `≤ 0` ⟹ mean `≤ α`,
  plus a count). Constructed for this note. Satisfies (i); fails (ii) and (iii).
* *Second* — **the descent route**, added at your request: least zero-confined `z₀`, produce a
  smaller one, contradict minimality. Satisfies (ii) and (iii); fails (i), because its resource
  is the 3-adic budget `ν₃(m+1)` and (L7) shows it cannot be accumulated. The note also records
  the audit's *other* diagnosis — that "every `z ∈ K` admits a descending round trip" is
  **provably equivalent to (DE)** — and points at `audits/descent`, verdict **STOP**.

## 8.3 The AI declaration — confirmed present, accurate, and now specific

Present as an unnumbered section before the references. Accuracy checked clause by clause
against this programme's record. It previously said only that "several claims were corrected or
withdrawn"; it now **names four**, all of which survive into the note:

1. a sign lemma used in an earlier draft of Theorem 3.5 was **false as stated** and was replaced
   by the one-sided form actually needed;
2. the square-poorness ceiling constant was corrected from a fixed `1/(2−log₂3)` to a per-block
   quantity, and its validity restricted to balanced blocks;
3. an apparent gap between record holders and shuffled surrogates was reclassified as a
   **selection effect**, and the comparison replaced by the null model of Prop. 4.6;
4. a drift slope reported from a fit over part of the data changed by a **factor of three** once
   the sample was pre-registered.

It also records that equation (1)'s label in this note was weakened after checking what Lean
actually proves.

**Scope — resolved by the author.** The first sentence originally said AI assistance was used
*"throughout the programme"*, which I could support for the audits, computations, literature
work and this note but **not** for the Lean library development, about which I had no evidence
either way. The author supplied the accurate scope, and it is now used verbatim:

> "AI assistance (Anthropic's Claude, including Claude Code) was used for the Lean formalization
> in `eoc-divergence`, the audits, computations, literature work, and the drafting of this note."

This is **wider** than what I had evidence for — it explicitly includes the Lean formalization —
and it replaces a vaguer phrase with an enumerated one.

## 8.4 Two rendering bugs found in the new material, and fixed

* `\vt[3]` was rendering as `ν₂[3]` rather than `ν₃` — the macro took no argument. Five
  occurrences, in (L2), (L7), §6, §7(a) and the new table. A `\vth` macro was added and all
  five corrected; verified in the rendered PDF (`ν₃(m+1)` ×3, `ν₃(x+1)` ×1, with `ν₂(3m…)`
  still correct where intended).
* `\bigl(…\bigr)` around `2−log₂3` was not producing visible parentheses; replaced with plain
  parentheses and verified in the PDF.

## 8.5 Layout

The three overfull boxes present after the expansion (the largest 174 pt, in the closed-routes
table) were removed by narrowing two table specifications and splitting one display in
Theorem 2.2. **The build now has none.**


---

# 9. Re-audit of the post-merge addition (Remark 4.8 and §8 item 4)

## 9.1 What was added

**Remark 4.8**, immediately after Conjecture 4.7, separating the conjecture's two halves; and
**§8 item (4)**, the upper half alone at any exponent `c < 1`, inserted after Sharp EOC so the
two sit together. Numbering came out as intended: Conj. 4.7, Rem. 4.8, Prop. 4.9; the later §8
items shift by one and are not cross-referenced by number anywhere.

## 9.2 The claims, checked

| claim | label | check |
|---|---|---|
| lower half ⟹ `r_min → ∞` ⟹ (DE) | **proved (paper)** | `2^{I₀N}N^{3/2} → ∞`; (DE) by Prop. 3.4(b), already in the note |
| lower half is stronger than Open Problem C | **proved (paper)** | OPC asks only that least realizers grow *at all*; an exponential rate is strictly more |
| Conj. 4.7 is at least as hard as (DE) | **proved (paper)** | immediate from the first row |
| upper half does **not** imply (DE) | **open** | an upper bound on the least confined integer is consistent with (DE); stated, not asserted as proved |
| `r_min(N,0) ≤ 2^{N+1} − 1` | **proved (paper)**, **verified** | derived and independently computed — see 9.3 |

## 9.3 The elementary bound was verified, not asserted

For `m = 2^k − 1` the derivation gives `m_j = 3^j 2^{k−j} − 1` with `a_j = 1` for `j < k−1`,
hence `S_j = j` and confinement `2^j ≤ 3^j` throughout, so depth `≥ k−1`.

**Checked computationally for `k = 2 … 25`** against `anatomy.conf_depth`: the valuation word
opens with `1^{k−1}` in every case and the depth is `≥ k−1` in every case. The true depths are
much larger than the bound — `91` at `k = 25` against `24` — and the note says so, so the bound
is presented as elementary rather than as the best available.

## 9.4 A label violation of my own, caught and fixed

The first draft of the remark used `\lab{proved}`, which is **not in the declared set**
(`proved (lean)` / `proved (paper)` / `cited` / `verified` / `heuristic` / `conjecture` /
`open`). Two occurrences, both corrected to `proved (paper)`. The label census is now
`cited` 16, `conjecture` 2, `heuristic` 6, `open` 15, `proved (lean)` 10, `proved (paper)` 21,
`verified` 10 — **declared labels only**.

## 9.5 Build

16 pp.; **0 errors, 0 undefined references or citations, 0 overfull boxes.**

## 9.6 One point of substance worth flagging to the reader of this audit

The remark makes the note *less* optimistic than it was, deliberately. Section 4 previously
presented Conjecture 4.7 as a statistical conjecture supported by data; Remark 4.8 records that
half of it is **at least as hard as the programme's central open problem**, and says in terms
that nothing in Section 4 should be read as evidence that it is within reach. That is the
correct reading and it was not previously stated.
---

# 10. Cross-map revision — self-audit of the changed sections only

`main.tex`, **19 pp.** after rebasing onto the merged #14, compiles with **0 errors, 0 undefined
references, 0 undefined citations, 0 overfull boxes**. §§1–9 above stand unchanged; this section re-audits only what this revision
touched. Source for every new figure: `audits/cross_map/` (PR #18) and `audits/fingerprint_comparison/`
(PR #17).

## 10.1 What changed

| § | change |
|---|---|
| 4 | Remark 4.5, `I(q) = D(β_q‖½)/β_q`, and its `r`-independence |
| 4 | Remark 4.10, the same null model run on `5x−1` |
| 5 | Remark 5.2, the Liouville argument for other multipliers |
| 7(b) | Remark 7.3, reframing Theorem 7.2 |
| 7(c) | **new subsection** "The growth side": Lemma 7.4, Proposition 7.5, the seven-map table |
| 7(d)–(h) | relabelled from (c)–(g); the one manual cross-reference ("the height formulation (c)") updated to (d) |
| 8 | new open problem: the `5x−1` residue law |
| 9 | the two new audits added to the resources list; the brittle count "four audits" replaced by "the audits listed below" |

Numbering after the rebase onto the merged #14 (all cross-references are `\ref`, so these resolve
automatically): Remark **4.5** (the rate), Conjecture **4.8** (sharp EOC), Remark **4.9** (#14's,
which half is hard), Proposition **4.10** (clustering), Remark **4.11** (the `5x−1` null),
Remark **5.2** (other multipliers), Remark **7.3** (reframing), Lemma **7.4** (sign alignment),
Proposition **7.5** (`5x−1`).

## 10.2 Labels

Census after the revision, with #14 merged in: `proved (paper)` 28, `cited` 17, `verified` 16,
`open` 16, `proved (lean)` 10, `heuristic` 9, `conjecture` 2. No new label kind was introduced.
(Before the rebase onto #14 the same count was 26 / 17 / 15 / 14 / 10 / 9 / 2; the differences
are #14's own labels, not this revision's.)

**All six new numbered statements carry a label**: Lemma 7.4 and Proposition 7.5
`proved (paper)`; Remark 4.5 `proved (paper)` + `verified`; Remark 4.10 `verified` +
`heuristic`; Remark 5.2 `proved (paper)` + `verified`; Remark 7.3 `proved (paper)` for the
conjugacy and `heuristic` for the reading.

**One label chosen deliberately.** Remark 4.10 is split: the measurements are `verified`, but the
*reading* that `5x−1`'s ladder really departs from the null — rather than the departure being an
artefact of a short, strongly correlated ladder — is `heuristic`, and so is the trapped-orbit
mechanism offered for it. `n_eff ≈ 3.4` is stated inside the remark in bold, not in a footnote.

## 10.3 Every new figure, against its source

> **Four rows below were superseded on 2026-09-25** and are marked. They traced
> correctly to their source at the time; the *source* was defective. See §13.
> This section is left as written, because an audit log that is rewritten after
> the fact records nothing.

| figure | in the note | source |
|---|---|---|
| `I(3)=0.0793186128`, `I(5)=0.0323008158`, `I(7)=0.1698737154` | Rem. 4.5 | `audits/cross_map/data/rates.txt` |
| rate verified to `N = 500` for `q = 3,5,7` | Rem. 4.5 | same |
| ~~66 holders, depth 459~~, `r_min(459)=848 537 873 557` **— SUPERSEDED §13: 93 holders** | Rem. 4.10 | `data/delta1_D.txt` |
| ~~slope `+0.0211`, Theil–Sen `+0.0219`~~, CIs at blocks 3/8/16 **— SUPERSEDED §13: `+0.0224`, `+0.0224`** | Rem. 4.10 | same |
| ~~`n_eff = 3.4`, lag-one `0.90`~~ **— SUPERSEDED §13: `3.0`, `0.94`** | Rem. 4.10 | same |
| 23 holders, `Δ₁ = 2.19` at `N = 282`, slope `−0.0033`, exponent `0.076`, `n_eff = 6.3` | Rem. 4.10 | `data/delta1_A.txt` |
| depths `10, 83, 568` at `q = 3`; shells for `q = 5, 7` | Rem. 5.2 | `data/sturmian.txt` |
| `Ξ↑ = 2Ξ↓ − 1/q` mod `2^2000` | Rem. 5.2 | same |
| shelter column, cycle search over odd seeds `≤ 20 001` | §7(c) table | `data/criterion.txt` |
| ~~`r_min ≡ 5 (mod 16)` at every `N ≤ 459`; 65 of 66 `≡ 21 (mod 32)`~~ **— RETRACTED §13; false at `N = 2`** | §8 | `data/residues_D.txt` |
| backward step ratio `2^{⌈α_q⌉}/q = 8/5` | §8 | `data/descent.txt` |

## 10.4 Three things corrected during drafting

* **The aggregate identity was cited too loosely.** Lemma 7.4's justification and Proposition 7.5's
  proof first wrote `\eqref{eq:aggregate}` as if the displayed identity were already stated for
  general `(q,r)`. It is stated for `3x+1`. Both now say that the *induction* giving (1) does not use
  the values of `q` and `r`, and write the general identity out.
* **`m_n ≍ m_0 2^{−R_n}` needed its caveat, and the caveat is not cosmetic.** The comparison holds
  only up to `E_N` of Proposition 2.1, which is `O(1)` only while orbit values are large — and it
  fails at exactly the point the section is about: the fixed point `m = 1` of `T_{5,−1}` has
  `R_n → −∞` while the orbit is constant. §7(c) now says this and says that the proof of
  Proposition 7.5 runs through the exact identity instead.
* **"Reproducing" was too strong for the `3x+1` control.** The control scan is five times shorter
  than the one behind Conjecture 4.8 and returns 23 holders where the published scan returns 24;
  the text now says "consistent with", states the ratio, and says what the control is for
  (calibrating the instrument, so the slope contrast is measured rather than assumed).

## 10.5 Two places where the new material is deliberately weaker than it could look

* The `(3,+5)` row of the §7(c) table says "open" in the same sense as `(3,+1)`, and the text now
  adds that "open" there means only that neither mechanism decides the row, **with no claim about
  the literature** for `3x+5`.
* Remark 5.2 records that the general-slope extension's range is `γ < 2/log₂q` and states plainly
  that **the general-slope case was not checked for `q ≠ 3`**; only the critical slope was.

## 10.6 Non-claims

Unchanged and re-read: the abstract's closing sentence, the Introduction's "Explicit non-claims"
paragraph, and the closing line of §8. The new §7(c) adds one of its own — that the table is
negative, does not bound or constrain (DE), and is a re-derivation of Theorems 4.3 and 3.5 in a
family rather than a new tool.

---

# 11. §7(i) — self-audit of the new subsection only

`main.tex`, **21 pp.**, compiles with **0 errors, 0 undefined references, 0 undefined citations,
0 BibTeX warnings, 0 overfull boxes**. §§1–10 above stand unchanged; this section audits only
§7(i), "Approximate, partial and conditional forms of the missing statement", and the four
references and one label kind it adds.

## 11.1 What changed

| file | change |
|---|---|
| `main.tex` §1 | the `Labels` paragraph now declares `analogy`, scoped explicitly to §7(i) |
| `main.tex` §7 | **new final subsection (i)**, after (h); nothing before it was touched |
| `refs.bib` | four new entries: Tao (averaged NS), Caffarelli–Kohn–Nirenberg, Beale–Kato–Majda, Serrin |

## 11.2 Length, against the brief's target

The brief asked for about 1–1.5 pages. The subsection typesets to **90 lines, ≈ 1.76 pages**
(pp. 16–18), measured against 51 lines on a full page. It is over target, and this is recorded
rather than fixed by cutting: the six mandated items include a four-row table, the averaged
Navier–Stokes paragraph and the floor/ceiling derivation, and two rounds of tightening (seven
passages compressed, two bullet lists converted to prose) took it from 91 lines to 90. Further
reduction would mean dropping mandated content or the caveats, which are the part of the
subsection most worth keeping.

## 11.3 One placement judgement, recorded

The brief says the Navier–Stokes paragraph should go "as the first part of this subsection" if §7
has none — and §7 had none, `grep -ci "navier|stokes|blowup"` returning 0 — but the content list
puts the Navier–Stokes comparison at position 5. **Both were honoured**: the subsection opens with
a short framing paragraph naming the analogy and its scope, and the full comparison, table and
averaged-equation discussion sit at position 5 as listed. If the intent was that the whole
Navier–Stokes treatment lead the subsection, that is a one-block move.

## 11.4 Every citation, verified against Crossref

| key | DOI | Crossref returns |
|---|---|---|
| `TaoAveragedNS2016` | `10.1090/jams/838` | Tao; *J. Amer. Math. Soc.* **29** (3), 601–674 |
| `CaffarelliKohnNirenberg1982` | `10.1002/cpa.3160350604` | Caffarelli, Kohn, Nirenberg; *Comm. Pure Appl. Math.* **35** (6), 771–831, 1982 |
| `BealeKatoMajda1984` | `10.1007/BF01212349` | Beale, Kato, Majda; *Comm. Math. Phys.* **94** (1), 61–66, 1984 |
| `Serrin1962` | `10.1007/BF00253344` | Serrin; *Arch. Rational Mech. Anal.* **9** (1), 187–195, 1962 |
| `Tao2022` | `10.1017/fmp.2022.8` | already in `refs.bib`; not re-added |

**One discrepancy resolved, not hidden.** Crossref gives the JAMS paper's `issued` date as
2015-06-30, the online-first date; the print volume 29, issue 3 is dated 2016. The entry uses
**2016**, which is the standard citation and the year the brief specifies. Author given names were
also pulled from Crossref and match the entries. The Serrin reference the brief asked to "confirm"
is the 1962 *Arch. Rational Mech. Anal.* paper, confirmed exactly.

## 11.5 Every number, traced

The subsection introduces **no new numerical figure**. The four it quotes —
`0.0737`, the interval `[0.061, 0.087]`, `I₀ = 0.0793…`, and `N = 346` with 24 distinct record
holders — are the figures of Conjecture 4.8, already traced in §2 of this audit to
`audits/record_holder_anatomy/REPORT.md` §§2.2 and 5.3. Everything else in the subsection is
symbolic (`ε`, `c`, `β`) or a cross-reference.

## 11.6 Cross-references and labels

All eighteen cross-references are `\ref`/`\cite`, none typed as a literal number, and LaTeX reports
**0 undefined**: `prop:equivalent`, `thm:reduction`, `conj:sharp`, `rem:halves`, `thm:rate`,
`thm:scales`, `thm:sparsity`, `thm:summable`, `thm:density`, `form:walk`,
`thm:signobstruction`, `rem:notenough`, `prop:5m1`, `prop:drift`, `eq:aggregate`, `sec:needed`,
plus `DeJesusEOC` and `EOCDivergenceRepo`.

Printed numbering as it now stands (for checking against the brief, which assumed a different
merge state): Theorem **3.2** (reduction), Proposition **3.4** (equivalent forms), Theorem **4.1**
(sparsity), Theorem **4.2** (summability), Theorem **4.4** (rate), Theorem **4.6** (three scales),
Conjecture **4.8** (Sharp EOC), Remark **4.9** (which half is hard), Theorem **5.4** (density),
Theorem **7.2** (sign obstruction), Remark **7.3**, Proposition **7.5** (`5x−1`), Formulation
**7.7** (the walk). The brief's "Conjecture 4.7 / Remark 4.8" are these 4.8 / 4.9.

Label census (raw `\lab` occurrences, each kind counted once more for the §1 declaration):
`proved (paper)` 30, `cited` 19, `verified` 17, `open` 17, `proved (lean)` 12, `heuristic` 10,
`conjecture` 3, `analogy` 3. **One new kind, `analogy`**, declared in §1 and used exactly twice in
the body, both in §7(i); it is defined there as a structural comparison carrying no transfer of
technique in either direction.

## 11.7 Non-claims

All existing non-claims are untouched: the abstract's closing sentence, the Introduction's
"Explicit non-claims" paragraph, §7(c)'s over-reading warning and the closing line of §8. §7(i)
adds two of its own — in its opening paragraph and in its final sentence — stating that nothing in
it is progress toward (DE) or the Collatz conjecture, that nothing in it bears on the Navier–Stokes
problem, and that the analogy transfers no technique in either direction. The Navier–Stokes results
are cited only for their standard statements, and no claim is made about that problem.

---

# 12. Navier–Stokes status, the `Δ_N` decomposition, and the new open problem

`main.tex`, **22 pp.**, compiles with **0 errors, 0 undefined references, 0 undefined citations,
0 BibTeX warnings, 0 overfull boxes**. §§1–11 above stand unchanged; this section audits only the
three changes below and the five references they add.

## 12.1 What changed

| § | change |
|---|---|
| preamble | `\usepackage{xurl}`, to break the one long URL in the bibliography (see 12.5) |
| 4 | **Remark 4.10**, the exact decomposition (2) and what the record-holder audit therefore measures |
| 7(i) | **new part 0**, the status of the Navier–Stokes problem as of September 2026, and the statement the analogy uses |
| 7(i) part 5 | reframed as an analogy with the **unforced** problem (A)/(B), with the structural difference stated first |
| 8 | new open problem, predicting `Δ_N` |
| `refs.bib` | five entries: the OpenAI manuscript, its Lean repository, the CMI statement, Fefferman's problem description, one press report |

## 12.2 Every Navier–Stokes claim, against a primary source

Each was read directly, not taken from a summary.

| claim in the note | source, and what it actually says |
|---|---|
| manuscript dated 8 September 2026 | the PDF's own `CreationDate` is `Tue Sep 8 15:06:26 2026`; 166 pp. |
| the displayed statement of the construction | Theorem 1.1 of \[OpenAINS2026\], read verbatim: `f ∈ C_c^∞(ℝ³×(0,∞);ℝ³)`, `u(·,0)=0`, `sup_{0≤t<1}‖u(t)‖_{L²}<∞`, `limsup_{t↑1}‖u(t)‖_{L^∞}=∞` |
| "establishes alternatives (C) and (D)" | its own words: *"This establishes alternative (C) in the Millennium problem statement for Navier–Stokes as stated by Fefferman in \[13\]. Compact support also yields the corresponding construction on `T³ = ℝ³/ℤ³`, establishing alternative (D)"* |
| a Lean formalization accompanies it | the repository `openai/NavierStokesAndEuler`, which states the two theorems it formalizes and is built with Lean 4.34.0-rc2 and Mathlib. **The manuscript itself does not mention Lean** — `grep -ni "lean\|formaliz"` over its text returns nothing — so the note attributes the formalization to the repository, not to the paper |
| CMI, 11 September 2026, "has apparently been settled", "deliberately unhurried" | the CMI announcement page, both phrases quoted verbatim; it does **not** say the prize has been awarded, and it does **not** use the labels (A)–(D) |
| (A) and (B) take `f ≡ 0` | Fefferman's official problem description, read directly: (A) and (B) each say *"Take `f(x,t)` to be identically zero"*, while (C) and (D) supply *"a smooth `f(x,t)`"* |
| priority and attribution publicly disputed | a press report of 14 September 2026 |

**Two things deliberately not done.** The note does not repeat the substance of the priority
dispute, does not name the parties to it and takes no position on it; the citation exists so a
reader can follow it up, and the bib entry says it is cited *only* for the existence of the dispute.
And the note nowhere asserts that the Millennium Prize has been resolved — it reports CMI's wording
and stops.

## 12.3 The claim the note makes in its own voice

Exactly one, and it is an inference from two primary sources rather than a report: **the unforced
global regularity question is untouched and remains open.** It follows from (A)/(B) requiring
`f ≡ 0` and the construction requiring a nonzero force. Nothing else in part 0 is the note's own
assertion; everything else is `cited`.

## 12.4 The decomposition, checked

With `A_N := p_N 2^{I₀N} N^{3/2}` and `Δ_N := log₂(r_min(N,0)·p_N)`,

```
I₀N + (3/2)log₂N − log₂A_N + Δ_N
  = I₀N + (3/2)log₂N − log₂p_N − I₀N − (3/2)log₂N + log₂r_min + log₂p_N = log₂ r_min ,
```

so (2) is an identity, as the label says. `Δ_N` coincides with the audit's `Δ₁`, since
`Δ₁ = log₂r_min − log₂(1/p_N) = log₂(r_min·p_N)`; that is why the remark can say the audit's
residual *is* `Δ_N` and the renewal phase never enters. Theorem 4.6 gives `A_N ≍ 1` two-sided,
which is what "bounded above and below" reports.

The §8 item's decisive clause was checked rather than asserted: from
`log₂r_min = log₂(1/p_N) + Δ_N` with `log₂(1/p_N) → ∞`, a uniform `Δ_N ≥ −c` gives
`r_min ≥ 2^{−c}/p_N → ∞`, which is (DE) by Proposition 3.4(b). A formula for `Δ_N` without such a
bound gives nothing.

## 12.5 Build, and one preamble change

The long press-report URL produced a single overfull box of 64 pt in the bibliography.
`\usepackage{xurl}` (present in this TeX installation) fixed it; the build is back to **0 overfull
boxes**. This is the only preamble change and it affects nothing but line breaking inside `\url`.

## 12.6 Numbering, labels, length

Inserting Remark 4.10 shifts the two statements after it: clustering is now **Proposition 4.11**
and the `5x−1` null **Remark 4.12**. All references to them are `\ref`, so the note is consistent;
§10.6 of this audit lists the earlier numbering and is left as the record of that revision.

Label census: `proved (paper)` 31, `cited` 20, `open` 18, `verified` 17, `proved (lean)` 12,
`heuristic` 10, `conjecture` 3, `analogy` 3 (one of which is the §1 declaration). No new kind.

§7(i) is now **112 typeset lines ≈ 2.2 pages** (pp. 16–18), up from 1.76: part 0 is new material
the brief required, and it is roughly half a page of it. The subsection is correspondingly further
from the original 1–1.5 page target, which is recorded here rather than fixed by cutting the
sourcing.

## 12.7 Non-claims

Unchanged and re-read. §7(i)'s two non-claims still stand and now carry more weight: the analogy is
explicitly with the unforced problem, the structural difference (the forced construction chooses a
force; the accelerated map is fixed) is stated before the table rather than after it, and part 0
opens by saying that no position is taken on any of the reported Navier–Stokes status.

---

# 13. The `5x-1` sieve correction (2026-09-25)

A defect was found in `audits/cross_map/scripts/scan_rare.c` while the controls of
that audit were being reproduced in `audits/pointwise_discovery`, whose scanner
sieves nothing. It is recorded in full in
`audits/cross_map/CORRECTION_2026-09-25.md`. This section audits only what changed
in `main.tex`.

## 13.1 The defect, in one line

For `q > 4` the rare-side condition at `n = 1` is `S₁ ≥ A[1]+1`, a **lower** bound,
so the admissible seeds form one class modulo `2^{A[1]+1}`; the scanner sieved to
one class modulo `2^{A[1]+2}` — the seeds with `v₂(qm+r)` equal to `A[1]+1`
**exactly** — and so visited half of them. For `q < 4` the same condition is an
upper bound that forces `v₂ = 1` exactly, so the sieve was already right there.
**The `3x+1` ladder, and everything built on it, is unaffected**; this was checked
and not assumed (§13.4).

## 13.2 What changed in the note

| § | change |
|---|---|
| Remark 4.10 (`the same null on 5x-1`) | every `5x-1` figure regenerated from the complete rescan: `66 → 93` holders, `66/66 → 92/93` positive, OLS `+0.0211 → +0.0224`, Theil–Sen `+0.0219 → +0.0224`, `n_eff 3.4 → 3.0`, lag-one `0.90 → 0.94`; a sentence added saying the earlier figures were defective and what survives |
| §8 item 10 (`Predicting Δ_N`) | the `5x-1` caution's figures regenerated (`66`/`3.4` → `93`/`3.0`) |
| §8 item 11 (`the 5x-1 residue law`) | **RETRACTED** — the statement is false at `N = 2` |
| §10 (resources) | the `cross_map` entry now names the correction note |

No other section refers to the `5x-1` ladder. Proposition 7.6 (`5x-1`), the
shelter/pigeonhole table of §7(c), Theorem 7.2 and Remark 7.3 are **proofs**, not
scans, and are untouched.

## 13.3 The retraction, checked against the note's own words

The retracted item asked whether `r_min(N) ≡ 5 (mod 16)` for every `N`, labelled
**verified** at every `N ≤ 459`. It is false at `N = 2`: `5·13 − 1 = 64`, so
`S₁ = 6 ≥ 3` and `13` is rare-side persistent, so `r_min(2) = 13 ≡ 13 (mod 16)`.

Two things are worth recording because they bear on how the error survived review.

1. **The note's algebra was right and its data was wrong.** The same item states
   that "`S₁ ≥ 3` requires `m ≡ 5 (mod 8)`, which splits into `5` and `13` modulo
   16". That is exactly the correct sieve. The clause that followed — "the class
   `13` is admissible yet never least" — was not a measurement of the class 13; it
   was a restatement of the fact that the scan never looked at it. A **verified**
   label was attached to a scan whose population was narrower than the statement
   being tested, and the narrowing was visible in the same sentence.
2. **The refutation was already in the repository.**
   `audits/fingerprint_comparison/data/records_2x2.txt` holds a `5x-1` ladder to
   `X = 5·10^7` computed by a scanner that sieves nothing: 52 holders, beginning
   `5, 13, 21, 45, 77, …`. The `cross_map` ladder gave 35 on the same range,
   beginning `5, 21, 533, 789, …`. Two audits in this repository disagreed about
   the same map from `N = 2` onward and were never compared. The cross-check
   `cross_map` did claim against that file compared only the single deepest entry
   — which the sieve happens not to move. **A cross-check against another dataset
   has to compare the whole object, not its extreme.**
3. **The retraction does not weaken any other claim.** The residue question is
   returned to **open** with no empirical pattern behind it. What survives is the
   *proved* part, `S₁ ≥ 3 ⟹ m ≡ 5 (mod 8)`, and the *proved* observation that
   (L1) has no `q > 4` counterpart.

## 13.4 The `3x+1` claim was verified, not assumed

Two independent checks, both recorded in the correction note:

* the patched scanner, re-run over the **whole** `3x+1` range `[1, 2·10^11)` with
  the same 8-way chunking, reproduces **all eight** committed
  `data/scan_A_raw/part_*.txt` files **byte for byte**, with the overflow guard
  firing 0 times in every worker;
* `audits/pointwise_discovery`, whose scanner has **no sieve at all**, reproduces
  the published `3x+1` ladder entry for entry — 23 holders, deepest
  `r_min(282) = 12 235 060 455`.

## 13.5 Labels

The retracted item carries **verified** for the refutation and **open** for the
question. No new **proved (paper)**, **proved (lean)** or **cited** label was
introduced anywhere by this change. Remark 4.10 keeps its **verified** /
**heuristic** split, with the figures replaced.

## 13.6 Non-claims

The correction changes a control measurement and a retracted question. **It does
not touch (DE), Open Problem C, the Collatz conjecture, any Lean theorem, the
`3x+1` record data, or the `p_N` values** — the exact mass recursion was never
involved, and its published numbers are reproduced unchanged by the regenerated
`delta1_D.txt`.

## 13.7 The corrected figures, traced to source

| figure | in the note | source |
|---|---|---|
| `93` holders, depth `459`, `r_min(459) = 848 537 873 557` | Rem. 4.10, §8 item 10 | `audits/cross_map/data/delta1_D.txt` |
| `Δ₁ > 0` at `92` of `93`; the exception `N = 13`, `Δ₁ = −0.40` | Rem. 4.10 | same |
| OLS `+0.0224`, Theil–Sen `+0.0224`, CIs at blocks 3/8/16 | Rem. 4.10 | same |
| `n_eff = 3.0`, lag-one `0.94` | Rem. 4.10, §8 item 10 | same |
| `r_min(2) = 13`, reported as `21` | §8 item 11 | `audits/cross_map/data/delta1_D.txt`, and pinned as a literal in `scripts/test_sieve.py` |
| `66` of the `93` holders `≡ 13 (mod 16)` | §8 item 11 | `audits/cross_map/data/residues_D.txt` |
| `m ≡ 5 (mod 8)` at all `93` holders (the proved part) | §8 item 11 | same |

**A figure this note never carried, and now can.** The corrected `cross_map`
ladder restricted to `X = 5·10^7` reproduces, entry for entry, the 52 holders that
`audits/fingerprint_comparison` had already recorded with an unsieved scanner.

**What did not move.** The `p_N` column of `delta1_D.txt` is identical at every `N`
to the version it replaces — the mass recursion is independent of the scan — and
every `3x+1` figure in the note is untouched.

## 13.8 Build

`make` in `papers/synthesis`: **0 errors, 0 undefined references, 0 undefined
citations, 0 overfull boxes**, 22 pp.
