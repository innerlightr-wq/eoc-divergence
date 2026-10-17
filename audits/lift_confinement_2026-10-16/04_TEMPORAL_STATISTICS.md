# 04_TEMPORAL_STATISTICS.md

## The structural fact that governs every statistic here

> **`b_n` is a deterministic function of `(d_0,…,d_n)` alone.**  `r_n` and `d_n` depend only on
> the prefix through position `n`; the future digits never enter.

Consequently any statistic pooled over **full words** counts each prefix with multiplicity equal
to its number of admissible continuations — and under confinement that multiplicity depends on
the slack.  **This is a weighting artefact, and it produced both apparent effects below.**

## The confinement slack has no effect `[DISPROVED as an effect]`

Exact integer slack `G_n = cap(n) − S_n`.

**Pooled over full words** (`N = 12`, all 8 045 confined words), `P(lift)` at `d_n = 1`:

| `G_n` | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| `P(lift)` | 0.7423 | 0.6879 | 0.6391 | 0.5982 |

an apparent monotone decline.  **Enumerating each confined prefix exactly once** (the correct
control), the same cells give:

| `G_n` | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| `P(lift)` | 0.5094 | 0.5054 | 0.4963 | 0.5055 |
| null `1−2^{−d_n}` | 0.5000 | 0.5000 | 0.5000 | 0.5000 |

**The trend disappears.**  Across all 18 populated `(G_n, d_n)` cells with ≥300 prefixes, the
observed rate matches `1 − 2^{−d_n}` to within `±0.021`, with most cells inside `±0.01`
(`results/run_slack.txt`).

> **Lift blocks behave exactly like uniform blocks on `[0,2^{d_n})`.**  The slack does not
> predict lifts; the digit `d_n` does, and only through the trivial `P(b_n = 0) = 2^{−d_n}`.

## The "lift density above null" finding — corrected

`03_...` shows mean `J` exceeding the per-word null `Σ(1−2^{−d_n})` (e.g. 8.883 vs 7.282 at
`N = 13`).  Resolved by position (`results/run_nullcheck.txt`):

| `n` | 1 | 2 | 3 | 5 | 6 | 8 | 10 | 12 |
|---|---|---|---|---|---|---|---|---|
| observed `P(lift)` | 1.0000 | 1.0000 | 0.8080 | 0.7245 | 0.6002 | 0.6378 | 0.6497 | 0.6757 |
| null | 0.5480 | 0.5480 | 0.5727 | 0.5954 | 0.6056 | 0.6209 | 0.6492 | 0.6717 |
| diff | +0.452 | +0.452 | +0.235 | +0.129 | **−0.005** | +0.017 | +0.0005 | +0.004 |

Tail aggregates: `n ≥ 1` diff `+0.1334`; `n ≥ 4` `+0.0512`; **`n ≥ 6` `+0.0025`**; `n ≥ 8` `+0.0058`.

> The excess is a **small-`n` boundary effect** — at `n = 1,2` the modulus `2^{S_n}` is 2 or 4,
> `r_n` has almost no room, and `P(lift) = 1` exactly.  By `n ≥ 6` the observed rate tracks the
> uniform null to three decimals.  **It is not a confinement effect**, and my first phrasing of
> it as a finding was misleading.  Corrected.

## Plateaus

Mean longest zero-lift run grows slowly (0.729 at `N = 7` to 1.872 at `N = 13`), while the
*maximum* plateau reaches `N − 5` on the minimisers (`05_EXTREMAL_WORDS.md`).  Both are
consistent with uniform blocks: the expected longest run of successes with per-step probability
`2^{−d_n}` grows logarithmically, and the extreme is attained by the one word whose realizer
stabilises.
