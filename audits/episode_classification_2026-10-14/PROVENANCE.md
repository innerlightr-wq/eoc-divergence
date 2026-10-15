# PROVENANCE.md

## 1. Repository states — recorded, not assumed

```
eoc-divergence         local HEAD  938dcc07045d168b8475ca22fc0d5fb469254582  main  clean
                       origin/main 46b3cf7e742380767bf5ba928949cdd2ff3ca715
eoc-lean-verification  local HEAD  6057a0d519566a32fc4153a8920e93f18d70b064  main  clean
                       origin/main 6057a0d519566a32fc4153a8920e93f18d70b064
```

The brief's leads (`938dcc0`, `6057a0d`) are the **local** states and are
current as such. `eoc-divergence`'s `origin/main` advanced to `46b3cf7` earlier
today when the October audit packages were published; the local checkout is still
at `938dcc0` and carries an unpushed commit. Both recorded; **neither repository
was modified, fetched into, or switched** in this round. Rev 8 was read with
`git show`, which does not touch the working tree.

## 2. The authoritative Revision 8

```
eoc-lean-verification, branch eoc-revision8 = b2dcae22dbefe8af89c83f00ebd038d6b21c0304
  paper/eoc_rev8.pdf   32 pp
    sha256 07c6610d633035e43b8a36905e0c58e517704ca12bb208e2340359dea30f294c
  paper/eoc_rev8.tex
    sha256 d495c8bba270e1cbd7846f1446f25c7a25b7b6b3b2bd7136ef6eb3a1b581320b
```

The `07c6610d` prefix matches the brief's lead. The similarly named
`~/Downloads/eoc_rev8.pdf` (prefix `998686d2`) is an **earlier draft** and was
**not** used; no substitution was made. Both copies are frozen read-only in
`sources/` with `sources/REV8_HASHES.txt`.

**Read firsthand this round:** Lemmas 2.2 and 2.4; §4 in full (Lemma 4.2,
Lemma 4.3, Theorem 4.4, Corollary 4.5, Remark 4.6, Theorem 4.7, Proposition 4.8,
Theorem 4.9, Proposition 4.10, Remark 4.11); §5.2 and Remarks 5.7–5.8 (the
unproved finite-defect claim and its withdrawn status); §6.1–6.2 (Definition 6.1,
Remark 6.2, Definition 6.3, Proposition 6.4); §7.1; §8 (Proposition 8.1,
Remark 8.2); §9.1 (Proposition 9.1); Open Problem F and §13
(Propositions 13.1–13.2, Remark 13.3). §§10–12, 14–17 were not re-read.

## 3. Prior workspaces — present and unmodified

| path | status | recovered |
|---|---|---|
| `audits/joint_episode_budget_2026-10-14/` | PRESENT, unmodified | the (DEPTH–DURATION) proposal that `D_L` refutes here; the carry/`z_n` dictionary; the Loeb benchmark |
| `audits/lopez_stoll_transfer_2026-10-14/` | PRESENT, unmodified | the `2^{R_n}` notation and the harmonic-packing constant; not re-audited |
| the Phase 6 return-gate round (local scratch, not published) | PRESENT, unmodified | Phase 6: the entry-gate `Θ(m_0/log m_0)` verdict, the mod-18 entry classes, and the open depth-`≈ℓ/10` dichotomy — which this round's `k/ℓ ≈ 0.45` measurement sits beside |

No percolation transfer, no López–Stoll 2021 re-audit, no RH work. Files modified
in any pre-existing package: **0** (checked).

A local search for prior fixed-run / fixed-turn / monotone-block / seed-cost
results found none beyond the above: the `v_2(m_0+1) − 1` ones-run fact appears in
the López–Stoll package as the `−1` warning control, and Phase 6's depth
dichotomy is the closest relative of §4's coverage measurement. Nothing matching
Theorem C or Theorem D was found locally.

## 4. Environment and numerical policy

```
Python 3.14.7, CPython standard library only.  No third-party package imported
or installed.  No Lean, no lake build.
```

Corridor membership is **always** `2^{S_n} ≤ 2^c · 3^n` on integers for integer
`c`. Carries use the closed form `C(D) = Σ_j 3^{t−1−j}2^{S_j}`; least realizers
use the exact congruence `3^t r + C ≡ 2^S (mod 2^{S+1})` with terminal oddness;
weighted sums are exact `Fraction`s. Floating point appears only in printed
diagnostics (`R_n`, `w_max`, `k/ℓ`, the `F(k)` coefficients) and never in a
decision about confinement, divisibility, or class membership.

## 5. Commands, runtimes, resources

One worker throughout, no parallelism, no subprocesses. `RLIMIT_AS` 4 GiB in
every script; `timeout` on every invocation; all runs from
`env -i PATH=/usr/bin:/bin HOME=$HOME`.

| script | runtime | peak RSS | result |
|---|---|---|---|
| `run_arithmetic.py` | ~60 s | 12.1 MiB | Lemmas A, B; Theorem C; 5 checks, **0 violations** |
| `two_run.py` | ~90 s | 11.8 MiB | `D_L` at 7 values of `L`; Theorem D on **60** triples; **0 failures** |
| `controls.py` | ~15 s | 11.7 MiB | Loeb classifier; controls A–E; **0 failures** |
| `coverage.py` | ~90 s | 16.4 MiB | 7301 episodes with `ℓ ≥ 10`; mean `k/ℓ = 0.4537` |
| `tests/regression.py` | ~60 s | — | the suite, clean process |

## 6. Errors made and corrected in this round

Recorded because three of these would have produced false statements, and because
the brief requires refuted formulations be preserved rather than silently changed.

1. **My `j = 1` sharpness panel compared Mersenne seeds against the `j = 1`
   bound** and reported three failures. Those seeds have `j > 1` (e.g.
   `2^{21}−1` has `j = 24`), so the test was mis-specified, not Theorem C.
   Corrected to report the actual `j` and, separately, the genuine `j = 1` prefix.
2. **My `D_L` check demanded `episodes = [(2,L+2)]`** and took `w_max`/`W_L` over
   all episodes, giving seven spurious failures. Time zero counts (Rev 8
   Def. 6.1), so `[0,1)` is a genuine initial episode and the prediction concerns
   the later one. Corrected; `D_L` then matches every predicted item exactly.
3. **My brute-force test for Theorem D omitted the trailing `d ≥ 2` maximality
   test**, so seeds whose second ones-run is *longer* than `v` passed spuriously
   — e.g. `x = 27` for `(u,q,v) = (1,2,1)`, whose second run is actually `v = 4`.
   28 reported failures, all spurious. Corrected; 60/60 then agree with brute
   force.
4. **The brief's candidate `F(k) = O((k+1)α^{k+1})` is an overestimate**;
   derived here as `Θ(α^{⌈(k+1)/2⌉})`. Recorded as a correction to the candidate,
   not as a new theorem.
