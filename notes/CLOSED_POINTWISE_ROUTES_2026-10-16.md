# Closed Pointwise Routes — 16 October 2026 additions

**Compiled 2026-10-16.** Three further audited negative results, continuing
[`CLOSED_POINTWISE_ROUTES_2026-10-14.md`](CLOSED_POINTWISE_ROUTES_2026-10-14.md)
and [`CLOSED_POINTWISE_ROUTES_2026-09-29.md`](CLOSED_POINTWISE_ROUTES_2026-09-29.md).
Same discipline: each entry says *this specific route, under the hypotheses
currently proved in this programme, does not yield a pointwise separator*, and
gives the exact obstruction. **No entry claims that no conceivable variant of the
idea can ever work**, and none of this bears on the Collatz conjecture, on `(DE)`,
or on `(PosPC)`, all of which remain exactly as open as before.

Repository states audited: this repository at `b787dfa`, `eoc-lean-verification`
at `6057a0d`, and Revision 8 of the manuscript.

**Three of the entries below record errors made during the audits themselves and
corrected in the same session.** They are kept in the packages rather than edited
away, because in two cases the correction is the result.

---

## 1. Hilbert's tenth problem over ℚ — no transfer

Full package: [`audits/h10_transfer_2026-10-16/`](../audits/h10_transfer_2026-10-16/).

**Scope.** Whether the machinery of the September 2026 OpenAI manuscript *Hilbert's
tenth problem over the rational numbers* supplies a new arithmetic constraint on
the pointwise realizer problem — specifically on the gap between 2-adic
compatibility and realization by an ordinary positive integer.

**Verdict D — no useful transfer.** The conclusion does not depend on whether that
manuscript is correct; it was not verified, and the obstruction is to the transfer.

That proof forces standard-from-nonstandard with three ingredients: **(i)** one
fixed nonzero integer `δ = f(η(a))` that every local obstruction divides to order
`≥ K`; **(ii)** a height estimate `h(s) ≤ H·M(s)^c` over **many** varying contact
primes; **(iii)** a **quadratic** canonical height beating the resulting linear
bound, giving `B² ≪ B` and hence `B = O(1)`. In the realizer setting:

* **(i) fails.** No nonzero integer is divisible by `2^{S_n}` for every `n` when
  `S_n → ∞`; the only candidate, `m₀ − r_n`, needs the `m₀` whose existence is the
  question.
* **(ii) fails.** The realizer set is `{r_N + k·2^{S_N}}`, so for every odd `q`,
  `gcd(2^{S_N},q) = 1` and every residue class mod `q` occurs — verified for
  `q = 3, 9, 27, 81, 243, 5, 7, 11, 13`. One prime, one modulus. This reproves
  §4b of the September index in one line.
* **(iii) is absent.** The structure is the affine reduction `m₀ ↦ m₀ mod 2^{S_n}`
  on `(ℤ₂,+)`, which carries no positive-definite quadratic form.

**And the route was already pre-closed.** The step `M^K | δ, δ ≠ 0 ⟹ M^K ≤ |δ|` is
verbatim the tool Revision 8 §5.3 names as "the only general tool converting
divisibility into a size statement", which Revision 7 §5.3 already showed evaluates
on the confined sector to a restatement of Lemma 2.4. Quantitatively:

> **Lemma O.** Zero-confinement *is* `2^{S_n} ≤ 3^n`, while the generic height is
> `H = max(C_N, 3^N) ≥ 3^N`. Hence `2^{S_N}/H − 1 ≤ 0` identically and `ρ_N ≥ 1`,
> with no arithmetic input beyond confinement.

**The hypothesis that defines the sector is exactly what voids the tool.** On the
*aperiodic* confined sector both horns of the §5.3 dichotomy fail at once: no
periodic collapse to pin `χ`, and a vacuous size branch. Periodic words are decided
by horn one — `[1,2] → m₀ = −5`, `[2,1,1,2] → −103/17`, `[1,1,3] → 19/5`, each exact
and `N`-independent — which is why they were never the hard case.

---

## 2. Temporal differentiation and nonlinear carry structure

Full package: [`audits/temporal_carry_2026-10-16/`](../audits/temporal_carry_2026-10-16/).

**Scope.** Whether the temporal position of a parity/exponent difference carries
arithmetic information about realizers beyond the 2-adic valuation of their
difference, and whether the carry's nonlinear dependence on exponent history
produces irreducible coupling between positions.

**Verdict D, with E for the specific late-stage hypothesis.**

**The nonlinearity is real but structureless.** With
`T_i = Σ_{j>i} 3^{N−1−j}2^{S_j}`,

```
   Δ_i Δ_k C_N = (2^{ε_i} − 1)(2^{ε_k} − 1) · T_k        ⟺        Δ_i Δ_k C_N = Δ_i C_N · Δ_k C_N / T_i
```

verified exactly on 66 600 and 7 200 cases, 0 failures. The second difference is a
*function* of the two first differences. The coupling is the identity
`2^{a+b} = 2^a 2^b` and nothing more. **This closes the higher-difference axis
prospectively**, not case by case.

**There is no residual odd component.** A single bump changes `S_N`, so the two
realizers have different moduli and their difference is not intrinsic; the matched
comparison is the `S_N`-preserving swap `d_i → d_i+1`, `d_k → d_k−1`. Then
`ΔC_N = W_{i,k}`, `v₂(W_{i,k}) = S_{i+1}` exactly, and the intrinsic odd part
`u = (Δr_N / 2^{S_{i+1}}) mod 2^{S_N − S_{i+1}}` satisfies

```
   u ≡ − V_{i,k} · 3^{−N}   (mod 2^{S_N − S_{i+1}}) ,     V_{i,k} = Σ_{j=i+1}^{k} 3^{N−1−j} 2^{S_j − S_{i+1}} ,
```

**exactly** — 36 712 swaps, 0 failures. Temporal position enters only as the index
range of a sum. This does **not** contradict the free-suffix result of the unpublished 14 October
growing-scale-pairs round (its Theorem D: `v₂(β) = σ−1` is exactly the part the word
data determine, the odd part being carried by the two independent suffixes), where
the odd part genuinely is undetermined — confirmed here: it spreads over all odd
classes mod 8.
Determination is bought only by removing the freedom that made the problem hard.

**Correction carried in the package.** The terminal-tip enumeration in this audit
used `N = 11`, `S_N = 22`, which is **not** zero-confined: the cap at `k = 11` is
`⌊11 log₂3⌋ = 17`, and `2²² = 4 194 304 > 3¹¹ = 177 147`. The algebraic results
above are unaffected; every statistic in that run applied to unconfined words and is
superseded by §3.

---

## 3. Zero confinement and realizer lift dynamics

Full package: [`audits/lift_confinement_2026-10-16/`](../audits/lift_confinement_2026-10-16/).

**Scope.** Writing `r_{n+1} = r_n + b_n 2^{S_n}` with `0 ≤ b_n < 2^{d_n}`,
`ℓ_n = 1_{b_n≠0}` and `J(N) = Σ_{n=1}^{N−1} ℓ_n`: whether zero confinement forces
continued changes in the canonical realizer residues.

**Verdict E — obstructed, by an exact finite counterexample pair.** On *complete*
enumerations of genuinely zero-confined words (`2^{S_k} ≤ 3^k` checked at **every**
`k`, exact integer comparisons):

```
   min J(N) = 3      for every N = 6..13     (least realizer r_N = 71, zero-lift plateau N−5)
   max J(N) = N−1    for every N             (all-ones word d ≡ 1, x = −1, never stabilises)
```

Both extremes are occupied at every length, so **zero confinement bounds the lift
count in neither direction.** The all-ones word is exact: `S_n = n`,
`C_n = 3ⁿ − 2ⁿ`, `r_n = 2ⁿ − 1`, `b_n = 1` always.

> This pair is a two-line refutation of any proposed confinement-driven lift-density
> bound, and **"are both extremes of the proposed statistic occupied inside the
> confined sector?" is a cheap reusable test** for future candidates.

**And the target was circular.** `J(∞) = ∞` for every infinite zero-confined word
says exactly that no such word has a nonnegative-integer realizer — which, since
infinite confinement forces `m_n > m₀` for all `n`, is the open problem itself.

**What the lift sequence is.** With `m_n = (3ⁿ r_n + C_n)/2^{S_n}`,

```
   b_n = 0  ⟺  2^{d_n} | 3 m_n + 1 ,        b_n ≡ −(3m_n + 1)·3^{−(n+1)}   (mod 2^{d_n}) ,
```

verified on 7 100 positions. So `J(N)` counts the times the word demands a deeper
2-adic valuation than its running least realizer supplies. Equivalently
`x = −Σ_{j≥0} 3^{−(j+1)}2^{S_j} ∈ ℤ₂` and `b_n` is the binary block of `x` on
`[S_n, S_{n+1})` — which makes the stabilization criterion a triviality rather than
something to reprove. **These are definitions made explicit, not new inequalities.**

**The statistics are uniform blocks plus a weighting artefact.** `b_n` depends only
on `(d_0,…,d_n)` and never on the future, so pooling over full words weights each
prefix by its continuation count — and under confinement that count correlates with
the slack. Counting each confined **prefix once**, the apparent slack effect at
`d_n = 1` collapses from `0.7423, 0.6879, 0.6391, 0.5982` to
`0.5094, 0.5054, 0.4963, 0.5055`, matching the null `1 − 2^{−d_n}`; across all 18
populated `(G_n, d_n)` cells the match is within `±0.021`.

**Corrections carried in the package.** Three claims were made and withdrawn during
the audit, each caught by its own output: a false lemma "`m_n` is always odd, hence
`d_n = 1 ⟹ b_n = 0`, hence `J(N) ≤ S_N − N`" (`m_n` is even at 4 914 of 8 480
positions; minimal counterexample `d = [1]`, `m₀ = 0`); "the minimisers are orbit
prefixes of small integers" (the congruence forces `v₂ ≥ d_j`, not equality, so
congruence words are not orbit words); and "`P(lift)` is flat in the slack".

---

## Common scope note

All three audits are **prefix-local**, and that is now the recurring wall rather
than an incidental feature of any one of them. `r_N` is itself a nonnegative integer
satisfying every congruence of the prefix, so **every finite word is realized** —
the Sturmian/Beatty confined prefix at `N = 30` has
`r₃₀ = 71 106 568 281 083`, a genuine positive-integer orbit reproducing all 30
valuations. Consequently any function of a finite prefix takes the same value on a
realizable and an unrealizable infinite word sharing it. `J(N)`, the carry, the
drift path and the valuation word are all prefix-local.

**A pointwise theorem must therefore supply an estimate uniform in `N` and over the
whole sector, not one verified for finitely many lengths.** §3 shows the natural
such statement (`J(N) ≥ cN` for all confined words) is false.

The quantity flagged in these packages as not obviously prefix-local, and not a
magnitude so not reached by Lemma O, is the **count** of nonzero lift blocks along a
single infinite word. Nothing here establishes a bound on it; it is recorded as the
one direction these three audits did not close.

---

## Reproducibility

Each package carries `SHA256SUMS`, its scripts, and frozen outputs. All computations
use exact integer and modular arithmetic (CPython standard library only — no numpy,
sympy or mpmath). No Lean was run in any of the three audits and **no Lean
verification is claimed** for any statement in this note.
