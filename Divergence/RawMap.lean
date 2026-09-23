import Divergence.CycleDrift

/-!
# The raw map, the Terras shift, and the bridge to the accelerated map

The windowed sparsity argument of M4 lives over the **raw** map

```
U n = n / 2          (n even),      U n = (3n+1) / 2      (n odd),
```

not over the accelerated `T`. This file develops what that argument needs:

* the **shift lemma** (Terras; Garcia–Tal Lemma 1), proved as an invariant for every `j ≤ N`
  rather than only at the endpoint, with parity preservation falling out as a corollary;
* **prefix injectivity** in congruence form — equal parity prefixes force `n ≡ n' [MOD 2^N]`;
* the **raw aggregate identity** `2^N · U^N n = 3^m · n + E N n` and the **contraction**
  bound (Curry Lemma 2.2) `2^N · U^N n < 3^m · (n + 2^N)`;
* the **bridge** `orbit M n = U^[S M n] M` for odd `M`, so the accelerated value set embeds
  in the raw one;
* **collision-freeness** of a divergent orbit's raw value set — the interface M4 consumes.

The parity prefix is exposed as a `Finset` (`parityPrefix`) with `oddCount` its cardinality, so
that M4's heavy case is a count of subsets of `range N` and nothing more.

No `sorry`, `admit`, `axiom`, or `opaque`.
-/

namespace Divergence

open Finset

/-! ## 1. The raw map and the parity prefix -/

/-- The raw `3x+1` map: `n/2` on even input, `(3n+1)/2` on odd input. -/
def U (n : ℕ) : ℕ := if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

theorem U_of_even {n : ℕ} (h : n % 2 = 0) : U n = n / 2 := by
  simp [U, h]

theorem U_of_odd {n : ℕ} (h : n % 2 = 1) : U n = (3 * n + 1) / 2 := by
  simp [U, h]

theorem two_mul_U_of_even {n : ℕ} (h : n % 2 = 0) : 2 * U n = n := by
  rw [U_of_even h]; omega

theorem two_mul_U_of_odd {n : ℕ} (h : n % 2 = 1) : 2 * U n = 3 * n + 1 := by
  rw [U_of_odd h]; omega

/-- The **parity prefix** of `n` at length `N`: the set of times `j < N` at which the raw
orbit of `n` is odd. M4's heavy case counts these as subsets of `range N`. -/
def parityPrefix (N n : ℕ) : Finset ℕ := (range N).filter (fun j => U^[j] n % 2 = 1)

/-- `oddCount N n` = number of odd values among `U^[j] n` for `j < N`. -/
def oddCount (N n : ℕ) : ℕ := (parityPrefix N n).card

theorem oddCount_eq_card (N n : ℕ) : oddCount N n = (parityPrefix N n).card := rfl

theorem parityPrefix_subset (N n : ℕ) : parityPrefix N n ⊆ range N :=
  Finset.filter_subset _ _

theorem oddCount_eq_sum (N n : ℕ) :
    oddCount N n = ∑ j ∈ range N, (if U^[j] n % 2 = 1 then 1 else 0) := by
  unfold oddCount parityPrefix
  exact Finset.card_filter _ _

@[simp] theorem oddCount_zero (n : ℕ) : oddCount 0 n = 0 := by
  simp [oddCount_eq_sum]

/-- Peeling the **last** step. -/
theorem oddCount_succ (N n : ℕ) :
    oddCount (N + 1) n = oddCount N n + (if U^[N] n % 2 = 1 then 1 else 0) := by
  rw [oddCount_eq_sum, oddCount_eq_sum, Finset.sum_range_succ]

/-- Peeling the **first** step — the form every induction below uses. -/
theorem oddCount_succ_left (N n : ℕ) :
    oddCount (N + 1) n = (if n % 2 = 1 then 1 else 0) + oddCount N (U n) := by
  rw [oddCount_eq_sum, oddCount_eq_sum, Finset.sum_range_succ']
  simp only [Function.iterate_succ_apply, Function.iterate_zero_apply]
  exact Nat.add_comm _ _

theorem oddCount_le (N n : ℕ) : oddCount N n ≤ N := by
  calc oddCount N n ≤ (range N).card := Finset.card_le_card (parityPrefix_subset N n)
    _ = N := Finset.card_range N

/-! ## 2. The shift lemma (Terras; Garcia–Tal Lemma 1) -/

/-- **Shift, as an invariant.** For every `j ≤ N`, adding `r·2^N` to the seed displaces the
`j`-th raw iterate by exactly `r · 3^{oddCount j n} · 2^{N-j}`. -/
theorem U_iter_shift (n r N : ℕ) : ∀ j ≤ N,
    U^[j] (n + r * 2 ^ N) = U^[j] n + r * 3 ^ oddCount j n * 2 ^ (N - j) := by
  intro j
  induction j with
  | zero => intro _; simp
  | succ j ih =>
    intro hj
    have hjN : j < N := by omega
    have hprev := ih (by omega)
    -- the displacement at time `j` is even, since `N - j ≥ 1`
    have hsplit : (2 : ℕ) ^ (N - j) = 2 * 2 ^ (N - (j + 1)) := by
      rw [← pow_succ']
      congr 1
      omega
    set d := r * 3 ^ oddCount j n * 2 ^ (N - (j + 1)) with hd
    have hc : r * 3 ^ oddCount j n * 2 ^ (N - j) = 2 * d := by
      rw [hsplit, hd]; ring
    rw [Function.iterate_succ_apply', Function.iterate_succ_apply', hprev, hc]
    by_cases hpar : U^[j] n % 2 = 1
    · -- odd step: the displacement is multiplied by 3
      have hoc : oddCount (j + 1) n = oddCount j n + 1 := by
        simp [oddCount_succ, hpar]
      have hsum : (U^[j] n + 2 * d) % 2 = 1 := by omega
      rw [U_of_odd hsum, U_of_odd hpar, hoc]
      have hexp : r * 3 ^ (oddCount j n + 1) * 2 ^ (N - (j + 1)) = 3 * d := by
        rw [hd, pow_succ]; ring
      rw [hexp]
      omega
    · -- even step: the displacement is halved
      have hpar0 : U^[j] n % 2 = 0 := by omega
      have hoc : oddCount (j + 1) n = oddCount j n := by
        simp [oddCount_succ, hpar]
      have hsum : (U^[j] n + 2 * d) % 2 = 0 := by omega
      rw [U_of_even hsum, U_of_even hpar0, hoc, ← hd]
      omega

/-- Parity is preserved along the whole prefix — a corollary of the displacement being even. -/
theorem U_iter_shift_parity (n r N : ℕ) {j : ℕ} (hj : j < N) :
    U^[j] (n + r * 2 ^ N) % 2 = U^[j] n % 2 := by
  have h := U_iter_shift n r N j (by omega)
  have hdvd : (2 : ℕ) ∣ r * 3 ^ oddCount j n * 2 ^ (N - j) :=
    Dvd.dvd.mul_left (dvd_pow_self 2 (by omega)) _
  omega

theorem oddCount_shift (n r N : ℕ) : oddCount N (n + r * 2 ^ N) = oddCount N n := by
  rw [oddCount_eq_sum, oddCount_eq_sum]
  refine Finset.sum_congr rfl fun j hj => ?_
  rw [U_iter_shift_parity n r N (Finset.mem_range.mp hj)]

/-- **The Terras / Garcia–Tal endpoint**, as a corollary. -/
theorem U_iter_shift_endpoint (n r N : ℕ) :
    U^[N] (n + r * 2 ^ N) = U^[N] n + r * 3 ^ oddCount N n := by
  have h := U_iter_shift n r N N (le_refl N)
  simpa using h

/-! ## 3. Prefix injectivity -/

/-- **Equal parity prefixes force a congruence.** No bound on `n, n'` is needed. -/
theorem modEq_of_parity_prefix (N : ℕ) : ∀ n n' : ℕ,
    (∀ j < N, U^[j] n % 2 = U^[j] n' % 2) → n ≡ n' [MOD 2 ^ N] := by
  induction N with
  | zero => intro n n' _; simpa using (Nat.modEq_one)
  | succ N ih =>
    intro n n' h
    have h0 : n % 2 = n' % 2 := by
      have := h 0 (by omega); simpa using this
    have hstep : ∀ j < N, U^[j] (U n) % 2 = U^[j] (U n') % 2 := by
      intro j hj
      have := h (j + 1) (by omega)
      rwa [Function.iterate_succ_apply, Function.iterate_succ_apply] at this
    have hUU : U n ≡ U n' [MOD 2 ^ N] := ih (U n) (U n') hstep
    have hmul : 2 * U n ≡ 2 * U n' [MOD 2 ^ (N + 1)] := by
      have := hUU.mul_left' (c := 2)
      rwa [pow_succ']
    by_cases hpar : n % 2 = 1
    · have hn' : n' % 2 = 1 := by omega
      rw [two_mul_U_of_odd hpar, two_mul_U_of_odd hn'] at hmul
      -- `3n + 1 ≡ 3n' + 1` cancels to `3n ≡ 3n'`, and `3` is invertible mod `2^{N+1}`
      have h3 : 3 * n ≡ 3 * n' [MOD 2 ^ (N + 1)] := by
        exact (Nat.ModEq.add_right_cancel' 1 hmul)
      have hcop : Nat.gcd (2 ^ (N + 1)) 3 = 1 := Nat.Coprime.pow_left _ (by decide)
      exact Nat.ModEq.cancel_left_of_coprime hcop h3
    · have hn0 : n % 2 = 0 := by omega
      have hn' : n' % 2 = 0 := by omega
      rwa [two_mul_U_of_even hn0, two_mul_U_of_even hn'] at hmul

/-- The `Finset` form M4 uses. -/
theorem modEq_of_parityPrefix_eq {N n n' : ℕ} (h : parityPrefix N n = parityPrefix N n') :
    n ≡ n' [MOD 2 ^ N] := by
  refine modEq_of_parity_prefix N n n' fun j hj => ?_
  have hmem : (j ∈ parityPrefix N n) ↔ (j ∈ parityPrefix N n') := by rw [h]
  simp only [parityPrefix, Finset.mem_filter, Finset.mem_range] at hmem
  have h1 : U^[j] n % 2 < 2 := Nat.mod_lt _ (by norm_num)
  have h2 : U^[j] n' % 2 < 2 := Nat.mod_lt _ (by norm_num)
  by_cases hc : U^[j] n % 2 = 1
  · have := (hmem.mp ⟨hj, hc⟩).2; omega
  · by_cases hc' : U^[j] n' % 2 = 1
    · have := (hmem.mpr ⟨hj, hc'⟩).2; omega
    · omega

/-! ## 4. The raw aggregate identity and the contraction bound -/

/-- The raw carry, from the aggregate identity below. -/
def E : ℕ → ℕ → ℕ
  | 0, _ => 0
  | N + 1, n => if n % 2 = 0 then 2 * E N (U n)
                else 3 ^ oddCount N (U n) + 2 * E N (U n)

@[simp] theorem E_zero (n : ℕ) : E 0 n = 0 := rfl

theorem E_succ (N n : ℕ) :
    E (N + 1) n = if n % 2 = 0 then 2 * E N (U n)
                  else 3 ^ oddCount N (U n) + 2 * E N (U n) := rfl

theorem E_succ_even {n : ℕ} (h : n % 2 = 0) (N : ℕ) : E (N + 1) n = 2 * E N (U n) := by
  rw [E_succ]; simp [h]

theorem E_succ_odd {n : ℕ} (h : n % 2 = 1) (N : ℕ) :
    E (N + 1) n = 3 ^ oddCount N (U n) + 2 * E N (U n) := by
  rw [E_succ]; simp [h]

/-- **The raw aggregate identity.** `2^N · U^N n = 3^m · n + E N n`, `m = oddCount N n`. -/
theorem raw_aggregate_identity : ∀ (N n : ℕ),
    2 ^ N * U^[N] n = 3 ^ oddCount N n * n + E N n := by
  intro N
  induction N with
  | zero => intro n; simp
  | succ N ih =>
    intro n
    rw [Function.iterate_succ_apply, oddCount_succ_left]
    by_cases hpar : n % 2 = 1
    · rw [show (if n % 2 = 1 then 1 else 0) = 1 from by simp [hpar], E_succ_odd hpar]
      have key : 2 ^ (N + 1) * U^[N] (U n) = 2 * (2 ^ N * U^[N] (U n)) := by ring
      rw [key, ih (U n)]
      have h2 : 2 * (3 ^ oddCount N (U n) * U n + E N (U n))
          = 3 ^ oddCount N (U n) * (2 * U n) + 2 * E N (U n) := by ring
      rw [h2, two_mul_U_of_odd hpar, pow_add]
      ring
    · have hpar0 : n % 2 = 0 := by omega
      rw [show (if n % 2 = 1 then 1 else 0) = 0 from by simp [hpar], E_succ_even hpar0,
        Nat.zero_add]
      have key : 2 ^ (N + 1) * U^[N] (U n) = 2 * (2 ^ N * U^[N] (U n)) := by ring
      rw [key, ih (U n)]
      have h2 : 2 * (3 ^ oddCount N (U n) * U n + E N (U n))
          = 3 ^ oddCount N (U n) * (2 * U n) + 2 * E N (U n) := by ring
      rw [h2, two_mul_U_of_even hpar0]

theorem E_eq_zero : ∀ (N n : ℕ), oddCount N n = 0 → E N n = 0 := by
  intro N
  induction N with
  | zero => intro n _; rfl
  | succ N ih =>
    intro n h
    rw [oddCount_succ_left] at h
    have hpar : n % 2 = 0 := by
      by_contra hc
      have h1 : n % 2 = 1 := by omega
      rw [show (if n % 2 = 1 then 1 else 0) = 1 from by simp [h1]] at h
      omega
    rw [E_succ_even hpar]
    rw [show (if n % 2 = 1 then 1 else 0) = 0 from by simp [hpar], Nat.zero_add] at h
    rw [ih (U n) h, Nat.mul_zero]

theorem E_lt : ∀ (N n : ℕ), E N n < 3 ^ oddCount N n * 2 ^ N := by
  intro N
  induction N with
  | zero => intro n; simp
  | succ N ih =>
    intro n
    rw [oddCount_succ_left]
    have hpos : 0 < 3 ^ oddCount N (U n) := pow_pos (by norm_num) _
    by_cases hpar : n % 2 = 1
    · rw [show (if n % 2 = 1 then 1 else 0) = 1 from by simp [hpar], E_succ_odd hpar,
        pow_add, pow_one]
      have h1 := ih (U n)
      have hexp : 3 ^ 1 * 3 ^ oddCount N (U n) * 2 ^ (N + 1)
          = 3 ^ oddCount N (U n) * (3 * (2 * 2 ^ N)) := by rw [pow_one]; ring
      calc 3 ^ oddCount N (U n) + 2 * E N (U n)
          < 3 ^ oddCount N (U n) + 2 * (3 ^ oddCount N (U n) * 2 ^ N) := by omega
        _ ≤ 3 ^ oddCount N (U n) * (3 * (2 * 2 ^ N)) := by nlinarith [pow_pos (show 0 < 2 by norm_num) N]
        _ = 3 ^ 1 * 3 ^ oddCount N (U n) * 2 ^ (N + 1) := hexp.symm
    · rw [show (if n % 2 = 1 then 1 else 0) = 0 from by simp [hpar], Nat.zero_add,
        E_succ_even (by omega)]
      have h1 := ih (U n)
      have hexp : 3 ^ oddCount N (U n) * 2 ^ (N + 1)
          = 2 * (3 ^ oddCount N (U n) * 2 ^ N) := by ring
      omega

/-- **Curry Lemma 2.2, cleared of division.** -/
theorem contraction (N n : ℕ) :
    2 ^ N * U^[N] n < 3 ^ oddCount N n * (n + 2 ^ N) := by
  have hid := raw_aggregate_identity N n
  have hE := E_lt N n
  have hexp : 3 ^ oddCount N n * (n + 2 ^ N)
      = 3 ^ oddCount N n * n + 3 ^ oddCount N n * 2 ^ N := by ring
  omega

/-! ## 5. The bridge to the accelerated map -/

theorem U_iter_two_pow_mul : ∀ (k y : ℕ), U^[k] (2 ^ k * y) = y := by
  intro k
  induction k with
  | zero => intro y; simp
  | succ k ih =>
    intro y
    rw [Function.iterate_succ_apply]
    have heven : (2 ^ (k + 1) * y) % 2 = 0 := by
      have : 2 ^ (k + 1) * y = 2 * (2 ^ k * y) := by ring
      omega
    rw [U_of_even heven]
    have hhalf : 2 ^ (k + 1) * y / 2 = 2 ^ k * y := by
      have : 2 ^ (k + 1) * y = 2 * (2 ^ k * y) := by ring
      omega
    rw [hhalf, ih y]

/-- One accelerated step is `a x` raw steps. `Odd x` is essential: for even `x` the accelerated
step has `a x = 0` while `U` still halves. -/
theorem U_iter_a_eq_T {x : ℕ} (hx : Odd x) : U^[a x] x = T x := by
  have hv : 1 ≤ a x := a_pos hx
  have hxodd : x % 2 = 1 := Nat.odd_iff.mp hx
  have hstep : 2 * U x = 3 * x + 1 := two_mul_U_of_odd hxodd
  have hT : 2 ^ a x * T x = 3 * x + 1 := two_pow_a_mul_T x
  have hUx : U x = 2 ^ (a x - 1) * T x := by
    have hsplit : (2 : ℕ) ^ a x = 2 * 2 ^ (a x - 1) := by
      rw [← pow_succ']
      congr 1
      omega
    rw [hsplit, mul_assoc] at hT
    omega
  have hiter : a x = (a x - 1) + 1 := by omega
  rw [hiter, Function.iterate_succ_apply, hUx, U_iter_two_pow_mul]

/-- **The bridge.** The accelerated orbit is the raw orbit sampled at the times `S M n`. -/
theorem bridge {M : ℕ} (hM : Odd M) : ∀ n, orbit M n = U^[S M n] M := by
  intro n
  induction n with
  | zero => simp
  | succ n ih =>
    have hcomm : S M (n + 1) = a (orbit M n) + S M n := by
      rw [S_succ]; omega
    rw [orbit_succ, hcomm, Function.iterate_add_apply, ← ih,
        U_iter_a_eq_T (odd_orbit hM n)]

theorem orbit_range_subset {M : ℕ} (hM : Odd M) :
    Set.range (orbit M) ⊆ Set.range (fun k => U^[k] M) := by
  rintro _ ⟨n, rfl⟩
  exact ⟨S M n, (bridge hM n).symm⟩

/-! ## 6. Collision-freeness — the M4 interface -/

/-- `A` is **collision-free** for `U`: distinct elements never merge under a common iterate. -/
def CollisionFree (A : Set ℕ) : Prop :=
  ∀ u ∈ A, ∀ v ∈ A, ∀ j, U^[j] u = U^[j] v → u = v

/-- A raw repeat makes the raw orbit eventually periodic, hence bounded. -/
private theorem raw_bounded_of_repeat {M i k : ℕ} (hik : i < k) (hrep : U^[i] M = U^[k] M) :
    ∀ j, U^[j] M ≤ (range k).sup (fun j => U^[j] M) := by
  intro j
  induction j using Nat.strong_induction_on with
  | _ j ih =>
    by_cases hj : j < k
    · exact Finset.le_sup (f := fun j => U^[j] M) (Finset.mem_range.mpr hj)
    · have hjk : k ≤ j := Nat.not_lt.mp hj
      have hshift : U^[j] M = U^[j - (k - i)] M := by
        have h1 : j = (j - k) + k := by omega
        have h2 : j - (k - i) = (j - k) + i := by omega
        rw [h2]
        conv_lhs => rw [h1]
        rw [Function.iterate_add_apply, Function.iterate_add_apply, hrep]
      rw [hshift]
      exact ih _ (by omega)

/-- **The M4 interface.** A divergent accelerated orbit has an injective raw orbit, whose value
set is collision-free. -/
theorem raw_injective_of_divergent {M : ℕ} (hM : Odd M) (hdiv : DivergentOrbit M) :
    Function.Injective (fun k => U^[k] M) ∧
      CollisionFree (Set.range (fun k => U^[k] M)) := by
  have hinj : Function.Injective (fun k => U^[k] M) := by
    intro i k hrep
    by_contra hne
    have key : ∃ B, ∀ j, U^[j] M ≤ B := by
      rcases Nat.lt_trichotomy i k with h | h | h
      · exact ⟨_, raw_bounded_of_repeat h hrep⟩
      · exact absurd h hne
      · exact ⟨_, raw_bounded_of_repeat h hrep.symm⟩
    obtain ⟨B, hB⟩ := key
    obtain ⟨N₀, hN₀⟩ := hdiv B
    have hlt := hN₀ N₀ le_rfl
    rw [bridge hM N₀] at hlt
    exact absurd hlt (not_lt.mpr (hB (S M N₀)))
  refine ⟨hinj, ?_⟩
  rintro _ ⟨i, rfl⟩ _ ⟨k, rfl⟩ j hcol
  simp only at hcol
  rw [← Function.iterate_add_apply, ← Function.iterate_add_apply] at hcol
  have : j + i = j + k := hinj hcol
  have hik : i = k := by omega
  rw [hik]

end Divergence
