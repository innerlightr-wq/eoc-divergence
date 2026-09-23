import Divergence

/-! Axiom audit. CI fails unless every line below reports a subset of
`[propext, Classical.choice, Quot.sound]`. Retargeted at each milestone;
at M5 this becomes `Divergence.divergent_iff_zeroConfined`. -/

-- M1
#print axioms Divergence.divergent_of_zeroConfined
#print axioms Divergence.injective_iff_divergent
#print axioms Divergence.aggregate_identity
#print axioms Divergence.cycle_drift

-- M2
#print axioms Divergence.U_iter_shift
#print axioms Divergence.U_iter_shift_parity
#print axioms Divergence.U_iter_shift_endpoint
#print axioms Divergence.oddCount_shift
#print axioms Divergence.modEq_of_parity_prefix
#print axioms Divergence.modEq_of_parityPrefix_eq
#print axioms Divergence.raw_aggregate_identity
#print axioms Divergence.E_lt
#print axioms Divergence.E_eq_zero
#print axioms Divergence.contraction
#print axioms Divergence.U_iter_two_pow_mul
#print axioms Divergence.U_iter_a_eq_T
#print axioms Divergence.bridge
#print axioms Divergence.orbit_range_subset
#print axioms Divergence.raw_injective_of_divergent
