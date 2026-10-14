# EOC_DIVERGENCE_TARGET.md — the exact pointwise objective and the proved rate

Everything here is recovered from the repository sources, not from memory.
Source commits: `eoc-divergence` `938dcc0` (branch `main`, clean),
`eoc-lean-verification` `6057a0d` (branch `main`, clean). Nothing in either
checkout was modified.

---

## 1. Conventions, verified against the sources

Accelerated odd map, `EOC/Realizer.lean` and `Divergence/`:

```
   T(m) = (3m+1) / 2^{v_2(3m+1)} ,       m odd  ==>  T(m) odd .
```

A valuation word of length `N` is `d = (d_1,…,d_N)`, `d_i >= 1`, with partial
sums `S_j = d_1 + … + d_j`. **Zero confinement** is, in the integral form the
repository uses (`Occupation/Compositions.lean`, `def Confined`):

```
   Confined c d   <->   for all j <= N:   2^{S_j} <= 2^c · 3^j ,
```
and zero confinement is `c = 0`: `2^{S_j} <= 3^j`. The integral form is used
throughout here; **no floating-point logarithm decides confinement anywhere in
this package.**

`Occupation.sN N = Nat.log 2 (3^N) = (3^N).bit_length() - 1 = floor(N·alpha)`,
`alpha = log_2 3`. A `0`-confined word has `S_N <= sN N`
(`confComps_eq_empty_of_gt`).

**Realizer modulus `2^{S_N+1}` and terminal oddness, verified.**
`EOC/Realizer.lean`:

* `realizerCongruence` (l. 286): for odd `m_0` and `d_i >= 1`,
  `Realizes d N m_0  <->  3^N·m_0 + q_N ≡ 2^{S_N} (mod 2^{S_N+1})`, with the
  carry `q_0 = 0`, `q_{j+1} = 3 q_j + 2^{s_j}`.
* `leastRealizer_unique` (l. 478): **exactly one** `x < 2^{S_N+1}` satisfies that
  congruence.
* `residue_pinning` (l. 543): if `m_0 < 2^{S_N+1}` then `m_0` *is* that unique
  least realizer of its own orbit word.

So: **one `0`-confined word of length `N` <-> exactly one odd residue class mod
`2^{S_N+1}`.** Multiplicity one, both directions. Verified independently by
brute force for `N = 1..14` in `scripts/bridge.py` (max fibre `= 1`, 0
violations) — see `results/bridge.log`.

## 2. The three statements, kept apart

**A. Aggregate confinement decay.** The density of eligible odd residues that
are `c`-confined through depth `N` decays at exponential rate `I_0`. *This is
what is proved.*

**B. Upper localization.** At each finite depth there is a relatively small
confined positive odd seed, e.g. `log_2 r_min(N,0) <= 0.8321… N + o(N)` under
the conditional chain of
`the growing-scale-pairs round (local scratch, not published)VERDICT.md`. *Conditional,
and an upper bound.*

**C. Pointwise escape.** *Every* fixed positive odd seed eventually fails zero
confinement. **This is the objective.**

`A` does not give `C`: a rate for the measure of a shrinking family says nothing
about one fixed point of the space, and a measure-zero exceptional set is
exactly what a single persistent seed would be. `B` does not give `C`: an upper
bound on the smallest confined seed is *consistent* with a persistent seed and
in fact is what a persistent seed would supply.

**The exact equivalence, recovered rather than assumed.** Write

```
   W(N,X) = #{ m odd, m < X : 2^{S_j(m)} <= 3^j for all j <= N } ,
   r_min(N,0) = least  0-confined-to-depth-N positive odd seed .
```

Then, immediately from the definitions:

> **Lemma T.** The following are equivalent.
> 1. Some positive odd `m` is `0`-confined at every depth (a *persistent seed*).
> 2. `r_min(N,0)` is bounded in `N`.
> 3. There is `X_0` with `W(N,X_0) >= 1` for every `N`.
>
> Hence `C` <=> `r_min(N,0) -> infinity` <=> for every `X_0`, `W(N,X_0) = 0`
> for all large `N`.

*Proof.* (1)=>(2): such an `m` is counted at every depth, so
`r_min(N,0) <= m`. (2)=>(3): take `X_0` = the bound + 1. (3)=>(1): the sets
`{m < X_0 : m is 0-confined to depth N}` are finite, nonempty and decreasing in
`N`, so their intersection is nonempty. ∎

**This is an equivalence with the divergence target, not with Collatz.** A
persistent zero-confined seed is a seed whose accelerated orbit never lets
`2^{S_j}` exceed `3^j`; excluding it is EOC's pointwise divergence-exclusion
statement. It is *not* the Collatz conjecture, and nothing below is strengthened
into one.

## 3. The proved arithmetic mass budget

`eoc-divergence/Occupation/Rate.lean` l. 478:

```lean
theorem confined_mass_rate (c : ℕ) :
    Tendsto (fun N => -(1 / (N:ℝ)) * Real.logb 2 (p N c)) atTop (𝓝 I₀)
```

with, from the same file,

```lean
noncomputable def alpha : ℝ := Real.logb 2 3
noncomputable def I₀ : ℝ := alpha * (1 - Real.binEntropy (1 / alpha) / Real.log 2)
```

i.e. `I_0 = alpha (1 - H_2(1/alpha))` in bits, and from
`Occupation/Compositions.lean` l. 217,

```lean
noncomputable def p (N c : ℕ) : ℝ := ∑ d ∈ confWords N c, (2:ℝ)⁻¹ ^ psum d N
```

so `p(N,c) = Σ over c-confined words d of length N of 2^{-S_N(d)}`.

```
   alpha = 1.584962500721 ,   I_0 = 0.079318612775 ,   g := alpha - I_0 = 1.505643887946 .
```

**Quantifiers, read off the statement.** The limit is for **each fixed `c`**;
`c` is bound *outside* the `Tendsto`. There is no uniformity in `c`, and §6 of
`ASYMPTOTIC_BUDGET.md` shows that the rate genuinely degrades once `c` grows
with `N`, so nothing may be inferred for a moving confinement parameter. The
conclusion is `p(N,c) = 2^{-I_0 N + o(N)}`.

**Status label.** `Occupation/{Compositions,Entropy,CyclicLemma,Rate}.lean`
declare no `sorry`, `admit`, `axiom` or `opaque`, and
`eoc-divergence/scripts/OccupationAxioms.lean` exists to print the axioms of
`confined_mass_rate`. **Nothing was compiled in this session.** This package
therefore labels the theorem **source-backed**, never "Lean-verified here".

## 4. The bridge from symbolic mass to residue density — exact, and verified

Put `Q_N = 2^{sN(N)+1}` and let `mu` be normalized counting measure on the odd
residues mod `Q_N` (there are `2^{sN(N)}` of them). Let

```
   C_N = { m odd mod Q_N : 2^{S_j(m)} <= 3^j for all j <= N } .
```

> **Theorem B.** `mu(C_N) = p(N,0)` **exactly**, for every `N`. More generally
> `mu(C_N^{(c)}) = p(N,c)` with the obvious `c`-confined set, provided
> `c + sN(N) + 1 <= log_2 Q_N`.

*Proof.* Confinement to depth `N` depends only on `d_1,…,d_N`, which by
`realizerCongruence` depend only on `m` mod `2^{S_N+1}`, and `S_N <= sN(N)`, so
`C_N` is well defined mod `Q_N`. By `leastRealizer_unique` each `0`-confined
word `d` is realized by exactly one class mod `2^{S_N(d)+1}`, which splits into
`2^{sN - S_N(d)}` classes mod `Q_N`. Distinct words give disjoint sets of
classes, since the class determines the word. Hence

```
   #C_N = Σ_{d confined} 2^{sN - S_N(d)} = 2^{sN} Σ_d 2^{-S_N(d)} = 2^{sN} p(N,0),
```
and dividing by `2^{sN}` gives the claim. ∎

**Verified by brute force, `N = 1..14`**, by enumerating every odd residue mod
`Q_N` and iterating the map: `#C_N`, `2^{sN} p(N,0)` and `Σ_d 2^{sN-S_N}` agree
exactly at every `N`; 0 violations (`scripts/bridge.py`, `results/bridge.log`).
E.g. `N = 14`: `sN = 22`, `Q_N = 8388608`, `#C_N = 168807 = 2^{22} p(14,0)`,
`#words = 51033`.

**Consequence used throughout:**

```
   mu(C_N) = 2^{-I_0 N + o(N)} ,        #{0-confined words of length N}
                                          = n_N = 2^{g N + o(N)} ,  g = alpha - I_0 .
```

(`n_N` from `#C_N = 2^{sN} p(N,0)` and the fact that the mass concentrates at
`S_N ≈ alpha N`; `log_2 n_N / N` measured `= 1.4481` at `N = 200` against
`g = 1.5056`, the gap being the `O(log N / N)` correction visible in the Lean
sandwich of §5.)

## 5. An independent check of the repository's own sandwich

`Rate.lean` proves `le_p` and `p_le`, i.e.
`tt(N,sN)/N <= p(N,0) <= (sN+1)·tt(N,sN)` with `tt(N,s) = C(s-1,N-1) 2^{-s}`.
An exact-rational dynamic program written here from the *definition* of
`Confined` confirms both inequalities at `N = 4,8,…,96` with **0 violations**
(`scripts/rate_checks.py` check (1)). This validates the DP against the
repository and the repository's bound against an independent computation.

## 6. One identity that makes the rate transparent

> **Proposition W.** `p(N,c) = P[ S_j <= alpha j + c for every j <= N ]`, where
> `S_j = d_1+…+d_j` and the `d_i` are i.i.d. with `P[d = k] = 2^{-k}`, `k >= 1`
> (Geometric(1/2), mean `2`).

*Proof.* The weight `2^{-S_N(d)} = Π_i 2^{-d_i}` is exactly the probability of
the letter string `d` under that product law, and `Σ_{all words} 2^{-S_N} = 1`.
Confinement `2^{S_j} <= 2^c 3^j` is `S_j <= alpha j + c` (both sides integers vs
a real line; the integral form is the one used). ∎

**Verified exactly** on 27 pairs `(N,c)`, `N <= 30`, `c in {0,1,3}`, by an
independent transfer matrix over exact rationals: 0 mismatches
(`scripts/rate_checks.py` check (2)).

This is **not an analogy**: the dyadic mass *is* that probability. It is why
`I_0 = J(alpha)` with `J(a) = a(1 - H_2(1/a))` — the Cramér rate for the walk
to keep slope `alpha` against its mean `2` — and it is the exact source of the
drift budget `2 - alpha = 0.415037…` that reappears in
`ASYMPTOTIC_BUDGET.md` §6. The repository's own `center_audit_2026-09-14`
measured the one-step drift under past-only confinement conditioning at
`+0.4149`, matching `2 - alpha` to three decimals.

**What the identity does *not* do.** It is a statement about the product law on
letter strings, i.e. about the *aggregate*. The actual orbit of a fixed `m`
produces one deterministic letter string. Proposition W therefore says nothing
pointwise, and asserting that a particular orbit's valuations behave like the
i.i.d. law is precisely the open Tao-type input, not a consequence of anything
here.
