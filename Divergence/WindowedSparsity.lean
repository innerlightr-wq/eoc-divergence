import Divergence.BinomialTail

/-!
# The windowed sparsity theorem (Garcia–Tal Fundamental Lemma; Curry Thm 2.3)

A collision-free set `A ⊆ ℕ` meets every dyadic-length window `[a, a + 2^N)` in at most
`4(N+1)·θ^N` points, with `θ < 2` the base certified in `Divergence.BinomialTail`. Since a
window of length `2^N` would contain `2^N` integers outright, this is a genuine power saving,
uniform in `a` — which is what makes the dyadic sum of M5 converge.

Fixing the window length to exactly `2^N` (rather than `2^N ≤ X < 2^(N+1)`) sharpens both
branches: `[1, 2^N]` carries exactly one element per residue class mod `2^N`, so the heavy
fibre costs `C(N,m)` with no factor of two.

The argument:

1. **Split.** With `z = (a-1)/2^N` every window element lands, after subtracting `z·2^N` or
   `(z+1)·2^N`, in `[1, 2^N]`. Two shifts, no pigeonhole.
2. **Fibre** by `m = oddCount N s`, over `m ∈ {0,…,N}`.
3. **Heavy fibre:** `s ↦ parityPrefix N s` is injective, giving `≤ C(N,m) ≤ tail N m`.
4. **Light fibre:** `s ↦ U^[N] s` is injective by collision-freeness, and contraction confines
   it to `[0, 2·3^m)`.

Steps 3 and 4 hold for **every** `m`. The heavy/light split enters once, in the final assembly,
only to decide which of the two bounds to feed to `exists_window_base`.

No `sorry`, `admit`, `axiom`, or `opaque`.
-/

namespace Divergence

open Finset

/-! ## 1. The window and the shifted blocks -/

open Classical in
/-- The dyadic window `A ∩ [a, a + 2^N)`, as a `Finset`. -/
noncomputable def windowFinset (A : Set ℕ) (a N : ℕ) : Finset ℕ :=
  (Finset.Ico a (a + 2 ^ N)).filter (· ∈ A)

open Classical in
/-- Elements of `[1, 2^N]` whose shift by `t·2^N` lands in `A`. -/
noncomputable def Bset (A : Set ℕ) (N t : ℕ) : Finset ℕ :=
  (Finset.Icc 1 (2 ^ N)).filter (fun s => s + t * 2 ^ N ∈ A)

theorem mem_windowFinset {A : Set ℕ} {a N y : ℕ} :
    y ∈ windowFinset A a N ↔ (a ≤ y ∧ y < a + 2 ^ N) ∧ y ∈ A := by
  simp only [windowFinset, Finset.mem_filter, Finset.mem_Ico]

theorem mem_Bset {A : Set ℕ} {N t s : ℕ} :
    s ∈ Bset A N t ↔ (1 ≤ s ∧ s ≤ 2 ^ N) ∧ s + t * 2 ^ N ∈ A := by
  simp only [Bset, Finset.mem_filter, Finset.mem_Icc]

/-- **The bridge** from `Set.ncard` to `Finset.card`. -/
theorem ncard_window_eq (A : Set ℕ) (a N : ℕ) :
    (A ∩ Set.Ico a (a + 2 ^ N)).ncard = (windowFinset A a N).card := by
  have hcoe : A ∩ Set.Ico a (a + 2 ^ N) = ↑(windowFinset A a N) := by
    ext y
    simp only [Set.mem_inter_iff, Set.mem_Ico, Finset.mem_coe, mem_windowFinset]
    tauto
  rw [hcoe, Set.ncard_coe_finset]

/-! ## 2. Step 1: the shift split -/

/-- **Two shifts suffice.** No pigeonhole on `z`: both terms are bounded, not one chosen. -/
theorem window_card_le_shifts (A : Set ℕ) {a : ℕ} (ha : 1 ≤ a) (N : ℕ) :
    (windowFinset A a N).card
      ≤ (Bset A N ((a - 1) / 2 ^ N)).card + (Bset A N ((a - 1) / 2 ^ N + 1)).card := by
  set z := (a - 1) / 2 ^ N with hz
  have hpow : 0 < 2 ^ N := pow_pos (by norm_num) N
  have hd : z * 2 ^ N + (a - 1) % 2 ^ N = a - 1 := by
    rw [Nat.mul_comm]
    exact Nat.div_add_mod (a - 1) (2 ^ N)
  have hm : (a - 1) % 2 ^ N < 2 ^ N := Nat.mod_lt _ hpow
  have hexp : (z + 1) * 2 ^ N = z * 2 ^ N + 2 ^ N := by ring
  have hlo : z * 2 ^ N < a := by omega
  have hhi : a ≤ (z + 1) * 2 ^ N := by omega
  have hsub : windowFinset A a N ⊆
      ((Bset A N z).image (fun s => s + z * 2 ^ N)) ∪
        ((Bset A N (z + 1)).image (fun s => s + (z + 1) * 2 ^ N)) := by
    intro y hy
    rw [mem_windowFinset] at hy
    obtain ⟨⟨hy1, hy2⟩, hyA⟩ := hy
    rw [Finset.mem_union]
    by_cases hcase : y ≤ (z + 1) * 2 ^ N
    · left
      refine Finset.mem_image.mpr ⟨y - z * 2 ^ N, ?_, by omega⟩
      rw [mem_Bset]
      refine ⟨⟨by omega, by omega⟩, ?_⟩
      have hback : y - z * 2 ^ N + z * 2 ^ N = y := by omega
      rw [hback]
      exact hyA
    · right
      have hgt : (z + 1) * 2 ^ N < y := Nat.not_le.mp hcase
      refine Finset.mem_image.mpr ⟨y - (z + 1) * 2 ^ N, ?_, by omega⟩
      rw [mem_Bset]
      refine ⟨⟨by omega, by omega⟩, ?_⟩
      have hback : y - (z + 1) * 2 ^ N + (z + 1) * 2 ^ N = y := by omega
      rw [hback]
      exact hyA
  calc (windowFinset A a N).card
      ≤ (((Bset A N z).image (fun s => s + z * 2 ^ N)) ∪
          ((Bset A N (z + 1)).image (fun s => s + (z + 1) * 2 ^ N))).card :=
        Finset.card_le_card hsub
    _ ≤ ((Bset A N z).image (fun s => s + z * 2 ^ N)).card
          + ((Bset A N (z + 1)).image (fun s => s + (z + 1) * 2 ^ N)).card :=
        Finset.card_union_le _ _
    _ ≤ (Bset A N z).card + (Bset A N (z + 1)).card :=
        Nat.add_le_add Finset.card_image_le Finset.card_image_le

/-! ## 3. Step 2: fibring by the odd-step count -/

theorem Bset_card_eq_sum_fibres (A : Set ℕ) (N t : ℕ) :
    (Bset A N t).card
      = ∑ m ∈ Finset.range (N + 1),
          ((Bset A N t).filter (fun s => oddCount N s = m)).card := by
  refine Finset.card_eq_sum_card_fiberwise ?_
  intro s _
  exact Finset.mem_range.mpr (by have := oddCount_le N s; omega)

/-! ## 4. Step 3: the heavy fibre -/

/-- On `[1, 2^N]` a congruence mod `2^N` is an equality: exactly one element per class. -/
private theorem eq_of_modEq_Icc {N s₁ s₂ : ℕ} (h1 : 1 ≤ s₁) (h1' : s₁ ≤ 2 ^ N)
    (h2 : 1 ≤ s₂) (h2' : s₂ ≤ 2 ^ N) (h : s₁ ≡ s₂ [MOD 2 ^ N]) : s₁ = s₂ := by
  unfold Nat.ModEq at h
  rcases eq_or_lt_of_le h1' with he1 | hl1 <;> rcases eq_or_lt_of_le h2' with he2 | hl2
  · omega
  · rw [he1, Nat.mod_self, Nat.mod_eq_of_lt hl2] at h; omega
  · rw [he2, Nat.mod_self, Nat.mod_eq_of_lt hl1] at h; omega
  · rw [Nat.mod_eq_of_lt hl1, Nat.mod_eq_of_lt hl2] at h; exact h

/-- **Heavy fibre.** Holds for every `m`; the heavy/light split is not used here. -/
theorem fibre_card_le_choose (A : Set ℕ) (N t m : ℕ) :
    ((Bset A N t).filter (fun s => oddCount N s = m)).card ≤ N.choose m := by
  have hmaps : ∀ s ∈ (Bset A N t).filter (fun s => oddCount N s = m),
      parityPrefix N s ∈ Finset.powersetCard m (Finset.range N) := by
    intro s hs
    rw [Finset.mem_filter] at hs
    rw [Finset.mem_powersetCard]
    exact ⟨parityPrefix_subset N s, by rw [← oddCount_eq_card]; exact hs.2⟩
  have hinj : Set.InjOn (parityPrefix N)
      ↑((Bset A N t).filter (fun s => oddCount N s = m)) := by
    intro s₁ hs₁ s₂ hs₂ heq
    simp only [Finset.coe_filter, Set.mem_ofPred_eq] at hs₁ hs₂
    rw [mem_Bset] at hs₁ hs₂
    exact eq_of_modEq_Icc hs₁.1.1.1 hs₁.1.1.2 hs₂.1.1.1 hs₂.1.1.2
      (modEq_of_parityPrefix_eq heq)
  calc ((Bset A N t).filter (fun s => oddCount N s = m)).card
      ≤ (Finset.powersetCard m (Finset.range N)).card :=
        Finset.card_le_card_of_injOn _ hmaps hinj
    _ = N.choose m := by rw [Finset.card_powersetCard, Finset.card_range]

theorem choose_le_tail {N m : ℕ} (h : m ≤ N) : N.choose m ≤ tail N m := by
  unfold tail
  exact Finset.single_le_sum (f := fun j => N.choose j) (fun _ _ => Nat.zero_le _)
    (Finset.mem_Icc.mpr ⟨le_refl m, h⟩)

/-! ## 5. Step 4: the light fibre -/

/-- **Light fibre.** Holds for every `m`; collision-freeness is what makes `U^[N]` injective. -/
theorem light_fibre_card_le {A : Set ℕ} (hA : CollisionFree A) (N t m : ℕ) :
    ((Bset A N t).filter (fun s => oddCount N s = m)).card ≤ 2 * 3 ^ m := by
  have hpow : 0 < 2 ^ N := pow_pos (by norm_num) N
  have hmaps : ∀ s ∈ (Bset A N t).filter (fun s => oddCount N s = m),
      U^[N] s ∈ Finset.range (2 * 3 ^ m) := by
    intro s hs
    rw [Finset.mem_filter, mem_Bset] at hs
    obtain ⟨⟨⟨_, hs2⟩, _⟩, hoc⟩ := hs
    rw [Finset.mem_range]
    have hcon := contraction N s
    rw [hoc] at hcon
    have hbound : 3 ^ m * (s + 2 ^ N) ≤ 2 ^ N * (2 * 3 ^ m) := by
      have : s + 2 ^ N ≤ 2 * 2 ^ N := by omega
      calc 3 ^ m * (s + 2 ^ N) ≤ 3 ^ m * (2 * 2 ^ N) := Nat.mul_le_mul_left _ this
        _ = 2 ^ N * (2 * 3 ^ m) := by ring
    exact Nat.lt_of_mul_lt_mul_left (lt_of_lt_of_le hcon hbound)
  have hinj : Set.InjOn (fun s => U^[N] s)
      ↑((Bset A N t).filter (fun s => oddCount N s = m)) := by
    intro s₁ hs₁ s₂ hs₂ heq
    simp only [Finset.coe_filter, Set.mem_ofPred_eq] at hs₁ hs₂
    rw [mem_Bset] at hs₁ hs₂
    simp only at heq
    -- shifting by `t·2^N` preserves the collision, because the two fibre elements share `m`
    have hcol : U^[N] (s₁ + t * 2 ^ N) = U^[N] (s₂ + t * 2 ^ N) := by
      rw [U_iter_shift_endpoint, U_iter_shift_endpoint, heq, hs₁.2, hs₂.2]
    have := hA _ hs₁.1.2 _ hs₂.1.2 N hcol
    omega
  calc ((Bset A N t).filter (fun s => oddCount N s = m)).card
      ≤ (Finset.range (2 * 3 ^ m)).card := Finset.card_le_card_of_injOn _ hmaps hinj
    _ = 2 * 3 ^ m := Finset.card_range _

/-! ## 6. Step 5: the windowed sparsity bound -/

/-- **Windowed sparsity.** A collision-free set meets every window of length `2^N` in at most
`4(N+1)·θ^N` points, with `θ < 2` — a power saving uniform in `a`. -/
theorem exists_window_sparsity :
    ∃ θ : ℝ, 1 ≤ θ ∧ θ < 2 ∧ ∀ A : Set ℕ, CollisionFree A →
      ∀ N a : ℕ, 1 ≤ a →
        ((A ∩ Set.Ico a (a + 2 ^ N)).ncard : ℝ) ≤ 4 * (N + 1) * θ ^ N := by
  obtain ⟨θ, hθ1, hθ2, hheavy, hlight⟩ := exists_window_base
  refine ⟨θ, hθ1, hθ2, ?_⟩
  intro A hA N a ha
  have hθpos : (0 : ℝ) < θ ^ N := pow_pos (lt_of_lt_of_le zero_lt_one hθ1) N
  -- every fibre, heavy or light, is at most `2θ^N`
  have hfibre : ∀ t m : ℕ, m ≤ N →
      ((((Bset A N t).filter (fun s => oddCount N s = m)).card : ℝ)) ≤ 2 * θ ^ N := by
    intro t m hm
    by_cases hcase : 31 * N ≤ 50 * m
    · have hnat : ((Bset A N t).filter (fun s => oddCount N s = m)).card ≤ tail N m :=
        le_trans (fibre_card_le_choose A N t m) (choose_le_tail hm)
      calc ((((Bset A N t).filter (fun s => oddCount N s = m)).card : ℝ))
          ≤ (tail N m : ℝ) := by exact_mod_cast hnat
        _ ≤ θ ^ N := hheavy N m hcase
        _ ≤ 2 * θ ^ N := by linarith
    · have hnat := light_fibre_card_le hA N t m
      have hl := hlight m N (by omega)
      calc ((((Bset A N t).filter (fun s => oddCount N s = m)).card : ℝ))
          ≤ ((2 * 3 ^ m : ℕ) : ℝ) := by exact_mod_cast hnat
        _ = 2 * (3 : ℝ) ^ m := by push_cast; ring
        _ ≤ 2 * θ ^ N := by linarith
  -- summing the `N+1` fibres
  have hB : ∀ t : ℕ, ((Bset A N t).card : ℝ) ≤ ((N : ℝ) + 1) * (2 * θ ^ N) := by
    intro t
    rw [Bset_card_eq_sum_fibres A N t]
    push_cast
    calc (∑ m ∈ Finset.range (N + 1),
            (((Bset A N t).filter (fun s => oddCount N s = m)).card : ℝ))
        ≤ ∑ _m ∈ Finset.range (N + 1), (2 * θ ^ N) := by
          refine Finset.sum_le_sum fun m hm => ?_
          exact hfibre t m (by have := Finset.mem_range.mp hm; omega)
      _ = ((N : ℝ) + 1) * (2 * θ ^ N) := by
          rw [Finset.sum_const, Finset.card_range, nsmul_eq_mul]
          push_cast
          ring
  -- two shifts
  have hwin := window_card_le_shifts A ha N
  have hwinR : ((windowFinset A a N).card : ℝ)
      ≤ ((Bset A N ((a - 1) / 2 ^ N)).card : ℝ)
        + ((Bset A N ((a - 1) / 2 ^ N + 1)).card : ℝ) := by exact_mod_cast hwin
  rw [ncard_window_eq]
  calc ((windowFinset A a N).card : ℝ)
      ≤ ((Bset A N ((a - 1) / 2 ^ N)).card : ℝ)
        + ((Bset A N ((a - 1) / 2 ^ N + 1)).card : ℝ) := hwinR
    _ ≤ ((N : ℝ) + 1) * (2 * θ ^ N) + ((N : ℝ) + 1) * (2 * θ ^ N) :=
        add_le_add (hB _) (hB _)
    _ = 4 * ((N : ℝ) + 1) * θ ^ N := by ring

end Divergence
