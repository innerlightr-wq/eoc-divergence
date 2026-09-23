import Descent.Basic

/-!
# L7: the lockstep invariance

A forward step with `d = 1` raises the 3-adic budget `v₃(m+1)` by exactly one — **and raises the
round-trip requirement by exactly one as well**. The surplus is therefore invariant under the
dominant forward move, so forward motion cannot accumulate 3-adic budget.

A step with even `d` destroys the budget outright; a step with odd `d` preserves divisibility
but resets the valuation to an unrelated quantity.

This is the obstruction identified in `audits/descent/DESCENT_AUDIT.md`.
-/

namespace Descent

open Divergence

private theorem two_pow_mod_three_aux (d : ℕ) :
    (d % 2 = 0 → 2 ^ d % 3 = 1) ∧ (d % 2 = 1 → 2 ^ d % 3 = 2) := by
  induction d with
  | zero => norm_num
  | succ d ih =>
    obtain ⟨h0, h1⟩ := ih
    rw [pow_succ]
    refine ⟨fun h => ?_, fun h => ?_⟩
    · have := h1 (by omega)
      omega
    · have := h0 (by omega)
      omega

/-- A forward `d = 1` step, division-free. -/
theorem two_mul_T_succ {m : ℕ} (h1 : a m = 1) : 2 * (T m + 1) = 3 * (m + 1) := by
  have hkey := two_pow_a_mul_T m
  rw [h1, pow_one] at hkey
  omega

/-- **L7, budget half.** A forward `d = 1` step raises the 3-adic budget by exactly one. -/
theorem v3_T_succ {m : ℕ} (h1 : a m = 1) :
    padicValNat 3 (T m + 1) = padicValNat 3 (m + 1) + 1 := by
  have hkey := two_mul_T_succ h1
  have hT : T m + 1 ≠ 0 := by omega
  have hm : m + 1 ≠ 0 := by omega
  have hl : padicValNat 3 (2 * (T m + 1)) = padicValNat 3 (T m + 1) := by
    rw [padicValNat.mul (by norm_num) hT, padicValNat.eq_zero_of_not_dvd (by omega)]
    omega
  have hr : padicValNat 3 (3 * (m + 1)) = padicValNat 3 (m + 1) + 1 := by
    rw [padicValNat.mul (by norm_num) hm, padicValNat.self (by norm_num)]
    omega
  rw [← hl, hkey, hr]

/-- **L7, requirement half.** With `a m = 1` the round-trip inequality at `(T m, j+1)` is
equivalent to the one at `(m, j)`: both sides pick up exactly one factor of `3`. -/
theorem rt_shift {m z j : ℕ} (h1 : a m = 1) :
    (2 ^ (j + 1) * (T m + 1) < 3 ^ (j + 1) * (z + 1))
      ↔ (2 ^ j * (m + 1) < 3 ^ j * (z + 1)) := by
  have hkey := two_mul_T_succ h1
  have hL : 2 ^ (j + 1) * (T m + 1) = 3 * (2 ^ j * (m + 1)) := by
    calc 2 ^ (j + 1) * (T m + 1) = 2 ^ j * (2 * (T m + 1)) := by ring
      _ = 2 ^ j * (3 * (m + 1)) := by rw [hkey]
      _ = 3 * (2 ^ j * (m + 1)) := by ring
  have hR : 3 ^ (j + 1) * (z + 1) = 3 * (3 ^ j * (z + 1)) := by ring
  rw [hL, hR]
  exact Nat.mul_lt_mul_left (by norm_num)

/-- **Even `d` destroys the budget.** For odd `m`, `a m` even forces `3 ∤ T m + 1`.
No `2 ≤ a m` is needed: `a_pos` already gives `a m ≥ 1`. -/
theorem not_three_dvd_T_succ {m : ℕ} (hm : Odd m) (heven : a m % 2 = 0) :
    ¬ (3 ∣ T m + 1) := by
  rintro ⟨c, hc⟩
  have hd1 := a_pos hm
  have hd2 : 2 ≤ a m := by omega
  have hP : (4 : ℕ) ≤ 2 ^ a m := by
    calc (4 : ℕ) = 2 ^ 2 := by norm_num
      _ ≤ 2 ^ a m := Nat.pow_le_pow_right (by norm_num) hd2
  have hmod := (two_pow_mod_three_aux (a m)).1 heven
  have hkey := two_pow_a_mul_T m
  have hexp : 3 * (2 ^ a m * c) = 3 * (m + 1) + (2 ^ a m - 2) := by
    have h : 2 ^ a m * (T m + 1) = 3 * m + 1 + 2 ^ a m := by
      rw [Nat.mul_add, Nat.mul_one, hkey]
    rw [hc] at h
    calc 3 * (2 ^ a m * c) = 2 ^ a m * (3 * c) := by ring
      _ = 3 * m + 1 + 2 ^ a m := h
      _ = 3 * (m + 1) + (2 ^ a m - 2) := by omega
  omega

/-- **Odd `d` preserves divisibility.** Includes `d = 1`, consistent with `v3_T_succ`. -/
theorem three_dvd_T_succ {m : ℕ} (hm : Odd m) (hodd : a m % 2 = 1) : 3 ∣ T m + 1 := by
  have hd1 := a_pos hm
  have hP : (2 : ℕ) ≤ 2 ^ a m := by
    calc (2 : ℕ) = 2 ^ 1 := by norm_num
      _ ≤ 2 ^ a m := Nat.pow_le_pow_right (by norm_num) hd1
  have hmod := (two_pow_mod_three_aux (a m)).2 hodd
  have hkey := two_pow_a_mul_T m
  have hexp : 2 ^ a m * (T m + 1) = 3 * (m + 1) + (2 ^ a m - 2) := by
    rw [Nat.mul_add, Nat.mul_one, hkey]
    omega
  have hdvd : (3 : ℕ) ∣ 2 ^ a m * (T m + 1) := by
    rw [hexp]
    have h2 : (3 : ℕ) ∣ 2 ^ a m - 2 := by omega
    exact Nat.dvd_add ⟨m + 1, rfl⟩ h2
  have hcop : Nat.Coprime 3 (2 ^ a m) := Nat.Coprime.pow_right _ (by decide)
  exact hcop.dvd_of_dvd_mul_left hdvd

end Descent
