# Joint episode budgets and arithmetic linkage — 2026-10-14

**Question.** Can the linkage between two or more *actual* corridor episodes
(`R_n ≤ c`, one-sided) produce a nonautomatic bound on their **combined
duration**, not obtained by charging each episode its own single-window lifetime
allowance?

**Verdict: no, and the failure is a theorem.** The amortized charge exists and is
genuinely joint — one shared pot, no refreshed per-episode seed budget — but it
is non-vacuous **only** where the drift stays in a bounded two-sided window,
which `EOC/BoundedDrift.lean` (in `eoc-lean-verification`) already closes.

Read [`VERDICT.md`](VERDICT.md) for the six answers;
[`JOINT_EPISODE_ARGUMENT.md`](JOINT_EPISODE_ARGUMENT.md) for the mathematics;
[`CLAIMS_AND_CONTROLS.md`](CLAIMS_AND_CONTROLS.md) for the
`[PRIOR]`/`[P]`/`[V]`/`[R]` ledger and controls A–E.

## What came out

* **New (small): the entry toll.** From Rev 8 Prop. 13.1, at every re-entry
  `z_{a_i} = 2^{R_{a_i}} > (2/3)2^c`, hence `W_i > (2/3)2^c` and
  **`η_i ℓ_i > 2/3`** — a universal floor on the carry-*weighted* duration,
  independent of `ℓ_i` and of the depth reached.
* **Why the joint charge points the wrong way.** The pot
  `Σ_{n<H} z_n = 3(𝓑_H − m_0)` is **99.94 %** gap weight at the Loeb seed
  (occupied `53.31` against gap `96115.13`), because `z_n ≤ 2^c` on the corridor
  while `z_n > 2^c` and growing in a gap. Amortizing against it bounds **gap**
  time: it rearranges to `O_c > H − 2^{−c}·pot`, a *lower* bound.
* **Non-vacuity is localized.** Slack is a stable `3.5×` on the Rev 8 Prop. 13.2
  oscillator (bounded two-sided drift) across `c = 0,1,2`, `N = 60,120,200`, and
  degrades like `2^{R_max−c}` to `10^4–10^7` on seeds whose drift escapes.
* **The small-`η` problem, made exact.** Stratifying by depth,
  `Σ_w L_w 2^{−w} < 2^{1−c}·pot` while `O_c = Σ_w L_w`. The route needs
  `w_max ≤ K log_2 O_c` with `K < 1`; measured
  `w_max/log_2 O_c ∈ [1.16, 1.73]`, so **`K<1` is not supported**.
* **Silent on divergence.** A hypothetical infinite zero-confined orbit is a
  *single* episode: `P = 1`, toll `= 0` exactly. **Classification:
  separated-return control, not divergence exclusion.**

## Prior art, credited

The two-sided allowance pin and the `Θ(m_0)`-versus-`O(log m_0)` scale verdict
were **already established** in the Phase 6 return-gate round (local scratch, not
published): the pinned surrogate `Q = N(1+K(log_2m_0−c)) + O(NK log_2((3/2)P))`,
*"all charges are the same to within a small additive constant"*, and *"the gate
overcounts by `Θ(m_0/log m_0)`"*. This round re-derives them by a different
resource (the carry pot rather than the entry gate) and adds the exact integral
form. The episode-count bound here is **strictly weaker** than Phase 6's attained
bound. See `JOINT_EPISODE_ARGUMENT.md` §§5–6, `PRIOR ART` boxes.

## Reproduction

CPython standard library only; no Lean, nothing installed. **Every corridor,
carry, matrix-product, oddness and weighted-sum decision is exact
`int`/`Fraction`; corridor membership is `2^{S_n} ≤ 2^c·3^n` and never a
floating-point logarithm.** Horizons are *certified* by the fixed-point drift
(`d = 2` at `m = 1`), not by a scan cutoff. One worker, `RLIMIT_AS` 4 GiB, peak
RSS ≤ 14 MiB.

```bash
python3 scripts/dictionary.py        # 11 accounting identities            ~20 s
python3 scripts/loeb.py              # Loeb benchmark 285175, c=1          ~10 s
python3 scripts/joint.py             # candidate bound + amortization test ~25 s
python3 scripts/pin_and_controls.py  # Proposition J + controls A,B,D,E    ~15 s
python3 scripts/controlC.py          # control C (Prop. 13.2 oscillator)   ~10 s
python3 scripts/where_nonvacuous.py  # where the bound is non-vacuous      ~15 s
python3 scripts/localtime.py         # corridor local-time profiles        ~10 s
python3 scripts/scale_gap.py         # resource scale vs target scale      ~20 s
python3 tests/regression.py          # 20 assertions, clean process        ~45 s
```

`results/` holds the frozen run logs (they record the original local paths, as
run records do). `MANUSCRIPT_HASHES.txt` records the Revision 8 identity,
including the discrepancy between the authoritative branch copy and an earlier
draft — see `PROVENANCE.md` §1.

## Scope

Nothing here proves, advances or conditionally establishes EOC, Open Problem F,
divergence exclusion, cycle exclusion, or the Collatz conjecture. No
corridor-uniform lifetime hypothesis is assumed (Rev 8 §7.1's warning
respected). Rev 8 Theorem 6.14's external sparsity dependency is untouched.
Lemmas 2.2/2.4, Definition 6.1, Propositions 13.1/13.2 and Remark 13.3 are the
manuscript's; the Eliahou–Rozier identity is Eliahou's and Rozier's. **No Lean
verification is claimed** — no `lake build` was run; Lean entries are
source-backed by reading the files named.
