import Mathlib.Analysis.SpecialFunctions.BinaryEntropy
import Mathlib.Data.Nat.Choose.Sum

/-!
# Two-sided entropy estimate for binomial coefficients

Mathlib's `Nat.pow_le_choose` is far too weak for counting confined words. This file ports the
classical max-term argument from `eoc-lean-verification`'s `EOC/BinomialEntropy.lean` and packages
it as the single two-sided estimate O3 consumes:

```
|log C(n,k) − n·H(k/n)| ≤ log (n+1)          (`abs_log_choose_sub_le`)
```

together with the sharper one-sided form `log C(n,k) ≤ n·H(k/n)` (`log_choose_le`), which loses
no `log (n+1)` and is what the upper bound uses.

Entropy is in **nats** throughout (`Real.binEntropy`); O3 divides by `Real.log 2` where bits are
wanted.

The endpoints `k = 0` and `k = n` are split out explicitly in `log_weight_eq`: there the identity
`p^k q^{n-k} = exp(−n·H(p))` holds only because Lean's conventions `0^0 = 1` and `log 0 = 0`
line up, and the interior argument (which needs `0 < p < 1`) does not apply.

No `sorry`, `admit`, `axiom`, or `opaque`.
-/

namespace Occupation

open Finset

variable {p q : ℝ}

/-! ## 1. The binomial terms -/

/-- The terms of the binomial distribution. -/
noncomputable def term (n : ℕ) (p q : ℝ) (j : ℕ) : ℝ := (n.choose j : ℝ) * p ^ j * q ^ (n - j)

theorem term_nonneg (hp : 0 ≤ p) (hq : 0 ≤ q) (n j : ℕ) : 0 ≤ term n p q j := by
  unfold term; positivity

/-- **The weighted binomial identity.** -/
theorem sum_term_eq_one (n : ℕ) (hpq : p + q = 1) :
    ∑ j ∈ range (n + 1), term n p q j = 1 := by
  have h := add_pow p q n
  rw [hpq, one_pow] at h
  have hrw : ∑ j ∈ range (n + 1), term n p q j
      = ∑ m ∈ range (n + 1), p ^ m * q ^ (n - m) * (n.choose m : ℝ) := by
    refine sum_congr rfl fun j _ => ?_
    unfold term
    ring
  rw [hrw, ← h]

/-- **Upper bound.** A single term is at most the whole sum. No `0 < n` is needed. -/
theorem choose_mul_le_one {n k : ℕ} (hk : k ≤ n) (hp : 0 ≤ p) (hq : 0 ≤ q) (hpq : p + q = 1) :
    (n.choose k : ℝ) * p ^ k * q ^ (n - k) ≤ 1 := by
  have hsum := sum_term_eq_one (p := p) (q := q) n hpq
  have hmem : k ∈ range (n + 1) := mem_range.mpr (by omega)
  have := Finset.single_le_sum (f := fun j => term n p q j)
    (fun j _ => term_nonneg hp hq n j) hmem
  rw [hsum] at this
  exact this

/-- **Division-free recurrence.** -/
theorem term_succ_mul (n j : ℕ) (hj : j < n) (p q : ℝ) :
    term n p q (j + 1) * (((j : ℝ) + 1) * q) = term n p q j * (((n : ℝ) - j) * p) := by
  unfold term
  have hrec : n.choose (j + 1) * (j + 1) = n.choose j * (n - j) := Nat.choose_succ_right_eq n j
  have hrec' : ((n.choose (j + 1) : ℝ)) * ((j : ℝ) + 1)
      = (n.choose j : ℝ) * ((n : ℝ) - (j : ℝ)) := by
    have hc := congrArg (fun m : ℕ => (m : ℝ)) hrec
    push_cast [Nat.cast_sub hj.le] at hc
    linarith
  have hq : q ^ (n - (j + 1)) * q = q ^ (n - j) := by
    rw [← pow_succ]
    congr 1
    omega
  calc (n.choose (j + 1) : ℝ) * p ^ (j + 1) * q ^ (n - (j + 1)) * (((j : ℝ) + 1) * q)
      = ((n.choose (j + 1) : ℝ) * ((j : ℝ) + 1)) * p ^ j * p * (q ^ (n - (j + 1)) * q) := by
        rw [pow_succ]; ring
    _ = ((n.choose j : ℝ) * ((n : ℝ) - (j : ℝ))) * p ^ j * p * q ^ (n - j) := by rw [hrec', hq]
    _ = (n.choose j : ℝ) * p ^ j * q ^ (n - j) * (((n : ℝ) - j) * p) := by ring

/-! ## 2. The maximum term is at `j = k` -/

section Ratio

variable (n k j : ℕ)

private theorem cast_pos (hk0 : 0 < k) (hkn : k < n) : (0 : ℝ) < n := by
  have : 0 < n := by omega
  exact_mod_cast this

theorem term_le_succ (hk0 : 0 < k) (hkn : k < n) (hjk : j < k)
    (hp : p = (k : ℝ) / n) (hq : q = ((n : ℝ) - k) / n) :
    term n p q j ≤ term n p q (j + 1) := by
  have hn0 : (0 : ℝ) < n := cast_pos n k hk0 hkn
  have hkn' : (k : ℝ) < n := by exact_mod_cast hkn
  have hjn : j < n := by omega
  have hjk' : (j : ℝ) + 1 ≤ (k : ℝ) := by exact_mod_cast hjk
  have hp0 : 0 < p := by rw [hp]; positivity
  have hq0 : 0 < q := by rw [hq]; exact div_pos (by linarith) hn0
  have hrec := term_succ_mul n j hjn p q
  have hTj : 0 ≤ term n p q j := term_nonneg hp0.le hq0.le n j
  have hA : (0 : ℝ) < ((j : ℝ) + 1) * q := by positivity
  have hkey : ((j : ℝ) + 1) * q ≤ ((n : ℝ) - j) * p := by
    have e1 : ((j : ℝ) + 1) * q = (((j : ℝ) + 1) * ((n : ℝ) - k)) / n := by rw [hq]; ring
    have e2 : ((n : ℝ) - j) * p = (((n : ℝ) - j) * (k : ℝ)) / n := by rw [hp]; ring
    have hjn' : (j : ℝ) < n := by exact_mod_cast hjn
    have hnum : ((j : ℝ) + 1) * ((n : ℝ) - k) ≤ ((n : ℝ) - j) * (k : ℝ) := by
      nlinarith [mul_le_mul_of_nonneg_left hjk' hn0.le]
    rw [e1, e2]
    gcongr
  have hstep : term n p q j * (((j : ℝ) + 1) * q) ≤ term n p q (j + 1) * (((j : ℝ) + 1) * q) := by
    calc term n p q j * (((j : ℝ) + 1) * q)
        ≤ term n p q j * (((n : ℝ) - j) * p) := mul_le_mul_of_nonneg_left hkey hTj
      _ = term n p q (j + 1) * (((j : ℝ) + 1) * q) := hrec.symm
  exact le_of_mul_le_mul_right hstep hA

theorem term_succ_le (hk0 : 0 < k) (hkn : k < n) (hkj : k ≤ j) (hjn : j < n)
    (hp : p = (k : ℝ) / n) (hq : q = ((n : ℝ) - k) / n) :
    term n p q (j + 1) ≤ term n p q j := by
  have hn0 : (0 : ℝ) < n := cast_pos n k hk0 hkn
  have hkn' : (k : ℝ) < n := by exact_mod_cast hkn
  have hjn' : (j : ℝ) < n := by exact_mod_cast hjn
  have hkj' : (k : ℝ) ≤ (j : ℝ) := by exact_mod_cast hkj
  have hp0 : 0 < p := by rw [hp]; positivity
  have hq0 : 0 < q := by rw [hq]; exact div_pos (by linarith) hn0
  have hrec := term_succ_mul n j hjn p q
  have hTj1 : 0 ≤ term n p q (j + 1) := term_nonneg hp0.le hq0.le n (j + 1)
  have hB : (0 : ℝ) < ((n : ℝ) - j) * p := mul_pos (by linarith) hp0
  have hkey : ((n : ℝ) - j) * p ≤ ((j : ℝ) + 1) * q := by
    have e1 : ((j : ℝ) + 1) * q = (((j : ℝ) + 1) * ((n : ℝ) - k)) / n := by rw [hq]; ring
    have e2 : ((n : ℝ) - j) * p = (((n : ℝ) - j) * (k : ℝ)) / n := by rw [hp]; ring
    have hnum : ((n : ℝ) - j) * (k : ℝ) ≤ ((j : ℝ) + 1) * ((n : ℝ) - k) := by
      nlinarith [mul_le_mul_of_nonneg_left hkj' hn0.le]
    rw [e1, e2]
    gcongr
  have hstep : term n p q (j + 1) * (((n : ℝ) - j) * p)
      ≤ term n p q j * (((n : ℝ) - j) * p) := by
    calc term n p q (j + 1) * (((n : ℝ) - j) * p)
        ≤ term n p q (j + 1) * (((j : ℝ) + 1) * q) := mul_le_mul_of_nonneg_left hkey hTj1
      _ = term n p q j * (((n : ℝ) - j) * p) := hrec
  exact le_of_mul_le_mul_right hstep hB

end Ratio

/-- **The maximum of the binomial terms is at `j = k`.** Stated in the interior: the endpoints
are handled directly by the consumer. -/
theorem term_le_term_max (n k : ℕ) (hk0 : 0 < k) (hkn : k < n)
    (hp : p = (k : ℝ) / n) (hq : q = ((n : ℝ) - k) / n) :
    ∀ j ≤ n, term n p q j ≤ term n p q k := by
  intro j hj
  rcases le_or_gt j k with hjk | hjk
  · have aux : ∀ d : ℕ, ∀ i : ℕ, i + d = k → term n p q i ≤ term n p q k := by
      intro d
      induction d with
      | zero => intro i hi; rw [show i = k by omega]
      | succ d ih =>
        intro i hi
        have h1 : term n p q i ≤ term n p q (i + 1) :=
          term_le_succ n k i hk0 hkn (by omega) hp hq
        exact le_trans h1 (ih (i + 1) (by omega))
    exact aux (k - j) j (by omega)
  · have aux : ∀ d : ℕ, ∀ i : ℕ, k + d = i → i ≤ n → term n p q i ≤ term n p q k := by
      intro d
      induction d with
      | zero => intro i hi _; rw [show i = k by omega]
      | succ d ih =>
        intro i hi hin
        have hprev : term n p q (k + d + 1) ≤ term n p q (k + d) :=
          term_succ_le n k (k + d) hk0 hkn (by omega) (by omega) hp hq
        have hrest := ih (k + d) rfl (by omega)
        rw [show i = k + d + 1 by omega]
        exact le_trans hprev hrest
    exact aux (j - k) j (by omega) hj

/-! ## 3. The lower bound -/

/-- At either endpoint the weight is `1` — here `0^0 = 1` is doing the work. -/
theorem weight_eq_one {n k : ℕ} (hn : 0 < n) (h : k = 0 ∨ k = n) :
    ((k : ℝ) / n) ^ k * (1 - (k : ℝ) / n) ^ (n - k) = 1 := by
  rcases h with h0 | hkn
  · subst h0; simp
  · subst hkn
    have hkne : (k : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr (by omega)
    have hkk : (k : ℝ) / (k : ℝ) = 1 := div_self hkne
    rw [Nat.sub_self, pow_zero, hkk, one_pow, mul_one]

/-- **Binomial entropy bound, division-free.** Endpoints included. -/
theorem one_le_succ_mul_choose_mul {n k : ℕ} (hk : k ≤ n) (hn : 0 < n) :
    (1 : ℝ) ≤ ((n : ℝ) + 1) * (n.choose k : ℝ)
      * ((k : ℝ) / n) ^ k * (1 - (k : ℝ) / n) ^ (n - k) := by
  have hn0 : (0 : ℝ) < n := by exact_mod_cast hn
  have hform : ((n : ℝ) + 1) * (n.choose k : ℝ) * ((k : ℝ) / n) ^ k
        * (1 - (k : ℝ) / n) ^ (n - k)
      = ((n : ℝ) + 1) * (n.choose k : ℝ)
        * (((k : ℝ) / n) ^ k * (1 - (k : ℝ) / n) ^ (n - k)) := by ring
  rw [hform]
  rcases Nat.eq_zero_or_pos k with hk0 | hk0
  · rw [weight_eq_one hn (Or.inl hk0), hk0, Nat.choose_zero_right]
    push_cast
    linarith
  rcases eq_or_lt_of_le hk with heq | hkn
  · rw [weight_eq_one hn (Or.inr heq), heq, Nat.choose_self]
    push_cast
    linarith
  · -- interior: the max-term argument
    set pp : ℝ := (k : ℝ) / n with hpp
    have hpq : pp + (1 - pp) = 1 := by ring
    have hqval : (1 : ℝ) - pp = ((n : ℝ) - k) / n := by
      rw [hpp]
      field_simp
    have hsum := sum_term_eq_one (p := pp) (q := 1 - pp) n hpq
    have hmax := term_le_term_max (p := pp) (q := 1 - pp) n k hk0 hkn hpp hqval
    have hbound : (1 : ℝ) ≤ ((n : ℝ) + 1) * term n pp (1 - pp) k := by
      calc (1 : ℝ) = ∑ j ∈ range (n + 1), term n pp (1 - pp) j := hsum.symm
        _ ≤ ∑ _j ∈ range (n + 1), term n pp (1 - pp) k :=
            sum_le_sum fun j hj => hmax j (by have := mem_range.mp hj; omega)
        _ = ((n : ℝ) + 1) * term n pp (1 - pp) k := by
            rw [sum_const, card_range, nsmul_eq_mul]
            push_cast
            ring
    unfold term at hbound
    calc (1 : ℝ) ≤ ((n : ℝ) + 1) * ((n.choose k : ℝ) * pp ^ k * (1 - pp) ^ (n - k)) := hbound
      _ = ((n : ℝ) + 1) * (n.choose k : ℝ) * (pp ^ k * (1 - pp) ^ (n - k)) := by ring

/-! ## 4. The entropy identity and the two-sided estimate -/

/-- The weight is positive, endpoints included. -/
theorem weight_pos {n k : ℕ} (hk : k ≤ n) (hn : 0 < n) :
    0 < ((k : ℝ) / n) ^ k * (1 - (k : ℝ) / n) ^ (n - k) := by
  have hn0 : (0 : ℝ) < n := by exact_mod_cast hn
  rcases Nat.eq_zero_or_pos k with hk0 | hk0
  · rw [weight_eq_one hn (Or.inl hk0)]; norm_num
  rcases eq_or_lt_of_le hk with heq | hkn
  · rw [weight_eq_one hn (Or.inr heq)]; norm_num
  · have hp0 : (0 : ℝ) < (k : ℝ) / n := by
      have : (0 : ℝ) < k := by exact_mod_cast hk0
      positivity
    have hq0 : (0 : ℝ) < 1 - (k : ℝ) / n := by
      have hkn' : (k : ℝ) < n := by exact_mod_cast hkn
      rw [sub_pos, div_lt_one hn0]
      exact hkn'
    positivity

/-- **The entropy identity** `p^k q^{n-k} = exp(−n·H(p))` at `p = k/n`, in log form. The
endpoints are split out: there it holds only because `0^0 = 1` and `log 0 = 0` line up. -/
theorem log_weight_eq {n k : ℕ} (hk : k ≤ n) (hn : 0 < n) :
    Real.log (((k : ℝ) / n) ^ k * (1 - (k : ℝ) / n) ^ (n - k))
      = -(n : ℝ) * Real.binEntropy ((k : ℝ) / n) := by
  have hn0 : (0 : ℝ) < n := by exact_mod_cast hn
  rcases Nat.eq_zero_or_pos k with hk0 | hk0
  · rw [weight_eq_one hn (Or.inl hk0), hk0]
    simp
  rcases eq_or_lt_of_le hk with heq | hkn
  · rw [weight_eq_one hn (Or.inr heq)]
    have hone : (k : ℝ) / n = 1 := by
      rw [heq]
      have : (n : ℝ) ≠ 0 := ne_of_gt hn0
      field_simp
    rw [hone]
    simp
  · -- interior
    have hkn' : (k : ℝ) < n := by exact_mod_cast hkn
    have hk' : (0 : ℝ) < k := by exact_mod_cast hk0
    have hp0 : (0 : ℝ) < (k : ℝ) / n := by positivity
    have hq0 : (0 : ℝ) < 1 - (k : ℝ) / n := by
      rw [sub_pos, div_lt_one hn0]; exact hkn'
    rw [Real.log_mul (by positivity) (by positivity), Real.log_pow, Real.log_pow]
    rw [Real.binEntropy, Real.log_inv, Real.log_inv]
    have hnk : ((n - k : ℕ) : ℝ) = (n : ℝ) - k := by rw [Nat.cast_sub hk]
    rw [hnk]
    have e1 : (n : ℝ) * ((k : ℝ) / n) = (k : ℝ) := by field_simp
    have e2 : (n : ℝ) * (1 - (k : ℝ) / n) = (n : ℝ) - k := by field_simp
    have hexp : -(n : ℝ) * ((k : ℝ) / n * -Real.log ((k : ℝ) / n)
          + (1 - (k : ℝ) / n) * -Real.log (1 - (k : ℝ) / n))
        = ((n : ℝ) * ((k : ℝ) / n)) * Real.log ((k : ℝ) / n)
          + ((n : ℝ) * (1 - (k : ℝ) / n)) * Real.log (1 - (k : ℝ) / n) := by ring
    rw [hexp, e1, e2]

/-- **Upper bound in log form**, with no `log (n+1)` loss. -/
theorem log_choose_le {n k : ℕ} (hk : k ≤ n) (hn : 0 < n) :
    Real.log (n.choose k) ≤ (n : ℝ) * Real.binEntropy ((k : ℝ) / n) := by
  have hn0 : (0 : ℝ) < n := by exact_mod_cast hn
  have hcpos : (0 : ℝ) < (n.choose k : ℝ) := by
    exact_mod_cast Nat.choose_pos hk
  have hwpos := weight_pos hk hn
  have hp0 : (0 : ℝ) ≤ (k : ℝ) / n := by positivity
  have hq0 : (0 : ℝ) ≤ 1 - (k : ℝ) / n := by
    have hkn' : (k : ℝ) ≤ n := by exact_mod_cast hk
    rw [sub_nonneg, div_le_one hn0]
    exact hkn'
  have hle := choose_mul_le_one (p := (k : ℝ) / n) (q := 1 - (k : ℝ) / n) hk hp0 hq0 (by ring)
  have hprod : (n.choose k : ℝ) * (((k : ℝ) / n) ^ k * (1 - (k : ℝ) / n) ^ (n - k)) ≤ 1 := by
    calc (n.choose k : ℝ) * (((k : ℝ) / n) ^ k * (1 - (k : ℝ) / n) ^ (n - k))
        = (n.choose k : ℝ) * ((k : ℝ) / n) ^ k * (1 - (k : ℝ) / n) ^ (n - k) := by ring
      _ ≤ 1 := hle
  have hlog := Real.log_nonpos (by positivity) hprod
  rw [Real.log_mul (ne_of_gt hcpos) (ne_of_gt hwpos), log_weight_eq hk hn] at hlog
  linarith

/-- **The two-sided estimate O3 consumes**, in nats. -/
theorem abs_log_choose_sub_le {n k : ℕ} (hk : k ≤ n) (hn : 0 < n) :
    |Real.log (n.choose k) - (n : ℝ) * Real.binEntropy ((k : ℝ) / n)|
      ≤ Real.log ((n : ℝ) + 1) := by
  have hn0 : (0 : ℝ) < n := by exact_mod_cast hn
  have hcpos : (0 : ℝ) < (n.choose k : ℝ) := by exact_mod_cast Nat.choose_pos hk
  have hwpos := weight_pos hk hn
  have hupper := log_choose_le hk hn
  -- lower side, from the division-free bound
  have hlow := one_le_succ_mul_choose_mul hk hn
  have hrw : ((n : ℝ) + 1) * (n.choose k : ℝ) * ((k : ℝ) / n) ^ k * (1 - (k : ℝ) / n) ^ (n - k)
      = ((n : ℝ) + 1) * ((n.choose k : ℝ)
          * (((k : ℝ) / n) ^ k * (1 - (k : ℝ) / n) ^ (n - k))) := by ring
  rw [hrw] at hlow
  have hlog := Real.log_nonneg hlow
  rw [Real.log_mul (by positivity) (by positivity),
      Real.log_mul (ne_of_gt hcpos) (ne_of_gt hwpos), log_weight_eq hk hn] at hlog
  rw [abs_le]
  constructor
  · linarith
  · have : (0 : ℝ) ≤ Real.log ((n : ℝ) + 1) := Real.log_nonneg (by linarith)
    linarith

end Occupation
