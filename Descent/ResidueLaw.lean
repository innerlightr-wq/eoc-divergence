import Descent.BackStep

/-!
# L4: the residue law for least confined integers

A least element of `{m | Odd m ∧ ConfinedUpTo N m}` is `≡ 3 or 7 (mod 12)`.

Two independent ingredients: confinement forces the first valuation to be `1`, hence
`m ≡ 3 (mod 4)`; and minimality rules out `m ≡ 2 (mod 3)`, because L1 would then produce a
strictly smaller member. Monotonicity of `ConfinedUpTo` is **used** (L1 delivers horizon `N+1`,
the set asks for `N`), not assumed.
-/

namespace Descent

open Divergence

theorem S_one (m : ℕ) : S m 1 = a m := by simp [S]

/-- Confinement forces the first valuation to be `1`. -/
theorem a_eq_one_of_confined {N m : ℕ} (hm : Odd m) (hN : 1 ≤ N) (hc : ConfinedUpTo N m) :
    a m = 1 := by
  have h1 := hc 1 hN
  rw [S_one, pow_one] at h1
  have hpos := a_pos hm
  by_contra hne
  have h2 : 2 ≤ a m := by omega
  have h4 : (4 : ℕ) ≤ 2 ^ a m := by
    calc (4 : ℕ) = 2 ^ 2 := by norm_num
      _ ≤ 2 ^ a m := Nat.pow_le_pow_right (by norm_num) h2
  omega

theorem mod_four_of_confined {N m : ℕ} (hm : Odd m) (hN : 1 ≤ N) (hc : ConfinedUpTo N m) :
    m % 4 = 3 := by
  have ha := a_eq_one_of_confined hm hN hc
  have hkey := two_pow_a_mul_T m
  rw [ha, pow_one] at hkey
  have hTodd := Nat.odd_iff.mp (odd_T m)
  have hmodd := Nat.odd_iff.mp hm
  omega

/-- **L4, the descent half.** A least confined integer is not `≡ 2 (mod 3)`. -/
theorem least_confined_mod_three {N r : ℕ} (hr : IsLeast {m | Odd m ∧ ConfinedUpTo N m} r) :
    r % 3 ≠ 2 := by
  intro h3
  have hodd : Odd r := hr.1.1
  have hconf : ConfinedUpTo N r := hr.1.2
  have hmem : back r ∈ {m | Odd m ∧ ConfinedUpTo N m} :=
    ⟨odd_back hodd h3, confinedUpTo_mono (Nat.le_succ N) (back_confinedUpTo hodd h3 hconf)⟩
  have hle := hr.2 hmem
  have hlt := back_lt hodd h3
  omega

/-- **L4.** -/
theorem least_confined_mod12 {N r : ℕ} (hN : 1 ≤ N)
    (hr : IsLeast {m | Odd m ∧ ConfinedUpTo N m} r) :
    r % 12 = 3 ∨ r % 12 = 7 := by
  have h4 := mod_four_of_confined hr.1.1 hN hr.1.2
  have h3 := least_confined_mod_three hr
  omega

end Descent
