# Reproducibility

## Environment

- Python 3 (CPython), **standard library only** (`fractions`, `math`, `collections`). No
  `mpmath`/`numpy`/`matplotlib` (not installed; an early `mpmath` import failed and was replaced
  by stdlib — recorded in DEVIATIONS.md).
- Exact integer/rational arithmetic for every identity: confinement is the integer test
  `2^{S_j} ≤ 3^j`; `p_N` and all discrepancies are `Fraction`; floats appear only in reported
  logs, `z`-scores and exponents.
- Lean: **no build was run and no Lean file was added or edited.** Toolchains recorded
  (`eoc-divergence` `v4.34.0`; `eoc-lean-verification` `v4.34.0-rc1`) and unchanged. Lean claims
  in these documents are read off the sources and labeled LEAN VERIFIED only where the file
  states the theorem and the repo-wide `axiom|sorry|admit` count is 0 (checked: 0).

## Commands and expected outputs

```sh
cd ~/scratch/collatz-partial-counting-20260926-205246
python3 scripts/a1_independent_offset.py    # -> repro/a1.out
python3 scripts/a2a3a4.py                   # -> repro/a2a3a4.out
python3 scripts/phaseB_Q.py                 # -> repro/phaseB_Q.out       (~5 min)
python3 scripts/phaseC_decomp.py            # -> repro/phaseC.out         (~8 min)
```
plus two inline checks whose captured output is kept: `repro/constants.out` (constant audit),
`repro/a3_fixed.out` (joint-modulus correction), `repro/phaseC_exponents.out` (exponent budget).

Hardened repository scripts, in the worktree of branch `research/harden-missing-formula-audit`:
```sh
python3 audits/missing_formula_selection/per_cylinder_survival.py   # ~2 min
python3 audits/missing_formula_selection/shell_discrepancy.py       # ~12 min (now exhaustive)
```

| check | expected |
|---|---|
| `a1`: confined words `N=1..12` | 12,447; `K<1`: 0; word/parity mismatches: 0 |
| `a1`: cylinder cases | 3,241; failure-count mismatches **0**; predicted-class mismatches **0** |
| `a1`: edge-case census | all six non-empty (2437/617/187/2437/405/2504) |
| `a2`: full-word, exhaustive | 173 / 8,045 / 312,455 words at `N=8/12/16`, 0 mismatches; brute-force cross-check 0 mismatches for `N≤12` |
| `a3`: joint modulus `u·2^K` | max `|P(fail|class)−P(fail)| = 0` for `u=3,5,7,9` |
| `a3`: `2^K` only | `0, 0.875, 0.875, 0.25` for `u=3,5,7,9` (informative — the point) |
| `a4`: singleton shells | `#shell(s=N)=1` and `r_w=2^{N+1}−1` at `N=4,8,12,16,20` |
| `phaseB`: `Q` ladder | `1.008174, 0.994797, 1.000408, 1.000816, 0.999991` at `B=12,16,20,24,28`; direct cross-check exact for `B≤20` |
| `phaseC`: identity | `id ok = True` at all five `(B,N)`; total signed error `+211.5` at `B=24` |
| hardened `per_cylinder` | 311,844 cylinders; survival-formula failures 0; **predicted-offset disagreements 0**; retraction table 7/18/21/33 |
| hardened `shell_discrepancy` | forward-verified 8,045/8,045, 312,455/312,455, **13,472,296/13,472,296**; 0 word mismatches; exact-identity failures 0 |

## Ranges and populations

| item | population | status |
|---|---|---|
| A1 | all zero-confined words `N ≤ 12` × `B ∈ {6,8,10,12,14}` | complete enumeration |
| A2 | all zero-confined words `N ∈ {8,12,16}`; brute force `N ≤ 12` | complete enumeration |
| A3 | `w=(1)`, `M=15`; complete `u·2^K` and `2^K` periods, `N ≤ 8` | complete enumeration |
| A4 | singleton shells `N ∈ {4,…,20}`; κ table symbolic at `B=100` | complete / symbolic |
| Phase B | `B ∈ {12,16,20,24,28}`, `N = ⌈0.65B⌉` | complete; direct cross-check `B ≤ 20` |
| Phase C | same ladder; shell resolution at `B=24` | complete |
| `B ≥ 32` (`N ≥ 21`) | — | **untested**, exceeds the pre-registered budget |
| certified `η > 0` regime | — | **not reached**: no `B` in range separates `η=0` from `η>0` |

## Input hashes

```
PREREGISTRATION.md  md5 cdb0dbe19216917aa3d9c7e6c8f2ed5c   (unedited)
```
Repository bases: `eoc-divergence` `9a1748a5414b0d0ca6b4b2fff18153f3bf92f64f`;
`eoc-lean-verification` `14dea46ae5af816754cf3883475fa73dea598130`.
New commit: `b57b15243d440540c7e13e07e0be32ea512a4bb4` on
`research/harden-missing-formula-audit`.
