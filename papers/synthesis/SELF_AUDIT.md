# Checkpoint 2 — self-audit of `main.tex`

Draft: `papers/synthesis/main.tex`, **14 pp.**, compiles with **0 errors, 0 undefined
references, 0 undefined citations, 0 font warnings**, 2 overfull boxes (both minor).
Title A, as approved.

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
