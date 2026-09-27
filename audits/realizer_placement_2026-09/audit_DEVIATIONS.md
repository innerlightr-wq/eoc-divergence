# Deviations from the pre-registration

`PREREGISTRATION.md` (md5 `cdb0dbe19216917aa3d9c7e6c8f2ed5c`) was not edited.

1. **`mpmath` unavailable.** The constant audit was written against `mpmath` for 40-digit
   precision; the module is not installed. Replaced by stdlib `math` (float64), which is
   sufficient for the ~10-decimal comparisons actually made, and the two symbolic identities
   (`I₀ = α(1−H₂(1/α))`, `1−I₀/α = H₂(1/α)`) were checked to `≤ 2.4e−16` instead of exactly.
   The documents therefore label these decimals as rounded, not proved.

2. **A3 sub-check initially wrong, then corrected.** I first tested uninformativeness over a
   complete `2^K` period and reported a large deviation (0.875). That test was mis-specified:
   independence of `t mod u` from `t mod 2^K` needs a complete period of the **joint** modulus
   `u·2^K`. Re-run over `u·2^K`: deviation exactly 0. Both outputs are kept
   (`repro/a2a3a4.out`, `repro/a3_fixed.out`) because the "wrong" one is itself the substantive
   finding. This strengthens, not weakens, the A3 verdict.

3. **Direct-enumeration cross-check reached `B = 20`, not `B = 22`.** The pre-registration
   allowed `B ≤ 22`, but `22` is not on the `B` ladder `{12,16,20,24,28}`, so the last
   cross-checked point is `B = 20`. No threshold was changed.

4. **Exponent-budget computation added** (`repro/phaseC_exponents.out`): the identity
   `log₂(T/P) = d` and the `κ < 1/(α−h/2)` threshold were not pre-registered. They are
   derivations, not tests, and no decision rule depends on them.

5. **`κ ↑ 1` analysis added** beyond the pre-registered `κ = 0.65`. Reported as a *refinement of
   the same target* with the same proof obligations; `κ = 0.65` is retained as the default and the
   question was not substituted.

6. **Repository change made** (allowed by the brief after validation): two scripts hardened on a
   new branch in an isolated worktree, one local commit, nothing pushed. The pre-registration did
   not anticipate code changes; they follow directly from A1 and A2 being upheld.

7. **No prose change to `notes/MISSING_FORMULA_SELECTION_LAW.md`.** A3 found a genuine overclaim
   there. Editing `notes/` was not in this task's scope, so the corrected wording is recorded in
   AUDIT_CORRECTIONS.md for the note's next revision rather than applied.

8. **No Lean additions.** Nothing proved here warranted one; in particular Lemma C1 is a
   hypothesis, and wrapping it in Lean would be the forbidden "wrapper around the final counting
   hypothesis". No `lake build` was run, so no build status is claimed either way.
