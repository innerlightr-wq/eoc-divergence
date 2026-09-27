# Formalization status: paper statements → Lean theorems

**Nothing here is an arithmetic counting gain.** Two generic finite-counting cores are now
machine-checked; the weighted bulk collision estimate is untouched and no exceptional-set exponent
improvement follows.

## Completed

| paper | Lean theorem | hypotheses | build evidence | axioms |
|---|---|---|---|---|
| **A4a** two-class domination | `EOC.CarryDomination.filter_subset_union` | `[DecidableEq ι]`, `[DecidableEq (ZMod q)]`, `c i = 0 ∨ c i = 1`, `T i = Z i + c i` | `lake build EOC.CarryDomination`, 1219 jobs, exit 0 | `propext, Classical.choice, Quot.sound` |
| **A4a** | `EOC.CarryDomination.card_filter_le` | as above (`DecidableEq ι` via `classical`) | same | same |
| **A4b′** real corollary | `EOC.CarryDomination.card_filter_le_of_bound` | plus a **supplied** `∀ t, #{Z = t} ≤ Lq + R` | same | same |
| **A9** occupancy identities | `EOC.Occupancy.sum_nOcc` | `[DecidableEq κ]` | `lake build EOC.Occupancy`, 853 jobs, exit 0 | same |
| **A9** | `EOC.Occupancy.card_sameLabel` | `[DecidableEq κ]` | same | same |
| **A9** | `EOC.Occupancy.card_candidates_add_card_sameLabel` | `+ [DecidableEq Ω]` | same | same |
| **A9** | `EOC.Occupancy.sum_sq_nOcc_le` | `∀ y, nOcc y ≤ q` | same | same |
| **A9** | `EOC.Occupancy.mul_succ_le_candidates_add` | `∀ y, nOcc y ≤ q` | same | same |
| **A9** | `EOC.Occupancy.capacity_lt_candidates` | `∀ y, nOcc y ≤ q`, `0 < #s`, `q + h < #s + 1` | same | same |

Verified by `lake env lean AxiomCheck.lean`: all nine depend on exactly
`[propext, Classical.choice, Quot.sound]`. **No `sorryAx`**, no `sorry`, no `admit`, no new `axiom`,
no `opaque`. Statements in `ℕ` throughout for A9 — no truncated subtraction anywhere.

## What these theorems do NOT do — remaining instantiation dependencies

**A4a is generic.** `Z`, `c`, `T` are arbitrary maps into `ZMod q` with `c` binary. It does **not**
formalize the prefix–suffix construction. To apply it one still needs, none of which is formalized:
- **A2**: `T_w = (P_hi(u) + Q_hi(v) + c) mod 2^d` with `c = ⌊(P_lo+Q_lo)/2^B⌋ ∈ {0,1}`, from
- **A3**: `r_{uv} ≡ 3^{−j}(2^a r_v − C_u) (mod 2^{a+b+1})`, and
- the identification of `Z` with `P_hi + Q_hi` on a product class, with `d = s+1−B`.

**A4b′ is conditional.** `hZ` is a *hypothesis*. It is **not** the Fourier/Parseval bound: nothing
here proves `|H₀(t) − L/q| ≤ √(E_A E_B)/q`, which needs Parseval plus Cauchy–Schwarz on the
`ZMod 2^d` characters. That is A4b and is **not** formalized.

**A9 is generic occupancy.** `z` is an arbitrary labelling and `n_z ≤ q` is a hypothesis. It does
**not** verify the Collatz LCP law. To apply it one still needs, none of which is formalized:
- **A8**: `v₂(r_v − r_{v'}) = S_L(v) + min(v_{L+1}, v'_{L+1})`;
- the step `collision ⟹ t < B−a`, i.e. that a nonzero multiple of `2^t` of absolute value `< H`
  forces `2^t < H`;
- the equivalence `t < B−a ⟺ y_v ≢ y_{v'} (mod H)`, which is what makes `z` the low-residue class;
- `n_z ≤ q` from distinctness of the `y_v` in `[0, qH)`;
- `h = H/2` from "each interval of even length `H` holds `H/2` odd residues".

So the Collatz-side conclusion — *LCP-only rejection cannot beat capacity* — is **not** machine-checked;
only its generic counting skeleton is.

## Scope of the A9 conclusion, unchanged

It excludes counting *all* pairs satisfying the divisibility-necessary condition as a way to beat
capacity under `q + h < n + 1`. It does **not** exclude other uses of common-prefix information, nor
additional arithmetic pair restrictions.
