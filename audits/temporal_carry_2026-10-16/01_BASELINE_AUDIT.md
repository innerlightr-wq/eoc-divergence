# 01_BASELINE_AUDIT.md

## Repository state — recorded, not modified

| repo | branch | HEAD | origin/main | worktree |
|---|---|---|---|---|
| `eoc-divergence` | `main` | `938dcc0` | `b787dfa` | clean |
| `eoc-lean-verification` | `main` | `6057a0d` | `6057a0d` | clean |

`eoc-divergence` local `main` still carries the unpushed `938dcc0` while `origin/main` has
advanced to `b787dfa`; the October 14 audit directories live on the remote, not in this
worktree.  **A local HEAD is not the published state.**  Nothing was touched.

## Prior findings reconciled against their own scripts

### 1. First-difference position and the valuation of realizer differences — **ALREADY PROVED**

`~/scratch/eoc-growing-scale-pairs-2026-10-14-102831/ARITHMETIC_PROOF_ATTEMPT.md`,
**Theorem D**, verbatim:

> Fix the branch node: let `P` be the longest common prefix of `w, w'`, of length `j` and sum
> `S_j`, with first differing digits `e < e'` and `sigma = S_j + e`.  Then
> `dt = u_{w'} − u_w = beta + 2^{sigma}(2^{e'−e}c' − c)`, `v_2(beta) = sigma − 1`.

Status there: "**proved** … and verified on all `14 878` pairs at `N = 8` and all `461 280` at
`N = 10`, 0 violations (`tests/test_reduction.py`), `v_2(beta) = sigma − 1` exactly, also 0
violations."

### 2. The unresolved odd part — **the stated open point, and this brief's target**

Same document, §5, verbatim:

> "The valuation datum `v_2(beta) = sigma−1` is exactly the part of `dt` that the word data
> determine; **the odd part of `dt/2^{sigma−1}` is carried by `c, c'` and is not determined by
> any `(j,S)` information.**"

This is the precise prior claim the present investigation tests.  **It is about FREE suffixes**
(`c, c'` range over independent continuations), a distinction that turns out to be decisive
(`05_CANDIDATE_LEMMAS.md` §4, P9).

### 3. Aggregate pair mass and the power-law barrier — **ALREADY PROVED (obstruction)**

Theorem E of the same package: every bound derivable from the proved structure has the shape
`U_N(x) ≤ C N^B n_N (2x)^{1−c}`, with `c = 0` for three of the four sources and `c = I₀/a =
0.0500` for the fourth.  A recorded rigorous obstruction, not a target.

### 4. The height/confinement obstruction — **PROVED, October 16**

`~/scratch/h10-collatz-realizer-2026-10-16-205247/`, Lemma O: zero-confinement *is*
`2^{S_n} ≤ 3^n` while the generic height is `H = max(C_N, 3^N) ≥ 3^N`, so `2^{S_N}/H − 1 ≤ 0`
identically and `ρ_N ≥ 1`.  Any divisibility-to-size tool is vacuous on the confined sector.
**The present brief §7 correctly forbids repeating it without a new ingredient.**

### 5. Proposition R — **PROVED but ALREADY KNOWN**

Same package: with `S_n → ∞`, a word has a nonnegative-integer realizer iff `(r_n)` is
eventually constant.  It is the statement of the gap, not progress on it.

## Novelty boundary for this investigation

Anything derived below is new only if it is **not** a consequence of:
the aggregate identity (Rev 8 Lemma 2.4); the carry recurrence `C_{n+1} = 3C_n + 2^{S_n}`;
Theorem D's valuation datum; the §5.3 dichotomy; or Lemma O.  `05_CANDIDATE_LEMMAS.md` applies
this test to every candidate, and **none survives it** as more than a closed-form restatement.

## Proved versus computationally observed, in the inherited baseline

| | status |
|---|---|
| aggregate identity, carry recurrence | **PROVED**, formalized (Rev 8 §14) |
| Theorem D, `v_2(beta) = sigma − 1` | **PROVED** + exhaustively verified at `N = 8, 10` |
| "odd part not determined by `(j,S)`" | **PROVED for free suffixes**; silent on controlled ones |
| Theorem E power-law barrier | **PROVED** obstruction |
| Lemma O, `ρ_N ≥ 1` | **PROVED** |
| `(DE)`, `(PosPC)`, Sharp EOC, Open Problem C | **UNRESOLVED** |
