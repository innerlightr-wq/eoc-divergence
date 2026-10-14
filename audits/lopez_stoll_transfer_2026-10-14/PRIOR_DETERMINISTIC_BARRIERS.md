# PRIOR_DETERMINISTIC_BARRIERS.md — what is already excluded, and under what hypotheses

Sources: `eoc-lean-verification@6057a0d` (clean), `eoc-divergence@938dcc0`
(clean). **No Lean compilation was run in this session**; every entry is
**source-backed** by reading the file, never "Lean-verified here". Sign
convention: the repository's `R_n = S_n - alpha n = -Delta_n`, so a *lower drift
floor* `R_n >= -B log_2(n+1) - C` is an *upper* bound `Delta_n <= B log_2(n+1) + C`.

---

## 1. Bounded drift and the realizer escape

`EOC/BoundedDrift.lean`:

| theorem | statement | hypotheses |
|---|---|---|
| `orbit_step` | `2^{a(m_i)} m_{i+1} = 3 m_i + 1` | — |
| `evPeriodic_of_noninj` | a repeated state makes the orbit eventually periodic | `m_i = m_j`, `i<j` |
| `noninjective_orbit_not_upper_confined` | **Case A**: a non-injective orbit is not permanently upper-confined | `Odd m_0` |
| `injective_orbit_no_lower_drift` | **Case B**: an injective orbit has no integer lower drift bound | `Odd m_0`, integer bound `G_n` |
| `three_pow_le_of_drift` | `R d N >= -G` for all `N` forces a power inequality | `∀N, -G <= R d N` |
| `leastRealizer_unbounded_of_int_drift` / `..._two_sided_drift` | bounded-drift words have unbounded least realizers | `∀i, 1 <= d i`, two-sided drift bounds |

**Net.** Every accelerated orbit is non-injective (hence eventually periodic) or
injective (hence divergent); in both branches a **bounded** drift corridor is
excluded. So statement **G** of `TWO_CLOCK_TRANSLATION.md` is closed for
positive-integer orbits — **but not symbolically**: witness **W4** is a
0-confined word with `max Delta_N = 1.00` through `N = 4000`. The exclusion is
arithmetic, and it comes from distinctness of integer states.

## 2. Finite-prefix packing and the logarithmic corridor

`EOC/FinitePrefixPacking.lean`, `EOC/LogCorridor.lean`, `EOC/HarmonicPacking.lean`:

* `finite_prefix_injective_drift_depth_bound` — finite-prefix injective
  drift-depth bound; the `B = 0` coefficient quoted in the public repository is
  **`2 - log_2 3 = 0.4150374993`**. Hypotheses: injectivity of the orbit segment
  on `[0,N)`, a drift floor over **every** prefix, a fixed odd seed.
* `logFloor_window_bound'` — **quantitative, unconditional**: if `orbit M` is
  injective on `[0,N)` and `R_k >= -B log_2(k+1) - C` for **all** `k < N`
  (`B >= 0`), then
  ```
     N^{8/9 - B}  <=  3 e^{7/9} * 2^C * M ,        3 e^{7/9} = 6.529890 .
  ```
  So the `B = 0` coefficient here is **`8/9`**, "versus `2 - log_2 3` from row V"
  (the file's own comparison).
* `sum_inv_orbit_le` — **the pigeonhole behind all of it**: if `m_0,...,m_{N-1}`
  are pairwise distinct then `sum_{k<N} 1/m_k <= 7/3 + (1/3) log N`. Mechanism:
  post-initial states are distinct integers **coprime to 6**
  (`orbit_succ_coprime_six`, `three_not_dvd_orbit_succ`), packed against
  `sum 1/(3j+1)`.
* `HarmonicFloor.R_le_of_nondescent_harmonic` — under non-descent with distinct
  states, `R_N <= (1/9) log_2(1 + 3N/(M-2)) + 2/(3 ln 2 (M-2))`.
* `LogCorridor.exits_logCorridor` — no odd seed stays in a logarithmic corridor
  forever, for `B < 8/9` **unconditionally**.

**Hypotheses actually required** (the brief asks explicitly): injectivity of the
orbit segment **yes**; a drift floor over **every** prefix **yes** — this is what
Theorem R of `CRITICAL_RETURN_CARRY.md` weakens; a fixed seed **yes** (`M`
appears in the bound); an asymptotic sequence of depths **no** (the bounds are
finite-prefix); additional collision-free or divergence assumptions **no** for
the `8/9` results, **yes** for §3.

## 3. The external Garcia-Tal / Curry input

From `eoc-lean-verification/README.md`, recorded there as **manuscript-level,
not Lean**, and here as **source-reported, not read in this session**:

* **Garcia-Tal (1999)**: qualitative Banach-density-zero for aperiodic/infinite
  orbits via a collision-free windowed pigeonhole. **No explicit exponent.**
* **Curry (2026)**, Theorem 2.3: for a collision-free set `A` and every
  `beta > beta*`, `#(A ∩ [a,a+X)) <= C_beta X^beta log(2X)` uniformly in `a`,
  with
  ```
     beta* = gamma* log_2 3 = H(gamma*) ~ 0.9653844 ,   gamma* ~ 0.6090897 ,
  ```
  `gamma*` identified with Rozier's critical ones-ratio `r_H`.
* **Curry Proposition 3.1**: an infinite aperiodic orbit's value set is
  collision-free, so **`sum_n 1/m_n < infinity` for a divergent orbit**, hence
  `E_N` stays **bounded**. *This is the input used by Corollary R1.*
* **Curry Theorems 4.1, 4.2, Corollary 4.3**: exclude every eventual logarithmic
  drift floor `R_n >= -B log_2 n + O(1)` for `B < 1/beta* ~ 1.0358567`, crossing
  the harmonic threshold `B = 1`.

The repository is explicit that this enters its Lean development only as the
hypothesis `LogFloorExclusion Bstar` — "a `Prop`, never an axiom" — and that the
`1.0358567` assessment is Curry's own literature claim, not independently
verified there or here.

## 4. Occupation rate

`eoc-divergence/Occupation/Rate.lean:478` `confined_mass_rate (c)`:
`-(1/N) log_2 p(N,c) -> I_0 = 0.079318612775`, for each **fixed** `c`.
Dependencies: `Occupation/{Compositions,Entropy,CyclicLemma}.lean`. These four
files declare no `sorry`/`admit`/`axiom`/`opaque`, and
`eoc-divergence/scripts/OccupationAxioms.lean` exists to print the axioms of the
theorem — **that script was not executed here.**

## 5. What remains possible after all of the above

Collecting §§1-4 against the lattice of `TWO_CLOCK_TRANSLATION.md`:

```
   G  (Delta bounded)                     CLOSED   [PRIOR, §1]
   F  (Delta = O(log N)), coeff < 8/9     CLOSED   [PRIOR, §2, unconditional]
   F           coeff < 1.0358567          CLOSED   [PRIOR + Curry, §3, external]
   constant-width returns i.o.            CLOSED   [P, Cor. R1 + Curry]
   ------------------------------------------------ the frontier -----------
   log-width returns i.o.                 OPEN
   sublinear-width returns (sqrt N) i.o.  OPEN
   E  (Delta = o(N))                      OPEN
   D  (liminf Delta/N = 0)                OPEN, and NOT forced (W1; and [2021] fails audit)
```

**The target genuinely beyond bounded drift and finite-prefix packing is
therefore the sublinear-width return regime**, `w(N) = N^{theta}` with
`0 < theta < 1`, infinitely often. Everything proved here is vacuous there, for
the structural reason given in `CRITICAL_RETURN_CARRY.md` §3: the only mechanism
available — harmonic packing of distinct integers coprime to `6` — produces a
`log`-sized budget, and `2^{w(N)}` with `w` sublinear-but-superlogarithmic
swamps it.
