# Phase 0 — exact facts, fixed before any computation

**Exploratory. No claim toward (DE) or the Collatz conjecture.**
Labels: **PROVED** (proof written out here) · **CITED** · **VERIFIED** · **HEURISTIC** · **OPEN**.

This file is committed *before* any script is written or run, so that the Phase-1 observables are
screened against facts fixed in advance rather than fitted after the fact.

## Setting

Fix an odd multiplier `q ≥ 3` and an odd shift `r`. On the odd 2-adic integers `Z₂^×` define

```
a(x) = v₂(qx + r) ≥ 1 ,        T(x) = (qx + r) / 2^{a(x)} .
```

The three maps of this study:

| | `q` | `r` | `α = log₂q` | mean drift per step `α − E[a]` |
|---|---|---|---|---|
| **A** | 3 | +1 | 1.5849625007… | **−0.4150374993…** |
| **B** | 3 | −1 | 1.5849625007… | **−0.4150374993…** |
| **C** | 5 | +1 | 2.3219280949… | **+0.3219280949…** |

Write `m_k = T^k(m_0)`, `a_k = a(m_k)`, `S_n = Σ_{k<n} a_k`, and the **drift** `R_n = S_n − nα`.
The one-step identity `2^{a_k}m_{k+1} = q m_k + r` gives, by induction, the **aggregate identity**

```
2^{S_n} m_n = q^n m_0 + C_n ,      C_n = r · Σ_{i<n} q^{n−1−i} 2^{S_i} .            (†)
```

so `m_n ≍ m_0 · 2^{−R_n}`: an orbit grows exactly when its drift falls. For A this is
`Divergence.aggregate_identity` (**CITED**, machine-checked); the general-`(q,r)` form is the same
induction.

---

## F1. The valuation is geometric(½) with mean 2, for all three maps. **PROVED**

> **Proposition F1.** Let `q` be odd, `r` odd, and let `x` be Haar-distributed on `Z₂^×` (normalized
> so `Z₂^×` has measure 1). Then for every `k ≥ 1`,
> ```
> P( v₂(qx + r) = k ) = 2^{−k} ,
> ```
> so `a` is geometric(½) on `{1,2,3,…}` with `E[a] = 2` and `Var(a) = 2`. The law does not depend on
> `q`, on `r`, or on the sign of `r`.

**Proof.** Multiplication by the unit `q` is a measure-preserving bijection of `Z₂^×`, so `y = qx` is
again Haar on `Z₂^×`; likewise `y ↦ −y`, so it suffices to treat `v₂(y + r)` for one odd `r`, and we
take `r = 1`. Since `y` is odd, `y + 1` is even and `v₂(y+1) ≥ 1`.

For `k ≥ 1`, `v₂(y+1) ≥ k` iff `y ≡ −1 (mod 2^k)`. The unit residues mod `2^k` are the `2^{k−1}` odd
classes, each of Haar measure `2^{−(k−1)}`, and exactly one of them is `−1`. Hence

```
P( v₂(y+1) ≥ k ) = 2^{1−k} ,     P( v₂(y+1) = k ) = 2^{1−k} − 2^{−k} = 2^{−k} .
```

These sum to 1, and `E[a] = Σ_{k≥1} k2^{−k} = 2`. ∎

**Consequence F1′ (all drift cumulants but the first are map-independent). PROVED.** The per-step
drift increment is `Δ = α − a`. For geometric(½) on `{1,2,…}`: `E[a] = 2`, `Var = 2`, third central
moment `6`, fourth central moment `38`. Therefore, exactly and for **all three maps**,

```
E[Δ] = α − 2 ,   Var(Δ) = 2 ,   skew(Δ) = −3/√2 = −2.1213203… ,   exkurt(Δ) = +13/2 .
```

Only the **mean** distinguishes the maps, and it does so by exactly `log₂q`. Every higher cumulant,
and hence every Edgeworth correction to the normalized drift distribution, is identical for A, B and
C. This is a pre-registered prediction for observable **O1**.

---

## F2. `x ↦ −x` conjugates A to B on `Z₂`. **PROVED**

> **Proposition F2.** For odd `x`, `v₂(3(−x)+1) = v₂(3x−1)` and `A(−x) = −B(x)`. Hence
> `A ∘ (−1) = (−1) ∘ B` on `Z₂^×`, the two maps have identical valuation words, identical `S_k`,
> identical drift `R_n` and identical confinement, and — since `x ↦ −x` preserves Haar measure on
> `Z₂^×` — **every Haar-population statistic of A equals that of B exactly.**

**Proof.** `3(−x)+1 = −(3x−1)`, and `v₂` is insensitive to sign, giving the first claim. Then
`A(−x) = (3(−x)+1)/2^{v₂(3x−1)} = −(3x−1)/2^{v₂(3x−1)} = −B(x)`. Negation is an isometric bijection of
`Z₂^×` carrying Haar to Haar. ∎

**Consequence F2′.** The positive odd integers under **B** are, orbit for orbit, the negative odd
integers under **A**. Any difference between the A- and B-populations of *positive integers* is
therefore, by definition, a **sign** effect in A. This is the channel of question Q3.

**Consequence F2″ (what the conjugacy does *not* do).** It is sign-*reversing*, not sign-preserving:
it says A and B agree on everything the sign does not touch, and it is exactly why the two disagree
where the sign does touch — the synthesis note's sign obstruction (**CITED**, `papers/synthesis`,
Thm. 7.2). The same conjugacy sends `+1` (a B-fixed point) to `−1` (an A-fixed point).

---

## F3. Terras–Everett residue correspondence, for each map. **PROVED**

> **Proposition F3.** Fix odd `q` and odd `r`. Let `D = (d_0,…,d_{n−1}) ∈ Z_{≥1}^n` with
> `S_k = Σ_{i<k} d_i` and `S = S_n`. Then
> ```
> { x ∈ Z₂^× : a(T^i x) = d_i for all i < n }
> ```
> is **exactly one residue class modulo `2^{S+1}`**, consisting of odd residues, of Haar measure
> `2^{−S}`. Equivalently: the odd integers realizing `D` form exactly one class mod `2^{S+1}`.

**Proof.** Induction on `n`. For `n = 1`: `a(x) = d` iff `qx + r ≡ 2^d (mod 2^{d+1})` iff
`x ≡ q^{−1}(2^d − r) (mod 2^{d+1})`, using that `q` is a unit mod `2^{d+1}`. The class is odd because
`2^d − r` is odd (`d ≥ 1`, `r` odd) and `q^{−1}` is odd; there are `2^d` odd classes mod `2^{d+1}`, so
the measure is `2^{−d}`.

Inductive step. Suppose the first `k` letters pin `x` to a class `x ≡ x₀ (mod 2^{S_k+1})`, i.e.
`x = x₀ + 2^{S_k+1} t` with `t ∈ Z₂` Haar. By `(†)`, `T^k(x) = (q^k x + C_k)/2^{S_k}`, hence

```
T^k(x) = y₀ + 2 q^k t ,      y₀ = (q^k x₀ + C_k)/2^{S_k} odd.
```

Since `q^k` is a unit, `t ↦ y₀ + 2q^k t` is a measure-preserving bijection from `Z₂` onto the odd
2-adics, so `y = T^k(x)` is Haar on `Z₂^×` and **independent of the first `k` letters**. Applying the
`n = 1` case to `y`: `a(y) = d_k` pins `y` to one class mod `2^{d_k+1}`, hence `t` to one class mod
`2^{d_k}`, hence `x` to one class mod `2^{S_k+1+d_k} = 2^{S_{k+1}+1}`, of measure `2^{−S_{k+1}}`. ∎

**Instances.** `(q,r) = (3,+1)` is the accelerated form of Terras (1976) and Everett (1977)
(**CITED**); `(3,−1)` and `(5,+1)` are the same statement with the same proof, which is why it is
proved here in general rather than quoted three times. The proof also re-derives F1 (the case
`n = 1`) and shows the letters `a_0, a_1, …` are **i.i.d.** geometric(½) under Haar.

### Consequence C1 (the exactness window). **PROVED**

Let `X ≥ 2` and let `N_odd(X)` be the odd integers in `[1, X]`. For any event `E` depending only on
the first `n` letters, with total `S` over the words in `E`,

```
| #{x ∈ N_odd(X) : x ∈ E} / #N_odd(X)  −  P_Haar(E) |  ≤  |E|·2^{S+1}/X  ,
```

because each word of total `S` occupies exactly one class mod `2^{S+1}`, so it is hit
`X/2^{S+2} + O(1)` times. **Up to depth `S ≲ log₂X` the integer population is exactly the Haar
population**, and the deviation is a boundary term, not a structural one.

### Consequence C2 (where differences may live). **PROVED**

- **A versus B.** By F2 their Haar fingerprints are *identical*, not merely similar. By C1 their
  positive-integer fingerprints are also identical for every statistic determined by the first
  `S ≲ log₂X` levels of valuation. **Any A-vs-B difference in the positive integers must therefore
  originate at depth beyond `≈ log₂X`** — which is exactly the regime in which an orbit has exhausted
  the seed's bit budget and is captured by a cycle (or, hypothetically, is not).
- **A versus C.** They differ already at `n = 1`, in the mean drift alone: `log₂5 − log₂3 =
  log₂(5/3) = 0.7369655942…`. By F1′ no other cumulant differs. Any A-vs-C difference that is *not* a
  consequence of the mean drift is therefore not predicted by Phase 0 and must be flagged.

### Consequence C3 (a pre-registered null for confinement). **PROVED**

Zero-confinement is `R_n ≤ 0` for all `n ≤ N`, i.e. `S_n ≤ nα`. Under Haar the letters are i.i.d.
with mean 2, so `R_n` is a random walk with drift `α − 2`:

- for **A** and **B** (`α = 1.585 < 2`) the drift of `R_n` is `+0.415`, so `R_n ≤ 0` for all `n` is a
  **large deviation**: `p_N(0) → 0` exponentially, at the rate `I₀ = α(1 − H₂(1/α)) = 0.0793186…`
  (**CITED**, `Occupation.confined_mass_rate`, formalized);
- for **C** (`α = 2.322 > 2`) the drift of `R_n` is `−0.322`, so `R_n ≤ 0` is the **typical**
  behaviour and `p_N(0)` decreases to a **strictly positive constant**. For C the rare event is the
  opposite one, `R_n ≥ 0` for all `n`.

So the confinement observable **O2** is not the same kind of object for C as for A/B, and the two
must not be compared by their rates without saying so. Pre-registered: `p_N^C(0) ↓ c > 0`, and the
rate formula `α(1 − H₂(1/α))`, being one-sided, does **not** apply at `α > 2`.

---

## What Phase 0 already answers, before any computation

| question | Phase-0 answer | status |
|---|---|---|
| Q1 (A vs C at Haar level) | Only the mean drift differs, by exactly `log₂(5/3)`. Variance 2, skewness `−3/√2`, excess kurtosis `13/2` and all Edgeworth corrections are identical. | **PROVED** (F1, F1′) |
| Q2 (A vs B at Haar level) | Identical, exactly, for every statistic. | **PROVED** (F2) |
| Q3 (the sign channel) | Any positive-integer A-vs-B difference lives at depth `> ≈ log₂X`. | **PROVED** (F2, F3, C1, C2) |
| Q4 (C as positive-drift control) | C's confinement is a positive-probability event, not a large deviation; its escape is the rare event. | **PROVED** (C3) |

Phase 1 measures these, looks for anything **not** on this list, and classifies every regularity as
**aggregation** / **selection** / **genuine** / **explained** before interpreting it, per the
decision procedure of *Two Normalization Nulls* (**CITED**; `sources/two_normalization_nulls.pdf`,
untracked).
