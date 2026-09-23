import Mathlib.NumberTheory.Padics.PadicVal.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# The accelerated `3x+1` map: definitions and the aggregate identity

This file sets up the accelerated Collatz map on odd naturals and proves the two structural
facts the rest of the development rests on: that the orbit stays odd and positive, and the
**aggregate identity** `2^{S_n} · m_n = 3^n · m_0 + C_n` (paper Lemma 2.4).

Definitions follow the paper:

* `a m = v₂(3m+1)`,
* `T m = (3m+1) / 2^{a m}`,
* `orbit m n = Tⁿ m`,
* `S m n = Σ_{i<n} a (orbit m i)`,
* `C` the carry, `C 0 = 0`, `C (n+1) = 3 · C n + 2^{S n}`.

`a` and `T` are `noncomputable` (via `padicValNat`); nothing downstream needs to evaluate them.

No `sorry`, `admit`, `axiom`, or `opaque`.
-/

namespace Divergence

open Finset

/-! ## 1. The map -/

/-- `a m = v₂(3m+1)`, the 2-adic valuation driving the accelerated map. -/
noncomputable def a (m : ℕ) : ℕ := padicValNat 2 (3 * m + 1)

/-- The accelerated Collatz map `T m = (3m+1)/2^{v₂(3m+1)}`. -/
noncomputable def T (m : ℕ) : ℕ := (3 * m + 1) / 2 ^ a m

/-- The orbit `orbit m n = Tⁿ m`. -/
noncomputable def orbit (m : ℕ) : ℕ → ℕ := fun n => Nat.rec m (fun _ ih => T ih) n

@[simp] theorem orbit_zero (m : ℕ) : orbit m 0 = m := rfl

theorem orbit_succ (m n : ℕ) : orbit m (n + 1) = T (orbit m n) := rfl

/-- Total valuation `S m n = Σ_{i<n} a (orbit m i)`. -/
noncomputable def S (m n : ℕ) : ℕ := ∑ i ∈ range n, a (orbit m i)

@[simp] theorem S_zero (m : ℕ) : S m 0 = 0 := Finset.sum_range_zero _

theorem S_succ (m n : ℕ) : S m (n + 1) = S m n + a (orbit m n) :=
  Finset.sum_range_succ _ n

/-- The carry `C`, from the aggregate identity: `C 0 = 0`, `C (n+1) = 3·C n + 2^{S n}`. -/
noncomputable def C (m : ℕ) : ℕ → ℕ :=
  fun n => Nat.rec 0 (fun k ih => 3 * ih + 2 ^ S m k) n

@[simp] theorem C_zero (m : ℕ) : C m 0 = 0 := rfl

theorem C_succ (m n : ℕ) : C m (n + 1) = 3 * C m n + 2 ^ S m n := rfl

/-! ## 2. Exactness of the division -/

/-- **Exactness.** `2^{a m} · T m = 3m+1`, for every `m` — no oddness needed, since
`3m+1 ≥ 1` is never `0` and `2^{v₂(·)}` always divides. -/
theorem two_pow_a_mul_T (m : ℕ) : 2 ^ a m * T m = 3 * m + 1 :=
  Nat.mul_div_cancel' (pow_padicValNat_dvd)

/-! ## 3. Oddness and positivity -/

/-- For odd `m`, `3m+1` is even, so `a m ≥ 1`. (False for even `m`: there `a m = 0`.) -/
theorem a_pos {m : ℕ} (hm : Odd m) : 1 ≤ a m := by
  unfold a
  have h2dvd : (2 : ℕ) ∣ (3 * m + 1) := by
    obtain ⟨w, hw⟩ := hm
    exact ⟨3 * w + 2, by rw [hw]; ring⟩
  have hne0 : padicValNat 2 (3 * m + 1) ≠ 0 := by
    intro hcon
    rcases padicValNat.eq_zero_iff.mp hcon with h1 | h1 | h1
    · norm_num at h1
    · omega
    · exact h1 h2dvd
  omega

/-- `T m` is odd for **every** `m`: dividing out the full power of `2` leaves an odd number. -/
theorem odd_T (m : ℕ) : Odd (T m) := by
  obtain ⟨k, hk0⟩ := (pow_padicValNat_dvd : 2 ^ a m ∣ (3 * m + 1))
  have hk : 3 * m + 1 = 2 ^ a m * k := hk0
  have hTm : T m = k := by
    unfold T
    rw [hk, Nat.mul_div_cancel_left k (by positivity)]
  rw [hTm]
  have hkne : k ≠ 0 := by
    intro hk0'
    rw [hk0', mul_zero] at hk
    omega
  have haeq : a m = padicValNat 2 (3 * m + 1) := rfl
  have hval : padicValNat 2 (3 * m + 1) = a m + padicValNat 2 k := by
    conv_lhs => rw [hk]
    rw [padicValNat.mul (by positivity) hkne, padicValNat_base_pow (by norm_num) (a m)]
  have hz : padicValNat 2 k = 0 := by
    have h2 := hval
    rw [← haeq] at h2
    omega
  rw [Nat.odd_iff]
  rcases padicValNat.eq_zero_iff.mp hz with h1 | h1 | h1
  · exact absurd h1 (by norm_num)
  · exact absurd h1 hkne
  · omega

theorem odd_orbit {m : ℕ} (hm : Odd m) (n : ℕ) : Odd (orbit m n) := by
  induction n with
  | zero => rwa [orbit_zero]
  | succ n _ => rw [orbit_succ]; exact odd_T _

theorem orbit_pos {m : ℕ} (hm : Odd m) (n : ℕ) : 0 < orbit m n :=
  (odd_orbit hm n).pos

/-! ## 4. Restart -/

/-- **Orbit restart.** `orbit m (n+k) = orbit (orbit m n) k`. -/
theorem orbit_add (m n k : ℕ) : orbit m (n + k) = orbit (orbit m n) k := by
  induction k with
  | zero => rfl
  | succ k ih =>
    have h : n + (k + 1) = (n + k) + 1 := by omega
    rw [h, orbit_succ, ih, orbit_succ]

/-- **Valuation restart.** `S m (n+k) = S m n + S (orbit m n) k`. -/
theorem S_add (m n k : ℕ) : S m (n + k) = S m n + S (orbit m n) k := by
  induction k with
  | zero => simp
  | succ k ih =>
    have h : n + (k + 1) = (n + k) + 1 := by omega
    rw [h, S_succ, ih, S_succ, orbit_add, add_assoc]

/-! ## 5. The aggregate identity -/

/-- **Paper Lemma 2.4.** `2^{S_n} · m_n = 3^n · m_0 + C_n`, for every `m` — the step relation
`two_pow_a_mul_T` is unconditional, so no oddness hypothesis is needed. -/
theorem aggregate_identity (m n : ℕ) :
    2 ^ S m n * orbit m n = 3 ^ n * m + C m n := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [S_succ, C_succ, orbit_succ, pow_add, mul_assoc, two_pow_a_mul_T]
    have key : 2 ^ S m n * (3 * orbit m n + 1)
        = 3 * (2 ^ S m n * orbit m n) + 2 ^ S m n := by ring
    rw [key, ih]
    ring

/-- The carry is strictly positive from time `1` on. -/
theorem C_pos (m : ℕ) {n : ℕ} (hn : 1 ≤ n) : 0 < C m n := by
  obtain ⟨k, rfl⟩ : ∃ k, n = k + 1 := ⟨n - 1, by omega⟩
  rw [C_succ]
  have : 0 < 2 ^ S m k := pow_pos (by norm_num) _
  omega

end Divergence
