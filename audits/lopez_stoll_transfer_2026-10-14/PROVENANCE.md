# PROVENANCE.md

## 1. Repositories — read only, verified unmodified

```
eoc-divergence            938dcc0  main  dirty+untracked 0
eoc-lean-verification     6057a0d  main  dirty+untracked 0
collatz-symbolic-periodicity 38fb58f main dirty+untracked 0
periodicity-conjecture-bridge edb9ed4 main dirty+untracked 0
```

Checked at the start and the end of the session. **No commit, push, deposit,
manuscript edit, branch switch, reset, stash, toolchain change or global
install.** No file in any checkout was written; no scratch clone was needed
because every repository was already present locally and was read in place.

**`number-theory` is ABSENT** from `~/GitHub/` (the directory does not exist).
Recorded rather than silently skipped; nothing in this investigation needed it —
the divergence target, the rate, the carry and the realizer congruence all live
in the two EOC repositories, and the Sturmian/periodicity material is in
`collatz-symbolic-periodicity` and `periodicity-conjecture-bridge`.

Prior scratch packages named in the brief — all **present** and **unmodified**:
`eoc-divergence-amplification-2026-10-14-135712`,
`eoc-growing-scale-pairs-2026-10-14-102831`,
`eoc-mac-linux-reconciliation-2026-10-14-094228`.

## 2. The two López–Stoll sources

```
[2009]  INTEGERS 9 (2009), 141-162, #A13.  DOI 10.1515/INTEG.2009.014.  REFEREED.
        ~/Downloads/j13.pdf   22 pp   610903 bytes
        sha256 e6901bbe7b84af724575afd8d1b21674df3ced39c70f8c2aef6ac312d5dedf0b
[2021]  arXiv:2101.12747v1 [math.NT], 29 Jan 2021.  PREPRINT, v1, no journal ref.
        ~/Downloads/2101.12747v1.pdf   51 pp   3711557 bytes
        sha256 e4c5bccec262d8fdb001d7970dee56c347c03d789796c165e79a18dc2d584b9a
```

Located by title, not by filename. Text extracted read-only with
`pdftotext -layout` to `sources/LS2009.txt`, `sources/LS2021.txt`; **neither PDF
was modified, moved or re-saved.**

**Read firsthand:** [2009] abstract, §1, Theorem 1, Corollary 2, and the §4
devil's-staircase statements (Lemmas 23, 25, 27, Definitions 26, 28). [2021]
abstract, §1 including eqs. (11)–(16) and Theorem 1, the §5 lemma statements,
**§6 in full** (Lemmas 19–26 and the proof of Theorem 1), Lemmas 39–40.
**Not read:** [2021] §§7–9 beyond their statements, and the 3-adic material.
Recorded because the audit's conclusion rests only on §1 and §6.

**Not read in this session, and labelled source-reported throughout:**
Monks–Yazinski (2004) Theorem 2.7 b; Lagarias Relation 2.31; García–Tal (1999);
Curry (2026). The last two are quoted from
`eoc-lean-verification/README.md`, which itself flags them as manuscript-level
and not Lean theorems.

## 3. Repository files read

| file | used for |
|---|---|
| `eoc-divergence/Occupation/Compositions.lean` | `Confined`, `psum`, `confWords`, `p` (l. 217) |
| `eoc-divergence/Occupation/Rate.lean` | `alpha`, `I₀` (ll. 32–35), `sN`, `tt`, `le_p`, `p_le`, `confined_mass_rate` (l. 478) |
| `eoc-divergence/scripts/OccupationAxioms.lean` | exists to print the axioms of `confined_mass_rate`; **not executed** |
| `eoc-lean-verification/EOC/Realizer.lean` | `realizerCongruence` (286), `leastRealizer_unique` (478), `residue_pinning` (543) |
| `eoc-lean-verification/EOC/BoundedDrift.lean` | Cases A/B, realizer escape |
| `eoc-lean-verification/EOC/FinitePrefixPacking.lean` | finite-prefix drift-depth bound, `coprime_six_packing` |
| `eoc-lean-verification/EOC/HarmonicPacking.lean` | `sum_inv_orbit_le`, `carryU`, `carryE` |
| `eoc-lean-verification/EOC/HarmonicFloor.lean` | `R_le_of_nondescent_harmonic` |
| `eoc-lean-verification/EOC/LogCorridor.lean` | `logFloor_window_bound'`, `exits_logCorridor`, the `8/9` and `1/β* = 1.0358567` thresholds |
| `eoc-lean-verification/README.md` §Literature | García–Tal / Curry statements |
| `eoc-lean-verification/scratch/center_audit_2026-09-14/REPORT.md` | the measured drift `+0.4149 ≈ 2−α` |

## 4. Environment

```
Python 3.14.7, CPython standard library only.
third-party: NONE imported, NONE installed.  mpmath/numpy/sympy/scipy MISSING.
```

No global dependency installed or upgraded. No Lean toolchain invoked.

## 5. Numerical policy

Confinement is **always** the integer comparison `2^{S_j} ≤ 2^c·3^j`;
`sN(N) = (3**N).bit_length() − 1`, the repository's own `Nat.log 2 (3^N)`;
carries, realizer residues and the `Φ_R` partial sums are exact `int`/`Fraction`.
Floating point appears only in printed diagnostics (`Δ_N`, ratios, `J`, `κ`) and
never in a decision that a word is confined or that a congruence holds.

## 6. Commands, results, resources

| script | runtime | peak RSS | result |
|---|---|---|---|
| `phi_identity.py` | ~5 s | < 60 MiB | master identity, `l = 0..60`, 9 seeds — **0 violations** |
| `carry_bridge.py` | ~20 s | < 90 MiB | four carry identities, `N = 1..40`, 8 seeds — **0 violations**; three expressions for `Σ2^{−Δ_i}` agree to all digits |
| `return_count.py` | ~15 s | < 80 MiB | Theorem R on 9 seeds — **0 violations**; control past injective depth **fails** (1.29e7 vs 288), confirming the hypothesis is load-bearing |
| `theorem_s.py` | ~8 s | < 70 MiB | Theorem S, 14 rows — **0 violations**; explicit caps `N_max` |
| `counterexamples.py` | ~25 s | < 120 MiB | W1–W4 all exactly 0-confined; two-clock identity exact on all four |
| `realizability.py` | ~3 s | < 60 MiB | X1 **0 violations** after the off-by-one correction; X2 **0 violations** |
| `clocks_and_rate.py` | ~4 min | < 280 MiB | Lean sandwich `N = 4..96` **0 violations**; `J(s)` at 7 values, `N ≤ 1000`, monotone convergence |

One worker throughout; no parallelism, no subprocesses, no nested workers. Well
inside the brief's limit of four workers and `min(4 GiB, 25 % of RAM)`.

## 7. Errors made and corrected in this session

Recorded because the brief asks for failed steps, and because two of these would
have produced false statements.

1. **First `D`-but-not-`E` witness was not confined** (`min Δ = −443.53`): the
   `d = 2` descent runs overshot. Rebuilt with an exact per-step confinement
   guard; the corrected W2 has `min Δ = 0.0090`.
2. **X1 stated as `v₂(m₀+1)`, off by one.** The exact check failed on all 15
   seeds; the derivation gives `v₂(m₀+1) − 1`, and the statement was corrected,
   not the test.
3. **`κ = −J′(α)` quoted as `1.3195`, wrong by a factor of 3.** Corrected to
   `0.438032659` via the closed form `J(s) = s − s log₂s + (s−1)log₂(s−1)`,
   `J′(s) = 1 + log₂((s−1)/s)`, cross-checked against difference quotients and
   against `J(α) = I₀` to 12 digits.
4. **A first version of Theorem S used `liminf Δ_N/N = 0`** as its hypothesis —
   withdrawn as circular (its only source was the preprint that fails audit) and
   as insufficient (`2^{o(N)}` swamps `N^{1/9}`).
