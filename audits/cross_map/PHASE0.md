# Phase 0 — the pre-registered prediction P0, proved

**Exploratory. No claim of progress toward the Collatz conjecture.**
Labels: **PROVED** (proof written out here) · **CITED** · **VERIFIED** (exact computation,
stated range) · **HEURISTIC** · **OPEN**.

Committed before Phase 1, as the brief requires.

## Setting and notation

For odd `q ≥ 3` and odd `r` (with `qx + r > 0` on the domain), put

```
a(x) = v₂(qx + r) ≥ 1 ,    T(x) = (qx + r)/2^{a(x)}    on odd positive x,
m_k = T^k(m₀),  a_k = a(m_k),  S_n = Σ_{k<n} a_k,  α = log₂q,  R_n = S_n − nα .
```

**The aggregate identity.** From `2^{a_k}m_{k+1} = q m_k + r`, setting `X_k = 2^{S_k}m_k` gives
`X_{k+1} = qX_k + r·2^{S_k}`, hence by induction

```
2^{S_n} m_n = q^n m₀ + r·C_n ,     C_n = Σ_{i<n} q^{n−1−i} 2^{S_i} ≥ q^{n−1} > 0  (n ≥ 1).   (†)
```

**PROVED** (the `(q,r) = (3,1)` case is `Divergence.aggregate_identity`, machine-checked; the proof
above is the same induction and does not use the values of `q, r`).

**The rare side.** Under Haar measure the letters `a_k` are i.i.d. geometric(½) with mean 2, for
every odd `q` and odd `r` (proved in `audits/fingerprint_comparison/PHASE0.md`, F1). So `R_n` is a
walk with mean increment `2 − α`, and the *rare* side — the one an orbit must fight to stay on — is

```
q < 4  (α < 2):   R_n ≤ 0,  i.e.  2^{S_n} ≤ q^n        ("below the line")
q > 4  (α > 2):   R_n ≥ 0,  i.e.  2^{S_n} ≥ q^n        ("above the line")
```

`q = 4` is excluded since `q` is odd. Say `m₀` **persists** if its orbit is on the rare side at
every `n ≥ 1`.

**The sign-alignment criterion** (`audits/fingerprint_comparison`, §6). **PROVED.** For a positive
cycle of length `L` and total `S`, `(†)` at the period gives `m(2^S − q^L) = r·C_L`; since
`m > 0` and `C_L > 0`, and `2^S ≠ q^L` by unique factorisation,

```
sign(S/L − α) = sign(r) ,     so a positive cycle is on the rare side  ⟺  sign(r) = sign(q − 4).
```

---

## P0 — for `D = 5x−1`, no positive odd integer persists. **PROVED**

> **Theorem P0.** Let `T(x) = (5x−1)/2^{v₂(5x−1)}` on odd positive `x`. There is no odd `m₀ ≥ 1`
> with `2^{S_n} ≥ 5^n` for every `n ≥ 1`.

**Proof.** Suppose `m₀` persists. Four steps.

**(1) The orbit is bounded, in fact strictly below its seed.** Here `q = 5`, `r = −1`, so `(†)` reads
`2^{S_n} m_n = 5^n m₀ − C_n` with `C_n > 0` for `n ≥ 1`. Hence for every `n ≥ 1`

```
m_n  =  (5^n m₀ − C_n)/2^{S_n}  <  5^n m₀ / 2^{S_n}  ≤  m₀ ,
```

the last step by persistence, `2^{S_n} ≥ 5^n`. Note the two signs that make this work: `C_n > 0`
enters with a **minus**, and persistence is an **upper** bound on `5^n/2^{S_n}`.

**(2) The orbit is eventually periodic.** Every `m_n` is a positive odd integer `< m₀`, so the orbit
takes at most `⌈m₀/2⌉` values; by pigeonhole some value repeats, and `T` is a function, so the orbit
is eventually periodic: there are `n₀ ≥ 0` and `L ≥ 1` with `m_{n+L} = m_n` for all `n ≥ n₀`.

**(3) The eventual cycle lies on or above the line.** Let `S_cyc = S_{n₀+L} − S_{n₀}` be the cycle's
valuation total. For `n = n₀ + kL`, `S_n = S_{n₀} + k·S_cyc`, and persistence gives

```
S_{n₀} + k·S_cyc  ≥  (n₀ + kL)·α    for every k ≥ 0,   i.e.   k(S_cyc − Lα) ≥ n₀α − S_{n₀} .
```

If `S_cyc − Lα < 0` the left side tends to `−∞`, a contradiction. Hence `S_cyc/L ≥ α`.

**(4) Contradiction with the criterion.** The cycle consists of positive odd integers, so the
criterion applies with `r = −1 < 0`: `S_cyc/L < α`. This contradicts (3). ∎

**What each step needs, checked.**

| step | what it uses | is it tight? |
|---|---|---|
| (1) | the form of `(†)` for `r = −1` (carry subtracted) **and** `q > 4` (persistence is an upper bound on `q^n/2^{S_n}`) | both are needed; see P0′ |
| (2) | positivity of every `m_n` and integrality | needs `m_n > 0`, which `r = −1, q ≥ 3, x ≥ 1` gives since `qx − 1 ≥ 2` |
| (3) | only the *cumulative* persistence, taken along multiples of the period | no strictness required |
| (4) | the criterion, which is `(†)` at the period plus `m > 0` | the two inequalities are `≥ α` and `< α`, so they already conflict; the strictness supplied by unique factorisation is not needed |

**VERIFIED** (`data/criterion.txt`): `D`'s only positive cycle found among orbits of odd seeds
`≤ 20001` is the fixed point `{1}`, with word `[2]`, `S/L = 2 < log₂5 = 2.3219…` — off the rare
side, as the criterion requires. (Step (4) does not depend on knowing the cycles; if `D` had no
positive cycle at all, step (2) would already be contradicted.)

---

## P0′ — the general principle, with one correction to the proposed statement

The brief proposes: persistence is *forced into boundedness* whenever the rare side is the shrinking
side, i.e. whenever `q > 4`. **That is not quite right, and the correction matters.** The
identification "rare side = shrinking side" is exact only when the carry has the favourable sign.

From `(†)`, `m_n = q^n m₀/2^{S_n} + r·C_n/2^{S_n}`. Persistence controls the **first** term
(`q^n/2^{S_n} ≤ 1` when `q > 4`). The second term is controlled only when `r < 0`, where it is
negative and can be dropped. When `r > 0` it is positive and is **not** bounded by persistence:
writing `t_i = 2^{S_i}/q^i ≥ 1`, persistence gives the exact identity

```
m_n  =  ( m₀ + (1/q)·Σ_{i<n} t_i ) / t_n ,
```

so `m_n ≥ (m₀ + n/q)/t_n`, and boundedness requires `t_n` to grow. For the `C`-cycle `{1,3}` it does
(`t_{2k} = (32/25)^k → ∞`), but nothing in the hypothesis forces it. So pigeonhole is available only
for `r < 0`.

This does **not** change the classification, because the two mechanisms are complementary: for
`q > 4` the case `r > 0` is exactly the case in which a cycle already shelters on the rare side, so
it is settled positively without any pigeonhole.

> **Principle P0′. PROVED.** Two independent binary conditions decide "does a positive integer
> persist on the rare side?"
>
> * **Shelter.** Some positive cycle lies on the rare side ⟺ `sign(r) = sign(q − 4)`
>   (the criterion). If so, persistence **holds**, witnessed by a cycle element.
> * **Pigeonhole.** Persistence forces `m_n < m₀`, hence eventual periodicity, ⟺ `r < 0` **and**
>   `q > 4` (step (1) of P0). If so, and if shelter fails, persistence is **impossible**.
>
> The two cover three of the four sign combinations. The remaining one — `q < 4` and `r > 0` — has
> neither: no cycle shelters on the rare side, and the rare side is the **growth** side
> (`R_n ≤ 0 ⟺ m_n ≳ m₀`), so no pigeonhole is available. That case is open.

| map | `q` | `r` | `sign(q−4)` | `sign(r)` | shelter | pigeonhole | persistence on the rare side |
|---|---|---|---|---|---|---|---|
| **A** `3x+1` | 3 | `+1` | `−` | `+` | no | no | **OPEN** — this is (DE) |
| **B** `3x−1` | 3 | `−1` | `−` | `−` | **yes** | no | **TRUE**, witnessed by `m = 1` |
| **C** `5x+1` | 5 | `+1` | `+` | `+` | **yes** | no | **TRUE**, witnessed by `m = 3` |
| **D** `5x−1` | 5 | `−1` | `+` | `−` | no | **yes** | **FALSE**, Theorem P0 |
| `3x+5` | 3 | `+5` | `−` | `+` | no | no | **OPEN**, same class as A |
| `7x+1` | 7 | `+1` | `+` | `+` | **yes** | no | **TRUE**, witnessed by `m = 1` (word `[3]`, `S/L = 3 > log₂7`) |
| `7x−1` | 7 | `−1` | `+` | `−` | no | **yes** | **FALSE**, by the proof of P0 verbatim |

**VERIFIED** (`data/criterion.txt`): the shelter column is confirmed against an exact cycle search
over odd seeds `≤ 20001` for all seven maps; predicted and observed agree in every row. For `7x−1`
no positive cycle was found in that range, which is consistent with (and stronger than) "no shelter".

> **The candidate insight, stated plainly.** (DE) for `3x+1` is hard because `3x+1` is the
> combination in which *both* mechanisms fail: no positive cycle shelters on the rare side, and the
> rare side is the growth side, so the orbit of a hypothetical persistent seed is unbounded and
> pigeonhole cannot be applied. Its two neighbours are settled for opposite reasons — `3x−1` because
> a cycle shelters, `5x−1` because persistence would force boundedness — and `3x+5` is open for the
> same reason `3x+1` is.

---

## P0″ — what the non-trivial question for `D` is instead

Since persistence on the rare side is impossible for `D`, and the rare side is the *shrinking* side,
every positive orbit of `5x−1` eventually spends its time on the growth side. The remaining
questions are the mirror images of the `3x+1` ones:

1. **Does any positive orbit of `5x−1` fail to diverge?** Equivalently, is the set of odd `m` whose
   orbit is eventually periodic infinite? **OPEN.** (It is nonempty: `m = 1` is a fixed point.)
   Note this is *not* settled by P0 — P0 excludes permanent residence on the rare side, which is a
   much stronger requirement than merely returning to it infinitely often.
2. **Is the set of positive cycles of `5x−1` finite, and is `{1}` the only one?** **OPEN**;
   **VERIFIED** only that `{1}` is the only cycle met by orbits of odd seeds `≤ 20001`.
3. The quantitative question that Phase 1 §3 takes up: **how fast does the least `N`-persistent
   positive integer grow?** P0 says it grows without bound; the rate is a separate matter, and `D`
   is therefore a test-bed on which the qualitative statement is a theorem and only the quantitative
   one is open — the reverse of the `3x+1` situation.

**Literature note. CITED, not verified in this session** (search results only, September 2026):
for `qx+1`-type maps with `q ≥ 5` the drift is positive and the standard heuristic is that almost
all orbits diverge. Stanislav Volkov gave a probabilistic model for the `5x+1` problem (2006);
Kontorovich and Lagarias, *Stochastic Models for the 3x+1 and 5x+1 Problems*
([arXiv:0910.1944](https://arxiv.org/abs/0910.1944)), develop stochastic models predicting that
almost all `5x+1` orbits escape to infinity and that the count of `n ≤ x` whose orbit reaches 1
grows like `x^α` with `α ≈ 0.68`. See also Lagarias, *The 3x+1 Problem: An Annotated Bibliography*
([arXiv:math/0608208](https://arxiv.org/pdf/math/0608208)). These concern `5x+1`; the author is not
aware of a corresponding treatment of `5x−1`, and none was located.
