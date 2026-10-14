# ASYMPTOTIC_BUDGET.md — every gain and loss exponent

All exponents are in bits per step of the accelerated orbit, i.e. coefficients
of `N`. `alpha = log_2 3 = 1.584962500721`,
`I_0 = 0.079318612775`, `g = alpha - I_0 = 1.505643887946`.

---

## 1. The ledger

| quantity | exponent | source | status |
|---|---|---|---|
| mass of the whole `0`-confined population, `mu(C_N) = p(N,0)` | `-I_0 = -0.0793186` | `Occupation.confined_mass_rate` | source-backed Lean |
| number of `0`-confined words, `n_N` | `+g = +1.5056439` | `#C_N = 2^{sN} p(N,0)`, Theorem B | proved here (exact bridge) + source-backed rate |
| realizer modulus, `log_2 2^{S_N+1}` | `+alpha` (max), `>= +1` | `S_N <= sN(N)`, `d_i >= 1` | source-backed (`Realizer.lean`) |
| mass of **one** cylinder (one seed's own class) | `-alpha = -1.5849625` | `2^{-S_N}`, sharp congruence | source-backed |
| index surplus of the down-shift transformation, `delta_N` | `O(log N / N) -> 0` | `JOINT_INVERSE_ATTEMPT.md` Theorem 4 | proved here |
| fibre cost of the down-shift, `max fibre` | `<= (alpha-1)N(N+1)/2`, tight to `11%` | same | proved here + audited |
| multiplicity of word `->` realizer class | `0` exactly (multiplicity `1`) | `leastRealizer_unique`; Theorem 3 | source-backed + verified `N<=14` |
| required index surplus for `(AMP*)` | `+delta`, any fixed `delta > 0` | `AMPLIFICATION_CRITERION.md` §4 | definition |
| confinement-budget drift that annihilates the rate | `2 - alpha = 0.4150375` | §6 below | proved here + numerically confirmed |
| one-step drift of `S_j - alpha j` under past-only confinement | `+0.4149` measured | repo `center_audit_2026-09-14` §4.2 | source-backed measurement |

## 2. The efficiency inequality, derived

`(AMP*)` is satisfiable only if, for some fixed `delta > 0` and infinitely many
`N`,

```
   (log_2 #I_N)/N  -  (log_2 max fibre)/N   >=   g + delta .
```

By Theorem 5 of `JOINT_INVERSE_ATTEMPT.md` the two terms obey
`(log_2 #I_N)/N <= (log_2 n_N)/N + (log_2 max fibre)/N`, so the left side is at
most `(log_2 n_N)/N = g + o(1)`. **The efficiency inequality therefore reads
`g + o(1) >= g + delta`, which fails for every fixed `delta > 0`.** This is the
exact analogue of the paper's `(U+m)/H -> 0` accounting, and it comes out the
wrong way round: in percolation gain and cost are both linear in `k` with the
*ratio* contracting by a fixed factor `c_ξ < 1`; here gain and cost are the same
quantity and the ratio is identically `1`.

## 3. Where the paper's financing comes from, and what EOC has instead

The percolation amplification is financed by `pi = P_{p_c}(n <= s_o < 2n) >= n^{-beta}`
with `beta < 1/2` forced by `beta + s < 1`, `s = 1/2 + eps` (proof of
Prop. 4.3). Translating to EOC currency by matching the scale `n <-> 2^N`:

| object | available mass | `beta_eff` | satisfies `beta < 1/2`? |
|---|---|---|---|
| the whole `0`-confined population | `2^{-I_0 N} = n^{-I_0}` | `0.0793` | **yes** |
| one seed's own cylinder | `2^{-alpha N} = n^{-alpha}` | `1.5850` | **no**, by a factor `3.17` |

**This is the quantitative statement of the aggregate/pointwise gap in the
paper's own currency, and it is the single most useful number this
investigation produced.** The aggregate confined population is *polynomially
heavy* in exactly the paper's sense and would finance the construction; a single
persistent seed is *exponentially light* and does not. The shortfall is
`n^{alpha - 1/2} = 2^{1.085 N}` — exponential, not a constant to be optimised.

To close it, an amplification would have to lift the available mass from
`n^{-alpha}` to `n^{-I_0}`, i.e. amplify by `n^{alpha - I_0} = n^{g} = 2^{1.5056 N}`
— which is *recovering the entire confined population from one seed*. And by
Theorem 1 even total success would gain nothing: the recovered population is
`C_N`, whose mass is exactly the rate being contradicted. The target is
simultaneously the maximum conceivable and strictly insufficient.

## 4. The spectral seed is structurally unavailable

Proposition 4.3 needs a starting map with `H = log(1/||K||) > 1`. Lemma 4.4
supplies it from `rho < 1`, the spectral radius of the symmetric walk, which
exists because the graph is **nonamenable**.

> **Proposition S.** Let `O` be a finite set and `K : O x O -> [0,infinity)` a
> kernel with all row sums and all column sums equal to `1` (Definition 4.2's
> normalization, after the transport identity). Then `||K||_{l^2(O)} = 1`
> exactly, so `H = 0` and `H > 1` is impossible.
>
> *Proof.* The constant vector `1` lies in `l^2(O)` because `O` is finite, and
> `K1 = 1`, so `||K|| >= 1`. Conversely `K` is doubly stochastic, so by the
> Schur test with unit weights `||K|| <= sqrt( max_x Σ_y K(x,y) · max_y Σ_x K(x,y) ) = 1`. ∎

At every finite depth `N` the natural EOC state space is the **finite** set of
odd residues mod `Q_N` — and it must be finite for `mu` and `p(N,c)` to mean
what `confined_mass_rate` says they mean. So the seed of the entire percolation
construction is unavailable on the space where the rate lives. The paper needs
its orbit `O` to be infinite precisely so that `1 ∉ l^2(O)`.

Moving to the infinite space (all positive odd integers at once) does not help:
there "confined to depth `N`" is not a property of a residue class, `Q_N` and
`mu` do not exist, and `p(N,c)` is not the measure of anything — one has left
the framework in which `I_0` is proved. The brief's own caution applies, and is
sharper than it looks: *"A stochastic operator on a finite residue space has a
constant-vector eigenvalue one. Therefore a claimed full-space contraction
requires particular scrutiny."* Proposition S is that scrutiny, and the answer
is that no contraction exists, for any kernel, not merely for the obvious ones.

A centred or killed operator could have norm `< 1`, but then it is no longer the
endpoint kernel of a local map with success probability `u`, and the
`u`/`M`/`r` accounting of Lemma 4.9 — which is what makes the iteration
contract — does not apply to it. Defining such an operator and justifying its
relevance to positive-integer realizability was not achieved here and is not
claimed.

## 5. Weak asymptotics: the two sides, kept apart

The brief asks whether a subpower bound would suffice, as it does in the paper.
The two sides have **different** requirements and must not be conflated.

**Upper-localization side.** A variance loss of `2^{o(N)}` preserves the
exponent `alpha - g/2 = 0.8321405567` of the previous round's conditional chain,
*when* the counting and localization inputs hold. That chain is
`SUM-PAIR at h_N => mu_2 <= (1+CN^B)E => B_{h_N} <= … => log_2 r_min <= 0.8321 N + o(N)`.
Subpower losses are harmless there, which is why `N^B` factors appear
throughout it. **It is an upper bound on `r_min`, consistent with a persistent
seed, and says nothing about divergence.**

**Divergence-exclusion side.** Here a subpower loss is *not* harmless in the
same way, because the quantity that must be beaten is itself exponential with a
small exponent. `(AMP*)` tolerates `N^B` or even `2^{o(N)}` fibres — that part
is genuinely weak-asymptotics-friendly — but it demands a *fixed exponential*
index surplus `2^{delta N}`. Theorem 4 gives `poly(N)`. So on this side the
subpower tolerance is in the fibre bound, where it is free, and the hard demand
is in the index set, where nothing subpower will do.

**No statement proved here about typical windows or random residues is
described as pointwise divergence exclusion.** Proposition W of
`EOC_DIVERGENCE_TARGET.md` §6 is an exact identity about a product law on letter
strings; the bridge from it to a fixed integer's orbit is the missing lemma of
§7 below, not a corollary.

## 6. The price of a drifting confinement budget

`confined_mass_rate` is proved for **fixed** `c`. This section prices the only
escape from Theorem 1.

> **Proposition D.** Let `J(a) = a(1 - H_2(1/a))` for `1 <= a <= 2`, so
> `J(1) = 1`, `J(alpha) = I_0`, `J(2) = 0`, and `J` is decreasing. With
> `c = c(N) = floor(theta N)`,
> ```
>    -(1/N) log_2 p(N, c(N))  ->  J(alpha + theta)   for 0 <= theta < 2 - alpha,
>    -(1/N) log_2 p(N, c(N))  ->  0                  for theta >= 2 - alpha .
> ```
>
> *Proof sketch.* By Proposition W, `p(N,c) = P[S_j <= alpha j + c, j <= N]` for
> i.i.d. Geometric(1/2) letters of mean `2`. Upper bound: drop all constraints
> but `j = N`, so `p(N,c) <= Σ_{s <= (alpha+theta)N} C(s-1,N-1) 2^{-s}`; each
> term is `2^{-N J(s/N) + O(log N)}` and `J` is decreasing on `[1,2]`, so the sum
> is `2^{-N J(alpha+theta) + O(log N)}` when `alpha + theta < 2`, and `O(1)` when
> `alpha + theta >= 2`. Lower bound: restrict to words whose partial sums follow
> the straight line of slope `min(alpha+theta, 2)`, which is admissible because
> the budget `theta N` is slack at every `j < N` and tight only at `j = N`; the
> resulting count is `2^{-N J(alpha+theta) - O(log N)}`. ∎

Numerically confirmed by exact-rational computation of `p(N, floor(theta N))`
(`scripts/rate_checks.py` check (3)), the finite-`N` rate decreasing monotonely
toward the prediction at every `theta`:

| `theta` | `J(alpha+theta)` | `N=60` | `N=120` | `N=200` |
|---|---|---|---|---|
| `0.00000` | `0.079318613` | `0.1777763` | `0.1392782` | `0.1206370` |
| `0.10000` | `0.042740307` | `0.0978516` | `0.0735820` | `0.0630918` |
| `0.30000` | `0.005067463` | `0.0350178` | `0.0217155` | `0.0161511` |
| `0.41504` | `0.000000000` | `0.0173852` | `0.0085328` | `0.0052381` |
| `0.80000` | `0.000000000` | `0.0006425` | `0.0000371` | `0.0000016` |

The convergence is slow because `p(N,c)` carries a `poly(N)` prefactor — the
same prefactor visible in the repository's own sandwich
`tt/N <= p <= (sN+1) tt` (validated here with 0 violations) — but it is monotone
and unambiguous in every column.

**Three consequences for any amplification with a controlled defect.**

1. `c = o(N)` leaves the rate at `I_0`: Theorem 1 applies verbatim.
2. `c = theta N`, `theta > 0`, lowers the rate to `J(alpha + theta) < I_0`, so
   the `eps` that must be beaten *shrinks*. **A linear defect makes the target
   strictly harder.**
3. `theta >= 2 - alpha = 0.4150375` kills the rate entirely, but a budget
   growing at `0.415` bits per step is no longer a confinement hypothesis: the
   drift `2 - alpha` is exactly the unconditional mean drift of
   `S_j - alpha j`, measured at `+0.4149` in the repository's own audit. At that
   budget the constraint is asymptotically vacuous and the objects it describes
   are not zero-confined in any sense bearing on the target.

The escape is closed in the only direction that would have helped.

## 7. What a usable gain would have to look like

Collecting §2, §3 and §6, a useful amplification step must satisfy, for some
fixed `delta > 0` and all large `N`:

```
   log_2 ( new distinct confined realizers produced )
        -  log_2 ( inverse multiplicity )
        -  ( confinement budget consumed, in units of the rate )
   >=  g N + delta N ,
```

with the budget term `o(N)` by §6.2, the multiplicity term `o(N)` being free,
and the first term therefore required to exceed `(g + delta)N` on its own —
i.e. to exceed the total number of confined realizers that exist. By Theorem 1
that is impossible if the objects produced are confined, and by Theorem 5 the
first two terms cannot be separated. **There is no admissible region.**
