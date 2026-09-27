# Prefix–suffix factorization: from an exact formula to a partial estimate

Scratch: `~/scratch/collatz-prefix-suffix-20260926-215500/`. No repository was modified in this
task (heads re-verified below). Labels: **DERIVED HERE**, **COMPUTATIONALLY VERIFIED WITHIN
STATED RANGE**, **UNRESOLVED**.

## 1. The assessment's four checkable claims — all confirmed

| claim | verdict |
|---|---|
| `σ > 1 − I₀/α = H₂(1/α) ≈ 0.949955527` suffices (the target permits `η > 0`) | **CONFIRMED.** `(1−σ)(ακ−1) < I₀(κ−1/α)`; since `ακ−1 = α(κ−1/α)`, dividing by `κ−1/α > 0` gives `(1−σ)α < I₀`. |
| the threshold is **κ-independent** | **CONFIRMED**, `1−I₀(κ−1/α)/(ακ−1) = 0.949955527188` to 12 decimals for `κ = 0.65,…,2.00` |
| `gcd(u,6)=1` needed for "`m_N mod u` determines `t mod u`" | **CONFIRMED**, and it corrects my own test: `u = 3, 9` gave deviation 0 because `2·3^N ≡ 0 (mod u)` makes `m_N mod u` **constant** on the cylinder, not by CRT. Valid instances are `u = 5,7,11`. |
| `r_{uv} ≡ 3^{−j}(2^a r_v − C_u) (mod 2^{a+b+1})` | **CONFIRMED**, **14,405 word/split checks over all zero-confined words of length 2–10, 0 mismatches** — exactly the count the assessment reported. Not present in the Lean sources: `leastRealizer_eq_prefix_add` uses lift digits, not the standalone suffix realizer. |

**Correction to my previous report.** I wrote that the target "needs a relative saving of exactly
`2^{−d}`". That is the `σ = 1` case, i.e. the *full* gain. The assessment is right: `σ > 0.949956`
suffices for *some* gain. Corrected.

## 2. The exact split, with the cutoff restored (DERIVED HERE)

Let `s = S_w`, `d = s+1−B`, `w = uv`, `|u| = j`, `S_u = a`, `S_v = b`. Put
`P := (−3^{−j}C_u) mod 2^{s+1} = P_lo + 2^B P_hi` and
`Q := (3^{−j}2^a r_v) mod 2^{s+1} = Q_lo + 2^B Q_hi`. Then `r_w = (P+Q) mod 2^{s+1}` and

```
r_w mod 2^B = (P_lo + Q_lo) mod 2^B
T_w := ⌊r_w/2^B⌋ = ( P_hi(u) + Q_hi(v) + c(u,v) ) mod 2^d ,   c = ⌊(P_lo+Q_lo)/2^B⌋ ∈ {0,1}.
```

**The top block is a prefix term plus a suffix term plus one carry bit.** Verified at **every**
interior split point: `B,N = (12,8), (16,11), (20,13), (16,15), (20,18)` —
**33,948,325 `(w,j)` checks, 0 `T_w` violations, 0 low-bit violations.** The carry is active
(`c = 1` in 36–53% of pairs), so it is not a rare correction.

Two consequences worth separating:

- The **`a ≥ B` special case** gives `Q_lo = 0`, hence `c = 0` and a clean product — but it is
  **empty at κ = 0.65**: no word of length 13 admits an interior split with `a ≥ 20`
  (0 of 17,637). At κ = 0.90 it covers 1,899,102 of 1,900,470 words, in 96 classes, all of which
  are exact product sets (0 non-product classes) with `Q_hi` injective (0 failures, by Terras).
- The **general split** removes that restriction, which is why it matters: at κ = 0.65 100% of
  splits have `a < B`.

**Symbolic admissibility factors, the arithmetic does not.** At fixed `(j,a)` the zero-confinement
condition on the suffix is `S_v(k) ≤ αk + (αj − a)`, depending only on `(j,a)` — verified: 0
non-product classes. The cutoff coupling survives, and is now exactly the carry bit.

## 3. The Fourier consequence, and what is provable

Since `e(g(P_hi+Q_hi+c)/2^d) = e(g(P_hi+Q_hi)/2^d)(1 + (e(g/2^d)−1)1_{c=1})`,

```
V(g) = A(g)·Bq(g)  +  (e(g/2^d) − 1)·T(g),        T(g) = Σ_{c=1} e(g(P_hi+Q_hi)/2^d),
```
with `A(g) = Σ_u e(gP_hi/2^d)`, `Bq(g) = Σ_v e(gQ_hi/2^d)`. The first term **factors exactly**;
the second carries the whole coupling and is damped by `|e(g/2^d)−1| = 2|sin(πg/2^d)|`.

**The carry term is exactly a signed difference of two counts (DERIVED HERE).** Because the `g=0`
term of `(e(g/2^d)−1)T(g)` vanishes,
```
carry = #{(u,v) : c=1, P_hi+Q_hi ≡ −1 (mod 2^d)} − #{(u,v) : c=1, P_hi+Q_hi ≡ 0 (mod 2^d)}.
```
**Verified: 14 classes at `B=20, N=18`, 0 mismatches against the direct Fourier computation.**
It is signed by construction, so favourable cancellation is retained rather than discarded at a
triangle inequality.

### The factored term meets the threshold; the carry term does not yet exist as an estimate

Parseval gives `Σ_g|A|² = 2^d Σ_x n_A(x)²`, so with `E_A := 2^dΣn_A² − (#U)²` and `E_B` likewise,
Cauchy–Schwarz bounds the factored error by `2^{−d}√(E_A E_B)`. Writing that as `L·2^{−σ_CS d}`
with `L = #U·#V`:

| split | `σ_CS` (proved, factored term) | vs `σ* = 0.949956` |
|---|---|---|
| `a ≥ B`, `B=16, N=15` | worst class **0.413**, aggregate **0.735** | **fails** |
| `a ≥ B`, `B=20, N=18` | worst class **0.540**, aggregate **0.857** | **fails** |
| **balanced**, `B=20, N=18`, `#U,#V ≥ 125` | **1.132 – 1.298** across 12 classes | **passes** |

**Why the `a ≥ B` split fails and the balanced split succeeds.** At `a ≥ B` the suffix classes are
tiny (`#V` = 1–3), so `E_B = #V(2^d − #V) ≈ 2^d #V`: Terras injectivity is vacuous and the suffix
Weyl sum has no cancellation — the singleton obstruction of the previous audit's A4, one level
down. A balanced split makes both `E_A` and `E_B` small. Measured: `E_A/E_A^{max} ≈ 0.0000`
throughout, i.e. the prefix map `P_hi` is essentially perfectly equidistributed and supplies the
saving.

**Net status of the factored term: `σ_CS ∈ [1.13, 1.30] > σ*`, from Parseval and Cauchy–Schwarz
alone** — no equidistribution hypothesis, no randomness, no mixing. This is a *strictly weaker*
statement than the cutoff-counting target and is quantitatively useful when substituted into it.

**Net status of the carry term: UNRESOLVED.** It is empirically comparable to or larger than the
factored term (e.g. carry `+35` against factored `+5.17`; `−19` against `+7.57`; `+33` against
`−47.97`), so it cannot be discarded. Measured `|carry|/#{c=1}` is `1.4e−4 … 1.2e−3`, and
`|carry| ≤ 35` against a budget of `≈ 890` at `L ≈ 9·10⁴`, `d = 7` — a factor ≈25 margin, but
**no proof**. Both `N(−1)` and `N(0)` sit within ≈`√` of `#{c=1}/2^d`, consistent with square-root
fluctuation and nothing stronger is established.

## 4. What this is and is not

**Is:** an exact algebraic reduction with the main term removed, plus a *proved* bound (σ ≈ 1.13–1.30)
on one of the two resulting pieces, plus an exact identification of the other piece as a signed
difference of two counts over an explicit threshold set.

**Is not:** a restatement of the target. The circularity test that killed the previous "Lemma C1"
is passed here: `#{T_w = 0}` is no longer the object to be bounded; the main term
`#U#V/2^d` has been extracted exactly, the factored discrepancy is bounded unconditionally, and
what remains is a different, smaller object (a difference of two counts on `{c=1}`).

**Is not:** an asymptotic theorem. Every number above is `B ≤ 20`, `N ≤ 18`, one value of `κ` per
table. `σ_CS` was computed per class, not proved uniformly in `B`; the class sizes `#U, #V` and the
energies `E_A, E_B` must be controlled uniformly before any exponent claim. No curve was fitted.

## 5. The single next step

Prove `|N(−1) − N(0)| ≤ C(B+1)^c·#U·#V·2^{−σ d}` with `σ > 0.949956`, over the carry set
`{(u,v) : P_lo(u) + Q_lo(v) ≥ 2^B}`. This is a threshold-coupled bilinear count in which both
marginals are explicit: `P_lo, P_hi` come from `−3^{−j}C_u mod 2^{s+1}` and `Q_lo, Q_hi` from
`3^{−j}2^a r_v mod 2^{s+1}`. The measured near-perfect equidistribution of `P_hi` is the natural
input; the obstruction is that the threshold set is defined by `P_lo` and `Q_lo`, which are *not*
independent of `P_hi` and `Q_hi`.

Secondary, unchanged and not pursued: `r_min(N,0) ≤ 2^{cN}` for some `c<1`.
