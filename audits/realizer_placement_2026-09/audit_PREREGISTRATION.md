# Pre-registration — partial counting target beyond the fresh-bit boundary

Written before running any test. Not edited afterwards; departures go in `DEVIATIONS.md`.

## Conventions fixed (all verified against source, see BASELINE_AND_SCOPE.md)

- `α = log₂3`; `I₀ = α − α log₂α + (α−1)log₂(α−1)` (Lean `PersistenceModel.lean:422`).
- `R_j = S_j − jα`; `Confined U d N ⟺ ∀ j ≤ N, R_j ≤ U` (Lean `Confinement.lean:15`).
  **Zero confinement is `U = 0`**, equivalently the exact integer test `2^{S_j} ≤ 3^j`.
- `A_{N,M} = #{m odd, 1 ≤ m ≤ M : m zero-confined for N steps}` — cutoff **inclusive** `[1,M]`.
- `p_N = Σ_{w confined, |w| = N} 2^{−S_N(w)}` (exact rational).
- `X = 2^B`, `M = X − 1`, `O_M = ⌈M/2⌉ = 2^{B−1} = X/2`.
- `Q_{N,M} = A_{N,M}/((X/2) p_N)`.
- **Exact-realizer modulus `q_w = 2^{S_w+1}`** (the `+1` enforces terminal parity: `m_N` odd),
  `r_w = leastpos(−C_N 3^{−N} mod 2^{S_N})` refined to the odd-endpoint class.
- `N = ⌈κB⌉`, default `κ = 13/20`.

## Questions

**A1.** Does `per_cylinder_survival.py` derive the failure residue `t*_w` from observed failures
(circular) or predict it independently? Test: compute `t*_w` from the *closed form* before
observing any failure label, then compare against direct accelerated iteration.

**A2.** Does `shell_discrepancy.py` verify the entire prescribed valuation word, or only
confinement plus total valuation? Test: assert the computed realizer reproduces the exact word
letter by letter.

**A3.** Is the note's claim about non-2-adic features correctly qualified, or does it overclaim
independence? Test the brief's finite example (`w = (1)`, `M = 15`, seeds 3,7,11,15).

**A4.** Under `ShellWeyl`'s actual normalization, does the singleton shell `S = N` force
`C ≥ 2^d` with `d = N+1−B`, and in which κ range does that bite?

**B.** Is `Q_{⌈κB⌉, 2^B−1}` bounded, and by what, at `κ = 0.65`?

## Populations and ranges (pre-registered ladder)

- A1: all zero-confined words of length `N ≤ 12` by exhaustive DFS; all odd `m ≤ 2^14−1` for
  cross-check by direct iteration. Include the five listed edge cases explicitly.
- A2: all zero-confined words of length `N ∈ {8, 12, 16}`; full-word equality asserted.
- A3: the exact stated example, plus all `w` of length 1–2 with `M ≤ 63`.
- A4: symbolic, plus the singleton shell at `N ∈ {4,…,20}`, `B ∈ {4,…,20}`.
- B: `B ∈ {12, 16, 20, 24, 28}` with `N = ⌈0.65B⌉ ∈ {8, 11, 13, 16, 19}`; `Q` computed
  **exactly** from word enumeration plus exact cylinder counts, cross-checked against direct
  seed enumeration for `B ≤ 22`.

**Resource limits.** No single script over ~20 min. Word enumeration capped at `N ≤ 20`
(≈1.3·10⁷ words). Direct seed enumeration capped at `B ≤ 22`. If a cell exceeds budget it is
reported as **aborted**, not estimated.

## Pass/fail criteria

- A1 PASSES the audit concern if the independently predicted `t*_w` matches observation with
  0 mismatches on every listed edge case; the concern is UPHELD if the existing script's
  prediction uses observed labels.
- A2 PASSES if full-word equality holds with 0 mismatches; the concern is UPHELD if the existing
  script checks only `(length, S_N)`.
- A3: the concern is UPHELD if the verified example contradicts a literal reading of the note's
  sentence; otherwise the note stands.
- A4: the concern is UPHELD as stated only if `d ≥ 1` in the target κ range; otherwise it is
  correct mathematics outside the target range.
- B: the target is SUPPORTED within range if `Q ≤ C₀(B+1)^{d₀}` with small fixed `C₀, d₀` and no
  growth consistent with `2^{ηB}`, `η > 0`; REFUTED if `Q` grows at an exponential rate exceeding
  the `η` ceiling `I₀(κ − 1/α) = 0.001512625`.

## Deviations requiring a record

Any change to κ, the `B`/`N` ladder, the confinement width `U`, the cutoff convention, the
definition of `Q`, or the pass/fail thresholds; any abandoned or substituted population; any
computation aborted; any move from exact to floating arithmetic in an identity check.

## Scope limits (from the brief, restated)

No restart of feature sweeps, cone/attainment experiments, Sturmian work, or occupation-count
proofs. `r_min(N,0) ≤ 2^{cN}` is a documented secondary option only. No pushes, PRs, DOIs, or
manuscript edits. No toolchain or dependency changes. No `sorry`/`admit`/`axiom`.
