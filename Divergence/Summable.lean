import Divergence.WindowedSparsity
import Mathlib.Analysis.SpecificLimits.Normed

/-!
# Reciprocal summability of a divergent orbit (Curry Prop. 3.1; paper Prop. 4.9)

Summing the windowed sparsity bound over the dyadic blocks `[2^k, 2^{k+1})` gives
`Σ 1/m_n < ∞` for every divergent accelerated orbit.

The block `[2^k, 2^{k+1})` is exactly a window of length `2^k` based at `a = 2^k`, so
`exists_window_sparsity` applies with no bookkeeping. The count is of *times* `n`, not values,
which is legitimate because a divergent orbit is injective. Each such time contributes at most
`2^{-k}`, so the total is dominated by `Σ 4(k+1)(θ/2)^k` — convergent because `θ < 2`.

No `sorry`, `admit`, `axiom`, or `opaque`.
-/

namespace Divergence

open Finset Filter

/-! ## 1. The dominating series -/

theorem summable_window_series {θ : ℝ} (h0 : 0 ≤ θ) (h2 : θ < 2) :
    Summable (fun k : ℕ => 4 * ((k : ℝ) + 1) * (θ / 2) ^ k) := by
  have hr : ‖θ / 2‖ < 1 := by
    rw [Real.norm_eq_abs, abs_of_nonneg (by positivity)]
    linarith
  have hlin : Summable (fun k : ℕ => (k : ℝ) * (θ / 2) ^ k) := by
    have h := summable_pow_mul_geometric_of_norm_lt_one (R := ℝ) 1 hr
    refine h.congr fun k => ?_
    rw [pow_one]
  have hgeo : Summable (fun k : ℕ => (θ / 2) ^ k) := summable_geometric_of_norm_lt_one hr
  refine ((hlin.mul_left 4).add (hgeo.mul_left 4)).congr fun k => ?_
  ring

/-! ## 2. Few times per dyadic block -/

/-- At most `4(k+1)θ^k` **times** land in the block `[2^k, 2^{k+1})`. -/
theorem block_times_card_le {M : ℕ} (hM : Odd M) (hdiv : DivergentOrbit M) {θ : ℝ}
    (hws : ∀ A : Set ℕ, CollisionFree A → ∀ N a : ℕ, 1 ≤ a →
      ((A ∩ Set.Ico a (a + 2 ^ N)).ncard : ℝ) ≤ 4 * ((N : ℝ) + 1) * θ ^ N)
    (k n : ℕ) :
    (((Finset.range n).filter
        (fun i => 2 ^ k ≤ orbit M i ∧ orbit M i < 2 ^ (k + 1))).card : ℝ)
      ≤ 4 * ((k : ℝ) + 1) * θ ^ k := by
  obtain ⟨_, hcf⟩ := raw_injective_of_divergent hM hdiv
  have horb : Function.Injective (orbit M) := injective_of_divergent hdiv
  set F := (Finset.range n).filter
      (fun i => 2 ^ k ≤ orbit M i ∧ orbit M i < 2 ^ (k + 1)) with hF
  set A := Set.range (fun j => U^[j] M) with hA
  have hsplit : (2 : ℕ) ^ k + 2 ^ k = 2 ^ (k + 1) := by ring
  have hfin : (A ∩ Set.Ico (2 ^ k) (2 ^ k + 2 ^ k)).Finite :=
    Set.Finite.subset (Set.finite_Ico _ _) Set.inter_subset_right
  have hsub : ↑(F.image (orbit M)) ⊆ A ∩ Set.Ico (2 ^ k) (2 ^ k + 2 ^ k) := by
    intro y hy
    simp only [Finset.coe_image, Set.mem_image, Finset.mem_coe, hF, Finset.mem_filter] at hy
    obtain ⟨i, ⟨_, hi1, hi2⟩, rfl⟩ := hy
    refine ⟨orbit_range_subset hM ⟨i, rfl⟩, ?_⟩
    rw [Set.mem_Ico, hsplit]
    exact ⟨hi1, hi2⟩
  have hcardimg : (F.image (orbit M)).card = F.card :=
    Finset.card_image_of_injective _ horb
  calc (F.card : ℝ) = ((F.image (orbit M)).card : ℝ) := by rw [hcardimg]
    _ = ((↑(F.image (orbit M)) : Set ℕ).ncard : ℝ) := by rw [Set.ncard_coe_finset]
    _ ≤ ((A ∩ Set.Ico (2 ^ k) (2 ^ k + 2 ^ k)).ncard : ℝ) := by
        exact_mod_cast Set.ncard_le_ncard hsub hfin
    _ ≤ 4 * ((k : ℝ) + 1) * θ ^ k := hws A hcf k (2 ^ k) Nat.one_le_two_pow

/-! ## 3. Reciprocal summability -/

theorem summable_inv_orbit {M : ℕ} (hM : Odd M) (hdiv : DivergentOrbit M) :
    Summable (fun n => 1 / (orbit M n : ℝ)) := by
  classical
  obtain ⟨θ, hθ1, hθ2, hws⟩ := exists_window_sparsity
  have hθ0 : (0 : ℝ) ≤ θ := le_trans zero_le_one hθ1
  have hser := summable_window_series hθ0 hθ2
  set C : ℝ := ∑' k : ℕ, 4 * ((k : ℝ) + 1) * (θ / 2) ^ k with hC
  have hnonneg : ∀ n, 0 ≤ 1 / (orbit M n : ℝ) := by
    intro n
    have := orbit_pos hM n
    positivity
  refine summable_of_sum_range_le (c := C) hnonneg ?_
  intro n
  -- group the times `i < n` by the dyadic block of `orbit M i`
  set g : ℕ → ℕ := fun i => Nat.log 2 (orbit M i) with hg
  set B : ℕ := (Finset.range n).sup g with hB
  have hmaps : ∀ i ∈ Finset.range n, g i ∈ Finset.range (B + 1) := by
    intro i hi
    exact Finset.mem_range.mpr (by have := Finset.le_sup (f := g) hi; omega)
  have hgroup := Finset.sum_fiberwise_of_maps_to hmaps (fun i => 1 / (orbit M i : ℝ))
  rw [← hgroup]
  -- each fibre sits inside a dyadic block, and each of its terms is at most `2^{-k}`
  have hfibre : ∀ k ∈ Finset.range (B + 1),
      (∑ i ∈ (Finset.range n).filter (fun i => g i = k), 1 / (orbit M i : ℝ))
        ≤ 4 * ((k : ℝ) + 1) * (θ / 2) ^ k := by
    intro k _
    have hsubset : (Finset.range n).filter (fun i => g i = k)
        ⊆ (Finset.range n).filter
            (fun i => 2 ^ k ≤ orbit M i ∧ orbit M i < 2 ^ (k + 1)) := by
      intro i hi
      rw [Finset.mem_filter] at hi ⊢
      obtain ⟨hin, hik⟩ := hi
      have hne : orbit M i ≠ 0 := (orbit_pos hM i).ne'
      have hgi : Nat.log 2 (orbit M i) = k := by rw [hg] at hik; exact hik
      refine ⟨hin, ?_, ?_⟩
      · have h := Nat.pow_log_le_self 2 hne
        rwa [hgi] at h
      · have h := Nat.lt_pow_succ_log_self (by norm_num : 1 < 2) (orbit M i)
        rwa [hgi] at h
    have hterm : ∀ i ∈ (Finset.range n).filter (fun i => g i = k),
        1 / (orbit M i : ℝ) ≤ (1 / 2 : ℝ) ^ k := by
      intro i hi
      have hi' := hsubset hi
      rw [Finset.mem_filter] at hi'
      have hlow : ((2 : ℝ) ^ k) ≤ (orbit M i : ℝ) := by exact_mod_cast hi'.2.1
      have hppos : (0 : ℝ) < (2 : ℝ) ^ k := by positivity
      rw [div_pow, one_pow]
      exact one_div_le_one_div_of_le hppos hlow
    calc (∑ i ∈ (Finset.range n).filter (fun i => g i = k), 1 / (orbit M i : ℝ))
        ≤ ∑ _i ∈ (Finset.range n).filter (fun i => g i = k), (1 / 2 : ℝ) ^ k :=
          Finset.sum_le_sum hterm
      _ = (((Finset.range n).filter (fun i => g i = k)).card : ℝ) * (1 / 2 : ℝ) ^ k := by
          rw [Finset.sum_const, nsmul_eq_mul]
      _ ≤ 4 * ((k : ℝ) + 1) * θ ^ k * (1 / 2 : ℝ) ^ k := by
          refine mul_le_mul_of_nonneg_right ?_ (by positivity)
          refine le_trans ?_ (block_times_card_le hM hdiv hws k n)
          exact_mod_cast Finset.card_le_card hsubset
      _ = 4 * ((k : ℝ) + 1) * (θ / 2) ^ k := by
          rw [div_pow, div_pow, one_pow]
          ring
  calc (∑ k ∈ Finset.range (B + 1),
          ∑ i ∈ (Finset.range n).filter (fun i => g i = k), 1 / (orbit M i : ℝ))
      ≤ ∑ k ∈ Finset.range (B + 1), 4 * ((k : ℝ) + 1) * (θ / 2) ^ k :=
        Finset.sum_le_sum hfibre
    _ ≤ C := by
        exact Summable.sum_le_tsum _ (fun k _ => by positivity) hser

end Divergence
