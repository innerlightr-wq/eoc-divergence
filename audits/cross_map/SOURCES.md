# Sources — cross-map study

No third-party PDFs were copied for this audit; nothing is untracked under `sources/`.

## Repository sources consulted (tracked)

- `papers/synthesis/main.tex` — the aggregate identity, `cycle_drift`, the signed marker, the sign
  obstruction (Thm. 7.2), Criterion 7.1, the density and clustering propositions.
- `docs/PROGRAMME_ENDPOINT.md`, `docs/EQUIVALENT_FORMS_OF_DE.md`.
- `audits/record_holder_anatomy/REPORT.md` — the published `A` ladder, `Δ₁` range, growth exponent
  and `n_eff`, all reproduced independently here as the control in item 3.
- `audits/sturmian_irrationality/REPORT.md` — the depth law, the valuation law's re-derivation, and
  the `q = 3` depths 10, 83, 568, reproduced here in item 6.
- `audits/fingerprint_comparison/` — Phase 0 F1 (letters i.i.d. geometric for every odd `q`, `r`)
  and §6 (the sign-alignment criterion).

## Lean results cited

`Divergence.aggregate_identity`, `Divergence.divergent_iff_zeroConfined`, `Divergence.cycle_drift`,
`Occupation.confined_mass_rate`, `Descent.ResidueLaw` (L4) — machine-checked in this repository.

## External, cited from a web search and **not verified in this session**

- S. Volkov, a probabilistic model for the `5x+1` problem (2006).
- A. Kontorovich and J. C. Lagarias, *Stochastic Models for the `3x+1` and `5x+1` Problems*,
  [arXiv:0910.1944](https://arxiv.org/abs/0910.1944) — models predicting that almost all `5x+1`
  orbits diverge, and the empirical exponent `α ≈ 0.68`.
- J. C. Lagarias, *The `3x+1` Problem: An Annotated Bibliography*,
  [arXiv:math/0608208](https://arxiv.org/pdf/math/0608208).

These concern `5x+1`; no corresponding treatment of `5x−1` was located.

## Reproduction

```
cd audits/cross_map/scripts
gcc -O3 -o scan_rare scan_rare.c
python3 criterion.py                      # the sign-alignment table, all seven maps
python3 rates.py                          # item 2: I(q) and the exact transfer recursion
python3 check_words.py                    # the recursion validated against DFS enumeration
python3 check_mass.py                     # Terras-Everett count check (lower side is exact)
python3 markers.py                        # item 4: signed marker, all four maps
python3 descent.py                        # item 5: L1 direction and the L2 chain identity
python3 sturmian.py                       # item 6: the depth law for q = 3, 5, 7
./run_scan_D.sh                           # D ladder, every odd m < 10^12, 8 workers (~20 min)
./run_scan_A.sh                           # A control ladder, m < 2*10^11
python3 delta1.py 5 upper ../data/scan_D_raw/part_*.txt
python3 delta1.py 3 lower ../data/scan_A_raw/part_*.txt
python3 residues.py "D = 5x-1, upper side" ../data/scan_D_raw/part_*.txt
```

Random seed fixed at `20260924` (used only by the bootstrap). Everything else is deterministic and
exact. Outputs as reported are in `data/`; the per-worker scan shards are in `data/scan_*_raw/`.
