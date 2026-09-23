# Equivalent forms of (DE)

Four statements of universal drift exit, recorded so that later work does not mistake one for
another. **Only form (a) is formalized in this repository.** Forms (b), (c) and (d) are
paper-level: they are stated here as they appear in the programme, and are *not* machine-checked.

## (a) The headline form — **formalized**

```lean
theorem divergent_iff_zeroConfined :
    (∃ M, Odd M ∧ DivergentOrbit M) ↔ (∃ m, Odd m ∧ ZeroConfined m)
```

(DE) is the assertion that the right-hand side is false: no positive odd `m` satisfies
`2^{S_n(m)} ≤ 3^n` for every `n`. Machine-checked, with no hypotheses, in `Divergence/Main.lean`.

## (b) The realizer-frontier form — **paper-level, not formalized**

`r_min(N, 0) → ∞`: the least integer realizing a `0`-confined word of length `N` grows without
bound. Equivalent to (a) by the residue–time duality of Revision 7, §6.

## (c) Qualitative escape at any fixed corridor — **paper-level, not formalized**

For **any** fixed `c ≥ 0`, an orbit that is `c`-confined at every horizon is injective, hence
divergent, hence yields a `0`-confined seed by the last-maximum argument. So escape at one
corridor width is escape at all of them, and (DE) does not depend on the choice of `c`.

*What is formalized is the `c = 0` case only*: `Divergence.not_zeroConfined_of_repeat` shows a
repeated orbit value contradicts `0`-confinement, and `Divergence.exists_zeroConfined_of_divergent`
supplies the seed. The general-`c` statement uses the same cycle-drift argument with the constant
`2^c` absorbed, but that generalisation is not in this repository.

## (d) The Hensel-tail form — **paper-level, not formalized**

No zero-confined `2`-adic integer has an expansion ending in `0^∞`. This is the `2`-adic
restatement of (b): a terminating tail is exactly a bounded realizer.

---

## What this list is for

These four are the same problem wearing different clothes. A reformulation into any of (b), (c)
or (d) is **not** progress on (DE); the companion repository's
`boundedPrefixRealizers_iff_positiveRealizer` makes the same point on the realizer side, where
"unbounded least realizers" is a restatement of non-realizability rather than a route to it.
