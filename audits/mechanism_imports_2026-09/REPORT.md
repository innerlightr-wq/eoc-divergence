# Progress update: six mechanism imports, and what survived them

**2026-09-26. Not paper material.** This is a working record, imported from scratch
runs made outside the repository. It modified nothing in the programme and proves
nothing about (DE). Its purpose is to record six closed routes, the lemmas that
came out of them, and one reformulation of the remaining gap that is sharper than
the wording currently in the synthesis.

Lemma ledger: [`LEMMAS.md`](LEMMAS.md). The reformulation:
[`SELECTION_RATIO.md`](SELECTION_RATIO.md). Scripts: [`scripts/`](scripts), with
[`scripts/RUN.md`](scripts/RUN.md); committed outputs: [`data/`](data).

---

## 0. Summary

> **Six independent mechanisms were imported and tested against the placement gap.
> All six terminate at the same object. One of them additionally rules out a whole
> class of candidate tools that the synthesis currently asks for.**

| # | import | verdict | terminates at |
|---|---|---|---|
| 1 | Rozier's abc machinery (arXiv:2306.15284v2) | **C** structural insight only | one-defect stratum; `d ≥ 2` needs the `n`-conjecture |
| 2 | switch complexity / `S`-unit equations | **D** low-switch sector irrelevant | endpoint factors are free integers; sector empty of danger |
| 3 | Sturmian local-to-global (initial squares) | **C** exact mechanical subsector only | confinement does not force long squares |
| 4 | Thales / imaginary-hypotenuse diagnostic | **E** pure reparameterisation | `θ_D ≡ H_n`, `θ_C ≡ R_n`; skew product, no feedback |
| 5 | inherited local membership (structural addresses) | **F** no nontrivial compression | precision consumed at the valuation rate |
| 6 | micro/macro fiber ensembles | **E** reduces to known counting | the selection ratio `Q`, i.e. placement |

Every audit was run with its own stop rules and controls, and every one stopped.
No verdict above C was reached by any of them.

## 1. The one result that changes a stated target

Observation 7.8 of the synthesis asks for *"a quantitative law for how the
terminating tail propagates into the parity digits — how many parity digits of `m`
are constrained by the fact that `m < 2^B`, as a function of `B` and of the depth"*,
and records that the programme contains no candidate for it.

Import 5 shows that **no candidate of that shape can exist**:

- **bit-loss lemma** (Lemma 5, [`LEMMAS.md`](LEMMAS.md)): fixed `2`-adic precision is
  consumed at exactly the cumulative valuation rate, `K_n = K_0 − S_n`. Every
  `m mod 2^K` class splits under one step — fraction `1.0000` at `K = 6,8,10,12,14`.
- **minimal automaton** (Lemma 7): the quotient of odd residues mod `2^N` by
  `L`-step future valuations saturates at the full `2^{N−1}` states, at `L = N−1`.
- **precision budget** (Lemma 6): the first `L` valuations are fixed by `m mod 2^{S_L+1}`
  and by no smaller modulus — the realizer cylinder itself.

So finite-state propagation of the terminating tail is not merely unachieved; it is
ruled out. The complementary half (Lemma 8) is that nothing is destroyed: the bits
the forward map consumes reappear as cylinder-tree multiplicity, at the exact rate
`a_n = log₂(1 / relative child mass)`.

**Suggested rewording of the target**, if 7.8 is ever revised: the unresolved issue
is not propagation of a compressed state but *arithmetic selection among the
surviving cylinders*. That is the object of [`SELECTION_RATIO.md`](SELECTION_RATIO.md).

## 2. What is worth keeping from the closed routes

Six lemmas, all proved and verified by exhaustive enumeration in exact integer
arithmetic; see [`LEMMAS.md`](LEMMAS.md) for statements, proofs and counts.

- **Lemma 1 (switch decomposition).** `C_n` is a signed sum of **exactly `r+2`**
  monomials `3^a 2^b`, `r` the number of valuation switches, with coefficients
  `±1` at the ends and `±2` inside, all monomials distinct. This strictly refines
  the earlier defect bound `2d+2`: for `1^a 2^b` the defect is `Θ(n)` while `r = 1`.
- **Lemma 2 (margin–switch theorem).** A word confined to a drift band of width `W`
  for `n` steps has `r+1 ≥ 2κ n/W − (α−1)`, `κ = (α−1)(2−α) = 0.2427814`;
  asymptotically tight. Equivalently: for fixed `r` the word must depart from the
  barrier by `≳ 0.4856 n/(r+2)` — a separation linear in `n`.
- **Lemma 3 (mechanical extremal).** The barrier-hugging word `a_j = ⌊jα⌋−⌊(j−1)α⌋`
  has switch density `r/n → 2(2−α) = 0.8300750`. Narrow confinement forces
  *near-maximal* switching, not low switching.
- **Lemma 4 (automatic height on confined blocks).** `C_n ≤ (n/3)·max(2^{S_n}, 3^n)`
  for every zero-confined word, with **no balance hypothesis**. This removes the
  balance requirement from the balanced-square criterion of the synthesis (§7(d))
  *inside the confined sector*, and explains why the `0^a1^a` counterexample cannot
  occur there.
- **Lemma 9 (mod-3 inheritance).** `δ_{n+1} = 2^{a_n} mod 3` closes exactly and
  separates two classes — and both classes have identical valuation distributions,
  so it restricts nothing. A clean instance of closure and separation without
  predictive content.
- **Lemma 10 (exponent identity).** `h + I₀ = α` with `h = αH₂(1/α) = 1.5056439`
  and `I₀ = 0.0793186`. This is the quantitative reason the union bound over
  confined words cannot close the finite-height count: it over-counts by `2^{hn}`.

## 3. Controls

Every import was run against `3x−1`, and two of them produced control statements
worth recording:

- The switch machinery exists **only for `p = 3`**: the run collapse needs
  `2^a − p = ±1` to have two solutions in `a`, which holds iff `p−1` and `p+1` are
  both powers of two, i.e. iff `p = 3`. For `5x±1` and `7x±1` it does not exist,
  so it cannot falsely appear powerful there.
- The selection ratio `Q` **is** the `3x+1` / `3x−1` discriminant: it collapses to
  zero for `3x+1` (extinct at `N = 84` for `M = 2^16`) and diverges for `3x−1`
  (`Q = 468` at `N = 180`, the anchor `m = 1` never dying). Any future bound on `Q`
  must therefore be sign-sensitive — consistent with the sign obstruction of §7(b).

## 4. What this does not do

No verdict here bears on (DE), and none of the six imports produced a pointwise
tool. The lemmas above are structural facts about the confined-word/cylinder
geometry; the reformulation in [`SELECTION_RATIO.md`](SELECTION_RATIO.md) is a
definition, not a result, and controlling it is at least as strong as (DE) — see
that file for the precise statement. Nothing in this directory should be read as
progress toward the Collatz conjecture.

## 5. Provenance

The six audits were run outside the repository, on 2026-09-26, against
`eoc-divergence` at `3407b1b` and `eoc-lean-verification` at `14dea46`. Neither
repository was modified by them. The Lean files carrying the endpoint-pressure
chain (`EOC/EndpointPressure.lean`, `EOC/FinalChain.lean` and companions) are
untracked working-tree material dated 2026-09-16/17 and had no build artifacts
present at the time of inspection; they are `sorry`-free by source inspection only.

The scripts committed here are fresh re-implementations written from the
definitions, not copies of the scratch code; each one re-derives the claim it
checks and prints its own counts.
