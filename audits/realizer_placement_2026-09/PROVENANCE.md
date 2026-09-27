# Provenance table for A1–A9

For each statement: exact content, assumptions, proof/script file, computational cross-check and
its tested range, status, and the commit containing it. **Status is one of: paper proof (argument
written out, not machine-checked) / finite verification only / Lean-verified.** Nothing below is
Lean-verified.

Commit `HASH` = `research/harden-missing-formula-audit` in `eoc-divergence`, base
`9a1748a5414b0d0ca6b4b2fff18153f3bf92f64f`. Local only; never pushed.

| # | statement | assumptions | proof text | script | cross-check and range | status |
|---|---|---|---|---|---|---|
| A1 | `t*_w ≡ −((3x_w+1)/2)·3^{−(N+1)} (mod 2^K)`; `K = ⌊(N+1)α − S⌋ ≥ 1` | zero-confined `w`, `x_w` odd (terminal parity) | `AUDIT_CORRECTIONS.md` §A1 | `a1_independent_offset.py`, `per_cylinder_survival.py` | 3,241 cylinders (`N ≤ 12`, `B ∈ {6,…,14}`), 0 offset disagreements; 311,844 cylinders in the repo script; `K<1` in 0 of 12,447 words | paper proof |
| A2 | `T_w = (P_hi + Q_hi + c) mod 2^d`, `c ∈ {0,1}`; `r_w mod 2^B = (P_lo+Q_lo) mod 2^B` | any split index `j`, `a+b = s` | `PREFIX_SUFFIX_FINDINGS.md` §2 | `carry_split.py` | 33,948,325 `(w,j)` checks at `B,N = (12,8),(16,11),(20,13),(16,15),(20,18)`, 0 violations | paper proof |
| A3 | `r_{uv} ≡ 3^{−j}(2^a r_v − C_u) (mod 2^{a+b+1})` | `|u|=j`, `S_u=a`, `S_v=b` | `PREFIX_SUFFIX_FINDINGS.md` §1 | `verify_claims.py` | 14,405 word/split checks, all zero-confined words of length 2–10, 0 mismatches | paper proof |
| A4 | `H(t) ≤ H₀(t)+H₀(t−1)`; `|H₀(t)−L/q| ≤ R` uniformly in `t`; `σ = min(1,τ)` | product class `U×V`, `c ∈ {0,1}` | `CARRY_ROBUST_AUDIT.md` §1 | `carry_robust.py` | all residues `t`, all `j = 2…N−2`, `B,N = (20,13),(20,18)`: 0 domination and 0 `R` violations | paper proof |
| A5 | `L_s ≥ C(s−1,N−1)/N` | `N ≤ s ≤ αN` | `THIN_BAND_LEMMA.md` §1 | `verify_combinatorial.py` | 32 shells, `N = 6…14`, 0 violations; ratio → 1.213 at the top shell | paper proof |
| A6 | `H_s^thin/(L_s/q) ≤ 2^{−γB+O(log B)}`, `γ = 0.054816179871361` | `κ=13/20`, `δ=1/10`, `j=⌊N/2⌋`, `B ≤ s ≤ ⌊αN⌋` | `THIN_BAND_LEMMA.md` §1 | `thin_band.py` | exact binomial bound `0.691825 / 0.0375106 / 0.000161790 / 1.72629e−09` at `B = 100/200/320/640`, argmax the top shell; monotonicity at 399 points, 0 violations | paper proof; **remainder not made explicit** |
| A7 | for `ℓ ≥ 3`, family is a singleton iff `b = ℓ` | `S_m ≤ αm+A`, `A ≥ 0`, `ℓ ≤ b ≤ αℓ+A` | `CLOSING_RECORD.md` §1 | `closing.py` | 186 nonempty families, `ℓ = 3…9`, `A ∈ {0,½,1,2,3}`, 35 singletons, 0 mismatches | paper proof |
| A8 | `v₂(r_v−r_{v'}) = S_L + min(v_{L+1},v'_{L+1})`; collision ⟹ `t < B−a` | one class (`b` fixed), `H = 2^{B−a}` | `CLOSING_RECORD.md` §4 | `lcp_lemma.py` | lcp law and the implication: 0 violations | paper proof |
| A9 | `P_LCP + Σ_z n_z² = n²+n`, `Σn_z² ≤ qn`, capacity `≤ nH/2`; so `n+1 > q+H/2` ⟹ LCP-rejection loses | distinct odd `y_v` in `[0,qH)` | `CLOSING_RECORD.md` §4, this file's note below | `lcp_obstruction.py` | `n_z ≤ q` and the equivalence: 0 violations; `n+1 > q+H/2` in every tested bulk class; `P_LCP/capacity = 4.50–21.15` | paper proof |

**A9, subtraction-free form** (preferred for formalization, avoids truncated `ℕ` subtraction):
```
P_LCP + Σ_z n_z² = n² + n ,   Σ_z n_z² ≤ q·n   ⟹   n(n+1) ≤ P_LCP + q·n ,
```
and with capacity `Σ_x h(x)² ≤ nH/2`, the conclusion is `nH/2 < P_LCP` whenever `n(n+1) > qn + nH/2`,
i.e. `n+1 > q + H/2`.

## Open, and not established by any of A1–A9

```
(*)  Σ_{a ∈ bulk} L_{s,a}·√(χ_{U,a} χ_{V,a}) ≤ C(B+1)^p · L_s · q^{1/25}
```
`C, p` independent of `B` and of the permitted shell; suffix constrained only by `S_v(m) ≤ αm + A`,
`A = αj − a`. **Weighted**: a few unfavourable classes are acceptable if their weights are
controlled, and a favourable representative class establishes nothing. No improvement to the
exceptional-set exponent has been obtained.
