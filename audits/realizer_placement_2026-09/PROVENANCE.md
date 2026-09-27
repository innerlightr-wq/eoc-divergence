# Provenance table for A1–A9

Status vocabulary, used strictly: **reported paper proof** (argument written out in this package,
not independently re-reviewed line by line, not machine-checked) · **finite computational
verification** · **LEAN-VERIFIED**. No statement is upgraded to "reviewed" merely for appearing in
`CONSOLIDATED_RECORD.md`.

Nine statements is not nine novel results: correctness, programme role and literature novelty are
separate questions and no priority search was conducted.

| # | statement | assumptions | proof source | verification artifact | tested range / evidence | status |
|---|---|---|---|---|---|---|
| A1 | independent failure offset `t*_w ≡ −((3x_w+1)/2)·3^{−(N+1)} (mod 2^K)`; `K ≥ 1` | zero-confined `w`; `x_w` odd | audit_AUDIT_CORRECTIONS.md §A1 | scripts/a1_independent_offset.py | 3,241 cylinders, `N ≤ 12`, `B ∈ {6..14}`; 0 offset disagreements | reported paper proof |
| A2 | `T_w = (P_hi+Q_hi+c) mod 2^d`, `c ∈ {0,1}` | any split `j` | PREFIX_SUFFIX_FINDINGS.md §2 | scripts/carry_split.py | 33,948,325 `(w,j)` checks, 0 violations | reported paper proof |
| A3 | `r_{uv} ≡ 3^{−j}(2^a r_v − C_u) (mod 2^{a+b+1})` | `|u|=j`, `S_u=a`, `S_v=b` | PREFIX_SUFFIX_FINDINGS.md §1 | scripts/verify_claims.py | 14,405 checks, words of length 2–10, 0 mismatches | reported paper proof |
| A4a | `H(t) ≤ H₀(t)+H₀(t−1)` | `T = Z + c`, `c ∈ {0,1}` | CARRY_ROBUST_AUDIT.md §1 | `EOC/CarryDomination.lean` | Lean kernel; axioms `propext, Classical.choice, Quot.sound` | **LEAN-VERIFIED** |
| A4b | `|H₀(t)−L/q| ≤ R = √(E_A E_B)/q` uniformly in `t`; `σ = min(1,τ)` | product class; Parseval + Cauchy–Schwarz | CARRY_ROBUST_AUDIT.md §1 | scripts/carry_robust.py | all `t`, all `j = 2..N−2`, `B,N=(20,13),(20,18)`; 0 violations | reported paper proof |
| A4b′ | real corollary: supplied `#{Z=t} ≤ Lq+R` ⟹ `#{T=t} ≤ 2Lq+2R` | `hZ` supplied externally | FORMALIZATION_STATUS.md | `EOC/CarryDomination.lean` | Lean kernel | **LEAN-VERIFIED** (conditional on `hZ`) |
| A5 | `L_s ≥ C(s−1,N−1)/N` | `N ≤ s ≤ αN` | THIN_BAND_LEMMA.md §1 | scripts/verify_combinatorial.py | 32 shells, `N = 6..14`, 0 violations | reported paper proof |
| A6 | `H_s^thin/(L_s/q) ≤ 2^{−γB+O(log B)}`, `γ = 0.054816179871361` | `κ=13/20`, `δ=1/10`, `j=⌊N/2⌋` | THIN_BAND_LEMMA.md §1 | scripts/thin_band.py | exact finite bound at `B=100/200/320/640`; monotonicity at 399 points | reported paper proof; `C`, `B₀` **existential only** (see SCOPE_CORRECTION.md) |
| A7 | for `ℓ ≥ 3`: singleton iff `b = ℓ` | `S_m ≤ αm+A`, `A ≥ 0`, `ℓ ≤ b ≤ αℓ+A` | CLOSING_RECORD.md §1 | scripts/closing.py | 186 families, `ℓ=3..9`, `A ∈ {0,½,1,2,3}`, 0 mismatches | reported paper proof; **not formalized** |
| A8 | `v₂(r_v−r_{v'}) = S_L+min`; collision ⟹ `t < B−a` | one class (`b` fixed), `H = 2^{B−a}` | CLOSING_RECORD.md §4 | scripts/lcp_lemma.py | 0 violations of either | reported paper proof |
| A9-generic | `P + Σn_z² = n²+n`, `Σn_z² ≤ qn`, `n(n+1) ≤ P+qn`, and `q+h<n+1 ⟹ nh < P` | `n_z ≤ q`, `0 < n` | CLOSING_RECORD.md §4 | `EOC/Occupancy.lean` | Lean kernel; axioms as above | **LEAN-VERIFIED** (generic occupancy; **no Collatz instantiation**) |
| A9-Collatz | the instantiation `z` = low-residue class, `h = H/2` | needs A8 + distinctness + oddness | CLOSING_RECORD.md §4 | scripts/lcp_obstruction.py | `n_z ≤ q` and the equivalence: 0 violations; `P/capacity = 4.50–21.15` | reported paper proof; **not formalized** |

## Preserved paths and hashes (md5, first 12 hex)

Preserved under `audits/realizer_placement_2026-09/` in `eoc-divergence`, branch
`research/harden-missing-formula-audit`. Scratch originals were **copied, not moved or modified**
in this round.

| preserved file | md5 | scratch original | identical? |
|---|---|---|---|
| `CONSOLIDATED_RECORD.md` | `871f046a5e8a` | `871f046a5e8a` | yes |
| `CLOSING_RECORD.md` | `3430f134006f` | `3430f134006f` | yes |
| `PREFIX_SUFFIX_FINDINGS.md` | `df965eee1cae` | `df965eee1cae` | yes |
| `CARRY_ROBUST_AUDIT.md` | `f87c38dace06` | `f87c38dace06` | yes |
| `BULK_THIN_DECOMPOSITION.md` | `85e23457145a` | `85e23457145a` | yes |
| `THIN_BAND_LEMMA.md` | `552c3a6833ee` | `552c3a6833ee` | yes |
| `BASELINE_VALIDATION.md` | `20ee1d7d831a` | `20ee1d7d831a` | yes |
| `FORMALIZATION_STATUS.md` | `6ee3aaa46ecf` | `6ee3aaa46ecf` | yes |
| `DEPENDENCY_PLAN.md` | `20fbe44dc964` | `20fbe44dc964` | yes |
| `SCOPE_CORRECTION.md` | `0d133e604799` | `0d133e604799` | yes |

**Editorial-version caveat.** `CONSOLIDATED_RECORD.md` was corrected in place in the scratch
directory in the previous round (the A6 remainder-scope wording and the novelty caveat) *before*
being copied, so **no pristine pre-correction original survives on disk**. The preserved file is the
corrected version; the correction itself is described in `SCOPE_CORRECTION.md`. All other records
were copied unmodified.

## Commits (all local; nothing pushed)

- `eoc-divergence` `research/harden-missing-formula-audit`, base `9a1748a`: `b57b152` (script
  repairs) → `59a38ef` (note correction) → `af47845` (package) → `245c383` (A4a status) → this.
- `eoc-lean-verification` `research/carry-domination-lemma`, base `14dea46`: `5155bc8` (A4a) → this.

## Open, and established by none of the above

```
(*)  Σ_{a ∈ bulk} L_{s,a}·√(χ_{U,a} χ_{V,a}) ≤ C(B+1)^p · L_s · q^{1/25}
```
`C, p` independent of `B` and of the permitted shell; suffix constrained only by `S_v(m) ≤ αm + A`,
`A = αj − a`. **Weighted**: a few unfavourable classes are acceptable if their weights are
controlled, and a favourable representative class establishes nothing. Conditional payoff (exponent
`0.949651926715094`, improvement `0.000303600473237`) is **conditional on (*)**.

**No exceptional-set exponent improvement has been obtained.**
