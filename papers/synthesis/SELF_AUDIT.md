# Checkpoint 2 — self-audit of `main.tex`

Draft: `papers/synthesis/main.tex`, **15 pp.**, compiles with **0 errors, 0 undefined
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

**One thing for you to confirm, since only you can.** The declaration's first sentence says AI
assistance was used *"throughout the programme"*. That is supported for the audits, the
computations, the literature work and this note. I have **no** evidence either way about the
Lean library development, and the repositories' own status files do not mention it. If AI was
not used there, narrow the first sentence to name the parts it covers.

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
