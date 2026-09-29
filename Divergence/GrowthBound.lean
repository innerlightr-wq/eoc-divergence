import Divergence.RawMap

/-!
# The raw growth bound

One step of the raw map `U` multiplies `n + 1` by at most `3/2`. Iterating, in exact `ℕ` form
with no division and no real numbers:

```
2 ^ N * (U^[N] n + 1)  ≤  3 ^ N * (n + 1).
```

This is the Archimedean half of several route-closure records in the programme's audit layer
(`notes/CLOSED_POINTWISE_ROUTES_2026-09-29.md`): it is what caps the initial-square half-length
of an integer's parity word, what bounds the amortization integral on the orbits of interest, and
what forces the 3-adic endpoint representative of an exponent code to equal the orbit value. It
records a closure; it is not a separator, and it bears on neither `(DE)` nor the Collatz
conjecture.

It is stated for the **raw** map `U` of `Divergence.RawMap`, where the induction is one line per
parity branch. The accelerated orbit embeds in the raw one by `Divergence.bridge`.

Nothing here is new mathematics: `2 * U n ≤ 3 * n + 1` is immediate from the two branches of the
definition, and the estimate is the standard `(3/2)^t` bound. What is new is only that it is now
machine-checked for every `n` and every `N`.

No `sorry`, no `admit`, no added assumption.
-/

namespace Divergence

/-- **One raw step multiplies `n + 1` by at most `3/2`**, in exact `ℕ` form.

Both branches of `U` are handled by `omega` from the corresponding doubled identity: on even
input `2 * (U n + 1) = n + 2 ≤ 3 * (n + 1)`, and on odd input it is the equality
`2 * (U n + 1) = 3 * (n + 1)`. -/
theorem two_mul_U_succ_le (n : ℕ) : 2 * (U n + 1) ≤ 3 * (n + 1) := by
  rcases Nat.mod_two_eq_zero_or_one n with h | h
  · have h2 := two_mul_U_of_even h
    omega
  · have h2 := two_mul_U_of_odd h
    omega

/-- **The raw growth bound.** `2 ^ N * (U^[N] n + 1) ≤ 3 ^ N * (n + 1)` for every `n` and `N`.

Equivalently `U^[N] n + 1 ≤ (3/2) ^ N * (n + 1)`, stated without division so that it holds in
`ℕ` unconditionally. Proved by induction on `N` from `two_mul_U_succ_le`; the odd branch is an
equality, so the bound is attained exactly on the all-odd prefixes. -/
theorem two_pow_mul_iterate_succ_le (N n : ℕ) :
    2 ^ N * (U^[N] n + 1) ≤ 3 ^ N * (n + 1) := by
  induction N with
  | zero => simp
  | succ N ih =>
    calc 2 ^ (N + 1) * (U^[N + 1] n + 1)
        = 2 ^ N * (2 * (U (U^[N] n) + 1)) := by
          rw [Function.iterate_succ_apply']; ring
      _ ≤ 2 ^ N * (3 * (U^[N] n + 1)) :=
          Nat.mul_le_mul (le_refl _) (two_mul_U_succ_le _)
      _ = 3 * (2 ^ N * (U^[N] n + 1)) := by ring
      _ ≤ 3 * (3 ^ N * (n + 1)) := Nat.mul_le_mul (le_refl _) ih
      _ = 3 ^ (N + 1) * (n + 1) := by ring

/-- The start is bounded by the same expression, since `2 ^ N ≤ 3 ^ N`. -/
theorem two_pow_mul_succ_le (N n : ℕ) : 2 ^ N * (n + 1) ≤ 3 ^ N * (n + 1) :=
  Nat.mul_le_mul (Nat.pow_le_pow_left (Nat.le_succ 2) N) (le_refl _)

/-- **The form the initial-square cap consumes.** Both endpoints of a length-`N` raw window are
bounded together: `2 ^ N * (max n (U^[N] n) + 1) ≤ 3 ^ N * (n + 1)`.

A repetition argument needs the *larger* of the two endpoints, because a nonzero difference
divisible by `2 ^ N` forces `2 ^ N ≤ max n (U^[N] n)`. -/
theorem two_pow_mul_max_succ_le (N n : ℕ) :
    2 ^ N * (max n (U^[N] n) + 1) ≤ 3 ^ N * (n + 1) := by
  rcases Nat.le_total n (U^[N] n) with h | h
  · rw [Nat.max_eq_right h]; exact two_pow_mul_iterate_succ_le N n
  · rw [Nat.max_eq_left h]; exact two_pow_mul_succ_le N n

/-- A raw orbit value never exceeds `3 ^ N * (n + 1)`. -/
theorem iterate_lt_three_pow_mul_succ (N n : ℕ) : U^[N] n < 3 ^ N * (n + 1) :=
  Nat.lt_of_lt_of_le
    (Nat.lt_of_lt_of_le (Nat.lt_succ_self _)
      (Nat.le_mul_of_pos_left _ (Nat.two_pow_pos N)))
    (two_pow_mul_iterate_succ_le N n)

end Divergence
