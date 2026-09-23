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

-- O2: the entropy estimate.
#print axioms Occupation.sum_term_eq_one
#print axioms Occupation.choose_mul_le_one
#print axioms Occupation.term_le_term_max
#print axioms Occupation.one_le_succ_mul_choose_mul
#print axioms Occupation.weight_eq_one
#print axioms Occupation.weight_pos
#print axioms Occupation.log_weight_eq
#print axioms Occupation.log_choose_le
#print axioms Occupation.abs_log_choose_sub_le
