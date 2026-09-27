# Dependency plan for the deferred formalizations

Ordered by dependency, not by importance. Nothing below is started.

## 1. A4b — the Fourier/energy layer (optional, separable)
`|H₀(t) − L/q| ≤ R`, `R = √(E_A E_B)/q`, uniformly in `t`, for a product class.
Needs: characters of `ZMod (2^d)`; the exact inversion `H₀(t) = q^{−1}Σ_g e(−gt/q)A(g)B(g)`;
Parseval `Σ_g |A(g)|² = q·Σ_x f(x)²`; Cauchy–Schwarz. `ShellWeyl.lean` already has
`blockWeyl`, `card_filter_lt_eq_fourier` and `card_filter_lt_le`, so this should reuse rather than
rebuild. **Feeds** `card_filter_le_of_bound`'s hypothesis `hZ`.

## 2. A8 → A9 instantiation
`v₂(r_v − r_{v'}) = S_L + min(v_{L+1}, v'_{L+1})`, then `collision ⟹ t < B−a`, then
`t < B−a ⟺ y_v ≢ y_{v'} (mod H)`, then `n_z ≤ q`, then `h = H/2`.
Needs the repository's `leastRealizer` and word API (`ResidueDiscrepancy.lean`, `LiftDigits.lean`).
This is what turns the generic `Occupancy` theorem into the stated Collatz obstruction.

## 3. A7 — singleton characterization (attempted-next candidate)
For `ℓ ≥ 3`, total `b`, corridor `A ≥ 0`, `ℓ ≤ b ≤ αℓ + A`: singleton iff `b = ℓ`.
Witnesses `(1^{ℓ−1}, b−ℓ+1)` and `(1^{ℓ−2}, 2, b−ℓ)`; the extra check is `ℓ ≤ α(ℓ−1) + A`.
Needs: **a proved rational bound `3/2 < α`**, not a float — `Real.logb 2 3 > 3/2 ⟺ 2^3 < 3^2`, i.e.
`8 < 9`. Prove the generic statement under `3/2 ≤ α` and specialize to `EOC.alpha` explicitly.
Also needs care with `ℕ` subtraction in `b−ℓ+1` and `b−ℓ` (guarded by `b > ℓ`), and the repository's
finite-word type with its total-valuation and corridor predicates. **Not attempted** in this pass.

## 4. A5 — rotation/composition lower bound
`L_s ≥ C(s−1,N−1)/N`. Needs a cyclic-rotation group action on compositions, the maximiser argument
on partial sums of `d_i − s/N`, and that each rotation class has `≤ N` members. Self-contained
combinatorics; no realizer arithmetic.

## 5. A6 — in this order, and not out of it
1. **exact finite summed-binomial inequality** `L_s^thin ≤ T_δ(N,s,j)` and
   `L_s^thin/L_s ≤ N·T_δ/C(s−1,N−1)` — depends on A5, purely finite, useful on its own;
2. **entropy bounds with uniform constants** `L_s^thin/L_s ≤ 2^{−NΔ_δ(θ)+O(log N)}`;
3. **floors/ceilings and the parameter range** `1+δ < θ ≤ α`, `N = ⌈κB⌉`, `j = ⌊N/2⌋`;
4. **certified positive exponent margin** `γ(13/20, 1/10) > 0` by rational arithmetic, not decimals;
5. **asymptotic conclusion**.

**Do not substitute the finite evaluations for step 2–5.** `B = 100,200,320,640` cross-checks step 1
only.

## Explicitly not to be reopened
The weighted bulk collision estimate; mechanism searches; carry cancellation; larger trajectory or
word scans; fitted finite exponents; optimization of diagnostic constants; any full occupation-count
or divergence-exclusion proof.
