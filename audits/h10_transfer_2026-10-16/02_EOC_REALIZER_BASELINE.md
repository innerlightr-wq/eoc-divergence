# 02_EOC_REALIZER_BASELINE.md

Authoritative source: `eoc_rev8_review (3).pdf` → `sources/eoc_rev8_downloads.pdf`,
sha256 `07c6610d633035e43b8a36905e0c58e517704ca12bb208e2340359dea30f294c`, 32 pp.,
*A Global Occupation Conjecture for the Accelerated 3x+1 Map: Residue–Time Duality,
Divergent-Orbit Sparsity, and the Pointwise Realizer Problem*, **Revision 8, 2026**.

Repositories, recorded not modified:

| repo | branch | HEAD | origin/main | worktree |
|---|---|---|---|---|
| `eoc-divergence` | `main` | `938dcc0` | `b787dfa` | clean |
| `eoc-lean-verification` | `main` | `6057a0d` | `6057a0d` | clean |
| `periodicity-conjecture-bridge` | `main` | `edb9ed4` | `a15702a` | clean |
| `collatz-confined-words` | **not present locally** | — | — | — |

`eoc-divergence` local `main` carries an unpushed commit `938dcc0` ("Formalize the raw growth
bound") on top of `bf1b377`, while `origin/main` has advanced to `b787dfa`.  **A local HEAD here
is not the published state.**  I touched nothing.

## 1. Definitions, verified against the paper

Accelerated map `T(m) = (3m+1)/2^{a(m)}`, `a(m) = ν₂(3m+1)`.  Drift `R_n = S_n − n log₂3`,
occupation `O_c(m₀) = #{n ≥ 0 : R_n ≤ c}`.

**Lemma 2.4 (aggregate identity), p. 336** — verbatim:
```
C_n = Σ_{j<n} 3^{n-1-j} 2^{S_j}   (C_0 = 0, C_{n+1} = 3C_n + 2^{S_n} > 0),
2^{S_n} m_n = 3^n m_0 + C_n       for all n ≥ 0.
```
**Lemma 2.5 (integral corridor)**: `R_n ≤ 0 ⟺ 2^{S_n} ≤ 3^n ⟺ S_n ≤ ⌊nα⌋`, `α = log₂3`.

Both confirm the brief's formulas.  I re-derived the identity and machine-checked it on seven
orbits to `n = 40` (`results/run_char.txt`).

## 2. The realizer characterization `[PROVED]` — but elementary, and ALREADY KNOWN

Since `3` is invertible mod `2^k`, the identity gives the realizer congruence
`m₀ ≡ −C_n 3^{−n} (mod 2^{S_n})`, and the canonical residue
`r_n = (−C_n 3^{−n}) mod 2^{S_n} ∈ [0, 2^{S_n})`.

> **Proposition R.**  Let a parity word have `S_n` nondecreasing and `S_n → ∞`.  Then:
> (a) the `r_n` are mutually compatible (`r_{n+1} ≡ r_n mod 2^{S_n}`) and determine a unique
>     `x ∈ ℤ₂`;
> (b) the word has a **nonnegative-integer** realizer iff `(r_n)` is eventually constant, and
>     the realizer is then that constant;
> (c) it has a **strictly positive** realizer iff `(r_n)` is eventually constant and nonzero.
>
> *Proof.* (a) is the congruence.  (⇐ of b) if `r_n = r` for `n ≥ N`, then `r ∈ ℤ_{≥0}` satisfies
> every congruence, by compatibility also for `n < N`.  (⇒ of b) if `m₀ ∈ ℤ_{≥0}` realizes, then
> `m₀ ≡ r_n (mod 2^{S_n})` with `0 ≤ r_n < 2^{S_n}`; as soon as `2^{S_n} > m₀` — which happens for
> all large `n` since `S_n → ∞` — this forces `r_n = m₀`.  (c) `r ≡ 0` corresponds to `m₀ = 0`. ∎

**Status: `[PROVED]` but `[ALREADY KNOWN]`.**  It is the standard fact that a 2-adic integer is a
nonnegative rational integer iff its expansion terminates, transported through the identity.  It
is the *statement* of the pointwise gap, not progress on it.  Recorded because the brief asks for
it explicitly, with the hypotheses made precise (`S_n → ∞`; nonnegative vs strictly positive).

**Verified** (`results/run_char.txt`): on orbits `m₀ = 7, 27, 97, 703, 10087, 159487, 270271`,
`r_n = m₀` from the first `n` with `2^{S_n} > m₀` onward.  And the Beatty/Sturmian zero-corridor
word `d_j = ⌊(j+1)α⌋ − ⌊jα⌋` is confined, has compatible residues, and `r_60` has 93 bits against
`S_60 = 95` — **no stabilization.  The gap, exhibited.**

## 3. The precise missing control, in the programme's own words

Rev 8 **§5.3, p. 584** — verbatim:

> "The only general tool converting divisibility into a size statement is that a nonzero multiple
> of `2^m` has absolute value at least `2^m`, which gives a dichotomy: either `A + χΛ = 0`,
> pinning `χ` to the single rational `−A/Λ`, or `|χ| ≥ 2^{S_N}/H − 1`, `H = max(|A|,|Λ|)`."

> **Observation 5.9**: "Arbitrary confined words supply only `(C_N, 3^N)`, with `log₂H = αN ≥ S_N`,
> so `ρ_N ≥ 1` and the second branch is vacuous."

And `notes/CLOSED_POINTWISE_ROUTES_2026-09-29.md` §7, quoting Revision 7 §5.3:

> "every tool whose only arithmetic input is *'a nonzero multiple of `2^m` has absolute value at
> least `2^m`'*, applied to the aggregate identity, is now known to evaluate on the confined
> sector to a restatement of Lemma 2.4."

**This is a standing meta-theorem of the programme, and it is the test any new mechanism must
pass.**  §6 of that note records six closed routes (symbolic complexity, periodic-approximation
surplus, amortization/drift, realizer deficit `δ`, cross-prime 2–3–∞, sign-symmetric carry cost),
each with its `3x−1` control.

`(DE)`, `(PosPC)`, Sharp EOC and Open Problem C are unchanged and open.
