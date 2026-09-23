import Occupation.CyclicLemma
import Occupation.Entropy
import Mathlib.Analysis.SpecialFunctions.Log.Deriv

/-!
# The exponential rate of confined-word mass

```
-(1/N) · log₂ (p N c)  →  I₀ = α(1 − H₂(1/α)) ≈ 0.0793186,      α = log₂3
```

The anchor total is `s_N = Nat.log 2 (3^N)`, the integral form of `⌊Nα⌋`: `2^{s_N} ≤ 3^N`, with
strictness from parity (`3^N` is odd, `2^{s_N}` even once `s_N ≥ 1`). No real floor is used.

* **Upper bound.** Confinement caps the total at `c + s_N`, and the terms
  `C(s-1,N-1)·2^{-s}` increase while `s ≤ 2N-2`, so the largest confined total dominates.
* **Lower bound.** The cycle lemma at the anchor: `#comps ≤ N · #confComps` (`card_comps_le_mul`).

Both bounds are `C(s-1,N-1)·2^{-s}` up to polynomial factors, with `s/N → α`, and the entropy
estimate of `Occupation.Entropy` converts them into `I₀`.

No `sorry`, `admit`, `axiom`, or `opaque`.
-/

namespace Occupation

open Finset Filter Topology

/-! ## 1. The constants and the anchor -/

/-- `α = log₂3`. -/
noncomputable def alpha : ℝ := Real.logb 2 3

/-- `I₀ = α(1 − H₂(1/α))`, with `H₂` the binary entropy **in bits**. -/
noncomputable def I₀ : ℝ := alpha * (1 - Real.binEntropy (1 / alpha) / Real.log 2)

theorem alpha_pos : 0 < alpha := by
  rw [alpha, Real.logb, div_pos_iff]
  left
  exact ⟨Real.log_pos (by norm_num), Real.log_pos (by norm_num)⟩

theorem one_lt_alpha : 1 < alpha := by
  rw [alpha, Real.logb, lt_div_iff₀ (Real.log_pos (by norm_num))]
  rw [one_mul]
  exact Real.log_lt_log (by norm_num) (by norm_num)

theorem alpha_lt_two : alpha < 2 := by
  rw [alpha, Real.logb, div_lt_iff₀ (Real.log_pos (by norm_num))]
  have h4 : Real.log 3 < Real.log 4 := Real.log_lt_log (by norm_num) (by norm_num)
  have : Real.log 4 = 2 * Real.log 2 := by
    rw [show (4 : ℝ) = 2 ^ 2 by norm_num, Real.log_pow]
    push_cast
    ring
  linarith

/-- The companion of `two_pow_lt_three_pow_iff`, in the non-strict direction. -/
theorem two_pow_le_three_pow_iff {S j : ℕ} :
    (2 : ℕ) ^ S ≤ 3 ^ j ↔ (S : ℝ) ≤ (j : ℝ) * Real.logb 2 3 := by
  have hlog2 : (0 : ℝ) < Real.log 2 := Real.log_pos (by norm_num)
  have hcast : ((2 : ℕ) ^ S ≤ 3 ^ j) ↔ ((2 : ℝ) ^ S ≤ (3 : ℝ) ^ j) := by
    constructor
    · intro h; exact_mod_cast h
    · intro h; exact_mod_cast h
  have hlogiff : ((2 : ℝ) ^ S ≤ (3 : ℝ) ^ j)
      ↔ (Real.log ((2 : ℝ) ^ S) ≤ Real.log ((3 : ℝ) ^ j)) :=
    (Real.log_le_log_iff (by positivity) (by positivity)).symm
  rw [hcast, hlogiff, Real.log_pow, Real.log_pow, Real.logb, ← mul_div_assoc,
    le_div_iff₀ hlog2]

/-- The anchor total `s_N`, the integral form of `⌊Nα⌋`. -/
noncomputable def sN (N : ℕ) : ℕ := Nat.log 2 (3 ^ N)

theorem two_pow_sN_le (N : ℕ) : 2 ^ sN N ≤ 3 ^ N :=
  Nat.pow_log_le_self 2 (by positivity)

theorem lt_two_pow_sN_succ (N : ℕ) : 3 ^ N < 2 ^ (sN N + 1) :=
  Nat.lt_pow_succ_log_self (by norm_num) _

/-- `N ≤ s_N`, since `2^N ≤ 3^N`. No hypothesis is needed. -/
theorem le_sN (N : ℕ) : N ≤ sN N := by
  have h : (2 : ℕ) ^ N ≤ 3 ^ N := Nat.pow_le_pow_left (by norm_num) N
  have := Nat.log_mono_right (b := 2) h
  rwa [Nat.log_pow (by norm_num)] at this

/-- **Strict**, by parity: `3^N` is odd while `2^{s_N}` is even once `s_N ≥ 1`. -/
theorem two_pow_sN_lt {N : ℕ} (hN : 1 ≤ N) : 2 ^ sN N < 3 ^ N := by
  rcases lt_or_eq_of_le (two_pow_sN_le N) with h | h
  · exact h
  · exfalso
    have hs1 : 1 ≤ sN N := le_trans hN (le_sN N)
    have heven : 2 ∣ 2 ^ sN N := dvd_pow_self 2 (by omega)
    have hodd : ¬ (2 ∣ 3 ^ N) := by
      intro hdvd
      have := Nat.Prime.dvd_of_dvd_pow Nat.prime_two hdvd
      omega
    exact hodd (h ▸ heven)

theorem sN_lt_two_mul {N : ℕ} (hN : 1 ≤ N) : sN N < 2 * N := by
  have h1 := two_pow_sN_le N
  have h2 : (3 : ℕ) ^ N < 2 ^ (2 * N) := by
    have h4 : (2 : ℕ) ^ (2 * N) = 4 ^ N := by rw [pow_mul]; norm_num
    rw [h4]
    exact Nat.pow_lt_pow_left (by norm_num) (by omega)
  have : (2 : ℕ) ^ sN N < 2 ^ (2 * N) := lt_of_le_of_lt h1 h2
  exact (Nat.pow_lt_pow_iff_right (by norm_num)).mp this

/-- `s_N ≤ Nα`. -/
theorem sN_le_mul (N : ℕ) : (sN N : ℝ) ≤ (N : ℝ) * alpha :=
  two_pow_le_three_pow_iff.mp (two_pow_sN_le N)

/-- `Nα < s_N + 1`. -/
theorem mul_lt_sN_succ (N : ℕ) : (N : ℝ) * alpha < (sN N : ℝ) + 1 := by
  have h := lt_two_pow_sN_succ N
  by_contra hcon
  rw [not_lt] at hcon
  have : (2 : ℕ) ^ (sN N + 1) ≤ 3 ^ N := by
    refine two_pow_le_three_pow_iff.mpr ?_
    push_cast
    exact hcon
  omega

/-! ## 2. Unimodality of the terms `C(s-1,N-1)·2^{-s}` -/

/-- `C(s-1, N-1) · s = C(s, N-1) · (s-N+1)`, by symmetry and `Nat.succ_mul_choose_eq`. -/
theorem choose_step {s N : ℕ} (hN : 1 ≤ N) (hs : N ≤ s) :
    (s - 1).choose (N - 1) * s = s.choose (N - 1) * (s - N + 1) := by
  have h := Nat.choose_mul_succ_eq (s - 1) (N - 1)
  have h1 : s - 1 + 1 = s := by omega
  rw [h1] at h
  have h2 : s - (N - 1) = s - N + 1 := by omega
  rw [h2] at h
  exact h

/-- The terms increase while `s + 2 ≤ 2N`. -/
theorem two_mul_choose_le {s N : ℕ} (hN : 1 ≤ N) (hs : N ≤ s) (hub : s + 2 ≤ 2 * N) :
    2 * ((s - 1).choose (N - 1)) ≤ s.choose (N - 1) := by
  have hstep := choose_step hN hs
  have hpos : 0 < s - N + 1 := by omega
  refine Nat.le_of_mul_le_mul_right ?_ hpos
  calc 2 * ((s - 1).choose (N - 1)) * (s - N + 1)
      = (s - 1).choose (N - 1) * (2 * (s - N + 1)) := by ring
    _ ≤ (s - 1).choose (N - 1) * s := by
        refine Nat.mul_le_mul_left _ ?_
        omega
    _ = s.choose (N - 1) * (s - N + 1) := hstep

/-- The term `C(s-1,N-1)·2^{-s}`. -/
noncomputable def tt (N s : ℕ) : ℝ := ((s - 1).choose (N - 1) : ℝ) * (2 : ℝ)⁻¹ ^ s

theorem tt_nonneg (N s : ℕ) : 0 ≤ tt N s := by
  unfold tt; positivity

theorem tt_le_succ {s N : ℕ} (hN : 1 ≤ N) (hs : N ≤ s) (hub : s + 2 ≤ 2 * N) :
    tt N s ≤ tt N (s + 1) := by
  have hnat := two_mul_choose_le hN hs hub
  have hcast : (2 : ℝ) * ((s - 1).choose (N - 1) : ℝ) ≤ (s.choose (N - 1) : ℝ) := by
    exact_mod_cast hnat
  unfold tt
  have hsimp : ((s + 1 - 1) : ℕ) = s := by omega
  rw [hsimp, pow_succ]
  have hp : (0 : ℝ) < (2 : ℝ)⁻¹ ^ s := by positivity
  nlinarith [hcast, hp]

/-- Every term with `N ≤ s ≤ M` is at most the top term, provided `M + 2 ≤ 2N`. -/
theorem tt_le_top {N : ℕ} (hN : 1 ≤ N) :
    ∀ M, M + 2 ≤ 2 * N → ∀ s, N ≤ s → s ≤ M → tt N s ≤ tt N M := by
  intro M
  induction M with
  | zero => intro _ s hs hsM; omega
  | succ M ih =>
    intro hM s hs hsM
    rcases Nat.lt_or_ge s (M + 1) with hlt | hge
    · have h1 : tt N s ≤ tt N M := ih (by omega) s hs (by omega)
      have h2 : tt N M ≤ tt N (M + 1) := tt_le_succ hN (by omega) (by omega)
      exact le_trans h1 h2
    · have hseq : s = M + 1 := by omega
      rw [hseq]

/-! ## 3. The two bounds on the mass -/

/-- Confinement caps the total at `c + s_N`. -/
theorem confComps_eq_empty_of_gt {N c s : ℕ} (h : c + sN N < s) :
    confComps N c s = ∅ := by
  rw [Finset.eq_empty_iff_forall_notMem]
  intro d hd
  rw [mem_confComps] at hd
  obtain ⟨⟨hsum, _⟩, hconf⟩ := hd
  have hcap := hconf N (le_refl N)
  rw [psum_total, hsum] at hcap
  have hlt : (2 : ℕ) ^ s < 2 ^ (c + sN N + 1) := by
    calc (2 : ℕ) ^ s ≤ 2 ^ c * 3 ^ N := hcap
      _ < 2 ^ c * 2 ^ (sN N + 1) :=
          mul_lt_mul_of_pos_left (lt_two_pow_sN_succ N) (pow_pos (by norm_num) c)
      _ = 2 ^ (c + sN N + 1) := by rw [← pow_add, Nat.add_assoc]
  have := (Nat.pow_lt_pow_iff_right (by norm_num : 1 < 2)).mp hlt
  omega

theorem confComps_eq_empty_of_lt {N s : ℕ} (c : ℕ) (h : s < N) : confComps N c s = ∅ := by
  rw [Finset.eq_empty_iff_forall_notMem]
  intro d hd
  rw [mem_confComps] at hd
  have := le_of_mem_comps (mem_comps.mpr hd.1)
  omega

/-- Each confined block is at most the corresponding binomial term. -/
theorem confComps_term_le {N c s : ℕ} (hN : 1 ≤ N) (hs : N ≤ s) :
    ((confComps N c s).card : ℝ) * (2 : ℝ)⁻¹ ^ s ≤ tt N s := by
  have hsub : confComps N c s ⊆ comps N s := Finset.filter_subset _ _
  have hcard : (confComps N c s).card ≤ (s - 1).choose (N - 1) := by
    calc (confComps N c s).card ≤ (comps N s).card := Finset.card_le_card hsub
      _ = (s - 1).choose (N - 1) := card_comps hN hs
  unfold tt
  have : ((confComps N c s).card : ℝ) ≤ (((s - 1).choose (N - 1) : ℕ) : ℝ) := by
    exact_mod_cast hcard
  have hp : (0 : ℝ) < (2 : ℝ)⁻¹ ^ s := by positivity
  nlinarith [this, hp]

/-- **Upper bound.** -/
theorem p_le {N c : ℕ} (hN : 1 ≤ N) (hbig : c + sN N + 2 ≤ 2 * N) :
    p N c ≤ ((c : ℝ) + sN N + 1) * tt N (c + sN N) := by
  rw [p_eq_sum]
  have hterm : ∀ s ∈ range (2 * N + c),
      ((confComps N c s).card : ℝ) * (2 : ℝ)⁻¹ ^ s
        ≤ if s ∈ Finset.Icc N (c + sN N) then tt N (c + sN N) else 0 := by
    intro s _
    split_ifs with hmem
    · rw [Finset.mem_Icc] at hmem
      exact le_trans (confComps_term_le hN hmem.1)
        (tt_le_top hN (c + sN N) hbig s hmem.1 hmem.2)
    · rw [Finset.mem_Icc, not_and_or, not_le, not_le] at hmem
      rcases hmem with hlt | hgt
      · rw [confComps_eq_empty_of_lt c hlt]
        simp
      · rw [confComps_eq_empty_of_gt hgt]
        simp
  calc ∑ s ∈ range (2 * N + c), ((confComps N c s).card : ℝ) * (2 : ℝ)⁻¹ ^ s
      ≤ ∑ s ∈ range (2 * N + c),
          (if s ∈ Finset.Icc N (c + sN N) then tt N (c + sN N) else 0) :=
        Finset.sum_le_sum hterm
    _ ≤ ((c : ℝ) + sN N + 1) * tt N (c + sN N) := by
        rw [Finset.sum_ite_mem]
        have hcard : ((range (2 * N + c) ∩ Finset.Icc N (c + sN N)).card : ℝ)
            ≤ (c : ℝ) + sN N + 1 := by
          have h1 : (range (2 * N + c) ∩ Finset.Icc N (c + sN N)).card
              ≤ (Finset.Icc N (c + sN N)).card := Finset.card_le_card Finset.inter_subset_right
          have h2 : (Finset.Icc N (c + sN N)).card = c + sN N + 1 - N := by
            rw [Nat.card_Icc]
          have : (range (2 * N + c) ∩ Finset.Icc N (c + sN N)).card ≤ c + sN N + 1 := by
            omega
          exact_mod_cast this
        rw [Finset.sum_const, nsmul_eq_mul]
        exact mul_le_mul_of_nonneg_right hcard (tt_nonneg _ _)

/-- **Lower bound**, from the cycle lemma at the anchor. -/
theorem le_p {N c : ℕ} (hN : 1 ≤ N) : tt N (sN N) / N ≤ p N c := by
  have hpos : 0 < N := hN
  have hlt := two_pow_sN_lt hN
  have hcount := card_comps_le_mul (N := N) (s := sN N) hpos hlt
  have hmono : confComps N 0 (sN N) ⊆ confComps N c (sN N) := by
    intro d hd
    rw [mem_confComps] at hd ⊢
    exact ⟨hd.1, hd.2.mono (Nat.zero_le c)⟩
  have hcard : (comps N (sN N)).card ≤ N * (confComps N c (sN N)).card :=
    le_trans hcount (Nat.mul_le_mul_left _ (Finset.card_le_card hmono))
  have hcomps : (comps N (sN N)).card = (sN N - 1).choose (N - 1) :=
    card_comps hN (le_sN N)
  -- a single block is at most the whole mass
  have hmem : sN N ∈ range (2 * N + c) := Finset.mem_range.mpr (by
    have := sN_lt_two_mul hN; omega)
  have hsingle : ((confComps N c (sN N)).card : ℝ) * (2 : ℝ)⁻¹ ^ (sN N) ≤ p N c := by
    rw [p_eq_sum]
    refine Finset.single_le_sum (f := fun s => ((confComps N c s).card : ℝ) * (2 : ℝ)⁻¹ ^ s)
      (fun s _ => by positivity) hmem
  -- and the block is at least `C(s_N-1,N-1)/N`
  have hNR : (0 : ℝ) < (N : ℝ) := by exact_mod_cast hpos
  have hcardR : (((sN N - 1).choose (N - 1) : ℕ) : ℝ)
      ≤ (N : ℝ) * ((confComps N c (sN N)).card : ℝ) := by
    have := hcomps ▸ hcard
    exact_mod_cast this
  rw [div_le_iff₀ hNR]
  unfold tt
  have hp : (0 : ℝ) < (2 : ℝ)⁻¹ ^ (sN N) := by positivity
  nlinarith [hsingle, hcardR, hp]

/-! ## 4. The rate along an anchor sequence -/

private theorem tendsto_log_div_nat :
    Tendsto (fun N : ℕ => Real.log (N : ℝ) / (N : ℝ)) atTop (𝓝 0) := by
  have h : Tendsto (fun x : ℝ => Real.log x / x) atTop (𝓝 0) :=
    Real.isLittleO_log_id_atTop.tendsto_div_nhds_zero
  exact h.comp tendsto_natCast_atTop_atTop

private theorem tendsto_logb_div_nat :
    Tendsto (fun N : ℕ => Real.logb 2 (N : ℝ) / (N : ℝ)) atTop (𝓝 0) := by
  have h := tendsto_log_div_nat.div_const (Real.log 2)
  rw [zero_div] at h
  refine h.congr fun N => ?_
  rw [Real.logb, div_div, div_div, mul_comm]

/-- A polynomially bounded prefactor contributes nothing to the rate. -/
private theorem tendsto_logb_poly_div {A : ℝ} (hA : 1 ≤ A) {g : ℕ → ℝ}
    (hg1 : ∀ᶠ N : ℕ in atTop, 1 ≤ g N)
    (hg2 : ∀ᶠ N : ℕ in atTop, g N ≤ A * N) :
    Tendsto (fun N : ℕ => Real.logb 2 (g N) / N) atTop (𝓝 0) := by
  have hlim : Tendsto (fun N : ℕ => (Real.logb 2 A + Real.logb 2 (N : ℝ)) / N) atTop (𝓝 0) := by
    have h1 : Tendsto (fun N : ℕ => Real.logb 2 A / N) atTop (𝓝 0) :=
      tendsto_const_div_atTop_nhds_zero_nat _
    have h2 := h1.add tendsto_logb_div_nat
    rw [add_zero] at h2
    refine h2.congr fun N => ?_
    rw [← add_div]
  refine squeeze_zero' ?_ ?_ hlim
  · filter_upwards [hg1, eventually_gt_atTop 0] with N h1 hN
    have hNR : (0 : ℝ) < N := by exact_mod_cast hN
    have : 0 ≤ Real.logb 2 (g N) := Real.logb_nonneg (by norm_num) h1
    positivity
  · filter_upwards [hg1, hg2, eventually_gt_atTop 0] with N h1 h2 hN
    have hNR : (0 : ℝ) < N := by exact_mod_cast hN
    have hAN : Real.logb 2 (g N) ≤ Real.logb 2 A + Real.logb 2 (N : ℝ) := by
      calc Real.logb 2 (g N) ≤ Real.logb 2 (A * N) :=
            Real.logb_le_logb_of_le (by norm_num) (by linarith) h2
        _ = Real.logb 2 A + Real.logb 2 (N : ℝ) :=
            Real.logb_mul (by linarith) (ne_of_gt hNR)
    exact div_le_div_of_nonneg_right hAN hNR.le

private theorem logb_tt {N s : ℕ} (hC : 0 < ((s - 1).choose (N - 1) : ℝ)) :
    Real.logb 2 (tt N s) = Real.log ((s - 1).choose (N - 1)) / Real.log 2 - s := by
  have hlog2 : Real.log 2 ≠ 0 := ne_of_gt (Real.log_pos (by norm_num))
  unfold tt Real.logb
  rw [Real.log_mul (ne_of_gt hC) (by positivity), Real.log_pow, Real.log_inv]
  field_simp
  ring

/-- **The rate along an anchor sequence** with `f N / N → α`. -/
theorem rate_core {f : ℕ → ℕ}
    (hfge : ∀ᶠ N : ℕ in atTop, N ≤ f N)
    (hfub : ∀ᶠ N : ℕ in atTop, f N ≤ 3 * N)
    (hfdiv : Tendsto (fun N : ℕ => (f N : ℝ) / N) atTop (𝓝 alpha)) :
    Tendsto (fun N : ℕ => -(1 / (N : ℝ)) * Real.logb 2 (tt N (f N))) atTop (𝓝 I₀) := by
  have hlog2 : (0 : ℝ) < Real.log 2 := Real.log_pos (by norm_num)
  have hinv : Tendsto (fun N : ℕ => (1 : ℝ) / N) atTop (𝓝 0) :=
    tendsto_one_div_atTop_nhds_zero_nat
  set G : ℕ → ℝ := fun N =>
    (f N : ℝ) / N
      - ((f N : ℝ) - 1) / N * Real.binEntropy (((N : ℝ) - 1) / ((f N : ℝ) - 1)) / Real.log 2
    with hGdef
  -- `G → I₀`
  have hnum : Tendsto (fun N : ℕ => ((N : ℝ) - 1) / N) atTop (𝓝 1) := by
    have hbase : Tendsto (fun N : ℕ => 1 - (1 : ℝ) / N) atTop (𝓝 1) := by
      have := tendsto_const_nhds (x := (1 : ℝ)) (f := (atTop : Filter ℕ)) |>.sub hinv
      rwa [sub_zero] at this
    refine hbase.congr' ?_
    filter_upwards [eventually_gt_atTop 0] with N hN
    have hNR : (N : ℝ) ≠ 0 := by
      have : (0 : ℝ) < N := by exact_mod_cast hN
      positivity
    field_simp
  have hden : Tendsto (fun N : ℕ => ((f N : ℝ) - 1) / N) atTop (𝓝 alpha) := by
    have hbase := hfdiv.sub hinv
    rw [sub_zero] at hbase
    refine hbase.congr fun N => ?_
    rw [sub_div]
  have hratio : Tendsto (fun N : ℕ => ((N : ℝ) - 1) / ((f N : ℝ) - 1)) atTop (𝓝 (1 / alpha)) := by
    have hq : Tendsto (fun N : ℕ => (((N : ℝ) - 1) / N) / (((f N : ℝ) - 1) / N)) atTop
        (𝓝 (1 / alpha)) := hnum.div hden (ne_of_gt alpha_pos)
    refine hq.congr' ?_
    filter_upwards [eventually_ge_atTop 2, hfge] with N hN hfN
    have hNR : (N : ℝ) ≠ 0 := by
      have : (0 : ℝ) < N := by exact_mod_cast (by omega : 0 < N)
      positivity
    have hfR : (f N : ℝ) - 1 ≠ 0 := by
      have h2 : (2 : ℝ) ≤ (f N : ℝ) := by exact_mod_cast (by omega : 2 ≤ f N)
      intro hcon
      linarith
    field_simp
  have hbe : Tendsto (fun N : ℕ => Real.binEntropy (((N : ℝ) - 1) / ((f N : ℝ) - 1)))
      atTop (𝓝 (Real.binEntropy (1 / alpha))) :=
    (Real.binEntropy_continuous.tendsto _).comp hratio
  have hGlim : Tendsto G atTop (𝓝 I₀) := by
    have hcomb := hfdiv.sub ((hden.mul hbe).div_const (Real.log 2))
    have hval : alpha - alpha * Real.binEntropy (1 / alpha) / Real.log 2 = I₀ := by
      rw [I₀]; ring
    rw [hval] at hcomb
    exact hcomb
  -- the error against `G` vanishes
  have hbound : Tendsto (fun N : ℕ => (Real.log 3 + Real.log (N : ℝ)) / ((N : ℝ) * Real.log 2))
      atTop (𝓝 0) := by
    have h1 : Tendsto (fun N : ℕ => Real.log 3 / (N : ℝ)) atTop (𝓝 0) :=
      tendsto_const_div_atTop_nhds_zero_nat _
    have h3 := (h1.add tendsto_log_div_nat).div_const (Real.log 2)
    rw [add_zero, zero_div] at h3
    refine h3.congr fun N => ?_
    rw [← add_div, div_div]
  have hkey : ∀ᶠ N : ℕ in atTop,
      |(-(1 / (N : ℝ)) * Real.logb 2 (tt N (f N))) - G N|
        ≤ (Real.log 3 + Real.log (N : ℝ)) / ((N : ℝ) * Real.log 2) := by
    filter_upwards [eventually_ge_atTop 2, hfge, hfub] with N hN2 hfN hfN3
    have hNpos : 0 < N := by omega
    have hNR : (0 : ℝ) < N := by exact_mod_cast hNpos
    have hfpos : 0 < f N := by omega
    have hk : N - 1 ≤ f N - 1 := by omega
    have hn : 0 < f N - 1 := by omega
    have hC : (0 : ℝ) < ((f N - 1).choose (N - 1) : ℝ) := by
      exact_mod_cast Nat.choose_pos hk
    have hcn : ((f N - 1 : ℕ) : ℝ) = (f N : ℝ) - 1 := by
      rw [Nat.cast_sub (by omega)]; norm_num
    have hck : ((N - 1 : ℕ) : ℝ) = (N : ℝ) - 1 := by
      rw [Nat.cast_sub (by omega)]; norm_num
    have habs := abs_log_choose_sub_le hk hn
    rw [hcn, hck] at habs
    have hfin : ((f N : ℝ) - 1) + 1 = (f N : ℝ) := by ring
    rw [hfin] at habs
    have hD : (-(1 / (N : ℝ)) * Real.logb 2 (tt N (f N))) - G N
        = (1 / ((N : ℝ) * Real.log 2))
          * ((((f N : ℝ) - 1) * Real.binEntropy (((N : ℝ) - 1) / ((f N : ℝ) - 1)))
             - Real.log ((f N - 1).choose (N - 1))) := by
      rw [logb_tt hC, hGdef]
      field_simp
      ring
    rw [hD, abs_mul, abs_of_pos (show (0:ℝ) < 1 / ((N : ℝ) * Real.log 2) by positivity)]
    have habs2 : |(((f N : ℝ) - 1) * Real.binEntropy (((N : ℝ) - 1) / ((f N : ℝ) - 1)))
        - Real.log ((f N - 1).choose (N - 1))| ≤ Real.log (f N : ℝ) := by
      rw [abs_sub_comm]
      exact habs
    have hlogle : Real.log (f N : ℝ) ≤ Real.log 3 + Real.log (N : ℝ) := by
      have h3N : ((f N : ℕ) : ℝ) ≤ 3 * (N : ℝ) := by exact_mod_cast hfN3
      calc Real.log (f N : ℝ) ≤ Real.log (3 * (N : ℝ)) :=
            Real.log_le_log (by exact_mod_cast hfpos) h3N
        _ = Real.log 3 + Real.log (N : ℝ) := Real.log_mul (by norm_num) (ne_of_gt hNR)
    calc 1 / ((N : ℝ) * Real.log 2) * |(((f N : ℝ) - 1)
            * Real.binEntropy (((N : ℝ) - 1) / ((f N : ℝ) - 1)))
            - Real.log ((f N - 1).choose (N - 1))|
        ≤ 1 / ((N : ℝ) * Real.log 2) * (Real.log 3 + Real.log (N : ℝ)) :=
          mul_le_mul_of_nonneg_left (le_trans habs2 hlogle) (by positivity)
      _ = (Real.log 3 + Real.log (N : ℝ)) / ((N : ℝ) * Real.log 2) := by ring
  have hdiff : Tendsto (fun N : ℕ => (-(1 / (N : ℝ)) * Real.logb 2 (tt N (f N))) - G N)
      atTop (𝓝 0) := by
    have hneg := hbound.neg
    rw [neg_zero] at hneg
    refine tendsto_of_tendsto_of_tendsto_of_le_of_le' hneg hbound ?_ ?_
    · filter_upwards [hkey] with N h
      exact neg_le_of_abs_le h
    · filter_upwards [hkey] with N h
      exact le_of_abs_le h
  have hsplit : (fun N : ℕ => -(1 / (N : ℝ)) * Real.logb 2 (tt N (f N)))
      = fun N : ℕ => G N + ((-(1 / (N : ℝ)) * Real.logb 2 (tt N (f N))) - G N) := by
    funext N; ring
  rw [hsplit]
  have := hGlim.add hdiff
  rwa [add_zero] at this

/-! ## 5. The theorem -/

theorem sN_div_tendsto : Tendsto (fun N : ℕ => (sN N : ℝ) / N) atTop (𝓝 alpha) := by
  refine tendsto_of_tendsto_of_tendsto_of_le_of_le'
    (g := fun N : ℕ => alpha - 1 / (N : ℝ)) (h := fun _ : ℕ => alpha) ?_ tendsto_const_nhds ?_ ?_
  · have := tendsto_const_nhds (x := alpha) (f := (atTop : Filter ℕ)) |>.sub
      tendsto_one_div_atTop_nhds_zero_nat
    rwa [sub_zero] at this
  · filter_upwards [eventually_gt_atTop 0] with N hN
    have hNR : (0 : ℝ) < N := by exact_mod_cast hN
    have h := mul_lt_sN_succ N
    rw [sub_le_iff_le_add, ← add_div, le_div_iff₀ hNR]
    linarith
  · filter_upwards [eventually_gt_atTop 0] with N hN
    have hNR : (0 : ℝ) < N := by exact_mod_cast hN
    rw [div_le_iff₀ hNR]
    have := sN_le_mul N
    linarith

theorem tt_pos {N s : ℕ} (hN : 1 ≤ N) (hs : N ≤ s) : 0 < tt N s := by
  have hC : (0 : ℝ) < ((s - 1).choose (N - 1) : ℝ) := by
    exact_mod_cast Nat.choose_pos (by omega : N - 1 ≤ s - 1)
  unfold tt
  positivity

/-- **The exponential rate of confined-word mass.** -/
theorem confined_mass_rate (c : ℕ) :
    Tendsto (fun N : ℕ => -(1 / (N : ℝ)) * Real.logb 2 (p N c)) atTop (𝓝 I₀) := by
  have hlog2 : (0 : ℝ) < Real.log 2 := Real.log_pos (by norm_num)
  -- anchors
  have hsNub : ∀ᶠ N : ℕ in atTop, sN N ≤ 3 * N := by
    filter_upwards [eventually_ge_atTop 1] with N hN
    have := sN_lt_two_mul hN; omega
  have hV0 : Tendsto (fun N : ℕ => -(1 / (N : ℝ)) * Real.logb 2 (tt N (sN N))) atTop (𝓝 I₀) :=
    rate_core (Eventually.of_forall le_sN) hsNub sN_div_tendsto
  have hdiv2 : Tendsto (fun N : ℕ => ((c + sN N : ℕ) : ℝ) / N) atTop (𝓝 alpha) := by
    have h1 : Tendsto (fun N : ℕ => (c : ℝ) / N) atTop (𝓝 0) :=
      tendsto_const_div_atTop_nhds_zero_nat _
    have h2 := h1.add sN_div_tendsto
    rw [zero_add] at h2
    refine h2.congr fun N => ?_
    push_cast
    rw [add_div]
  have hcub : ∀ᶠ N : ℕ in atTop, c + sN N ≤ 3 * N := by
    filter_upwards [eventually_ge_atTop 1, eventually_ge_atTop c] with N hN hcN
    have := sN_lt_two_mul hN; omega
  have hU0 : Tendsto (fun N : ℕ => -(1 / (N : ℝ)) * Real.logb 2 (tt N (c + sN N)))
      atTop (𝓝 I₀) := by
    refine rate_core ?_ hcub hdiv2
    filter_upwards with N
    have := le_sN N; omega
  -- prefactors vanish
  have hpre1 : Tendsto (fun N : ℕ => Real.logb 2 ((c : ℝ) + sN N + 1) / N) atTop (𝓝 0) := by
    refine tendsto_logb_poly_div (A := (c : ℝ) + 3) (by linarith [Nat.cast_nonneg (α := ℝ) c]) ?_ ?_
    · filter_upwards with N
      have : (0 : ℝ) ≤ (sN N : ℝ) := Nat.cast_nonneg _
      have : (0 : ℝ) ≤ (c : ℝ) := Nat.cast_nonneg _
      linarith
    · filter_upwards [eventually_ge_atTop 1] with N hN
      have hNR : (1 : ℝ) ≤ (N : ℝ) := by exact_mod_cast hN
      have hsN : (sN N : ℝ) ≤ 2 * N := by
        have := sN_lt_two_mul hN
        exact_mod_cast le_of_lt (by exact_mod_cast this : (sN N : ℝ) < 2 * (N : ℝ))
      have hc : (0 : ℝ) ≤ (c : ℝ) := Nat.cast_nonneg _
      nlinarith
  have hpre2 : Tendsto (fun N : ℕ => Real.logb 2 (N : ℝ) / N) atTop (𝓝 0) := tendsto_logb_div_nat
  -- the two bounding sequences
  have hU : Tendsto (fun N : ℕ =>
      -(1 / (N : ℝ)) * Real.logb 2 (((c : ℝ) + sN N + 1) * tt N (c + sN N))) atTop (𝓝 I₀) := by
    have hsum := (hpre1.neg).add hU0
    rw [neg_zero, zero_add] at hsum
    refine hsum.congr' ?_
    filter_upwards [eventually_ge_atTop 1] with N hN
    have hNR : (0 : ℝ) < N := by exact_mod_cast (by omega : 0 < N)
    have hp : (0 : ℝ) < (c : ℝ) + sN N + 1 := by
      have : (0 : ℝ) ≤ (sN N : ℝ) := Nat.cast_nonneg _
      have : (0 : ℝ) ≤ (c : ℝ) := Nat.cast_nonneg _
      linarith
    have ht : (0 : ℝ) < tt N (c + sN N) := tt_pos hN (by have := le_sN N; omega)
    rw [Real.logb_mul (ne_of_gt hp) (ne_of_gt ht)]
    field_simp
    ring
  have hV : Tendsto (fun N : ℕ =>
      -(1 / (N : ℝ)) * Real.logb 2 (tt N (sN N) / N)) atTop (𝓝 I₀) := by
    have hsum := hV0.add hpre2
    rw [add_zero] at hsum
    refine hsum.congr' ?_
    filter_upwards [eventually_ge_atTop 1] with N hN
    have hNR : (0 : ℝ) < N := by exact_mod_cast (by omega : 0 < N)
    have ht : (0 : ℝ) < tt N (sN N) := tt_pos hN (le_sN N)
    rw [Real.logb_div (ne_of_gt ht) (ne_of_gt hNR)]
    field_simp
    ring
  -- squeeze
  have hbig : ∀ᶠ N : ℕ in atTop, c + sN N + 2 ≤ 2 * N := by
    have hgap : (0 : ℝ) < 2 - alpha := by linarith [alpha_lt_two]
    have htend : Tendsto (fun N : ℕ => (N : ℝ) * (2 - alpha)) atTop atTop :=
      Filter.Tendsto.atTop_mul_const hgap tendsto_natCast_atTop_atTop
    filter_upwards [htend.eventually_ge_atTop ((c : ℝ) + 2)] with N hN
    have h1 := sN_le_mul N
    have hcast : ((c + sN N + 2 : ℕ) : ℝ) ≤ ((2 * N : ℕ) : ℝ) := by
      push_cast
      nlinarith
    exact_mod_cast hcast
  refine tendsto_of_tendsto_of_tendsto_of_le_of_le' hU hV ?_ ?_
  · filter_upwards [eventually_ge_atTop 1, hbig] with N hN hb
    have hNR : (0 : ℝ) < N := by exact_mod_cast (by omega : 0 < N)
    have hple := p_le hN hb
    have hppos := p_pos (N := N) (c := c) hN
    have hlb : Real.logb 2 (p N c) ≤ Real.logb 2 (((c : ℝ) + sN N + 1) * tt N (c + sN N)) :=
      Real.logb_le_logb_of_le (by norm_num) hppos hple
    have h1N : (0 : ℝ) < 1 / (N : ℝ) := by positivity
    nlinarith [hlb, h1N]
  · filter_upwards [eventually_ge_atTop 1] with N hN
    have hNR : (0 : ℝ) < N := by exact_mod_cast (by omega : 0 < N)
    have hlep := le_p (N := N) (c := c) hN
    have htp : (0 : ℝ) < tt N (sN N) / N := div_pos (tt_pos hN (le_sN N)) hNR
    have hlb : Real.logb 2 (tt N (sN N) / N) ≤ Real.logb 2 (p N c) :=
      Real.logb_le_logb_of_le (by norm_num) htp hlep
    have h1N : (0 : ℝ) < 1 / (N : ℝ) := by positivity
    nlinarith [hlb, h1N]

end Occupation
