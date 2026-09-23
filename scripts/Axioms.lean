import Divergence

/-! Axiom audit. CI fails unless every line below reports a subset of
`[propext, Classical.choice, Quot.sound]`. Retargeted at each milestone;
at M5 this becomes `Divergence.divergent_iff_zeroConfined`. -/

#print axioms Divergence.divergent_of_zeroConfined
#print axioms Divergence.injective_iff_divergent
#print axioms Divergence.aggregate_identity
#print axioms Divergence.cycle_drift
