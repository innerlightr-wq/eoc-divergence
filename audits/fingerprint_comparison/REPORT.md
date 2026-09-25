# Comparative fingerprint study: `3x+1`, `3x−1`, `5x+1`

**Exploratory. No claim toward the Collatz conjecture or toward (DE).**
Labels: **PROVED** (proof written out, here or in a cited source) · **CITED** ·
**VERIFIED** (exact computation, stated range) · **HEURISTIC** · **OPEN**.

Phase 0 is in [`PHASE0.md`](PHASE0.md), committed before any script was written.
Raw outputs are in [`data/`](data/); every program is in [`scripts/`](scripts/).
All arithmetic that reaches a decision is exact (Python integers/`Fraction`, or C
`unsigned __int128` with a `2^100` guard); floating point appears only in reported
averages.

## The maps

| | map | `α = log₂q` | mean drift per step `α − E[a]` | rare side of the drift line |
|---|---|---|---|---|
| **A** | `x ↦ (3x+1)/2^{v₂(3x+1)}` | 1.5849625007… | **−0.4150374993…** | below (`R_n ≤ 0`) |
| **B** | `x ↦ (3x−1)/2^{v₂(3x−1)}` | 1.5849625007… | **−0.4150374993…** | below (`R_n ≤ 0`) |
| **C** | `x ↦ (5x+1)/2^{v₂(5x+1)}` | 2.3219280949… | **+0.3219280949…** | above (`R_n ≥ 0`) |

`R_n = S_n − nα` is the drift, `S_n` the cumulative valuation. A fourth map,
**D** = `5x−1`, is added in §6 as a *control on the explanation*, not as a fourth subject.

---

# 1. Phase 0, verified

`PHASE0.md` proves, before any computation:

- **F1** — for odd `q` and odd `r`, `v₂(qx+r)` is geometric(½) on `{1,2,…}` with mean 2 under
  Haar measure on `Z₂^×`, **independently of `q`, of `r`, and of the sign of `r`**. **PROVED**
- **F1′** — hence the per-step drift `Δ = α − a` has, for **all three maps**, variance `2`,
  skewness `−3/√2`, excess kurtosis `13/2`; only the mean differs, by exactly `log₂q`. **PROVED**
- **F2** — `x ↦ −x` conjugates A to B on `Z₂^×`, so every Haar statistic of A equals that of B
  *exactly*, and the positive integers of B are the negative integers of A. **PROVED**
- **F3** — the Terras–Everett correspondence for general odd `(q,r)`: a word `D` of total `S` is
  realized by exactly one residue class mod `2^{S+1}`; the letters are i.i.d. geometric under
  Haar. **PROVED**
- **C1/C2/C3** — the exactness window `S ≲ log₂X`; A-vs-B differences among positive integers must
  live beyond it; A-vs-C differences not implied by the mean drift are unpredicted; and C's
  confinement is a positive-probability event, so the one-sided rate formula does not apply to it.

**VERIFIED** (`scripts/phase0_verify.py`, `data/phase0_verify.txt`), in exact arithmetic:

| check | result |
|---|---|
| F1 over every odd residue mod `2^20`, all three maps | `P(a=k) = 2^{−k}` **exactly** for `1 ≤ k < 19`; identical for A, B, C |
| F3 for all `4`-letter words with letters `≤ 4`, mod `2^18` | 256 words each; **0 violations** of the exact count `2^{m−1−S}` |
| F2 on every odd `\|x\| < 2^14` | `A(−x) = −B(x)` and equal valuations; **0 violations** |

---

# 2. O1 — drift

## 2.1 Haar, exact (`data/o1_drift.txt`)

Because the letters are i.i.d. geometric(½) regardless of `q`, the law of `S_N` **does not involve
`q` at all**: `P(S_N = s) = \binom{s−1}{N−1}2^{−s}`. The normalized drift
`Z_N = (2N − S_N)/\sqrt{2N}` is therefore *the same random variable* for A, B and C, and one table
serves all three.

| | mean | variance | skewness | excess kurtosis |
|---|---|---|---|---|
| **A** | `−0.4150374993` | 2 | `−2.1213203436` | `+6.5` |
| **B** | `−0.4150374993` | 2 | `−2.1213203436` | `+6.5` |
| **C** | `+0.3219280949` | 2 | `−2.1213203436` | `+6.5` |

`mean(C) − mean(A) = log₂(5/3) = 0.7369655942…` **exactly**.

Finite-`N` shape (exact CDF against Gaussian and first Edgeworth correction, continuity-corrected):

| `N` | `sup\|F_N − Φ\|` | `sup\|F_N − Edgeworth₁\|` | `√N · sup\|F_N − Φ\|` |
|---|---|---|---|
| 32 | 2.491767e−02 | 2.652113e−03 | 0.140956 |
| 128 | 1.246492e−02 | 6.147563e−04 | 0.141024 |
| 512 | 6.233219e−03 | 1.486188e−04 | 0.141042 |
| 1024 | 4.407641e−03 | 7.360521e−05 | **0.141045** |

The constant is `γ₁φ(0)/6 = (3/√2)(1/√(2π))/6 = 0.1410474…` — the skewness term, and nothing else.
Correcting for it leaves `O(N^{−1})` (the last column of `Edgeworth₁` halves at each doubling).

> **Classification: aggregation (CLT null).** The deviation decays at `N^{−1/2}`, then at `N^{−1}`
> once the skewness term is removed — the signature the *Two Normalization Nulls* note assigns to
> mirage A. It carries no map-specific content, because `γ₁` is map-independent.

## 2.2 Positive integers (`data/letters_*.txt`, `data/q3_convergence.txt`)

`P(a_k = j)` over **all** odd `x < X`, with no conditioning of any kind (orbits that have reached a
cycle keep emitting that cycle's letters). At depth 1 the values are the exact geometric ones; the
pooled total-variation distance to geometric(½) over depths 1–10 at `X = 2·10^6` is
`1.4e−03` (A), `9.8e−04` (B), `1.2e−04` (C) — the boundary term of C1.

Deep behaviour, `X = 2·10^6`:

| depth | A: `P(a=1)` | A: mean `a` | B: `P(a=1)` | B: mean `a` | C: `P(a=1)` | C: mean `a` |
|---|---|---|---|---|---|---|
| 1 | 0.50000000 | 2.000000 | 0.50000000 | 1.999997 | 0.50000000 | 2.000000 |
| 20 | 0.45182700 | 1.997922 | 0.53034000 | 1.922626 | 0.49971200 | 2.002100 |
| 60 | 0.15716600 | 2.004646 | 0.70691900 | 1.438779 | 0.49951100 | 2.003770 |
| 200 | **0.00000000** | **2.000000** | 0.73694100 | 1.357721 | 0.49822629 | 2.012537 |
| 500 | 0.00000000 | 2.000000 | **0.74113700** | **1.358975** | — | — |

A collapses onto its single cycle's word `2^∞`; B onto a mixture of three cycle words; C stays at
the Haar law until orbits escape past the `2^100` guard (alive falls to 72 % by depth 200).

---

# 3. O2 — confinement (`data/o2_confinement.txt`)

Exact integer transfer recursion, `A[k] = bitlen(q^k) − 1 = ⌊k log₂q⌋`.

| | side | `p_N` behaviour | rate, measured as `local slope − 1.5·Δlog₂N/ΔN` at `N=400→500` | reference `I(α) = α(1 − H₂(1/α))` |
|---|---|---|---|---|
| **A/B** | lower (confinement) | decays | **0.0789** | **0.0793186128** |
| **A/B** | upper | `→ 0.2863154` (constant) | — | — |
| **C** | lower | `→ 0.3520516` (constant) | — | — |
| **C** | upper (anti-confinement) | decays | **0.0318** | **0.0323008158** |

A and B are identical here by F2 — this is not an approximate agreement, it is the same recursion.

Two things are worth stating precisely.

1. **The mirror is exact.** A's rare event is being *below* the line and C's is being *above* it,
   and the two rates are the **same function** `α(1−H₂(1/α))` evaluated at `log₂3` and `log₂5`.
   The `3/2·log₂N` correction fits on both sides: for A/B at `N = 200`,
   `−log₂p_N = 24.127`, against `I₀N + 1.5log₂N − 3.28 = 24.05` (the constant `−3.28` is the
   author's own **VERIFIED** value, `papers/synthesis` Prop. `prop:density`). **VERIFIED**
2. **The rate formula is one-sided.** It gives `0.0323…` at `α = log₂5`, which is the rate of C's
   *anti*-confinement; applying it to C's confinement would be wrong, since that probability tends
   to a positive constant. Phase 0 C3 pre-registered this.

> **Classification: explained (multiplier).** Every entry is a function of `α = log₂q` alone.

---

# 4. O3 — integer-orbit statistics (`data/capture_2e8.txt`)

Odd seeds `< X`, exact `__int128`, `2^100` guard, step budget 5000 (A, B) / 3000 (C).

| | A (`X=2·10^8`) | B (`X=2·10^8`) | C (`X=2·10^7`) |
|---|---|---|---|
| cycles | `{1}` | `{1}`, `{5,7}`, `{17,25,37,55,41,61,91}` | `{1,3}`, `{13,33,83}`, `{17,43,27}` |
| capture fractions | 1.000000000 | 0.326783640 / 0.324844600 / 0.348371760 | 0.001151 / 0.001828 / 0.000441 |
| escaped past `2^100` | 0 | 0 | **0.996580300** (mean 234.15 steps) |
| uncaptured & bounded | **0** | **0** | **0** |
| steps to capture | mean 64.349, sd 26.516, max 358 | mean 52.587, sd 23.501, max 302 | mean 38.240, sd 26.687, max 263 |
| mean `S`/steps | 1.994502 | 2.028496 | 2.815399 |
| `log₂(max/x)` | **mean 1.185915**, sd 1.431 | **mean 1.187167**, sd 1.432 | mean 3.466455, sd 4.151 |
| `log₂(max/x)/log₂x` | 0.045537 | 0.045589 | 0.158587 |

`uncaptured & bounded = 0` everywhere: no orbit in these ranges stayed under the guard for the whole
budget without meeting a listed cycle, so no unlisted cycle appears. **VERIFIED** over the stated
ranges only.

Two entries deserve comment.

- **The maximum excursion is the same for A and B to 0.1 %** (1.185915 vs 1.187167). It is a
  pre-capture quantity, and pre-capture the two maps are Haar-identical (F2), so agreement is what
  Phase 0 predicts. This is the strongest *null* in the study.
- **`mean S/steps` differs** (1.9945 vs 2.0285, both `≠ 2`). This is **selection**: the stopping
  time is correlated with the letters, and the correlation has opposite sign for the two maps
  because A's cycle sits above the drift line and B's below it. It is not a Haar-level difference;
  by F2 there is none.

---

# 5. O4 — extremes (`data/records_*.txt`, `data/records_2x2.txt`)

`r_min(N)` = least positive odd `m` whose orbit stays on the **rare** side for `N` steps
(confinement for A/B, anti-confinement for C). Exact scan, `X = 5·10^7`.

| map | rare-side record ladder | distinct holders | deepest reached |
|---|---|---|---|
| **A** `3x+1` | `3, 7, 27, 703, 10087, 35655, 270271, 362343, 381727, 626331, 1027431, 1126015, 8088063, 13421671, 20638335, 26716671` | **16** | `N = 187` at `26 716 671` |
| **B** `3x−1` | `1` | **1** | `N = 600` (the scan cap) at `1` |
| **C** `5x+1` | `3` | **1** | `N = 600` (the scan cap) at `3` |

An independent scan to `X = 10^8` reproduces the audit's published A-ladder exactly, reaching
`N = 236` at `63 728 127` — the same holder and depth recorded in
`audits/record_holder_anatomy`. **VERIFIED** (cross-check).

B's ladder is degenerate exactly as predicted. C's is degenerate too, which was *not* predicted in
advance and is explained in §6.

---

# 6. The mechanism behind O4: a sign-alignment criterion

The cycle data (`data/cycles.txt`) makes the pattern exact.

| map | cycle | word | `L` | `S` | `S/L` | vs `log₂q` | on the **rare** side? |
|---|---|---|---|---|---|---|---|
| A | `{1}` | `[2]` | 1 | 2 | 2.000000 | above | no |
| B | `{1}` | `[1]` | 1 | 1 | 1.000000 | below | **yes** |
| B | `{5,7}` | `[1,2]` | 2 | 3 | 1.500000 | below | **yes** |
| B | `{17,25,37,55,41,61,91}` | `[1,1,1,2,1,1,4]` | 7 | 11 | 1.571429 | below | **yes** |
| C | `{1,3}` | `[1,4]` | 2 | 5 | 2.500000 | above | **yes** |
| C | `{13,33,83}` | `[1,1,5]` | 3 | 7 | 2.333333 | above | **yes** |
| C | `{17,43,27}` | `[1,3,3]` | 3 | 7 | 2.333333 | above | **yes** |

> **Proposition (sign alignment). PROVED.** Let `q ≥ 3` be odd, `r ∈ {+1,−1}`, `α = log₂q`, and
> `T(x) = (qx+r)/2^{v₂(qx+r)}` on odd `x`. Call a seed *permanently rare-side* if its drift stays on
> the side opposite to its mean for every `n` (below the line when `α < 2`, above it when `α > 2`).
> Then
>
> 1. every **positive** cycle satisfies `sign(S/L − α) = sign(r)`;
> 2. hence a positive cycle is permanently rare-side **iff `sign(r) = sign(α − 2)`**;
> 3. when the signs agree, the least permanently rare-side positive integer **is a cycle element**,
>    so `r_min(N)` is bounded and the record ladder is degenerate;
> 4. when they disagree, no positive cycle can serve, and whether *any* positive integer is
>    permanently rare-side is the `(q,r)`-analogue of (DE).
>
> *Proof.* (1) The aggregate identity at the period gives `m(2^S − q^L) = r·C_L` with
> `C_L = Σ_{i<L} q^{L−1−i}2^{S_i} > 0`; `2^S ≠ q^L` by unique factorisation, so for `m > 0`,
> `sign(2^S − q^L) = sign(r)`, i.e. `sign(S/L − α) = sign(r)`. (2) The rare side is
> `sign(S/L − α) = sign(α − 2)`, since `E[a] = 2` (F1). (3), (4) are immediate. ∎

This is a re-derivation and generalization of two things already in the repository — the cycle-drift
theorem (`Divergence.cycle_drift`, formalized, **CITED**) and the signed marker
(`audits/record_holder_anatomy` P1/P3, **CITED**) — not a new theorem. Its use here is diagnostic:
it settles all four sign combinations at once.

| `(q, r)` | `sign(r)` | `sign(log₂q − 2)` | prediction | measured ladder, `X = 5·10^7` |
|---|---|---|---|---|
| `(3, +1)` = **A** | `+` | `−` | **disagree ⇒ non-degenerate** | **16 holders**, deepest `N=187` at `26 716 671` |
| `(3, −1)` = **B** | `−` | `−` | agree ⇒ degenerate | 1 holder, `r_min ≡ 1` |
| `(5, +1)` = **C** | `+` | `+` | agree ⇒ degenerate | 1 holder, `r_min ≡ 3` |
| `(5, −1)` = **D** | `−` | `+` | **disagree ⇒ non-degenerate** | **52 holders**, deepest `N=264` at `39 090 837` |

The fourth row is a **control on the explanation**, run after the criterion was written down: `5x−1`
was not part of the brief, and its ladder was predicted to be non-degenerate before it was computed.
It is. **VERIFIED**

> **Note added 2026-09-25.** This row's `5x−1` ladder is **correct** and needed no change:
> `records2.c` steps by 2 over every odd seed and sieves nothing. It is also, as it turns out, the
> thing that refutes the `5x−1` ladder that `audits/cross_map` published — the two disagreed from
> `N = 2` and were never compared. The corrected `cross_map` ladder restricted to `X = 5·10^7`
> reproduces these 52 holders exactly. See
> [`../cross_map/CORRECTION_2026-09-25.md`](../cross_map/CORRECTION_2026-09-25.md) §4.

---

# 7. O5 — the LIL envelope (`data/o5_lil.txt`)

For i.i.d. letters with mean 2 and variance 2, `limsup (S_n − 2n)/\sqrt{4n\ln\ln n} = 1` a.s.
Envelopes are accumulated from `n ≥ 100` (below that the normalizer is degenerate and produces a
spurious spike — an artifact, not a signal).

| population | running max | running min |
|---|---|---|
| one Haar word, `n = 10^7` | `+0.664` | `−0.763` |
| one Haar word, `n = 2·10^4` | `+1.036` | `−1.216` |
| C integer orbits, 200 seeds `< 10^9`, `n = 2·10^4` | median `+0.764`, max `+2.192` | median `−0.750`, min `−1.920` |

**A and B integer orbits cannot be measured at all**, and that is the finding. Over 20 000 random
seeds below `10^12`: A has orbit length to capture mean 93.69, median 91, max **265**; B mean 82.33,
median 78, max **259**. At `n = 265`, `\ln\ln n = 1.72` and the LIL normalizer is 42.7 — the law is
not yet meaningful. Every integer orbit of A and of B is finite, because it is captured by a cycle
in `O(log x)` steps; only C, whose drift pushes orbits away, supplies orbits long enough to probe
the envelope, and on those the envelope is Haar-like.

> **Classification: explained (drift sign).** The difference is that C's orbits are long and A's and
> B's are not, which is the sign of `α − 2`.

---

# 8. Controls (`data/controls.txt`)

| control | result |
|---|---|
| **Shuffled confined words (A).** Each record holder's confined word, shuffled 2000× (multiset, hence density and drift, preserved) | still confined to the full depth in 174/2000 (`m=27`, depth 36) down to **16/2000** (`m=63 728 127`, depth 236); **median shuffled depth 2** in every case |
| **Least realizer `r(D)` of each holder's own word**, computed by exact lifting (F3) | `r(D)` equals the holder itself for all six tested (`27, 703, 10087, 270271, 626331, 1126015`) — an independent check of both the lifting code and the record-holder property |
| **Shuffled Haar words**, all three maps | shuffled and unshuffled agree (A/B: mean depth 2.430 vs 2.545; C: 1.817 vs 1.770), as they must — this calibrates the test rather than testing the maps |

Confinement is a property of the **arrangement**, not of the letter multiset. Every regularity below
was checked against these before being interpreted.

---

# 9. Answers to the pre-registered questions

## Q1 — A versus C at the Haar level: are the differences exactly those predicted by the multiplier?

> **Yes, exactly, and the statement is stronger than "predicted by the multiplier": the multiplier
> enters only through the mean.** **PROVED** + **VERIFIED**

The letter law is `q`-free (F1), so `S_N`'s law is literally identical for the three maps; the drift
differs by the deterministic shift `α`. Variance, skewness, excess kurtosis, the whole Edgeworth
expansion, and the finite-`N` constant `0.141045` are identical. On the confinement side the two
rates are the same function `α(1−H₂(1/α))` at `log₂3` and `log₂5`, and the sides swap. **No A-vs-C
difference was found that is not a function of `α` alone.**

*Classification:* the CLT-shaped part is **aggregation**; the confinement rates are **explained**
(multiplier); nothing **genuine** remains in this comparison.

## Q2 — A versus B: identical Haar fingerprints, and every positive-integer difference attributed

**Haar: identical, exactly**, by F2 — not to within measurement, but as the same recursion and the
same random variable. Verified to 0 violations on every odd `|x| < 2^14`.

**Positive integers.** Every difference found, and its attribution (`data/attribution.txt`):

| difference | attribution |
|---|---|
| deep letter law: A `→ δ(a=2)`, B `→` mixture with `P(a=1) = 0.738`, mean `1.3615` | **(i) cycle capture.** Predicted from the exact cycle words and the measured capture weights with nothing fitted: `P(a=1) = 0.738043`, mean letter `= 1.361492`; measured at depth 500, `0.741137` and `1.358975` (residual is the cycle-phase distribution at a fixed depth) |
| letter law at fixed depth `k`, finite `X` | **(i) cycle capture**, quantitatively. With `c_k` the measured capture fraction and no free parameter, `P(a=1) = (1−c_k)/2 + c_k·P₁^{cyc}` matches to `≤ 0.009` at every one of 12 `(map, X, depth)` points, and the residual shrinks with `X` |
| capture fractions (A: 1; B: 0.3268/0.3248/0.3484) | **(i) cycle capture**, by definition |
| steps to capture (A 64.35, B 52.59) | **(i) cycle capture**: B has three attractors, two of them reachable without descending to 1 |
| `mean S`/steps (A 1.9945, B 2.0285) | **selection**: the stopping rule is correlated with the letters, with opposite sign because A's cycle is above the drift line and B's below |
| record ladder (A non-degenerate, B `≡ 1`) | **(i) cycle capture**, in its sharpest form: B's cycles lie on the rare side and A's does not (§6) |
| `log₂(max/x)` (A 1.185915, B 1.187167) | **no difference** — 0.1 %, a pre-capture quantity, Haar-identical by F2 |

> **Nothing was found that is not explained by cycle capture.** No item is flagged under (ii).

## Q3 — the sign channel: does any positive-integer statistic of A depart from Haar beyond depth `log₂X` in a way B's does not share?

> **No, on the measurements made.** **VERIFIED** over the stated ranges.

The test: hold the depth fixed and grow `X`, so that the capture fraction at that depth falls while
the Terras–Everett window grows. If a residual sign effect existed it would survive.

| `X` | A, depth 20 | B, depth 20 | A, depth 40 | B, depth 40 |
|---|---|---|---|---|
| `4.19·10^6` | 0.46246719 | 0.52333832 | 0.32589388 | 0.63289785 |
| `6.71·10^7` | 0.48703641 | 0.50814736 | 0.38677105 | 0.58580092 |
| `2.68·10^8` | **0.49279714** | **0.50452899** | 0.41255479 | 0.56605250 |

Both converge to the Haar value `0.5`, from opposite sides, at the rate of the capture fraction, and
the capture-mixture model of Q2 accounts for the gap with no free parameter. The departures are real
and they are entirely cycle capture; the opposite signs are the sign channel, and the sign channel
shows **cycles and nothing else**.

*What this does and does not say.* It is a statement about the first 40 valuations of seeds below
`2.7·10^8`. The open problem lives at depths that grow with the seed, and no finite scan reaches it;
by C1 no scan ever can, since the exactness window is `S ≲ log₂X` by construction.

## Q4 — C as a positive-drift control

| | A's confined record holders | C's escaping orbits |
|---|---|---|
| what they are | the extreme order statistic of a large-deviation event (mass `2^{−I₀N}N^{−3/2}`) | the **bulk**: 99.658 % of seeds `< 2·10^7` |
| O1 drift | one-sided by construction: `R_n ≤ 0` for all `n ≤ N` | Haar: mean `+0.322`/step, all higher cumulants Haar |
| O2 | the rare side | the typical side (mass `→ 0.352`) |
| O3 | 16 holders below `5·10^7`; the deepest reaches `N = 187` | escape past `2^100` in mean 234.1 steps; `log₂(max/x)` mean 3.466 vs A's 1.186 |
| O4 | non-degenerate ladder | *anti*-confined ladder is degenerate at `3` (§6) |
| O5 | orbits too short to probe the LIL (max 265 steps) | envelope measurable and Haar-like: median `±0.75` at `n = 2·10^4` |

The comparison is between an extreme order statistic and a bulk, which is why it is reported as a
contrast of kinds rather than of numbers. The one quantitative statement that transfers is §6: C's
rare-side ladder is degenerate for the *same* reason B's is, and A is the odd one out.

---

# 10. New insights, stated honestly

1. **The sign channel is exactly one bit, and it is `sign(r)` against `sign(log₂q − 2)`** (§6).
   This is elementary and follows from facts already in the repository, but the 2×2 form is useful:
   it says that among `3x±1` and `5x±1`, precisely `3x+1` and `5x−1` have a non-trivial
   rare-side problem, and it predicted `5x−1`'s non-degenerate ladder before that ladder was
   computed. **PROVED** + **VERIFIED**
2. **`5x−1` is the structural twin of `3x+1`** for this question — same sign misalignment, opposite
   drift. It is a possible testbed on which any proposed (DE)-style argument must also work or
   visibly fail. Recorded as a direction, **not** as a result. **OPEN**
3. **The two-sided `N^{−3/2}` correction appears on C's anti-confinement side too**, with the same
   rate formula at `α = log₂5`. This extends the shape of the *Three Scales* result to the mirror
   problem. It is the same ballot/renewal mechanism with the walk's drift reversed, so it is
   classified **explained**, not genuine — but it had not been checked before. **VERIFIED**
4. **The strongest null is the maximum excursion**: A and B agree to 0.1 % on `log₂(max/x)`, which
   is what F2 requires and what a sign effect, if any existed at the pre-capture level, would have
   broken.

Nothing in this list bears on (DE) or on the Collatz conjecture, and nothing here is offered as
progress toward either.

---

# 11. Stop rule

> *"If every A-vs-B difference is explained by cycle capture and every A-vs-C difference by the
> multiplier, record that as the result: the fingerprints differ only where the dynamics predict,
> and the sign channel shows nothing beyond cycles."*

**That is the result.** Every A-vs-B difference measured is cycle capture, quantitatively and with
no fitted parameter; every A-vs-C difference measured is a function of `α = log₂q` alone. The sign
channel shows cycles and nothing else. Phase 1 is complete and the study stops here.
