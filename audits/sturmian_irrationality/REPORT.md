# Irrationality of the 2-adic Sturmian carry constant — audit

**Scope.** `audits/sturmian_irrationality/`. Exact integer / 2-adic arithmetic only. Every claim
is labelled **PROVED** · **VERIFIED** (exact, finite range) · **HEURISTIC** · **CITED** · **OPEN**.

**Sources**, archived in `sources/`:

| Tag | Note | sha256 | pages |
|---|---|---|---|
| **(A)** | *The 2-Adic Sturmian Carry Constant in the Collatz Carry Equation*, 5 June 2026 | `382cec9fb67b884f…` | 8 |
| **(B)** | *The Sturmian–Mahler Edge of the Accelerated Collatz Realizer Problem*, June 2026 | `dde58e9240588fce…` | 11 |

---

# Phase 0, Task 1 — reconciliation of (A) and (B)

## 1.1 The two constants differ by a sign

(A) Definition 4.1: for an infinite valuation word `w` with partial sums `s_j(w)`,

```
Ξ(w) = Σ_{j≥0} 3^{−(j+1)} 2^{s_j(w)} ∈ ℤ₂ ,        Ξ_α := Ξ(c_α).
```

(B) Theorem 4.1: with `S_i = ⌊iα + β⌋`,

```
Ξ_{α,β} = −(1/3) Σ_{i≥0} 3^{−i} 2^{S_i} = − Σ_{i≥0} 3^{−i−1} 2^{S_i} .
```

The summands are identical term by term once `s_i(w) = S_i`. Hence

> **Ξ_{α,β} = − Ξ(w_β)**, where `w_β` is the mechanical word with `s_i(w_β) = ⌊iα + β⌋`.

## 1.2 The characteristic word is the intercept `β = 0`

(A) §3 defines `c_α` by `d_j = 1 + ⌊(j+1)θ⌋ − ⌊jθ⌋` with `θ = α − 1`, and records
`s_j(c_α) = j + ⌊jθ⌋`. Since `j ∈ ℤ`,

```
s_j(c_α) = j + ⌊j(α−1)⌋ = j + ⌊jα⌋ − j = ⌊jα⌋ = ⌊jα + 0⌋ .
```

So `c_α = w_0`, and therefore

> **`Ξ_{α,0} = − Ξ_α`.**  **PROVED.**

This is the reconciliation. (A) works with `+Ξ_α` and approximants `x_n = Q_n` satisfying
`x_n → −Ξ_α`; (B) works with `Ξ_{α,0} = −Ξ_α` and approximants `Q_n → Ξ_{α,0}`. Irrationality of
one is irrationality of the other, so **Phase 0 may be conducted entirely in (A)'s normalization**,
and its conclusion transfers verbatim to (B)'s Open Problem 1 at `β = 0`.

*Sanity anchor.* (B) Remark 4.2 evaluates the periodic word `(1,2)^∞` to `−5`; (A) §9 records the
same shell `(2,3)` as `Q = −5` with `Ξ((1,2)^∞) = C/δ = 5/1 = 5`. Consistent with the sign
relation.

## 1.3 Orientation of the convergents

(A) §3: `R_n = p_n − q_nα = p'_n − q_nθ` with `p'_n = p_n − q_n`; the shell is **upper** when
`R_n > 0` (`p_n/q_n > α`) and **lower** when `R_n < 0`. Signs alternate (classical). Since
`α > 1`, the first shell `(q_0,p_0) = (1,1)` has `R_0 = 1 − α < 0`: **lower**. Hence

> **lower convergents are exactly the even indices** in (A)'s listing
> `(1,1), (1,2), (2,3), (5,8), (12,19), (41,65), (53,84), (306,485), (665,1054), (15601,24727), …`
> — `n = 0, 2, 4, 6, 8, …` — and there are infinitely many. **PROVED** (alternation is classical).

`X_n` is the **lower** Christoffel (mechanical) block of the shell in both notes, regardless of
whether the shell itself is upper or lower; `|X_n| = q_n`, `S(X_n) = p_n`.

---

# Phase 0, Task 2 — the valuation law, re-derived

## 2.1 Statement

> **(A) Theorem 7.1.** With `x_n = −C_n δ_n^{−1} ∈ ℤ₂`, `δ_n = 3^{q_n} − 2^{p_n}`:
> `x_n → −Ξ_α` in `ℤ₂`, and exactly
>
> ```
> v₂(x_n + Ξ_α) = p_n − 1                  (R_n > 0, upper)
> v₂(x_n + Ξ_α) = p_n + p_{n+1} − 1        (R_n < 0, lower)
> ```

## 2.2 Re-derivation

The proof has three independent parts; I checked each line.

**(i) Periodic-carry identity** ((A) Thm 4.2). Grouping `j = tq + r` and summing the 2-adic
geometric series `Σ_t (3^{−q}2^{S_X})^t`, which converges because `v₂(3^{−q}2^{S_X}) = S_X ≥ 1`,
gives `Ξ(X^∞) = C(X)/δ_X = −Q(X)`. **Checked — correct.** Requires only `S_X ≥ 1`.

**(ii) Floor-comparison** ((A) Lemma 5.1). Put `θ = θ_n + η`, `η = −R_n/q_n`,
`m_j = j p'_n mod q_n`, so `{jθ_n} = m_j/q_n`; `gcd(p'_n, q_n) = 1` gives `m_j ≥ 1` for
`1 ≤ j < q_n` and `m_{q_n} = 0`. Classical best-approximation facts used:
`1/(q_n+q_{n+1}) < |R_n| < 1/q_{n+1}` and `q_{n+1}|R_n| + q_n|R_{n+1}| = 1`.

*Upper (`R_n > 0`).* Mismatch at `j` ⟺ `m_j < jR_n`. For `1 ≤ j < q_n` this fails since
`m_j ≥ 1` while `jR_n < q_nR_n < q_n/q_{n+1} < 1`. At `j = q_n` it holds (`0 < q_nR_n`), and
`−1 < q_nη < 0` gives `⌊q_nθ⌋ = p'_n − 1`. Depths `p_n` and `p_n − 1`. **Checked — correct.**

*Lower (`R_n < 0`).* Mismatch at `j` ⟺ `m_j + j|R_n| ≥ q_n`. Needs `j|R_n| ≥ 1`, so `j > q_{n+1}`.
At `j = q_{n+1}`: `m_{q_{n+1}} = q_n − 1` (from `q_{n+1}p_n − q_np_{n+1} = −1`) and
`m_j + j|R_n| = (q_n−1) + (1 − q_n|R_{n+1}|) < q_n`. For `j = q_{n+1}+i`, `1 ≤ i ≤ q_n−1`:
`m_j = (ip'_n mod q_n) − 1 ≤ q_n − 2` and `j|R_n| < 2`, so no mismatch. At
`j* = q_n + q_{n+1}`: `m_{j*} = q_n − 1` and

```
m_{j*} + j*|R_n| = q_n + q_n(|R_n| − |R_{n+1}|) > q_n ,
```

since `|R_n| > |R_{n+1}|`. Depths `p_n + p_{n+1} − 1` and `p_n + p_{n+1}`. **Checked — correct.**

> ⚠ **Typo in (A).** The displayed line reads `m_{j*} + j*|R_n| = q_n + q_n|R_n| − |R_{n+1}|`;
> the last term should be `q_n|R_{n+1}|`, from `q_{n+1}|R_n| = 1 − q_n|R_{n+1}|`. The inequality
> `> q_n` is unaffected (it needs only `|R_n| > |R_{n+1}|`), so **no consequence for the law**.
> Recorded because the trust chain runs through this line.

**(iii) Ultrametric dominance** ((A) Lemma 6.1). `2^a − 2^b` has `v₂ = min(a,b)` for `a ≠ b`;
letters `≥ 1` force `s_j ≥ s_{j*} + (j − j*)`, so every later term has `v₂ ≥ A + 1` and cannot
cancel the leading one. **Checked — correct.**

## 2.3 Exactly which `n` the law covers

The floor-comparison proof uses, beyond the classical facts:

| hypothesis | where used | holds for |
|---|---|---|
| `gcd(p'_n, q_n) = 1` | `m_j ≥ 1` for `1 ≤ j < q_n` | all `n` |
| `q_n ≥ 2` | the range `1 ≤ i ≤ q_n − 1` is non-empty | `n ≥ 2` |
| `q_{n+1} > q_n` | `q_nR_n < q_n/q_{n+1} < 1` | `n ≥ 1` |
| `S(X_n) = p_n ≥ 1` | convergence of the periodic series | all `n ≥ 0` |

For `α = log₂3` the denominators are `1, 1, 2, 5, 12, 41, 53, 306, 665, 15601, …`, so

> **the law is established for all `n ≥ 2`.** **PROVED** (re-derived).

`n = 0, 1` (both `q = 1`) are outside its scope and are not used below.

---

# Phase 0, Task 3 — the Liouville argument

> **Theorem (irrationality).** `Ξ_α ∉ ℚ`. Equivalently `Ξ_{α,0} ∉ ℚ`, resolving (B)'s Open
> Problem 1 at intercept `β = 0`.

**Proof.** Suppose `Ξ_α ∈ ℚ`.

**Step 1 — the denominator is odd.** `Ξ_α ∈ ℤ₂` by (A) Definition 4.1 (the terms have
`v₂ = s_j → ∞`). A rational lying in `ℤ₂` lies in `ℤ_{(2)}`, so write `Ξ_α = u/v` in lowest terms
with `v ≥ 1` **odd**, `u ∈ ℤ`.

**Step 2 — the integer `M_n`.** For `n ≥ 2` set

```
M_n := u·δ_n − v·C_n ∈ ℤ ,        δ_n = 3^{q_n} − 2^{p_n},   C_n = C(X_n).
```

Since `x_n = −C_n/δ_n`,

```
x_n + Ξ_α = −C_n/δ_n + u/v = M_n / (v·δ_n) .
```

`δ_n` is odd (`3^{q_n}` odd, `2^{p_n}` even, `p_n ≥ 1`) and `v` is odd, so

```
v₂(M_n) = v₂(x_n + Ξ_α) .                                           (★)
```

**Step 3 — `M_n ≠ 0`.** By Task 2 the right side of (★) is a *finite* integer for every `n ≥ 2`.
Hence `x_n + Ξ_α ≠ 0` and `M_n ≠ 0`. *(This is the only place the law's finiteness is used, and it
is exactly the step that fails for a periodic word — see the control in Task 5.)*

**Step 4 — archimedean height bound.** Two estimates.

*Wall.* `|δ_n| ≤ 3^{q_n}`. If `R_n < 0` then `2^{p_n} < 3^{q_n}` and `0 < δ_n < 3^{q_n}`. If
`R_n > 0` then `δ_n < 0` and `|δ_n| = 2^{p_n} − 3^{q_n} = 3^{q_n}(2^{R_n} − 1) < 3^{q_n}`, using
`|R_n| < 1`.

*Carry.* `s_j(X_n) = j + ⌊jθ_n⌋ ≤ j(1 + θ_n) = j·p_n/q_n`, and `p_n/q_n = α + R_n/q_n`, so for
`0 ≤ j ≤ q_n`

```
2^{s_j} ≤ 2^{j p_n/q_n} = 3^{j}·2^{jR_n/q_n} ≤ 3^{j}·2^{|R_n|} < 2·3^{j} ,
```

whence every term of `C_n = Σ_{j<q_n} 3^{q_n−1−j}2^{s_j}` is `< 2·3^{q_n−1}` and

```
C_n < 2 q_n 3^{q_n−1} < q_n 3^{q_n} .
```

Therefore, with `H := max(|u|, v) ≥ 1`,

```
0 < |M_n| ≤ |u|·|δ_n| + v·C_n < (|u| + v q_n)·3^{q_n} ≤ 2H q_n · 3^{q_n} .   (†)
```

**Step 5 — the contradiction, at lower convergents.** A nonzero integer satisfies
`|M_n| ≥ 2^{v₂(M_n)}`. Let `n ≥ 2` be **lower** (`R_n < 0`). By (★) and Task 2,
`v₂(M_n) = p_n + p_{n+1} − 1`, so with (†)

```
2^{p_n + p_{n+1} − 1} < 2H q_n · 3^{q_n} .
```

Taking `log₂` and using `q_nα = p_n − R_n = p_n + |R_n|`:

```
p_n + p_{n+1} − 1 < log₂(2H q_n) + q_nα = log₂(2H q_n) + p_n + |R_n| ,
```

hence, since `|R_n| < 1`,

```
p_{n+1} < 2 + log₂(2H) + log₂ q_n .                                  (‡)
```

But `p_{n+1} > q_{n+1} > q_n`, so (‡) forces `q_n < 2 + log₂(2H) + log₂ q_n`, which fails for every
`q_n` exceeding an explicit bound depending only on `H`. Since there are infinitely many lower
convergents (Task 1.3) and `q_n → ∞`, (‡) fails for all large even `n`. Contradiction. ∎

**Why only lower convergents.** At an upper convergent `v₂(M_n) = p_n − 1` and the same chain
gives `p_n − 1 < log₂(2Hq_n) + p_n + |R_n|`, i.e. `0 < 1 + |R_n| + log₂(2Hq_n)` — vacuous. The
argument needs the extra full continued-fraction level `p_{n+1}` that (A) Remark 5.2 identifies as
structural: `c_α` is the limit of *lower* mechanical words, so lower-convergent periodic extensions
agree with it one level longer. **The irrationality rests precisely on that asymmetry.**

**Effectivity.** The proof is effective: the contradiction appears at the first lower convergent
with `q_n ≥ 2 log₂(2H) + 10` (crudely), i.e. at continued-fraction depth `O(log log H)` for
`log₂3`. This is the input to Phase 2.

**Dependencies, stated exactly.**

1. (A) Theorem 4.2 — re-derived, Task 2(i). **PROVED**.
2. (A) Lemma 5.1 — re-derived, Task 2(ii), one typo noted without consequence. **PROVED for `n ≥ 2`**.
3. (A) Lemma 6.1 — re-derived, Task 2(iii). **PROVED**.
4. Classical continued-fraction facts: alternation of `R_n`, `1/(q_n+q_{n+1}) < |R_n| < 1/q_{n+1}`,
   `q_{n+1}|R_n| + q_n|R_{n+1}| = 1`, `|q_np_{n+1} − q_{n+1}p_n| = 1`. **CITED** (standard).
5. **No property of the continued fraction of `log₂3` beyond `q_n → ∞` is used.** In particular no
   irrationality measure for `α`, and no bound on its partial quotients. *(By contrast (A)'s
   window criterion (3) does need `log q_{n+1} = o(p_n)`; the Liouville argument does not.)*

---

---

# Phase 0, Task 4 — numerical verification

`Ξ_α mod 2^K` by the carry recursion `A ← 3A + 2^{s_j}` with `s_j = ⌊jα⌋ = bitlen(3^j) − 1`
(exact), then `Ξ ≡ 3^{−J}A_J`; `C_n` by the same recursion over `q_n` steps with
`s_j(X_n) = ⌊j p_n/q_n⌋`; `x_n ≡ −C_n δ_n^{−1} (mod 2^K)`. No float enters. Convergents from a
Stern–Brocot descent whose only primitive is the exact comparison `2^p < 3^q ⟺ p < bitlen(3^q)`;
the shell list reproduces (A) §3 exactly, including `(190537, 301994)`.

`Ξ_α mod 2^64 = 5980427723603026949`.

| `n` | `q_n` | `p_n` | side | law `ℓ_n` | observed `v₂(x_n+Ξ_α)` | match |
|---:|---:|---:|:---|---:|---:|:---:|
| 2 | 2 | 3 | lower | 10 | 10 | ✓ |
| 3 | 5 | 8 | upper | 7 | 7 | ✓ |
| 4 | 12 | 19 | lower | 83 | 83 | ✓ |
| 5 | 41 | 65 | upper | 64 | 64 | ✓ |
| 6 | 53 | 84 | lower | 568 | 568 | ✓ |
| 7 | 306 | 485 | upper | 484 | 484 | ✓ |
| 8 | 665 | 1054 | lower | 25780 | 25780 | ✓ |
| 9 | 15601 | 24727 | upper | 24726 | 24726 | ✓ |
| 10 | 31867 | 50508 | lower | 176250 | 176250 | ✓ |
| 11 | 79335 | 125743 | upper | 125742 | 125742 | ✓ |
| 12 | 111202 | 176251 | lower | 478244 | 478244 | ✓ |

**VERIFIED**: the law holds exactly at every shell `n = 2 … 12`, upper and lower, at `K = 480000`
(29 s). This passes the brief's target `(79335, 125743)` by one further level.

## The finite consequence, made explicit

Each lower convergent forces, for a hypothetical `Ξ_α = u/v` of height `H = max(|u|, v)`,
`H > 2^{ℓ_n}/(2 q_n 3^{q_n})`. Using `⌊q_nα⌋ = p_n` at lower convergents (checked exactly):

| `n` | `ℓ_n` | excludes all heights `H` with `log₂H` below |
|---:|---:|---:|
| 2 | 10 | 5 |
| 4 | 83 | 59 |
| 6 | 568 | 477 |
| 8 | 25780 | 24716 |
| 10 | 176250 | 125726 |
| 12 | 478244 | **301975** |

> **VERIFIED:** `Ξ_α` is not a rational number of height `≤ 2^{301975}`.

That is the finite, machine-checked shadow of the theorem. Full irrationality follows from the
law at *all* `n`, which is PROVED (Task 2), not merely verified.

---

# Phase 0, Task 5 — controls

The template must **not** fire on a rational point. For the rational `−x_m = C_m/δ_m` the
analogue of `M_n` is `M_n^{(m)} = C_m δ_n − δ_m C_n`, computed here in **exact integers** (no
modular reduction), with `v₂(M_n^{(m)}) = v₂(x_n − x_m)`.

`x_2 = −C_2/δ_2 = −5/1 = −5`, the `(1,2)^∞` point — so `m = 2` *is* the requested `−5` control.

| `n` | `v₂(x_n + 5)` | `log₂\|M_n\|` | `q_n log₂3` |
|---:|---:|---:|---:|
| 3 | 7 | 9 | 7 |
| 4 | **10** | 21 | 19 |
| 5 | **10** | 69 | 64 |
| 6 | **10** | 88 | 84 |
| 7 | **10** | 492 | 484 |
| 8 | **10** | 1062 | 1054 |
| 9 | **10** | 24739 | 24726 |

**Frozen at 10 = ℓ_2 = p_2 + p_3 − 1** from `n = 4` on. (At `n = 3` the value is
`min(ℓ_2, ℓ_3) = min(10, 7) = 7`, exactly as the ultrametric predicts.) Two further controls:

| fixed `m` | `ℓ_m` | frozen value of `v₂(x_n − x_m)` | from |
|---:|---:|---:|---|
| 2 | 10 | **10** | `n ≥ 4` |
| 4 | 83 | **83** | `n ≥ 6` |
| 6 | 568 | **568** | `n ≥ 8` |

In every row `2^{v₂(M_n)} ≤ \|M_n\|` holds comfortably — **no contradiction is produced**.

## Why the template cannot fire on a rational point

The Liouville step needs `2^{v₂(M_n)} ≤ |M_n| < 2Hq_n3^{q_n}` to be *violated*, i.e. it needs
`v₂(M_n)` to outgrow `q_n log₂3 + O(log q_n)`. At a rational point `−x_m`,

```
v₂(M_n^{(m)}) = v₂( (x_n + Ξ_α) − (x_m + Ξ_α) ) = min(ℓ_n, ℓ_m) = ℓ_m   for ℓ_n > ℓ_m,
```

a **constant**, while `log₂|M_n|` grows linearly in `q_n`. The inequality is therefore satisfied
for every `n` and no contradiction arises. The freeze is not an accident of the computation: it
is the ultrametric identity above, and it happens at exactly the depth where `c_α` first
disagrees with the periodic word `X_m^∞`.

Against this, at the true point the valuation is `ℓ_n = p_n + p_{n+1} − 1` at lower convergents,
which exceeds `q_nα + O(log q_n) = p_n + O(log q_n)` by the full amount `p_{n+1}`. **The
argument fires only on the unbounded growth of the approximation depth, which a rational point
cannot have.** Step 3 of the proof (`M_n ≠ 0`) and Step 5 (the growth) are precisely the two
places a rational target fails.

---

# Phase 0 — VERDICT

| Task | Result |
|---|---|
| 1 — reconciliation | **PROVED**: `Ξ_{α,0} = −Ξ_α`; `c_α` is intercept `β = 0`; lower shells are the even indices |
| 2 — valuation law re-derived | **PROVED for `n ≥ 2`**; one typo in (A) recorded, no consequence |
| 3 — Liouville argument | **PROVED** |
| 4 — numerics | **VERIFIED**, shells `n = 2…12`, `K = 480000`, all 11 exact matches |
| 5 — controls | **PASS**: frozen at `ℓ_m`; template correctly fails to fire |

> ## **Phase 0: PROVED.**  `Ξ_α ∉ ℚ`, equivalently `Ξ_{α,0} ∉ ℚ`.

Scope, exactly: the **characteristic** point, intercept `β = 0`. (B)'s Open Problem 1 asks this
for every `β`; Phase 1 addresses the rest.

## Reproduction

```bash
cd audits/sturmian_irrationality
python3 cf.py 300000        # exact convergents
python3 task4.py 480000 12  # valuation law, shells 2..12   (~30 s)
python3 task5.py            # rational-point controls
```


---

# Phase 1c — irrationality of `Φ(c_s)` for every irrational slope

Raw-map (parity-vector) coordinates: `T(x) = x/2` (even), `(3x+1)/2` (odd) on `ℤ₂`; `Φ(v)` is the
unique `x ∈ ℤ₂` with parity vector `v`. Working directory `phase1c/`.

## Task 0 — López–Stoll comparison: **BLOCKED**

> J. López, P. Stoll, *The 3x+1 conjugacy map over a Sturmian word*, **Integers 9** (2009) A13.

**The PDF is not in `sources/` and is not present anywhere on this machine** (searched
`~/Downloads`, `~/GitHub`, `~/Documents`). This session's web-search budget is also exhausted.
Per the brief's own instruction — *"otherwise STOP and ask me for it"* — **Task 0 is stopped and
the paper is requested.**

Consequence for the audit: the stop rule *"STOP at Task 0 if López–Stoll already prove it"*
**cannot be evaluated**. Everything below is therefore framework only, and **no novelty or
priority claim is made or may be made** until Task 0 is completed. It is entirely possible that
López–Stoll, or the `arXiv:2101.12747` line, already contains part or all of Task 3.

## Task 1 — framework

### 1.1 Isometry — **CITED**, verified

> **Bernstein–Lagarias (1996)**, *The 3x+1 conjugacy map*, Canad. J. Math. **48**: the parity-vector
> map `Q : ℤ₂ → ℤ₂` is a 2-adic **isometry** conjugating `T` to the shift. Hence with `Φ = Q^{-1}`,
> `|Φ(v) − Φ(w)|₂ = |v − w|₂`, i.e.
>
> ```
> v₂( Φ(v) − Φ(w) )  =  length of the longest common prefix of v and w.
> ```

**VERIFIED**: 200 random pairs agreeing to a prescribed length `L` and differing at `L`, at
`K = 400`: `v₂(Φ(a) − Φ(b)) = L` in every case.

### 1.2 Closed form — **PROVED**, verified

`T(x) = (3^{v}x + v)/2` with `v = x mod 2`, so `2x_{j+1} = 3^{v_j}x_j + v_j`. With
`k_j = #{i < j : v_i = 1}`, induction gives

```
2^j x_j  =  3^{k_j} x_0  +  Σ_{i<j} 3^{k_j − k_{i+1}} 2^i v_i .
```

Dividing by `3^{k_j}` and letting `j → ∞` — the remainder `2^j 3^{−k_j} x_j` has `v₂ ≥ j → 0` in
`ℤ₂` — yields

> ```
> Φ(v)  =  − Σ_{i : v_i = 1} 3^{−k_{i+1}} 2^{i} ,        k_{i+1} = #{ i' ≤ i : v_{i'} = 1 } .
> ```

*Check.* `v = 1^∞`: `k_{i+1} = i+1`, so `Φ = −⅓Σ(2/3)^i = −1`. ✓ `v = 0^∞ ↦ 0`. ✓

**VERIFIED**: `Φ(1^∞) ≡ −1` and `Φ(0^∞) = 0` mod `2^400`; and for 200 random words the closed
form's output, iterated through `T` for 200 steps, reproduces the prescribed parity vector exactly.

### 1.3 Periodic words — **PROVED**, verified; **and a correction to the stated height bound**

Grouping `i = tℓ + r` and summing the 2-adic geometric series `Σ_t (2^ℓ3^{−k})^t`
(`v₂(2^ℓ3^{−k}) = ℓ ≥ 1`):

> ```
> Φ(w^∞)  =  c_w / (2^ℓ − 3^k) ,      c_w = Σ_{r<ℓ, w_r=1} 3^{\,k − κ_{r+1}} 2^{r} ∈ ℤ ,
> ```

with `κ_{r+1} = #{i ≤ r : w_i = 1}`. **VERIFIED** against the closed form for 300 random periods
of length `≤ 14`, mod `2^400`: exact agreement in every case.

> ⚠ **The height bound `|c_w| ≤ ℓ·max(2^ℓ, 3^k)` is FALSE for general `w`.**
>
> Writing `a_r = k − κ_{r+1}` (ones strictly after `r`), the term is `3^{a_r}2^{r}`. For a word
> whose ones are all at the *end*, `a_r` and `r` are both large together and the term outruns
> both `2^ℓ` and `3^k`. Explicitly, for `w = 0^{10}1^{10}`:
> ```
> c_w = 1024·(3^{10} − 2^{10}) = 59 417 600 ,   ℓ·max(2^ℓ,3^k) = 20·2^{20} = 20 971 520 ,
> ```
> a ratio of **2.83**. Exhaustive search over *all* words of each length shows the first failure
> at `ℓ = 10` (`w = 0000111111`, ratio 1.039) and the ratio growing steadily — 4.75 at `ℓ = 18`,
> with the extremal witness always of the form `0^a1^b`. It is unbounded.

The bound **does** hold once the word is balanced, which is the only case Task 3 needs:

> **Proposition (corrected height bound).** If `w` is a mechanical word of length `ℓ` with `k`
> ones, then `|c_w| ≤ 3ℓ · max(2^ℓ, 3^k)`.
>
> *Proof.* Balance gives `a_r ≤ s(ℓ−1−r) + 1` with `s = k/ℓ`. Hence
> `3^{a_r}2^r ≤ 3·2^{\,r + s(ℓ−1−r)log₂3}`, whose exponent is **linear** in `r`, so the maximum is
> at an endpoint: `r = 0` gives `≤ 3·3^{k}`, `r = ℓ−1` gives `≤ 3·2^{ℓ−1}`. Summing `≤ ℓ` terms
> gives the claim. ∎

**VERIFIED**: over **all** Christoffel words with `q < 400` (48 000-odd words), the worst value of
`|c_w| / (ℓ·max(2^ℓ,3^k))` is **0.4531**, at `(p,q) = (200,317)` — so even the un-corrected
constant holds comfortably on mechanical words. The factor 3 in the Proposition is slack.

**Effect on the plan.** `log₂|c_w| ≤ max(ℓ, k·log₂3) + log₂(3ℓ)`, which is exactly the ceiling
Task 1.4 asks for, with `O(1) = log₂3`. So Task 3's arithmetic is unaffected — but the
balancedness hypothesis must be carried explicitly, and a version of Task 3 applied to arbitrary
periodic approximants would be **unsound**.

## Reproduction

```bash
cd audits/sturmian_irrationality/phase1c
python3 conj.py      # 1.1 isometry, 1.2 closed form, 1.3 periodic values
python3 height.py    # the height-bound counterexample and the mechanical-word scan
```
