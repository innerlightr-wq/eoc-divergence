# 01_SOURCE_AUDIT.md — the OpenAI H10/ℚ manuscript

**File:** `~/Downloads/main (3).pdf` → `sources/openai_H10_rationals.pdf`
sha256 `f9c3a77d59893f720a382e6dbf34fbb93adcdfd27af3dcdf4e4336157143defb`, 62 pp.,
*Hilbert's tenth problem over the rational numbers*, OpenAI, dated 24 September 2026.
Abstract: "no algorithm decides whether a polynomial with integer coefficients has a rational
zero.  The number of variables is part of the input."

## 1. Architecture (§1.2, p. 5)

For each nonconstant `f ∈ ℤ[X₁..Xₙ]`, an effectively generated sequence of finite tests with
```
f has an integer zero   ⟺   every test succeeds .                    (1.1)
```
Each test is answerable by finitely many rational-solvability queries, so a decision procedure
for rational solvability would decide integer solvability — contradicting Matiyasevich.  **The
entire arithmetic burden is the ⟸ direction: a failed test must exist whenever `f` has no
integer zero.**

## 2. The mechanism that matters here — forcing standard from nonstandard

1. **Compactness** (§2.4): if all tests succeed, there is a ring `R` containing a zero
   `a = (a₁..aₙ)` of `f`, embedded in an **elementary extension of ℚ**.  The ambient integer
   sort `*ℤ` **may contain nonordinary elements** (p. 5).
2. **Indices** (§2.3, Lemma 2.7, pp. 11–12): the tests attach an elliptic point `T_a` to each
   `a ∈ R`, inside a fixed infinite cyclic `ℤP` of finite index in a rank-one elliptic group,
   giving `T̃_a = η(a)P` with `η : R → *ℤ` **injective and additive, `η(1)=1`, but not
   multiplicative**.  Lemma 2.7: the theory `T` is recursive and **has a model whose ring is
   `ℤ`**, with `T_a = aP`.
3. **Local comparisons** (§2.1–2.2): paired tests on a curve and its conjugate force each `ã`
   to be integral at the relevant prime and to agree with `η(a)` to precision `K`.
4. **The height contradiction** (§2.7, Prop. 2.12, pp. 16–17) — the endgame:
   * `δ = f(η(a₁),…,η(aₙ)) ∈ *ℤ`; if `δ = 0`, elementarity gives an ordinary integer zero;
   * otherwise `|δ| ≤ C_f B^D` with `B = max(1,|η(a_j)|)` (2.22);
   * for **every** `A ∈ R`, every contact prime of its representation divides **this same `δ`**
     to order `≥ K`, so `M_K(s̃)^K | δ` (2.24);
   * hence `M_K(s̃)^c ≤ |δ|^{c/K} ≪_f B`, and the five-point height estimate
     `h(s) ≤ H·M(s)^c` gives `h(s̃) ≪_f B` (2.25);
   * applied to `x(η(a_j)P)`, the transferred canonical-height comparison grows **quadratically**
     in `|η(a_j)|`, so `B² ≪_f B`, forcing `B = O(1)`;
   * additivity and injectivity then identify the modeled roots with ordinary integers,
     contradicting `δ ≠ 0`.

**Distilled, the forcing uses three ingredients:**
* **(i)** one *fixed* nonzero integer `δ` that every local obstruction must divide to high order;
* **(ii)** a height estimate converting that divisibility into a size bound — `h(s) ≤ H·M(s)^c`,
  with `M(s)` the product of the **contact primes**, the nonexceptional primes where one of five
  fixed linear forms has odd valuation (§4, pp. 26–43);
* **(iii)** a **quadratic** canonical height beating the linear bound.

## 3. Load-bearing external inputs (not verified here)

* §3: pointwise 2-converse [48, Thm 1.1] and the Cassels–Tate pairing [6];
* §4.7: the odd regular Fontaine–Mazur theorem at 2 [49, Thm 1.1], "whose statement has no
  hypothesis on the residual image";
* §4: five-point quaternionic quotient, an abelian-surface family, Faltings-height comparison,
  modularity, a uniform modular-level bound;
* §6: a prime-pattern theorem supplying simultaneous local witnesses in the integer model.

## 4. Verification status and concerns

**I did not verify the manuscript, and nothing below depends on whether it is correct.**
Recorded concerns, in the brief's spirit of not accepting it on authority:

* it is an unrefereed preprint claiming a major open problem, dated three weeks ago;
* the chain in §4 is long and each link is a deep theorem; the Faltings-height/modularity/uniform
  level sequence is where I would expect a referee to concentrate;
* §2.7's step (2.24) is explicitly a **transfer** of an ordinary divisibility fact through an
  elementary extension, with the caveat (p. 17) that "the coarsenings may have been chosen
  externally one prime at a time; only the universal assertion just established enters this
  transferred implication" — a point requiring care that I did not check.

**For the present purpose this is moot.**  The question is whether the *machinery* transfers to
the Collatz realizer problem.  `03_TRANSFER_ANALYSIS.md` shows it does not, and that conclusion
is independent of the manuscript's correctness.
