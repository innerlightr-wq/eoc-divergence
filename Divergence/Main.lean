import Divergence.LastMaximum

/-!
# The headline theorem (paper Thm. 6.14 + Prop. 4.10)

```
(∃ M, Odd M ∧ DivergentOrbit M)  ↔  (∃ m, Odd m ∧ ZeroConfined m)
```

for the accelerated `3x+1` map, with **no hypotheses**.

**This does not exclude divergent orbits.** It reduces that question to the non-existence of a
zero-confined positive odd seed — universal drift exit — which remains open. What it does is make
the reduction unconditional: the Garcia–Tal / Curry windowed sparsity theorem, which the
companion work consumed as an external input, is proved in `Divergence.WindowedSparsity`.

* `→` : windowed sparsity ⟹ reciprocal summability (`Divergence.Summable`) ⟹ the carry product
  is bounded ⟹ `ρ n → 0` ⟹ a last maximum exists, and restarting there is zero-confined
  (`Divergence.LastMaximum`).
* `←` : a zero-confined seed has no repeats, hence an injective and therefore divergent orbit
  (`Divergence.CycleDrift`).

No `sorry`, `admit`, `axiom`, or `opaque`. The axiom audit below is enforced in CI.
-/

namespace Divergence

/-- **The headline theorem.** A divergent accelerated orbit exists if and only if a zero-confined
positive odd seed exists. -/
theorem divergent_iff_zeroConfined :
    (∃ M, Odd M ∧ DivergentOrbit M) ↔ (∃ m, Odd m ∧ ZeroConfined m) := by
  constructor
  · rintro ⟨M, hM, hdiv⟩
    exact exists_zeroConfined_of_divergent hM hdiv
  · rintro ⟨m, hm, hzc⟩
    exact ⟨m, hm, divergent_of_zeroConfined hm hzc⟩

/-- Universal drift exit would exclude divergence. -/
theorem no_divergent_of_no_zeroConfined (h : ∀ m, Odd m → ¬ ZeroConfined m) :
    ∀ M, Odd M → ¬ DivergentOrbit M := by
  intro M hM hdiv
  obtain ⟨m, hm, hzc⟩ := divergent_iff_zeroConfined.mp ⟨M, hM, hdiv⟩
  exact h m hm hzc

/-- And conversely: excluding divergence would give universal drift exit. -/
theorem no_zeroConfined_of_no_divergent (h : ∀ M, Odd M → ¬ DivergentOrbit M) :
    ∀ m, Odd m → ¬ ZeroConfined m := by
  intro m hm hzc
  obtain ⟨M, hM, hdiv⟩ := divergent_iff_zeroConfined.mpr ⟨m, hm, hzc⟩
  exact h M hM hdiv

end Divergence

#print axioms Divergence.divergent_iff_zeroConfined
#print axioms Divergence.no_divergent_of_no_zeroConfined
#print axioms Divergence.no_zeroConfined_of_no_divergent
