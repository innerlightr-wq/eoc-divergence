# Lemma ledger

Conventions are the repository's: accelerated map `T(m) = (3m+1)/2^{v₂(3m+1)}` on odd
`m`; word `a = (a_1…a_n)`; `S_j = a_1+⋯+a_j`; `α = log₂3`; `H_j = jα − S_j`, so
zero-confinement is `2^{S_j} ≤ 3^j`, i.e. `H_j ≥ 0`. Carry `C_0 = 0`,
`C_{k+1} = 3C_k + 2^{S_k}`; aggregate identity `2^{S_n} m_n = 3^n m_0 + C_n`;
realizer congruence `m_0 ≡ −C_n 3^{−n} (mod 2^{S_n})`, and the cylinder of `w` is the
residue class `r_w + 2^{S_n+1}ℤ`.

Every statement below is **proved**, and every count is from an exhaustive
enumeration in exact integer (or exact rational) arithmetic. Scripts and outputs:
[`scripts/`](scripts), [`data/`](data).

---

## 1. Switch decomposition of `C_n`

Let `w` have runs `R_1…R_ℓ` with letters `α_t`, boundaries `0 = p_0 < p_1 < ⋯ < p_ℓ = n`,
and `σ_t = +1` if `α_t = 1`, `−1` if `α_t = 2`. Put `B_t := 2^{S_{p_t}} 3^{n−p_t}`. Then

```
C_n  =  σ_1 B_0  +  Σ_{t=1}^{ℓ−1} 2σ_{t+1} B_t  −  σ_ℓ B_ℓ ,        ℓ = r + 1,
```

with **exactly `r+2` terms**, coefficients `±1` at the ends and `±2` inside, and the
`r+2` monomials pairwise distinct. Here `r = r(w)` is the number of switches
`a_{i+1} ≠ a_i`.

*Proof.* A run from `p_{t−1}` to `p_t` with letter `a` contributes
`Σ_{i=p_{t−1}}^{p_t−1} 3^{n−1−i} 2^{S_i} = [B_t − B_{t−1}]/(2^a − 3)`, and `2^a − 3 = −1`
for `a = 1`, `+1` for `a = 2`; so the contribution is `σ_t(B_{t−1} − B_t)`. Collecting:
`coeff(B_0) = σ_1`, `coeff(B_ℓ) = −σ_ℓ`, and for `0 < t < ℓ`,
`coeff(B_t) = σ_{t+1} − σ_t = 2σ_{t+1}` because runs alternate. The exponent of `3` is
`n − p_t`, strictly decreasing, so the monomials are distinct. ∎

**Verified**: all 65,534 `{1,2}`-words of length `≤ 15`; 0 mismatches in value, 0 in
term count, 0 coincident monomials; coefficient multiset `{−2,−1,+1,+2}` only.

**Remark.** Since `r ≤ 2d` where `d` counts the 2s, this refines the defect bound
`2d+2`, and the refinement is not cosmetic: `1^a 2^b` has `d = b = Θ(n)` but `r = 1`,
so the truth is 3 terms where the defect bound gives `Θ(n)`.

*(Integrality note: the run collapse requires `2^a − 3 = ±1`, so the two-letter
alphabet `{1,2}` is forced. For a general multiplier `p` the condition `2^a − p = ±1`
has two solutions in `a` iff `p−1` and `p+1` are both powers of two, i.e. iff `p = 3`.)*

## 2. Margin–switch theorem

Let `w` be a `{1,2}`-word of length `n` with `0 ≤ H_j ≤ W` for all `j`, and let
`κ := (α−1)(2−α) = 0.2427814…`. Then

```
r(w) + 1  ≥  2κ·n/W − (α−1) ,        equivalently   W ≥ 2κ·n/(r + 1 + α − 1).
```

*Proof.* A 1-run of length `L` raises `H` by `L(α−1)`; a 2-run lowers it by `L(2−α)`.
Both endpoints of every run lie in `[0,W]`, so 1-runs have `L ≤ W/(α−1)` and 2-runs
`L ≤ W/(2−α)`. With `u` 1-runs, `v` 2-runs, `u+v = r+1`, `|u−v| ≤ 1`, and using
`1/(α−1) + 1/(2−α) = 1/κ` (valid because `(α−1)+(2−α) = 1`):
`n ≤ uW/(α−1) + vW/(2−α) ≤ ((r+1)/2)(W/κ) + W/(2(2−α))`. ∎

**Verified**: all 34,125 zero-confined `{1,2}`-words of length `≤ 16`; 0 violations.
Asymptotically tight: the extremal family alternating maximal 1-runs and 2-runs
inside `[0,W]` attains `n/((r+1)W) → 1/(2κ) = 2.0595`.

**Corollary.** For fixed `r`, a word of length `n` must depart from the barrier by at
least `≈ 0.4856 n/(r+2)` — a separation linear in `n`. Bounded switch count and
narrow confinement are incompatible.

## 3. Switch density of the mechanical extremal

The barrier-hugging word `a_j = ⌊jα⌋ − ⌊(j−1)α⌋` has `S_j = ⌊jα⌋`, hence
`H_j = {jα} ∈ [0,1)` — the narrowest possible band — and switch density

```
r(w)/n  ⟶  2(2 − α)  =  0.8300750… .
```

Its 1s are isolated and its 2-runs have length 1 or 2, so the run count is `≈ 2·#(1s)`.

**Verified**: `r/n = 0.8300000, 0.8300000, 0.8300700` at `n = 10^3, 10^4, 10^5`.

**Remark.** Staying in the narrowest band forces *near-maximal* switching, strictly
above the general bound of Lemma 2. Balance does not buy few runs; it forces many.

## 4. Automatic height on confined blocks

For every zero-confined word, `2^{S_i} ≤ 3^i` for all `i < n`, so

```
C_n / 3^n  =  Σ_{i<n} 2^{S_i}/3^{i+1}  ≤  n/3 ,      hence   C_n ≤ (n/3)·max(2^{S_n}, 3^n)
```

since `max(2^{S_n},3^n) = 3^n` on a confined word. **No balance hypothesis is needed.**

**Verified**: all 34,125 zero-confined `{1,2}`-words of length `≤ 16`; 0 violations;
maximum observed `C_n/3^n = 3.987`.

**Consequence.** The balanced-square criterion of the synthesis (§7(d)) requires
`c_W ≤ poly(ℓ)·max(2^ℓ, 3^k)`, which in accelerated coordinates is exactly the display
above (the Sturmian numerator `c_W` equals `C_n`; see Lemma 11). So *inside the
confined sector* the balance hypothesis is automatic. The counterexample `W = 0^a1^a`
that forces the hypothesis in general has its ones at the end, so its early prefixes
have ones-density `0 ≪ β`: it is not confined.

## 5. Bit-loss lemma

If `m ≡ m′ (mod 2^K)` and the common next valuation `a` is determined (`a ≤ K−2`), then
`3m+1 ≡ 3m′+1 (mod 2^K)`, so `T(m) ≡ T(m′) (mod 2^{K−a})` — and no finer: the fiber of
size `2^a` splits into `2^a` distinct images. Hence the retained precision obeys

```
K_{n+1} = K_n − a_n ,        K_n = K_0 − S_n .
```

**Verified**: every odd residue class mod `2^K` splits under one step, for
`K = 6, 8, 10, 12, 14` — fraction `1.0000` in each case. No finite `2`-adic membership
is inheritance-stable.

## 6. Precision budget

The first `L` valuations of `m` are determined by `m mod 2^{S_L+1}`, and by no smaller
modulus. This is the realizer congruence; the smallest state that closes the valuation
dynamics is therefore the realizer cylinder itself.

**Verified**: 70,000 `(m,L)` pairs; 0 failures of sufficiency.

## 7. Minimal-automaton saturation

Quotient the odd residues mod `2^N` by equality of the first `L` valuations. The class
count grows and reaches the full `2^{N−1}` at `L = N−1`, for `N = 10,12,14,16,18`. No
merging survives: there is no nontrivial finite-state compression of the dynamics.

## 8. Precision / multiplicity duality

With odd-Haar mass `μ(w) = 2^{−S_n}`, the child `wa` satisfies `μ(wa)/μ(w) = 2^{−a}` and
`Σ_{a≥1} 2^{−a} = 1`. Equivalently, the realizer cylinders form a partition:

```
C(w) = ⊔_{a≥1} C(wa) ,     so for every height M,   N_M(w) = Σ_{a≥1} N_M(wa),
```

where `N_M(w) = #(C(w) ∩ [1,M])`. Hence

```
precision lost in one step  =  a_n  =  log₂( 1 / relative child mass ).
```

The bit-loss lemma and the branching of the cylinder tree are the same fact read in
two directions: what the forward map destroys in resolution, the tree carries as mass
subdivision. Nothing is destroyed.

**Verified**: 728 tree nodes at `M = 10^4, 10^6`, 0 partition failures (tested by
directly partitioning `C(w) ∩ [1,M]` by next valuation, with no truncation); 255 words,
0 failures of `Σ_a μ(wa) = μ(w)` as exact truncated geometric sums.

## 9. The mod-3 inheritance law

Mod 3, `3m_n + 1 ≡ 1`, so `2^{a_n} m_{n+1} ≡ 1`, and since `2 ≡ −1 (mod 3)`:

```
δ_{n+1}  :=  m_{n+1} mod 3  =  2^{a_n} mod 3  =  { 2 if a_n odd, 1 if a_n even }.
```

This closes exactly — and does not even use `δ_n`. The class `0 mod 3` is never in the
image. **Verified**: 599,994 steps from 100,000 seeds; 0 mismatches.

**But it restricts nothing.** Both classes have the identical geometric next-valuation
distribution (`0.5, 0.25, 0.125, …`). A marker can close perfectly and separate cleanly
while inducing no reduced dynamics on the target. (It is already used in the programme:
the descent lemma (L1) takes `m ≡ 2 (mod 3)` as the condition for a backward step.)

## 10. Exponent identity

With `h := α H₂(1/α)` the confined-word entropy and `I₀ := α(1 − H₂(1/α))` the
confined-mass rate (formalized as `Occupation.confined_mass_rate`):

```
h + I₀ = α ,        h = 1.5056439… ,   I₀ = 0.0793186… ,   α = 1.5849625… .
```

**Consequence.** `#W_n^{conf} ≈ 2^{hn}` grows while `p_n ≈ 2^{−I₀n}` decays. A union
bound over confined words adds `1` per word and therefore over-counts the finite-height
population by `2^{hn}`: population counting alone cannot close the placement gap, and
the identity says by exactly how much it fails.

## 11. Dictionary to the Sturmian conjugacy coordinates

The parity coding and the accelerated coding are related by the Sturmian morphism
`σ : a ↦ 1 0^{a−1}`, under which `ℓ = S_n`, `k = n`, and the ones-density is `n/S_n`
(critical value `β = 1/α`). Under this dictionary the periodic-value numerator of the
Sturmian work equals the EOC carry,

```
c_w  =  Σ_{j<n} 3^{n−1−j} 2^{S_j}  =  C_n ,
```

and `Φ(w^∞) = c_w/(2^ℓ − 3^k) = C_n/(2^{S_n} − 3^n)` is the EOC rational anchor.
Also, if two accelerated words agree on letters `1…L` and differ at `L+1`, then
`v₂(m − m′) = S_L + min(a_{L+1}, a′_{L+1})`.

**Verified**: 265,719 words over `{1,2,3}` of length `≤ 11`, 0 mismatches for `c_w = C_n`;
the anchor is the exact periodic fixed point, 0 mismatches; the depth law on 60,001 odd
pairs, 0 mismatches.

*(The depth law is not new — it is Lemma 6.1 of the author's companion note on the
2-adic Sturmian carry constant, recorded here only for the dictionary.)*
