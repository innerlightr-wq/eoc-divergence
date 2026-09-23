import Divergence.Basic

/-!
# Descent audit: confinement up to a finite horizon

This library formalizes the three results retained by `audits/descent/DESCENT_AUDIT.md`:

* **L1** the backward `d = 1` step and its inheritance of confinement (`Descent.BackStep`);
* **L2** the chain law — the backward chain from `x` has length exactly `v₃(x+1)`
  (`Descent.ChainLaw`);
* **L4** the residue law for least confined integers (`Descent.ResidueLaw`);
* **L7** the lockstep invariance (`Descent.Lockstep`), the reason a descent proof of (DE)
  cannot accumulate 3-adic budget by forward motion.

It imports **only** `Divergence.Basic` and modifies nothing in `Divergence/` or `Occupation/`.

`Divergence.ZeroConfined m` is by definition `∀ n, 2 ^ S m n ≤ 3 ^ n`. Since `Divergence.CycleDrift`
is not imported here, the infinite-horizon statements are written in that unfolded form; they
apply to `Divergence.ZeroConfined` directly, being definitionally the same proposition.

No `sorry`, `admit`, `axiom`, or `opaque`.
-/

namespace Descent

open Divergence

/-- `m` is zero-confined for `N` steps: `2^{S_j} ≤ 3^j` for every `j ≤ N`. -/
def ConfinedUpTo (N m : ℕ) : Prop := ∀ j ≤ N, 2 ^ S m j ≤ 3 ^ j

theorem confinedUpTo_mono {N N' m : ℕ} (h : N' ≤ N) (hc : ConfinedUpTo N m) :
    ConfinedUpTo N' m := fun j hj => hc j (le_trans hj h)

@[simp] theorem confinedUpTo_zero (m : ℕ) : ConfinedUpTo 0 m := by
  intro j hj
  interval_cases j
  simp

/-- The finite horizons assemble to the infinite one. The right-hand side is
`Divergence.ZeroConfined m` unfolded. -/
theorem forall_confinedUpTo_iff {m : ℕ} :
    (∀ N, ConfinedUpTo N m) ↔ ∀ n, 2 ^ S m n ≤ 3 ^ n := by
  constructor
  · intro h n
    exact h n n (le_refl n)
  · intro h N j _
    exact h j

end Descent
