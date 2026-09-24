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
