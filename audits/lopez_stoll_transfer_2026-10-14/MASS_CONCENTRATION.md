# MASS_CONCENTRATION.md — the large-deviation and conditioned-mass estimates

Notation as in `TWO_CLOCK_TRANSLATION.md`. `H_2` is the binary entropy in bits.

```
   J(s) := s ( 1 - H_2(1/s) )   for 1 <= s <= 2 ;   J(1) = 1, J(2) = 0, J decreasing.
   I_0  := J(alpha) = alpha (1 - H_2(1/alpha)) = 0.079318612775 .
```

---

## 1. The geometric model is an identity, not a model [PRIOR + P]

**Source.** `eoc-divergence@938dcc0`, `Occupation/Compositions.lean:217`
```
   p(N,c) = sum over c-confined words d of length N of 2^{-S_N(d)} ,
   Confined c d  <->  for all j <= N, 2^{psum d j} <= 2^c 3^j
```
and `Occupation/Rate.lean:478`
```
   confined_mass_rate (c) : Tendsto (fun N => -(1/N) logb 2 (p N c)) atTop (𝓝 I₀) ,
   I₀ = alpha * (1 - binEntropy (1/alpha) / log 2) .
```
`c` is bound **outside** the limit: there is **no uniformity in `c`**, and §5
below shows the rate genuinely degrades once `c` grows with `N`. Status:
**source-backed; nothing was compiled in this session.**

> **Proposition M1 [P, prior session, re-verified].** `sum_{all words} 2^{-S_N} = 1`,
> so with `P[d = k] = 2^{-k}` (`k >= 1`, i.i.d., mean `2`),
> ```
>    p(N,c) = P[ S_j <= alpha j + c  for every j <= N ] .
> ```
> The dyadic mass **is** that probability — not an analogy.

> **Proposition M2 (the exact bridge) [P, prior session, re-verified].** With
> `Q_N = 2^{sN(N)+1}`, `sN(N) = floor(N log_2 3)`, and `mu` the normalized
> counting measure on odd residues mod `Q_N`,
> ```
>    mu(C_N) = p(N,0)   exactly, for every N ,
> ```
> where `C_N` is the set of 0-confined-to-depth-`N` odd residue classes.
> Verified by brute force over all odd residues mod `Q_N` for `N <= 14`,
> 0 violations (`audits/amplification_transfer_2026-10-14/`,
> `scripts/bridge.py`).

**Crucial scope line, carried from the brief.** The increments are i.i.d. under
the **normalized dyadic residue measure**. They are **not** independent along
the future trajectory of a **fixed** positive integer: that orbit produces one
deterministic word. Nothing in §§2-5 is a pathwise statement.

## 2. The endpoint rate [P]

> **Theorem M3.** For fixed `1 < s < 2`,
> ```
>    P[ S_N <= s N ] = 2^{-N J(s) + o(N)} ,     J(s) = s (1 - H_2(1/s)) .
> ```
>
> *Proof.* The words of length `N` with `S_N = t` are the positive compositions
> of `t` into `N` parts, `C(t-1, N-1)` of them, each of weight `2^{-t}`. So
> `P[S_N = t] = C(t-1,N-1) 2^{-t}` exactly and
> `P[S_N <= sN] = sum_{t=N}^{floor(sN)} C(t-1,N-1) 2^{-t}`.
> With `t = aN`, Stirling gives
> `C(aN-1, N-1) = 2^{aN H_2(1/a) + O(log N)}`, so the `t`-th term is
> `2^{-aN(1 - H_2(1/a)) + O(log N)} = 2^{-N J(a) + O(log N)}`.
> `J` is decreasing on `[1,2]`, so the sum of at most `sN` terms is dominated by
> `a = s`: `P = 2^{-N J(s) + O(log N)}`. ∎

Note `J(alpha) = I_0` and `J(2) = 0`: the terminal-point rate at the critical
slope **is** the confinement rate, because the optimal straight-line path to
`S_N = alpha N` lies exactly on the barrier and the ballot-type correction for
staying under it for all `j <= N` is only polynomial. That is also visible in the
repository's own sandwich `tt(N,sN)/N <= p(N,0) <= (sN+1) tt(N,sN)`
(`Rate.lean` `le_p`, `p_le`), validated independently here with 0 violations at
`N = 4,...,96`.

**Verified** by exact rational summation (`scripts/clocks_and_rate.py` part B),
monotone convergence in every column:

| `s` | `J(s)` | `N=50` | `N=150` | `N=400` | `N=1000` |
|---|---|---|---|---|---|
| 1.1 | 0.616553314 | 0.662490 | 0.637012 | 0.625978 | 0.620982 |
| 1.3 | 0.286845212 | 0.339146 | 0.309392 | 0.297047 | 0.291584 |
| **1.584963** | **0.079318613** | 0.127834 | 0.101663 | 0.089627 | 0.084074 |
| 1.7 | 0.038389710 | 0.079226 | 0.056272 | 0.046694 | 0.042343 |
| 1.9 | 0.003798321 | 0.031054 | 0.015313 | 0.009175 | 0.006435 |

The `O(log N)/N` prefactor is the whole of the residual gap.

## 3. The conditional estimate [P]

> **Theorem M4.** Fix `epsilon > 0` with `alpha - epsilon > 1`. Then
> ```
>    P[ S_N <= (alpha - epsilon) N  |  C_N ]  <=  2^{-N [ J(alpha-epsilon) - I_0 ] + o(N)} ,
> ```
> and the exponent is **positive**, since `J` is strictly decreasing on `[1,2]`
> and `alpha - epsilon < alpha`, so `J(alpha-epsilon) > J(alpha) = I_0`.
>
> *Proof.* The event `{S_N <= (alpha-epsilon)N} ∩ C_N` is contained in
> `{S_N <= (alpha-epsilon)N}`, whose probability is `2^{-N J(alpha-epsilon)+o(N)}`
> by Theorem M3. The denominator is `P[C_N] = p(N,0) = 2^{-I_0 N + o(N)}` by
> `confined_mass_rate`. Divide. ∎
>
> **Parameter restrictions, stated.** `alpha - epsilon > 1` (else the event is
> empty, every `d_j >= 1` forcing `S_N >= N`); `epsilon` **fixed**, because both
> `o(N)` terms are non-uniform in `epsilon` (§5). Numerically
> `J(1.4) - I_0 = 0.112313`, `J(1.5)-I_0 = 0.041322`,
> `J(1.55)-I_0 = 0.016556` — the exponent degrades to `0` as `epsilon -> 0`,
> which is exactly why §5 is a separate problem.

**In EOC coordinates** `Delta_N = alpha N - S_N`, Theorem M4 reads

```
   P[ Delta_N >= epsilon N  |  C_N ]  <=  2^{-N[J(alpha-epsilon) - I_0] + o(N)} ,
```
i.e. **within the confined ensemble, a linear terminal deficit is exponentially
unlikely.** Under the conditioned measure the typical `Delta_N` is `o(N)`.

## 4. The four levels, kept apart

The brief insists on this separation and it is the crux of the whole file.

| level | statement | what it is about |
|---|---|---|
| **endpoint constraint** | `S_N <= sN` | one coordinate of the word |
| **full-prefix confinement** | `C_N`: `S_j <= alpha j` for every `j <= N` | the whole path |
| **conditional law** | Theorem M4 | a *measure* on words, conditioned on `C_N` |
| **deterministic orbit** | one fixed `m_0` | a single word, with no measure on it |

> **Theorem M4 is a statement about the conditioned measure and carries no
> pathwise content.** "Typical confined words have `Delta_N = o(N)`" does not
> say that a **particular** confined orbit has `Delta_N = o(N)`: a single word is
> a measure-zero event, and witness **W1** of `TWO_CLOCK_TRANSLATION.md` §2 is a
> 0-confined word with `Delta_N/N = alpha - 1` for every `N` — in the
> exponentially-thin part of the ensemble for every `N`, yet perfectly
> admissible. **A conditional endpoint estimate is not a pathwise return
> theorem.** This is the same wall as in
> `audits/amplification_transfer_2026-10-14/` (Theorem 1 there:
> statistical scarcity caps nothing pointwise).

## 5. Why the fixed-`epsilon` asymptotic may not be substituted — and the price of a moving budget

Theorem M4's `o(N)` terms come from two Stirling estimates and a sum of `O(N)`
terms; neither is uniform as `epsilon -> 0`. Substituting `epsilon_N -> 0` is
invalid without a uniform estimate; that is `MOVING_CORRIDOR.md`.

What **is** proved, for the companion question of a moving **confinement budget**
`c = c(N)` (recall `confined_mass_rate` is fixed-`c` only):

> **Proposition M5 [P, prior session, re-verified].** With `c = floor(theta N)`,
> ```
>    -(1/N) log_2 p(N, c(N))  ->  J(alpha + theta)   for 0 <= theta < 2 - alpha,
>                             ->  0                  for theta >= 2 - alpha ,
> ```
> `2 - alpha = 0.415037499`. (Upper bound proved as in Theorem M3; the lower
> bound is a **sketch** — the straight-line family of slope `min(alpha+theta,2)`
> is admissible because the budget is slack at every `j < N` — and is confirmed
> numerically at `N = 60, 120, 200` for eight values of `theta`.)

So a confinement defect of **any positive linear rate strictly lowers the rate**
(`J(alpha+theta) < I_0`), making a mass-based target harder, and a defect of rate
`>= 2 - alpha` destroys the rate entirely. `2 - alpha` is exactly the
unconditional mean drift of `S_j - alpha j`, measured at `+0.4149` in the
repository's own `scratch/center_audit_2026-09-14` §4.2.
