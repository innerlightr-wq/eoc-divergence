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

# Phase 3 — literature check

## Method, and its limits — stated first

This session's **web-search budget was exhausted (200/200)** before Phase 3 began. The check below
was made against the **arXiv API only**. It is therefore **incomplete**:

* no MathSciNet / zbMATH / Google Scholar;
* abstract- and title-level only, not full texts;
* journal-only papers (e.g. **López–Stoll, Integers 9 (2009) A13**) are invisible to it — and that
  paper is separately requested in Phase 1c Task 0;
* **Calegari–Dimitrov–Tang** (arithmetic holonomy bounds) was **not checked at all**.

**Accordingly: no novelty claim is asserted anywhere in this audit.** What follows is what the
search found, plus a structural argument that is independent of any search.

## What the search returned

`all:"Hecke-Mahler"` — 7 hits:

| year | paper | authors |
|---|---|---|
| 2024-12 | Transcendence of Hecke–Mahler Series | Luca, Ouaknine, Worrell |
| 2022-12 | Rotation number of 2-interval piecewise affine maps | Gaivão, Laurent, Nogueira |
| 2022-03 | Transcendence and continued fraction expansion of values of Hecke–Mahler series | Bugeaud, Laurent |
| 2019-07 | Dynamics of 2-interval piecewise affine maps and Hecke–Mahler series | Laurent, Nogueira |
| 2018-09 | Mahler's method in several variables II | Adamczewski, Faverjon |
| 2017-04 | Rotation number of interval contracted rotations | Laurent, Nogueira |
| 2004-07 | On the arithmetic properties of complex values of Hecke–Mahler series | Pellarin |

`abs:"Sturmian" AND abs:"transcendence"` — 2 hits: Luca–Ouaknine–Worrell (2022-04), *On the
transcendence of a series related to Sturmian words*; Roy (2018-09), on conics.

`abs:"Mahler method" AND abs:"p-adic"` — **0 hits**.
`abs:"automatic" AND abs:"p-adic" AND abs:"transcendence"` — **0 hits**.

## The structural point — **PROVED**, and independent of any search

> **The constant of Phase 0 has no archimedean value at all.**

The terms of `Ξ_α = Σ_j 3^{−(j+1)}2^{⌊jα⌋}` satisfy `2^{⌊jα⌋} = 3^{j}·2^{⌊jα⌋−jα}` with the
exponent in `(−1, 0]`, so each term lies in `[1/6, 1/3]`: the series is `Θ(1)` termwise and
**diverges in `ℝ`**. In Hecke–Mahler coordinates the evaluation point `(z₁,z₂) = (1/3, 2)` sits
exactly on the boundary `|z₁z₂^{θ}| = 1` of the archimedean domain of convergence.

Every theorem in the list above is a statement about a **complex** value of a Hecke–Mahler series
(Pellarin's title says so outright; Bugeaud–Laurent require `0 < |z₁|, |z₁z₂^θ| < 1` **strictly**;
Mahler and Loxton–van der Poorten require the open domain). Luca–Ouaknine–Worrell treat
`Σ_n f(⌊nθ+ρ⌋)β^{−n}` with `f` a polynomial and `|β| > 1` algebraic — coefficients of *polynomial*
growth, hence an archimedean-convergent series; the "`p`-adic" there is the Subspace Theorem's
auxiliary places, **not the place of the value**. Our coefficients `2^{⌊jα⌋}` grow like `3^j`.

So the question Phase 0 answers is not a special case of any of these: **they are about a value
that, at our point, does not exist.** This is a hypothesis-level exclusion, not an impression.

### The four candidates, checked against their own abstracts

Fetched from the arXiv API, not paraphrased from (B):

| paper | what it proves | the hypothesis that excludes `Ξ_α` |
|---|---|---|
| **Bugeaud–Laurent**, `2203.12901` (2022) | `F_{θ,ρ}(z₁,z₂)` transcendental at algebraic `(β,α)` with `0 < \|β\|, \|βα^θ\| < 1`; plus the continued fraction and irrationality exponent of `F_{θ,ρ}(1/b, 1/a)` | the domain is **strict**. In (B)'s coordinates our point is `(x,y) = (1/3, 2)` and `\|x y^{α}\| = (1/3)·2^{log₂3} = 1` — **exactly on the boundary**; also `\|y\| = 2 > 1`, while their rational evaluations use `(1/b, 1/a)` with both coordinates `< 1` |
| **Luca–Ouaknine–Worrell**, `2412.07908` (2024) | `Σ_n f(⌊nθ+α⌋)β^{−n}` transcendental for `f ∈ ℤ[x]` **non-constant polynomial** and algebraic `\|β\| > 1` | our coefficient is `2^{⌊jα⌋}` — **exponential in `⌊jα⌋`, not polynomial** |
| **Luca–Ouaknine–Worrell**, `2204.08268` (2022) | `Σ a_n/b^n` transcendental for `a_n` in a **finite** set of algebraic numbers, Sturmian-coded, `\|b\| > 1` | our `a_j = 2^{⌊jα⌋}` is **unbounded**; equivalently the effective ratio `2^{α}/3 = 3/3 = 1`, so there is no `\|b\| > 1` |
| **Pellarin**, `math/0407378` (2004) | algebraic dependence relations of **complex** values of Hecke–Mahler series on `𝔾_m²(ℂ)`; contains Mahler, Loxton–van der Poorten, Masser | complex values; ours has none |

The same number `1` appears in three of the four rows — `\|x y^α\| = 1`, effective ratio `2^α/3 = 1`,
terms `Θ(1)`. That is one fact wearing three costumes: **`2^{log₂3} = 3` is exactly the resonance
that puts the Collatz point on every boundary at once.**

## Independent cross-check

Note (B) §9 performs the same audit hypothesis by hypothesis — Mahler 1929, Loxton–van der
Poorten 1977, Bugeaud–Laurent 2023, Luca–Ouaknine–Worrell 2022/2025, Masser 1982/1999 — and
reaches the same conclusion, naming in each case the hypothesis that excludes `Ξ_{α,β}`. (B) §9
also records the point that matters for Phase 2: Bugeaud–Laurent's effectivity mechanism is the
**continued fraction of the real value**, which has no 2-adic counterpart, 2-adic integer
approximation being governed by Hensel truncations instead.

## Verdict

> **Phase 3: no applicable prior result found.** *(Superseded 23 Sept 2026: with the manual
> Google Scholar and zbMATH sweep complete — see "Manual sweep" below — the gate is **CLOSED**
> and the approved novelty statement is "no prior proof is known; the question is stated as open
> in López–Stoll (2009) and treated as open in López–Stoll (2021)".)*

The archimedean Hecke–Mahler literature provably cannot apply, because our evaluation point is
off its domain.

### Calegari–Dimitrov–Tang — **closed by structure**

`arXiv:2109.09040`, `arXiv:2408.15403`. Their arithmetic holonomy bounds constrain **archimedean**
values of **holonomic** functions with controlled denominators. Two independent exclusions:

* **Place.** `Ξ_α` has *no archimedean value at all* (§ above; and López–Stoll themselves call
  `−Φ_R(1c_α)` at this slope "the divergent series", §7 Lemma 27). A method that bounds
  archimedean values cannot contain a statement about an object with none. This exclusion is
  airtight and needs no holonomy discussion.
* **Structure.** Note (B) Remark 6.3: `Ξ_{α,β}` satisfies no standard `d`-Mahler equation
  `Σ a_i(x) f(x^{d_i}) = 0`; its functional-equation monoid is the *continued-fraction* monoid,
  not a fixed power map. **CITED** to (B).

> **Methodologically related, cannot contain the result.**

### Lagarias's annotated bibliography — **interim cross-check of López–Stoll (2009)**

`arXiv:math/0608208` (*The 3x+1 problem: an annotated bibliography, II*), entry **67**, Lagarias's
own annotation of López–Stoll, *The 3x+1 conjugacy map over a Sturmian word*, Integers **9**
(2009) A13, 141–162, MR 2506145:

> "It is unknown whether there is any aperiodic `x ∈ ℤ₂` such that `Φ(x)` is periodic; this is
> conjectured not to happen. This paper studies this function for `x` whose 2-adic expansion is a
> Sturmian word… This paper finds a **generalized continued fraction expansion for `Φ(x)^{-1}`**
> in this case convergent in the metric on the 2-adic integers `ℤ₂`. It **explicitly computes a
> number of examples, suggesting** that the images `Φ(x)` then have 2-adic expansions of full
> complexity."

**"Suggesting", not proving.** On this evidence the 2009 paper supplies a 2-adically convergent
generalized continued fraction and computational evidence, and **no irrationality theorem**.
**CITED** — this is Lagarias's annotation, not the paper; Task 0 stays open until the paper itself
is read.

### Remaining gaps

1. ~~López–Stoll (2009)~~ — **obtained and read**; see Phase 1c Task 0b. It proves irrationality
   of the *real* values only, and explicitly diverges at the critical slope. **Closed.**
2. **Journal literature off arXiv**, and full texts of the arXiv papers — not checked.
3. ~~The author's Google Scholar "cited by" sweep on both López–Stoll papers~~ — **done**; see
   *Manual sweep* below. **Closed.**

## Manual sweep, Elias, September 2026 — **the Phase 3 gate is CLOSED**

Run by the author on Google Scholar and zbMATH, the two indexes the programmatic sweep could not
reach. Reported here as received; the classifications are the author's.

### Cited-by

| target | index | result |
|---|---|---|
| López–Stoll 2009 | Google Scholar ("Cited by", count 6) | Rozier 2018 (arXiv) and Rozier 2019 (Integers) — the same paper twice; López–Stoll 2012 (de Gruyter and EMIS copies of the same paper); López–Stoll 2021; De Jesús, EOC. **No HIT.** |
| López–Stoll 2021 | Google Scholar | no "cited by"; zbMATH holds a preprint record only |
| López–Stoll 2009, `Zbl 1195.11040` | zbMATH | cited in **1** document: Rozier 2019, `Zbl 1448.11060`. **No HIT.** |

Scholar's 6 collapses to **3 distinct works** once the duplicate hostings are merged — consistent
with OpenAlex's `cited_by = 3`, and all three were already screened in the programmatic sweep
above.

### Keyword searches (Google Scholar) — all clean

`"periodicity conjecture" Sturmian` · `Collatz "2-adic" Sturmian irrational` ·
`"3x+1" "mechanical word"` · `"3x+1" Sturmian irrational`. Results were either already known or
unrelated.

### Individually checked and classified

| work | class | reason |
|---|---|---|
| **Winkler (2026)**, *Admissible `qx+1` Sequences, Semiconvergents, and Rational Catalan Numbers*, preprint, 14 Sept 2026, Ruhr University Bochum (ResearchGate 414300439) | RELATED | word-level and cycle-lemma combinatorics of admissible sequences; semiconvergents appear on the continued-fraction side, as in note (A) §9. No 2-adic value and no `Φ`. |
| **Stephan (2026)**, *Ceiling orbits … not P-recursive* | RELATED | orbit combinatorics |
| **Stephan (2026)**, *Confinement schemas … powers of rational numbers modulo one* | RELATED | confinement of `(3/2)^n` mod 1; the distribution side, not the 2-adic value |
| **Stephan (2026)**, *Transcendence criteria for the minimal word of the rational base 3/2*, `arXiv:2609.19007` | RELATED | closest of the three: transcendence criteria for a rational-base minimal word — **and the irrationality of its constant `K` is left open there** |
| **Douzi (2024)**, HAL `hal-04488755` | NOISE | claimed Collatz proof; no 2-adic or `Φ` content |
| **Fernández & Ibáñez (2026)**, *Christoffel words as extremal structures in Collatz dynamics*, `arXiv:2607.24844` | RELATED | Christoffel words as extremal cycle words — relevant to the cycle-side notes, not to this result |

### Verdict

> **No prior proof found across OpenAlex, Google Scholar and zbMATH.** Three indexes, two of them
> manual and full-text. The nearest neighbours either study the real values off the critical
> slope (López–Stoll), or leave the analogous constant's irrationality open (Stephan 2026).

> **Novelty statement approved for the note** (exact wording): *"no prior proof is known; the
> question is stated as open in López–Stoll (2009) and treated as open in López–Stoll (2021)."*

**`NOTE.md`'s prohibition is lifted** as of 23 September 2026. Note that this is a *no prior proof
found* verdict across three indexes, not a proof of priority — gap 2 above (journal literature off
arXiv) is narrowed by the zbMATH and Scholar passes but not formally exhausted, and the novelty
wording above is phrased to say exactly that and no more.

---

# Phase 1c — irrationality of `Φ(c_s)` for every irrational slope

Raw-map (parity-vector) coordinates: `T(x) = x/2` (even), `(3x+1)/2` (odd) on `ℤ₂`; `Φ(v)` is the
unique `x ∈ ℤ₂` with parity vector `v`. Working directory `phase1c/`.

## Task 0a — López–Stoll **2021** (`arXiv:2101.12747`) — read; **the stop rule does not fire**

Archived as `sources/LopezStoll_2021_2101.12747.pdf`, sha256 `e4c5bccec262d8fd…`, 51 pp.
(identical to the copy in `~/Downloads`).

### Normalization — a clash worth pinning

Their `α` is the **ones-density / Sturmian slope**, `0 < α < 1`. Note (A)'s `α` is `log₂3`. They
are reciprocal:

```
α_LS  =  ln2/ln3  =  log₃2  =  1/α_A  ≈ 0.630930 .
```

Their special words (§1, eq. after Theorem 1) are

```
1c_α := ⌈(j+1)α⌉ − ⌈jα⌉ ,      0c_α := ⌊(j+1)α⌋ − ⌊jα⌋      (j = 0,1,2,…).
```

### The identification — **VERIFIED**

The raw parity vector of the accelerated characteristic word has its ones exactly at the
cumulative valuations `⌊j·log₂3⌋` (block map `d ↦ 1 0^{d−1}`). Computed to 2000 digits, that word
**is** `1c_α` under their ceiling definition, on the nose:

```
v     = 1101101101011011010110110110101101101011…
1c_α  = 1101101101011011010110110110101101101011…          identical for all 2000 digits
```

and, mod `2^3000`,

> **`Ξ_α = −Φ(1c_{ln2/ln3})`.** **VERIFIED** (`Ξ_α ≡ −Φ(v) ≡ 5980427723603026949 mod 2^64`).

Their term formula agrees exactly: `t_i = 2^{⌊(i−1)/α⌋}/3^i` (§10 Lemma 41, citing [9] Lemma 11)
is `3^{−(j+1)}2^{⌊j·log₂3⌋}` under `i = j+1` — **literally the summands of `Ξ_α`**.

### What they prove, and where it stops

* **Theorem 1** (stated §1, proved §6): if the trajectory of some `ζ ∈ ℚ_odd` is divergent, then
  `lim h/ℓ = ln2/ln3` **exactly**. So the critical density is the *only* place a rational
  divergent trajectory could live.
* Their aperiodicity theorem requires `lim(h/ℓ) > ln2/ln3` **strictly** (abstract; (13)–(14)).
* Their irrationality results are about the **real** value `Φ_R`, not the 2-adic one: §1 records
  that ([9], §4) the devil's staircases `F`, `F*` "show the irrationality of `Φ_R(1c_α)` (for
  `1 > α > ln2/ln3`) and `Φ*_R(1c_α)` (for `0 < α < ln2/ln3`)". **The critical slope is excluded
  from both ranges.**
* At `α = ln2/ln3` the real series **diverges**. §7 Lemma 27 calls it "the divergent series
  `−Φ_R(1c_α)`"; §10 Lemma 41 computes the terms `t_i ∈ (1/6, 1/3]` with arithmetic mean
  `1/(6 ln 2) ≈ 0.240449`. §§7, 10, 11 study the critical word — its factors, its term
  distribution, its "pseudo trajectories" — **without an irrationality statement for it.**

> **Conclusion.** `arXiv:2101.12747` does **not** prove `Φ(1c_{ln2/ln3}) ∉ ℚ`. Their method is the
> archimedean one and it is unavailable at exactly this slope, by their own computation. The
> Phase 0 result is the 2-adic statement at the critical density — the case their Theorem 1
> identifies as the only possible home of a rational divergent trajectory.

This **confirms rather than contradicts** the Phase 3 structural argument, from the authors of the
closest prior work: at the critical slope there is no archimedean value to talk about.

## Task 0b — López–Stoll **2009** (Integers 9, A13) — read; **the stop rule does not fire**

Archived as `sources/LopezStoll_2009_Integers9_A13.pdf`, sha256 `e6901bbe7b84af72…`, 22 pp.
(Integers **9** (2009), #A13, 141–162.)

### What they prove

* **Theorem 1.** For irrational `α = [0;a₁,a₂,…] ∈ (0,1)` with convergents `(p_k/q_k)` and
  `1c_α(j) = ⌈(j+1)α⌉ − ⌈jα⌉`, **in `ℤ₂`**:
  ```
  Φ(1c_α) = −1/3 − Σ_{j≥0} (−1)^{j+1} · 2^{q_{j+1}+q_j−1} / [ 3(3^{p_{j+1}}−2^{q_{j+1}})(3^{p_j}−2^{q_j}) ] .
  ```
* **Corollary 2.** A generalized continued fraction for `−1/Φ(1c_α)`, convergent in `ℤ₂`.
* **§4.** Leaving the 2-adic world, `Φ_R` is studied as a *real* function. Their Definition 22
  restricts the domain to `ℚ ∩ (ln2/ln3, 1]`, because `Σ 2^{nq}/3^{np}` converges in `ℝ`
  **iff `ln2/ln3 < p/q ≤ 1`**. There they prove `Φ_R(m_α)` is **irrational**, and that the devil's
  staircase `F` maps irrationals to irrationals. For `0 < α < ln2/ln3` they build the dual `F*`
  and prove irrationality of the real limit point `ζ`.

### Where it stops — in their own words

> "Furthermore, **`F` diverges at `x = ln(2)/ln(3)`**, the odd approximations in Theorem 1
> approach `−∞` and the even `+∞`, while in Corollary 2 both approximations approach `0`."

So `(ln2/ln3, 1]` is covered by `F`, `(0, ln2/ln3)` by `F*`, and **the single point
`x = ln2/ln3` — our slope — is excluded from both, by their own computation.**

On the 2-adic question they claim nothing:

* abstract: "The given examples **suggest** that `Φ` always maps Sturmian words to infinite words
  of full complexity";
* §4: "It seems that `F` additionally maps irrationals to transcendental numbers. **We have no
  proof.**"

> **The stop rule does not fire.** López–Stoll 2009 proves irrationality of the **real** values
> `Φ_R`, `Φ*_R` off the critical slope. It does not prove — and does not claim — irrationality of
> the **2-adic** `Φ(1c_α)`, at any slope.

### The brief's question: are their convergents the periodic cycle values?

**Partly, and the distinction matters.** Their Definition 26 sets `F(p/q) = ϕ(m_{p/q})/(2^q − 3^p)`,
which *is* the periodic cycle value `Φ(m_{p/q}^∞)`. But the proof of their Lemma 27 shows

```
−P_{2k+1}/Q_{2k+1} = F(p_{2k+1}/q_{2k+1}) ,      −P_{2k}/Q_{2k} = F(p_{2k}/q_{2k}) + g(p_{2k}/q_{2k}) .
```

So the **odd** continued-fraction convergents are cycle values; the **even** ones are cycle values
*plus the gap* `g`. Only half of the CF convergents are periodic cycle values.

### Independent verification of note (A)'s valuation law — **VERIFIED**

Computing `Φ` of the periodic word `m_{p_k/q_k}^∞` directly (mod `2^{4000}`) and comparing with
`Φ(1c_α)`, against note (A) Theorem 7.1 (their `(p_k,q_k)` is note (A)'s shell `(q_n,p_n)`):

| k | `p_k/q_k` | shell | `v₂(Φ(1c) − Φ(per))` | note (A) law | side |
|---:|:--|:--|---:|---:|:--|
| 1 | 1/1 | (1,1) | 2 | 2 | lower |
| 2 | 1/2 | (1,2) | 1 | 1 | upper |
| 3 | 2/3 | (2,3) | 10 | 10 | lower |
| 4 | 5/8 | (5,8) | 7 | 7 | upper |
| 5 | 12/19 | (12,19) | 83 | 83 | lower |
| 6 | 41/65 | (41,65) | 64 | 64 | upper |
| 7 | 53/84 | (53,84) | 568 | 568 | lower |
| 8 | 306/485 | (306,485) | 484 | 484 | upper |

**Exact agreement in every row** — an independent confirmation of note (A)'s law, from a different
construction. (It even holds at `k = 1, 2`, which note (A)'s own proof excludes for `q_n = 1`.)

Their Theorem 1's partial sums were also checked directly against `Φ(1c_α)`: the error after `j`
terms has `v₂` equal to the *next* term's exponent `q_{j+2}+q_{j+1}−1`, giving the sequence
`2, 4, 10, 26, 83, 148, 568, 1538, …` — whose odd-indexed members `10, 83, 568` are exactly note
(A)'s lower-convergent values.

### Observation beyond note (A)'s proven range

The table agrees at `k = 1` and `k = 2` — shells `(1,1)` and `(1,2)`, both with `q_n = 1`. Note
(A)'s Lemma 5.1 explicitly requires `q_n ≥ 2` (the range `1 ≤ i ≤ q_n − 1` must be non-empty), so
these two rows lie **outside its proven range**. The law's *formula* nonetheless returns the right
values there (`2` and `1`). **Recorded as an observation, not as a theorem**: two data points do
not extend a proof, and nothing in Phase 0 uses `n < 2`.

### ⚠ Citation debt — **action required on notes (A) and (B)**

> **Note (A)'s Theorem 7.1 is, in its lower-convergent half, the leading 2-adic term of
> López–Stoll 2009 Theorem 1 — and neither note (A) nor note (B) cites López–Stoll anywhere**
> (0 occurrences in either bibliography, checked).

This does **not** affect correctness: note (A)'s proof is self-contained and was re-derived in
Phase 0 Task 2, and its statement is *sharper* in one respect — it gives the upper and lower cases
separately with exact constants, where López–Stoll's series exposes the depths only through the
alternation. But the object, the approximants, and the depths coincide.

> **Required citation.** Notes (A) and (B) must cite
> **J. López and P. Stoll, *The 3x+1 conjugacy map over a Sturmian word*, Integers 9 (2009), #A13,
> 141–162 (MR 2506145)** as the **first source of the approximants and of the approximation
> depths**, with note (A)'s Theorem 7.1 presented as an **independent and sharper derivation** —
> sharper in giving the exact upper (`p_n − 1`) and lower (`p_n + p_{n+1} − 1`) constants
> separately. Note (A)'s description of its result as the tower's "first theorem-grade structural
> result" must be qualified accordingly.
>
> *Author has confirmed he will revise (A) and (B) on Zenodo.*

**Consequence for Phase 0: none, except to strengthen it.** The valuation law that the Liouville
argument consumes is now sourced twice, independently.

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

---

# Phase 1c — scope correction: the all-slope extension is a **target**, not a corollary

Recorded at the author's instruction, and it is the right call.

## Why it is not immediate

Phase 0 works at the critical slope because, at each shell, the approximant is a **periodic cycle
value** `Φ(m_{p/q}^∞) = c_w/(2^ℓ − 3^k)` — a rational whose height is controlled by the
balanced-word bound of Task 1.3. What is *not* automatic in general is the identification of such
a value with a continued-fraction convergent: by López–Stoll's Lemma 27,

```
−P_{2k+1}/Q_{2k+1} = F(p_{2k+1}/q_{2k+1})         (a periodic cycle value)
−P_{2k}/Q_{2k}     = F(p_{2k}/q_{2k}) + g(p_{2k}/q_{2k})   (cycle value + gap)
```

so **only the odd-indexed convergents are periodic-word values**. Any argument that silently
treats every convergent as a cycle value — and therefore imports the height bound for one — is
unsound.

*Clarifying observation.* The verification above computed `Φ(m_{p_k/q_k}^∞)` **directly** at every
shell, both parities, and matched note (A)'s law in all eight rows. So at the critical slope the
periodic values are genuine approximants at **every** shell; what is index-dependent is only their
coincidence with López–Stoll's `−P_k/Q_k`. The obstruction to the general-slope theorem is
therefore in the *proof* for arbitrary `α`, not in the parity as such.

## The target, stated

> For every irrational slope `α ∈ (0,1)`, prove:
>
> 1. **the depth law** — `v₂(Φ(1c_α) − Φ(m_{p/q}^∞))` at those convergents where the periodic
>    value is the approximant, equivalently the longest-common-prefix law of Phase 1c Task 2;
> 2. **balanced-word height bounds** there — available: Task 1.3's
>    `|c_w| ≤ 3ℓ·max(2^ℓ, 3^k)` for mechanical `w`, whose `log₂` is
>    `max(ℓ, k·log₂3) + log₂(3ℓ)`;
> 3. **depth > Liouville ceiling for infinitely many of them**, in **both** regimes
>    `α ≤ ln2/ln3` and `α > ln2/ln3`.

The two regimes are genuinely different: `ln2/ln3` is where the real series changes convergence
behaviour (López–Stoll Definition 22), where `F` and `F*` change roles, and where the ceiling
`max(ℓ, k log₂3)` switches which argument attains the maximum. A single uniform argument across
the critical slope should not be assumed.

**Phase 0 is unaffected**: it concerns the critical slope and the lower convergents only, where
the approximants are periodic cycle values — verified directly, not inferred.

---

# Phase 3 — literature workflow (Zotero + citation APIs)

## Step 1 — Zotero: **local API unreachable; collection not found**

| check | result |
|---|---|
| Zotero installed | yes, `/usr/bin/zotero` |
| Zotero **running** | **no** — no process, nothing listening |
| local API `http://localhost:23119/api/…` | **unreachable** (connection refused; also probed `:23120`, `/connector/ping`, `/api/`) |
| data directory | `~/Zotero/` with `zotero.sqlite` (5.5 MB) |
| Better BibTeX | installed (`~/Zotero/better-bibtex/`), but **no auto-exported `.bib`** anywhere under `~/Zotero` |

The Zotero 7 local API only serves while the application is running, so it could not be used. I
read the database **read-only instead**, and to guarantee the library was not touched I copied
`zotero.sqlite` to the scratch directory first and opened the copy with
`sqlite3.connect('file:…?mode=ro', uri=True)`. **Nothing in `~/Zotero` was written, moved or
locked.**

> ### ⚠ There is no collection named "Sturmian irrationality".
>
> All 180-odd collection names were listed; no match, and no near-match. The relevant tree is:
>
> ```
> [ 13] EOC — Collatz Conjecture Research            (0 items directly)
>        [14] 00 — Reviews & Surveys                       6
>        [15] 01 — Classical 3x+1 Results                 10
>        [16] 02 — Accelerated Collatz & Valuation Dynamics 6
>        [17] 03 — Probabilistic / Random Models           4
>        [18] 04 — Tao Almost-All Results                  3
>        [19] 05 — Mixing, Fourier & Residue Methods       3
>        [20] 06 — Divergent-Orbit Constraints             4
>        [21] 07 — Congruences, Realizers & Arithmetic Placement 6
>        [22] 08 — Recent Results & Refinements            3
>        [23] 09 — Directly Cited in EOC                  23
>        [24] 10 — Closest Prior Art / Novelty Checks      8
>        [25] 11 — Open Problems & Conjectural Context     4
> ```
>
> **Reported rather than guessed**: `references.bib` has *not* been written, because the source
> collection is ambiguous. Name the collection (or say "create it from the HIT/RELATED list
> below") and I will export it.

Both conjugacy-map papers are already in the library — a title search returns
*The 3x+1 Conjugacy Map* (Bernstein–Lagarias) and *The 3x+1 Conjugacy Map over a Sturmian Word*
(López–Stoll 2009) — so the collection may simply be a naming difference.

## Step 2 — cited-by sweep

### Queries run, with result counts

| API | query | result |
|---|---|---|
| OpenAlex | `title.search:"The 3x+1 conjugacy map over a Sturmian word"` | 1 work → `W1989074566`, **cited_by = 3** |
| OpenAlex | `title.search:"The 3x+1 Periodicity Conjecture in R"` | **0** — OpenAlex stores the title with a typo, *"Periodicity **Conjeture**"* |
| OpenAlex | `works/doi:10.48550/arxiv.2101.12747` | `W3127959870`, **cited_by = 0** |
| OpenAlex | `title.search:"The 3x+1 conjugacy map"` | 5 works → `W2033304944` (Bernstein–Lagarias 1996), **cited_by = 33** |
| OpenAlex | `filter=cites:W1989074566` | 3 citing works retrieved |
| OpenAlex | `filter=cites:W3127959870` | 0 citing works |
| OpenAlex | `filter=cites:W2033304944` | 33 citing works retrieved |
| Semantic Scholar | `paper/arXiv:2101.12747/citations`, and title searches for the other two | **0 returned for all three** — see the caveat below |

### Every citing work of López–Stoll 2009, screened in full (no keyword triage)

| # | citing work | class | reason |
|---|---|---|---|
| 1 | **López & Stoll (2012)**, *The 2-Adic, Binary and Decimal Periods of 1/3^k Approach Full Complexity for Increasing k*, Integers **12**, `10.1515/integers-2012-0013` | **RELATED** | Same authors, same complexity theme — but about the expansions of `1/3^k`, which are **rational** (eventually periodic) 2-adics. No statement about `Φ` on aperiodic Sturmian input. |
| 2 | **Rozier (2018)**, *Parity Sequences of the 3x+1 Map on the 2-adic Integers and Euclidean Embedding*, `arXiv:1805.00133` | **RELATED** | Same object (`Φ`, parity sequences): a new inverse-transform formula, ergodicity of the induced automorphism, a self-similar plane embedding. No irrationality or aperiodicity theorem. |
| 3 | **López & Stoll (2021)**, *The 3x+1 Periodicity Conjecture in ℝ*, `arXiv:2101.12747` | **RELATED** | Read in full (Task 0a). Proves aperiodicity for ones-density **strictly** above `ln2/ln3`; `F` diverges at the critical slope. |

### Second net — works citing Bernstein–Lagarias 1996 that mention Sturmian

All 33 screened against `sturmian · mechanical · irrational · aperiodic · transcend · periodicity conjecture · conjugacy`. Five flagged; **the only two mentioning Sturmian are López–Stoll 2009 and 2021**, both already assessed. The other three:

| citing work | class | reason |
|---|---|---|
| **Yazinski (2011)**, *Pseudoperiodicity and the 3x+1 Conjugacy Function*, `arXiv:1102.5547` | **RELATED** | Directly about periodicity of `Φ`; proves families of 2-adics are *not* fixed points, supporting the `Φ` Fixed Point Conjecture. Not about Sturmian input, and not an irrationality theorem. |
| **Monks & Yazinski (2004)**, *The autoconjugacy of the 3x+1 function*, Discrete Math. **275**, 219–236 | **RELATED** | Structure of `Φ` itself. No Sturmian or irrationality content. |
| *The Collatz conjecture and De Bruijn graphs* (2012/2013) | **NOISE** | Identifies a graph isomorphism with the Bernstein–Lagarias conjugacy; no arithmetic of values. |

The remaining 28 are **NOISE** for this question (ergodic/stochastic models, fractal visualisations, De Bruijn graphs, solenoidal/automatic-sequence papers, Lagarias's bibliographies, surveys).

### Verdict

> **No HIT.** Nothing found proves — or claims — that `Φ` of a Sturmian or mechanical word is
> irrational/aperiodic in `ℤ₂`, at any slope.

### ⚠ Coverage caveat — stated precisely, because the requested wording would overstate it

The brief's template verdict was *"cited-by sweep clean (OpenAlex + Semantic Scholar)"*. **That
would be inaccurate**: Semantic Scholar returned **0 citing works for all three targets**,
including Bernstein–Lagarias 1996, which certainly has citations there. That is an **API failure**
(unauthenticated rate limiting), not a finding. The honest statement is:

> **Cited-by sweep clean on OpenAlex. Semantic Scholar did not return data and contributes no
> coverage.**

Two further limits:

* OpenAlex citation counts for **Integers** — a small open-access journal — may be incomplete, so
  `cited_by = 3` for the 2009 paper is a lower bound.
* `cited_by = 0` for the 2021 preprint is plausible for a 2021 arXiv posting but is also exactly
  what an indexing gap looks like; note that OpenAlex has its title misspelled, which is a sign of
  thin metadata.

**The manual Google Scholar / zbMATH check was the final cross-check. It was run by the author in
September 2026 and is recorded under "Manual sweep" in the Phase 3 section above: Scholar's 6 citing records collapse to
the same 3 distinct works OpenAlex found, and zbMATH shows 1. The gate is CLOSED.**

## Step 3 — `references.bib`

Written to `audits/sturmian_irrationality/references.bib`: **28 entries**, Better BibTeX-style keys
(`<firstauthor-lowercase><year><first significant title word>`, stopwords and leading numerals
skipped — e.g. `lopez2009conjugacy`). Built from collections **[23]** and **[24]** where relevant to
this note, plus the specified works and every RELATED item from the sweep. **The Zotero library was
not modified.**

### Works to add to collection [24] — not currently in the library

| work | identifier |
|---|---|
| López & Stoll (2021), *The 3x+1 Periodicity Conjecture in ℝ* | `arXiv:2101.12747` |
| López & Stoll (2012), *The 2-Adic, Binary and Decimal Periods of 1/3^k…*, Integers 12 | `10.1515/integers-2012-0013` |
| Rozier (2018), *Parity Sequences of the 3x+1 Map…* | `arXiv:1805.00133` |
| Yazinski (2011), *Pseudoperiodicity and the 3x+1 Conjugacy Function* | `arXiv:1102.5547` |
| Monks & Yazinski (2004), *The autoconjugacy of the 3x+1 function* | `10.1016/S0012-365X(03)00125-0` |
| Bugeaud & Laurent (2023), Acta Arith. **209**, 59–90 | `10.4064/aa220323-18-1` (`arXiv:2203.12901`) |
| Luca, Ouaknine & Worrell (2025), Bull. LMS **57** (5), 1360–1368 | `10.1112/blms.70033` (`arXiv:2412.07908`) |
| Luca, Ouaknine & Worrell (2022), *On the transcendence of a series related to Sturmian words* | `arXiv:2204.08268` |
| Adamczewski & Bugeaud (2006), *Real and p-adic expansions involving symmetric patterns*, IMRN | `10.1155/IMRN/2006/75968` |
| Pellarin (2004), *On the arithmetic properties of complex values of Hecke–Mahler series* | `arXiv:math/0407378` |
| Calegari, Dimitrov & Tang (2021), *The Unbounded Denominators Conjecture* | `arXiv:2109.09040` |
| Calegari, Dimitrov & Tang (2024), *The linear independence of 1, ζ(2), L(2,χ₋₃)* | `arXiv:2408.15403` |
| Lothaire (2002), *Algebraic Combinatorics on Words*, CUP | ISBN 9780521812207 |

Already present (no action): Terras 1976, Everett 1977, Lagarias 1985 and both annotated
bibliographies, Bernstein 1994, Bernstein–Lagarias 1996, López–Stoll 2009, Mahler 1957, Ridout 1958,
Schlickewei 1976, Evertse–Schlickewei 2002, Dvoretzky–Motzkin 1947.

*Correction (23 Sept 2026).* Two page ranges in the first build of `references.bib` were wrong —
Bugeaud–Laurent was entered as 59–75 and Luca–Ouaknine–Worrell as 1360–1374. Both were re-checked
against the publisher DOI records via Crossref and OpenAlex, which agree on **59–90** and
**1360–1368** (Bull. LMS issue 5). The bib file and the table above are corrected. Note (B)'s own
bibliography had both right; the error was in this audit's file, not in the note.

*Note on `monks2004autoconjugacy`:* OpenAlex dates it 2003 (online first); the Discrete Math.
issue is dated 6 January 2004. The entry uses 2004, as in the brief, with the discrepancy recorded.

---

# Revision — López–Stoll citations, and the Zenodo depositions

The citation debt recorded in Phase 1c was discharged on 23 September 2026. Neither note has a
LaTeX source, so nothing was reconstructed: the deliverable is the patch list
`revisions/2026-09-sturmian-citations/REVISIONS.md` plus two standalone addenda that travel beside
the unchanged originals.

## Deposited

| | current version DOI | concept DOI | superseded |
|---|---|---|---|
| (A) | `10.5281/zenodo.22917426` ⚠ | `10.5281/zenodo.20556483` ⚠ | `22916798`, `22916962` |
| (B) | `10.5281/zenodo.22917246` ✅ | `10.5281/zenodo.20594173` ✅ **cite this** | `22916849`, `22917066` |

**(B) is settled.** `SturmianMahlerEdgeAcceleratedCollatzRealizerProblem (1).pdf` (327 659 B,
`830ff7dc768ed1a692e9b050a5e28fa0`) and `B_addendum.pdf` (390 796 B,
`3ecb5e274e5603249f9168dddb314125`) — note and addendum, nothing else.

**(A)'s umbrella record has a regression** — see below. Cite it by **version** DOI until fixed.

**Note (A)'s record title is not the note's title.** The note renders as *The 2-Adic Sturmian
Carry Constant in the Collatz Carry Equation* and sits inside an umbrella record covering the
tower line. `references.bib` records both names on `dejesus2026sturmiancarry`.

## ⚠ Umbrella record `22917426`: 25 of 29 collection files dropped

Verified 23 September 2026 from the record endpoint, `/files`, and the concept version list.

The current version holds **5 files**, all verified by MD5, **no duplicates**, and every one
matching a local artefact:

| file | md5 | is |
|---|---|---|
| `AdicSturmianCarryConstant (1).pdf` | `8064824b…` | note (A) |
| `A_addendum.pdf` | `de6e65cf…` | the (A) citation addendum |
| `AdjacentTowerProductsCollatzCarryEquation (1).pdf` | `ab51c2d2…` | Tier-1 note, **unmodified** |
| `FiniteChristoffelProducts (1).pdf` | `cf4a5c83…` | Tier-1 note, **unmodified** |
| `BitAnalyzerCollatzCarryEquation (1).pdf` | `aad1685b…` | Tier-1 note, **unmodified** |

But the last full-collection version, `10.5281/zenodo.20599453` (8 June 2026), holds **29 files**.
The three September versions replaced the file set rather than adding to it (1 → 2 → 5 files), so
**25 files are absent from the current version**, including `NearCritical.pdf` — which note (A)
cites as its own reference [9]. The record hosting note (A) no longer serves the note (A) depends
on.

Nothing is lost permanently: Zenodo versions are immutable and `20599453` still serves all 29. But
the concept DOI resolves to the *latest* version, so `10.5281/zenodo.20556483` now lands a reader
on the 5-file record. **The fix is one more version carrying all 29 original files plus
`A_addendum.pdf`, 30 in total.** Until then, cite the version DOI of whichever state is meant.
Full file list in `revisions/2026-09-sturmian-citations/ZENODO.md`.

## Collection-addendum scope — verified against the downloaded PDFs

All 29 files of `10.5281/zenodo.20599453` were downloaded and MD5-verified against the record
manifest (29/29). Each was then scanned page by page for `Ξ`, `carry constant`, `v₂(Q…)`, `ℓ(D)`
and `López`/`Stoll`.

**Exactly twelve PDFs contain `Ξ`.** One of them is note (A) itself, already covered by
`A_addendum.pdf`; the other eleven are the collection-addendum scope.

### The eleven — quoted line and page

| # | note (file) | quoted line | page |
|---|---|---|---|
| 1 | *A Bit Analyzer for the Collatz Carry Equation* (`BitAnalyzerCollatzCarryEquation.pdf`) | "Definition 2.1 (Bit analyzer). The bit depth of D is `ℓ(D) = v2(Q(D) + Ξα)`, and the centered…" | p. 2 |
| 2 | *Adjacent Tower Products in the Collatz Carry Equation* (`AdjacentTowerProductsCollatzCarryEquation.pdf`) | "analyzer is `ℓ(D) = v2(Q(D) + Ξα)`, where `Ξα` is the 2-adic Sturmian carry constant of the second note [1]." | p. 1 |
| 3 | *Finite Christoffel Products in the Collatz Carry Equation* (`FiniteChristoffelProducts.pdf`) | "quotient `Q(D) = −C(D)/δ`, and bit depth `ℓ(D) = v2(Q(D) + Ξα)` with `Ξα` the archived Sturmian…" | p. 2 |
| 4 | *Standard-Block Nonsingularity in the Collatz Carry Equation* (`StandardBlockNonsingularity (1).pdf`) | "dition, in which the 2-adic Sturmian carry constant of the companion note [2] pins the only…" | p. 1 |
| 5 | *Grouped Tower Products in the Collatz Carry Equation* (`GroupedTowerProductsCarry_Equation (1).pdf`) | "`v2(Qa,b + Ξα) = 83 = p5 + p6 − 1`." | p. 1 |
| 6 | *Tail-Tracking and the Leading-Block Principle* (`TailTrackingLeadingBlockPrinciple.pdf`) | "of the convergents of `α = log2 3`. The bit depth `ℓ(D) = v2(Q(D) + Ξα)` is governed by a…" | p. 1 |
| 7 | *The Wrap Regime in the Collatz Carry Equation* (`WrapRegimeCollatzCarryEquation.pdf`) | "gorithm computes `ℓ(D) = v2(Q(D) + Ξα)` for every finite product of standard tower blocks:" | p. 1 |
| 8 | *The Positive-Entropy 2-Adic Carry Law* (`PositiveEntropy2Adic.pdf`) | "Let `Ξα` denote the rigid Sturmian 2-adic carry constant associated to…" | p. 8 |
| 9 | *Unbalanced Residents … The (7, 11) Shell* (`UnbalancedResidentsCollatzCarryEquation (1).pdf`) | "so `ℓ(D−17) = v2(Q + Ξα) = 2`. The shell's quotients reach `|Q| ≈ 158`…" | p. 3 |
| 10 | *Unbalanced Residents and Time-Axis Contacts* (`UnbalancedResidentsTime_AxisContactsCCE.pdf`) | "restarted — has computable `ℓ(D) = v2(Q(D) + Ξα)`, with nonsingularity certificates across entire…" | p. 2 |
| 11 | *The Anatomy of the −17 Cycle: Time-Axis and Finite-Field Structure* (`TimeAxisFiniteFieldStructure.pdf`) | "`ℓ(D−17) = v2(Q + Ξα) = 2`." | p. 5 |

**Every quoted line was located in the downloaded PDF.** All eleven titles match the triage list.

### ⚠ One correction to the reason given for item 2

The Step 5 survey in this report said Adjacent Tower Products "cites (A)'s Theorem 7.1 explicitly",
and that reason carried into the triage list. **It is wrong, and the error was mine** — a grep for
the string "Theorem 7.1" matched the note's *own* Theorem 7.1. The only two occurrences of "7.1"
in that note are:

> p. 4 — "Theorem 7.1 (Standard-factorization ladder). Let `Rn < 0`. For `1 ≤ b ≤ an+2`,"
> p. 6 — "ladder identities (Thm. 7.1) and the five verified instances;"

both referring to its own numbering. Its actual dependence is the one quoted in the table: it uses
the bit analyzer `ℓ(D) = v₂(Q(D) + Ξα)` and attributes `Ξα` to "the second note [1]". **The
attribution requirement is unchanged** — it consumes the carry constant and the first-disagreement
depth either way — only the stated reason is corrected.

### Cleared — 16 PDFs with zero occurrences of `Ξ`

`CompositeDecomposition.pdf` · `CorrelatedPrimeLayersCollatzCarryEquation.pdf` ·
`CorridorBracketsBottleneckRatios.pdf` · `FiniteFieldZeroSums.pdf` ·
`ImprimitiveSplittingForcedLayerZeros.pdf` · `LocalIsolationWallContactsCollatzCarry.pdf` ·
`modulus_depth_landmarks.pdf` · `NearCritical.pdf` · `ProjectiveClosureCoordinates.pdf` ·
`ProjectiveNearMisses.pdf` · `ShellMixedBracketTracers.pdf` · `ShellNearMissBottleneck.pdf` ·
`ShellPureTracer.pdf` · `WallPrimeTracersCCEquation.pdf` · `ZeroSubwindowObstructions.pdf` ·
`ZeroWindowVarieties.pdf`

Plus `cubic_modulus_threshold_referee_note.md` — the referee note, triaged separately below.

### ⚠ The partition is 1 + 11 + 16 + 1, not 11 + 17 + 1

The triage brief gave the partition as `11 + 17 + 1 = 29`. That arithmetic works only by counting
note (A) among the "17 cleared", and note (A) is not cleared — it is the note the existing
`A_addendum.pdf` is about, and it contains `Ξ` 33 times. The checkable partition is:

| class | count | |
|---|---|---|
| note (A) — covered by `A_addendum.pdf` | **1** | `AdicSturmianCarryConstant.pdf` |
| needs the collection addendum | **11** | the table above |
| cleared, no `Ξ` and no depth law | **16** | the list above |
| referee note, not a note | **1** | `cubic_modulus_threshold_referee_note.md` |
| | **29** | ✓ |

## The 29th file — identified and triaged

The count of 28 notes against 29 files in `20599453` is explained: **28 PDFs and one Markdown
file.** The odd one out is

> `cubic_modulus_threshold_referee_note.md` — 12 542 B, md5 `7b7cf52b0e842ec3a868f3074e6e61b6`
> (verified on download), 138 lines.

**It is not a note.** It is a *hostile-referee technical note* asking whether the cubic compactness
threshold `θ_crit ≈ 0.317672` has number-theoretic meaning for carry-residue modulus growth, and
its own verdict is **"False lead as a dynamical threshold; admissible only as an imported partition
bookkeeping marker."**

**Triage — every marker returns zero:**

| marker | count |
|---|---|
| `Ξ` · `Xi` · `carry constant` | 0 · 0 · 0 |
| `López` · `Lopez` · `Stoll` | 0 · 0 · 0 |
| `Christoffel` · `Sturmian` · `mechanical` | 0 · 0 · 0 |
| `convergent` · `approximant` · `continued fraction` | 0 · 0 · 0 |
| `Theorem 7.1` · `first-disagreement` | 0 · 0 |

It does use the block value `Q(D)`, via `Q ≡ −C_L(D)·3^{−L} (mod 2^m)`, and it is about "depth" —
but the depth is the **modulus depth** `θ = m/S`, the shell/entropy coordinate, not the
first-disagreement depth `v₂(Q(D) + Ξ_α)` that the López–Stoll attribution concerns. Its machinery
is hypergeometric cut-point laws, large deviations and TV distance to Bernoulli(`ρ`); there is no
approximant, no convergent shell, and no carry constant anywhere in it.

> **Verdict: no attribution needed.** Same class as Composite Decomposition, Correlated Prime
> Layers, Corridor Brackets / Bottleneck Ratios and Finite-Field Zero Sums.

So the full set of 29 files partitions as: 28 notes plus one referee note, and the referee note is
out of scope for this revision.

## Tier-1 citation debt — **STILL OPEN**

Adding the three Tier-1 notes to the umbrella record does **not** discharge their debt:

* `A_addendum.pdf` in the record has md5 `de6e65cfa6fbbddbb7faf062c38fe685` — byte-identical to
  the addendum built in this audit, which addresses **note (A) only**. **No extended addendum
  exists.** It names no Tier-1 note.
* The three Tier-1 PDFs are byte-identical to their June copies and to `~/Downloads`, so they are
  **unmodified** and still contain no López–Stoll citation anywhere.

Co-depositing an unmodified note beside an addendum that does not mention it changes nothing about
what that note claims. The Tier-1 requirement is unchanged from the Step 5 survey: each of Bit
Analyzer, Adjacent Tower Products and Finite Christoffel Products needs its own one-sentence
attribution to López–Stoll 2009 via note (A), and the `n ≥ 3` range wherever it quotes the
per-shell depth.

## Superseded versions, and why

| version | what was wrong |
|---|---|
| `22916798` (A) | addendum only, no note |
| `22916962` (A) | note + addendum, but 25 collection files already dropped |
| `22916849` (B) | note only, no addendum |
| `22917066` (B) | the note deposited **twice** under two filenames, identical md5; addendum absent |

`22917066` is why every check here is by checksum rather than by file count or size: it had two
files of plausible size and would have passed a weaker test.

## Reproducibility note

`revisions/2026-09-sturmian-citations/references.bib` is a **frozen build input** — the exact
bibliography the two deposited PDFs were compiled against — and carries a header saying so. The
canonical `references.bib` in this directory continues to take additions, including the Zenodo
DOIs above, and the two files are therefore expected to differ.
