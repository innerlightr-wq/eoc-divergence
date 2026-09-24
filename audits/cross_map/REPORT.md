# Cross-map study: the strongest parts of the programme through `3x±1` and `5x±1`

**Exploratory. No claim of progress toward the Collatz conjecture.**
Labels: **PROVED** (proof written out, here or in a cited source) · **CITED** ·
**VERIFIED** (exact computation, stated range) · **HEURISTIC** · **OPEN**.

Phase 0 is in [`PHASE0.md`](PHASE0.md), committed before Phase 1. Raw outputs are in
[`data/`](data/); programs in [`scripts/`](scripts/). Every decision is made in exact arithmetic
(Python integers / `Fraction`, or C `unsigned __int128` behind a `2^100` guard); floating point
appears only in reported averages and fits.

## The maps

```
A: x ↦ (3x+1)/2^{v₂(3x+1)}      B: x ↦ (3x−1)/2^{v₂(3x−1)}
C: x ↦ (5x+1)/2^{v₂(5x+1)}      D: x ↦ (5x−1)/2^{v₂(5x−1)}
```

`α = log₂q`, `S_n = Σ_{k<n} a_k`, `R_n = S_n − nα`. The **rare side** is `R_n ≤ 0` when `q < 4` and
`R_n ≥ 0` when `q > 4`. **Sign alignment** (`audits/fingerprint_comparison` §6, **PROVED**): a
positive cycle satisfies `sign(S/L − α) = sign(r)`, so it shelters on the rare side iff
`sign(r) = sign(q − 4)`. `A` and `D` are the non-degenerate cases; `B` and `C` are the controls.

---

# Phase 0 result, in one line

**P0 is PROVED**: no positive odd integer persists forever on the rare side of `D = 5x−1`. The
proposed proof holds, every step checked. **P0′ needed one correction**: pigeonhole is available when
`r < 0` **and** `q > 4`, not merely when `q > 4` — for `r > 0` the carry enters `(†)` with the wrong
sign and boundedness is not forced. The classification is unchanged, because for `q > 4, r > 0` a
cycle already shelters. Details, including the `3x+5` and `7x±1` checks and the literature note for
P0″, are in `PHASE0.md`.

---

# Phase 1 — the item × map table

| # | item | **A** `3x+1` | **B** `3x−1` | **C** `5x+1` | **D** `5x−1` |
|---|---|---|---|---|---|
| 1 | divergence reduction | **holds**, an equivalence (**CITED**, Lean) | **fails** at `cycle_drift` | not the right pairing | **degenerates**: the right-hand side is provably empty (P0) |
| 2 | rare-side rate `I(q)` | `0.0793186128` (**CITED**, formalized) | same as A (**PROVED**, `r`-free) | `0.0323008158` | same as C (**PROVED**) |
| 3 | record ladder vs the mass | `Δ₁` flat, slope `−0.003`, CI contains 0 (**VERIFIED**, reproducing the published audit) | degenerate, `r_min ≡ 1` | degenerate, `r_min ≡ 3` | **`Δ₁` grows**, slope `+0.021`, CI excludes 0 (**VERIFIED**) |
| 4 | signed marker | rare-side periodic points **negative** | **positive** | **positive** | **negative** |
| 5 | descent L1 (well-ordering) | **holds**, step decreases | holds, but backward fixed point at `+1` | **fails**: step increases | **fails**: step increases |
| 5 | descent L2 (chain length) | `v₃(m+1)` | `v₃(m−1)` | `v₅(3m+1)` | `v₅(3m−1)` — all **PROVED**, **VERIFIED** |
| 5 | descent L4 (residue law) | `≡ 3, 7 (mod 12)` (**CITED**, formalized) | vacuous | vacuous | `≡ 5 (mod 16)` at every `N ≤ 459` (**VERIFIED**, not proved) |
| 6 | Sturmian irrationality | **holds** (**CITED**) | same constant as A | **holds**, same proof | same constant as C, up to `Ξ↑ = 2Ξ↓ − 1/q` |

---

## Item 1 — the divergence reduction

For **A**, `Divergence.divergent_iff_zeroConfined` is an equivalence (**CITED**, machine-checked).
Its two halves use different inputs:

* *persistent ⇒ divergent* uses `cycle_drift`: a cycle of `A` has `S/L > α`, so a zero-confined
  orbit cannot repeat a value, hence is injective, hence (with the windowed sparsity theorem)
  unbounded.
* *divergent ⇒ persistent seed* uses the last-maximum argument, which needs the error term
  `E_n = Σ log₂(1 + r/(q m_k))` to be `O(1)` — that is Curry's summability `Σ 1/m_n < ∞`, available
  precisely because a divergent orbit has large values.

**B.** The first half **fails, exactly at `cycle_drift`**: `B`'s cycles have `S/L < α`, so a
persistent orbit *may* repeat, and `m = 1` does. The right-hand side of the equivalence is therefore
true while a divergent `B`-orbit is not known, so no equivalence survives. The failure is the sign
alignment, in the form the fingerprint audit isolated.

**C, D.** For `q > 4` the rare side is the *shrinking* side, so the anomaly paired with the rare side
is **non**-divergence, not divergence. A caveat that matters and is easy to miss: **`R_n` bounded is
not equivalent to the orbit being bounded** once the orbit takes small values. `D`'s fixed point
`m = 1` has word `[2]^∞`, hence `R_n = −0.3219…·n → −∞`, while the orbit is bounded — the error term
`E_n = n·log₂(4/5)` cancels `R_n` exactly. This is why the Phase-0 proof runs through the exact
identity `(†)` and never through `R_n`.

**Does the reduction become a theorem for `D` by P0?** No. P0 makes the right-hand side ("there is a
persistent positive seed") provably **false**, so an equivalence would prove the left-hand side
false — but the natural left-hand side for `q > 4` is non-divergence, which is *not* implied: a
bounded orbit need not persist (`m = 1` again). What P0 gives is the one-way chain
`persistent ⇒ bounded ⇒ eventually periodic ⇒ contradiction`, which is the theorem itself and settles
nothing further about `D`'s divergence. That open question is P0″.

## Item 2 — the rare-side rate (`data/rates.txt`)

In parity coordinates the rare side is a constraint on the ones-density at the critical value
`β = 1/α = log_q 2`, and the letters are i.i.d. under Haar (`audits/fingerprint_comparison`
PHASE0 F1), so Sanov gives `D(β‖½) = 1 − H₂(β)` bits per parity symbol; a length-`N` accelerated
word carries `≈ αN` parity symbols, hence per accelerated step

```
I(q) = α · D(β‖½) = D(β‖½)/β = α(1 − H₂(1/α)) .
```

**`r` does not appear**, so `A` and `B` share a rate and `C` and `D` share one. **PROVED** (as a
derivation of the known `q = 3` form; `I(3)` itself is `Occupation.confined_mass_rate`, **CITED**).

| `q` | `α` | `β = 1/α` | `D(β‖½)` | `I(q) = D/β` | measured slope at `N = 400→500`, minus `1.5·Δlog₂N` |
|---|---|---|---|---|---|
| 3 | 1.5849625007 | 0.6309297536 | 0.0500444728 | **0.0793186128** | 0.07893803 |
| 5 | 2.3219280949 | 0.4306765581 | 0.0139112042 | **0.0323008158** | 0.03184132 |
| 7 | 2.8073549221 | 0.3562071871 | 0.0605102383 | **0.1698737154** | 0.16996176 |

**VERIFIED** by the exact integer prefix-sum transfer recursion to `N = 500`. Three checks on the
recursion itself:

* **Word counts.** Against a direct DFS enumeration of the admissible words, exact agreement at
  `N = 4, 6, 8` for `q = 3, 5, 7`, both sides (`data/check_words.txt`).
* **Integer counts.** Terras–Everett predicts `#{odd m < 2^{K+1} : N-persistent} = 2^K p_N`. On the
  **lower** side every admissible word has `S ≤ A[N] ≤ K`, and the identity holds exactly
  (`data/check_mass.txt`: `4, 19, 226` at `N = 3, 5, 7`). On the **upper** side `S` is unbounded, so
  words with `S > K` contribute at most one integer each below `2^{K+1}` and the truncated prediction
  under-counts by exactly that tail — which is what `data/check_mass.txt` shows, and is not an error
  in the recursion.
* **Truncation.** `log₂(1/p_N)` agrees to ten decimals for slack `150 / 300 / 600` at
  `N = 100, 200, 300`.

## Item 3 — `D`'s record ladder against the exact mass (`data/delta1_D.txt`)

The scan covers **every odd `m < 10^12`** in the class `m ≡ 5 (mod 16)` forced by the first letter,
8 workers, exact `__int128`. Result: **66 distinct record holders, depths `1 … 459`, deepest
`r_min(459) = 848 537 873 557`.** (A cross-check at `X = 5·10^7` reproduces the fingerprint audit's
`N = 264` at `39 090 837`, and the same program run on `A` reproduces the published `N = 236` at
`63 728 127`.)

Against the exact rare-side mass, `Δ₁(N) = log₂ r_min(N) − log₂(1/p_N)`:

| `N` | `r_min(N)` | `log₂ r_min` | `log₂(1/p_N)` | `Δ₁` |
|---|---|---|---|---|
| 16 | 533 | 9.0580 | 5.1518 | 3.9062 |
| 100 | 284 501 | 18.1181 | 10.6098 | **7.5083** |
| 237 | 39 090 837 | 25.2203 | 16.6008 | **8.6195** |
| 401 | 39 980 551 349 | 35.2186 | 22.9288 | **12.2897** |
| 454 | 848 537 873 557 | 39.6262 | 24.8835 | **14.7427** |

* `Δ₁ > 0` at **66 of 66** holders — the same sign as `A`'s published 24 of 24.
* But it **grows**: OLS slope `+0.021080`, Theil–Sen `+0.021928`, block-bootstrap 95 % CI
  `[+0.0160, +0.0233]` (blocks of 3), `[+0.0118, +0.0234]` (blocks of 8), `[+0.0084, +0.0253]`
  (blocks of 16) — bounded away from zero at every block size.
* Implied growth exponent `I(5) + slope = 0.0534`, against the null `I(5) = 0.0323`.
* Serial correlation is severe: `ρ₁ = +0.90`, `n_eff = n(1−ρ)/(1+ρ) = 3.4`. **The bootstrap
  intervals should not be read as if there were 66 independent observations.**

### The control: the same pipeline on `A` (`data/delta1_A.txt`)

The measurement above is only as good as the instrument, so the identical scan, the identical mass
recursion and the identical fit were run on `A` over every odd `m < 2·10^{11}`:

| | **A** `3x+1` (lower side) | **D** `5x−1` (upper side) |
|---|---|---|
| scan range | `m < 2·10^{11}` | `m < 10^{12}` |
| distinct holders | **23**, depths `1…344`, deepest `r_min(344) = 12 235 060 455` | **66**, depths `1…459`, deepest `r_min(459) = 848 537 873 557` |
| `Δ₁ > 0` | 23 of 23 | 66 of 66 |
| `Δ₁` range (median) | `0.33 … 4.72` (**2.72**); `2.19` at `N = 282` | `1.98 … 14.74` (**8.55**) |
| OLS slope | **`−0.003328`** | **`+0.021080`** |
| Theil–Sen slope | `−0.004322` | `+0.021928` |
| bootstrap 95 % CI (blocks 3 / 8 / 16) | `[−0.019, +0.008]` / `[−0.024, +0.019]` / `[−0.017, +0.009]` — **contains 0 throughout** | `[+0.016, +0.023]` / `[+0.012, +0.023]` / `[+0.008, +0.025]` — **excludes 0 throughout** |
| implied growth exponent | `0.0760` (null `I(3) = 0.0793`) | `0.0534` (null `I(5) = 0.0323`) |
| `ρ₁`, `n_eff` | `+0.571`, `6.3` | `+0.901`, `3.4` |

The `A` column reproduces `audits/record_holder_anatomy` independently: 23 holders where the deeper
scan finds 24, `Δ₁ = 2.19` bits at `N = 282` against the published `1.9–2.5`, a growth exponent of
`0.0760` against the published `0.0737`, and `n_eff = 6.3` against the published `≈ 7`. The
instrument is therefore calibrated, and the contrast in the slope row is measured, not assumed.

**This is the one place where a map departs from the null that `A` satisfies.** The null model is the
same, the mass is exact and independently validated (item 2), and the pipeline reproduces `A`'s
published numbers — so the departure is in the placement of the integers, not in the counting.

**What it means, given P0.** For `D`, `r_min(N) → ∞` is a **theorem** (P0: if `r_min` were bounded
along a subsequence, a single integer would be `N`-persistent for arbitrarily large `N`, hence
persistent, which P0 forbids). So `D` is the reverse of `A`: the qualitative statement is settled and
only the rate is open. That makes the growing `Δ₁` a statement about *how far beyond the density the
frontier sits*, with no conjectural content attached.

**A structural reason, HEURISTIC.** For `D` the rare side is the shrinking side, so by step (1) of P0
a persistent seed's whole orbit is trapped in `[1, m₀]`. The word a small seed can realize is
therefore not free: the orbit must fit inside the interval below the seed. The null model counts
words with their dyadic densities and has no such constraint, so it should under-predict `r_min`, and
increasingly with `N`. `A` has no analogue of this constraint — its rare side is the growth side, and
a confined orbit is unbounded. This is offered as a mechanism, not a proof; the `n_eff ≈ 3.4` caveat
applies to the measurement it explains.

## Item 4 — the signed marker, as one statement (`data/markers.txt`)

A purely periodic point with word of length `L` and total `S` is `m = r·C_L/(2^S − q^L)` with
`C_L > 0`. On the rare side the denominator's sign is fixed, giving

```
sign(m) = sign(r) · sign(q − 4) .
```

So **rare-side periodic points are negative exactly when no cycle shelters** — that is, exactly for
`A` and `D`. The signed marker and the sign-alignment criterion are the same statement. **PROVED.**

**VERIFIED** by enumeration of the rare-side periodic words (`data/markers.txt`):

| map | rare-side periodic words, period `≤ 10` | sign |
|---|---|---|
| A | 1750 (→ **1717 distinct points**, matching `audits/record_holder_anatomy`) | all **negative** |
| B | 1750 | all **positive** |
| C | 3 611 208 (capped at `S ≤ A[L]+5`; the upper side bounds `S` only from below) | all **positive** |
| D | 3 611 208 (same cap) | all **negative** |

The conjugacies `A(−x) = −B(x)` and `D(−x) = −C(x)` are **VERIFIED** with 0 violations on every odd
`|x| < 2^14`. So Theorem 7.2's construction — two systems agreeing on the aggregate identity, the
confinement condition and the `S_k` combinatorics, disagreeing on the positive-side answer — has an
exact twin in the pair `(D, C)`.

> **And that is the point.** Theorem 7.2's obstruction applies verbatim to `(D, C)`. Yet `D` **is**
> settled, by P0. So Theorem 7.2 is not what makes `A` hard. P0 escapes it by using the archimedean
> **magnitude** (`m_n < m₀`) and well-ordering — Criterion 7.1(ii) and (iii) — while using no 2-adic
> integrality at unbounded depth at all, i.e. failing (i). For `D` that is enough, because the rare
> side is the shrinking side. For `A` it is not available, and (i) becomes unavoidable.

## Item 5 — the descent lemmas (`data/descent.txt`, `data/residues_D.txt`)

**L2 generalizes exactly.** The `a = 1` backward step is `p = (2m − r)/q`; seeking `c` with
`p + c = (2/q)(m + c)` gives `c = r/(q−2)`, hence the integral identity

```
q^j · ( (q−2)·back^j(m) + r )  =  2^j · ( (q−2)m + r ) ,
```

so the `a = 1` backward chain has length exactly `v_q((q−2)m + r)`. **PROVED.**
**VERIFIED** on every odd `m < 2·10^5`, 0 mismatches, for all four maps:
`A: v₃(m+1)`, `B: v₃(m−1)`, `C: v₅(3m+1)`, `D: v₅(3m−1)`. The single degenerate case is
`(q−2)m + r = 0`, i.e. the backward fixed point `m = −r/(q−2)`; it is a positive integer only for
`B` (`m = 1`), which is exactly the sign-sensitivity the descent audit records.

**L1 reverses direction for `q > 4`.** Prepending a letter `a` replaces `S_k` by `a + S_{k−1}`. On
the lower side (`q < 4`) the constraint is an upper bound, `a = 1` always works, and
`p/m → 2/q = 0.667 < 1`: the step **decreases** the seed, which is what well-ordering needs. On the
upper side (`q > 4`) the constraint is a lower bound and needs
`a ≥ max_k (A[k] − A[k−1]) = ⌈α⌉ = 3`, giving `p/m → 8/5 = 1.6 > 1`: the step **increases** the seed.
**PROVED.** Two consequences: there is no well-ordering descent for `C` or `D`; and for them the
persistence-preserving move (`a ≥ 3`) is *not* the move carrying the `q`-adic chain (`a = 1`), so the
two halves of the descent machinery decouple, whereas for `A` they are the same move.

**L4 has an empirical analogue for `D`, not a proved one.** Over all `N ≤ 459`,
`r_min(N) ≡ 5 (mod 16)` without exception, and 65 of the 66 distinct holders are `≡ 21 (mod 32)`
(the exception is the first, `m = 5`). **VERIFIED**, not proved: `A`'s L4 is proved *through* L1, and
L1 is unavailable here. The residue is only partly forced — `S₁ ≥ 3` requires `m ≡ 5 (mod 8)`, which
splits into `5` and `13 (mod 16)`, and the class `13` is admissible (`m = 13` is persistent for about
nine steps) yet never least.

**L7.** The lockstep statement has no clean analogue: a forward step with the persistence-preserving
letter `a = 3` sends `3m − 1 ↦ (15m − 11)/8`, and `15m − 11 ≡ −1 (mod 5)`, so the 5-adic budget is
destroyed outright rather than advanced in lockstep. **PROVED** (one line).

## Item 6 — the Sturmian depth law and the Liouville argument (`data/sturmian.txt`)

With `Ξ = Σ_{j≥0} q^{−(j+1)} 2^{⌊jα⌋} ∈ Z₂`, `p_n/q_n` the convergents of `α = log₂q`,
`δ_n = q^{q_n} − 2^{p_n}` and `x_n = −C(X_n)/δ_n`, the depth law

```
v₂(x_n + Ξ) = p_n − 1                (upper convergent, R_n > 0)
v₂(x_n + Ξ) = p_n + p_{n+1} − 1      (lower convergent, R_n < 0)
```

is **VERIFIED** at every shell inside the modulus, for `q = 3, 5, 7`:

| `q` | shells checked | depths |
|---|---|---|
| 3 | `n = 2…7` | 10, 7, 83, 64, 568, 484 — reproducing `audits/sturmian_irrationality` exactly |
| 5 | `n = 2…7` | 201, 136, 1831, 1492, 29383, 20086 |
| 7 | `n = 2…7` | 86, 72, 1908, 1602, 15038, 8320 |

**Where `q` enters, and why it cancels. PROVED.** The wall bound is `|δ_n| ≤ q^{q_n}`; the carry bound
is `2^{s_j} ≤ 2^{j p_n/q_n} = q^j 2^{jR_n/q_n} < 2q^j`, so `C_n < 2q_n q^{q_n−1}`; hence
`|M_n| < 2H q_n q^{q_n}`. At a lower convergent `v₂(M_n) = p_n + p_{n+1} − 1`, and
`q_nα = p_n + |R_n|`, so

```
p_n + p_{n+1} − 1 < log₂(2H q_n) + q_nα = log₂(2H q_n) + p_n + |R_n|   ⟹   p_{n+1} < 2 + log₂(2H) + log₂ q_n ,
```

which fails for large `n` since `p_{n+1} > q_{n+1} > q_n → ∞`. **The base `q` cancels exactly between
the carry bound and `q_nα = p_n + |R_n|`.** The argument therefore needs only: `α` irrational (true
for every odd `q ≥ 3`, since `2^p = q^s` is impossible), infinitely many lower convergents (classical
alternation), and `q_n → ∞`. It goes through verbatim for all four maps.

For `q > 4` the extremal rare-side word is the **upper** mechanical word `s_j = ⌈jα⌉`, and since
`jα` is never an integer for `j ≥ 1`,

```
Ξ↑ = 2·Ξ↓ − 1/q ,
```

an affine relation over `Q`: one constant is irrational iff the other is. **VERIFIED** mod `2^2000`
for `q = 5` and `q = 7`. So `C` and `D` need no separate argument.

---

# New insights, stated honestly

1. **The hardness of (DE) is a two-sign condition, and `3x+1` is the unique combination that defeats
   both mechanisms.** Shelter settles a map positively when `sign(r) = sign(q−4)`; pigeonhole settles
   it negatively when `r < 0` and `q > 4`; the remaining combination — `q < 4`, `r > 0` — has
   neither, because the rare side is then the *growth* side. That is `3x+1` and `3x+5`.
   **PROVED**, and it is a synthesis of `cycle_drift` and the signed marker rather than a new
   theorem. The P0′ correction (pigeonhole needs `r < 0`, not merely `q > 4`) is new relative to the
   brief's proposed statement.
2. **Theorem 7.2 is not what makes `3x+1` hard.** Its obstruction applies verbatim to the pair
   `(D, C)`, which is conjugate to `(A, B)` by `x ↦ −x` — and yet `D` is settled by P0. P0 uses the
   archimedean magnitude and well-ordering and *no* 2-adic integrality at unbounded depth, which is
   exactly Criterion 7.1 with (i) missing. The criterion's part (i) is therefore not a formality: it
   is what the growth side forces. **PROVED.**
3. **`D`'s record frontier departs from the random-placement null, and `A`'s does not.** Measured by
   one pipeline on both maps: `A`'s `Δ₁` has slope `−0.003` with every bootstrap interval containing
   zero, `D`'s has slope `+0.021` with every interval excluding it. The pipeline reproduces `A`'s
   published `Δ₁ ≈ 2.2` bits, growth exponent `0.076` and `n_eff ≈ 6`, so the contrast is measured.
   Because P0 makes the qualitative statement a theorem for `D`, this is a clean quantitative
   question with no conjectural overhang — and the natural mechanism (a persistent `D`-orbit is
   trapped below its seed; an `A`-orbit is not) is one the null model cannot see. **VERIFIED** for
   the measurement, **HEURISTIC** for the mechanism, with `n_eff ≈ 3.4` stated.
4. **The descent machinery decouples for `q > 4`.** For `A` the backward `a = 1` step both preserves
   confinement (L1) and carries the 3-adic chain (L2). For `C` and `D` the persistence-preserving
   move is `a ≥ 3` and *increases* the seed, while the chain-carrying move is still `a = 1`; the two
   are different moves. **PROVED.**
5. **Everything else is re-derivation.** The rate `I(q) = D(β‖½)/β`, the signed marker, the Sturmian
   depth law and the Liouville argument all transfer with `q` appearing only through `α` — in the
   Liouville argument it cancels exactly. Nothing in items 2, 4 or 6 is new beyond the observation
   that the `q`-dependence is that shallow.

Nothing above bears on the Collatz conjecture, and no claim of progress toward it is made.
