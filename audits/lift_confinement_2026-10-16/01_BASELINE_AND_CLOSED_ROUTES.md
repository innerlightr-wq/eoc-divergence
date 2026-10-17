# 01_BASELINE_AND_CLOSED_ROUTES.md

## Repository state — recorded, not modified

| repo | branch | HEAD | origin/main | worktree |
|---|---|---|---|---|
| `eoc-divergence` | `main` | `938dcc0` | `b787dfa` | clean |
| `eoc-lean-verification` | `main` | `6057a0d` | `6057a0d` | clean |

## A confirmed error in my own October 16 work

The terminal-tip enumeration used `N = 11`, `S_N = 22`.  Zero confinement requires
`2^{S_k} ≤ 3^k`; at `k = 11` the cap is `⌊11 log₂3⌋ = 17`, and by exact integer comparison
```
2^22 = 4 194 304   >   3^11 = 177 147 .
```
**That population was not zero-confined — it was far outside the sector.**  The conclusion drawn
there (temporal differentiation explained by the carry formula) rested on exact algebraic
identities and is unaffected, but **every statistical statement in that run applied to
unconfined words** and is superseded by the enumeration here.

## Constraints inherited from the two October 16 audits

| result | status | constraint it imposes here |
|---|---|---|
| **Lemma O** (H10 audit): confinement `2^{S_n} ≤ 3^n` and height `H ≥ 3^N` give `ρ_N ≥ 1` identically | **PROVED** | any divisibility-to-size tool is vacuous on this sector — do not retry |
| **Separability** (temporal audit): `Δ_iΔ_k C_N = Δ_iC·Δ_kC/T_i` | **PROVED** | the carry's nonlinearity is exactly `2^{a+b}=2^a2^b`; no higher difference carries new information |
| **Prefix-locality obstruction** (temporal audit): `r_N` always realizes the prefix, so every finite word is realized | **PROVED** | no prefix-local invariant separates realizable from unrealizable infinite words — `J(N)` is prefix-local |
| **Proposition R** (H10 audit): `x ∈ ℤ_{≥0} ⟺ J(∞) < ∞` given `S_n → ∞` | **PROVED**, **ALREADY KNOWN** | the brief's own instruction: do not reprove it |
| **`r_min` frontier** (Rev 8 / memory): envelope stuck at `10.2953`, route retired | recorded | `min J(N)` turns out to be governed by exactly this quantity (§05) |
| **Theorem D** (Oct 14): `v_2(β) = σ−1`; odd part undetermined for **free** suffixes | **PROVED** | the valuation side of pair differences is settled |

## Novelty boundary

A result here is new only if it is not a consequence of: Rev 8 Lemma 2.4; the carry recurrence;
Proposition R; prefix-locality; or Lemma O.  `07_CANDIDATE_LEMMAS.md` applies this test to each
candidate.
