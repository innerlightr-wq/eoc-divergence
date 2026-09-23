# eoc-divergence

**This repository does not exclude divergent orbits.** Its main theorem reduces that question to
the non-existence of a zero-confined positive odd seed — universal drift exit — which remains open.

A small, self-contained Lean 4 + Mathlib formalization of the divergence side of the accelerated
`3x + 1` map, companion to:

> De Jesús, Elias (2026). *A Global Occupation Conjecture for the Accelerated 3x + 1 Map:
> Residue–Time Duality, Divergent-Orbit Sparsity, and the Pointwise Realizer Problem.* Zenodo.
> [doi:10.5281/zenodo.22906673](https://doi.org/10.5281/zenodo.22906673)

The deposited paper is included at [`docs/eoc_rev7.pdf`](docs/eoc_rev7.pdf)
(sha256 `a499a3abc2efb63a0826dd24f1a08bbae2c57c6fa462f2e87331da4e98766560`).

## The headline theorem

For the accelerated map on odd naturals, with

```
a(m) = ν₂(3m+1),    T(m) = (3m+1) / 2^a(m),    Sₙ = Σ_{i<n} a(T^i m),
```

write `DivergentOrbit M` for `T^n M → ∞` and `ZeroConfined m` for `2^{Sₙ} ≤ 3ⁿ` at every `n`
(the integral form of `Rₙ = Sₙ − n·log₂3 ≤ 0`). Then

> **∃ M odd with a divergent orbit  ⟺  ∃ m odd that is zero-confined.**

```lean
theorem divergent_iff_zeroConfined :
    (∃ M, Odd M ∧ DivergentOrbit M) ↔ (∃ m, Odd m ∧ ZeroConfined m)
```

This is paper Theorem 6.14 together with Proposition 4.10, made **unconditional** by formalizing
the Garcia–Tal / Curry windowed sparsity theorem rather than assuming it. It does not rule out
divergence; it converts the question into an exactly equivalent one about the existence of a single
zero-confined seed.

## Status

**Complete.** All five milestones are done. `divergent_iff_zeroConfined` is proved with **no
hypotheses** and depends on no axioms beyond Lean's three standard ones. In particular the
Garcia–Tal / Curry windowed sparsity theorem is *proved here*, not assumed, which is what makes
the equivalence unconditional. See [`docs/STATUS.md`](docs/STATUS.md) for the ledger.

## Ledger

| Module | Paper / source reference | Status |
|---|---|---|
| `Divergence/Basic.lean` | Lemma 2.4 (aggregate identity) | **proved** |
| `Divergence/CycleDrift.lean` | Lemma 4.2 (cycle drift); `←` direction | **proved** |
| `Divergence/RawMap.lean` | Terras shift; Curry Lemma 2.2 (contraction); bridge | **proved** |
| `Divergence/BinomialTail.lean` | entropy tail bound; `γ = 31/50` certificates | **proved** |
| `Divergence/WindowedSparsity.lean` | Garcia–Tal Fundamental Lemma; Curry Thm 2.3 | **proved** |
| `Divergence/Summable.lean` | Curry Prop 3.1 / paper Prop 4.9 | **proved** |
| `Divergence/LastMaximum.lean` | paper Prop 4.10 | **proved** |
| `Divergence/Main.lean` | paper Thm 6.14 | **proved** |
| `Occupation/*.lean` | companion: confined-mass rate | **proved** (separate library) |

**No module introduces an external hypothesis.** Every `Prop` the headline theorem depends on is
proved in this repository.

## Companion result (occupation side)

A **separate** Lean library, `Occupation`, holds one occupation-side result:

```lean
theorem confined_mass_rate (c : ℕ) :
    Tendsto (fun N : ℕ => -(1 / (N : ℝ)) * Real.logb 2 (p N c)) atTop (𝓝 I₀)
```

where `p N c = Σ 2^{-S_N(d)}` over the `c`-confined words `d` of length `N` (all letters `≥ 1`,
`2^{S_j} ≤ 2^c·3^j` for every `j ≤ N`), and

```
I₀ = α(1 − H₂(1/α)) ≈ 0.0793186,      α = log₂3.
```

**This is not part of the headline equivalence.** `Divergence` does not import `Occupation`, and
`divergent_iff_zeroConfined` does not depend on any of it. It is a companion: it proves the
*statistical* rate that Revision 7 §3.3 and the Sturmian-capacity note treated as a
standard-technique expectation rather than a theorem. Confined-word mass decays at exactly the
exponential rate `I₀` — no more, no less.

The proof is purely combinatorial: no probability, no central limit theorem, no tilting. The
upper bound organises words by total valuation and uses unimodality of `C(s−1,N−1)·2^{-s}`; the
lower bound is the cycle lemma at the anchor total `s_N = ⌊Nα⌋`, realised integrally as
`Nat.log 2 (3^N)`.

`Occupation` has its own axiom audit (`scripts/OccupationAxioms.lean`), enforced in CI under the
same permitted set, and introduces no external hypothesis.

### Attribution

* **Dvoretzky & Motzkin (1947)**, and **Spitzer**, for the cycle lemma — the rotation argument
  behind the lower bound.
* **Terras (1976)** and **Everett (1977)** for the word/residue correspondence that makes
  confined words the right objects to count.
* The rate constant `I₀` is from the author's earlier notes.

## Guarantees

No `sorry`, `admit`, `axiom`, `opaque`, `native_decide`, or `implemented_by` anywhere. CI runs
`lake build` and checks that the headline theorem depends on no axioms beyond Lean's three
standard ones (`propext`, `Classical.choice`, `Quot.sound`).

## Building

```bash
lake exe cache get
lake build
```

Pinned to Lean `v4.34.0` and Mathlib `v4.34.0`.

## Attribution

* **Terras (1976)** and **Everett (1977)** — parity-prefix counting and the stopping-time framework.
* **Garcia & Tal**, *A note on the generalized 3n+1 problem*, Acta Arith. **90** (1999) 245–250 —
  the windowed collision argument. Their inequality (6) is already a power-saving bound, with
  inexplicit Heppner exponents.
* **M. J. Curry** (Zenodo, 2026, [doi:10.5281/zenodo.22087163](https://doi.org/10.5281/zenodo.22087163))
  — the explicit, Heppner-free version followed here.
* **Eliahou (1993)** and **Rozier (2017)** — the product identity.

## Related

[`innerlightr-wq/eoc-lean-verification`](https://github.com/innerlightr-wq/eoc-lean-verification),
branch `rev7-finalization`, holds the full EOC programme. It is a reference only, not a Lake
dependency; this repository is deliberately self-contained.

## License

Code is Apache-2.0 ([`LICENSE`](LICENSE)); the contents of `docs/` are CC BY 4.0
([`docs/LICENSE`](docs/LICENSE)).
