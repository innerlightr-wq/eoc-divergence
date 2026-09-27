# Closing record: thin band settled, bulk collision estimate frozen as the target

Scratch `~/scratch/collatz-prefix-suffix-20260926-215500/`. No repository modified.
**Verdict: USEFUL LOCAL LEMMA, GLOBAL GAIN STILL OPEN.**
Labels: **DERIVED HERE**, **COMPUTATIONALLY VERIFIED WITHIN STATED RANGE**, **UNRESOLVED**.
Nothing here is Lean-verified; no novelty claim.

## 1. The singleton filter is now retired on a proof, not on finite counts

**Lemma (DERIVED HERE, verified).** For positive valuation words of length `ℓ ≥ 3`, total `b`, under
`S_m ≤ αm + A` with `A ≥ 0` and feasibility `ℓ ≤ b ≤ αℓ + A`: the admissible family is a singleton
**iff** `b = ℓ`.

*Proof.* `b = ℓ` forces all-ones. If `b > ℓ`, the words `(1^{ℓ−1}, b−ℓ+1)` and
`(1^{ℓ−2}, 2, b−ℓ)` are distinct (they differ at position `ℓ−1`), positive, and both total `b`.
Confinement is automatic before the last two positions; the only extra check for the second is
`ℓ ≤ α(ℓ−1) + A`, which holds since `ℓ/(ℓ−1) ≤ 3/2 < α` for `ℓ ≥ 3`; the final condition for both is
the assumed feasibility of `b`. ∎

*Verified:* 186 nonempty `(ℓ,b,A)` families, `ℓ = 3…9`, `A ∈ {0, ½, 1, 2, 3}`, 35 singletons,
**0 mismatches** with the criterion `b = ℓ`.

Applied with both halves of length `≥ 3`: `|U_a| = 1 ⟺ a = j` (prefix, `A = 0`) and
`|V_a| = 1 ⟺ b = N−j` (suffix, `A = αj − a`). These are exactly the zero-excess endpoints `k = 0`
and `e−k = 0`, inside the frozen band for every `δ ≥ 0`. **The ad-hoc filter is superseded.**

## 2. A bookkeeping correction I accept

The jump from `C ≈ 3.08` to `C ≈ 29.52` was my bookkeeping, not the mathematics: I gave every band
class the trivial bound. Both bounds remain valid on every class, so the finite record should keep
`min{ L_{s,a}, (2L_{s,a}/q)(1 + √(χ_{U,a}χ_{V,a})) }` throughout. Recomputed that way:

| | best finite proved `C` |
|---|---|
| `κ = 0.65`, `B = 20` | **2.0000** |
| `κ = 0.90`, `B = 20` | **3.0762** |

Two records are now kept separately: the **frozen partition** for the asymptotic proof, and the
**smaller rigorous bound per class** for finite diagnostics. Neither settles the asymptotics.

## 3. The target, frozen at a concrete exponent

`N = ⌈(13/20)B⌉`, `j = ⌊N/2⌋`, `B ≤ s ≤ ⌊αN⌋`, band `min{k, e−k} ≤ ⌊N/10⌋`, `q = 2^{s+1−B}`:

> **(\*) UNRESOLVED.** There are `C, p` independent of `B` and of the permitted shell `s` with
> ```
> Σ_{a ∈ bulk} L_{s,a}·√(χ_{U,a} χ_{V,a})  ≤  C(B+1)^p · L_s · q^{1/25} ,
> ```
> the suffix family constrained only by its inherited corridor `S_v(m) ≤ αm + A`, `A = αj − a`.

**Payoff, verified to 4.8e−16 on every figure:**

| quantity | value |
|---|---|
| `ακ − 1` | 0.030225625468751 |
| `η = (ακ−1)/25` | 0.001209025018750 |
| exponent `1 − I₀κ + η` | **0.949651926715094** |
| baseline `H₂(1/α)` | 0.949955527188331 |
| **improvement** | **0.000303600473237** |
| sanity: `η < I₀(κ − 1/α) = 0.001512625491987` | true |

So `(\*)` would give `#(E_0 ∩ [0,X)) ≪ (log X)^{p'} X^{0.9496519267…}`, through
`ResidueDiscrepancy.exceptional_count_le_of_leastRealizerBound` directly, with no absolute-value
Weyl hypothesis. **Conditional on `(\*)`, which is not proved.**

## 4. Bounded proof attempt: one arithmetic input beyond capacity, and why it is not enough

**Lemma (DERIVED HERE, verified).** Within a bulk class every `v ∈ V` shares the total `b`, so the
exact realizers `r_v` are distinct **odd** residues mod `2^{b+1}`. With `L = lcp(v,v')` and
`t := S_L(v) + min(v_{L+1}, v'_{L+1})`:

1. `v₂(r_v − r_{v'}) = t` — the accelerated lcp law. *Verified: 0 violations.*
2. `y_v := 3^{−j}r_v mod 2^{b+1}` has `v₂(y_v − y_{v'}) = t`, since `3^{−j}` is a unit.
3. A collision `⌊y_v/H⌋ = ⌊y_{v'}/H⌋`, `H = 2^{B−a}`, forces `|y_v − y_{v'}| < H`; the difference is
   a **nonzero** multiple of `2^t`, so `2^t ≤ |diff| < H`, giving
   ```
   collision  ⟹  t < B − a :
   colliding pairs must share a common prefix of SMALL total valuation.
   ```
   *Verified: 0 violations across the tested bulk classes.*

This is genuine arithmetic information beyond distinctness — it eliminates exactly the
long-shared-prefix pairs, which capacity cannot see. **But it does not deliver `(\*)`, and the
reason is quantitative:** short common prefixes are typical, so the excluded fraction of pairs is
only **2.9%–11.6%** across the tested bulk classes. At a representative bulk class
(`s=27, a=12, d=8, |V|=2258`):

| bound on `Σ_x h(x)²` | value | implied `χ_V` |
|---|---|---|
| truth | 21,896 | **0.099** |
| capacity `(H/2)|V|` | 289,024 | 13.51 |
| lcp-restricted | 4,725,567 | ≫ |
| what `(\*)` needs (`χ_Uχ_V ≲ q^{2/25} ≈ 1.56`) | — | — |

The lcp-restricted bound is **weaker than capacity** at these parameters, and capacity itself
overshoots the truth by a factor ≈136 in `χ_V`. **Recorded as a precise negative:** the lcp law is a
correct and non-circular arithmetic restriction, but it removes a vanishing fraction of the pair
count, whereas `(\*)` needs `Σh²` within a `q^{2/25}` factor of `|V|²/q`.

## 5. Position

```
thin words  : controlled by combinatorics  (complete, verified asymptotically and at B = 100…640)
bulk words  : arithmetic collision estimate (*) still required  (UNRESOLVED)
```

Settled this round: the singleton characterisation (on a proof), the payoff arithmetic, the
bookkeeping correction, and one arithmetic lemma with a quantified negative. Not settled: `(\*)`,
hence no improvement to the exceptional-set exponent. The finite diagnostics (`C = 2.00`/`3.08`,
`τ_bulk ≈ 0.97`) remain diagnostics.

**Next attempt should use something the lcp law does not: the carry equations coupling `r_v` across
the class, or the corridor `A` as an active constraint rather than a side condition.** What would
not count as progress: assuming the collision count is small, or another favourable finite
`τ_bulk`.
