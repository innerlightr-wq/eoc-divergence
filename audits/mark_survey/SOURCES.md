# Sources — mark survey

Local copies of PDFs and their `pdftotext -layout` extractions live in
`sources/` and are **not tracked** (repo-wide `.gitignore`: `**/sources/*.pdf`,
`**/sources/*.txt`). Originals in `~/Downloads` were copied, never moved or
modified. Line references in the phase-1 notes are to the page numbers of the
PDF, which the extraction preserves.

## Author's own work

### S1. Shared quarter-gamma lattice and the limits of the Thales–Ramanujan analogy
- Author: Elias De Jesús (ORCID 0009-0007-0190-9143)
- Date on paper: June 2026; PDF produced 2026-06-12 (pdfTeX 1.40.27), 8 pp.
- Local file: `~/Downloads/QuarterGammaRamanujan (1).pdf`
  → `sources/QuarterGammaRamanujan.pdf` (untracked)
- Companion repository: https://github.com/innerlightr-wq/thales-ramanujan-quarter-gamma
  (read at commit `14242bc`, local clone `~/GitHub/thales-ramanujan-quarter-gamma`)
- Zenodo, as recorded in that repository's README:
  concept DOI 10.5281/zenodo.20665588; version DOI reproduced by the code
  10.5281/zenodo.20672985
- **Title discrepancy (recorded, not resolved):** the repository cites the note as
  *"Ramanujan's Formula for 1/π and the Thales Integral Witness"*, while the PDF
  read here is titled *"Shared quarter-gamma lattice and the limits of the
  Thales–Ramanujan analogy"*. The section/identity numbering matches the
  repository's manuscript-to-check map (`docs/zenodo_record.md`), so these are
  taken to be the same work under a revised title. The PDF carries no DOI line.
- Contains no Lean; verification is Python (SymPy + mpmath, 34 checks R1–R8).

---

## The rest of the reading set

All files below are the author's own technical notes, copied read-only from `~/Downloads` into
`sources/` (untracked). Column "PDF" gives the local tag; "produced" is the PDF creation date from
`pdfinfo`, which is not always the date on the paper.

| tag | title (as on the PDF) | date on paper | pp | produced | original filename in `~/Downloads` |
|---|---|---|---|---|---|
| A01 | Local Algebraicity and Graded Global Periods on the Thales Partition Manifold, Revision 2 | Jul 2026 | 15 | 2026-07-24 | `ThalesPart_rev2.pdf` |
| A02 | Structural Layers of the Thales Semicircle | May 2026 | 10 | 2026-05-18 | `SkeletonsThalesSemicircle (1).pdf` |
| A03 | Parity-Complementary Mollifier Operators on the Thales Partition Manifold | Apr 2026 | 13 | 2026-04-18 | `MollifierOperators.pdf` |
| A04 | `√π` as a Dimensional-Reduction and Transition-Normalization Constant | Apr 2026 | 21 | 2026-05-28 | `DimensionalReduction (1).pdf` |
| A05 | Boundary and Interior Record Chronologies for the Two-Mode Oscillator Spectrum | Aug 2026 | 16 | 2026-08-04 | `oscillatorRecords (1).pdf` |
| A06 | Strain–Vorticity Interaction and Rotational Coherence (RVP, interaction-response revision) | Sep 2026 | 15 | 2026-09-09 | `RVP (1).pdf` |
| A08 | Two Complementary Periods, Modular Self-Duality, and a Beat Frequency on the Thales–Legendre Partition | Jun 2026 | 8 | 2026-06-13 | `ThalesBeat.pdf` |
| A09 | Archimedean Compensation on the Thales Semicircle, Revision 3 | Feb 2026 | 22 | 2026-02-13 | `Archimedean_Compensationv1 (1).pdf` |
| A10 | The Partition-Intrinsic Cubic and the Limits of Operator-Balance Embeddings in Perturbative GR | Aug 2026 | 17 | 2026-08-31 | `OperatorIntrinsicCubic.pdf` |
| A11 | From Cubic Transition Hypotheses to Transversal Constraint Geometry | Aug 2026 | 23 | 2026-08-31 | `IntrinsicCubic_ver (2) (2).pdf` |
| A12 | The Dual Diagonal and Reconstruction of Orthogonal Hyperrectangles | 2026 | 10 | 2026-04-17 | `AggregatedScalars.pdf` |
| A13 | The Minkowski Interval as a Thales Coupling Diagnostic | Apr 2026 | 16 | 2026-05-02 | `MinkowskiInterval (2).pdf` |
| A14 | Spectral Coupling and Structure-Dependent Relaxation in First-Order Consensus Networks, Rev. 2 | Aug 2026 | 6 | 2026-08-05 | `spectralConvergence.pdf` |
| A15 | The Compactness Partition on the Period Dial, Version 2 | Aug 2026 | 11 | 2026-08-04 | `period_dial_addendum_v2.pdf` |
| A16 | Compactness as a Thermodynamic Saturation Coordinate, Version 2 | May 2026 | 18 | 2026-05-27 | `CompactnessThermodynamicSaturation (6).pdf` |
| B01 | A Global Occupation Conjecture for the Accelerated 3x+1 Map, Revision 7 | 2026 | 31 | 2026-09-22 | `eoc_rev7.pdf` |
| B02 | Transport Deficits and 2-Adic Survival Budgets in Accelerated Collatz Words | Aug 2026 | 26 | 2026-08-12 | `transportDeficits (1) (4).pdf` |
| B03 | Conditional Obstructions and Launch Renormalization in Accelerated Collatz Dynamics | Aug 2026 | 20 | 2026-08-14 | `launchRenormalization (2).pdf` |
| B04 | Three Scales of Confinement in Accelerated Collatz Words, second revision | Sep 2026 | 28 | 2026-09-08 | `ScalesConfinement (1) (2).pdf` |
| B05 | Inheritance-Preserving Differentiation in the Collatz Survivor Tower | Jul 2026 | 32 | 2026-07-06 | `Inheritance_differentiation (4) (1).pdf` |
| B06 | Pointwise Survivor Discrepancy in a Width-Two Collatz System | — | 16 | 2026-07-12 | `halfcylinderv2 (1).pdf` |
| B07 | Representation Sufficiency and Licensed Inference | Aug 2026 | 18 | 2026-08-12 | `representation_sufficiency_audit (1).pdf` |
| C01 | A Bit Analyzer for the Collatz Carry Equation | Jun 2026 | 6 | 2026-06-05 | `BitAnalyzerCollatzCarryEquation (1).pdf` |
| C02 | The Positive-Entropy 2-Adic Carry Law | Jun 2026 | 11 | 2026-06-08 | `PositiveEntropy2Adic.pdf` |
| C03 | Tail-Tracking and the Leading-Block Principle in the Collatz Carry Equation | Jun 2026 | 6 | 2026-06-05 | `TailTrackingLeadingBlockPrinciple.pdf` |
| C04 | Finite-Field Zero Sums in the Collatz Carry Equation | Jun 2026 | 4 | 2026-06-05 | `FiniteFieldZeroSums.pdf` |
| D01 | A Sturmian Complexity Clock in Accelerated Collatz Words (revised) | Aug 2026 | 26 | 2026-08-25 | `SturmianClock (3) (2).pdf` |
| D02 | Boundary-Driven Renewal Structure in a Sturmian-Modulated Confined-Word Process | Aug 2026 | 16 | 2026-08-10 | `SturmianBound.pdf` |

All are by Elias De Jesús, Independent Researcher, ORCID 0009-0007-0190-9143. Where a note carries a
Zenodo DOI in its own reference list it is cited there; this survey did not re-resolve those DOIs.

**Group C sampling.** Group C in `~/Downloads` holds 29 distinct notes of one family (the Collatz
carry equation / Sturmian tower). Four were read, chosen for structural distinctness: C01 and C03
(the bit-depth diagnostic and its non-adjacent generalization), C02 (the residue law), C04 (the
odd-prime layer). The screen outcome for all four is the same — S1, word-level — and the shared
diagnostic `ℓ(D) = v₂(Q(D)+Ξ_α)` is common to the family, so the sample is reported as
representative of the family's candidate content and **not** as a census of it.

**Group E** (third-party Collatz literature in `~/Downloads`: an arXiv Syracuse preprint,
`2101.12747v1`, `2609.06358v1`, `j13.pdf`, `paper-B1E2b-new.pdf`, `ls09.txt`) was not read for this
survey. Where external results are invoked, they are invoked through the repository's own citations
in `papers/synthesis/refs.bib` and the two existing audit reports.

**Repository sources consulted** (tracked, not copied): `papers/synthesis/main.tex`,
`docs/PROGRAMME_ENDPOINT.md`, `docs/EQUIVALENT_FORMS_OF_DE.md`,
`audits/record_holder_anatomy/REPORT.md`, `audits/sturmian_irrationality/REPORT.md`.

**Companion repository consulted**: `thales-ramanujan-quarter-gamma`, local clone at commit
`14242bc` — `README.md`, `docs/mathematical_scope.md`, `docs/scope_and_nonclaims.md`,
`thales_ramanujan/checks.py`.
