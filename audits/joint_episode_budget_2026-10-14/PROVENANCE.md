# PROVENANCE.md

## 1. The manuscript — identity resolved, and a discrepancy recorded

The brief names *"A Global Occupation Conjecture for the Accelerated 3x + 1 Map:
Residue–Time Duality, Divergent-Orbit Sparsity, and the Pointwise Realizer
Problem"*, Revision 8. **There is no Revision 8 PDF in `~/Downloads` under an
obvious name, and none in `eoc-divergence` (which carries `docs/eoc_rev7.pdf`).**
It was located instead on a branch of the Lean repository:

```
eoc-lean-verification, branch eoc-revision8 = b2dcae22dbefe8af89c83f00ebd038d6b21c0304
   paper/eoc_rev8.pdf   32 pp   sha256 07c6610d633035e43b8a36905e0c58e517704ca12bb208e2340359dea30f294c
   paper/eoc_rev8.tex           sha256 d495c8bba270e1cbd7846f1446f25c7a25b7b6b3b2bd7136ef6eb3a1b581320b
   paper/revision8/CHANGES.md   (hunks H1-H20, Revision 7 -> 8)
```

**Discrepancy, recorded rather than resolved silently.** `~/Downloads` also holds
`eoc_rev8.pdf` (sha256 `998686d2…`) and `eoc_rev8.tex` (sha256 `30483cac…`),
dated 2026-10-04 14:53, and **both differ from the branch copies** (68 diff
lines). The Downloads copy is an **earlier draft of Rev 8**: it lacks the episode
decomposition `15+4+6+64+1+5+3=98`, the sentence *"83 of the 98 occupation times
are separated returns"*, the sharpening into Open Problem F, and the certified
`§15` maximum. **The branch copy (`b2dcae2`) is therefore the authoritative
Revision 8 and is the one used throughout.** Both are hashed in
`sources/MANUSCRIPT_HASHES.txt`; the branch `.tex`/`.pdf` and the Downloads
`.tex` are frozen read-only in `sources/`, and the repository was not modified
(`git show` only).

Dependencies read firsthand from the branch PDF: Lemma 2.2 (Eliahou–Rozier),
Lemma 2.4 (aggregate), Remark 2.3 (the two quantities called `E`),
Definition 6.1 and Remark 6.2 (lifetime / occupation / drift exit, the
full-forward-orbit convention, Loeb's example and the `97 → 98` correction),
Definition 6.3 and Proposition 6.4, Definition 6.13 and Theorem 6.14,
Theorem 7.1, §7.1, Open Problem F, Propositions 13.1 and 13.2, Remark 13.3.
§8 (self-financing) and §9.2 (coordinate-collapse ledger) were read at the level
of their statements and the role they play; §§8–9 were not re-derived.

## 2. Repositories — read only, verified unmodified

```
eoc-divergence         HEAD = 938dcc07045d168b8475ca22fc0d5fb469254582  main  dirty+untracked 0
eoc-lean-verification  HEAD = 6057a0d519566a32fc4153a8920e93f18d70b064  main  dirty+untracked 0
```

Verified at the start and the end of the session. No branch switch (the Rev 8
files were read with `git show eoc-revision8:…`, which does not touch the working
tree), no commit, push, reset, stash, publication or global install. No scratch
clone was needed: both repositories were already present and were read in place.

Lean modules read (names located, not invented): `EOC/Carry.lean`-equivalent
content via `Occupation/`, `EOC/Realizer.lean`, `EOC/BoundedDrift.lean`,
`EOC/FinitePrefixPacking.lean`, `EOC/HarmonicPacking.lean`
(`sum_inv_orbit_le`, `carryU`, `carryE`), `EOC/HarmonicFloor.lean`,
`EOC/LogCorridor.lean`, `eoc-divergence/Occupation/{Compositions,Rate}.lean`.
There is **no** module named `SeparatedReturns`, `OrbitLifetime` or
`TransportRegeneration` in either repository; the corresponding content is in
`LogCorridor.lean`, `HarmonicPacking.lean` and the manuscript's §§8, 13.
Recorded rather than invented.

## 3. Prior routes checked before proposing anything

| path | status | what was recovered |
|---|---|---|
| the Phase 6 return-gate round (local scratch, not published) | **PRESENT, read** | Phase 6. Answers 1–3, 7–10 and the secondary findings. **Decisive for attribution:** the pinned surrogate `Q = N(1+K(log_2m_0−c))+O(NK log_2((3/2)P))`, *"all charges are the same to within a small additive constant"*, *"none … supplies a quantity that decreases"*, *"the gate overcounts by `Θ(m_0/log m_0)`"*, the `Θ(m_0 2^{−c})` attained episode bound, the mod-18 entry classes, and the open depth-`≈ℓ/10` dichotomy (`corr = +0.923`) |
| the Phase 7 gate-placement round (absent from the machine) | **ABSENT** | not on this machine. Limitation recorded; placement recovered indirectly from the Lopez-Stoll package and the EOC record (placement `=` Open Problem C, obstruction `=` the additive term) |
| `audits/lopez_stoll_transfer_2026-10-14/` | PRESENT, **unmodified** | the carry/`z_n` dictionary, `Σ_i 2^{−Δ_i} = 3m_0(2^{E_N}−1)`, the harmonic-packing constant `3e^{7/9}`, and the `N^{8/9}` shape |
| the growing-scale-pairs round (local scratch, not published) | PRESENT, **unmodified** | Theorem E's power-law barrier shape; not re-audited |
| `audits/amplification_transfer_2026-10-14/` | PRESENT, **unmodified** | that statistical scarcity caps nothing pointwise; not re-audited |

No renewed López–Stoll audit and no percolation-transfer work was done, as
instructed. Files modified in any pre-existing package: **0** (checked).

## 4. Environment and numerical policy

```
Python 3.14.7, CPython standard library only.  No third-party package imported
or installed.  No Lean, no lake build, no rebuild.
```

All corridor, carry, matrix-product, oddness and rational weighted-sum decisions
are exact `int`/`Fraction`. **Corridor membership is always
`2^{S_n} ≤ 2^c · 3^n` on integers**, for integer `c`; the depth strata are
decided by `2^{S_n+w} ≤ 2^c 3^n < 2^{S_n+w+1}`. Printed `R_n`, `η_i`, `A_i`,
depths and ratios are floating diagnostics only, never a decision. Horizons are
**certified**: once `m_n = 1` the orbit sits at the fixed point with `d = 2`, so
`R` strictly increases and no later index can be occupied — `loeb.py` checks that
`[H, H+40)` is empty rather than relying on a cutoff.

## 5. Commands, runtimes, resources

One worker throughout, no parallelism, no subprocesses. `RLIMIT_AS` set to 4 GiB
in every script; `timeout` on every invocation; all runs from
`env -i PATH=/usr/bin:/bin HOME=$HOME`.

| script | runtime | peak RSS | result |
|---|---|---|---|
| `dictionary.py` | ~20 s | 11.9 MiB | 11/11 identities, **0 violations** |
| `loeb.py` | ~10 s | 12.5 MiB | `O_1=98`, `L_1=14`, `τ_1=15`, all 7 runs, `W_i`/`η_i`/gaps exact |
| `joint.py` | ~25 s | 13.6 MiB | C1 holds, vacuous; gap share `≥0.998`; `A_i` non-monotone (2/7) |
| `pin_and_controls.py` | ~15 s | 13.6 MiB | Prop. J at **17 re-entries, 0 violations**; controls A, B, D, E |
| `controlC.py` | ~10 s | < 20 MiB | oscillator `P ~ 0.42N`, realizer reproduces the word |
| `where_nonvacuous.py` | ~15 s | < 20 MiB | slack `3.5×` on bounded drift, `10^4–10^7` otherwise |
| `localtime.py` | ~10 s | < 20 MiB | `w_max/log_2 O_c ∈ [1.16,1.73]` |
| `scale_gap.py` | ~20 s | < 20 MiB | `pot/m_0 ∈ [0.34,0.74]`; overshoot to `1.5×10^8` |

## 6. Errors made and corrected in this session

1. **Control C was wrong as first written** — it chose the digit by testing
   `S_n + 2` (the post-step sum) instead of corridor membership at `n`, producing
   one episode of length 200 instead of the oscillation. Corrected in
   `scripts/controlC.py`; the fixed version shows `P ≈ 0.42N`.
2. **My amortization hypothesis was refuted** — I expected `A_i` to be
   non-decreasing in `i`; it is not (2 of 7 cases). The correct statement is the
   two-sided pin, which is Phase 6's.
3. **I initially presented Proposition J, its corollary, and the
   `Θ(m_0/log m_0)` scale verdict as new.** All three are Phase 6 answers 3, 7
   and 8. Attribution corrected in `JOINT_EPISODE_ARGUMENT.md` (two `PRIOR ART`
   boxes) and in the ledger before the verdict was written.
