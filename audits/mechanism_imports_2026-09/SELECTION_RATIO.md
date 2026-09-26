# The finite-height selection ratio

**A definition, not a result.** This file records a reformulation of the placement gap
that came out of the six imports. It proves nothing, and controlling the object defined
here is *at least as strong as* (DE) — see §3. It is written down because it is a
better-conditioned coordinate than the frontier residual `Δ_N`, and because it has one
property no purely symbolic quantity has: it separates `3x+1` from `3x−1`.

---

## 1. The decomposition

For a height cutoff `M` and depth `N`, put

```
A_{N,M}  =  #{ m odd, 1 ≤ m ≤ M : m is zero-confined for N steps }        (integer)
O_M      =  #{ m odd, 1 ≤ m ≤ M }  =  ⌈M/2⌉
p_N      =  Σ_{w confined, |w| = N} 2^{−S_N(w)}                           (odd-Haar mass)
```

and define the **selection ratio** `Q_{N,M}` by the identity

```
                    A_{N,M}  =  Q_{N,M} · O_M · p_N .
```

The three factors separate cleanly:

- `p_N` — the symbolic/`2`-adic confinement rate. **Solved**: `−(1/N)log₂ p_N → I₀`
  is formalized (`Occupation.confined_mass_rate`), with the two-sided polynomial
  correction also proved.
- `O_M` — the available finite-height population. **Trivial.**
- `Q_{N,M}` — the arithmetic selection correction. **This is where the missing
  information lives.**

By Lemma 8 of [`LEMMAS.md`](LEMMAS.md), `A_{N,M}` is the surviving mass of the
realizer-cylinder tree at depth `N`: confinement deletes nodes and the deleted mass
escapes. And once `2^{S_N+1} > M` — i.e. beyond `N ≈ log₂M/α` — each occupied cylinder
holds exactly one integer `≤ M`, so `A_{N,M}` is literally a count of confined words
with small least realizer.

## 2. Relation to `Δ_N`

`A_{N,M} ≥ 1` exactly when `r_min(N,0) ≤ M`. Evaluating at `M = r_min(N,0)`, where
`A_{N,M} = 1` and `O_M = (M+1)/2`:

```
              Δ_N  =  1 − log₂ Q_{N,M} − log₂(1 + 1/M) ,
```

exactly, with `Δ_N = log₂ r_min(N,0) − log₂(1/p_N)` as in the synthesis. So `Q` does not
replace `Δ_N`; it **globalises** it — `Δ_N` is the specialisation of `Q` to the single
frontier value of `M`.

**Why the global version is better conditioned.** `Δ_N` is a min-statistic driven by
rare record replacements: `r_min(N,0) = 27` for every `N ∈ [4,36]`, so `Δ_N` is a
staircase, and the blind test in the finite-height audit found only three replacement
events in an 86-row window. `Q_{N,M}` averages over the whole surviving cohort —
thousands of seeds — and is correspondingly stable.

## 3. What a bound would buy, and how strong it is

Since `p_N ≍ N^{−3/2} 2^{−I₀N}`, a bound `Q_{N,M} ≤ poly(N)` uniform in `M` gives, for
each fixed `M`,

```
A_{N,M} → 0     and, since A_{N,M} ∈ ℤ_{≥0},     A_{N,M} = 0  for  N ≳ log₂M / I₀ .
```

Every positive odd integer lies below some `M`, so this is (DE). The integrality step is
the only part doing real work, and it is why `A` — an integer count — is the right
object rather than a mass.

> **Strength.** `Q ≤ poly(N)` **implies** (DE). It therefore belongs with the exponential
> realizer floor and `Δ_N = O(1)` among the statements *strictly stronger than, or at
> least as hard as*, (DE) — not among weaker intermediate targets. Nothing here suggests
> it is easier to prove; this file records the coordinate, not a route.

A weaker subexponential bound suffices: one needs only `Q_{N,M} < 2^{I₀N} N^{3/2}/O_M`.

## 4. Measurements

Exact counts, `O_M = (M+1)/2` with `M = 2^B − 1`; see [`data/eoc_tree.out`](data/eoc_tree.out).

| `B` | `N` | `A_{N,M}` | `O_M·p_N` | `Q` |
|---|---|---|---|---|
| 16 | 8 | 2936 | 2936.000 | 1.0000 |
| 16 | 24 | 436 | 430.529 | 1.0127 |
| 16 | 40 | 96 | 97.850 | 0.9811 |
| 20 | 16 | 16220 | 16208.969 | 1.0007 |
| 20 | 40 | 1483 | 1565.593 | 0.9472 |
| 22 | 24 | 27113 | 27553.832 | 0.9840 |
| 22 | 48 | 3080 | 3269.699 | 0.9420 |

Over `M = 2^{16}…2^{22}` and `N = 8…48`, `Q ∈ [0.92, 1.12]`: the selected count tracks
the Haar prediction to a few percent.

**This is a measurement over a bounded range and nothing more.** Near extinction the
counts fall to single digits (`A ∈ {1,2,3}`), and the `Q` values there carry no weight.
No claim is made that `Q` is bounded, nor that it is close to 1 outside the tested range.

## 5. The `3x−1` control

`3x−1` has the same `α`, the same confined-word count and the same `p_N` — the symbolic
side is identical — but `m = 1` is a zero-confined positive fixed point, so
`A_{N,M} ≥ 1` forever. At `M = 2^{16}`:

| `N` | `A(3x+1)` | `A(3x−1)` | `O_M·p_N` | `Q(3x+1)` | `Q(3x−1)` |
|---|---|---|---|---|---|
| 48 | 26 | 66 | 5.11e1 | 0.509 | 1.292 |
| 100 | **0** | 3 | 1.13e0 | 0.000 | 2.653 |
| 140 | 0 | 3 | 7.96e−2 | 0.000 | 37.712 |
| 180 | 0 | 3 | 6.41e−3 | 0.000 | **467.992** |

`3x+1` is extinct at `N = 84`; `3x−1` is still alive at `N = 190`.

> `Q` collapses for `3x+1` and diverges for `3x−1`. **Any bound on `Q` must therefore be
> sign-sensitive**, which is consistent with the sign obstruction of §7(b) of the
> synthesis: the aggregate identity, confinement and the sign of a denominator cannot
> separate the two systems, so whatever does the separating must enter through `Q`.

**This is not evidence that `Q` is powerful.** `Q` sees the difference *because it is
defined from `A_{N,M}`*, and `A_{N,M}` is the thing that differs. The content of the
control is a constraint on future proofs, not a property of the coordinate.

## 6. Why the obvious bound fails

`N_M(w) ≤ 1 + M/2^{S_N+1}` summed over confined words gives
`A_{N,M} ≤ #W_N^{conf} + O_M p_N`. By Lemma 10, `#W_N^{conf} ≈ 2^{hN}` with
`h = 1.5056439`, so the union bound over-counts by `2^{hN}` and is useless. The `+1` per
word is the whole obstruction: one must know *which* of the `2^{hN}` confined cylinders
contain an integer `≤ M`, and that is the placement question.

Second-moment machinery does not apply: `A_{N,M} = Σ_w N_M(w)` is an exact count, not an
estimate of a random variable, so the first moment *is* the answer and there is no
variance to control.
