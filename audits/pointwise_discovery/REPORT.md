# Audit: a pointwise finite-height constraint on the accelerated `3x+1` map

**Verdict: D — no usable pointwise signal.** 2026-09-25.

Pre-registration and the theorem ledger the search was residualized against:
[`PHASE0.md`](PHASE0.md). Rejected relations: [`REJECTED_CANDIDATES.md`](REJECTED_CANDIDATES.md).
Candidate ledger: [`CANDIDATE_CONSTRAINTS.md`](CANDIDATE_CONSTRAINTS.md).
Scripts: [`scripts/`](scripts), with [`scripts/RUN.md`](scripts/RUN.md); committed
outputs: [`data/`](data); figures: [`figures/`](figures).

This audit was run outside the repository and is imported here as a record. It
modified nothing; the one change it motivated — the `5x-1` first-step sieve — is
in [`../cross_map`](../cross_map), with its own correction note.

---

## 0. Verdict

> ## D — no usable pointwise signal.
>
> In the tested regime, finite integer height produces **no** constraint on deep
> valuation/parity data beyond what the Terras–Everett correspondence and the
> confined-word count already give. The null was not merely un-rejected: it was
> confirmed to a measured precision, on complete enumerations, by a pipeline
> demonstrated to have ~235× the power needed to see the corresponding effect on
> a control map where an elementary argument says it must be there.

Three things came out of the run that are worth keeping, none of them a
constraint:

1. **An exact reduction of the question** ([`CANDIDATE_CONSTRAINTS.md`](CANDIDATE_CONSTRAINTS.md) C1): all of
   the content of `m < 2^B` at depth `n` is the single scalar
   `delta(w) = S_n + 1 - log2 r(w)`. The missing law of *After the Reduction* §(f)
   is exactly a law for the joint distribution of `(S(w), delta(w))` — nothing
   else can carry it. This is a restatement, but it makes the target finite and
   measurable, and it is what the rest of the run measured.
2. **A quantified negative contrast** ([`CANDIDATE_CONSTRAINTS.md`](CANDIDATE_CONSTRAINTS.md) M1): the
   archimedean size of the seed leaves a ~470-sigma fingerprint on the deep word
   statistics of `5x-1`, and none (< 2 sigma) on `3x+1`. The programme asserts
   this difference qualitatively; here it is measured.
3. **A defect in a published control dataset** (§6): the `5x-1` record ladder in
   `audits/cross_map` is computed over a sieved population and is wrong from
   `N = 2` onward. This refutes Open Problem 11 of the synthesis note as stated.

**Nothing here bears on (DE), on Open Problem C, or on the Collatz conjecture,
and nothing is offered as progress toward any of them.**

---

## 1. What was asked, and what it reduces to

The brief asked whether, for odd `m_0 < 2^B`, additional restrictions appear on
the orbit data as `lambda = n/B` grows. The programme's own statement of the gap
(*After the Reduction* §(f)) is that a usable law would bound, as a function of
`B` and `n`, how much of the parity prefix is **forced** by `m < 2^B`.

That question has an exact answer, and getting it first is what made the rest of
the run decidable. By Terras–Everett a word `w` of length `n` and total `S` is
realized by exactly one residue class mod `2^{S+1}`, whose least positive member
is
```
        r(w) = q^{-n} ( 2^S - r C_n(w) )  mod 2^{S+1}
```
— an explicit arithmetic function of the word alone. Every odd `m < 2^{S+1}` is
therefore the least realizer of its own depth-`n` word. Writing
`delta(w) = S + 1 - log2 r(w)`:

```
   { odd m < 2^B : n-confined }   <->   { w confined : delta(w) > S(w) + 1 - B }
```

So finite height forces **nothing** about the word except through `delta`.
Two consequences fix the geography of the problem:

| regime | status |
|---|---|
| `lambda <~ 1/log2 3 = 0.6309`<br>(exactly: `A[n]+1 <= B`) | finite height is **provably vacuous**: `#{odd m < 2^B : n-confined} = 2^{B-1} p_n(0)` exactly. *(This is the repository's own §5.6 fact, on the `lambda` axis. 216 grid cells, 0 violations.)* |
| in between | mixed: a word's class may have several representatives below `2^B`, and the count is neither forced nor a bijection |
| `lambda >= 1 - 1/B`<br>(exactly: `n >= B-1`) | one integer per word; the bijection above is exact |

And the null that reproduces **every** known counting fact is the uniform-class
null
```
        H0:   delta independent of the word,   P(delta > t) = 2^{-t}.
```
Under H0 the induced word law of `{odd m < 2^B : n-confined}` is *exactly* the
dyadic law `2^{-S(w)}/p_n(0)` — i.e. exactly the law of a random confined `2`-adic
integer, for every `B`. **Any departure from H0 is therefore residual to the
aggregate identity, the Terras–Everett correspondence, the confined-word count,
the `N^{-3/2}` correction and the density exclusions, all at once.** That is the
sense in which every measurement below is residualized.

---

## 2. What was run

Exact integer arithmetic throughout; floating point appears only in reported
logarithms and never in a decision. The core reproduces 13/13 published values of
`eoc-divergence` (`data/verify_core.txt`), including `num_2 = 3`,
`num_14 = 168807`, the `log2(1/p_N) - I_0 N - 1.5 log2 N` table at
`N = 10 .. 300`, the `3x+1` record ladder, the `3x-1` conjugacy, and the
shelter/pigeonhole witnesses.

| dataset | construction | size |
|---|---|---|
| **D1** | complete scans, no sieving: `3x+1` to `2^32` and `2^36`; `3x-1` to `2^28` and `2^32`; `5x+1` to `2^28`; `5x-1` to `2^32` (twice, with different dump thresholds). Exact `__int128`, overflow guard `2^118` — **0 guard hits in all eight scans**, so every recorded depth is exact, not a lower bound | `1.3e8`–`3.4e10` seeds each |
| **D2** | rare-side words sampled **exactly** from the dyadic law by an integer transfer table; every sampled word re-realized and re-read to confirm | 20–40 k per (map, `n`), 29 datasets |
| **D3** | complete cohorts of `n`-confined integers, `n = 140,160,180,200` | 2 124 – 83 587 |
| **D4** | the same for `3x-1`, `5x+1`, `5x-1` on their own rare sides | — |

Sampler gate (pre-registered): reproduces `num_N` exactly, matches the exact word
frequencies at `n = 6` to `0.0015` over 200 000 draws, and the counting bijection
was brute-forced at three `(B,n)` points with 0 violations.

---

## 3. The measurements

**M1 — the `lambda` grid** (`figures/fig1_occupancy_grid.png`). `E_B(n) = #{odd m<2^B : n-confined} /
(2^{B-1} p_n(0))`, complete scan, exact denominator. Identically 1 on all 216
cells with `A[n]+1 <= B` (a theorem, used as a pipeline check). Above that:
per-bit-length `z`-scores in `[-3.4, +3.4]` over ~200 cells, both signs, no
organisation in `lambda`; the one systematic part is the known clustering
immediately above `r_min(n)`, and chain-root thinning removes it
(`n=160`: `E=1.43, z=+2.9` → `E_root=1.07, z=+0.4`). A sum rule
`sum_b 2^b (E_b(n)-1) = 0` makes the coexistence of deficit and excess a
theorem, not an observation.

**M2 — the `delta` marginal** (`figures/fig2_delta_law.png`). `P(delta > t)` against `2^{-t}`,
`t = 1..10`, 25 datasets, 4 maps, `n = 20..300`. **Not one `|z| > 4`.**
Mean `delta` `1.424-1.460` against `1/ln2 = 1.4427`.

**M3 — dependence.** Spearman `rho(word statistic, delta)` with `S` partialled
out, 27 statistics × 25 datasets: `max |rho| = 0.023`; **zero** exceedances of
`4 SE`. Multivariate `R^2` on all 27 statistics at or below chance in every
dataset.

**M3b — the small-realizer tail.** The 1 % of words with the smallest realizers
against the rest, standardised within `S`: they differ in `S` (`t = -34` to
`-59`, which H0 predicts exactly) and in **nothing else** (`max |t| = 2.4` over
675 tests). This is the record-holder audit's "the extremes are generic",
reproduced with thousands of points instead of 24.

**M4 — the pointwise test.** All 72 804 integers below `2^32` that are
100-confined, against 20 000 exactly-sampled generic confined words: every word
statistic agrees to within **0.02 standard deviations**, `max |t| = 2.37`,
including `S` itself. These integers sit at `delta ~ 124`, a regime no sampling
can reach. *(Coarse-binned versions of this test, run first, threw `|t|` up to
5.7. Those are binning plus chain correlation, dissected in
`REJECTED_CANDIDATES.md` R6 and settled by M4e below; they are recorded rather
than dropped.)*

**M4d/M4e — height against word shape.** Over complete cohorts below `2^36`,
`rho(word statistic, log2 m)` on chain roots with a chain-level bootstrap:
`max |z| = 2.74, 1.72, 2.00` at `n = 140, 160, 180`. *The size of a confined
integer carries no information about its valuation word.*

**M6/M7/M8 — the terminating tail in deep data.** `chi^2(m mod 32, a_k)` on
chain roots reaches the null by `k ~ 50` and stays (`z = 0.13, 0.09, -0.65` at
`k = 50, 100, 139`). The aggregate letter law of the 55 665 chain-root 36-bit
integers that are 140-confined, against the **exact rational** ensemble law with
a word-level bootstrap: `max |z| = 1.98` over `d = 1..10`;
`P(a=1)` differs by `+1.3e-4 ± 1.1e-4`.

**M9 — the controls, and the power calibration** (`figures/fig4_control_contrast.png`). The same pipeline,
same depth, comparable cohort sizes:

| map | rare side is | cohort | `max |z|` |
|---|---|---|---|
| `3x+1` | the **growth** side | 55 665 roots < `2^36` | **1.98** |
| `3x-1` | growth (sign-conjugate of `3x+1`) | 5 143 < `2^32` | 4.82 |
| `5x-1` | the **shrinking** side | 406 761 < `2^32` | **465.7** |

and the `5x-1` effect is attributed, not fitted: persistence there *proves*
`m_n < m_0`, so the orbit is trapped in `[1, m_0]`; **34.54 %** of the cohort has
already repeated an orbit value by depth 140. For `3x+1`, **0** of 83 587 orbits
repeat (forced by `Divergence.not_zeroConfined_of_repeat`) and **100 %** have the
seed as their minimum.

---

## 4. The negative result, quantified

At depth `n = 140`, over a complete enumeration of the confined integers below
`2^36`, with the L1/L2 chain correlation removed and error bars from a word-level
bootstrap:

* the aggregate letter law is the exact confined-ensemble law to
  `1.1 x 10^-4` in `P(a = 1)`;
* no word statistic correlates with `log2 m` beyond `|rho| = 0.011 ± 0.004`;
* no word statistic correlates with `delta` beyond `|rho| = 0.023` at `4 SE = 0.028`;
* the 1 %-smallest-realizer words differ from generic words by less than
  `0.18 sd` in every statistic, at matched `S`;
* no envelope, no forbidden region: the apparent per-bin extremes track
  `log2 K_bin + 0.833`, the i.i.d. extreme-value prediction.

**Any finite-height law for `3x+1` must live below those levels, or in the part of
the `(S, delta)` plane no computation reaches.**

---

## 5. Why no computation reaches it (`figures/fig3_reach.png`)

This is the sharpest structural thing the run produced, and it is quantitative.

The frontier is at deficit
```
   delta_frontier(n) = S_n + 1 - log2 r_min(n,0)  ~  (alpha - I_0) n  =  1.5056 n ,
```
`1.585 - 0.0793`, since `log2 r_min ~ I_0 n` while `S_n ~ alpha n`. At `n = 200`
that is `delta ~ 291`. A sample of `K` words reaches only `delta ~ log2 K`: at
`K = 2 x 10^4`, `delta ~ 14`. **To reach the frontier by sampling one needs
`~2^{1.5 n}` words**, and a complete enumeration to `2^B` reaches only
`delta ~ alpha n - B`.

So the `(S, delta)` law is measured to be exactly uniform in the bulk
(`delta <~ 14`, by sampling) and exactly consistent with uniform as a *count* in
the far tail (`delta ~ 100-300`, by complete enumeration, `E_B(n)` within a few
sigma). The open problem lives at `delta` linear in `n`, between and beyond both.
That is a precise form of the programme's "the population is known, the placement
is not", and it explains why the record-holder audit had 24 points and could not
have had many more.

---

## 6. A defect in a published control dataset — the `5x-1` record ladder

Found because this project had to reproduce the controls.

`audits/cross_map/scripts/scan_rare.c` sieves the scan to the first-letter class.

**Root cause, exactly.** For `q < 4` the rare-side condition at `n = 1` is
`S_1 <= A[1] = 1`, which with `a >= 1` pins `a_0 = 1` — so the sieve
(`m == 3 (mod 4)` for `3x+1`) is **exact**, and the `3x+1` ladder is correct.
For `q > 4` the condition is `S_1 >= A[1]+1`, a **lower** bound: `d0 = 3` is only
the smallest admissible first letter. The code's comment — *"larger first letters
live in sub-classes of the same modulus"* — is false. Seeds with `v2(5m-1) = 4`
satisfy `5m == 17 (mod 32)`, i.e. `m == 29 (mod 32)`, i.e. `m == 13 (mod 16)`:
a **different** class mod 16, not a sub-class of `5 (mod 16)`. Stepping by 16 from
`m = 5` therefore never visits them.

Complete scan of every odd `m < 2^32` (this project, cross-checked against an
independent pure-Python exact recomputation below `2 x 10^5`, identical):

* **74** distinct record holders to `N = 366`; **53 of them are `== 13 (mod 16)`**;
* the smallest counterexample is `N = 2`: the true `r_min(2) = 13`, while
  `../cross_map/data/delta1_D.txt` records `21`. `5 . 13 - 1 = 64`, so `S_1 = 6 >= 3` and
  `13` is rare-side persistent for 12 steps;
* further disagreements: true `r_min(16) = 45` (published `533`),
  `r_min(22) = 77`, `r_min(25) = 269`, `r_min(32) = 397` (published `789`).

**What this does and does not affect.**

* **Refuted as stated:** Open Problem 11 of *After the Reduction* — "is
  `r_min(N) == 5 (mod 16)` for every `N`?" — is **false**, at `N = 2`. The
  companion observation that "the class 13 is admissible yet never least" is an
  artefact of the sieve.
* **Needs recomputation:** Remark "the same null on `5x-1`" — the 66 holders,
  `Delta_1 > 0` at 66 of 66, and the slope `+0.0211`. On the corrected complete
  ladder (`m < 2^32`): **74 holders, `Delta_1 > 0` at 73 of 74** (the exception is
  `N = 13`, `Delta_1 = -0.396`), least-squares slope **`+0.0196`** per unit `N`.
  The qualitative reading — `Delta_1` positive and growing, unlike `3x+1` —
  **survives**; the numbers do not. (Ranges differ: the published scan covers
  `m < 10^12`, 233× larger, so the holder counts are not directly comparable. The
  `p_N` values agree with the published ones exactly at every `N` checked.)
* **Unaffected: `3x+1`, and provably so** — for `q < 4` the sieve is exact (see
  the root cause above). This project's independent scan, which sieves nothing,
  reproduces `data/delta1_A.txt` **entry for entry**: 23 record holders,
  `3, 7, 27, 703, 10087, 35655, 270271, 362343, 381727, 626331, 1027431, 1126015,
  8088063, 13421671, 20638335, 26716671, 56924955, 63728127, 217740015,
  1200991791, 1827397567, 2788008987, 12235060455`, the last at `N = 282`.
  Also unaffected: every Lean theorem; Proposition `5x-1` itself, which is a proof
  and not a scan; and everything on the divergence side. `7x-1` and any other
  `q > 4` map scanned with the same program would carry the same defect.

The fix is small — the admissible seeds for `q > 4` are one class modulo `2^{d0}`,
not modulo `2^{d0+1}` — and it has been applied, together with a regression test
and a rescan of the full published range; see
[`../cross_map/CORRECTION_2026-09-25.md`](../cross_map/CORRECTION_2026-09-25.md),
which supersedes the `m < 2^32` figures quoted above with the `m < 10^12` ones.

---

## 7. Limitations, stated plainly

* The frontier cannot be improved here. The repository already scanned every odd
  `m == 3 (mod 4)` below `10^12`; this project scanned to `2^36` for `3x+1`.
  §5 says why more scanning does not help.
* Word sampling resolves `P(delta > t)` only to `t <~ 14`; the far tail is reached
  only as a *count*, never as a feature test.
* The upper-side word mass for `q > 4` is computed with an explicit truncation
  and a certified bound on the omitted mass (`< 7 x 10^-10` relative at `n = 60`).
* All null results are bounds on effect size, not proofs of exact independence.
  The right reading of §4 is "any effect is smaller than these numbers", not
  "there is no effect".
* The 27 word statistics are the interpretable ones named in the brief. A law
  living in some statistic outside that list would not have been seen — though
  M7/M8 close off the whole letter-law channel, and M4 closes off *every*
  statistic simultaneously by showing the two cohorts have the same word
  distribution.

---

## 8. Recommendation

**Do not push anything into either repository on the strength of the search
itself.** The search is a clean negative and belongs where it is.

One item does deserve action, independently of this experiment:

> **The `5x-1` control scan should be rerun without the first-letter sieve**, and
> Open Problem 11 and the `5x-1` half of Remark "the same null on `5x-1`" corrected.

**That recommendation has been carried out**; see
[`../cross_map/CORRECTION_2026-09-25.md`](../cross_map/CORRECTION_2026-09-25.md).

If the negative result is thought worth recording, the two statements that would
carry it are §4 (the quantified null, with the exact letter law as the null) and
§5 (the `delta ~ 1.5n` frontier against the `log2 K` sampling reach) — the second
being the one that explains why the first was always going to be the answer.
