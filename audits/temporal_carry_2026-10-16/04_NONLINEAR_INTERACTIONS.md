# 04_NONLINEAR_INTERACTIONS.md

All identities below are exact and were verified by exhaustive/large-sample integer arithmetic.

## 1. Single perturbation `[PROVED]`

Bumping `d_i → d_i + ε` leaves `S_j` unchanged for `j ≤ i` and multiplies `2^{S_j}` by `2^ε` for
`j > i`.  Splitting the sum at `i`:
```
Δ_i C_N = (2^ε − 1) · T_i ,        T_i = Σ_{j>i} 3^{N−1−j} 2^{S_j} .
```
**Verified exactly on 15 000 `(word, i, ε)` triples, 0 failures** (`results/run_derive.txt`, P1).

The temporal position enters **only** through `T_i`, the carry mass after `i`.  This is already
the whole of "temporal differentiation" at first order.

## 2. Second difference — the interaction term `[PROVED]`

With `A = Σ_{j≤i}`, `B = Σ_{i<j≤k}`, `D = Σ_{j>k}` (so `T_i = B + D`, `T_k = D`),
```
C_N(ε_i, ε_k) = A + 2^{ε_i} B + 2^{ε_i+ε_k} D ,
```
whence
```
Δ_i Δ_k C_N = (2^{ε_i} − 1)(2^{ε_k} − 1) · T_k .
```
**Verified exactly on 66 600 `(word, i, k, ε_i, ε_k)` tuples, 0 failures.**

The interaction is **nonzero** — there is genuine coupling between temporal positions — but it is
**multiplicatively separable**:
```
Δ_i Δ_k C_N  =  (Δ_i C_N · Δ_k C_N) / T_i .
```
**Verified exactly on 7 200 `(word, i, k)` pairs, 0 failures.**

> **This is the central structural finding.**  The second difference is a *function* of the two
> first differences and the tail `T_i`.  It carries no information absent from them.  The entire
> "nonlinear dependence of the carry on parity/exponent history" is the identity
> `2^{a+b} = 2^a 2^b`, which is exactly separable — the opposite of the irreducible coupling the
> hypothesis anticipated.

Higher differences follow the same pattern for the same reason: `C_N` is an affine function of
the vector `(2^{S_0}, …, 2^{S_{N−1}})`, and the word acts on that vector by independent scalings.

## 3. The brief's four-way distinction, answered

| effect | present? | verdict |
|---|---|---|
| trivial exponential sensitivity | **yes** | `(2^ε − 1)T_i` is exactly this, and it is all of first order |
| altered terminal exponent sum | **yes, and it is a confound** | a single bump changes `S_N`, so the two realizers have different moduli; this is why only the `S_N`-preserving swap is admissible |
| modular wraparound | **yes, and it is a representative artefact** | `Δr_N` is defined mod `2^{S_N}`; the integer odd part is not well defined (`02_TEMPORAL_MODEL.md` §3) |
| genuine arithmetic interaction not implied by known formulas | **no** | §2: the interaction factorises exactly |

## 4. Survival into the realizer

The swap gives `ΔC_N = W_{i,k}` exactly (**19 774 swaps, 0 failures**), and since `S_j` is
strictly increasing the `j = i+1` term has strictly least valuation, so
```
v_2(W_{i,k}) = S_{i+1}      exactly        (19 751 swaps, 0 failures).
```
Passing to the realizer, `Δr_N ≡ −W_{i,k} 3^{−N} (mod 2^{S_N})`, so the valuation survives
unchanged and the rest is `05_CANDIDATE_LEMMAS.md` Lemma T+.

**Nothing is lost and nothing is gained in the passage from carry to realizer**: multiplication
by the unit `−3^{−N}` is a bijection on residues preserving `v_2`.
