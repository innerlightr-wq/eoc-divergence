# PROVENANCE.md

## 1. Repositories — read only, unmodified

```
eoc-divergence          938dcc0   branch main   dirty+untracked 0
eoc-lean-verification   6057a0d   branch main   dirty+untracked 0
```

Verified at the start and the end of the session (`git -C … rev-parse HEAD`,
`git -C … status --porcelain --untracked-files=all | wc -l`). **No commit, push,
publication, deposit, branch switch, reset, stash, README edit, toolchain
change or global install.** No file in either checkout was written. No scratch
clone was needed, because both repositories were already present locally and
were read in place without modification.

`number-theory` was listed in the brief but is **not present** under
`~/GitHub/`; the directories there are
`collatz-symbolic-periodicity`, `eoc-divergence`, `eoc-lean-verification`,
`eoc-main-integration`, `periodicity-conjecture-bridge`, … and no
`number-theory`. Nothing in this investigation needed it: the divergence target,
the rate, and the realizer congruence all live in the two repositories above.
Reported rather than silently skipped.

## 2. Files read (not copied, not altered)

| file | role |
|---|---|
| `eoc-divergence/Occupation/Compositions.lean` | `Confined`, `comps`, `confComps`, `confWords`, `psum`, `p` (l. 217) |
| `eoc-divergence/Occupation/Rate.lean` | `alpha`, `I₀` (ll. 32–35), `sN`, `tt`, `le_p`, `p_le`, `rate_core`, `confined_mass_rate` (l. 478) |
| `eoc-divergence/scripts/OccupationAxioms.lean` | exists to print the axioms of `confined_mass_rate`; **not executed here** |
| `eoc-lean-verification/EOC/Realizer.lean` | `realizerCongruence` (l. 286), `leastRealizer_unique` (l. 478), `residue_pinning` (l. 543), `coarseAnchor`, `leastRealizer` |
| `eoc-lean-verification/scratch/center_audit_2026-09-14/REPORT.md` | §4.2 measured one-step drift `+0.4149 ≈ 2 - alpha` |
| `the growing-scale-pairs round (local scratch, not published){ARITHMETIC_PROOF_ATTEMPT,VERDICT}.md` | Theorem D (§5), Theorem C′, Theorem E; the conditional chain and its exponent `0.8321405567` |

The three prior scratch packages
(`eoc-pair-correlation-2026-10-14-074710`,
`eoc-mac-linux-reconciliation-2026-10-14-094228`,
`eoc-growing-scale-pairs-2026-10-14-102831`) were read and **not modified**.

## 3. The percolation paper

```
Nonuniqueness of percolation on nonamenable quasi-transitive graphs
OpenAI, September 24, 2026.  53 pages, A4, PDF 1.7, pdfTeX-1.40.29.
path    ~/Downloads/paper.pdf     (located by title: the filename carries no hint)
size    649525 bytes
sha256  46a78d044d2713e48cb3faa9b0b9d22da9480193e2202fe63d8e0daa7d8a3dbb
```

Version identification: the title page carries the date **September 24, 2026**,
matching the brief; `pdfinfo` reports Title "Nonuniqueness of percolation on
nonamenable quasi-transitive graphs", Author "OpenAI", Subject "The
bond-percolation nonuniqueness conjecture of Benjamini and Schramm". No arXiv
identifier, version string or DOI appears in the file. Text extracted read-only
to `sources/paper.txt` (`pdftotext -layout`); **the PDF itself was not modified,
moved or re-saved.**

Read firsthand: §4.1–4.5 in full (Def. 4.2, Prop. 4.3, Lemmas 4.1, 4.4–4.9),
§1.2, §2.2–2.5, and the opening statements of §§5–9. Sections 6–9 were read at
the level of their statements and the role they play, not line by line; this is
recorded because the brief asked for §§7–9 and the deeper spectral-deformation
arguments were **not** audited in detail — they were not needed, since the
transfer fails at §4.

## 4. Environment

```
Python 3.14.7   CPython standard library only
third-party: NONE imported, NONE installed
  mpmath MISSING   numpy MISSING   sympy MISSING   scipy MISSING
```

No global dependency was installed or upgraded. Every script imports only
`math`, `fractions`, `os`, `sys`.

## 5. Numerical policy

**Every confinement decision is the integer comparison
`2^{S_j} <= 2^c · 3^j` on Python integers**, the integral form of
`Occupation.Confined`. `sN(N)` is computed as `(3**N).bit_length() - 1`, the
repository's own `Nat.log 2 (3^N)`. The dyadic masses `p(N,c)` are exact
`Fraction`s. Floating point appears **only** in printed diagnostics
(`log_2` of an already-exact rational, and the rate functions `J`, `H_2`), never
in a decision that a word is or is not confined.

## 6. Commands and results

| command | runtime | peak RSS | result |
|---|---|---|---|
| `scripts/mass.py` | ~3 min | < 200 MiB | counts and masses, `N <= 200`; `log_2 n_N/N = 1.4481` and `-log_2 p/N = 0.1206` at `N = 200` (vs `g = 1.5056`, `I_0 = 0.0793`, gap = the `O(log N/N)` prefactor) |
| `scripts/rate_checks.py` | ~12 min | < 300 MiB | sandwich **0 violations** (12 depths); walk identity **0 mismatches** (27 pairs); drifting rate converging to `J(alpha+theta)` in all 8 columns |
| `scripts/bridge.py` | ~6 min | < 200 MiB | Theorem B **0 violations** `N = 1..14`; multiplicity max fibre **`= 1`**, **0 violations** |
| `scripts/recombine.py` | ~2 min | < 200 MiB | down-shift survival **exactly `1.0000`**, `N = 3..12`; up-shift `0.40–0.69`, defect `1..6` |
| `scripts/fibres.py` | ~3 min | < 200 MiB | `delta_N` plateau identified as an artifact; max fibres `27, 40, 55` at `N = 10,12,14` |
| `scripts/check_thm4.py` | ~1 min | < 200 MiB | Theorem 4's bound holds and is tight to `11%` (`32.2, 45.6, 61.4` vs `27, 40, 55`); the position-`j`-only relaxation is exactly attained, argmax `(1,…,1)` at every depth |
| `scripts/placement.py` | ~4 min | < 200 MiB | `W(N,X)/fair ∈ [0.9837, 1.0000]`, `N = 1..24`, all odd `m < 2^17` |
| `scripts/tail_ratio.py` | ~1 s | < 100 MiB | record depths `1,3,36,50,65,84,108` by direct iteration; `rho/r_min` peaks at `17.3414`, drops below `1` at each transition |

Logs in [`results/`](results/). One worker throughout; no parallelism, no
subprocesses, no nested workers. Well inside the brief's limits of four workers
and `min(4 GiB, 25% of RAM)`; the largest object built is a dictionary of
`O(N · alpha N)` exact integers, and the brute-force scans are over at most
`2^22` residues.

## 7. What was not done

* **No Lean compilation.** No `lake build`, no `lake exe cache get`, no
  toolchain invocation. `confined_mass_rate` is labelled **source-backed**
  everywhere in this package and **never** "Lean-verified here".
* **No exhaustive search beyond validated ranges.** The brute-force residue
  scans stop at `N = 14` (`Q_14 = 8388608`) and the initial-window scan at
  `2^17`, because each exists to validate an identity or refute a proposal, not
  to look for patterns.
* **No large pair enumeration.** The `O(n_N^2)` pair sums of the previous round
  were *not* recomputed; their results were recovered from that package.
* **§§6–9 of the percolation paper** were read at statement level only (§3).
