# Realizer placement beyond the fresh-bit boundary — research record

**Verdict: USEFUL LOCAL LEMMA, GLOBAL GAIN STILL OPEN.** No improvement to the exceptional-set
exponent was obtained. Nothing here is Lean-verified.

Read in this order:

1. `PROVENANCE.md` — the A1–A9 table: statement, assumptions, proof text, script, cross-check range,
   status. **Start here.**
2. `CONSOLIDATED_RECORD.md` — the three-way split: paper proofs / finite checks only / open, plus the
   conditional payoff and the identified next action.
3. The individual records, in the order they were produced:
   `audit_BASELINE_AND_SCOPE.md`, `audit_AUDIT_CORRECTIONS.md`, `audit_PARTIAL_COUNTING_TARGET.md`,
   `audit_ARITHMETIC_LEMMA_ATTEMPT.md`, `PREFIX_SUFFIX_FINDINGS.md`, `CARRY_ROBUST_AUDIT.md`,
   `BULK_THIN_DECOMPOSITION.md`, `THIN_BAND_LEMMA.md`, `CLOSING_RECORD.md`.
4. Pre-registrations and deviations: `audit_PREREGISTRATION.md`, `audit_DEVIATIONS.md`,
   `audit_REPRODUCIBILITY.md`.

`scripts/` is standard-library Python 3, exact integer/rational arithmetic for every identity;
floats only for reported logs, z-scores and exponents. `repro/` holds the captured outputs. Each
script prints its enumeration size and violation count.

## Scope limits, stated once

- Every computation is at `B ≤ 20`, `N ≤ 18`, except A6's exact binomial evaluation (`B ≤ 640`),
  which evaluates a combinatorial bound and enumerates no words.
- Finite constants (`C = 2.00`/`3.08`, `τ_bulk ≈ 0.97`) are diagnostics, not uniform bounds.
- The open estimate is `(*)` in `PROVENANCE.md`. It is **weighted**; a favourable representative
  class establishes nothing.
- Nine statements is not nine novel results; no priority search was conducted.
