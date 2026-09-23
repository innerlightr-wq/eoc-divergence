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

# Status

| Task | Result |
|---|---|
| 1 — reconciliation | **PROVED**: `Ξ_{α,0} = −Ξ_α`; `c_α` is intercept `β = 0`; lower shells are the even indices |
| 2 — valuation law re-derived | **PROVED for `n ≥ 2`**; one typo in (A) recorded, no consequence |
| 3 — Liouville argument | **written; proof above** |
| 4 — numerical verification | *not yet run* |
| 5 — controls | *not yet run* |

**Verdict for Phase 0 is withheld** until Tasks 4 and 5 pass, per the audit rule that controls
precede any positive claim. The proof in Task 3 does not depend on those checks; they are there to
catch an error in it.
