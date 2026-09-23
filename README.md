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

**Milestone M4 of 5 complete.** The `←` direction (`divergent_of_zeroConfined`) is proved, and the
windowed sparsity theorem — the substantial input to the `→` direction — is now formalized rather
than assumed. See [`docs/STATUS.md`](docs/STATUS.md) for the current ledger.

## Ledger

| Module | Paper / source reference | Status |
|---|---|---|
| `Divergence/Basic.lean` | Lemma 2.4 (aggregate identity) | **proved** |
| `Divergence/CycleDrift.lean` | Lemma 4.2 (cycle drift); `←` direction | **proved** |
| `Divergence/RawMap.lean` | Terras shift; Curry Lemma 2.2 (contraction); bridge | **proved** |
| `Divergence/BinomialTail.lean` | entropy tail bound; `γ = 31/50` certificates | **proved** |
| `Divergence/WindowedSparsity.lean` | Garcia–Tal Fundamental Lemma; Curry Thm 2.3 | **proved** |
| `Divergence/Summable.lean` | Curry Prop 3.1 / paper Prop 4.9 | not started |
| `Divergence/LastMaximum.lean` | paper Prop 4.10 | not started |
| `Divergence/Main.lean` | paper Thm 6.14 | not started |

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
