import Divergence.Basic

/-!
# Cycles drift upward, and the `←` direction of the headline theorem

This file proves paper **Lemma 4.2**: a repeated orbit value forces `2^{S_cyc} > 3^L` on the
cycle, and iterating the cycle then pushes `2^{S_n}` past `3^n`, so a periodic orbit is never
zero-confined. Contrapositively, a zero-confined seed has an injective orbit — and an injective
`ℕ`-valued orbit diverges.

That is the `←` half of

```
(∃ M, Odd M ∧ DivergentOrbit M) ↔ (∃ m, Odd m ∧ ZeroConfined m)
```

The Bernoulli step is done entirely in `ℕ` via `pow_succ_mul_le`, with the explicit witness
`t = 3^i · 3^L`; no real-valued drift `R_n` appears. `R_n` is only needed in `LastMaximum`.

No `sorry`, `admit`, `axiom`, or `opaque`.
-/

namespace Divergence

open Finset

/-! ## 1. The two properties -/

/-- `m` is **zero-confined**: `2^{S_n} ≤ 3^n` for every `n`, the integral form of `R_n ≤ 0`. -/
def ZeroConfined (m : ℕ) : Prop := ∀ n, 2 ^ S m n ≤ 3 ^ n

/-- The orbit of `M` **diverges**: it exceeds every bound from some time on. -/
def DivergentOrbit (M : ℕ) : Prop := ∀ K, ∃ N₀, ∀ n, N₀ ≤ n → K < orbit M n

/-! ## 2. Periodicity bookkeeping -/

/-- If `L` is a period of `x`, so is every multiple of `L`. -/
theorem orbit_periodic {x L : ℕ} (h : orbit x L = x) (t : ℕ) : orbit x (t * L) = x := by
  induction t with
  | zero => simp
  | succ t ih =>
    have hst : (t + 1) * L = t * L + L := by ring
    rw [hst, orbit_add, ih, h]

/-- **Valuation over `t` periods.** `S x (t·L) = t · S x L` when `orbit x L = x`. -/
theorem S_periodic {x L : ℕ} (h : orbit x L = x) (t : ℕ) : S x (t * L) = t * S x L := by
  induction t with
  | zero => simp
  | succ t ih =>
    have hst : (t + 1) * L = t * L + L := by ring
    rw [hst, S_add, ih, orbit_periodic h t]
    ring

/-! ## 3. The Bernoulli step, in `ℕ` -/

/-- `B^t · (B + t) ≤ (B+1)^t · B`: the only growth estimate the cycle argument needs, with no
subtraction and no reals. It holds for every `B`, including `B = 0`, so no `1 ≤ B` is assumed. -/
theorem pow_succ_mul_le (B t : ℕ) : B ^ t * (B + t) ≤ (B + 1) ^ t * B := by
  induction t with
  | zero => simp
  | succ t ih =>
    have step : B ^ t * B * (B + (t + 1)) ≤ B ^ t * ((B + 1) * (B + t)) := by
      have h : B * (B + (t + 1)) ≤ (B + 1) * (B + t) := by nlinarith
      calc B ^ t * B * (B + (t + 1)) = B ^ t * (B * (B + (t + 1))) := by ring
        _ ≤ B ^ t * ((B + 1) * (B + t)) := Nat.mul_le_mul_left _ h
    calc B ^ (t + 1) * (B + (t + 1))
        = B ^ t * B * (B + (t + 1)) := by rw [pow_succ]
      _ ≤ B ^ t * ((B + 1) * (B + t)) := step
      _ = (B + 1) * (B ^ t * (B + t)) := by ring
      _ ≤ (B + 1) * ((B + 1) ^ t * B) := Nat.mul_le_mul_left _ ih
      _ = (B + 1) ^ (t + 1) * B := by rw [pow_succ]; ring

/-! ## 4. Paper Lemma 4.2 -/

/-- **The cycle inequality.** A repeated value forces the cycle's total valuation above the
cycle's length times `log₂3`: `3^L < 2^{S_cyc}` with `L = j - i`. -/
theorem cycle_drift {m i j : ℕ} (hm : Odd m) (hij : i < j)
    (hrep : orbit m i = orbit m j) :
    3 ^ (j - i) < 2 ^ S (orbit m i) (j - i) := by
  set x := orbit m i with hxdef
  set L := j - i with hLdef
  have hL : 1 ≤ L := by omega
  have hcyc : orbit x L = x := by
    rw [hxdef, ← orbit_add]
    have : i + L = j := by omega
    rw [this, ← hrep]
  have hagg := aggregate_identity x L
  rw [hcyc] at hagg
  -- `2^{S_cyc} · x = 3^L · x + C_L`, with `C_L > 0` and `x > 0`
  have hCpos : 0 < C x L := C_pos x hL
  have hxpos : 0 < x := orbit_pos hm i
  have hlt : 3 ^ L * x < 2 ^ S x L * x := by omega
  exact lt_of_mul_lt_mul_right hlt (Nat.zero_le x)

/-- **A periodic orbit is not zero-confined.** Iterating the cycle `t = 3^i · 3^L` times makes
`2^{S_n}` overtake `3^n`. -/
theorem not_zeroConfined_of_repeat {m i j : ℕ} (hm : Odd m) (hij : i < j)
    (hrep : orbit m i = orbit m j) : ¬ ZeroConfined m := by
  intro hzc
  set x := orbit m i with hxdef
  set L := j - i with hLdef
  have hL : 1 ≤ L := by omega
  have hcyc : orbit x L = x := by
    rw [hxdef, ← orbit_add]
    have : i + L = j := by omega
    rw [this, ← hrep]
  set B := 3 ^ L with hBdef
  set A := 2 ^ S x L with hAdef
  have hB1 : 1 ≤ B := Nat.one_le_pow _ _ (by norm_num)
  have hAB : B + 1 ≤ A := cycle_drift hm hij hrep
  set t := 3 ^ i * B with htdef
  set n := i + t * L with hndef
  -- the two sides at time `n`
  have hS : 2 ^ S m n = 2 ^ S m i * A ^ t := by
    have h1 : S m n = S m i + t * S x L := by
      rw [hndef, S_add, ← hxdef, S_periodic hcyc t]
    rw [h1, pow_add, hAdef, ← pow_mul]
    ring_nf
  have h3 : 3 ^ n = 3 ^ i * B ^ t := by
    rw [hndef, pow_add, hBdef, ← pow_mul]
    ring_nf
  -- `3^i · B^t < A^t`
  have hkey : 3 ^ i * B ^ t < A ^ t := by
    have step1 : B ^ t * (3 ^ i * B) < B ^ t * (B + t) := by
      have hBt : 0 < B ^ t := pow_pos (by omega) t
      have : 3 ^ i * B < B + t := by rw [htdef]; omega
      exact mul_lt_mul_of_pos_left this hBt
    have step2 : B ^ t * (B + t) ≤ (B + 1) ^ t * B := pow_succ_mul_le B t
    have step3 : (B + 1) ^ t * B ≤ A ^ t * B :=
      Nat.mul_le_mul_right _ (Nat.pow_le_pow_left hAB t)
    have hmul : B * (3 ^ i * B ^ t) < B * A ^ t := by
      calc B * (3 ^ i * B ^ t) = B ^ t * (3 ^ i * B) := by ring
        _ < B ^ t * (B + t) := step1
        _ ≤ (B + 1) ^ t * B := step2
        _ ≤ A ^ t * B := step3
        _ = B * A ^ t := by ring
    exact Nat.lt_of_mul_lt_mul_left hmul
  -- contradiction with zero-confinement at time `n`
  have hone : 1 ≤ 2 ^ S m i := Nat.one_le_pow _ _ (by norm_num)
  have hfinal : 3 ^ n < 2 ^ S m n := by
    rw [hS, h3]
    calc 3 ^ i * B ^ t < A ^ t := hkey
      _ = 1 * A ^ t := by ring
      _ ≤ 2 ^ S m i * A ^ t := Nat.mul_le_mul_right _ hone
  exact absurd (hzc n) (by omega)

/-! ## 5. Injectivity and divergence -/

/-- Zero-confinement rules out repeats, so the orbit is injective. -/
theorem injective_of_zeroConfined {m : ℕ} (hm : Odd m) (hzc : ZeroConfined m) :
    Function.Injective (orbit m) := by
  intro i j hrep
  by_contra hne
  rcases Nat.lt_trichotomy i j with h | h | h
  · exact not_zeroConfined_of_repeat hm h hrep hzc
  · exact hne h
  · exact not_zeroConfined_of_repeat hm h hrep.symm hzc

/-- Past a repeat, the orbit only revisits values it already took before time `j`. -/
private theorem bounded_of_repeat {M i j : ℕ} (hij : i < j) (hrep : orbit M i = orbit M j) :
    ∀ n, orbit M n ≤ (range j).sup (orbit M) := by
  intro n
  induction n using Nat.strong_induction_on with
  | _ n ih =>
    by_cases hn : n < j
    · exact Finset.le_sup (Finset.mem_range.mpr hn)
    · have hn' : j ≤ n := Nat.not_lt.mp hn
      have hshift : orbit M n = orbit M (n - (j - i)) := by
        have h2 : n - (j - i) = i + (n - j) := by omega
        have h1 : n = j + (n - j) := by omega
        rw [h2]
        conv_lhs => rw [h1]
        rw [orbit_add, orbit_add, ← hrep]
      rw [hshift]
      exact ih _ (by omega)

/-- An injective `ℕ`-valued orbit diverges: only finitely many indices sit below any bound. -/
theorem divergent_of_injective {M : ℕ} (hinj : Function.Injective (orbit M)) :
    DivergentOrbit M := by
  intro K
  have hfin : ((orbit M) ⁻¹' (Set.Iic K)).Finite :=
    Set.Finite.preimage hinj.injOn (Set.finite_Iic K)
  obtain ⟨N₀, hN₀⟩ := hfin.bddAbove
  refine ⟨N₀ + 1, fun n hn => ?_⟩
  by_contra hcon
  have hcon' : orbit M n ≤ K := not_lt.mp hcon
  have : n ≤ N₀ := hN₀ (show n ∈ (orbit M) ⁻¹' (Set.Iic K) from hcon')
  omega

/-- A divergent orbit has no repeats: a repeat would bound it forever. -/
theorem injective_of_divergent {M : ℕ} (hdiv : DivergentOrbit M) :
    Function.Injective (orbit M) := by
  intro i j hrep
  by_contra hne
  have key : ∃ K, ∀ n, orbit M n ≤ K := by
    rcases Nat.lt_trichotomy i j with h | h | h
    · exact ⟨_, bounded_of_repeat h hrep⟩
    · exact absurd h hne
    · exact ⟨_, bounded_of_repeat h hrep.symm⟩
  obtain ⟨K, hK⟩ := key
  obtain ⟨N₀, hN₀⟩ := hdiv K
  exact absurd (hN₀ N₀ le_rfl) (not_lt.mpr (hK N₀))

theorem injective_iff_divergent {M : ℕ} :
    Function.Injective (orbit M) ↔ DivergentOrbit M :=
  ⟨divergent_of_injective, injective_of_divergent⟩

/-- **The `←` direction of the headline theorem.** A zero-confined positive odd seed has a
divergent orbit. -/
theorem divergent_of_zeroConfined {m : ℕ} (hm : Odd m) (hzc : ZeroConfined m) :
    DivergentOrbit m :=
  divergent_of_injective (injective_of_zeroConfined hm hzc)

end Divergence
