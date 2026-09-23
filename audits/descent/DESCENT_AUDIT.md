# Bounded audit: can inheritance + well-ordering give a descent proof of (DE)?

**Scratch area.** Docs and Python only. Nothing under `Divergence/` or `Occupation/` is touched.
All arithmetic below is exact integer arithmetic; no floating-point value enters any decision.

Every claim carries one of: **PROVED** · **VERIFIED** (exact computation, stated finite range) ·
**HEURISTIC** · **OPEN**.

## Setting

`T(m) = (3m+1)/2^{v₂(3m+1)}` on odd `m`; `S_j(m)` the cumulative valuation.
`m` is **zero-confined for `N` steps** if `2^{S_j(m)} ≤ 3^j` for all `1 ≤ j ≤ N`.

* `Z = {positive odd m zero-confined forever}`; **(DE) ⇔ Z = ∅**
  (`Divergence.divergent_iff_zeroConfined`).
* `Z_N = {positive odd m zero-confined for N steps}`; `r_min(N) = min Z_N`.
* `Z_{N+1} ⊆ Z_N` and `Z = ⋂_N Z_N`.

---

# Phase 1 — the inheritance lemmas

## L1 (backward step) — **PROVED**, **VERIFIED**

> If `m ∈ Z_N` and `m ≡ 2 (mod 3)`, then `p = (2m−1)/3` is a positive odd integer with
> `p < m`, `v₂(3p+1) = 1`, `T(p) = m`, and `p ∈ Z_{N+1}`. The same holds with `Z` for `Z_N`.

**Proof.** `m ≡ 2 (mod 3)` gives `2m − 1 ≡ 0 (mod 3)`, so `p ∈ ℤ`. Then `3p + 1 = 2m`, and `m`
odd gives `v₂(2m) = 1`, so `T(p) = m` with first valuation `1`; `3p = 2m − 1` is odd, so `p` is
odd. `p < m ⟺ 2m − 1 < 3m ⟺ −1 < m`. For confinement: the orbit of `p` is `p, m, T(m), …` with
`S_j(p) = 1 + S_{j−1}(m)` for `j ≥ 1`. At `j = 1`, `2¹ = 2 ≤ 3`. For `2 ≤ j ≤ N+1`,

```
2^{S_j(p)} = 2·2^{S_{j−1}(m)} ≤ 2·3^{j−1} ≤ 3·3^{j−1} = 3^j,
```

using `m ∈ Z_N` at index `j−1 ≤ N`. ∎

**VERIFIED**: all odd `m < 2·10⁶` with `m ≡ 2 (mod 3)` and `conf_depth(m) ≥ 1` —
**166 666 cases, 0 failures** (`phase1.py`, `check_L1`).

## L2 (chain length) — **PROVED**, **VERIFIED**

> With `y = (2x−1)/3` one has `y + 1 = 2(x+1)/3`. The backward `d = 1` chain from `x` has
> length **exactly `v₃(x+1)`**, and after `j` steps `y_j + 1 = (2/3)^j (x+1)`, i.e.
> `y_j = 2^j(x+1)/3^j − 1`.

**Proof.** `y + 1 = (2x − 1 + 3)/3 = 2(x+1)/3`. The step is available iff `3 | 2x − 1`, i.e.
`x ≡ 2 (mod 3)`, i.e. `3 | x + 1`. Iterating, `y_j + 1 = 2^j(x+1)/3^j`, which is an integer iff
`3^j | x+1` (as `gcd(2,3) = 1`); so the chain stops exactly after `v₃(x+1)` steps. Each `y_j` is
odd (`y_j + 1 = 2^j·((x+1)/3^j)` is even for `j ≥ 1`) and positive (`x + 1 ≥ 3^j > (3/2)^j`). ∎

**VERIFIED**: all odd `x < 2·10⁶` with `x ≡ 2 (mod 3)` — **333 333 cases, 0 failures**, checking
both the chain length against `v₃(x+1)` and the closed form `(y_j+1)·3^j = 2^j·(x+1)` at every
intermediate `j`.

**This is the structural heart of the audit.** Descent, if it exists, lives at the **3-adic
place** — the contracting place of `3/2` — and its budget is `v₃(x+1)`, not anything 2-adic.

## L3 (only `d = 1` preserves confinement backward) — **PROVED**, **VERIFIED**

> Every preimage `p` of `m` with `v₂(3p+1) = d ≥ 2` fails zero-confinement at the **first** step.

**Proof.** `S_1(p) = d`, and confinement at `j = 1` demands `2^d ≤ 3`, so `d = 1`. ∎

**VERIFIED**: all odd `m < 2·10⁴` and `d = 2..12` giving an integral odd preimage —
**36 663 cases, 0 failures**; every such `p` has `conf_depth(p) = 0`.

So the backward tree inside `Z_N` is a **path**, not a tree: from any node there is at most one
confinement-preserving predecessor, and it exists iff `3 | m+1`.

## L4 (finite-depth residue law) — **PROVED**, **VERIFIED to N = 200**

> `r_min(N) ≢ 2 (mod 3)` for every `N ≥ 1`. Combined with the forced first valuation
> (`2^{S_1} ≤ 3 ⟹ v₂(3m+1) = 1 ⟹ m ≡ 3 (mod 4)`):
>
> **`r_min(N) ≡ 3 or 7 (mod 12)` for every `N ≥ 1`.**

**Proof.** If `r_min(N) ≡ 2 (mod 3)`, L1 gives `p = (2·r_min(N) − 1)/3 ∈ Z_{N+1} ⊆ Z_N` with
`p < r_min(N)`, contradicting minimality. Separately, every `m ∈ Z_N` with `N ≥ 1` has
`2^{v₂(3m+1)} ≤ 3`, hence `v₂(3m+1) = 1`, hence `3m + 1 ≡ 2 (mod 4)`, hence `m ≡ 3 (mod 4)`.
The residues mod 12 that are `≡ 3 (mod 4)` are `{3, 7, 11}`, and `11 ≡ 2 (mod 3)` is excluded. ∎

**VERIFICATION RANGE.** Exhaustive scan of **all odd `m < 10⁸`** (79.7 s), giving `r_min(N)`
for **every `N = 1 … 200`**. All values `≡ 3 or 7 (mod 12)`; `r_min` non-decreasing. The 18
record holders:

| `r_min` | depth | covers `N` | mod 12 | `v₃(m+1)` |
|---:|---:|:---|---:|---:|
| 3 | 1 | 1 | 3 | 0 |
| 7 | 3 | 2–3 | 7 | 0 |
| 27 | 36 | 4–36 | 3 | 0 |
| 703 | 50 | 37–50 | 7 | 0 |
| 10087 | 65 | 51–65 | 7 | 0 |
| 35655 | 84 | 66–84 | 3 | 0 |
| 270271 | 102 | 85–102 | 7 | 0 |
| 362343 | 103 | 103 | 3 | 0 |
| 381727 | 108 | 104–108 | 7 | 0 |
| 626331 | 110 | 109–110 | 3 | 0 |
| 1027431 | 114 | 111–114 | 3 | 0 |
| 1126015 | 140 | 115–140 | 7 | 0 |
| 8088063 | 154 | 141–154 | 3 | 0 |
| 13421671 | 180 | 155–180 | 7 | 0 |
| 20638335 | 183 | 181–183 | 3 | 0 |
| 26716671 | 187 | 184–187 | 3 | 0 |
| 56924955 | 193 | 188–193 | 3 | 0 |
| 63728127 | 200 | 194–200 | 3 | 0 |

**Every record holder has `v₃(m+1) = 0`** — which is L4 restated: a least realizer has **no
backward chain at all**, by L2. The residue law removes exactly the class `11 (mod 12)` from
candidacy, and that class is exactly the part of `Z_1` with `3 | m+1`: of the 750 000 members of
`Z_1` below `3·10⁶`, the residues mod 12 split `{3: 250000, 7: 250000, 11: 250000}`, and the
250 000 with a backward chain are precisely the `11 (mod 12)` ones.

## L5 (forward ladder inheritance) — **PROVED**, **VERIFIED** (finite analogue)

> **Infinite form.** If `m* ∈ Z` then its orbit has infinitely many strict future-maximum times
> `k₁ < k₂ < ⋯`, each restart `m_{k_i} ∈ Z`, and `m_{k₁} < m_{k₂} < ⋯`.

**Proof.** `m* ∈ Z` ⟹ no repeated value (`Divergence.not_zeroConfined_of_repeat`) ⟹ the orbit is
injective ⟹ divergent (`Divergence.injective_iff_divergent`) ⟹ `ρ_n = 2^{S_n}/3^n → 0`
(`Divergence.rho_tendsto_zero`). Since `ρ_n > 0`, for every `n₀` the tail `(ρ_n)_{n ≥ n₀}` has a
last maximum (`Divergence.exists_last_max`), which is a strict future-maximum time `≥ n₀`; hence
infinitely many. By the restart identity `ρ_{k+j} = ρ_k · ρ_j(m_k)`, a strict future maximum at
`k` is exactly `2^{S_j(m_k)} < 3^j` for all `j ≥ 1`, so `m_k ∈ Z`.

Monotonicity is the **future-minimum theorem**: the aggregate identity
`2^{S_n} m_n = 3^n m_0 + C_n` with `C_n > 0` for `n ≥ 1` gives, whenever `2^{S_n} ≤ 3^n`,

```
2^{S_n} m_n > 3^n m_0 ≥ 2^{S_n} m_0   ⟹   m_n > m_0.
```

So each `m ∈ Z` is a **strict future minimum** of its own orbit, and `k₁ < k₂` forces
`m_{k₁} < m_{k₂}`. ∎

> **Finite-depth analogue.** If `m ∈ Z_N`, then `m < m_n` for all `1 ≤ n ≤ N`, and for every
> `k ≤ N` that is a strict future maximum of `ρ` within the window (`ρ_k > ρ_n` for
> `k < n ≤ N`), the restart satisfies `m_k ∈ Z_{N−k}`; these ladder values increase with `k`.

**VERIFIED**: on all 18 record holders (ladder counts 2–12), and on a sweep of all odd
`m < 3·10⁶` with `conf_depth ≥ 3` — **375 000 cases, 0 failures** on all three properties
(future-minimum, restarts confined, ladder values increasing).

## L6 (least element) — **PROVED** (residue) · **VERIFIED, external** (size)

> If `Z ≠ ∅`, then `z₀ = min Z` satisfies `z₀ ≡ 3 or 7 (mod 12)` and `z₀ > 2^71`.

**Proof of the residue.** `z₀ ∈ Z ⟹ z₀ ∈ Z_1 ⟹ z₀ ≡ 3 (mod 4)`. If `z₀ ≡ 2 (mod 3)`, the `Z`-form
of L1 gives `(2z₀ − 1)/3 ∈ Z` strictly smaller, contradicting minimality. Hence
`z₀ ≡ 3 or 7 (mod 12)`. ∎

**Size.** Any `z ∈ Z` has an injective, hence divergent, orbit, so it never reaches `1`; it is a
Collatz counterexample. `z₀ > 2^71` therefore follows from the exhaustive convergence
verification (Bařina). **This is an external computational result, cited and not re-run here.**
Note `1 ∉ Z` independently: `3·1+1 = 4`, so `S_1(1) = 2` and `2² = 4 > 3`.

## Reproduction

```bash
cd audits/descent
python3 phase1.py 2000001     # L1, L2, L3
python3 rmin_scan.py 100000000 # L4 table to N = 200
python3 phase1b.py             # L5 ladder checks, L6 residue census
```

---

*Phases 2–5 follow. L2 and L4 are retained as standalone results regardless of the verdict.*
