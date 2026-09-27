# The explicit thin-band lemma: audited, plus three corrections to my report

Scratch `~/scratch/collatz-prefix-suffix-20260926-215500/`. No repository modified.
Labels: **DERIVED HERE**, **COMPUTATIONALLY VERIFIED WITHIN STATED RANGE**, **UNRESOLVED**.
Not Lean-verified; no novelty claim for the rotation or entropy arguments.

## 0. Three corrections I accept

**(a) Sign label.** My numbers `−0.246340, −0.072419, +0.043529` are `(ακ−1) − κΔ`; my prose wrote
them as `Δκ − (ακ−1)`, which is the negative. Numbers right, formula label wrong. Confirmed.

**(b) `0.862458` is the ceiling for the *endpoint* estimate only.** I called it "the natural ceiling
for the present toolset"; that overstates it. Enlarging the thin set to a band of width `δ` costs
entropy and lowers the ceiling to `1/(α − Δ_δ(α))`:

| `δ` | `Δ_δ(α)` | κ ceiling | `γ(0.65,δ)` |
|---|---|---|---|
| 0 (endpoints) | 0.425485676 | 0.862458 | 0.246340 |
| 0.01 | 0.363446471 | 0.818655 | 0.206015 |
| 0.05 | 0.229810178 | 0.737924 | 0.119151 |
| **0.10** | **0.130833547** | **0.687697** | **0.054816** |

So near `0.862458` no fixed-width band is controlled, only the endpoints. This reinforces keeping
`κ = 0.65` primary, and I withdraw the suggestion of aiming at `κ ≈ 0.86`.

**(c) My "symmetric extremes" claim was wrong for confined words.** The unrestricted binomial
envelope is symmetric under `j ↔ N−j`; the zero-confined family is not. Prefix confinement
`a ≤ αj` forces, at `j = N/2`,
```
(e−k)/N ≥ 1/κ − (α+1)/2 ,
```
which is `+0.245980` at `κ = 0.65` and `+0.136090` at `κ = 0.70` — both `> δ = 0.1`, so **the
suffix-side half of the band is empty for confined words** at those κ. (It may be nonempty from
`κ ≈ 0.80`: the bound falls to `−0.042481`.) Including it in the composition count is conservative
and valid, but it is not a symmetric family of real words. Corrected.

## 1. The lemma, verified

For `N = ⌈κB⌉`, `j = ⌊N/2⌋`, unresolved shell `B ≤ s ≤ ⌊αN⌋`, excess `e = s−N`, `k = a−j`, band
`min{k, e−k} ≤ ⌊δN⌋`:
```
L_s^thin ≤ T_δ(N,s,j) := Σ_{k in band} C(j+k−1, j−1)·C(N−j+e−k−1, N−j−1)
L_s      ≥ C(s−1,N−1)/N                                    (rotation bound, verified earlier)
⟹  H_s^thin/(L_s/q)  ≤  q·N·T_δ(N,s,j)/C(s−1,N−1) ,        q = 2^{s+1−B}
```
granting **every** thin word a below-cutoff realizer. No histogram, independence, or collision
input. The composition counts are correct: a length-`j` prefix with total `a = j+k` in positive
parts numbers `C(a−1,j−1)`, the suffix `C(b−1,N−j−1)` with `b = (N−j)+(e−k)`.

**Asymptotics.** With `θ = s/N`, `F(θ) = θH₂(1/θ)`, `G(z) = (½+z)H₂(½/(½+z))`,
`Δ_δ(θ) = F(θ) − G(δ) − G(θ−1−δ)`, the binomial entropy bounds give
`L_s^thin/L_s ≤ 2^{−NΔ_δ(θ)+O(log N)}`, hence
`H_s^thin/(L_s/q) ≤ 2^{N[θ−Δ_δ(θ)]−B+O(log N)}`.

**The top shell is the worst — verified, not inferred.** Re-deriving `F'(θ) = log₂(θ/(θ−1))` and
`G'(z) = log₂((½+z)/z)`,
```
d/dθ[θ − Δ_δ(θ)] = log₂[ 2(θ−1)(θ−½−δ) / (θ(θ−1−δ)) ] ,
numerator − denominator = (θ−1)² + δ(2−θ) > 0   on 1+δ < θ ≤ α < 2.
```
Algebraic identity and positivity checked at 399 points, **0 violations**; `θ − Δ_δ(θ)` is increasing
(min `1.0536` at `θ=1.11`, max `1.4541` at `θ=α`). Independently, the exact evaluation's argmax is
the **top** shell at every `B` tested (`s = 103, 206, 329, 659`). Hence uniformly over unresolved
shells,
```
H_s^thin/(L_s/q) ≤ 2^{−γ(κ,δ)B+O(log B)} ,   γ(κ,δ) = 1 − κ[α − Δ_δ(α)] .
```

**At `(κ,δ) = (13/20, 1/10)`:** `Δ_{0.1}(α) = 0.130833546677096` and
`γ = 0.054816179871361`. My values agree with the assessment's **to all 15 printed digits**.

**Exact finite evaluation** of `q·N·T_δ/C(s−1,N−1)`, integer binomials, every unresolved shell:

| `B` | `N` | max over unresolved shells | argmax `s` | assessment's value | ratio |
|---|---|---|---|---|---|
| 100 | 65 | 0.691825 | 103 | 0.691826 | 0.999999 |
| 200 | 130 | 0.0375106 | 206 | 0.0375106 | 1.000000 |
| 320 | 208 | 0.000161790 | 329 | 0.000161790 | 1.000002 |
| 640 | 416 | 1.72629e−09 | 659 | 1.72629e−09 | 0.999997 |

**Reproduced.** (Residual differences are display rounding.)

## 2. Containment of my earlier numeric "thin" set

My earlier classification was `|U_a| = 1 or |V_a| = 1`, chosen from the finite data. Checked against
the frozen band `min{k,e−k} ≤ ⌊0.1N⌋`:

| | my thin classes | **not** in the frozen band |
|---|---|---|
| `κ=0.65`, `B=20,N=18`→`N=13` | 1 | **0** |
| `κ=0.90`, `B=20, N=18` | 13 | **0** |

**The frozen band contains my numeric set at both κ**, so the lemma covers it and the ad-hoc
criterion can be retired. I keep the distinction recorded rather than conflating them.

## 3. A regime warning I have to add

At `B = 20` the frozen band is **not yet numerically effective**, and this is expected rather than a
problem: `γB ≈ 1.1` bits is swamped by the `O(log B)` overhead. Recomputing with the frozen band at
`B=20` gives combinatorial bounds of `5.82` (`κ=0.65`) up to `573.6` (`κ=0.90`, top shell), and the
total proved constant degrades from `C = 3.08` (ad-hoc thin set) to `C = 29.52` (frozen band) at
`κ=0.90`, because the band contains up to 4 classes per shell instead of 1 and each is given the
trivial bound.

> **The lemma must be judged by the exact binomial evaluation at `B ≥ 100` (§1), not by the
> `B ≤ 20` enumeration.** The two live in different regimes, and neither substitutes for the other.
> The assessment's `B = 100…640` table is the right evidence, and it reproduces exactly.

## 4. The inherited corridor, kept explicit

Zero-confinement of `uv` gives, for `i = j+m`, `a + S_v(m) ≤ α(j+m)`, i.e.
```
S_v(m) ≤ αm + A ,      A := αj − a  ( ≥ 0 exactly when a ≤ αj ) .
```
So the suffix is confined **within the inherited corridor `A`**, not at zero width, and `A` must
appear in the hypotheses of any collision estimate. This is also what makes the §0(c) asymmetry
work. Recorded so it cannot be dropped later.

## 5. What remains — unchanged

> **UNRESOLVED.** For `κ = 13/20`, the frozen band `δ = 1/10`, and a balanced split, prove
> ```
> Σ_{a ∈ bulk} L_{s,a}·√(χ_{U,a} χ_{V,a}) ≤ C·L_s·q^{1−τ} ,   τ > σ* = 0.949955527 ,
> ```
> `C` independent of `B`, with the suffix constrained only within the inherited corridor `A = αj−a`.

With that plus §1, the carry-robust bound
`H_s ≤ H_s^thin + 2L_s^bulk/q + (2/q)Σ_bulk L_{s,a}√(χ_Uχ_V)` would give an upper count fitting
`ResidueDiscrepancy.exceptional_count_le_of_leastRealizerBound` directly, with no absolute-value
Weyl hypothesis. **The thin-band lemma does not establish the bulk estimate**, and does not convert
the finite bulk margin (`τ_bulk = 0.9703` at `κ=0.90, d=9`, frozen band) into a uniform result.

**Net position.** Combinatorial treatment of an explicit thin band: **complete and verified**
(asymptotically, and exactly at `B = 100…640`). Bulk collision estimate: **open**. Improvement of
the exceptional-set exponent: **still conditional**.
