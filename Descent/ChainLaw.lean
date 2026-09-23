import Descent.BackStep

/-!
# L2: the chain law

The backward `d = 1` chain from `x` has length **exactly** `v₃(x+1)`, and after `j` steps

```
3^j · (back^[j] x + 1) = 2^j · (x + 1).
```

The closed form is stated division-free, so no `ℕ`-division appears downstream.

**This is where descent lives.** The only budget available to a backward chain is the 3-adic
valuation of `x + 1` — the contracting place of `3/2`.
-/

namespace Descent

open Divergence

/-- The backward step is available exactly when `3 ∣ x + 1`. -/
theorem back_available_iff (x : ℕ) : x % 3 = 2 ↔ 3 ∣ x + 1 := by omega

/-- One step, division-free. -/
theorem three_mul_back_succ {x : ℕ} (hx : Odd x) (h3 : 3 ∣ x + 1) :
    3 * (back x + 1) = 2 * (x + 1) := by
  have hx3 : x % 3 = 2 := (back_available_iff x).mpr h3
  have h := three_mul_back hx hx3
  have h1 : 1 ≤ x := hx.pos
  omega

/-- The chain, division-free: oddness and the closed form together. -/
theorem back_iterate_spec {x : ℕ} (hx : Odd x) :
    ∀ j, 3 ^ j ∣ x + 1 → Odd (back^[j] x) ∧ 3 ^ j * (back^[j] x + 1) = 2 ^ j * (x + 1) := by
  intro j
  induction j with
  | zero => intro _; simpa using hx
  | succ j ih =>
    intro hdvd
    have hj : (3 : ℕ) ^ j ∣ x + 1 := dvd_trans (pow_dvd_pow 3 (by omega)) hdvd
    obtain ⟨hodd, heq⟩ := ih hj
    obtain ⟨k, hk⟩ := hdvd
    have hpos : (0 : ℕ) < 3 ^ j := pow_pos (by norm_num) j
    have hy1 : back^[j] x + 1 = 3 * (2 ^ j * k) := by
      refine Nat.eq_of_mul_eq_mul_left hpos ?_
      rw [heq, hk]
      ring
    have h3y : (3 : ℕ) ∣ back^[j] x + 1 := ⟨2 ^ j * k, hy1⟩
    have hstep := three_mul_back_succ hodd h3y
    have hy3 : back^[j] x % 3 = 2 := (back_available_iff _).mpr h3y
    rw [Function.iterate_succ_apply']
    refine ⟨odd_back hodd hy3, ?_⟩
    calc (3 : ℕ) ^ (j + 1) * (back (back^[j] x) + 1)
        = 3 ^ j * (3 * (back (back^[j] x) + 1)) := by ring
      _ = 3 ^ j * (2 * (back^[j] x + 1)) := by rw [hstep]
      _ = 2 * (3 ^ j * (back^[j] x + 1)) := by ring
      _ = 2 * (2 ^ j * (x + 1)) := by rw [heq]
      _ = 2 ^ (j + 1) * (x + 1) := by ring

theorem odd_back_iterate {x j : ℕ} (hx : Odd x) (hdvd : 3 ^ j ∣ x + 1) : Odd (back^[j] x) :=
  (back_iterate_spec hx j hdvd).1

/-- **L2, closed form.** -/
theorem three_pow_mul_back_iterate {x j : ℕ} (hx : Odd x) (hdvd : 3 ^ j ∣ x + 1) :
    3 ^ j * (back^[j] x + 1) = 2 ^ j * (x + 1) :=
  (back_iterate_spec hx j hdvd).2

/-- The `(j+1)`-st step is available exactly when `3^{j+1} ∣ x+1`. -/
theorem back_step_available {x j : ℕ} (hx : Odd x) (hdvd : 3 ^ j ∣ x + 1) :
    3 ∣ back^[j] x + 1 ↔ 3 ^ (j + 1) ∣ x + 1 := by
  have heq := three_pow_mul_back_iterate hx hdvd
  have hcop : Nat.Coprime (3 ^ (j + 1)) (2 ^ j) :=
    Nat.Coprime.pow _ _ (show Nat.Coprime 3 2 by decide)
  constructor
  · rintro ⟨c, hc⟩
    have hmul : (3 : ℕ) ^ (j + 1) * c = 2 ^ j * (x + 1) := by
      rw [← heq, hc]; ring
    exact hcop.dvd_of_dvd_mul_left ⟨c, hmul.symm⟩
  · rintro ⟨k, hk⟩
    have hpos : (0 : ℕ) < 3 ^ j := pow_pos (by norm_num) j
    refine ⟨2 ^ j * k, ?_⟩
    refine Nat.eq_of_mul_eq_mul_left hpos ?_
    rw [heq, hk]
    ring

/-- **L2, chain length.** The chain runs for exactly `v₃(x+1)` steps. -/
theorem back_chain_length {x : ℕ} (hx : Odd x) :
    (∀ j < padicValNat 3 (x + 1), 3 ∣ back^[j] x + 1)
      ∧ ¬ (3 ∣ back^[padicValNat 3 (x + 1)] x + 1) := by
  have : Fact (Nat.Prime 3) := ⟨Nat.prime_three⟩
  have hx1 : x + 1 ≠ 0 := by omega
  have hdvdv : (3 : ℕ) ^ padicValNat 3 (x + 1) ∣ x + 1 := pow_padicValNat_dvd
  refine ⟨fun j hj => ?_, fun hcon => ?_⟩
  · have hdj : (3 : ℕ) ^ j ∣ x + 1 := dvd_trans (pow_dvd_pow 3 (by omega)) hdvdv
    exact (back_step_available hx hdj).mpr (dvd_trans (pow_dvd_pow 3 (by omega)) hdvdv)
  · exact pow_succ_padicValNat_not_dvd hx1 ((back_step_available hx hdvdv).mp hcon)

end Descent
