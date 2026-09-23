import Divergence.Summable
import Mathlib.Analysis.SpecialFunctions.Exp

/-!
# The last maximum, and the zero-confined seed (paper Prop. 4.10)

A divergent orbit is restarted at the **last** index where the ratio

```
ρ n = 2^{S_n} / 3^n
```

attains its global maximum. Past that index `ρ` is strictly smaller, which is exactly
`2^{S_k(m*)} < 3^k` for the restarted seed `m* = m_{n₀}` — i.e. `m*` is zero-confined.

Everything is phrased through `ρ` rather than `R_n = S_n − n·log₂3`, so **no logarithm appears**.
`Real.exp` is used once, in `Q_le_exp`, to bound the Eliahou–Rozier carry product from above; it
is never inverted.

The last-maximum step is isolated as `exists_last_max`, a fact about arbitrary positive real
sequences tending to `0`, with no Collatz content.

No `sorry`, `admit`, `axiom`, or `opaque`.
-/

namespace Divergence

open Finset Filter

/-! ## 1. The ratio `ρ` and the carry product `Q` -/

/-- `ρ n = 2^{S_n}/3^n`. Zero-confinement is `ρ n ≤ 1`; `R_n → −∞` is `ρ n → 0`. -/
noncomputable def rho (M n : ℕ) : ℝ := (2 : ℝ) ^ S M n / (3 : ℝ) ^ n

/-- The Eliahou–Rozier carry product `∏_{i<n} (1 + 1/(3 m_i))`. -/
noncomputable def Q (M n : ℕ) : ℝ := ∏ i ∈ Finset.range n, (1 + 1 / (3 * (orbit M i : ℝ)))

theorem rho_pos (M n : ℕ) : 0 < rho M n := by
  unfold rho
  positivity

@[simp] theorem rho_zero (M : ℕ) : rho M 0 = 1 := by
  unfold rho
  simp

@[simp] theorem Q_zero (M : ℕ) : Q M 0 = 1 := by
  unfold Q
  simp

/-- **The step identity.** `Odd M` is essential: at `M = 0` the orbit value is `0` and the
factor `1 + 1/(3·0)` is not the true ratio. -/
theorem rho_succ {M : ℕ} (hM : Odd M) (n : ℕ) :
    rho M (n + 1) * (orbit M (n + 1) : ℝ)
      = rho M n * (orbit M n : ℝ) * (1 + 1 / (3 * (orbit M n : ℝ))) := by
  have hpos : (0 : ℝ) < (orbit M n : ℝ) := by exact_mod_cast orbit_pos hM n
  have hstep : (2 : ℝ) ^ a (orbit M n) * (orbit M (n + 1) : ℝ) = 3 * (orbit M n : ℝ) + 1 := by
    have h := two_pow_a_mul_T (orbit M n)
    rw [← orbit_succ] at h
    exact_mod_cast h
  have key : (2 : ℝ) ^ S M n * ((2 : ℝ) ^ a (orbit M n) * (orbit M (n + 1) : ℝ))
      / (3 : ℝ) ^ (n + 1) = rho M (n + 1) * (orbit M (n + 1) : ℝ) := by
    unfold rho
    rw [S_succ, pow_add]
    ring
  rw [← key, hstep]
  unfold rho
  field_simp
  ring

/-- **The product identity**, `ρ n · m_n = m_0 · Q n`. -/
theorem rho_mul_orbit {M : ℕ} (hM : Odd M) (n : ℕ) :
    rho M n * (orbit M n : ℝ) = (M : ℝ) * Q M n := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [rho_succ hM n, ih]
    unfold Q
    rw [Finset.prod_range_succ]
    ring

/-- `Q` is bounded by the exponential of the reciprocal sum. -/
theorem Q_le_exp {M : ℕ} (hM : Odd M) (n : ℕ) :
    Q M n ≤ Real.exp ((1 / 3) * ∑ i ∈ Finset.range n, 1 / (orbit M i : ℝ)) := by
  have hstep : ∀ i ∈ Finset.range n,
      1 + 1 / (3 * (orbit M i : ℝ)) ≤ Real.exp (1 / (3 * (orbit M i : ℝ))) := by
    intro i _
    have := Real.add_one_le_exp (1 / (3 * (orbit M i : ℝ)))
    linarith
  have hnn : ∀ i ∈ Finset.range n, (0 : ℝ) ≤ 1 + 1 / (3 * (orbit M i : ℝ)) := by
    intro i _
    have := orbit_pos hM i
    positivity
  calc Q M n ≤ ∏ i ∈ Finset.range n, Real.exp (1 / (3 * (orbit M i : ℝ))) :=
        Finset.prod_le_prod₀ (f := fun i => 1 + 1 / (3 * (orbit M i : ℝ)))
          (g := fun i => Real.exp (1 / (3 * (orbit M i : ℝ)))) hnn hstep
    _ = Real.exp (∑ i ∈ Finset.range n, 1 / (3 * (orbit M i : ℝ))) :=
        (Real.exp_sum _ _).symm
    _ = Real.exp ((1 / 3) * ∑ i ∈ Finset.range n, 1 / (orbit M i : ℝ)) := by
        congr 1
        rw [Finset.mul_sum]
        refine Finset.sum_congr rfl fun i _ => ?_
        field_simp

/-! ## 2. `ρ → 0` -/

theorem orbit_tendsto_atTop {M : ℕ} (hdiv : DivergentOrbit M) :
    Tendsto (fun n => (orbit M n : ℝ)) atTop atTop := by
  refine tendsto_atTop.mpr fun b => ?_
  obtain ⟨N₀, hN₀⟩ := hdiv ⌈b⌉₊
  refine Filter.eventually_atTop.mpr ⟨N₀, fun n hn => ?_⟩
  have h := hN₀ n hn
  have : (⌈b⌉₊ : ℝ) ≤ (orbit M n : ℝ) := by exact_mod_cast le_of_lt h
  exact le_trans (Nat.le_ceil b) this

theorem rho_tendsto_zero {M : ℕ} (hM : Odd M) (hdiv : DivergentOrbit M) :
    Tendsto (rho M) atTop (nhds 0) := by
  have hsum := summable_inv_orbit hM hdiv
  set Sinf : ℝ := ∑' i, 1 / (orbit M i : ℝ) with hSinf
  set C : ℝ := Real.exp ((1 / 3) * Sinf) with hC
  -- a uniform bound on the carry product
  have hQ : ∀ n, Q M n ≤ C := by
    intro n
    refine le_trans (Q_le_exp hM n) ?_
    rw [hC]
    refine Real.exp_le_exp.mpr ?_
    refine mul_le_mul_of_nonneg_left ?_ (by norm_num)
    refine Summable.sum_le_tsum _ (fun i _ => ?_) hsum
    have := orbit_pos hM i
    positivity
  -- `ρ n = M·Q n / m_n ≤ M·C / m_n → 0`
  refine squeeze_zero (fun n => le_of_lt (rho_pos M n)) (g := fun n => (M : ℝ) * C / (orbit M n : ℝ))
    (fun n => ?_) ?_
  · have hmpos : (0 : ℝ) < (orbit M n : ℝ) := by exact_mod_cast orbit_pos hM n
    rw [le_div_iff₀ hmpos, rho_mul_orbit hM n]
    refine mul_le_mul_of_nonneg_left (hQ n) ?_
    exact Nat.cast_nonneg M
  · exact Filter.Tendsto.const_div_atTop (orbit_tendsto_atTop hdiv) _

/-! ## 3. The last maximum -/

/-- **Generic.** A positive real sequence tending to `0` has a strict last maximum: some `n₀`
with `f (n₀ + k) < f n₀` for every `k ≥ 1`. No Collatz content. -/
theorem exists_last_max {f : ℕ → ℝ} (hpos : ∀ n, 0 < f n)
    (hlim : Tendsto f atTop (nhds 0)) :
    ∃ n₀, ∀ k, 1 ≤ k → f (n₀ + k) < f n₀ := by
  classical
  -- past some `N₁` the sequence drops below `f 0`
  have hev : ∀ᶠ n in atTop, f n < f 0 := hlim.eventually (gt_mem_nhds (hpos 0))
  obtain ⟨N₁, hN₁⟩ := Filter.eventually_atTop.mp hev
  have hN₁pos : 0 < N₁ := by
    by_contra hcon
    have : N₁ = 0 := by omega
    exact absurd (hN₁ 0 (by omega)) (by simp)
  set F : Finset ℕ := (Finset.range N₁).filter (fun n => f 0 ≤ f n) with hF
  have h0F : 0 ∈ F := by
    rw [hF, Finset.mem_filter]
    exact ⟨Finset.mem_range.mpr hN₁pos, le_refl _⟩
  have hFne : F.Nonempty := ⟨0, h0F⟩
  -- outside `F` the sequence is below `f 0`
  have houtside : ∀ n, n ∉ F → f n < f 0 := by
    intro n hn
    by_cases hlt : n < N₁
    · by_contra hcon
      exact hn (by rw [hF, Finset.mem_filter]; exact ⟨Finset.mem_range.mpr hlt, not_lt.mp hcon⟩)
    · exact hN₁ n (by omega)
  -- the maximum value on `F`, and the last index attaining it
  obtain ⟨b, hbF, hb⟩ := Finset.exists_mem_eq_sup' hFne f
  set G : Finset ℕ := F.filter (fun n => f n = F.sup' hFne f) with hG
  have hGne : G.Nonempty := ⟨b, by rw [hG, Finset.mem_filter]; exact ⟨hbF, hb.symm⟩⟩
  set n₀ := G.max' hGne with hn₀
  have hn₀G : n₀ ∈ G := G.max'_mem hGne
  have hn₀F : n₀ ∈ F := by
    have := hn₀G; rw [hG, Finset.mem_filter] at this; exact this.1
  have hn₀val : f n₀ = F.sup' hFne f := by
    have := hn₀G; rw [hG, Finset.mem_filter] at this; exact this.2
  have hf0 : f 0 ≤ f n₀ := by
    rw [hn₀val]; exact Finset.le_sup' f h0F
  refine ⟨n₀, fun k hk => ?_⟩
  by_cases hmem : n₀ + k ∈ F
  · have hle : f (n₀ + k) ≤ f n₀ := by
      rw [hn₀val]; exact Finset.le_sup' f hmem
    rcases lt_or_eq_of_le hle with h | h
    · exact h
    · exfalso
      have : n₀ + k ∈ G := by
        rw [hG, Finset.mem_filter]
        exact ⟨hmem, by rw [h, hn₀val]⟩
      have := G.le_max' _ this
      omega
  · exact lt_of_lt_of_le (houtside _ hmem) hf0

/-! ## 4. The restarted seed is zero-confined -/

/-- `ρ` factors across a restart, by `S_add` and `orbit_add`. -/
theorem rho_restart (M n₀ k : ℕ) : rho M (n₀ + k) = rho M n₀ * rho (orbit M n₀) k := by
  unfold rho
  rw [S_add, pow_add, pow_add]
  ring

theorem zeroConfined_of_rho_lt_one {m : ℕ} (h : ∀ k, 1 ≤ k → rho m k < 1) : ZeroConfined m := by
  intro n
  rcases Nat.eq_zero_or_pos n with rfl | hn
  · simp
  · have hlt := h n hn
    unfold rho at hlt
    rw [div_lt_one (by positivity)] at hlt
    exact_mod_cast le_of_lt hlt

/-- **Paper Prop. 4.10.** A divergent orbit produces a zero-confined positive odd seed. -/
theorem exists_zeroConfined_of_divergent {M : ℕ} (hM : Odd M) (hdiv : DivergentOrbit M) :
    ∃ m, Odd m ∧ ZeroConfined m := by
  obtain ⟨n₀, hn₀⟩ := exists_last_max (rho_pos M) (rho_tendsto_zero hM hdiv)
  refine ⟨orbit M n₀, odd_orbit hM n₀, zeroConfined_of_rho_lt_one fun k hk => ?_⟩
  have h := hn₀ k hk
  rw [rho_restart] at h
  have hp := rho_pos M n₀
  nlinarith [h, hp]

end Divergence
