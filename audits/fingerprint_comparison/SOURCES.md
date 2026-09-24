# Sources — fingerprint comparison

Local copies of PDFs and their text extractions live in `sources/` and are **not tracked**
(repo-wide `.gitignore`: `**/sources/*.pdf`, `**/sources/*.txt`). Originals in `~/Downloads` were
copied, never moved or modified.

## The author's own notes

| tag | title | date | local file |
|---|---|---|---|
| NULLS | *Two Normalization Nulls and the Tests That Tell Them Apart — a decision procedure for separating real structure from aggregation and selection mirages* | June 2026 (CC BY 4.0) | `~/Downloads/two_normalization_nulls.pdf` → `sources/two_normalization_nulls.pdf` (untracked) |

Elias De Jesús, Independent Researcher, ORCID 0009-0007-0190-9143. The note's decision procedure —
identify the generating operation, apply the matching scale knob (`n` for aggregation, `w` for
selection), and only then look in the CLT-free channels — is the classification scheme used
throughout `REPORT.md`. Its references [1]–[5] were not re-resolved for this study.

## Repository sources consulted (tracked, not copied)

- `papers/synthesis/main.tex` — the aggregate identity, the valuation-mean classification, the
  cycle-drift theorem, the signed marker, Prop. `prop:density` (the `−3.28 ± 0.05` constant), and
  the sign obstruction (Thm. 7.2).
- `docs/PROGRAMME_ENDPOINT.md`, `docs/EQUIVALENT_FORMS_OF_DE.md`.
- `audits/record_holder_anatomy/REPORT.md` — the published A-ladder, used as the cross-check in §5.

## External results cited

- Terras (1976) and Everett (1977), the parity/valuation residue correspondence for `3x+1`; the
  general odd-`(q,r)` form used here is proved in `PHASE0.md` F3 rather than quoted.
- `Divergence.cycle_drift`, `Occupation.confined_mass_rate` — machine-checked in this repository.

## Reproduction

```
cd audits/fingerprint_comparison/scripts
gcc -O3 -o orbits  orbits.c  -lm
gcc -O3 -o records records.c
gcc -O3 -o records2 records2.c
python3 phase0_verify.py          # exact verification of F1, F2, F3
python3 o1_drift.py               # O1, exact Haar moments and Edgeworth table
python3 o2_confine.py             # O2, exact transfer recursion to N = 500
python3 cycles.py                 # the cycle table of section 6
python3 o5_lil.py                 # O5, LIL envelopes            (seed 20260924)
python3 controls.py               # shuffles and exact least realizers (seed 20260924)
python3 attribution.py            # the Q2/Q3 attribution table
./orbits  <A|B|C> <capture|letters> <X> <budget>
./records <A|B|C> <X>
./records2 <q> <+1|-1> <lower|upper> <X>
```

Random seeds are fixed (`20260924`); everything else is deterministic and exact. Outputs as reported
are in `data/`.
