# Audit: irrationality of `Φ(s)` for EVERY Sturmian word `s`

**Verdict: PROVED.** The route I1–I4 closes. Every ingredient is either a
published theorem (I1, I2) or an elementary argument already present in the
paper in a weaker form (I3, I4).

Labels: **PROVED** (proof written out here or in a cited source) · **CITED** ·
**VERIFIED** (exact computation, stated range) · **OPEN**.

Time box: one session. Nothing in `papers/` was edited. The draft section for
the paper is [`DRAFT_SECTION.md`](DRAFT_SECTION.md), in this folder.

---

## Statement proved

> **Theorem.** Let `γ ∈ (0,1)` be irrational and `ρ ∈ [0,1)`. Let `s` be either
> mechanical word of slope `γ` and intercept `ρ`,
> `s(j) = ⌊(j+1)γ + ρ⌋ − ⌊jγ + ρ⌋` or `⌈(j+1)γ + ρ⌉ − ⌈jγ + ρ⌉`.
> Then `Φ(s) ∉ Q`. More precisely, if `Φ(s) = u/v` in lowest terms with
> `H = max(|u|, v)`, then every half-length `ℓ` of an initial square of `s`
> satisfies
> ```
>        c(γ)·ℓ  ≤  log₂H + log₂(2 + 3ℓ) + log₂3 ,        c(γ) = 2 − max(1, γ·log₂3) ≥ 2 − log₂3 = 0.41503…
> ```
> which fails for all large `ℓ`; and `s` has initial squares of unbounded
> half-length.

This covers **every Sturmian word**: every irrational slope, every intercept,
both the lower and the upper mechanical word. The constant `c(γ)` is exactly the
one already in §8 of the paper.

---

## I1 — initial squares. **CITED**, no exceptions

> **Theorem (Allouche–Davison–Queffélec–Zamboni 2001; see also Damanik–Killip–Lenz
> 2000).** Each Sturmian sequence begins in infinitely many squares; hence
> `ice(ω) ≥ 2` for every Sturmian sequence `ω`.

Quoted verbatim from Berthé–Holton–Zamboni, *Initial powers of Sturmian
sequences*, Acta Arith. **122** (2006) 315–347, §1:

> *"In [3] it is shown that each Sturmian sequence begins in infinitely many
> squares (see also [19]), and hence `ice(ω) ≥ 2` for all Sturmian sequences `ω`."*

with `[3] = J.-P. Allouche, J. P. Davison, M. Queffélec, L. Q. Zamboni,
Transcendence of Sturmian or morphic continued fractions, J. Number Theory **91**
(2001), 39–66` and `[19] = D. Damanik, R. Killip, D. Lenz, Comm. Math. Phys.
**212** (2000), 191–204`.

**Exceptional slopes or intercepts: none.** The statement is for *all* Sturmian
sequences. Infinitely many squares means infinitely many *distinct* prefixes of
the form `WW`, and a word has at most one prefix of each length, so
`|W| → ∞`. **This is what I4 needs, and it is exactly attained**: BHZ Theorem 1.1
shows `ice = 2` is achieved for some slopes, so the exponent cannot be improved
above 2 in general — but 2 suffices, because `2 > max(1, γ·log₂3)` for every
`γ ∈ (0,1)`, with margin `c(γ) ≥ 2 − log₂3 > 0`.

*(BHZ also give the exact formula for `ice(ω)` via the Ostrowski expansion of the
intercept, and Theorem 1.1 characterises the slopes admitting `ice = 2`: there is
`ω ∈ X_γ` with `ice(ω) = 2` iff for each `(s,t)`, `s > 1`, only finitely many `k`
have `(a_k,a_{k+1}) = (s,t)` or `(a_k,a_{k+1},a_{k+2}) = (1,1,t)`. We do not need
this.)*

**VERIFIED** (`data/i1_squares.txt`, `data/i1_adversarial.txt`): over 4 slopes
(`log₃2`, `1/φ`, `√2−1`, `[0;1,97,1,…]`) × 6 intercepts each, and then **12 000
random intercepts** across 3 slopes, **every** word has initial squares, with
**zero** intercepts having none. Worst case over 64 ≤ L ≤ 1200: best initial
exponent `≥ 2.11`. Square half-lengths are convergent and **semiconvergent**
denominators (`2,8,65,485` and `19,38,84,168,252,401,569,1054,2108` for `log₃2`;
Fibonacci for `1/φ`; `1,5,29,169,985` for `√2−1`).

## I2 — roots of initial squares are Christoffel conjugates. **CITED**

This is the load-bearing step, and it is a published proposition.

> **Proposition 3.2 (Berthé–Holton–Zamboni 2006).** *"Suppose `ω` begins in a word
> `w` to power `r ≥ 2`, where `|w| ≥ 2`, and `w` is primitive. Then there is a
> nonnegative integer `m` such that **`w` is a cyclic permutation of
> `τ_{i₁} ∘ ⋯ ∘ τ_{i_m}(01)`**, and `ω^{(m)}` begins in `01` or `10` to power
> `> ⌊r⌋ − 1`. Furthermore, `m` is one of the numbers `s_k − 1` or `s_k − c_k − 1`."*

Here `τ₀ : 0↦0, 1↦01` and `τ₁ : 0↦10, 1↦1` are the two standard Sturmian
morphisms; `τ_{i₁}∘⋯∘τ_{i_m}` applied to the standard pair `(0,1)` yields a
standard pair, and the concatenation of a standard pair is a **standard
(Christoffel) word**. So the primitive root `W` of an initial square is a
**conjugate of a Christoffel word**, hence `W^∞` is balanced and is a periodic
mechanical word of rational slope `k/ℓ` in lowest terms.

*(If `W` is not primitive, `W = V^t` and `s` begins in `V^{2t}`; apply the above
to `V`. So primitivity is free.)*

**VERIFIED** (`data/i2_i3_i4.txt`): **48/48** initial-square roots across 4
slopes × 4 intercepts are conjugates of `christoffel(k, ℓ)`, checked as exact set
membership among all `ℓ` rotations. **0 failures.**

**Why this is not automatic — CONTROL 3.** A balanced finite word need not have a
balanced periodization, exactly as flagged in the brief. Smallest witnesses found
by exhaustive search (`data/controls.txt`): `W = 0110`, `1001` (`ℓ=4, k=2`),
`01110`, `10001` (`ℓ=5`) are balanced while `W^∞` is not, and none is a
Christoffel conjugate. **I2 is doing real work.**

## I3 — height bound. **PROVED with `C = 3`**; `C = 1` **VERIFIED** only

> **Lemma.** Let `W` be a conjugate of a Christoffel word, `|W| = ℓ`, `k` ones.
> Then `0 < c_W ≤ 3·ℓ·max(2^ℓ, 3^k)`, where
> `c_W = Σ_{i<ℓ, W_i=1} 3^{k−k_{i+1}(W)} 2^i` and `Φ(W^∞) = c_W/(2^ℓ − 3^k)`.

**Proof.** `Φ(W^∞) = c_W/(2^ℓ − 3^k)` is Proposition 4.1 of the paper (grouping
the series of Prop. 2.1 by periods; `2^ℓ ≠ 3^k` by unique factorisation). For the
bound: `W^∞` is balanced by I2, so `W` is a factor of a mechanical word of slope
`k/ℓ` and the discrepancy bound `|k_{i+1}(W) − (i+1)k/ℓ| < 1` holds. Hence
`k − k_{i+1}(W) < k(ℓ−1−i)/ℓ + 1`, so with `ρ = 3^{k/ℓ}`
```
      3^{k−k_{i+1}(W)} 2^i  <  3 · ρ^{ℓ−1−i} 2^i  ≤  3 · max(ρ^{ℓ−1}, 2^{ℓ−1})  ≤  3·max(3^k, 2^ℓ),
```
the middle step because `i ↦ ρ^{ℓ−1−i}2^i` is monotone, so its maximum over
`0 ≤ i ≤ ℓ−1` is at an endpoint. The sum has at most `ℓ` terms. ∎

This is precisely the argument sketched in Remark 4.3 of the paper ("for an
arbitrary balanced `w` the proof of Lemma 4.2 goes through with the discrepancy
bound … at the cost of a factor 3"), now applied where it is needed.

**VERIFIED, and `C = 1` appears to suffice.** Over **all** conjugates of **all**
Christoffel words with `ℓ ≤ 40`, the maximum of `c_W /(ℓ·max(2^ℓ,3^k))` is
**0.4394**, attained at `p/q = 12/19`, `W = 0101101101011011011`
(`data/i2_i3_i4.txt`). In all 48 sampled initial squares the ratio is `≤ 0.455`.
**`C = 1` is VERIFIED for `ℓ ≤ 40` and in every sampled square; it is not proved.**
The theorem uses `C = 3`, which is proved.

**Balance is essential — CONTROL 2.** For `W = 0^a 1^a` the ratio
`c_W/(ℓ·max(2^ℓ,3^k))` is `0.87, 2.83, 10.39, 41.02` at `a = 6, 10, 14, 18` and
diverges, so no constant works without I2.

## I4 — the Liouville step. **PROVED**

Suppose `Φ(s) = u/v` in lowest terms, `H = max(|u|,v)`. Since `Φ(s) ∈ Z₂`, `v` is
**odd**. Let `WW` be an initial square of `s`, `W` primitive, `|W| = ℓ`, `k` ones,
`δ = 2^ℓ − 3^k` (**odd**, as `ℓ ≥ 1`), and put

```
        M = u·δ − v·c_W  ∈  Z .
```

**`M ≠ 0`.** If `M = 0` then `Φ(s) = u/v = c_W/δ = Φ(W^∞)`; `Φ` is a bijection, so
`s = W^∞`, contradicting aperiodicity of `s` (`γ` irrational).

**Lower bound.** `Φ(s) − Φ(W^∞) = M/(vδ)` with `v, δ` odd, so
`v₂(M) = v₂(Φ(s) − Φ(W^∞)) = lcp(s, W^∞) ≥ 2ℓ`, the last step because both `s`
and `W^∞` begin with `WW`. Hence `|M| ≥ 2^{2ℓ}`.

**Upper bound.** By I3, `|M| ≤ H(|δ| + |c_W|) ≤ H(2^ℓ + 3^k + 3ℓ·max(2^ℓ,3^k))
≤ H(2 + 3ℓ)·max(2^ℓ, 3^k)`, so
`log₂|M| ≤ log₂H + log₂(2 + 3ℓ) + max(ℓ, k·log₂3)`.

**Combining**, `2ℓ ≤ log₂H + log₂(2+3ℓ) + max(ℓ, k·log₂3)`. Since `W` is a factor
of a Sturmian word of slope `γ`, `|k − γℓ| ≤ 1`, so
`max(ℓ, k·log₂3) ≤ max(1, γ·log₂3)·ℓ + log₂3`. Therefore

```
        c(γ)·ℓ  ≤  log₂H + log₂(2 + 3ℓ) + log₂3 ,      c(γ) = 2 − max(1, γ·log₂3) .
```

Since `γ < 1`, `γ·log₂3 < log₂3` and `c(γ) > 2 − log₂3 = 0.41503…> 0`, while
`ℓ → ∞` by I1. Contradiction. ∎

**Every constant explicit; the `o(1)` is `log₂3` from `|k − γℓ| ≤ 1`.** With
`C = 1` (verified, not proved) the bound improves to
`c(γ)·ℓ ≤ log₂H + log₂(2+ℓ) + log₂3`.

**VERIFIED** (`data/i2_i3_i4.txt`): at every one of the 48 sampled squares the
margin `2ℓ − max(ℓ, k·log₂3)` equals `c(γ)·ℓ` to three decimals —
`1.000·ℓ` for the three slopes with `γ·log₂3 ≤ 1` and `0.431·ℓ` for
`γ = 0.98986`, matching `c(γ) = 0.4311`.

---

## Controls

| control | required behaviour | result |
|---|---|---|
| **rational slope** `p/q` (exact rational arithmetic) | word periodic, `Φ` rational, argument silent | `M = u·δ − v·c_W = 0` **exactly** at `p/q = 2/3, 5/8, 12/19, 41/65`; word verified periodic. **SILENT** ✓ |
| **Thue–Morse** (aperiodic, not Sturmian) | method must be silent, not claim irrationality | **no initial square at all** for `L < 2048` — I1 has no input. **SILENT** ✓ |
| `W = 0^a1^a` (balanced, unbalanced periodization) | height bound must fail | ratio `→ ∞` (`0.87, 2.83, 10.39, 41.02`) ✓ |
| balanced ⇏ balanced periodization | I2 must be non-vacuous | witnesses `0110, 1001, 01110, 10001` found ✓ |

**Exactness.** Slopes and intercepts are carried as integers over `2^512`; every
floor is an integer shift; `safety_margin` reports the minimum distance of
`jγ + ρ` to `Z` over the range used (≥ 496 bits in every run, against a
representation error of at most `j ≤ 2^13` units), which certifies every floor.
All `c_W`, `2^ℓ − 3^k` and `M` are exact Python integers.

---

## Novelty — stated honestly

* For **`γ ≠ β = ln2/ln3`** irrationality of `Φ(s)` for **any** aperiodic `s` of
  lower ones-density `≠ β` already follows from density results:
  **Monks–Yazinski (2004, Thm 2.7(b), refereed)** below `β`, and
  **López–Stoll (2021, Thm 1, first half, unrefereed preprint)** above `β`. A
  Sturmian word of slope `γ` has ones-density exactly `γ`, so for `γ ≠ β` the
  conclusion is **not new**.
* The **new content is exactly two things**: (a) the **critical slope
  `γ = β`, at every intercept**, where both density halves are vacuous and where
  the paper currently proves only intercept `0` and its shifts; and (b) **one
  elementary, effective, 2-adic proof covering all Sturmian words uniformly**,
  replacing an unrefereed archimedean argument above `β` and supplying an
  explicit height bound below `β`, which a density argument does not give.
* Relative to **the paper as it stands**, the gain is the removal of
  Remark 8.9's restriction to intercept `0`: from one word per slope (plus its
  countably many shifts, Cor. 8.8) to the **whole uncountable Sturmian subshift
  `X_γ`**, for every irrational `γ`.
* I1 and I2 are **not ours** — ADQZ 2001 / DKL 2000 and BHZ 2006 Prop. 3.2. The
  contribution is I3 (the height bound for Christoffel conjugates, one line from
  the paper's own Remark 4.3) and I4 (the Liouville comparison), plus the
  observation that the two published combinatorial facts are exactly what the
  argument needs.

## What this does **not** do

It says nothing about divergent orbits of positive integers, nothing about the
Periodicity Conjecture in general — which quantifies over **all** aperiodic parity
vectors, of which the Sturmian ones are a measure-zero, one-parameter-per-slope
family — and nothing about the Collatz conjecture.

## Verdict

> **PROVED**, with `C = 3` in I3. The route closes for every irrational slope and
> every intercept, with `c(γ) ≥ 2 − log₂3` uniform. The one loose end is
> cosmetic: `C = 1` is verified for `ℓ ≤ 40` and in every sampled square but not
> proved; nothing depends on it.

A draft section is in [`DRAFT_SECTION.md`](DRAFT_SECTION.md). **The paper has not
been edited.**
