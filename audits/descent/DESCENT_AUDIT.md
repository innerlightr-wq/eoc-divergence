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

**Two bookkeeping consequences, not evidence.** Both of the following are *restatements* of what
is already proved, and are recorded only because they make the mechanism legible:

* Every record holder has `v₃(m+1) = 0`. This is **L4 read through L2**: `r_min ≢ 2 (mod 3)` is
  exactly `3 ∤ r_min + 1`, which by L2 says the backward chain from a least realizer has length
  zero. It is a consequence of L4, not independent corroboration of it.
* The residue census of `Z_1` below `3·10⁶` splits `{3: 250000, 7: 250000, 11: 250000}` with
  exactly the `11 (mod 12)` third carrying a backward chain. This is forced by
  `Z_1 = {m ≡ 3 (mod 4)}` together with `m ≡ 2 (mod 3) ⟺ 3 | m+1`; the equal thirds are
  arithmetic, not data.

## L5 (forward ladder inheritance) — **PROVED**, **VERIFIED** (finite analogue)

> **Infinite form.** If `m* ∈ Z` then its orbit has infinitely many strict future-maximum times
> `k₁ < k₂ < ⋯`, each restart `m_{k_i} ∈ Z`, and `m_{k₁} < m_{k₂} < ⋯`.

**Why "weak" is automatically "strict".** A weak future maximum would allow `ρ_{k+j} = ρ_k` for
some `j ≥ 1`, i.e. `2^{S_{k+j} − S_k} = 3^j`, i.e. `S_{k+j} − S_k = jα`. The left side is an
integer and `α = log₂3` is irrational, so this is impossible for `j ≥ 1`. (Equivalently:
`2^a = 3^j` has no solution with `j ≥ 1`, by unique factorisation.) Every future maximum is
therefore strict, and "ladder time" is unambiguous.

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

---

# Phase 2 — controls (each must fail, and the failure point must be named)

## C1 — the 2-adic integers: **fails at well-ordering**

The backward `d = 1` map `y = (2x−1)/3` is **total on `ℤ₂`**, because `3` is a unit there
(**VERIFIED**: total on `ℤ/2^64`, all residues). The zero-confined set `K ⊆ ℤ₂` is closed under
it, by the same computation as L1. And `−1` is a fixed point: `(2(−1)−1)/3 = −1`
(**VERIFIED** as `2^64 − 1`, the unique fixed point).

**Exact point of failure — two of them.**

1. `ℤ₂` carries no order, so `K` has no least element. The well-ordering step of any descent
   argument has no analogue.
2. L4's mechanism is vacuous: the residue hypothesis `m ≡ 2 (mod 3)` is no longer a restriction,
   since `3` is invertible. There is no "`v₃(x+1) = 0`" obstruction to inherit.

At `x = −1` the budget is `v₃(0) = ∞`: unlimited backward motion that never decreases anything.

## C2 — the negative integers: **fails at the fixed point**

* `−1` is a fixed point of both the forward and the backward map, and is zero-confined forever
  (**VERIFIED** to depth 200).
* `{−5, −7}` is a zero-confined cycle: `S_{2t} = 3t` and `8^t ≤ 9^t` for every `t`
  (**VERIFIED**: `depth(−5) = 200`, capped). So `Z⁻ ≠ ∅`.
* `−5` has `v₃(−5+1) = v₃(−4) = 0` — a dead end, the exact analogue of a least realizer with no
  backward chain (**VERIFIED**).

**Exact point of failure.** The backward fixed point `−1` lies **inside** the set. Descent from
it loops forever at the same value, so no strictly decreasing chain exists and no contradiction
is reached, even though `Z⁻ ≠ ∅`.

## C3 — `3x − 1` on the positive integers: **fails at `p < m`**

For `T'(m) = (3m−1)/2^{v₂(3m−1)}` the valuation-`1` preimage is `p = (2m+1)/3`, and the mirrored
chain law is `y − 1 = 2(x−1)/3`, so the backward chain from `x` has length exactly `v₃(x−1)`
(**VERIFIED**: all odd `x < 2·10⁶` with `x ≡ 1 (mod 3)` — **333 333 cases, 0 failures**, chain
length and closed form `(y_j−1)·3^j = 2^j(x−1)`).

`m = 1` is a fixed point of `T'` and is zero-confined forever (**VERIFIED** to the cap), so the
analogue of (DE) is **false** here.

**Exact point of failure, and where the sign of the `+1` enters.**

| | `3x+1` | `3x−1` |
|---|---|---|
| backward `d=1` map | `y = (2x−1)/3` | `y = (2x+1)/3` |
| chain law | `y+1 = 2(x+1)/3` | `y−1 = 2(x−1)/3` |
| budget | `v₃(x+1)` | `v₃(x−1)` |
| backward fixed point | `x = −1` | `x = +1` |
| fixed point positive? | **no** | **yes** |
| `p < m` holds iff | `−1 < m` — always | `1 < m` — **fails at `m = 1`** |

L1's strict decrease `p < m` is equivalent to `−1 < m` for `3x+1` and to `1 < m` for `3x−1`. In
the second case it fails at exactly one point, the fixed point, and that single point is where
the descent breaks. **VERIFIED**: `(2·1+1)/3 = 1`, so `p = m`, not `p < m`.

This is the precise sense in which descent for `3x+1` depends on the `+1`: it places the backward
fixed point at `−1`, outside the positive integers, so the strict inequality `p < m` is
unconditional. Any proposed descent mechanism that does not use this — and so would "succeed" on
C3 — is invalid. **The L1/L4 mechanism does not succeed on C3**: L4's proof needs `p < r_min`
strictly, and at `m = 1` it does not hold, so no false conclusion is produced.

---

# Phase 3 — the round-trip criterion

## The move set on `Z`

Exactly two moves preserve membership in `Z`:

* **F (forward to a ladder time).** From `z ∈ Z` go to `m_k` for `k` a strict future-maximum time
  of `ρ`. Then `m_k ∈ Z` (L5) and, by the future-minimum theorem, `m_k > z`. **F always increases.**
* **B (backward `d = 1` step).** From `x ∈ Z` with `3 | x+1` go to `y = (2x−1)/3 < x` (L1). By
  L2 it is available exactly `v₃(x+1)` times in a row, landing at `y_j = 2^j(x+1)/3^j − 1`. By
  L3 no other backward step preserves confinement: the backward structure is a **path**, not a tree.

The set reachable from `z₀` is therefore the set of all `y_j` obtained by: choose a ladder time
`k`, then take `j ≤ v₃(m_k+1)` backward steps. A descent proof needs one such element below `z₀`.

**By L4 the first move from `z₀` must be F**, since `v₃(z₀+1) = 0`.

## The exact condition

`y_j < z₀ ⟺ 2^j(m_k+1)/3^j − 1 < z₀ ⟺ 2^j(m_k+1) < 3^j(z₀+1)`. So a descending round trip
exists iff

> **(RT)** there is a ladder time `k` and an integer `j` with
> `j ≤ v₃(m_k + 1)` and `2^j (m_k + 1) < 3^j (z₀ + 1)`,

equivalently `v₃(m_k+1) > log_{3/2}\big((m_k+1)/(z₀+1)\big)`.

In `ρ`-form, with `ρ_k = 2^{S_k}/3^k` and the product identity `ρ_k m_k = z₀ Q_k`,
`1 < Q_k ≤ Q_∞`, one has `m_k ≍ z₀/ρ_k = z₀·2^{D_k}` where `D_k = kα − S_k = −R_k ≥ 0` is the
drift deficit. So the requirement reads

```
        v₃(m_k + 1)   ≳   D_k / (α − 1)   ≈   1.7095 · D_k .
```

Along the ladder `D_{k_1} < D_{k_2} < ⋯ → ∞`, so **the requirement grows without bound**.

## L7 (lockstep invariance) — **PROVED**, **VERIFIED**. *The decisive obstruction.*

> Under a forward step with `d = 1`, both sides of (RT) advance by exactly one:
> `v₃(m_{k+1}+1) = v₃(m_k+1) + 1` and `j_req(m_{k+1}) = j_req(m_k) + 1`.
> Hence the **surplus** `σ_k := v₃(m_k+1) − j_req(m_k)` is **invariant** under `d = 1` steps.

**Proof.** If `d = 1` then `m_{k+1} = (3m_k+1)/2`, so `m_{k+1} + 1 = 3(m_k+1)/2`. Since `2` is a
unit at `3`, `v₃(m_{k+1}+1) = v₃(m_k+1) + 1`. For the requirement, substituting
`m_{k+1}+1 = (3/2)(m_k+1)` into (RT) at exponent `j+1`,

```
2^{j+1}(m_{k+1}+1) = 3·2^j(m_k+1)   and   3^{j+1}(z₀+1) = 3·3^j(z₀+1),
```

so (RT) holds at `(k+1, j+1)` iff it holds at `(k, j)`; the least admissible `j` shifts by
exactly one. ∎

**VERIFIED**: **1297 forward `d = 1` steps across the 16 deepest record holders, 0 failures** on
all three assertions.

**Starting value.** At `k = 0`, `j_req(z₀) = 1` (the least `j` with `2^j < 3^j`) and
`v₃(z₀+1) = 0` by L4, so `σ_0 = −1`. A round trip needs `σ_k ≥ 0`.

**What `d ≥ 2` does.** `m_{k+1} + 1 = (3(m_k+1) + 2^d − 2)/2^d`, and `2^d ≡ 2 (mod 3)` iff `d`
is odd. So:

* **`d` even ⟹ `3 ∤ m_{k+1}+1` ⟹ `v₃ = 0`: the budget is destroyed.**
  **VERIFIED**: 530 of 530 even-`d` steps destroy it.
* `d` odd `≥ 3` ⟹ the budget survives and resets to `1 + v₃(m_k + 1 + (2^d−2)/3)` — a *fresh*
  quantity, not an accumulated one. **VERIFIED**: 182 of 182 odd-`d` steps leave it nonzero-capable.

So the surplus starts at `−1`, is frozen by the dominant `d = 1` steps, is reset to a deficit by
every even-`d` step, and can only be raised by an odd `d ≥ 3` step — which simultaneously buys a
fresh geometric budget and cuts the requirement by `(d − α)/(α − 1)`.

## Classification of (RT)

**(b) — equivalent to (DE). PROVED.**

Let **P** = "every `z ∈ Z` admits a descending round trip". If (DE) holds then `Z = ∅` and P is
vacuously true. Conversely, if P holds and `Z ≠ ∅`, applying P to `z₀ = min Z` produces
`y_j ∈ Z` with `y_j < z₀` (membership by L1 iterated), contradicting minimality; so `Z = ∅`.
Hence **P ⟺ (DE)**.

Proving P is therefore exactly as hard as proving (DE). This is the generic trap for descent
schemes: any statement of the form "every element of `Z` has a property that yields a
contradiction" is equivalent to `Z = ∅` and carries no independent leverage.

**(c) — and, conditionally on `Z ≠ ∅`, plausibly false. HEURISTIC.**

If `Z ≠ ∅`, the orbit of `z₀` diverges, so `D_{k_i} → ∞` strictly along the ladder and the
requirement `j_req` is unbounded and non-decreasing. By L7 the budget is not accumulated: it is
reset at every step with `d ≥ 2` and merely tracks the requirement at every step with `d = 1`.
Modelling the reset budget as geometric with `P(v₃ ≥ j) = 3^{−j}`, the expected number of
descending round trips along the whole orbit is `Σ_i 3^{−j_req(k_i)} < ∞`, and small. There is no
mechanism forcing even one.

---

# Phase 4 — the pre-registered experiment

The Phase 3 table *is* the Phase 4 experiment: for each record holder `z` (proxy for `z₀`) and
each ladder time `k ≥ 1` within the confined window, the available budget `v₃(m_k+1)` against the
required `j`.

| quantity | value |
|---|---|
| ladder times examined (`k ≥ 1`, 16 record holders) | **67** |
| descending round trips **observed** | **4** |
| geometric baseline `Σ 3^{−j_req}` | **6.86** |

Observed successes (all with tiny requirement, `j_req ∈ {1,2}`):
`z=10087` at `k=64,65`; `z=270271` at `k=102`; `z=626331` at `k=105`.

**Round trips are no more frequent than the geometric baseline predicts — in fact fewer
(4 vs 6.86).** There is no structural forcing.

The observed `v₃` distribution over ladder values is shifted upward relative to geometric
(`v₃ = 0` seen 36% against 67%), but this is **not** evidence of forcing: it is L7. Consecutive
ladder values often sit in a `d = 1` run, where `v₃` increases by one per step — and so does the
requirement, leaving the surplus unchanged.

All four observed successes occur where the orbit had come back *close to* `z` (e.g.
`m_64 = 13667` against `z = 10087`, a ratio of 1.36), keeping `j_req` at 1 or 2. For a genuine
`z₀ ∈ Z` this cannot persist: `ρ_k → 0` forces `m_{k_i}/z₀ → ∞` along the ladder. **The finite-depth
successes are an artefact of `Z_N` elements whose orbits do not actually diverge.**

---

# Verdict: **STOP**

The pre-registered rule fires twice, independently:

1. **Phase 3 lands in (b)** — (RT) is *proved* equivalent to (DE) — **and in (c)**: conditionally
   on `Z ≠ ∅`, the required 3-adic coincidence is exponentially unlikely and nothing forces it.
2. **Phase 4 shows round trips are no more frequent than the geometric baseline** (4 observed vs
   6.86 expected).

The CONTINUE condition is not met: Phase 3 found **no** structural reason for ladder-time values
to carry forced 3-adic anomalies. It found the opposite — **L7**, a proved statement that the
dominant forward move advances budget and requirement at exactly the same rate, so the surplus
cannot be accumulated by forward motion at all.

**Inheritance plus well-ordering does not yield a descent proof of (DE).** The three controls
localise why a descent argument could ever work here (the backward fixed point `−1` is not a
positive integer, C3), and L7 localises why this particular one cannot (the budget is frozen
along `d = 1` and reset along even `d`).

## Results retained regardless of the verdict

* **L2** — the backward `d = 1` chain from `x` has length exactly `v₃(x+1)`. Descent lives at
  the **3-adic place**, the contracting place of `3/2`, and `v₃(x+1)` is its entire budget.
* **L4** — `r_min(N) ≡ 3 or 7 (mod 12)` for every `N ≥ 1`. Verified exhaustively for
  `N = 1…200` by scanning all odd `m < 10⁸`.
* **L7** — the lockstep invariance. New here, and the reason the criterion cannot be met by
  forward motion.

## Reproduction

```bash
cd audits/descent
python3 phase1.py 2000001        # L1, L2, L3
python3 rmin_scan.py 100000000   # L4 table to N = 200
python3 phase1b.py               # L5 ladder checks, residue census
python3 phase2.py                # C1, C2, C3 controls
python3 phase3.py                # round-trip criterion at ladder times
python3 phase3b.py               # L7 lockstep invariance
```
