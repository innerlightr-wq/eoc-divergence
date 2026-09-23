import Descent.Basic

/-!
# L1: the backward `d = 1` step

If `m` is odd with `m ≡ 2 (mod 3)`, then `p = (2m−1)/3` is a positive odd integer with `p < m`,
`v₂(3p+1) = 1` and `T p = m`; and confinement is inherited with one horizon to spare.

Every hypothesis below supplies `m ≥ 1`, so the `ℕ`-subtraction in `(2m−1)/3` is exact and
non-truncating; `three_mul_back` states that explicitly and is used in place of the division
everywhere downstream.
-/

namespace Descent

open Divergence

/-- The backward `d = 1` map. -/
def back (m : ℕ) : ℕ := (2 * m - 1) / 3

section
variable {m : ℕ} (hm : Odd m) (h3 : m % 3 = 2)
include hm h3

theorem three_dvd_two_mul_sub_one : 3 ∣ 2 * m - 1 := by
  have h1 : 1 ≤ m := hm.pos
  omega

/-- The division is exact. -/
theorem three_mul_back : 3 * back m = 2 * m - 1 :=
  Nat.mul_div_cancel' (three_dvd_two_mul_sub_one hm h3)

theorem odd_back : Odd (back m) := by
  have h1 : 1 ≤ m := hm.pos
  have h := three_mul_back hm h3
  rw [Nat.odd_iff]
  omega

theorem back_pos : 0 < back m := by
  have h1 : 1 ≤ m := hm.pos
  have h := three_mul_back hm h3
  omega

theorem back_lt : back m < m := by
  have h1 : 1 ≤ m := hm.pos
  have h := three_mul_back hm h3
  omega

/-- `3·back m + 1 = 2m`: the forward step out of `back m`. -/
theorem three_mul_back_add_one : 3 * back m + 1 = 2 * m := by
  have h1 : 1 ≤ m := hm.pos
  have h := three_mul_back hm h3
  omega

theorem a_back : a (back m) = 1 := by
  have hkey := three_mul_back_add_one hm h3
  have hm0 : m ≠ 0 := by have := hm.pos; omega
  have hnd : ¬ (2 ∣ m) := by
    have := Nat.odd_iff.mp hm
    omega
  unfold a
  rw [hkey, padicValNat.mul (by norm_num) hm0, padicValNat.self (by norm_num),
    padicValNat.eq_zero_of_not_dvd hnd]

theorem T_back : T (back m) = m := by
  have h := two_pow_a_mul_T (back m)
  rw [a_back hm h3, three_mul_back_add_one hm h3] at h
  omega

/-- The orbit of `back m` is `back m` followed by the orbit of `m`. -/
theorem orbit_back (n : ℕ) : orbit (back m) (n + 1) = orbit m n := by
  induction n with
  | zero => rw [orbit_succ, orbit_zero, T_back hm h3, orbit_zero]
  | succ n ih =>
    rw [orbit_succ, ih, orbit_succ]

theorem S_back (n : ℕ) : S (back m) (n + 1) = 1 + S m n := by
  induction n with
  | zero => rw [S_succ, S_zero, orbit_zero, a_back hm h3, S_zero]
  | succ n ih =>
    rw [S_succ, ih, orbit_back hm h3, S_succ]
    omega

/-- **L1.** Confinement is inherited backward, with one horizon to spare. -/
theorem back_confinedUpTo {N : ℕ} (hc : ConfinedUpTo N m) : ConfinedUpTo (N + 1) (back m) := by
  intro j hj
  match j with
  | 0 => simp
  | (i + 1) =>
    have hiN : i ≤ N := by omega
    rw [S_back hm h3, pow_add, pow_one]
    have hmi := hc i hiN
    have h3i : (0 : ℕ) < 3 ^ i := pow_pos (by norm_num) i
    calc 2 ^ 1 * 2 ^ S m i ≤ 2 ^ 1 * 3 ^ i := Nat.mul_le_mul_left _ hmi
      _ ≤ 3 ^ 1 * 3 ^ i := Nat.mul_le_mul_right _ (by norm_num)
      _ = 3 ^ (i + 1) := by ring

/-- **L1, infinite form.** The hypothesis and conclusion are `Divergence.ZeroConfined` unfolded. -/
theorem back_step_zeroConfined (hz : ∀ n, 2 ^ S m n ≤ 3 ^ n) :
    ∀ n, 2 ^ S (back m) n ≤ 3 ^ n := by
  intro n
  match n with
  | 0 => simp
  | (i + 1) =>
    have := back_confinedUpTo hm h3 (N := i) (fun j hj => hz j)
    exact this (i + 1) (le_refl _)

end

end Descent
