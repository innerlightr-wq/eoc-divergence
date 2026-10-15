# PROVENANCE.md

## 1. Inputs

| source | used for |
|---|---|
| [`audits/episode_classification_2026-10-14/RUN_ARITHMETIC.md`](../episode_classification_2026-10-14/RUN_ARITHMETIC.md) §5 (Theorem D) | the realizing class of `1^u q 1^v`; the **only** mathematical input to Theorem U |
| [`audits/episode_classification_2026-10-14/CLASSIFICATION.md`](../episode_classification_2026-10-14/CLASSIFICATION.md) §4 | the measured `k/ℓ = 0.4537` coverage facts used in Level B |
| [`audits/joint_episode_budget_2026-10-14/VERDICT.md`](../joint_episode_budget_2026-10-14/VERDICT.md) | the no-amortizable-resource and `Θ(m_0)`-pot results used in Level D |
| EOC Revision 8 — Prop. 6.4 (residue–time duality), Remark 5.8 (moving anchor), Remark 6.2 (`O_1(285175) = 98`), Remark 13.3, Prop. 13.1 | Levels B, C, D and the scope note in `TWO_RUN_FLOOR.md` §5 |
| `eoc-lean-verification`, `EOC/Realizer.lean` — `leastRealizer_unique`, `residue_pinning` | Level C |

Revision 8 was read from `eoc-lean-verification` branch `eoc-revision8` =
`b2dcae22dbefe8af89c83f00ebd038d6b21c0304`, `paper/eoc_rev8.pdf` sha256
`07c6610d633035e43b8a36905e0c58e517704ca12bb208e2340359dea30f294c`, with
`git show` (which does not touch the working tree). That file is not in this
repository, which carries `docs/eoc_rev7.pdf`.

**No external paper is relied on.** `TWO_RUN_FLOOR.md` §3 and `VERDICT.md` §3
describe the *shape* of the available `×2,×3` methods (measure-theoretic,
exceptional-set) in order to say why they do not apply; no named theorem is cited
as supplying anything, and no claim is made about what exists for this diagonal.

## 2. Environment and numerical policy

```
Python 3.14.7, CPython standard library only.  No third-party package imported
or installed.  No Lean, no lake build, no formal theorem added.
```

`A*` is computed by modular inversion mod `2^{n+1}`; confinement is decided as
`2^{S_j} ≤ 2^c·3^j`; minimality is brute force over odd candidates. Every
congruence, divisibility, confinement and minimality decision is exact `int`.
Floating point appears only in printed diagnostics (`log₂(r+1)/S`, the real form
of the cone) and never in a decision.

| script | runtime | peak RSS | result |
|---|---|---|---|
| `scripts/floor.py` | ~40 s | 10.6 MiB | the class exact and minimal on 120 triples; every step of Theorem U on 2912 triples; Observation P at four `(q,v)`; the cone, 0 violations; the critical diagonal admissible at five `b`. **All pass** |

One worker, `RLIMIT_AS` 4 GiB, timeout on the invocation.

## 3. Novelty discipline

* **Theorem U is an elementary corollary of the published Theorem D**, and is
  labelled as such everywhere. What is new is only the observation that the two
  bounds oppose each other in `u`, fixing the exponent at `1/(1+log₂3)`.
* **Observation P** (periodicity of `A*_u` for fixed `(q,v)`) follows in one line
  from Theorem D and the structure of `⟨3⟩ ≤ (Z/2^{n+1})^×`; it is standard group
  theory and no novelty is claimed for it.
* **Proposition A** (the admissible cone) is elementary from the drift
  arithmetic.
* The bit-count/placement split is Theorem D's content, already published in the
  episode-classification audit.
* No literature connection is presented as a mathematical advance.
