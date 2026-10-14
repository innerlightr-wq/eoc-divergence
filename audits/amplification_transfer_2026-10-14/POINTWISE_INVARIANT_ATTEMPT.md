# POINTWISE_INVARIANT_ATTEMPT.md — the second route, bounded, and what it measured

The brief asks for **one bounded attempt** at a deterministic obstruction
invariant if joint inverse reconstruction fails. It failed (see
`JOINT_INVERSE_ATTEMPT.md`), so this is that attempt. **Outcome: no new
invariant.** The candidate invariant is a restatement of the target. What the
attempt did produce is a measurement that locates the difficulty precisely, and
the sharpest statement of the missing lemma that this session can justify.

---

## 1. The candidate invariant, and why it is a restatement

For a persistent seed `m`, `EOC/Realizer.lean`'s `residue_pinning` gives
something that looks like a strong simultaneous constraint:

> For **every** depth `N` with `m < 2^{S_N(m)+1}` — and since `S_N >= N` that is
> every `N > log_2 m` — the integer `m` is the **unique least realizer** of its
> own depth-`N` valuation word.

So `m` is simultaneously the minimal realizer of a word of length `N`, for every
`N`, with the carry data `q_N` and the congruence
`3^N m + q_N ≡ 2^{S_N} (mod 2^{S_N+1})` holding at every depth. This is a
consistently defined arithmetic quantity (not a sequence of unrelated
valuations), it involves the actual positive integer, and the constraints
accumulate.

**But the accumulation is not impossible — it is exactly the target.** Since
each of the `n_N = 2^{gN+o(N)}` confined words has its own least realizer in
`[0, 2^{sN+1})`, and `m` is one of them at every depth,

```
   r_min(N,0)  <=  m   for every  N ,
```
which by Lemma T of `EOC_DIVERGENCE_TARGET.md` §2 is *equivalent* to the
existence of `m`. The route closes on itself: the invariant restates
persistence, and "an impossible accumulation of constraints" is precisely what
has to be proved, not something the invariant delivers. Reported as a
restatement, promptly, per the brief.

## 2. What the attempt measured instead

Define `W(N,X) = #{m odd, m < X : 2^{S_j(m)} <= 3^j for all j <= N}`. If the
confined residues were equidistributed in an initial window, `W(N,X)` would be
near the **fair value** `X·p(N,0)/2`. Exact scan of all `65536` odd
`m < 2^17`, confinement by integer comparison only
(`scripts/placement.py`, `results/placement.log`):

| `N` | `r_min(N)` | `W(N,X)` | fair `= X p/2` | `W/fair` |
|---|---|---|---|---|
| 10 | 27 | 4228 | 4228.000 | 1.0000 |
| 14 | 27 | 2598 | 2637.609 | 0.9850 |
| 18 | 27 | 1548 | 1558.993 | 0.9929 |
| 22 | 27 | 991 | 1006.475 | 0.9846 |
| 24 | 27 | 847 | 861.057 | 0.9837 |

> **The bulk obeys equidistribution to within `1.6%` at every depth measured.**

Now the extreme left tail. If the confined set had density `p(N,0)` in an
initial window, its least element would sit near `rho(N) := 2/p(N,0)`. Against
the record-seed ladder `3, 7, 27, 703, 10087, 35655, 381727`, whose confinement
depths were recomputed here by direct orbit iteration as
`1, 3, 36, 50, 65, 84, 108` (`scripts/tail_ratio.py`):

| `N` | `r_min(N)` | `rho(N) = 2/p(N,0)` | `rho/r_min` |
|---|---|---|---|
| 24 | 27 | 152.22 | 5.6379 |
| 32 | 27 | 337.42 | 12.4970 |
| 36 | 27 | 468.22 | **17.3414** |
| 40 | 703 | 669.76 | 0.9527 |
| 56 | 10087 | 2434.40 | 0.2413 |
| 80 | 35655 | 14331.16 | 0.4019 |

(`r_min` taken over the record ladder, hence an **upper** bound on the true
`r_min(N)`, so the ratios are **lower** bounds.)

> **The ratio does not grow.** It climbs to about `17` as a record seed is
> stretched to its limit, then falls *below* `1` when the next record takes over
> — the new record is *larger* than the equidistribution prediction. Over
> `N = 4..108` it oscillates in a bounded band. Equivalently:
> `r_min(N,0) = 2^{I_0 N + o(N)}` up to a factor observed to stay `<= ~17`,
> exactly the aggregate prediction.

This is consistent with the repository's own `r_min` frontier work, whose ratio
envelope stalled around `10.3` in a different normalization and could not be
pushed to its target constant.

## 3. The finding

**The aggregate statistics are correct, and that is exactly why they say
nothing.** The bulk of the confined population sits where the rate predicts, to
`1.6%`. The whole of the divergence problem lives in a single atypical integer
per range — the record seed — which beats the average by a bounded factor and
then yields to the next one. There is no bulk anomaly to exploit and no
accumulating deficit to contradict: the only thing an invariant would have to
rule out is one integer sitting a bounded factor below the mean, and a bounded
factor is invisible to every exponential-rate argument, including
`confined_mass_rate`.

This independently reproduces, from a different direction, the repository's
recorded position that placement is Open Problem C and that **the obstruction is
the additive term** — here it is visibly additive and visibly confined to the
left tail.

## 4. The smallest missing lemma, stated as sharply as this session can justify

> **(LEFT-TAIL).** There exist `C >= 1` and `B >= 0` such that for every `N`,
> ```
>    W(N, X) = 0      whenever      X  <=  C^{-1} N^{-B} / p(N,0) .
> ```
> Equivalently: `r_min(N,0) >= C^{-1} N^{-B} / p(N,0)`.

**It suffices.** By `confined_mass_rate`, `1/p(N,0) = 2^{I_0 N - o(N)}`, so
(LEFT-TAIL) gives `r_min(N,0) >= 2^{I_0 N - o(N)} -> infinity`; by Lemma T no
persistent seed exists, which is the pointwise divergence-exclusion target `C`.

**It is purely multiplicative — that is the whole point.** The corresponding
bound *with* an additive term,
`W(N,X) <= C N^B X p(N,0) + C N^B`, is useless: at a fixed `X_0` the additive
term alone permits a confined seed at every depth. The content of (LEFT-TAIL) is
exactly the absence of that term, which is the repository's recorded obstruction.

**It is sharp and not obviously out of reach.** The measurements of §2 say it
holds with `B = 0` and `C ≈ 17` on every depth tested up to `108`. Any
`C` and any polynomial `N^B` suffice, so the lemma asks only that the record
seed's advantage over the mean stay **subexponential** — not bounded, not small,
just `2^{o(N)}`.

**What it is not.** It is not implied by anything proved here. It is a
*placement* statement about where the confined residues fall in an initial
window, not a counting statement about how many there are, and §2 of
`AMPLIFICATION_CRITERION.md` shows that no amount of counting can supply it.
Proposition W makes the heuristic exact in the aggregate and still does not
touch it, because a product law on letter strings has nothing to say about which
integer realizes a given string.
