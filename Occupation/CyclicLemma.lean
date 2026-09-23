import Mathlib.Analysis.SpecialFunctions.Log.Base
import Occupation.Compositions

/-!
# The cycle lemma (Dvoretzky–Motzkin 1947; Spitzer)

If real increments `x₀,…,x_{N-1}` have negative total, then some cyclic rotation has **every**
nonempty partial sum negative: rotate to start at the *last* index at which the partial sums
attain their maximum.

`exists_rot_neg` is generic — a fact about periodic real sequences with no Collatz content, in
the same spirit as `Divergence.exists_last_max`. Its arithmetic corollary `exists_rot_confined`
is stated **integrally**, as `2^s < 3^N`, so no real number leaks into the counting layer; the
only bridge is `two_pow_lt_three_pow_iff`.

Everything is indexed by `ℕ` with an explicit `% N`, rather than by `Fin N` with its group
structure: this Mathlib has no `NatCast (Fin N)`, and the `ℕ` form keeps every index
manipulation inside `omega`'s reach.

`card_comps_le_mul` is the counting consequence the lower bound needs: rotation maps every
composition to a `0`-confined one, and is at most `N`-to-1.

No `sorry`, `admit`, `axiom`, or `opaque`.
-/

namespace Occupation

open Finset

/-! ## 1. The integral/real bridge -/

/-- The one place reals meet the counting: `2^S < 3^j ↔ S < j·log₂3`. -/
theorem two_pow_lt_three_pow_iff {S j : ℕ} :
    (2 : ℕ) ^ S < 3 ^ j ↔ (S : ℝ) < (j : ℝ) * Real.logb 2 3 := by
  have hlog2 : (0 : ℝ) < Real.log 2 := Real.log_pos (by norm_num)
  have hcast : ((2 : ℕ) ^ S < 3 ^ j) ↔ ((2 : ℝ) ^ S < (3 : ℝ) ^ j) := by
    constructor
    · intro h; exact_mod_cast h
    · intro h; exact_mod_cast h
  have hlogiff : ((2 : ℝ) ^ S < (3 : ℝ) ^ j)
      ↔ (Real.log ((2 : ℝ) ^ S) < Real.log ((3 : ℝ) ^ j)) :=
    (Real.log_lt_log_iff (by positivity) (by positivity)).symm
  rw [hcast, hlogiff, Real.log_pow, Real.log_pow, Real.logb, ← mul_div_assoc,
    lt_div_iff₀ hlog2]

/-! ## 2. Cyclic rotation -/

/-- Cyclic rotation: `rot r d` reads `d` from position `r`, wrapping around. -/
def rot {N : ℕ} (r : ℕ) (d : Fin N → ℕ) : Fin N → ℕ := fun i => letter d ((r + (i : ℕ)) % N)

theorem letter_rot {N : ℕ} (r : ℕ) (d : Fin N → ℕ) {i : ℕ} (hi : i < N) :
    letter (rot r d) i = letter d ((r + i) % N) := by
  simp [letter, rot, hi]

/-- The partial sums of a rotation. -/
theorem psum_rot {N : ℕ} (r : ℕ) (d : Fin N → ℕ) {k : ℕ} (hk : k ≤ N) :
    psum (rot r d) k = ∑ i ∈ range k, letter d ((r + i) % N) := by
  unfold psum
  exact Finset.sum_congr rfl fun i hi =>
    letter_rot r d (lt_of_lt_of_le (Finset.mem_range.mp hi) hk)

/-- **A rotation permutes a full period.** -/
theorem sum_range_rot {N : ℕ} (hN : 0 < N) (f : ℕ → ℕ) (r : ℕ) :
    ∑ i ∈ range N, f ((r + i) % N) = ∑ i ∈ range N, f i := by
  set p := r % N with hp
  have hplt : p < N := Nat.mod_lt _ hN
  have hkey : ∀ i, i < N → (r + i) % N = if i + p < N then i + p else i + p - N := by
    intro i hi
    have h1 : (r + i) % N = (p + i) % N := by
      simp [hp, Nat.add_mod]
    rw [h1]
    split_ifs with hc
    · rw [Nat.mod_eq_of_lt (by omega), Nat.add_comm]
    · have he : p + i = (p + i - N) + N := by omega
      rw [he, Nat.add_mod_right, Nat.mod_eq_of_lt (by omega)]
      congr 1
      omega
  refine Finset.sum_nbij' (fun i => if i + p < N then i + p else i + p - N)
    (fun j => if p ≤ j then j - p else j + N - p) ?_ ?_ ?_ ?_ ?_
  · intro i hi; rw [Finset.mem_range] at hi ⊢; split <;> omega
  · intro j hj; rw [Finset.mem_range] at hj ⊢; split <;> omega
  · intro i hi; rw [Finset.mem_range] at hi; split <;> split <;> omega
  · intro j hj; rw [Finset.mem_range] at hj; split <;> split <;> omega
  · intro i hi; rw [hkey i (Finset.mem_range.mp hi)]

theorem sum_rot {N : ℕ} (hN : 0 < N) (r : ℕ) (d : Fin N → ℕ) :
    ∑ i, rot r d i = ∑ i, d i := by
  have h1 : ∑ i, rot r d i = psum (rot r d) N := (psum_total _).symm
  have h2 : ∑ i, d i = psum d N := (psum_total _).symm
  rw [h1, h2, psum_rot r d (le_refl N), psum, sum_range_rot hN (letter d) r]

theorem rot_mem_comps {N s : ℕ} (hN : 0 < N) {d : Fin N → ℕ} (hd : d ∈ comps N s) (r : ℕ) :
    rot r d ∈ comps N s := by
  rw [mem_comps] at hd ⊢
  refine ⟨by rw [sum_rot hN]; exact hd.1, fun i => ?_⟩
  have hmod : (r + (i : ℕ)) % N < N := Nat.mod_lt _ hN
  simp [rot, letter, hmod]
  exact hd.2 _

/-- Rotating by `r` then by `r'` is rotating by `r + r'`. -/
theorem rot_rot {N : ℕ} (hN : 0 < N) (r r' : ℕ) (d : Fin N → ℕ) :
    rot r' (rot r d) = rot (r + r') d := by
  funext i
  have hmod : (r' + (i : ℕ)) % N < N := Nat.mod_lt _ hN
  rw [rot, letter_rot r d hmod, rot]
  congr 1
  rw [Nat.add_mod_mod, Nat.add_assoc]

theorem rot_zero_mod {N : ℕ} {r : ℕ} (hr : r % N = 0) (d : Fin N → ℕ) :
    rot r d = d := by
  funext i
  rw [rot]
  have : (r + (i : ℕ)) % N = (i : ℕ) := by
    rw [Nat.add_mod, hr, Nat.zero_add, Nat.mod_mod, Nat.mod_eq_of_lt i.isLt]
  simp [this, letter, i.isLt]

/-! ## 3. The cycle lemma -/

/-- **The cycle lemma** (Dvoretzky–Motzkin; Spitzer). Generic: no Collatz content. -/
theorem exists_rot_neg {N : ℕ} (hN : 0 < N) (y : ℕ → ℝ) (hper : ∀ i, y (i + N) = y i)
    (htot : ∑ i ∈ range N, y i < 0) :
    ∃ m, m < N ∧ ∀ k, 1 ≤ k → k ≤ N → ∑ i ∈ range k, y (m + i) < 0 := by
  classical
  set σ : ℕ → ℝ := fun k => ∑ i ∈ range k, y i with hσ
  have hsucc : ∀ k : ℕ, σ (k + 1) = σ k + y k := fun k => Finset.sum_range_succ y k
  have hblock : ∀ a k : ℕ, ∑ i ∈ range k, y (a + i) = σ (a + k) - σ a := by
    intro a k
    induction k with
    | zero => simp
    | succ k ih =>
      rw [Finset.sum_range_succ, ih]
      have he : a + (k + 1) = (a + k) + 1 := by omega
      rw [he, hsucc]
      ring
  have hshift : ∀ k : ℕ, σ (N + k) = σ k + σ N := by
    intro k
    induction k with
    | zero => simp [hσ]
    | succ k ih =>
      have he : N + (k + 1) = (N + k) + 1 := by omega
      rw [he, hsucc, ih, hsucc]
      have hyk : y (N + k) = y k := by rw [Nat.add_comm N k]; exact hper k
      rw [hyk]
      ring
  -- the last index in `range N` at which `σ` is maximal
  have hne : (range N).Nonempty := ⟨0, Finset.mem_range.mpr hN⟩
  obtain ⟨b, hbmem, hb⟩ := Finset.exists_mem_eq_sup' hne σ
  set G : Finset ℕ := (range N).filter (fun n => σ n = (range N).sup' hne σ) with hG
  have hGne : G.Nonempty := ⟨b, by rw [hG, Finset.mem_filter]; exact ⟨hbmem, hb.symm⟩⟩
  set m := G.max' hGne with hm
  have hmG : m ∈ G := G.max'_mem hGne
  have hmrange : m ∈ range N := by
    have h := hmG; rw [hG, Finset.mem_filter] at h; exact h.1
  have hmval : σ m = (range N).sup' hne σ := by
    have h := hmG; rw [hG, Finset.mem_filter] at h; exact h.2
  have hmax : ∀ n ∈ range N, σ n ≤ σ m := by
    intro n hn; rw [hmval]; exact Finset.le_sup' σ hn
  have hlast : ∀ n ∈ range N, m < n → σ n < σ m := by
    intro n hn hmn
    rcases lt_or_eq_of_le (hmax n hn) with h | h
    · exact h
    · exfalso
      have hnG : n ∈ G := by rw [hG, Finset.mem_filter]; exact ⟨hn, by rw [h, hmval]⟩
      have := G.le_max' _ hnG
      omega
  have hmlt : m < N := Finset.mem_range.mp hmrange
  have hzero : (0 : ℝ) ≤ σ m := by
    have h := hmax 0 (Finset.mem_range.mpr hN)
    simpa [hσ] using h
  have hσN : σ N < 0 := htot
  refine ⟨m, hmlt, fun k hk1 hkN => ?_⟩
  rw [hblock m k]
  rcases lt_trichotomy (m + k) N with hlt | heq | hgt
  · have := hlast (m + k) (Finset.mem_range.mpr hlt) (by omega)
    linarith
  · rw [heq]
    linarith
  · obtain ⟨k', hk'⟩ : ∃ k', m + k = N + k' := ⟨m + k - N, by omega⟩
    have hk'lt : k' < N := by omega
    rw [hk', hshift k']
    have := hmax k' (Finset.mem_range.mpr hk'lt)
    linarith

/-! ## 4. The arithmetic corollary -/

/-- A composition whose total satisfies `2^s < 3^N` has a `0`-confined rotation. -/
theorem exists_rot_confined {N s : ℕ} (hN : 0 < N) {d : Fin N → ℕ}
    (hd : d ∈ comps N s) (hlt : 2 ^ s < 3 ^ N) :
    ∃ r : ℕ, rot r d ∈ confComps N 0 s := by
  have hsum : (∑ i, d i) = s := (mem_comps.mp hd).1
  set α : ℝ := Real.logb 2 3 with hα
  set y : ℕ → ℝ := fun i => (letter d (i % N) : ℝ) - α with hy
  have hper : ∀ i, y (i + N) = y i := by
    intro i
    simp only [hy, Nat.add_mod_right]
  have htot : ∑ i ∈ range N, y i < 0 := by
    have hrw : ∑ i ∈ range N, y i
        = (∑ i ∈ range N, (letter d i : ℝ)) - (N : ℝ) * α := by
      simp only [hy]
      rw [Finset.sum_sub_distrib, Finset.sum_const, Finset.card_range, nsmul_eq_mul]
      congr 1
      exact Finset.sum_congr rfl fun i hi => by
        rw [Nat.mod_eq_of_lt (Finset.mem_range.mp hi)]
    rw [hrw]
    have hps : ∑ i ∈ range N, (letter d i : ℝ) = (s : ℝ) := by
      rw [← Nat.cast_sum]
      have : ∑ i ∈ range N, letter d i = s := by rw [← psum, psum_total, hsum]
      rw [this]
    rw [hps]
    have := two_pow_lt_three_pow_iff.mp hlt
    linarith
  obtain ⟨m, hmlt, hm⟩ := exists_rot_neg hN y hper htot
  refine ⟨m, ?_⟩
  rw [mem_confComps]
  refine ⟨mem_comps.mp (rot_mem_comps hN hd m), ?_⟩
  intro j hj
  rcases Nat.eq_zero_or_pos j with rfl | hj1
  · simp
  · have hlt' := hm j hj1 hj
    have hrw : ∑ i ∈ range j, y (m + i)
        = (psum (rot m d) j : ℝ) - (j : ℝ) * α := by
      simp only [hy]
      rw [Finset.sum_sub_distrib, Finset.sum_const, Finset.card_range, nsmul_eq_mul]
      congr 1
      rw [psum_rot m d hj, Nat.cast_sum]
    rw [hrw] at hlt'
    have hkey : (psum (rot m d) j : ℝ) < (j : ℝ) * α := by linarith
    simpa using le_of_lt (two_pow_lt_three_pow_iff.mpr hkey)

/-! ## 5. The counting consequence -/

/-- Rotation to a confined representative is at most `N`-to-1. -/
theorem card_comps_le_mul {N s : ℕ} (hN : 0 < N) (hlt : 2 ^ s < 3 ^ N) :
    (comps N s).card ≤ N * (confComps N 0 s).card := by
  classical
  set pick : (Fin N → ℕ) → (Fin N → ℕ) := fun d =>
    if h : d ∈ comps N s then rot (Classical.choose (exists_rot_confined hN h hlt)) d else d
    with hpick
  have hmaps : ∀ d ∈ comps N s, pick d ∈ confComps N 0 s := by
    intro d hd
    simp only [hpick]
    split_ifs
    exact Classical.choose_spec (exists_rot_confined hN hd hlt)
  rw [Finset.card_eq_sum_card_fiberwise hmaps]
  have hfibre : ∀ w ∈ confComps N 0 s,
      ((comps N s).filter (fun d => pick d = w)).card ≤ N := by
    intro w _
    have hsub : (comps N s).filter (fun d => pick d = w)
        ⊆ (range N).image (fun r' => rot r' w) := by
      intro d hd
      rw [Finset.mem_filter] at hd
      obtain ⟨hdc, hdw⟩ := hd
      simp only [hpick] at hdw
      split_ifs at hdw
      set r := Classical.choose (exists_rot_confined hN hdc hlt) with hr
      refine Finset.mem_image.mpr ⟨(N - r % N) % N, ?_, ?_⟩
      · exact Finset.mem_range.mpr (Nat.mod_lt _ hN)
      · rw [← hdw, rot_rot hN]
        have hrm : r % N < N := Nat.mod_lt _ hN
        have key : (r + (N - r % N) % N) % N = 0 := by
          rcases Nat.eq_zero_or_pos (r % N) with h0 | hpos
          · have he : N - r % N = N := by omega
            rw [he, Nat.mod_self, Nat.add_zero, h0]
          · have h1 : (N - r % N) % N = N - r % N := Nat.mod_eq_of_lt (by omega)
            rw [h1, Nat.add_mod, Nat.mod_eq_of_lt (show N - r % N < N by omega)]
            have h2 : r % N + (N - r % N) = N := by omega
            rw [h2, Nat.mod_self]
        exact rot_zero_mod key d
    calc ((comps N s).filter (fun d => pick d = w)).card
        ≤ ((range N).image (fun r' => rot r' w)).card := Finset.card_le_card hsub
      _ ≤ (range N).card := Finset.card_image_le
      _ = N := Finset.card_range N
  calc (∑ w ∈ confComps N 0 s, ((comps N s).filter (fun d => pick d = w)).card)
      ≤ ∑ _w ∈ confComps N 0 s, N := Finset.sum_le_sum hfibre
    _ = (confComps N 0 s).card * N := by rw [Finset.sum_const, smul_eq_mul]
    _ = N * (confComps N 0 s).card := by ring

end Occupation
