# Zero confinement and temporal lift-digit dynamics

**2026-10-16.  Verdict: E (lift mechanism obstructed) + D (identities explain the statistics).
No repository modified; nothing published.**

## First, a correction to my own prior work

The October 16 terminal-tip enumeration used `N = 11`, `S_N = 22`.  Zero confinement requires
`2^{S_k} ≤ 3^k`, and `2^22 = 4 194 304 > 3^11 = 177 147`.  **That population was not confined.**
The algebraic conclusions there stand; every statistical statement in that run is superseded by
the genuinely confined enumeration here.

## The question, answered

> Does zero confinement constrain the lift pattern strongly enough to give a new theorem?

**No — it constrains `J(N)` in neither direction.**  On complete exact enumerations:

```
min J(N) = 3     for every N = 6..13    (least realizer 71, zero-lift plateau N−5)
max J(N) = N−1   for every N            (all-ones word, x = −1, never stabilises)
```

Both extremes are occupied at every length.  **This pair is a two-line refutation of any
proposed confinement-driven lift-density bound**, and it is the counterexample the brief asked to
be preserved.

And Target A is circular: `J(∞) = ∞` for all infinite confined words says exactly that no such
word has a nonnegative-integer realizer — which, since confinement forces `m_n > m_0`, *is* the
open problem.

## What the lift sequence actually is

**Theorem L2** `[PROVED, 7 100 positions, 0 failures]`.  With `m_n = (3^n r_n + C_n)/2^{S_n}`,
```
b_n = 0  ⟺  2^{d_n} | 3 m_n + 1 ,        b_n ≡ −(3m_n+1)·3^{−(n+1)}  (mod 2^{d_n}) .
```
> **`J(N)` counts the times the word demands a deeper 2-adic valuation than its running least
> realizer supplies.**

Also **L1**: `x = −Σ3^{−(j+1)}2^{S_j}` and `b_n` is the binary block of `x` in `[S_n, S_{n+1})` —
so Proposition R becomes a triviality rather than something to reprove.

## The statistics are uniform blocks plus weighting artefacts

`b_n` depends only on `(d_0,…,d_n)` — never on the future.  So pooling over full words weights
each prefix by its continuation count, and slack correlates with that count.  Counting each
**prefix once**:

| `G_n` (slack), at `d_n=1` | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| pooled over words | 0.7423 | 0.6879 | 0.6391 | 0.5982 |
| **per prefix** | **0.5094** | **0.5054** | **0.4963** | **0.5055** |
| null `1−2^{−d_n}` | 0.5000 | 0.5000 | 0.5000 | 0.5000 |

The slack effect vanishes.  Across all 18 populated cells the match to the null is within
`±0.021`.  The separate "lift density above null" excess is a small-`n` boundary effect
(`P(lift) = 1` exactly at `n = 1,2`), gone by `n ≥ 6` (diff `+0.0025`).

## Retractions

Three of my own claims were withdrawn mid-session, each caught by its own output:

* **L3** — "`m_n` is always odd, so `d_n=1 ⟹ b_n=0`, so `J(N) ≤ S_N − N`".  False: `m_n` is even
  at 4 914/8 480 positions.  Minimal counterexample `d=[1]`, `m_0=0`.  Replaced by **L3′**.
* "Minimisers are orbit prefixes of small integers" — contradicted at `N = 9, 13`.  The
  congruence forces `v_2 ≥ d_j`, not equality, so congruence words ≠ orbit words.
* "`P(lift)` is essentially flat in the slack" — contradicted by the `d_n=1` column directly
  above it.  Resolved by the prefix control.

## Documents

`01_BASELINE_AND_CLOSED_ROUTES.md` · `02_LIFT_BLOCK_THEORY.md` ·
`03_ZERO_CONFINED_ENUMERATION.md` · `04_TEMPORAL_STATISTICS.md` · `05_EXTREMAL_WORDS.md` ·
`06_EOC_TRANSFER.md` · `07_CANDIDATE_LEMMAS.md` · `08_POINTWISE_VERDICT.md`

## Reproducing

```
cd scripts
python3 run_theory.py     # L1, L2 (and the false L3, kept for the record)
python3 run_fix.py        # the L3 retraction and corrected L3'
python3 run_enum.py       # exact confined enumeration + lift statistics
python3 run_extremal.py   # min J = 3
python3 run_min71.py      # the 71 correction: congruence words vs orbit words
python3 run_controls.py   # all-ones benchmark; both extremes confined
python3 run_slack.py      # the prefix control that kills the slack effect
python3 run_nullcheck.py  # the small-n boundary effect
```
Exact integer/modular arithmetic; stdlib only; frozen outputs in `results/`.
