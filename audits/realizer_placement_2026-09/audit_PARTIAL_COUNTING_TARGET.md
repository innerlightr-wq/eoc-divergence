# The partial counting target

## The target, stated exactly

Fix `κ` rational with `1/α < κ`, `X = 2^B`, `M = X−1`, `N = ⌈κB⌉`, confinement width `U = 0`
(zero confinement). **Target:**

> **(T_κ,η)** There exist `C₀ > 0`, `d₀ ∈ ℕ`, `η ≥ 0`, all independent of `B`, and `B₀`, such that
> for every integer `B ≥ B₀`
> ```
> A_{N, X−1}  ≤  C₀ (B+1)^{d₀} 2^{ηB} · (X/2) · p_N .
> ```

Because `iidGeom2VectorProb N (geomPersistenceEvent collatzAlpha 0 N) = p_N` **exactly**
(BASELINE_AND_SCOPE.md), `(T_κ,η)` is literally the first-moment hypothesis of
`ExceptionalPowerBound.exceptional_count_le_of_firstMoment` with
`C = C₀(B+1)^{d₀}2^{ηB}`, i.e.

> **(T_κ,η) ⟺ `Q_{N,X−1} ≤ C₀(B+1)^{d₀}2^{ηB}`.**

**Notation warning.** The brief writes `(B+1)^d`; `d` there is a fixed polynomial degree. It must
not be confused with the unresolved block length `d_w = S_w+1−B`, which **grows** with `B`
(measured: `d_max = 2,3,4,6,11` at `B = 20,40,80,160,320`, i.e. `≈ (ακ−1)B`). I write `d₀` for
the polynomial degree and `d` for the block length.

## The implication to the exceptional set

Applying `exceptional_count_le_of_firstMoment` with `A := κ` (legitimate: `hNA` requires
`A·log₂X ≤ N`, and `N = ⌈κB⌉ ≥ κB` — verified exactly for `B = 20…320`) gives, for `U = 0`,

```
#(E_0 ∩ [0,X))  ≤  C₀ (B+1)^{d₀} 2^{ηB} · exp(λ*·0)/2 · X^{1 − I₀κ}
                =  (C₀/2) (log₂X + 1)^{d₀} · X^{1 − I₀κ + η}.
```

So the exponent is `1 − I₀κ + η`, against the **unconditional** baseline `1 − I₀/α = H₂(1/α)`
from `exceptional_count_le_rpow`. The gain condition is

> `η < I₀(κ − 1/α)`,

and the polynomial factor `(log₂X+1)^{d₀}` is harmless because the gain is a strict power saving.

## Verified exponent arithmetic

| quantity | value |
|---|---|
| `α = log₂3` | `1.584962500721156` |
| `1/α` | `0.6309297535714575` |
| `I₀` (Lean def) | `0.07931861277485547` |
| `H₂(1/α) = 1 − I₀/α` (**baseline**) | `0.9499555271883304` |
| `1 − I₀·0.65` | `0.948442901696` |
| `η` ceiling at `κ=0.65`: `I₀(0.65 − 1/α)` | **`0.001512625492`** |
| illustrative `η=0.001` → exponent | `0.949442901696` |
| net gain at `η=0.001` | `0.000512625492` |

The brief's `I₀ ≈ 0.0793186128`, `H₂(1/α) ≈ 0.949955527`, `1−I₀·0.65 ≈ 0.948442902`,
`0.949442902` all agree to `≤ 3.1e−10` (rounding only). **They are rounded decimals, not proved
constants**; the Lean side carries `I₀` symbolically and every inequality above should be
discharged from `I0_pos'`, `one_sub_I0_div_alpha_eq` and rational bounds on `α`, not from these
decimals.

**No loss from the persistence rate.** `geometric_persistence_upper_bound_bits` uses the exact
`I₀` (LEAN VERIFIED), so no substitution `γ < I₀` is needed and the ceiling above is the true one.

## Is the target genuinely intermediate?

**Yes, and this is checkable rather than rhetorical.**

- It is strictly **beyond** what is already proved. The note's plateau lemma gives
  `Q_{N,M} = 1` *exactly* for `N ≤ N*(B) = max{N : max_S(confined,N)+1 ≤ B} ≈ (B−1)/α`, i.e. for
  `κ ≤ ≈ 1/α`. The target needs `κ = 0.65 > 1/α = 0.63093`.
- It is strictly **weaker** than (DE). (DE) would need `Q ≤ poly` uniformly in `M` for all `N`;
  `(T_κ,η)` fixes `N` at a constant multiple of `log₂X` and allows an exponential factor `2^{ηB}`.
- It yields a **strict** exponent improvement over an unconditional theorem already in the
  repository, so the improvement is measurable rather than definitional.

**However, the margin is small and should be stated plainly.** At `κ = 0.65` the *maximum*
achievable gain is `0.0015126` in the exponent. Larger `κ` is much better:

| `κ` | exponent `1−I₀κ` | max gain |
|---|---|---|
| 0.65 | 0.948443 | 0.001513 |
| 0.80 | 0.936545 | 0.013410 |
| 0.95 | 0.924645 | 0.025310 |
| 1.00 | 0.920681 | 0.029274 |

**Recommended refinement (not a substitution of the question).** Taking `κ ↑ 1⁻` multiplies the
available gain by ≈19 and still keeps `N < B`, so the A4 singleton-shell obstruction
(which needs `κ ≥ 1`) does not bite. `κ = 0.95` is therefore a strictly better instance of the
*same* target with the *same* proof obligations. `κ = 0.65` is retained below as the
pre-registered default.

## Measured status of the target (COMPUTATIONALLY VERIFIED WITHIN STATED RANGE)

Exact `Q` at `N = ⌈0.65B⌉`, `M = 2^B−1`; `A_{N,M}` from exact cylinder counts, cross-checked
against direct odd-seed enumeration for `B ≤ 20` (agreement exact):

| `B` | `N` | words | `A_{N,M}` | `(X/2)p_N` | `Q` | `log₂Q` | `log₂Q / B` |
|---|---|---|---|---|---|---|---|
| 12 | 8 | 173 | 185 | 183.5 | 1.008174 | +0.01175 | 0.000979 |
| 16 | 11 | 2,652 | 1,864 | 1873.75 | 0.994797 | −0.00753 | −0.000470 |
| 20 | 13 | 17,637 | 23,315 | 23305.5 | 1.000408 | +0.00059 | 0.000029 |
| 24 | 16 | 312,455 | 259,555 | 259343.5 | 1.000816 | +0.00118 | 0.000049 |
| 28 | 19 | 5,936,673 | 2,955,232 | 2955259.75 | 0.999991 | −0.00001 | −0.0000004 |

Every `log₂Q/B` is **inside** the `η` ceiling `0.001512625` and shrinking. **This is not
confirmation of uniformity.** At these `B`, `N = ⌈0.65B⌉` exceeds `N*(B)` by only
`≈ 0.019B + 0.6 ≈ 1–2` steps, so the measurement sits immediately adjacent to the exact plateau
and cannot separate `η = 0` from `η > 0`. Labeled: **computational evidence only**, range
`B ≤ 28`; `B ≥ 32` untested (word enumeration at `N = 21` exceeds the pre-registered budget).

## Novelty limitation

A gain over `exceptional_count_le_rpow` is an improvement **inside this repository**. The
exceptional set here is `E_0` (permanently zero-confined odd seeds), which is *not* the set
addressed by the strongest cited literature: Tao (Forum Math. Pi 10, 2022, arXiv:1909.03562)
bounds orbits attaining almost bounded values for **almost all** seeds in logarithmic density —
a different (density-one) statement about a different set, neither implying nor implied by a
power bound on `E_0`. Applegate–Lagarias (Math. Comp. 64, 1995) and Krasikov–Lagarias
(Acta Arith. 109, 2003) bound **predecessor-tree counts**, again a different set. I found **no**
primary result giving a power bound on the permanently-confined set with exponent below
`H₂(1/α)`, but I did not conduct an exhaustive novelty search, so the correct label is
**not established as novel** rather than novel.
