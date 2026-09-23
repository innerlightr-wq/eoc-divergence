import Mathlib.Data.Fin.Tuple.NatAntidiagonal
import Mathlib.Data.Nat.Choose.Sum
import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-!
# Confined words as compositions, and their dyadic mass

A word of length `N` is a tuple `d : Fin N → ℕ` with every letter at least `1`; with total
`S_N(d) = s` these are exactly the **positive compositions of `s` into `N` parts**, counted by
`C(s-1, N-1)` (`card_comps`).

`d` is **`c`-confined** when `2^{S_j} ≤ 2^c · 3^j` for every `j ≤ N` — the integral form of
`S_j ≤ αj + c`, the same shape as `Divergence.ZeroConfined`. Confinement caps the total, so the
**dyadic mass**

```
p N c = Σ_{c-confined d of length N} 2^{-S_N(d)}
```

is a finite sum.

This library is self-contained: it imports nothing from `Divergence`.

No `sorry`, `admit`, `axiom`, or `opaque`.
-/

namespace Occupation

open Finset

/-! ## 1. Partial sums -/

/-- The letters of `d`, extended by `0` past the end. -/
def letter {N : ℕ} (d : Fin N → ℕ) (i : ℕ) : ℕ := if h : i < N then d ⟨i, h⟩ else 0

/-- Partial sum `S_j(d) = d₀ + ⋯ + d_{j-1}`. -/
def psum {N : ℕ} (d : Fin N → ℕ) (j : ℕ) : ℕ := ∑ i ∈ range j, letter d i

@[simp] theorem psum_zero {N : ℕ} (d : Fin N → ℕ) : psum d 0 = 0 := by
  simp [psum]

theorem psum_succ' {N : ℕ} (d : Fin N → ℕ) (j : ℕ) :
    psum d (j + 1) = psum d j + letter d j := Finset.sum_range_succ _ j

theorem psum_succ {N : ℕ} (d : Fin N → ℕ) {j : ℕ} (hj : j < N) :
    psum d (j + 1) = psum d j + d ⟨j, hj⟩ := by
  rw [psum_succ']
  simp [letter, hj]

theorem psum_total {N : ℕ} (d : Fin N → ℕ) : psum d N = ∑ i, d i := by
  rw [psum, ← Fin.sum_univ_eq_sum_range (letter d) N]
  exact Finset.sum_congr rfl fun i _ => by simp [letter, i.isLt]

theorem psum_mono {N : ℕ} (d : Fin N → ℕ) {j k : ℕ} (h : j ≤ k) : psum d j ≤ psum d k := by
  unfold psum
  refine Finset.sum_le_sum_of_subset_of_nonneg (fun i hi => ?_) (fun i _ _ => Nat.zero_le _)
  exact Finset.mem_range.mpr (lt_of_lt_of_le (Finset.mem_range.mp hi) h)

/-! ## 2. Confinement -/

/-- `d` is `c`-confined: `2^{S_j} ≤ 2^c · 3^j` for every `j ≤ N`. -/
def Confined {N : ℕ} (c : ℕ) (d : Fin N → ℕ) : Prop :=
  ∀ j ≤ N, 2 ^ psum d j ≤ 2 ^ c * 3 ^ j

instance {N c : ℕ} (d : Fin N → ℕ) : Decidable (Confined c d) := by
  unfold Confined
  infer_instance

theorem Confined.mono {N c c' : ℕ} {d : Fin N → ℕ} (h : Confined c d) (hcc : c ≤ c') :
    Confined c' d := by
  intro j hj
  exact le_trans (h j hj) (Nat.mul_le_mul_right _ (Nat.pow_le_pow_right (by norm_num) hcc))

/-! ## 3. Compositions -/

/-- Positive compositions of `s` into `N` parts. -/
def comps (N s : ℕ) : Finset (Fin N → ℕ) :=
  (Finset.Nat.antidiagonalTuple N s).filter (fun d => ∀ i, 1 ≤ d i)

/-- The `c`-confined ones among them. -/
def confComps (N c s : ℕ) : Finset (Fin N → ℕ) := (comps N s).filter (Confined c)

theorem mem_comps {N s : ℕ} {d : Fin N → ℕ} :
    d ∈ comps N s ↔ (∑ i, d i) = s ∧ ∀ i, 1 ≤ d i := by
  rw [comps, Finset.mem_filter, Finset.Nat.mem_antidiagonalTuple]

theorem mem_confComps {N c s : ℕ} {d : Fin N → ℕ} :
    d ∈ confComps N c s ↔ ((∑ i, d i) = s ∧ ∀ i, 1 ≤ d i) ∧ Confined c d := by
  rw [confComps, Finset.mem_filter, mem_comps]

/-- Every part is at least `1`, so the total is at least the number of parts. -/
theorem le_of_mem_comps {N s : ℕ} {d : Fin N → ℕ} (hd : d ∈ comps N s) : N ≤ s := by
  rw [mem_comps] at hd
  calc N = ∑ _i : Fin N, 1 := by simp
    _ ≤ ∑ i, d i := Finset.sum_le_sum fun i _ => hd.2 i
    _ = s := hd.1

/-- **Stars and bars.** -/
theorem card_comps : ∀ {N s : ℕ}, 1 ≤ N → N ≤ s → (comps N s).card = (s - 1).choose (N - 1) := by
  intro N
  induction N with
  | zero => intro s h; omega
  | succ N ih =>
    intro s _ hs
    rcases Nat.eq_zero_or_pos N with rfl | hN
    · -- length `1`: the single word `![s]`
      have : comps 1 s = {fun _ => s} := by
        ext d
        rw [mem_comps, Finset.mem_singleton]
        constructor
        · rintro ⟨hsum, _⟩
          funext i
          rw [Fin.fin_one_eq_zero i]
          simpa using hsum
        · rintro rfl
          exact ⟨by simp, fun _ => by omega⟩
      rw [this, Finset.card_singleton]
      simp
    · -- split on the first letter
      have hmaps : ∀ d ∈ comps (N + 1) s, d 0 ∈ Finset.Icc 1 (s - N) := by
        intro d hd
        rw [mem_comps] at hd
        rw [Finset.mem_Icc]
        refine ⟨hd.2 0, ?_⟩
        have htail : N ≤ ∑ i : Fin N, d i.succ := by
          calc N = ∑ _i : Fin N, 1 := by simp
            _ ≤ ∑ i : Fin N, d i.succ := Finset.sum_le_sum fun i _ => hd.2 _
        have := hd.1
        rw [Fin.sum_univ_succ] at this
        omega
      rw [Finset.card_eq_sum_card_fiberwise hmaps]
      -- each fibre is a composition of `s - a` into `N` parts
      have hfib : ∀ a ∈ Finset.Icc 1 (s - N),
          ((comps (N + 1) s).filter (fun d => d 0 = a)).card = (comps N (s - a)).card := by
        intro a ha
        rw [Finset.mem_Icc] at ha
        refine Finset.card_nbij' (fun d => Fin.tail d) (fun e => Fin.cons a e) ?_ ?_ ?_ ?_
        · intro d hd
          rw [Finset.mem_coe, Finset.mem_filter, mem_comps] at hd
          rw [Finset.mem_coe, mem_comps]
          have hsum := hd.1.1
          rw [Fin.sum_univ_succ, hd.2] at hsum
          refine ⟨?_, fun i => hd.1.2 _⟩
          show ∑ i : Fin N, Fin.tail d i = s - a
          have htl : ∑ i : Fin N, Fin.tail d i = ∑ i : Fin N, d i.succ := rfl
          omega
        · intro e he
          rw [Finset.mem_coe, mem_comps] at he
          rw [Finset.mem_coe, Finset.mem_filter, mem_comps]
          refine ⟨⟨?_, ?_⟩, by simp⟩
          · rw [Fin.sum_univ_succ]
            simp only [Fin.cons_zero, Fin.cons_succ]
            omega
          · intro i
            refine Fin.cases ?_ ?_ i
            · simpa using (by omega : 1 ≤ a)
            · intro j
              simpa using he.2 j
        · intro d hd
          rw [Finset.mem_coe, Finset.mem_filter] at hd
          rw [← hd.2]
          exact Fin.cons_self_tail d
        · intro e _
          simp
      rw [Finset.sum_congr rfl hfib]
      -- each inner card is a binomial coefficient
      have hinner : ∀ a ∈ Finset.Icc 1 (s - N),
          (comps N (s - a)).card = (s - a - 1).choose (N - 1) := by
        intro a ha
        rw [Finset.mem_Icc] at ha
        exact ih hN (by omega)
      rw [Finset.sum_congr rfl hinner]
      -- reindex and apply the hockey-stick identity
      have hreindex : ∑ a ∈ Finset.Icc 1 (s - N), (s - a - 1).choose (N - 1)
          = ∑ u ∈ Finset.Icc (N - 1) (s - 2), u.choose (N - 1) := by
        refine Finset.sum_nbij' (fun a => s - a - 1) (fun u => s - u - 1) ?_ ?_ ?_ ?_ ?_
        · intro a ha; rw [Finset.mem_Icc] at ha ⊢; omega
        · intro u hu; rw [Finset.mem_Icc] at hu ⊢; omega
        · intro a ha; rw [Finset.mem_Icc] at ha; omega
        · intro u hu; rw [Finset.mem_Icc] at hu; omega
        · intro a _; rfl
      rw [hreindex, Nat.sum_Icc_choose]
      congr 1 <;> omega

/-! ## 4. Confinement caps the total -/

theorem confComps_eq_empty {N c s : ℕ} (hN : 1 ≤ N) (h : 2 * N + c ≤ s) :
    confComps N c s = ∅ := by
  rw [Finset.eq_empty_iff_forall_notMem]
  intro d hd
  rw [mem_confComps] at hd
  obtain ⟨⟨hsum, _⟩, hconf⟩ := hd
  have hcap := hconf N (le_refl N)
  rw [psum_total, hsum] at hcap
  -- `3^N < 4^N = 2^{2N}` for `N ≥ 1`
  have h34 : (3 : ℕ) ^ N < 2 ^ (2 * N) := by
    have : (2 : ℕ) ^ (2 * N) = 4 ^ N := by
      rw [pow_mul]
      norm_num
    rw [this]
    exact Nat.pow_lt_pow_left (by norm_num) (by omega)
  have hlt : (2 : ℕ) ^ s < 2 ^ (c + 2 * N) := by
    calc (2 : ℕ) ^ s ≤ 2 ^ c * 3 ^ N := hcap
      _ < 2 ^ c * 2 ^ (2 * N) :=
          mul_lt_mul_of_pos_left h34 (pow_pos (by norm_num) c)
      _ = 2 ^ (c + 2 * N) := by rw [pow_add]
  have := (Nat.pow_lt_pow_iff_right (by norm_num : 1 < 2)).mp hlt
  omega

/-! ## 5. The dyadic mass -/

/-- All `c`-confined words of length `N`. -/
def confWords (N c : ℕ) : Finset (Fin N → ℕ) :=
  (Finset.range (2 * N + c)).biUnion (fun s => confComps N c s)

/-- **The dyadic mass** `p N c = Σ_{c-confined d} 2^{-S_N(d)}`. -/
noncomputable def p (N c : ℕ) : ℝ := ∑ d ∈ confWords N c, (2 : ℝ)⁻¹ ^ psum d N

theorem p_eq_sum (N c : ℕ) :
    p N c = ∑ s ∈ Finset.range (2 * N + c), ((confComps N c s).card : ℝ) * (2 : ℝ)⁻¹ ^ s := by
  rw [p, confWords]
  rw [Finset.sum_biUnion]
  · refine Finset.sum_congr rfl fun s _ => ?_
    have : ∀ d ∈ confComps N c s, (2 : ℝ)⁻¹ ^ psum d N = (2 : ℝ)⁻¹ ^ s := by
      intro d hd
      rw [mem_confComps] at hd
      rw [psum_total, hd.1.1]
    rw [Finset.sum_congr rfl this, Finset.sum_const, nsmul_eq_mul]
  · intro s _ t _ hst
    simp only [Function.onFun, Finset.disjoint_left]
    intro d hd hd'
    rw [mem_confComps] at hd hd'
    exact hst (hd.1.1 ▸ hd'.1.1 ▸ rfl)

/-- The all-ones word is `0`-confined, hence `c`-confined, so the mass is positive. -/
theorem p_pos {N c : ℕ} (hN : 1 ≤ N) : 0 < p N c := by
  have hones : (fun _ => 1 : Fin N → ℕ) ∈ confWords N c := by
    rw [confWords, Finset.mem_biUnion]
    refine ⟨N, Finset.mem_range.mpr (by omega), ?_⟩
    rw [mem_confComps]
    refine ⟨⟨by simp, fun _ => le_refl 1⟩, ?_⟩
    intro j hj
    have hps : psum (fun _ => 1 : Fin N → ℕ) j = j := by
      unfold psum
      have hall : ∀ i ∈ Finset.range j, letter (fun _ => 1 : Fin N → ℕ) i = 1 := by
        intro i hi
        have hiN : i < N := lt_of_lt_of_le (Finset.mem_range.mp hi) hj
        simp [letter, hiN]
      rw [Finset.sum_congr rfl hall]
      simp
    rw [hps]
    calc (2 : ℕ) ^ j ≤ 3 ^ j := Nat.pow_le_pow_left (by norm_num) j
      _ ≤ 2 ^ c * 3 ^ j := Nat.le_mul_of_pos_left _ (pow_pos (by norm_num) c)
  refine Finset.sum_pos' (fun d _ => by positivity) ⟨_, hones, by positivity⟩

end Occupation
