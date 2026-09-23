import Divergence.RawMap
import Mathlib.Analysis.SpecialFunctions.Pow.Real

/-!
# The binomial tail bound, with exact integer certificates

M4's window count splits into a **heavy** case, counted by the upper binomial tail
`tail N k = Σ_{j≥k} C(N,j)`, and a **light** case, bounded by `3^m`. Both must come out below
`2^N` by a *fixed geometric margin*, or M5's dyadic sum diverges.

The saving is certified here by two exact comparisons of integer literals:

* `50^50 < 2^50 · 31^31 · 19^19` — equivalently `H(31/50) < 1`;
* `3^31 < 2^50` — equivalently `(31/50)·log₂3 < 1`.

No logarithm is ever evaluated, and no floating-point number appears. The single real-valued
export `exists_window_base` converts them into one base `θ < 2` serving **both** branches, so M5
has a single ratio `θ/2` to sum. The `rpow` step happens there and nowhere else.

With `γ = 31/50` the two bases are `≈ 1.9427` and `3^(31/50) ≈ 1.9762`, so `θ ≈ 1.9762 < 2`.

No `sorry`, `admit`, `axiom`, or `opaque`.
-/

namespace Divergence

open Finset

/-! ## 1. The upper binomial tail -/

/-- `tail N k = Σ_{j=k}^{N} C(N,j)`. -/
def tail (N k : ℕ) : ℕ := ∑ j ∈ Finset.Icc k N, N.choose j

theorem tail_eq_zero_of_lt {N k : ℕ} (h : N < k) : tail N k = 0 := by
  unfold tail
  rw [Finset.Icc_eq_empty (by omega), Finset.sum_empty]

/-- For `b ≤ a` the binomial weight is monotone along the tail. -/
private theorem weight_mono {a b N k j : ℕ} (hab : b ≤ a) (hkj : k ≤ j) (hjN : j ≤ N) :
    a ^ k * b ^ (N - k) ≤ a ^ j * b ^ (N - j) := by
  obtain ⟨t, rfl⟩ : ∃ t, j = k + t := ⟨j - k, by omega⟩
  have h1 : N - k = (N - (k + t)) + t := by omega
  rw [h1, pow_add, pow_add]
  calc a ^ k * (b ^ (N - (k + t)) * b ^ t)
      = a ^ k * b ^ (N - (k + t)) * b ^ t := by ring
    _ ≤ a ^ k * b ^ (N - (k + t)) * a ^ t := Nat.mul_le_mul_left _ (Nat.pow_le_pow_left hab t)
    _ = a ^ k * a ^ t * b ^ (N - (k + t)) := by ring

/-- **The sum-to-one argument.** Every tail term carries weight at least `a^k b^{N-k}`, and the
whole weighted sum is `(a+b)^N`. -/
theorem tail_mul_le {a b N k : ℕ} (hab : b ≤ a) :
    tail N k * (a ^ k * b ^ (N - k)) ≤ (a + b) ^ N := by
  have hexp : (a + b) ^ N = ∑ j ∈ range (N + 1), a ^ j * b ^ (N - j) * N.choose j := by
    rw [add_pow]
    simp
  have hsub : Finset.Icc k N ⊆ range (N + 1) := by
    intro j hj
    rw [Finset.mem_Icc] at hj
    exact Finset.mem_range.mpr (by omega)
  calc tail N k * (a ^ k * b ^ (N - k))
      = ∑ j ∈ Finset.Icc k N, a ^ k * b ^ (N - k) * N.choose j := by
        rw [tail, Finset.sum_mul]
        exact Finset.sum_congr rfl fun j _ => by ring
    _ ≤ ∑ j ∈ Finset.Icc k N, a ^ j * b ^ (N - j) * N.choose j := by
        refine Finset.sum_le_sum fun j hj => ?_
        rw [Finset.mem_Icc] at hj
        exact Nat.mul_le_mul_right _ (weight_mono hab hj.1 hj.2)
    _ ≤ ∑ j ∈ range (N + 1), a ^ j * b ^ (N - j) * N.choose j :=
        Finset.sum_le_sum_of_subset hsub
    _ = (a + b) ^ N := hexp.symm

/-! ## 2. The tail counts subsets by cardinality -/

/-- **The form M4's heavy case consumes**, alongside `modEq_of_parityPrefix_eq`. -/
theorem card_subsets_card_ge (N k : ℕ) :
    ((range N).powerset.filter (fun T => k ≤ T.card)).card = tail N k := by
  have hfib : ∀ T ∈ (range N).powerset.filter (fun T => k ≤ T.card), T.card ∈ Finset.Icc k N := by
    intro T hT
    rw [Finset.mem_filter, Finset.mem_powerset] at hT
    rw [Finset.mem_Icc]
    refine ⟨hT.2, ?_⟩
    calc T.card ≤ (range N).card := Finset.card_le_card hT.1
      _ = N := Finset.card_range N
  rw [Finset.card_eq_sum_card_fiberwise hfib]
  refine Finset.sum_congr rfl fun j hj => ?_
  rw [Finset.mem_Icc] at hj
  have hset : ((range N).powerset.filter (fun T => k ≤ T.card)).filter (fun T => T.card = j)
      = Finset.powersetCard j (range N) := by
    ext T
    simp only [Finset.mem_filter, Finset.mem_powerset, Finset.mem_powersetCard]
    constructor
    · rintro ⟨⟨hsub, _⟩, hcard⟩
      exact ⟨hsub, hcard⟩
    · rintro ⟨hsub, hcard⟩
      exact ⟨⟨hsub, by omega⟩, hcard⟩
  rw [hset, Finset.card_powersetCard, Finset.card_range]

/-! ## 3. The two integer certificates -/

/-- `H(31/50) < 1`, as an exact comparison of integer literals. -/
theorem entropy_certificate : (50 : ℕ) ^ 50 < 2 ^ 50 * (31 ^ 31 * 19 ^ 19) := by norm_num

/-- `(31/50)·log₂3 < 1`, as an exact comparison of integer literals. -/
theorem light_certificate : (3 : ℕ) ^ 31 < 2 ^ 50 := by norm_num

private theorem heavy_base_ge_one : (31 : ℕ) ^ 31 * 19 ^ 19 ≤ 50 ^ 50 := by norm_num

/-! ## 4. The heavy and light estimates, in `ℕ` -/

/-- **Heavy side.** No `k ≤ N` is needed: for `k > N` the tail is empty. -/
theorem heavy_tail_pow {N k : ℕ} (h : 31 * N ≤ 50 * k) :
    tail N k ^ 50 * (31 ^ 31 * 19 ^ 19) ^ N ≤ (50 ^ 50) ^ N := by
  rcases Nat.lt_or_ge N k with hlt | hk
  · rw [tail_eq_zero_of_lt hlt]
    simp
  -- the weighted bound, raised to the 50th power
  have hbase := tail_mul_le (a := 31) (b := 19) (N := N) (k := k) (by norm_num)
  have hpow : (tail N k * (31 ^ k * 19 ^ (N - k))) ^ 50 ≤ ((31 + 19) ^ N) ^ 50 :=
    Nat.pow_le_pow_left hbase 50
  -- `(31^31·19^19)^N ≤ (31^k·19^{N-k})^50`, since `50k ≥ 31N`
  have hweight : (31 ^ 31 * 19 ^ 19 : ℕ) ^ N ≤ (31 ^ k * 19 ^ (N - k)) ^ 50 := by
    have hu : 50 * k = 31 * N + (50 * k - 31 * N) := by omega
    have hv : 19 * N = 50 * (N - k) + (50 * k - 31 * N) := by omega
    have hexpand : (31 ^ k * 19 ^ (N - k) : ℕ) ^ 50 = 31 ^ (50 * k) * 19 ^ (50 * (N - k)) := by
      rw [mul_pow, ← pow_mul, ← pow_mul, Nat.mul_comm k 50, Nat.mul_comm (N - k) 50]
    have hexpand' : (31 ^ 31 * 19 ^ 19 : ℕ) ^ N = 31 ^ (31 * N) * 19 ^ (19 * N) := by
      rw [mul_pow, ← pow_mul, ← pow_mul, Nat.mul_comm 31 N, Nat.mul_comm 19 N]
    rw [hexpand, hexpand']
    conv_lhs => rw [hv]
    conv_rhs => rw [hu]
    rw [pow_add, pow_add]
    calc 31 ^ (31 * N) * (19 ^ (50 * (N - k)) * 19 ^ (50 * k - 31 * N))
        = 31 ^ (31 * N) * 19 ^ (50 * (N - k)) * 19 ^ (50 * k - 31 * N) := by ring
      _ ≤ 31 ^ (31 * N) * 19 ^ (50 * (N - k)) * 31 ^ (50 * k - 31 * N) :=
          Nat.mul_le_mul_left _ (Nat.pow_le_pow_left (by norm_num) _)
      _ = 31 ^ (31 * N) * 31 ^ (50 * k - 31 * N) * 19 ^ (50 * (N - k)) := by ring
  calc tail N k ^ 50 * (31 ^ 31 * 19 ^ 19) ^ N
      ≤ tail N k ^ 50 * (31 ^ k * 19 ^ (N - k)) ^ 50 := Nat.mul_le_mul_left _ hweight
    _ = (tail N k * (31 ^ k * 19 ^ (N - k))) ^ 50 := (mul_pow _ _ _).symm
    _ ≤ ((31 + 19) ^ N) ^ 50 := hpow
    _ = (50 ^ 50) ^ N := by rw [← pow_mul, ← pow_mul, Nat.mul_comm]

/-- **Light side, in `ℕ`.** Too weak to export on its own — it carries no geometric saving — but
convenient internally. -/
theorem light_pow_le {m N : ℕ} (h : 50 * m ≤ 31 * N) : 3 ^ m ≤ 2 ^ N := by
  have h50 : (3 ^ m : ℕ) ^ 50 ≤ (2 ^ N) ^ 50 := by
    calc (3 ^ m : ℕ) ^ 50 = 3 ^ (50 * m) := by rw [← pow_mul, Nat.mul_comm]
      _ ≤ 3 ^ (31 * N) := Nat.pow_le_pow_right (by norm_num) h
      _ = (3 ^ 31) ^ N := by rw [← pow_mul, Nat.mul_comm]
      _ ≤ (2 ^ 50) ^ N := Nat.pow_le_pow_left (le_of_lt light_certificate) N
      _ = (2 ^ N) ^ 50 := by rw [← pow_mul, ← pow_mul, Nat.mul_comm]
  exact (Nat.pow_le_pow_iff_left (by norm_num)).mp h50

/-! ## 5. The single real base `θ < 2` -/

/-- From `x^d ≤ C^N` with `C > 0`, the `d`-th root of `C` bounds `x` geometrically. -/
private theorem le_base_pow {x N d : ℕ} {C : ℝ} (hd : d ≠ 0) (hC : 0 < C)
    (h : (x : ℝ) ^ d ≤ C ^ N) : (x : ℝ) ≤ (C ^ ((1 : ℝ) / d)) ^ N := by
  have hpos : (0 : ℝ) < C ^ ((1 : ℝ) / d) := Real.rpow_pos_of_pos hC _
  refine le_of_pow_le_pow_left₀ hd (le_of_lt (pow_pos hpos N)) ?_
  have hkey : ((C ^ ((1 : ℝ) / d)) ^ N) ^ d = C ^ N := by
    rw [← pow_mul, ← Real.rpow_natCast (C ^ ((1 : ℝ) / d)) (N * d),
        ← Real.rpow_mul (le_of_lt hC)]
    have hdne : (d : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr hd
    have : (1 : ℝ) / d * ((N * d : ℕ) : ℝ) = (N : ℝ) := by
      push_cast
      field_simp
    rw [this, Real.rpow_natCast]
  rw [hkey]
  exact h

/-- Both certificates, packaged as **one** base `θ < 2` valid for the heavy and the light branch,
so M5 sums a single ratio `θ/2`. -/
theorem exists_window_base :
    ∃ θ : ℝ, 1 ≤ θ ∧ θ < 2 ∧
      (∀ N k : ℕ, 31 * N ≤ 50 * k → (tail N k : ℝ) ≤ θ ^ N) ∧
      (∀ m N : ℕ, 50 * m ≤ 31 * N → (3 : ℝ) ^ m ≤ θ ^ N) := by
  -- the heavy base `(50^50 / (31^31·19^19))^{1/50}` and the light base `(3^31)^{1/50}`
  set Ch : ℝ := (50 : ℝ) ^ 50 / ((31 : ℝ) ^ 31 * (19 : ℝ) ^ 19) with hChdef
  set Cl : ℝ := (3 : ℝ) ^ 31 with hCldef
  have hden : (0 : ℝ) < (31 : ℝ) ^ 31 * (19 : ℝ) ^ 19 := by positivity
  have hChpos : 0 < Ch := by rw [hChdef]; positivity
  have hClpos : 0 < Cl := by rw [hCldef]; positivity
  set θh : ℝ := Ch ^ ((1 : ℝ) / 50) with hθh
  set θl : ℝ := Cl ^ ((1 : ℝ) / 50) with hθl
  have hθhpos : 0 < θh := Real.rpow_pos_of_pos hChpos _
  have hθlpos : 0 < θl := Real.rpow_pos_of_pos hClpos _
  -- `θ^50 = C` for both
  have hpow50 : ∀ C : ℝ, 0 < C → (C ^ ((1 : ℝ) / 50)) ^ (50 : ℕ) = C := by
    intro C hC
    rw [← Real.rpow_natCast (C ^ ((1 : ℝ) / 50)) 50, ← Real.rpow_mul (le_of_lt hC)]
    norm_num
  refine ⟨max θh θl, ?_, ?_, ?_, ?_⟩
  · -- `1 ≤ θ`
    have h1 : (1 : ℝ) ≤ θl := by
      refine le_of_pow_le_pow_left₀ (n := 50) (by norm_num) (le_of_lt hθlpos) ?_
      rw [one_pow, hθl, hpow50 Cl hClpos, hCldef]
      norm_num
    exact le_trans h1 (le_max_right _ _)
  · -- `θ < 2`, from the two integer certificates
    refine max_lt ?_ ?_
    · refine lt_of_pow_lt_pow_left₀ 50 (by norm_num) ?_
      rw [hθh, hpow50 Ch hChpos, hChdef, div_lt_iff₀ hden]
      exact_mod_cast entropy_certificate
    · refine lt_of_pow_lt_pow_left₀ 50 (by norm_num) ?_
      rw [hθl, hpow50 Cl hClpos, hCldef]
      exact_mod_cast light_certificate
  · -- heavy branch
    intro N k hNk
    have hnat := heavy_tail_pow hNk
    have hdiv : ((tail N k : ℝ)) ^ (50 : ℕ) ≤ Ch ^ N := by
      rw [hChdef, div_pow, le_div_iff₀ (by positivity)]
      exact_mod_cast hnat
    have hb := le_base_pow (x := tail N k) (N := N) (d := 50) (C := Ch) (by norm_num) hChpos hdiv
    exact le_trans hb (pow_le_pow_left₀ (le_of_lt hθhpos) (le_max_left _ _) N)
  · -- light branch
    intro m N hmN
    have hnat : (3 ^ m : ℕ) ^ 50 ≤ (3 ^ 31 : ℕ) ^ N := by
      calc (3 ^ m : ℕ) ^ 50 = 3 ^ (50 * m) := by rw [← pow_mul, Nat.mul_comm]
        _ ≤ 3 ^ (31 * N) := Nat.pow_le_pow_right (by norm_num) hmN
        _ = (3 ^ 31) ^ N := by rw [← pow_mul, Nat.mul_comm]
    have hdiv : (((3 ^ m : ℕ) : ℝ)) ^ (50 : ℕ) ≤ Cl ^ N := by
      rw [hCldef]
      exact_mod_cast hnat
    have hb := le_base_pow (x := 3 ^ m) (N := N) (d := 50) (C := Cl) (by norm_num) hClpos hdiv
    have hb' : (3 : ℝ) ^ m ≤ θl ^ N := by
      rw [hθl]
      push_cast at hb
      exact hb
    exact le_trans hb' (pow_le_pow_left₀ (le_of_lt hθlpos) (le_max_right _ _) N)

end Divergence
