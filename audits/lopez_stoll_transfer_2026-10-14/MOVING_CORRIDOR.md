# MOVING_CORRIDOR.md — what survives when the band moves

The brief asks what can be proved for `epsilon_N -> 0` and insists that a
fixed-`epsilon` asymptotic must not be substituted into a moving-`epsilon`
regime without proving uniformity. This file states the uniformity that is
available, the range of `epsilon_N` it covers, and the point at which it stops.

---

## 1. Where the non-uniformity is

Theorem M4 of `MASS_CONCENTRATION.md` reads
`P[S_N <= (alpha-eps)N | C_N] <= 2^{-N[J(alpha-eps) - I_0] + o(N)}`. Two `o(N)`
terms enter:

* the Stirling estimate `C(aN-1,N-1) = 2^{aN H_2(1/a) + O(log N)}`, whose
  `O(log N)` is **uniform** in `a` on compact subsets of `(1,2)`;
* `p(N,0) = 2^{-I_0 N + o(N)}` from `confined_mass_rate`, whose `o(N)` is a
  `Tendsto` statement with **no rate at all** — it is the limit of a sequence,
  and nothing in `Rate.lean` converts it into an explicit error.

The second is the binding one. The repository does, however, give an explicit
**sandwich** that can replace it, and that is what makes §2 possible.

> **Lemma U1 [PRIOR, `Rate.lean` `le_p`, `p_le`].**
> `tt(N,sN)/N <= p(N,0) <= (sN(N)+1) tt(N,sN)`, where
> `tt(N,s) = C(s-1,N-1) 2^{-s}` and `sN(N) = floor(N log_2 3)`.
> Validated here against an independent exact-rational DP at
> `N = 4,8,...,96`, **0 violations**.

So `p(N,0) = tt(N,sN) * N^{\pm 1} * O(1)`: the `o(N)` in the denominator is in
fact `O(log N)`, explicitly.

## 2. The moving-band estimate that is provable

> **Theorem U2 [P].** There are absolute constants `c_1, c_2` such that for every
> `N >= 2` and every `eps` with `0 < eps <= alpha - 1`,
> ```
>    P[ S_N <= (alpha - eps) N  |  C_N ]
>         <=  c_1 N^{2} * 2^{-N [ J(alpha - eps) - I_0 ]} .
> ```
> *Proof.* Numerator: `P[S_N <= (alpha-eps)N] = sum_{t<=(alpha-eps)N} C(t-1,N-1)2^{-t}`,
> at most `(alpha-eps)N` terms each `<= max_t tt(N,t) <= c * 2^{-N J(alpha-eps)}`
> by monotonicity of `J` on `[1,2]` and the uniform Stirling bound. Denominator:
> `p(N,0) >= tt(N,sN)/N >= c' N^{-1} 2^{-I_0 N}` by Lemma U1 and
> `|J(sN/N) - J(alpha)| = O(1/N)` (`J` is Lipschitz on compacts and
> `sN(N)/N = alpha + O(1/N)`). Multiply. ∎

**The allowed range of `eps_N`, stated exactly.** Theorem U2 is informative
precisely while its exponent beats the polynomial prefactor:
```
    N [ J(alpha - eps_N) - I_0 ]  >=  (2 + delta) log_2 N      for some delta > 0 .
```
`J` has the closed form `J(s) = s - s log_2 s + (s-1) log_2(s-1)`, hence
`J'(s) = 1 + log_2((s-1)/s)` and
```
    kappa := -J'(alpha) = -1 - log_2((alpha-1)/alpha) = 0.438032659 ,
    J(alpha - eps) - I_0 = kappa eps + O(eps^2)
```
(checked: the difference quotient `(J(alpha-eps)-I_0)/eps` is `0.445874,
0.453841, 0.466002, 0.508903` at `eps = 0.01, 0.02, 0.034963, 0.084963`,
decreasing toward `kappa` as `eps -> 0`; and `J(alpha)` agrees with
`I_0 = 0.079318612775` to all 12 digits in both forms). So the condition is
`eps_N >= (2+delta) log_2 N / (kappa N)`, i.e.

> **Corollary U3 [P].** Theorem U2 is non-vacuous exactly for
> ```
>     eps_N  >>  log N / N ,
> ```
> i.e. for moving deficits `Delta_N >= eps_N N` with `eps_N N >> log N`. In
> deficit coordinates: **the conditioned measure gives an exponential penalty
> for `Delta_N >> log N`, and nothing for `Delta_N = O(log N)`.**

## 3. The barrier, and why it is the same barrier as everywhere else

Corollary U3's reach is `Delta_N >> log N`. That is **exactly** the reach of the
deterministic barriers of `PRIOR_DETERMINISTIC_BARRIERS.md` §2 (coefficients
`8/9`, `1.0358567`) and of Theorem R of `CRITICAL_RETURN_CARRY.md` (whose
`sum_i 2^{-Delta_i} < infinity` fails precisely at `Delta_i <= log_2 i`).

> **Three independent routes — aggregate conditional measure, finite-prefix
> harmonic packing, and the carry identity — all stop at the same place,
> `Delta ~ log N`.** The coincidence is not accidental: all three are driven by
> a `sum 1/k`-type budget. The conditional estimate's prefactor is polynomial
> because `p(N,0)` carries a polynomial prefactor; the packing bound's is
> polynomial because `sum_{k<N} 1/m_k <= 7/3 + (1/3) log N`; and the carry
> bound's is polynomial for the same reason, being the same sum.

## 4. What is *not* proved, and is not claimed

* **No moderate-deviation theorem.** A genuine moderate-deviation statement
  (`Delta_N ~ sqrt(N)`, Gaussian window) would need the local CLT for the
  conditioned walk, i.e. a Brownian-meander limit for the geometric walk
  conditioned to stay under the line. That is standard in shape but was **not
  derived here**, and without it the regime `log N << Delta_N << N` has no
  estimate in this package.
* **No pathwise content.** Theorems U2/U3 are statements about the measure on
  words conditioned on `C_N`. Witness **W1** of `TWO_CLOCK_TRANSLATION.md` is a
  0-confined word sitting in the exponentially-penalized region
  (`Delta_N = (alpha-1)N`) at **every** `N`; the penalty is a statement about
  how many such words there are, not about whether a given orbit is one of them.
  **The moving-corridor estimate is therefore not a return theorem**, and this
  is the same wall recorded in
  `audits/amplification_transfer_2026-10-14/VERDICT.md`.
* **No substitution of fixed-`eps` results.** Theorem M4 is used nowhere with
  `eps` depending on `N`; Theorem U2 is the only moving-band statement here and
  it carries its prefactor explicitly.
