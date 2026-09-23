import Divergence

/-! Axiom audit. CI fails unless every line below reports a subset of
`[propext, Classical.choice, Quot.sound]`. -/

-- The headline theorem and its two corollaries.
#print axioms Divergence.divergent_iff_zeroConfined
#print axioms Divergence.no_divergent_of_no_zeroConfined
#print axioms Divergence.no_zeroConfined_of_no_divergent

-- M1: the map, the aggregate identity, cycle drift.
#print axioms Divergence.aggregate_identity
#print axioms Divergence.cycle_drift
#print axioms Divergence.injective_iff_divergent
#print axioms Divergence.divergent_of_zeroConfined

-- M2: the raw map.
#print axioms Divergence.U_iter_shift
#print axioms Divergence.U_iter_shift_endpoint
#print axioms Divergence.oddCount_shift
#print axioms Divergence.modEq_of_parity_prefix
#print axioms Divergence.modEq_of_parityPrefix_eq
#print axioms Divergence.raw_aggregate_identity
#print axioms Divergence.contraction
#print axioms Divergence.bridge
#print axioms Divergence.orbit_range_subset
#print axioms Divergence.raw_injective_of_divergent

-- M3: the binomial tail and the certified base.
#print axioms Divergence.tail_mul_le
#print axioms Divergence.card_subsets_card_ge
#print axioms Divergence.entropy_certificate
#print axioms Divergence.light_certificate
#print axioms Divergence.heavy_tail_pow
#print axioms Divergence.exists_window_base

-- M4: windowed sparsity.
#print axioms Divergence.window_card_le_shifts
#print axioms Divergence.fibre_card_le_choose
#print axioms Divergence.light_fibre_card_le
#print axioms Divergence.exists_window_sparsity

-- M5: summability, the last maximum, the reduction.
#print axioms Divergence.summable_inv_orbit
#print axioms Divergence.rho_mul_orbit
#print axioms Divergence.rho_tendsto_zero
#print axioms Divergence.exists_last_max
#print axioms Divergence.exists_zeroConfined_of_divergent
