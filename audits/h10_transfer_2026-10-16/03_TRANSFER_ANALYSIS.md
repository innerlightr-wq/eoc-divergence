# 03_TRANSFER_ANALYSIS.md

**Question.** Can any mechanism in the H10/ℚ manuscript distinguish a genuine positive-integer
Collatz realizer from a parity sequence realizable only in `ℤ₂`?

**Answer: no.**  Two independently sufficient obstructions, each precisely located.

## Obstruction 1 — H10's divisibility step is exactly the tool EOC already proved vacuous

H10's endgame (2.22)–(2.25) rests on
```
M_K(s̃)^K | δ ,  δ ≠ 0   ⟹   M_K(s̃)^K ≤ |δ| ≤ C_f B^D .
```
That is **verbatim** the arithmetic input Rev 8 §5.3 names as "the only general tool converting
divisibility into a size statement: a nonzero multiple of `2^m` has absolute value at least
`2^m`", with `M_K` in place of `2^m`.  Revision 7 §5.3's meta-theorem — that every such tool
evaluates on the confined sector to a restatement of Lemma 2.4 — therefore **applies to the H10
mechanism before any transfer is attempted.**

The quantitative reason, and it is forced rather than measured:

> **Lemma O.** `[PROVED]`  On the zero-confined sector, `2^{S_n} ≤ 3^n` by definition
> (Rev 8 Lemma 2.5), while the generic height is `H = max(C_N, 3^N) ≥ 3^N`.  Hence
> `2^{S_N}/H − 1 ≤ 0` identically, i.e. `ρ_N = log₂H/S_N ≥ 1`, and the size branch of the
> dichotomy is **vacuous on the whole sector**, with no arithmetic input beyond confinement.

**The hypothesis that defines the interesting sector is exactly what voids the tool.**  Measured
(`results/run_rho2.txt`): `ρ_N` at `N = 10,20,40,60` is `1.1455 … 1.0417` (Beatty word),
`1.1336 … 1.0820` (periodic `[1,2]`), `1.1792 … 1.0000` (orbit `m₀=27`) — all `≥ 1` asymptotically.

**A correction to my own first write-up.** I initially asserted that periodic words have
`ρ_N → 0` and so escape; my own table contradicted that.  The resolution: periodic words are
caught by the *first* horn, not the second.  For a purely periodic word, `m_{Np} = m₀` forces
`m₀ = C_{Np}/(2^{Nσ} − 3^{Np})`, a fixed rational independent of `N` — verified exactly:
period `[1,2]` gives `m₀ = −5`, `[2,1,1,2]` gives `−103/17`, `[1,1,3]` gives `19/5`, each `N`-independent,
and integrality is then checked directly.  **The hard sector is the aperiodic confined words,
where horn one is unavailable (no collapse) and horn two is vacuous (`ρ_N ≥ 1`).  Both fail
simultaneously.**

## Obstruction 2 — H10's two engines have no Collatz analogue

### (a) The contact-prime product `M(s)` — there is only one prime

H10's `h(s) ≤ H·M(s)^c` is powerful because `M(s)` ranges over **many** primes, the
nonexceptional primes where one of five fixed linear forms has odd valuation, and varies with
`s`.  The Collatz realizer condition is a **single congruence modulo `2^{S_N}`**.  Its solution
set is `{r_N + k·2^{S_N} : k ≥ 0}`, so for every odd `q`, `gcd(2^{S_N}, q) = 1` and CRT gives
every residue class mod `q`.

**Verified** (`results/run_primes.txt`), Beatty word at `N = 40`, modulus `2^63`: the realizers
hit all `q` classes for `q = 3, 9, 27, 81, 243, 5, 7, 11, 13`.  This reproves in one line the
repository's own §4b finding that "a code imposes no 3-adic condition on its start… so there is
no CRT modulus and no joint-prime height".  **There is nothing for `M(s)` to be.**

### (b) The quadratic canonical height — Collatz has no quadratic form

H10 closes with
```
h(x(η(a_j)P)) ≪_f B   (linear)      versus      ĥ(nP) ≍ c n²   (quadratic)
⟹ B² ≪_f B ⟹ B = O(1) ⟹ nonstandard forced to standard.
```
The quadratic is the Néron–Tate canonical height: a **positive-definite quadratic form on a
finitely generated abelian group**.  The Collatz realizer structure is the affine reduction
`m₀ ↦ m₀ mod 2^{S_n}`; the ambient group is `(ℤ₂, +)`, which carries no such form, and every
comparison available — `S_n` against `n log₂3`, `log m₀` against `S_n`, `log C_n` against `S_n` —
is **linear in the exponent**.  Without a quadratic-versus-linear squeeze the architecture has no
endgame.

## The brief's six candidate routes, answered

| | route | verdict |
|---|---|---|
| **A** | finite arithmetic tests detect an obstruction to positive-integer realization | **no.**  H10's tests are answerable by rational-solvability queries about a *fixed* polynomial.  The Collatz analogue — "is `r_n` eventually constant?" — is not a finite test: any finite prefix of a non-realizable word is realizable (by `r_N` itself, a perfectly good nonnegative integer).  **Every finite test passes.** |
| **B** | valuations restrict `C_n`, `S_n`, or the residue classes | **no.**  The only valuation present is `ν₂`, already fully used by the identity; §(a) above shows no odd prime is constrained.  H10's pole-parity condition (§3) controls *denominator* valuations of rational points — Collatz realizers are integers with no denominators to control. |
| **C** | height inequalities bound the least realizer | **no, and this is Obstruction 1.**  The least realizer is `r_N` itself; the bound `log₂ r_N ≤ S_N` is the trivial one, and Lemma O shows nothing sharper follows from divisibility on the confined sector.  `δ = S+1 − log₂ r` is the repo's own closed route. |
| **D** | compactness/local-to-global recovers ordinary-integer realizability | **no — and this is the heart.**  H10 gets compactness *for free* and spends its entire §2–§6 on *undoing* it (forcing `B = O(1)`).  Collatz has the same free compactness (the `ℤ₂` limit) and no forcing step.  The transfer would have to import the forcing, which is §(b). |
| **E** | an elliptic-curve or rational-solvability reduction transfers | **no.**  I found no mathematically justified reduction.  Collatz's objects are integers under an affine-with-valuation map; there is no curve, no rank-one group, no cyclic `ℤP`, and nothing for `η` to be.  Writing one down would be an analogy, not a reduction. |
| **F** | reformulate as arithmetic feasibility / Diophantine without losing pointwise character | **possible but empty.**  "Does this word have a positive-integer realizer?" is already a `Σ⁰₁` question (search `m₀`); the difficulty is that non-realizability is `Π⁰₁` and the finite tests all pass (row A).  A Diophantine reformulation inherits exactly that, and H10's contribution is about *undecidability of a class*, not about deciding a single instance. |

## What the comparison does legitimately give

A sharper statement of the gap.  H10 shows that forcing standard-from-nonstandard is possible
when one has (i) a fixed nonzero integer sink, (ii) a many-prime height estimate, (iii) a
quadratic form.  **The Collatz realizer problem has none of the three**, and now one can say
precisely which is missing rather than only that "the gap is open".  That is a conceptual gain,
not a theorem.
