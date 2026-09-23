import Descent

/-! Axiom audit for the `Descent` library. CI fails unless every line below reports a
subset of `[propext, Classical.choice, Quot.sound]`. -/

-- confinement
#print axioms Descent.confinedUpTo_mono
#print axioms Descent.forall_confinedUpTo_iff

-- L1
#print axioms Descent.three_mul_back
#print axioms Descent.odd_back
#print axioms Descent.back_lt
#print axioms Descent.a_back
#print axioms Descent.T_back
#print axioms Descent.orbit_back
#print axioms Descent.S_back
#print axioms Descent.back_confinedUpTo
#print axioms Descent.back_step_zeroConfined

-- L2
#print axioms Descent.three_mul_back_succ
#print axioms Descent.three_pow_mul_back_iterate
#print axioms Descent.odd_back_iterate
#print axioms Descent.back_step_available
#print axioms Descent.back_chain_length

-- L4
#print axioms Descent.a_eq_one_of_confined
#print axioms Descent.mod_four_of_confined
#print axioms Descent.least_confined_mod_three
#print axioms Descent.least_confined_mod12

-- L7
#print axioms Descent.two_mul_T_succ
#print axioms Descent.v3_T_succ
#print axioms Descent.rt_shift
#print axioms Descent.not_three_dvd_T_succ
#print axioms Descent.three_dvd_T_succ
