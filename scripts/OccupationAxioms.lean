import Occupation

/-! Axiom audit for the `Occupation` companion library. CI fails unless every line
below reports a subset of `[propext, Classical.choice, Quot.sound]`. -/

-- O1: compositions and the cycle lemma.
#print axioms Occupation.card_comps
#print axioms Occupation.confComps_eq_empty
#print axioms Occupation.p_eq_sum
#print axioms Occupation.p_pos
#print axioms Occupation.two_pow_lt_three_pow_iff
#print axioms Occupation.sum_range_rot
#print axioms Occupation.exists_rot_neg
#print axioms Occupation.exists_rot_confined
#print axioms Occupation.card_comps_le_mul
