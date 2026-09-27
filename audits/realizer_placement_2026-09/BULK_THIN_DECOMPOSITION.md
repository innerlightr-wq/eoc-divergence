# Bulk/thin decomposition: verified tools, a better κ, and the located obstruction

Scratch `~/scratch/collatz-prefix-suffix-20260926-215500/`. No repository modified.
Labels: **DERIVED HERE**, **COMPUTATIONALLY VERIFIED WITHIN STATED RANGE**, **UNRESOLVED**.

## 0. Two corrections I accept

**(a) My `B=16` "FAIL" labels were wrong-headed.** I compared raw finite `τ_eff` against `σ*`,
which tests a uniform exponent *with constant 1*. A uniform theorem `R ≤ C L q^{−τ}` is compatible
with a smaller finite `τ_eff` at cost `C ≥ q^{τ−τ_eff}`. At the binding `B=16` shell (`q = 256`),
even `τ_eff = 0.830` is compatible with `τ = 0.96` at `C ≥ 2^{8(0.13)} = 2.056`. **The balanced
splits did not refute a uniform estimate**; they failed a constant-one test at a finite scale.
Relabelled throughout. Symmetrically, the `B=20` passes prove nothing uniform.

**(b) "Limited by the worse marginal" was the wrong phrasing.** With `E_A = u²χ_U`, `E_B = v²χ_V`,
```
R/L = √(χ_U χ_V)/q ,    H(0) ≤ min{ L , (2L/q)(1 + √(χ_U χ_V)) }
```
so it is the **product** that matters, and a good marginal can compensate a bad one. Verified, and
note `δ_U + δ_V = 2(1 − τ_eff)`, so the "product budget" `δ_U+δ_V < 2(1−σ*) = 0.100088946` is
*the same condition* as `τ_eff > σ*`, not a new one.

## 1. The assessment's new mathematics — all verified

| claim | verdict |
|---|---|
| **Rotation / cycle-lemma bound** `L_s ≥ C(s−1,N−1)/N` | **CONFIRMED.** Proof checked: with `e_i = d_i − s/N` (sum 0), rotating just after a maximiser of the partial sums makes every new partial sum `≤ 0`, so `S'_k ≤ (s/N)k ≤ αk` since `s ≤ αN`; each rotation class has `≤ N` members. Verified exactly: **32 shells, `N = 6…14`, 0 violations**; the ratio tightens to **1.213** at the top shell (`N=14, s=22`), so it is nearly sharp where it matters. |
| class-weight bound `L_{s,a}/L_s ≤ N·C(a−1,j−1)C(s−a−1,N−j−1)/C(s−1,N−1)` | **CONFIRMED** (numerator is the unrestricted count, denominator by the rotation bound) |
| `Δ = αH₂(1/α) − (α−½)H₂(½/(α−½)) ≈ 0.425486` | **CONFIRMED**: `1.505643888 − 1.080158212 = 0.425485676`, diff `3.2e−07` |
| `κ=0.65` makes the `a=j` singleton-prefix class harmless; `κ=0.90` does not | **CONFIRMED**: net exponent `Δκ − (ακ−1)` per `B` is `−0.246340` at `0.65`, `−0.072419` at `0.80`, `+0.043529` at `0.90` |
| suffix pair-counting form `Q_hi(v) = ⌊y_v/H⌋`, `q = M_v/H`, and the capacity bound `Σh² ≤ (H/2)|V|` | **CONFIRMED**: 86 classes, 0 form violations, all `y_v` odd, 0 capacity violations |
| Lean interface accepts an upper count with `C ≥ 1`, Weyl not mandatory | **CONFIRMED** (re-read `ResidueDiscrepancy.lean:125-134`) |

## 2. DERIVED HERE: the combinatorial tool fixes a better primary κ

The suppression `Δκ` beats the unresolved block `ακ−1` exactly when
```
κ < 1/(α − Δ) = 0.862458 .
```
Both degenerate extremes are governed by the **same** `Δ`: the singleton-prefix class `a = j` and
the singleton-suffix class `b = N−j` give, at `j = N/2`, the same binomial
`C((α−½)N, N/2)`, hence the same exponent — the situation is symmetric under `j ↔ N−j`.

Consequently the largest κ at which this purely combinatorial argument disposes of the degenerate
classes is `κ ≈ 0.8625`, where the **maximum available gain is**
```
I₀(κ − 1/α) = 0.018364      (against 0.001513 at κ = 0.65)
```
a **12× larger prize** than the pre-registered default, still inside the range where the thin
classes need no arithmetic input. This is a refinement of the target's κ, not a substitution of the
question: `κ = 0.65` remains the primary theorem target and `0.90` the stress test, but
`κ ≈ 0.86` is the natural ceiling for the present toolset and is where I would aim a first theorem.

## 3. The decomposition, run with every class retained

`H_s(0) ≤ Σ_a min{ L_a , (2L_a/q)(1 + √(χ_{U,a}χ_{V,a})) }`, thin `= (|U_a| = 1 or |V_a| = 1)`,
balanced split `j = ⌊N/2⌋`, **no size filter**.

`κ = 0.90` (`B=20, N=18`, `j=9`):

| `s` | `d` | #cls | thin | `Σ_thin L_a·q/L_s` | comb. bound `W·` | bulk `τ` | `C_shell` |
|---|---|---|---|---|---|---|---|
| 22 | 3 | 5 | 2 | 1.253 | 2.977 | 1.699 | 2.497 |
| 24 | 5 | 6 | 1 | 1.812 | 0.536 | 1.328 | 2.665 |
| 26 | 7 | 6 | 1 | 4.608 | 0.214 | 1.160 | 2.952 |
| 27 | 8 | 6 | 1 | 8.358 | 0.140 | 1.072 | 3.387 |
| **28** | **9** | 6 | 1 | **16.715** | **0.0934** | **0.9655** | **4.590** |

Total proved `C = 3.0762`. At `κ = 0.94` (`B=16, N=15`, `j=7`): `C = 4.1241`, bulk `τ = 0.8925` at
the binding shell. At `κ = 0.65` (`B=20, N=13`): only `d = 1` exists, `Σ_thin L·q/L_s = 0.295`
against a combinatorial bound of `0.443`, and `C = 2.0000` — still the `d=1` triviality, so
uninformative, as before.

**The diagnosis inverts my previous one.** The bulk is in reasonable shape: `τ_bulk` at the binding
shell is `0.9655` (`κ=0.90`) — above `σ*`, margin `0.016`. **The thin classes are the problem**:
their contribution relative to the cylinder mass grows like `q = 2^d` (1.04 → 16.72 across the
shells), and the combinatorial bound, while valid, gives `0.0934·q = 47.8 > 1` at `d = 9` — so it
does **not** suppress them at `κ = 0.90`. It does at `κ < 0.8625` (§2). The assessment predicted
exactly this.

## 4. What remains

> **UNRESOLVED (the one estimate).** For `κ < 0.8625` and a balanced split, prove
> `Σ_{a ∈ bulk} L_{s,a}·√(χ_{U,a} χ_{V,a}) ≤ C·L_s·q^{1−τ}` with `τ > σ* = 0.949955527` and `C`
> independent of `B`, the thin classes being handled by the rotation bound of §1.

The suffix side is now an explicit pair count: with `M_v = 2^{b+1}`, `H = 2^{B−a}`,
`y_v = 3^{−j}r_v mod M_v`,
```
Σ_x h(x)² = #{(v,v') : ⌊y_v/H⌋ = ⌊y_{v'}/H⌋} ,
```
pairs of transformed suffix realizers in a common dyadic interval. Distinctness of the `y_v` (Terras
plus multiplication by a unit) and their oddness give only the capacity bound `Σh² ≤ (H/2)|V|`,
equivalently `χ_V ≤ 2^b/|V| − 1`: **useful exactly to the extent that the confined suffix family is
dense in its residue space.** Any improvement must extract what zero-confinement adds beyond
distinctness. That is the point at which genuinely new arithmetic information would enter, and it is
not supplied by anything measured here.

**Honest limits.** Everything is `B ≤ 20`, `N ≤ 18`, one split per row; `τ_bulk` and `C` are finite
diagnostics, not uniform bounds, and per §0(a) a finite `τ_bulk` below `σ*` is not a refutation. The
`Δ` argument disposes of the two extreme degenerate classes; the full thin set at a general split
still needs the summed combinatorial bound, which I computed numerically (`W`) but did not bound
asymptotically for all thin `a`. No curve was fitted and no scan was enlarged.
