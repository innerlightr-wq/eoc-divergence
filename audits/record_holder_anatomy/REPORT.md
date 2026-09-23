# Audit: anatomy of the record holders, signed markers, and a Markov-type spectrum

**Exploratory.** Nothing here is, or may be presented as, progress toward (DE) or the Collatz
conjecture. The repository's headline theorem is an equivalence, not an exclusion; see
`docs/PROGRAMME_ENDPOINT.md` and `docs/EQUIVALENT_FORMS_OF_DE.md`.

Labels: **PROVED** (proved here, with the proof written out) · **VERIFIED** (exact computation,
stated range) · **CITED** (source given) · **HEURISTIC** · **OPEN**.

**Status: Phase 1 complete and accepted (P1–P3). Phase 2 in progress.**

## Standing corrections, recorded at the author's instruction

1. **The sign-flip correction (P1.c).** "`T` preserves the sign of nonzero rationals" is **false**:
   `T(−1/5) = 1/5`. Only the one-sided form holds — **positivity is forward-invariant** — and it
   is all the eventually-periodic case needs. **CITED**: Monks–Yazinski, *Discrete Math.* **275**
   (2004), **Lemma 3.4**; part (a) is the forward-invariance, part (b) is the failure on `(−1,0]`.
2. **The M1 ceiling (§P3 → M1).** For an initial square with block `W` of length `ℓ`, `k` ones,
   put `θ_W = (k/ℓ)·log₂3`. The ceiling is
   ```
   ℓ ≤ (log₂ m_k + O(log ℓ)) / (2 − θ_W) ,
   ```
   **computed per block from that block's own `θ_W`**, never from a fixed constant, and **valid
   only when `W` is balanced**. The necessary condition it expresses is therefore *"poor in
   **balanced** squares"* — an unbalanced square of any exponent violates nothing.
3. **P3's corollary (§P3).** *No argument using only the aggregate identity, the confinement
   condition and the sign of the denominator can separate the positive integers from the dust.*
   The `3x+1` and `3x−1` systems agree on all three and disagree on the answer.
4. **(PosPC) belongs in `docs/PROGRAMME_ENDPOINT.md`**, as a strictly stronger signed conjecture
   sitting between (DE) and (LPC) — **not** in `EQUIVALENT_FORMS_OF_DE.md`, which lists
   statements equivalent to (DE).

---

## 0. Setting and notation

Two coordinate systems are used and kept apart.

**Accelerated coordinates** (the repository's). `T(m) = (3m+1)/2^{a(m)}` with `a(m) = v₂(3m+1)`,
acting on the odd elements of `ℤ₂` — equivalently on `ℤ₂^×`, and on rationals with odd
denominator and odd numerator. `m_k = T^k(m_0)`, `S_k = Σ_{i<k} a(m_i)`, `α = log₂3`,
`R_k = S_k − kα`. `m` is **zero-confined for `N` steps** if `2^{S_k} ≤ 3^k` for `1 ≤ k ≤ N`, and
**zero-confined** (`m ∈ K`) if for every `k`. Since `2^{S_k} ≤ 3^k ⟺ S_k ≤ kα`, zero-confinement
is exactly `R_k ≤ 0` for every `k`.

*One exclusion.* `T` is undefined at `m = −1/3`, where `3m+1 = 0` and `a = ∞`. That point is not
in `K`: in standard coordinates its parity word is `1 0^∞`, whose ones-count is eventually
constant, so `R_k → +∞`. Everything below is on `ℤ₂^× ∖ {−1/3}`.

**Parity coordinates** (the paper's). `T_std(x) = x/2` for even `x`, `(3x+1)/2` for odd `x`;
`Φ` the Bernstein–Lagarias conjugacy; `w` a finite parity word of length `ℓ` with `k` ones.

**The aggregate identity. CITED** (`Divergence/Basic.lean`, `aggregate_identity`, machine-checked):
```
2^{S_n} · m_n = 3^n · m_0 + C_n ,     C_0 = 0 ,  C_{n+1} = 3·C_n + 2^{S_n} ,
```
so `C_n = Σ_{i<n} 3^{n−1−i}·2^{S_i}`, and in particular
```
C_n ≥ 3^{n−1} > 0      for every n ≥ 1.                                     (†)
```

---

## P1. The signed marker: every eventually periodic point of `K` is a **negative rational**

### P1.a Purely periodic points, in accelerated coordinates — **PROVED**

> **Proposition 1.** Let `m ∈ ℤ₂^×` be a purely periodic point of `T` of period `L ≥ 1`, with
> total valuation `S := S_L`. If `m` is zero-confined then `m` is a negative rational; explicitly
> ```
> m = C_L / (2^S − 3^L) ,     C_L > 0 ,     2^S − 3^L < 0 .
> ```

*Proof.* Periodicity gives `m_L = m_0 = m`, so the aggregate identity at `n = L` reads
`2^S m = 3^L m + C_L`, i.e. `m(2^S − 3^L) = C_L`. By (†), `C_L > 0`.

Zero-confinement at `k = L` gives `2^S ≤ 3^L`. Equality is impossible: `2^S = 3^L` with `L ≥ 1`
contradicts unique factorisation. Hence `2^S − 3^L < 0`, the denominator is a nonzero integer,
`m = C_L/(2^S − 3^L)` is rational, and it is a positive number over a negative one, so `m < 0`. ∎

Two remarks. First, the denominator is **odd** (`2^S − 3^L` with `S ≥ L ≥ 1`), as it must be for
`m` to be a `2`-adic unit. Second, the proof uses zero-confinement only at the single index
`k = L`; confinement at the intermediate indices is not needed.

*Worked instances (arithmetic by hand, no script).*
`m = −1`: `3(−1)+1 = −2`, `a = 1`, so `L = 1`, `S = 1`, `C_1 = 1`, and `1/(2−3) = −1` ✓, with
`2^1 = 2 ≤ 3 = 3^1`.
`m = −5`: `T(−5) = −14/2 = −7`, `T(−7) = −20/4 = −5`, so `L = 2`, valuation word `(1,2)`,
`S = 3`, `C_2 = 3·2^0 + 1·2^1 = 5`, and `5/(8−9) = −5` ✓, with `2^3 = 8 ≤ 9 = 3^2`.

### P1.b The same statement in parity coordinates — **PROVED** (from paper Prop. 4.1)

> **Proposition 1′.** Let `w` be a finite parity word of length `ℓ` with `k ≥ 1` ones, and
> suppose the periodic point `Φ(w^∞)` is zero-confined. Then `Φ(w^∞) < 0`.

*Proof.* Paper Prop. 4.1 gives `Φ(w^∞) = c_w/(2^ℓ − 3^k)` with
`c_w = Σ_{i<ℓ, w_i=1} 3^{k−k_{i+1}(w)} 2^i ∈ ℤ_{>0}`, and `2^ℓ ≠ 3^k`. In parity coordinates
zero-confinement reads `k_j(w^∞) ≥ jβ` for every `j`, i.e. `2^j ≤ 3^{k_j}`; at `j = ℓ` this is
`2^ℓ ≤ 3^k`, hence `2^ℓ − 3^k < 0` and `Φ(w^∞) < 0`. ∎

The two propositions are the same fact in the two coordinate systems; P1.a is the one that
matches the Lean development.

### P1.c Eventually periodic points — **PROVED**, and **a correction to the brief**

> **Proposition 2.** Every eventually periodic point of `K` is a negative rational.

The brief proposes to get this from "`T` preserves the sign of nonzero rationals". **That
statement is false.** Counterexample, in accelerated coordinates: `m = −1/5` is a `2`-adic unit,
`3m+1 = 2/5`, `a = v₂(2/5) = 1`, so `T(−1/5) = 1/5 > 0`. The sign is not preserved anywhere on
`(−1/3, 0)`, where `3m+1 > 0`. What *is* true is the one-sided version, and it is the one needed:

> **Lemma 3 (positivity is forward-invariant).** If `m > 0` is a rational `2`-adic unit then
> `T(m) > 0`, hence every `m_k > 0`.
>
> *Proof.* `m > 0 ⟹ 3m+1 > 1 > 0`, and dividing by `2^{a} > 0` preserves the sign. ∎

(The standard-coordinate analogue is **CITED**: Monks–Yazinski, *Discrete Math.* **275** (2004),
Lemma 3.4(a), "if `x > 0` then `O(x)` is strictly positive"; their (b) is exactly the failure on
`(−1, 0]`, which is why the two-sided phrasing is wrong.)

*Proof of Proposition 2.* Let `x ∈ K` be eventually periodic; say `m_j` is purely periodic of
period `L`, with cycle total `S_cyc = S_{j+L} − S_j`. For every `t ≥ 0`,
```
R_{j+tL} = R_j + t·(S_cyc − Lα) ,
```
and zero-confinement gives `R_{j+tL} ≤ 0` for all `t`, so the increment satisfies
`S_cyc − Lα ≤ 0`, i.e. `2^{S_cyc} ≤ 3^L`. Applying the computation of Proposition 1 to the cycle
through `m_j` (which needs confinement only at that one index, as noted) gives `m_j < 0`, and
`m_j` rational.

Now `x` is rational: `x` is determined by `m_j` through `j` backward steps, each of which is
`m ↦ (2^{a}m' − 1)/3` with `a` and `m'` rational, so `x ∈ ℚ`. And `x < 0`: if `x > 0` then by
Lemma 3 every `m_k > 0`, in particular `m_j > 0`, contradicting `m_j < 0`. `x = 0` is excluded
because `0` is not a unit. Hence `x < 0`. ∎

### What P1 is, and is not

**Classification: PROVED, but not new — a re-derivation that makes an existing observation into
a marker.** The negative zero-confined cycles `{−1}` and `{−5,−7}` are already recorded in
`audits/descent/DESCENT_AUDIT.md`, control C2, and Prop. 4.1 is in the paper. What P1 adds is
the *general* statement with its sign, in both coordinate systems, and the correction in P1.c.

Its use is as a **marker**: the rational points of `K` that can be enumerated are all on the
negative side, so the positive side is precisely where the open problem lives. It rules nothing
out on the positive side, because nothing in Proposition 1 or 2 applies to a point that is not
eventually periodic.

---

## P2. The positive-side Periodicity Conjecture

> **(PosPC)** `K` contains no positive rational.

Equivalently: no rational `2`-adic unit `x > 0` satisfies `2^{S_k(x)} ≤ 3^k` for every `k`.

### P2(i) Lagarias's Periodicity Conjecture ⇒ (PosPC) — **PROVED**

**CITED** (paper §1, Lagarias 1985 §2): **(LPC)** no aperiodic parity vector has a rational
`Φ`-value; equivalently, every `x ∈ ℚ ∩ ℤ₂` has an eventually periodic parity vector, i.e. an
eventually cyclic orbit.

*Proof.* Suppose `x ∈ K ∩ ℚ` with `x > 0`. By (LPC) the orbit of `x` is eventually cyclic, so `x`
is an eventually periodic point of `K`; by Proposition 2, `x < 0`. Contradiction. ∎

### P2(ii) (PosPC) ⇒ (DE) — **PROVED**

*Proof.* (DE) is the assertion that no positive odd integer lies in `K`
(`Divergence.divergent_iff_zeroConfined`, right-hand side negated). A positive odd integer is a
positive rational `2`-adic unit, so (PosPC) excludes it. ∎

> **The implication is strict as far as anything known goes.** (PosPC) also excludes positive
> non-integer rationals, and no argument here recovers it from (DE). **(PosPC) should therefore
> *not* be added to `EQUIVALENT_FORMS_OF_DE.md`**, whose whole purpose is to list statements that
> are *equivalent* to (DE) so that a reformulation is not mistaken for progress. (PosPC) is a
> strictly stronger statement, and P2(iii) says exactly how much stronger.

### P2(iii) (PosPC) ⇔ zero-confinement fails for every `3x+v` — **PROVED**

> **Proposition 4.** (PosPC) holds **iff** for every odd `v ≥ 1`, no positive odd integer `n₀` has
> a zero-confined `T_v`-orbit, where `T_v(n) = (3n+v)/2^{v₂(3n+v)}` on odd `n`.

Here the `T_v`-orbit's valuations `a_j = v₂(3n_j+v)` define `S_k` exactly as before, and
"zero-confined" means `2^{S_k} ≤ 3^k` for every `k`.

*Proof.* **(⇒).** Suppose some odd `v ≥ 1` and odd `n₀ > 0` have a zero-confined `T_v`-orbit
`(n_j)`. Put `x_j = n_j/v ∈ ℚ`. Since `v` is odd, each `x_j` is a `2`-adic unit, and `x_j > 0`.
Moreover
```
x_{j+1} = n_{j+1}/v = (3n_j+v)/(v·2^{a_j}) = (3x_j+1)/2^{a_j} ,
```
and `a_j = v₂(3n_j+v) = v₂(v(3x_j+1)) = v₂(3x_j+1)` because `v` is odd. So `x_{j+1} = T(x_j)`
with the *same* valuation at every step, hence the same `S_k`. Therefore `x_0 = n₀/v` is a
positive rational in `K`, and (PosPC) fails.

**(⇐).** Suppose `x ∈ K` is a positive rational, `x = u/v` in lowest terms with `v ≥ 1` odd and
`u ≥ 1` odd (odd because `x` is a `2`-adic unit; `u ≥ 1` because `x > 0`). Put `n_j = v·T^j(x)`.
Each `n_j` is an integer, directly: `n_{j+1} = v·T(x_j) = (3n_j+v)/2^{a_j}` with
`a_j = v₂(3x_j+1) = v₂(3n_j+v)` (again because `v` is odd), and dividing an integer by the exact
power of two it contains leaves an integer. (The standard-coordinate form of the same closure is
**CITED**: Monks–Yazinski Lemma 3.1(a), `T((1/h)ℤ) ⊆ (1/h)ℤ` for odd `h`.) Each `n_j`
is odd (`n_j = v·x_j` with `v`, `x_j` both odd units) and positive (Lemma 3), and
`n_{j+1} = v·T(x_j) = (3n_j+v)/2^{a_j}` with `a_j = v₂(3n_j+v)`. So `(n_j)` is a `T_v`-orbit of
positive odd integers with the same `S_k`, hence zero-confined. ∎

**The three checks the brief asks for, explicitly.**

* *Denominators.* The correspondence needs `v` **odd** in both directions: in (⇒) to make `x_j` a
  `2`-adic unit and to transfer the valuation, in (⇐) because `v` is the denominator of a
  `2`-adic unit and is therefore automatically odd. The reduction is not to lowest terms in (⇒):
  any odd `v` works, and `gcd(n₀,v) > 1` is harmless.
* *Parity.* `3n+v` is even for `n`, `v` both odd, so `T_v` is defined on odd `n` and returns odd
  `n` — the same closure the `3x+1` map has. This is where `v` odd is used a third time.
* *The scaling.* Scaling by `v` is an exact conjugacy of the two maps, **valuation by
  valuation**, not merely up to bounded error. This matters: `S_k` is preserved on the nose, so
  zero-confinement — a statement about `S_k` at *every* index — transfers without slack. A
  scaling that changed even one `a_j` would break the correspondence.

**Reading.** (PosPC) is (DE) asserted simultaneously for the whole family `3x+v`, `v` odd — the
accelerated analogue of the paper's Corollary 7.3. **CITED**: the paper's Cor. 7.3 makes the same
move in parity coordinates for the maps `T_q`. So the content of P2 is: *the positive side of `K`
is exactly the union, over odd `v`, of the `3x+v` divergence questions*, and (LPC) implies all of
them at once.

---

## P3. Sign control: the `3x−1` system

> **Proposition 5.** Let `T'(m) = (3m−1)/2^{v₂(3m−1)}` on odd `m`, with `S_k` defined as before.
> If `m` is a purely periodic point of `T'` of period `L` with total `S` and is zero-confined,
> then
> ```
> m = C'_L / (3^L − 2^S) ,   C'_L = Σ_{i<L} 3^{L−1−i}·2^{S_i} > 0 ,   3^L − 2^S > 0 ,
> ```
> so **`m > 0`**.

*Proof.* The one-step identity is `2^{a_k} m_{k+1} = 3m_k − 1`. With `X_k = 2^{S_k}m_k` this gives
`X_{k+1} = 3X_k − 2^{S_k}`, so `X_n = 3^n m_0 − C'_n` with the *same* positive carry
`C'_n = Σ_{i<n}3^{n−1−i}2^{S_i}`. The `−1` has moved the carry to the other side. At `n = L`,
periodicity gives `2^S m = 3^L m − C'_L`, i.e. `m(3^L − 2^S) = C'_L`. Zero-confinement gives
`2^S ≤ 3^L`, strictly by unique factorisation, so both `C'_L` and `3^L − 2^S` are positive and
`m > 0`. ∎

*Worked instance (by hand).* `m = 1`: `3·1−1 = 2`, `a = 1`, so `L = 1`, `S = 1`, `C'_1 = 1`, and
`1/(3−2) = 1` ✓, with `2^1 = 2 ≤ 3`. So `+1` is a zero-confined **positive** periodic point of the
`3x−1` system, exactly as `audits/descent/DESCENT_AUDIT.md` control C3 records.

### Where the sign changes, and what the marker does there

**The sign flips at exactly one place, and it is visible.** In both systems
`C_L = Σ 3^{L−1−i}2^{S_i} > 0`; what differs is which side of the periodicity equation it lands
on:

| | `3x+1` | `3x−1` |
|---|---|---|
| aggregate identity | `2^{S_n}m_n = 3^n m_0 + C_n` | `2^{S_n}m_n = 3^n m_0 − C'_n` |
| periodic point | `m = C_L/(2^S − 3^L)` | `m = C'_L/(3^L − 2^S)` |
| zero-confined ⟹ denominator | `2^S − 3^L < 0` | `3^L − 2^S > 0` |
| **conclusion** | **`m < 0`** | **`m > 0`** |

The zero-confinement hypothesis does the *same* work in both columns — it fixes the sign of
`3^L − 2^S`. The `±1` decides which numerator that sign multiplies. This is the same dependence
on the sign of the `+1` that the descent audit isolated (there: the backward fixed point sits at
`−1` for `3x+1` and at `+1` for `3x−1`), seen from the forward side.

**The marker behaves correctly. PROVED.** Proposition 5 says that for `3x−1` the marker points
the *other* way: it asserts that zero-confined periodic points there are **positive**, and `+1`
is one. It therefore makes **no claim that positivity is excluded for `3x−1`** — and it could
not, since that claim is false. Any argument for the `3x+1` positive side that would survive
transplanting to `3x−1` is thereby invalid, and P1 does not survive that transplant: the
transplanted P1 yields positivity, not a contradiction with it.

### P3 Corollary — the limit of the whole method. **PROVED**

> **No argument that uses only (i) the aggregate identity, (ii) the confinement condition and
> (iii) the sign of the denominator can separate the positive integers from the rest of `K`.**

P1 is a statement
about *eventually periodic* points only. The `3x−1` control shows that no strengthening of P1
that keeps using only the aggregate identity and the sign of the denominator can reach the
non-eventually-periodic points: the two systems have identical aggregate identities up to the
sign of the carry, identical confinement conditions, and identical `S_k` combinatorics, yet
opposite answers on the positive side. Whatever separates them must be something P1 does not
use.

---

## Answers to the Phase-1 part of the pre-registered questions

Q1–Q4 are Phase-3 questions and are not answered here. Two things Phase 1 already settles:

* The **signed marker is well defined and one-directional**: it classifies the eventually
  periodic points of `K` (all negative, for `3x+1`) and says nothing about the rest. Phase 3's
  M3 — the signed border from record holders to the negative rational points of `K` — is
  therefore a measurement against a set that P1 has now characterised, which is what makes it
  worth measuring.
* The **`3x−1` control is live from the start**, not only at Phase 3: P3 shows it already
  separates the two systems at the level of the marker. Every Phase-3 measurement must be run on
  it (control C4), and a pattern that does not distinguish `3x+1` from `3x−1` is, by P3, not
  about the sign.

## Classification of the Phase-1 findings

| finding | status | new? |
|---|---|---|
| P1.a/P1.b — zero-confined periodic points of `3x+1` are negative rationals | **PROVED** | **explained by known facts** — a general re-derivation of Prop. 4.1 and of the descent audit's C2 observation, in both coordinate systems |
| P1.c — "`T` preserves the sign of nonzero rationals" is **false** (`−1/5 ↦ 1/5`); the correct input is one-sided forward-invariance of positivity | **PROVED** | **a correction to the brief**; the one-sided form is CITED (Monks–Yazinski Lemma 3.4(a)) |
| P2(i) (LPC) ⇒ (PosPC), P2(ii) (PosPC) ⇒ (DE) | **PROVED** | routine, but the strictness matters |
| P2 — (PosPC) is **strictly stronger** than (DE) as far as anything known, and must **not** be added to `EQUIVALENT_FORMS_OF_DE.md` | **PROVED** (the implication) / **OPEN** (the converse) | **genuinely useful bookkeeping** |
| P2(iii) — (PosPC) ⇔ (DE) for every `3x+v`, `v` odd, by an exact valuation-by-valuation conjugacy | **PROVED** | **explained by known facts** — the accelerated analogue of the paper's Cor. 7.3 |
| P3 — the identical argument gives **positivity** for `3x−1`; the marker points the other way and correctly claims nothing | **PROVED** | **genuinely new as stated**, though it is the forward-side twin of the descent audit's fixed-point observation |
| P3 corollary — no strengthening of P1 using only the aggregate identity and the denominator sign can reach the non-eventually-periodic points | **PROVED** | **genuinely new**, and it is a limit on the method, not a result |

**Nothing in Phase 1 bears on (DE) or on the Collatz conjecture.** P1 classifies a set of points
that is, by construction, disjoint from the open question; P2 relates (PosPC) to (DE) in the easy
direction only; P3 is a control that shows where the sign enters.

---

## Phase 2 onward

Phase 2 follows below. Phase 3's interpretation (M2–M4 and the answers to Q1–Q4) is **not**
offered here, by instruction: Phase 2 reports data.

---

# Phase 2 — record-holder data

**Status: data only. No Phase-3 interpretation is offered here.** Q1–Q4 are answered in Phase 3.

## 2.0 The exact method

`scripts/scan.c` (and `scan_pm.c`, the `3x±1` variant). For odd `m` it iterates
`x ↦ (3x+1)/2^{v₂(3x+1)}`, accumulating `S_k`, and stops at the first `k` with `S_k > A[k]`,
where **`A[k] = floor(k·log₂3) = bit_length(3^k) − 1`** is precomputed exactly in
`alpha_table.h`. Confinement `2^{S_k} ≤ 3^k` is exactly `S_k ≤ A[k]`, because `2^{S} = 3^k` is
impossible for `k ≥ 1`. **No floating-point value enters any decision**, and no big-integer
arithmetic enters the inner loop: orbit values are carried in `unsigned __int128` behind an
overflow guard at `2^100` (never triggered; the largest orbit value seen over the whole scan has
42 bits).

Two exact prunings:

* **Only `m ≡ 3 (mod 4)` can be 1-confined.** `S_1 = v₂(3m+1)` and `2^{S_1} ≤ 3` force
  `S_1 = 1`, i.e. `3m+1 ≡ 2 (mod 4)`, i.e. `m ≡ 3 (mod 4)`. The scan steps by 4. (For `3x−1`
  the same computation gives `m ≡ 1 (mod 4)`.)
* Since the scan runs in increasing `m`, the first three `m` it meets with depth `≥ N` **are**
  `r₁(N) < r₂(N) < r₃(N)`. No post-processing is needed beyond merging disjoint ranges.

**Speed.** `audits/descent/rmin_scan.py` took **79.7 s** to reach `10⁸`; `scan.c` takes
**0.74 s** — a factor **108**. The work is linear in the bound, so this is what makes the
extension below feasible at all.

**A second, independent exact method** is used as a cross-check on the *words* rather than the
integers: `anatomy.minrep(word)` reconstructs the least positive odd `m` realizing a given
valuation word, from the fact that the odd `m` with a given word of total `S` form exactly one
residue class mod `2^{S+1}` (Terras/Everett; the repository's `modEq_of_parity_prefix`). The
class is refined one letter at a time by solving `A′ + 3^{k+1}t ≡ 2^{d−1} (mod 2^d)` for `t`.
**VERIFIED:** `minrep` applied to each record holder's own valuation word returns that record
holder, and the same total `S`, for all of them.

**A third check, on the scanner itself.** The C scanner was compared against an independent
Python reference implementation (`anatomy.conf_depth`, arbitrary precision) on **40 random
4000-wide windows below `10^11`**: identical maximum depth *and* identical argmax in every
window, no exception. This is independent of the `N ≤ 200` cross-check below, which tests the
scanner against previously published values rather than against a second implementation.

## 2.1 Cross-check against the published `N ≤ 200` table

**VERIFIED. PASS — all 200 values agree** with the record-holder table of
`audits/descent/DESCENT_AUDIT.md`, recomputed from scratch by the new method.

**One immediate correction, from the same `10⁸` range.** The published table stops at `N = 200`
because *the scan* stopped there, not because the number did: `r₁ = 63728127` has confinement
depth **236**, so it is `r₁(N)` for **`N = 194 … 236`**, not merely `194 … 200`.

## 2.2 The record holders `r₁, r₂, r₃`

Exact scan of every odd `m ≡ 3 (mod 4)` below **1 000 000 000 000** = `2^39`  in 37 min on 8 cores.
`r₁(N)` is therefore certified for **`N = 1 … 346`**, and the full triple `r₁,r₂,r₃` for `N = 1 … 344`.

| `N`-range | `r₁` | `r₂` | `r₃` | `r₁ mod 12` | `v₃(r₁+1)` = chain | `r₂/r₁` | `r₃/r₂` |
|---|---|---|---|---|---|---|---|
| 1–1 | 3 | 7 | 11 | 3 | 0 | 2.3333 | 1.5714 |
| 2–2 | 7 | 11 | 15 | 7 | 0 | 1.5714 | 1.3636 |
| 3–3 | 7 | 15 | 27 | 7 | 0 | 2.1429 | 1.8000 |
| 4–4 | 27 | 31 | 39 | 3 | 0 | 1.1481 | 1.2581 |
| 5–33 | 27 | 31 | 47 | 3 | 0 | 1.1481 | 1.5161 |
| 34–34 | 27 | 31 | 703 | 3 | 0 | 1.1481 | 22.6774 |
| 35–36 | 27 | 703 | 1 055 | 3 | 0 | 26.0370 | 1.5007 |
| 37–49 | 703 | 1 055 | 1 407 | 7 | 0 | 1.5007 | 1.3336 |
| 50–50 | 703 | 1 407 | 10 087 | 7 | 0 | 2.0014 | 7.1692 |
| 51–51 | 10 087 | 15 039 | 34 239 | 7 | 0 | 1.4909 | 2.2767 |
| 52–57 | 10 087 | 34 239 | 35 655 | 7 | 0 | 3.3944 | 1.0414 |
| 58–65 | 10 087 | 35 655 | 37 503 | 7 | 0 | 3.5347 | 1.0518 |
| 66–69 | 35 655 | 37 503 | 45 055 | 3 | 0 | 1.0518 | 1.2014 |
| 70–78 | 35 655 | 37 503 | 45 127 | 3 | 0 | 1.0518 | 1.2033 |
| 79–79 | 35 655 | 45 127 | 60 975 | 3 | 0 | 1.2657 | 1.3512 |
| 80–80 | 35 655 | 45 127 | 270 271 | 3 | 0 | 1.2657 | 5.9891 |
| 81–84 | 35 655 | 270 271 | 288 615 | 3 | 0 | 7.5802 | 1.0679 |
| 85–95 | 270 271 | 288 615 | 362 343 | 7 | 0 | 1.0679 | 1.2555 |
| 96–96 | 270 271 | 362 343 | 376 831 | 7 | 0 | 1.3407 | 1.0400 |
| 97–102 | 270 271 | 362 343 | 381 727 | 7 | 0 | 1.3407 | 1.0535 |
| 103–103 | 362 343 | 381 727 | 401 151 | 3 | 0 | 1.0535 | 1.0509 |
| 104–104 | 381 727 | 401 151 | 626 331 | 7 | 0 | 1.0509 | 1.5613 |
| 105–108 | 381 727 | 626 331 | 667 375 | 7 | 0 | 1.6408 | 1.0655 |
| 109–109 | 626 331 | 667 375 | 1 027 431 | 3 | 0 | 1.0655 | 1.5395 |
| 110–110 | 626 331 | 1 027 431 | 1 126 015 | 3 | 0 | 1.6404 | 1.0960 |
| 111–114 | 1 027 431 | 1 126 015 | 1 127 871 | 3 | 0 | 1.0960 | 1.0016 |
| 115–115 | 1 126 015 | 1 127 871 | 1 327 743 | 7 | 0 | 1.0016 | 1.1772 |
| 116–117 | 1 126 015 | 1 327 743 | 1 394 431 | 7 | 0 | 1.1792 | 1.0502 |
| 118–134 | 1 126 015 | 1 394 431 | 1 689 023 | 7 | 0 | 1.2384 | 1.2113 |
| 135–139 | 1 126 015 | 1 689 023 | 2 252 031 | 7 | 0 | 1.5000 | 1.3333 |
| 140–140 | 1 126 015 | 2 252 031 | 8 088 063 | 7 | 0 | 2.0000 | 3.5915 |
| 141–144 | 8 088 063 | 9 280 639 | 12 132 095 | 3 | 0 | 1.1474 | 1.3072 |
| 145–153 | 8 088 063 | 12 132 095 | 13 421 671 | 3 | 0 | 1.5000 | 1.1063 |
| 154–154 | 8 088 063 | 13 421 671 | 14 378 779 | 3 | 0 | 1.6594 | 1.0713 |
| 155–156 | 13 421 671 | 14 378 779 | 19 638 399 | 7 | 0 | 1.0713 | 1.3658 |
| 157–165 | 13 421 671 | 19 638 399 | 20 132 507 | 7 | 0 | 1.4632 | 1.0252 |
| 166–179 | 13 421 671 | 20 132 507 | 20 638 335 | 7 | 0 | 1.5000 | 1.0251 |
| 180–180 | 13 421 671 | 20 638 335 | 26 716 671 | 7 | 0 | 1.5377 | 1.2945 |
| 181–183 | 20 638 335 | 26 716 671 | 56 924 955 | 3 | 0 | 1.2945 | 2.1307 |
| 184–187 | 26 716 671 | 56 924 955 | 63 728 127 | 3 | 0 | 2.1307 | 1.1195 |
| 188–191 | 56 924 955 | 63 728 127 | 64 040 575 | 3 | 0 | 1.1195 | 1.0049 |
| 192–193 | 56 924 955 | 63 728 127 | 95 592 191 | 3 | 0 | 1.1195 | 1.5000 |
| 194–216 | 63 728 127 | 95 592 191 | 96 883 183 | 3 | 0 | 1.5000 | 1.0135 |
| 217–228 | 63 728 127 | 95 592 191 | 181 930 687 | 3 | 0 | 1.5000 | 1.9032 |
| 229–231 | 63 728 127 | 95 592 191 | 217 740 015 | 3 | 0 | 1.5000 | 2.2778 |
| 232–232 | 63 728 127 | 217 740 015 | 1 104 180 463 | 3 | 0 | 3.4167 | 5.0711 |
| 233–236 | 63 728 127 | 217 740 015 | 1 200 991 791 | 3 | 0 | 3.4167 | 5.5157 |
| 237–241 | 217 740 015 | 1 200 991 791 | 1 442 817 471 | 3 | 0 | 5.5157 | 1.2014 |
| 242–248 | 217 740 015 | 1 200 991 791 | 1 801 487 687 | 3 | 0 | 5.5157 | 1.5000 |
| 249–249 | 1 200 991 791 | 1 801 487 687 | 1 827 397 567 | 3 | 0 | 1.5000 | 1.0144 |
| 250–250 | 1 200 991 791 | 1 827 397 567 | 2 741 096 351 | 3 | 0 | 1.5216 | 1.5000 |
| 251–269 | 1 827 397 567 | 2 741 096 351 | 2 788 008 987 | 7 | 0 | 1.5000 | 1.0171 |
| 270–272 | 1 827 397 567 | 2 788 008 987 | 3 136 510 111 | 7 | 0 | 1.5257 | 1.1250 |
| 273–275 | 2 788 008 987 | 3 136 510 111 | 4 704 765 167 | 3 | 0 | 1.1250 | 1.5000 |
| 276–276 | 2 788 008 987 | 3 136 510 111 | 6 273 020 223 | 3 | 0 | 1.1250 | 2.0000 |
| 277–279 | 2 788 008 987 | 3 136 510 111 | 12 235 060 455 | 3 | 0 | 1.1250 | 3.9009 |
| 280–281 | 2 788 008 987 | 12 235 060 455 | 14 500 812 391 | 3 | 0 | 4.3885 | 1.1852 |
| 282–340 | 12 235 060 455 | 14 500 812 391 | 18 352 590 683 | 3 | 0 | 1.1852 | 1.2656 |
| 341–343 | 12 235 060 455 | 14 500 812 391 | 21 751 218 587 | 3 | 0 | 1.1852 | 1.5000 |
| 344–344 | 12 235 060 455 | 14 500 812 391 | 850 097 105 055 | 3 | 0 | 1.1852 | 58.6241 |
| 345–346 | 898 696 369 947 | — | — | 3 | 0 | — | — |

**24 distinct values of `r₁`**, strictly increasing. `r₁ mod 12 ∈ {3,7}` and `v₃(r₁+1) = 0` at every one (PASS).

**The runtime wall.** The work is linear in the bound. Fitting the last twelve jump points (the first `N` at which each new `r₁` appears) gives

```
log₂ r₁(N)  ≈  0.0811·N + 10.25     (doubling every 12.3 steps of N)
```

so each `+12.3` in `N` doubles the scan. At the measured rate (37 min for `2^39` on 8 cores):

* `N ≈ 371` needs a bound near `2^40` ≈ 1.4e+12 — about **52 min**;
* `N ≈ 396` needs a bound near `2^42` ≈ 5.7e+12 — about **3.5 h**;
* `N ≈ 446` needs a bound near `2^46` ≈ 9.6e+13 — about **58.5 h**;

So the practical wall on this machine is **`N ≈ 371`–`391`**: a few hours. Beyond that a linear scan is the wrong tool, and the next step would have to be a search over the class tree rather than over the integers.

## 2.3 M1 — the square-poorness profile, exact

`scripts/m1.py`. For an integer `m` whose parity word begins with a repetition of block `W`
(`|W| = ℓ`, `k` ones, agreement length `R`, exponent `e = R/ℓ`), with
`δ_W = 2^ℓ − 3^k`, `c_W` as in paper eq. (4.1) and `M = m·δ_W − c_W`:

```
v₂(M) = R                      exactly, by the isometry (paper Prop. 2.2)
|M| ≤ |m|·(|δ_W| + c_W)
 ⟹  R ≤ log₂|m| + log₂(|δ_W| + c_W)
 ⟹  Q := ℓ·(e − max(1, θ_W)) ≤ log₂|m| + O(log ℓ),     θ_W = (k/ℓ)·log₂3,
```
the last step using the **balanced** height bound `c_W ≤ 3ℓ·max(2^ℓ,3^k)`. At `e = 2` this is
the brief's ceiling, `ℓ ≤ (log₂m + O(log ℓ))/(2 − θ_W)`, computed per block from that block's
own `θ_W`. Every test is an exact integer test; `Q` is evaluated as the integer
`R − max(ℓ, bit_length(3^k) − 1)`.

**Two exact checks are run on every row, at every step of every orbit.**

* the **isometry** `v₂(M) = R` — this is the derivation's load-bearing identity;
* the **upper bound** `|M| ≤ |m|(|δ_W| + c_W)` and hence `slack = bitlen(rhs) − R ≥ 0`.

> **Result. VERIFIED, and the stop rule did not fire.**
> Over every record holder, every control, and every step of every confined run —
> **several thousand rows** —
> * **isometry check `v₂(M) = R`: 0 failures**;
> * **balanced blocks with negative slack: 0**;
> * **other flagged rows: 0**.
>
> No violation by a balanced block was found, so there is nothing to stop and report under the
> M1 stop rule. The derivation of Phase 1's Correction 2 is confirmed on data: the rows with
> the largest `Q` relative to `log₂|m_k|` are always balanced or near-balanced, and unbalanced
> blocks never come near the ceiling.

## 2.4 Controls

### C1 — the negative zero-confined cycles

| point | conf. depth (cap 240) | note |
|---|---|---|
| `−1` | 240 (i.e. forever) | fixed point, valuation word `(1)^∞`; parity word `1^∞`, so `M = 0` at every period — correctly flagged *periodic*, ceiling vacuous |
| `−5` | 240 (forever) | the `{−5,−7}` cycle, valuation word `(1,2)^∞` |
| `−7` | **0** | **same cycle, other rotation.** `v₂(3(−7)+1) = v₂(−20) = 2` and `2² > 3`, so `−7` fails confinement at the *first* step |
| `−17` | 240 (forever) | the 11-element cycle; `ℓ = 11`, `k = 7`, `2¹¹ = 2048 ≤ 2187 = 3⁷` |
| `−25` | 5 | another rotation of the same cycle |
| `−91` | 0 | another rotation |
| `−3, −11, −43` | 0 | the `d ≥ 3` preimages of `−1`; **L3** — only `d = 1` preserves confinement backward |

**Recorded observation (VERIFIED, and it is the cycle lemma).** Zero-confinement is **not** a
property of a cycle but of a *starting point on it*: `−5` is confined forever and `−7`, on the
same cycle, fails at step one. `Occupation.exists_rot_confined` is exactly the statement that
*some* rotation is confined.

### C2 — the critical Sturmian point

Valuation word `d_i = ⌊(i+1)α⌋ − ⌊iα⌋ ∈ {1,2}` (exact: `⌊iα⌋ = bit_length(3^i) − 1`), so
`S_N = ⌊Nα⌋ = A[N]` — the word sits exactly on the confinement boundary at every index. Its
least realizers, by the class construction:

| `N` | `S_N` | class modulus | `r(D_N)` | `log₂ r(D_N) − S_N` |
|---|---|---|---|---|
| 10 | 15 | `2^16` | 23 547 | −1 |
| 20 | 31 | `2^32` | 3 384 695 803 | 0 |
| 30 | 47 | `2^48` | 71 106 568 281 083 | −1 |
| 40 | 63 | `2^64` | 12 466 316 350 106 524 667 | 0 |
| 50 | 79 | `2^80` | 552 492 451 323 951 177 423 867 | −1 |
| 60 | 95 | `2^96` | 5 149 367 558 190 029 606 251 027 451 | −3 |

**`r(D_N) ≈ 2^{S_N}`: the Sturmian edge realizer is essentially the whole class modulus.** The
extremal *word* is not the extremal *realizer*.

### C3 — random confined words, and shuffled surrogates

*Random.* Draw `d_k` uniformly from `{1,…,A[k] − S_{k−1}}` at each step (uniform over the
allowed letter, **not** uniform over words — stated because it matters), then take the least
realizer. Median over 12 draws:

| `N` | median `log₂ r` | range | `S_N = A[N]` |
|---|---|---|---|
| 40 | 62 | 57 – 63 | 63 |
| 80 | 125 | 121 – 126 | 126 |
| 160 | 253 | 250 – 253 | 253 |

*Shuffled surrogates.* Permute a record holder's **own** valuation word — same multiset of
valuations, hence the **same ones-density and the same total drift** — and keep the permutations
that are still zero-confined. Six draws each:

| record holder `r₁` | `log₂ r₁` | depth | `log₂` of the surrogate's least realizer |
|---|---|---|---|
| 1 126 015 | 20 | 140 | 215, 215, 216, 217, 217, 217 |
| 8 088 063 | 22 | 154 | 241, 241, 242, 242, 243, 243 |
| 13 421 671 | 23 | 180 | 280, 281, 283, 283, 283, 283 |
| 26 716 671 | 24 | 187 | 292, 292, 295, 295, 295, 295 |
| 56 924 955 | 25 | 193 | 301, 304, 305, 305, 305, 305 |
| 63 728 127 | 25 | **236** | 368, 368, 373, 373, 373, 373 |

> **What this does and does not show — recorded at the author's instruction.** A permutation of
> a record holder's own valuation word, preserving density and total drift exactly, has a least
> realizer around `2^{370}` where the record holder itself is `2^{25}`, with at most **5 bits**
> of spread across draws.
>
> **That gap is a selection effect, and C3-shuffle is the wrong null for size.** A record holder
> is the **minimum over all** zero-confined words of length `N`; a shuffled surrogate is **one
> typical** word, whose least realizer necessarily sits near `2^{S}` — the class modulus — since
> the least element of a class mod `2^{S+1}` is of that order for a generic class. Comparing a
> minimum-over-a-huge-family against a single draw measures the size of the family, not any
> property of the record holder.
>
> So the shuffle control retains a narrower value: it shows that **ordering, not density or
> endpoint drift, is what distinguishes one confined word from another** — a shuffled word is
> still confined, still has the same `S_N`, and its realizer is still generic. For **size**, the
> correct null is the random-placement model `N0` of §2.7, which compares `r_k(N)` against the
> exact density `p_N(0)` and so accounts for the size of the family.

### C4 — the `3x−1` sign control

> **PROVED, and VERIFIED.** `m ↦ −m` is an **exact conjugacy** from `3x−1` on the positive
> integers to `3x+1` on the negative integers: `v₂(3(−m)+1) = v₂(1−3m) = v₂(3m−1)` and
> `T(−m) = −T′(m)`, so the two systems have **identical valuation words, identical `S_k`, and
> identical confinement**. VERIFIED on every odd `m < 4000` to depth 300: identical words and
> identical depths, no exception.

So C4 and C1 are the *same data* under a sign flip, which is exactly what P3 predicted. The
record-holder ladder makes the contrast visible:

| system | `r₁(N)` | `r₂(N)` | `r₃(N)` |
|---|---|---|---|
| `3x+1`, `N = 1 … 236` | 3 → 63 728 127, **18 distinct values, strictly increasing** | 7 → … | 11 → … |
| **`3x−1`, `N = 1 … 1000`** | **1, for every `N`** | **5, for every `N ≥ 1`** | **17, for every `N ≥ 3`** |

For `3x−1` the ladder is **degenerate**: `r₁(N)` does not grow at all, because `1`, `5` and `17`
lie on positive zero-confined cycles and are confined forever. By the conjugacy these are
`−1`, `−5`, `−17`. Note also `r₁ ≡ 1 (mod 12)` there, so **L4's residue law is sign-specific
too**.

## 2.5 What Correction 2 actually says, tested

`scripts/unbalanced_demo.py`. The Phase-1 correction says the M1 ceiling is **proved only for
balanced blocks**, because its input is the balanced height bound `c_W ≤ 3ℓ·max(2^ℓ,3^k)`. It is
worth being precise about what was and was not observed.

Take `W = 1 0^a 1^a` and the parity word `W W`; the least integer realizing it is
`(−c_L·3^{−k_L}) mod 2^L` (paper Prop. 2.2's computation), and it reproduces the word exactly.

| `a` | `ℓ` | `k` | `disc(W)` | balanced | `c_W / (3ℓ·max(2^ℓ,3^k))` | `log₂m` | `R` | ceiling | holds? | `v₂(M)=R` |
|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 5 | 3 | 4/5 | yes | 0.102 | 9 | 12 | 15.28 | ✓ | ✓ |
| 6 | 13 | 7 | 36/13 | no | 0.269 | 23 | 26 | 30.00 | ✓ | ✓ |
| 12 | 25 | 13 | 144/25 | no | **1.717** | 47 | 53 | 55.19 | ✓ | ✓ |
| 16 | 33 | 17 | 256/33 | no | **6.625** | 65 | 67 | 74.12 | ✓ | ✓ |
| 20 | 41 | 21 | 400/41 | no | **27.03** | 81 | 83 | 89.88 | ✓ | ✓ |
| 24 | 49 | 25 | 576/49 | no | **114.5** | 97 | 99 | 106.02 | ✓ | ✓ |

> **The honest reading. VERIFIED.** The **input** to the ceiling fails from `a = 12` on, and
> fails unboundedly (ratio 114.5 at `a = 24`, growing). The **conclusion** nevertheless holds
> on every row — because the least realizer of a length-`L` word is of size `≈2^L` while
> `R ≤ L`, so the ceiling is satisfied for a reason that has nothing to do with the height
> bound. An unbalanced block could break the ceiling only if it *also* had an anomalously small
> realizer, and **no such case was found — here, or anywhere else in Phase 2**.
>
> So Correction 2 stands as a statement about **what is proved**, not about what was observed:
> off the balanced class the inequality is unproved (with the trivial height bound it is
> vacuous, since `(1−θ)ℓ ≤ log₂m` is empty for `θ ≥ 1`), and M1 must therefore record the
> discrepancy and apply the ceiling only where it is small. The exact isometry `v₂(M) = R`
> holds on every row regardless, balanced or not — it does not depend on the height bound.

## 2.6 The residue laws at the second and third record holders

**L4** says `r₁(N) ≡ 3 or 7 (mod 12)`. It does **not** extend to `r₂` and `r₃`, and the reason is
exactly L4's own proof, which uses minimality. What does extend is this:

> **L4′. PROVED** (from **L1**, `Descent/BackStep.lean`). For `i ≥ 2`, `r_i(N) ≡ 2 (mod 3)` is
> permitted, and whenever it holds, the backward `d = 1` image `(2r_i(N) − 1)/3` is one of
> `r_1(N), …, r_{i−1}(N)`.
>
> *Proof.* L1: if `m ∈ Z_N` and `m ≡ 2 (mod 3)` then `p = (2m−1)/3` is a positive odd integer
> with `p < m` and `p ∈ Z_{N+1} ⊆ Z_N`. So `p` is an `N`-confined positive odd integer strictly
> below `r_i(N)`, and the `N`-confined integers below `r_i(N)` are exactly
> `r_1(N), …, r_{i−1}(N)`. ∎

**VERIFIED** over every `N = 1 … 346` (see §2.2): `r₁ ≡ 2 (mod 3)` in **0** cases, which is L4;
and in **every** case where `r₂` or `r₃` is `≡ 2 (mod 3)`, the backward image is an earlier
`r_j`, with no exception.

Residue census over `N = 1 … 236` (every `r_i ≡ 3 (mod 4)`, forced by `2^{S_1} ≤ 3`):

| | `≡ 3 (mod 12)` | `≡ 7 (mod 12)` | `≡ 11 (mod 12)` |
|---|---|---|---|
| `r₁` | 130 | 106 | **0** — this is L4 |
| `r₂` | 81 | 70 | 80 |
| `r₃` | 85 | 67 | 64 |

The roughly equal thirds at `r₂, r₃` are the arithmetic already noted in
`audits/descent/DESCENT_AUDIT.md` ("the equal thirds are arithmetic, not data"): the classes
`≡ 3 (mod 4)` split evenly mod 12, and only the `11 (mod 12)` third carries a backward chain.
The content is that `r₁` is the one that never does.

## 2.7 `N0` — the random-placement null model for **size**

`scripts/nullmodel.py`, `scripts/delta.py`.

**The exact density.** The odd `m` with a given zero-confined valuation word `d` of total `S`
form exactly one residue class mod `2^{S+1}`, so their density **among odd integers** is `2^{-S}`.
Summing over all zero-confined words of length `N`:
```
p_N(0)  =  Σ_{d confined, |d| = N}  2^{−S(d)}       ( = Occupation.p N 0 )
```
computed here **exactly** by the transfer recursion over `(k, S)`:
```
f[0][0] = 1 ,      f[k+1][S′] = Σ_{d ≥ 1} f[k][S′−d]     for  S′ ≤ A[k] ,
num_N := Σ_S f[N][S]·2^{A[N]−S}  ∈ ℤ ,        p_N(0) = num_N / 2^{A[N]} .
```
No floating point, no asymptotics: `num_N` is an exact integer, and it is *also* the exact count
of odd `m ∈ [1, 2^{A[N]+1})` that are `N`-confined.

> **VERIFIED.** `num_N` equals that count, computed independently by orbit iteration, for
> `N = 1,2,3,4,5,6,8,10,12,14` — e.g. `num_2 = 3` and the 2-confined odd `m < 16` are exactly
> `{7, 11, 15}`; `num_{14} = 168 807`. No mismatch.

**Scales 1 and 2, tested on the exact density.** `Occupation.confined_mass_rate` gives
`−(1/N)log₂p_N(0) → I₀ = α(1 − H₂(1/α)) = 0.0793186…` (**PROVED**, formalized). The *Three
Scales of Confinement* note adds the polynomial factor, `p_N(0) ≍ 2^{−I₀N}·N^{−3/2}`
(**CITED**, paper-proved, not formalized). Testing the second exactly:

| `N` | `log₂(1/p_N)` | `/N` | `log₂(1/p_N) − I₀N − (3/2)log₂N` |
|---|---|---|---|
| 10 | 3.954 | 0.3954 | −1.822 |
| 20 | 5.699 | 0.2849 | −2.371 |
| 50 | 9.556 | 0.1911 | −2.876 |
| 100 | 14.822 | 0.1482 | −3.075 |
| 150 | 19.572 | 0.1305 | −3.169 |
| 200 | 24.127 | 0.1206 | −3.202 |
| 250 | 28.495 | 0.1140 | −3.283 |
| 300 | 32.861 | 0.1095 | −3.277 |

> **An exact-arithmetic confirmation of Scale 2. VERIFIED numerically.** The last column settles
> to **≈ −3.20 … −3.28** across `N = 100 … 300`, against `−(1/N)log₂p_N` still only at `0.110`
> versus `I₀ = 0.0793` at `N = 300`. So in this range the exact density is
> ```
> p_N(0)  ≈  2^{−3.28} · 2^{−I₀N} · N^{−3/2} ,
> ```
> and the `N^{−3/2}` factor accounts for essentially all of the visible correction to the
> exponential rate: with it the residual is flat to about a tenth of a bit per doubling, without
> it the residual grows by ≈ 1.4 bits per doubling. The exponent `−3/2` itself is **CITED**
> (*Three Scales of Confinement*, paper-proved, **not** formalized); what is established here is
> that the exact `p_N(0)`, computed in integer arithmetic with no asymptotics, is consistent
> with it over `N = 100 … 300`. `I₀` is **PROVED** and formalized
> (`Occupation.confined_mass_rate`). This is a numerical confirmation, not a proof of the
> exponent.

**The null.** Under random placement the `N`-confined odd integers are a Poisson process of rate
`λ = p_N(0)/2` per integer, so `r_k(N) ~ Gamma(k, λ)` and
```
Δ_k(N)  :=  log₂ r_k(N) − log₂ k − log₂(1/p_N(0)) ,
E[Δ_k]  =  1 + ψ(k)/ln 2 − log₂ k    →   +0.167 (k=1),  +0.610 (k=2),  +0.746 (k=3).
```

**Two things that would corrupt the test, both handled.**

*The saw-tooth.* `r_k(N)` is a step function of `N` while `log₂(1/p_N)` rises smoothly, so `Δ_k`
jumps at each new record holder and then decays deterministically. Averaging over all `N`
measures the step widths, not the placement. **The order statistic is sampled exactly at the
jumps**, and that is where `N0` is tested.

*Clustering, which breaks the independence the Poisson model assumes.* By **L1**, a confined
`m ≡ 2 (mod 3)` has a **smaller and more-confined** backward `d = 1` image, and by **L2** the
chain from `m` has length exactly `v₃(m+1)`. So confined integers arrive in **chains**, not
independently, and the Poisson expectations `E[Δ₂], E[Δ₃]` assume something false. Two
consequences, both acted on:

* **`Δ₁` at the jump points is the primary Q5 test.** `r₁(N)` is always a chain root (that is
  **L4**), so it is the one order statistic the chains do not displace.
* **A lineage-thinned null.** Restrict the population to **chain roots** — confined `m` with
  `m ≢ 2 (mod 3)`, equivalently `3 ∤ m+1`, equivalently `v₃(m+1) = 0`, equivalently no backward
  `d = 1` step. Their density is exactly
  ```
  q_N(0) = (2/3)·p_N(0) ,
  ```
  **PROVED**: `2^{S+1}` is invertible mod 3, so each residue class mod `2^{S+1}` meets each
  class mod 3 in density `1/3`, and exactly `2/3` of every class consists of roots. The thinned
  test compares the `k`-th smallest confined **root** against Poisson at rate `q_N(0)/2`.

  **VERIFIED** by direct count over a full period mod `3·2^{A[N]+1}`, for `N = 1 … 14`: the
  `N`-confined odd integers number exactly `3·num_N` and the roots among them exactly `2·num_N`,
  with no exception — e.g. at `N = 14`, `num_N = 168 807`, all-confined `506 421 = 3·num_N`,
  roots `337 614 = 2·num_N`.

---

# Phase 3 — measurements M2, M3, M4

`scripts/phase3.py`. Exact arithmetic; divisions appear only in the reported ratios.

## 3.1 M2 — Sturmian proximity

Two quantities per record holder: the integer drift deficit `D_k = A[k] − S_k ≥ 0` (zero
exactly on the critical line), and the longest common prefix of the orbit's **valuation word**
with a **shift** of the critical Sturmian valuation word `d_i = ⌊(i+1)α⌋ − ⌊iα⌋` (shifts
`0 … 2000`).

| `r₁` | depth | `max D_k` | `D` at depth | mean `D` | best lcp | shift | lcp/depth |
|---|---|---|---|---|---|---|---|
| 27 | 36 | 6 | 1 | 2.86 | 3 | 0 | 0.083 |
| 703 | 50 | 6 | 2 | 3.54 | 1 | 0 | 0.020 |
| 10 087 | 65 | 6 | 1 | 2.69 | 1 | 0 | 0.015 |
| 270 271 | 102 | 14 | 0 | 8.31 | 1 | 0 | 0.010 |
| 626 331 | 110 | 11 | 1 | 5.23 | 3 | 0 | 0.027 |
| 1 126 015 | 140 | 14 | 4 | 7.81 | 1 | 0 | 0.007 |
| 13 421 671 | 180 | 15 | 2 | 7.01 | 1 | 0 | 0.006 |
| 26 716 671 | 187 | 15 | 1 | 6.14 | 1 | 0 | 0.005 |
| 56 924 955 | 193 | 15 | 0 | 8.27 | 3 | 0 | 0.016 |
| **63 728 127** | **236** | 12 | 1 | 6.61 | **1** | 0 | **0.004** |

*(control: the Sturmian word's own prefix scores lcp/depth = 1.000 by construction.)*

> **VERIFIED, and it is a clean negative.** Over depths up to 236 the record holders agree with
> the best Sturmian shift for **1 to 3 valuations**. They are not near the critical Sturmian
> word in any prefix sense — no nearer than a generic confined word would be.
>
> The drift tells the other half of the story: `max D_k` runs 6–15 and the mean 2.7–8.3, so the
> orbits wander well away from the critical line, but `D` at the final confined step is **0–4**
> in every case. A record holder ends **drift-critical**, which is why the next step breaks
> confinement — this is the future-minimum / last-maximum structure of `Divergence.LastMaximum`,
> seen from the data side, not a new phenomenon.

## 3.2 M3 — the signed border to the rational points of `K`

By **P1** every zero-confined periodic point of `K` is a negative rational; they were enumerated
exactly:

| period `≤` | points | all negative? | height range |
|---|---|---|---|
| 4 | 9 | ✔ | 1 … 85 |
| 6 | 46 | ✔ | 1 … 1 085 |
| 8 | 296 | ✔ | 1 … 13 349 |
| 10 | **1 717** | ✔ | 1 … 148 813 |

> **P1 VERIFIED on all 1 717 zero-confined periodic points of period ≤ 10. Every one is a
> negative rational, with no exception.**

Border ratio `v₂(m − x_w)/log₂ height(x_w)`, maximised over the 769 points of period ≤ 9:

| target | `log₂m` | best ratio | `v₂` | nearest `x_w` |
|---|---|---|---|---|
| 27 | 4 | 2.153 | 5 | `−5` |
| 703 | 9 | 1.538 | 17 | `−2123/1675` |
| 35 655 | 15 | **2.262** | 14 | `−73/17` |
| 270 271 | 18 | 1.277 | 14 | `−1993/1417` |
| 1 126 015 | 20 | 1.272 | 14 | `−2059/1931` |
| 8 088 063 | 22 | 1.125 | 16 | `−19171/18659` |
| 26 716 671 | 24 | 0.984 | 14 | `−19171/18659` |
| 63 728 127 | 25 | 1.195 | 17 | `−19171/18659` |
| C2 Sturmian `r(D_N)`, `N = 20, 40, 60` | 31, 63, 92 | **4.307** each | 10 | `−5` |
| C1 `−5`, `−17` | 2, 4 | ∞ | ∞ | themselves |

The Sturmian realizers score a constant 4.307 because `1c_β`'s valuation word opens
`1,2,1,2,1,2,…`, agreeing with `(1,2)^∞` — the word of `−5` — for six valuations; that is a
fixed initial coincidence, not a deepening one, and it does not grow with `N`.

## 3.3 M4 — the Markov-type exponent, ranked

`E(x) = max over rationals p/q (q odd) of v₂(x − p/q)/log₂ height(p/q)`, searched over odd
`q ≤ 2049` and every `t ≤ K`; the exact representation `p/q = x` is excluded (it gives `∞`).

| rank | target | `E` | `E`/trivial ceiling |
|---|---|---|---|
| **1** | **the periodic points of `K`** (`−1, −5, −17, …`) | **∞** — each *is* a rational of tiny height | — |
| 2 | 8 088 063 · 26 716 671 · **63 728 127** | 5.678 | 0.38 · 0.35 · 0.34 |
| 3 | 1 126 015 | 4.417 | 0.32 |
| 4 | Sturmian `r(D_{20/40/60})` | 4.307 | 0.30 · 0.15 · 0.11 |
| 5 | 13 421 671 | 3.876 | 0.36 |
| 6 | 703 · 270 271 | 3.786 | 0.57 · 0.31 |
| 7 | 10 087 | 3.445 | 0.52 |
| 8 | 626 331 | 2.850 | 0.37 |
| 9 | 35 655 · 56 924 955 | 2.702 | 0.54 · 0.35 |
| 10 | 27 | 2.524 | 0.72 |

Next-best `E` for the periodic points once they themselves are excluded: `−1 → 1.292`,
`−5 → 2.524`, `−17 → 2.524`. Also `Φ(1c_β) mod 2^{190}` scores 4.307, at `−5`, for the same
initial-coincidence reason as its realizers.

---

# Answers to the pre-registered questions

## Q1 — do the record holders show structure beyond the L4 residue law and the Descent lineage facts that survives C3?

> **No. Every pattern found reduces to something already proved, or to a selection effect.**
> **Classification: explained by known facts.**

The complete list of what was found, and what each reduces to:

| observation | reduces to |
|---|---|
| `r₁ ≡ 3 or 7 (mod 12)` at all 346 values; `r₁` never `≡ 11` | **L4**, proved (`Descent/ResidueLaw.lean`) |
| `v₃(r₁+1) = 0` at every record holder | **L4 read through L2** — the same statement |
| `r₂, r₃` *do* hit `11 (mod 12)`, and when they do the backward image is an earlier `r_j` | **L4′**, proved here from **L1** (§2.6) |
| record holders end drift-critical (`D` at the last confined step is 0–4) | the future-minimum / last-maximum structure, `Divergence.LastMaximum` |
| the orbit wanders far from the critical line mid-run (`max D_k` 6–15) | nothing; it is what confinement permits |
| record holders are `2^{25}` where shuffled surrogates are `2^{370}` | **a selection effect** — minimum over a huge family against one draw (§2.4) |
| the ones-density tends to `β` along the run | forced: confinement *is* `k/ℓ ≥ β` |
| square-poorness relative to size | see Q2 — it is not poorness, and it is not extreme |

Nothing was found that survives C3 once C3 is read correctly, and nothing at all that is not
either a proved lemma of `Descent`/`Divergence` or an artefact of how the record holders are
selected.

## Q2 — is the square-poorness ceiling ever approached? how much slack?

> **Never approached by the record holders, and they are not the extreme case.**
> **Classification: explained by known facts.**

Writing `Q = ℓ·(e − max(1,θ_W))` for the best initial repetition at any step of a run, and
comparing with `log₂|m_k|` at that step (the ceiling says `Q ≤ log₂|m_k| + O(log ℓ)`):

| object | `Q/log₂m_k` | headroom, bits |
|---|---|---|
| shuffled surrogates (C3) | ≈ 0.04 | 285 – 365 |
| random confined words (C3) | ≈ 0.16 | 53 – 237 |
| **record holders** | **0.34 – 0.72** | **9 – 20** |
| critical Sturmian realizers (C2) | 0.53 – 0.73 | 15 – 17 |

So the record holders have **9–20 bits of headroom** and never come within a factor of the
ceiling. They are **squarer** than a random realizer of the same depth, not poorer — but the
Sturmian edge is squarer still, and the ordering
`shuffles < random < record holders ≲ Sturmian` is exactly the ordering of how *structured* the
underlying word is. That is a restatement of the construction, not a discovery.

The ceiling itself was never violated: **0 balanced blocks with negative slack and 0 isometry
failures over several thousand rows** (§2.3). The M1 stop rule did not fire.

## Q3 — do M3/M4 show discrete top levels, or a continuum?

> **One isolated top level, then a continuum. No second or third Markov-like level.**
> **Classification: genuinely new as an observation; explained by known facts as a mechanism.**

The Markov-type exponent `E(x) = max v₂(x − p/q)/log₂height(p/q)` ranks as:

* **level 1, isolated: `E = ∞`.** The rational points of `K` — and by **P1** these are exactly
  the negative rationals of §3.2, 1 717 of them at period `≤ 10`, every one negative. They have
  `E = ∞` because each *is* a rational of small height. Removing the exact representation drops
  them straight into the band (`−1 → 1.29`, `−5 → 2.52`, `−17 → 2.52`).
* **then a band, `E ≈ 2.5 … 5.7`, with no gap.** Record holders (2.52 – 5.68), the Sturmian
  realizers (4.31 each), and `Φ(1c_β) mod 2^{190}` (4.31) are interleaved. The three record
  holders at the top of the band (`8 088 063`, `26 716 671`, `63 728 127`, all at 5.678) reach
  it through the **same** rational, `−3/3 = −1`, at `t = 9` — a shared coincidence, not three
  independent ones.

So the spectrum is: the rational points of `K` (a single discrete level, characterised by P1),
and below them a continuum in which the record holders are not distinguished. **No Markov-like
ladder of intermediate levels was found.**

## Q4 — does the signed border show a trend with `N`?

> **Oscillating, with no trend, and the absolute agreement does not grow at all.**
> **Classification: explained by known facts.**

Best border ratio `v₂(m − x_w)/log₂height(x_w)` over the 769 periodic points of period `≤ 9`,
as `r₁` runs from `27` to `63 728 127` (`log₂m` from 4 to 25):

```
2.15, 1.54, 1.65, 2.26, 1.28, 2.15, 1.27, 1.12, 2.10, 0.98, 2.15, 1.19
```

no monotone component; and the *absolute* agreement `v₂` stays in **5 … 17** across the whole
range while `log₂m` triples. **Record holders do not approach the rational points of `K` as `N`
grows.** The Sturmian realizers behave the same way for a transparent reason: their constant
4.307 comes from `1c_β`'s valuation word opening `1,2,1,2,1,2` — a six-letter coincidence with
the word of `−5` that never deepens.

This is the P1 marker doing its job and finding nothing: the eventually periodic points of `K`
are a classified, negative, small-height family, and the record holders stay a bounded 2-adic
distance from all of them.

---

# Q5 — the record holders against `N0`

## 5.0 Pre-registration, written before any of the fits below were run

The Phase-2 fits used a least-squares line through the jump points and a nominal standard
error. That is not adequate here, for two reasons recorded in §2.7: the confined integers come
in **chains** (L1/L2), so the residuals are serially correlated, and the number of *distinct*
record holders is small. The following is fixed in advance.

1. **The sample is the 24 distinct record holders**, each at its **first-appearance `N`**, not
   the 346 values of `N`. Repeating a record holder across an `N`-range adds no information.
2. **Error bars by block bootstrap** over that series (moving blocks of length 3, 20 000
   resamples), not by the nominal `σ`.
3. **Three models, fixed before fitting:**
   * **B — linear drift:** `Δ(N) = a + b·N`;
   * **A1 — constant plus decaying transient:** `Δ(N) = a + b/N`;
   * **A2 — constant plus exponential transient:** `Δ(N) = a + b·e^{−N/c}`.
   Model **B** is the "persistent drift" hypothesis; **A1** and **A2** are the "the null holds,
   with a transient" hypotheses. They are compared by **AICc**, with the sample size replaced
   by the **effective** sample size `n_eff = n·(1−ρ₁)/(1+ρ₁)` estimated from the lag-1
   autocorrelation of the residuals, and separately by the **block-bootstrap distribution of the
   AICc difference**. A model is called preferred only if `ΔAICc ≥ 2` and the bootstrap puts it
   ahead in at least 80 % of resamples.
4. **Censoring**: a jump point at `N` is visible only if `Δ < log₂(bound) − log₂(1/p_N)`. Points
   failing `threshold ≥ Δ + 3.5` are dropped before fitting, as in §2.7.

## 5.1 What the drift would mean, either way — recorded before the verdict

This is worth fixing in advance, because it bounds how much the answer to Q5 can matter.

The exact density gives `log₂(1/p_N(0)) = I₀N + (3/2)log₂N − 3.28 + o(1)` (§2.7), so
```
log₂ r₁(N)  =  I₀·N + (3/2)·log₂N − 3.28 + Δ₁(N) .
```
* If `Δ₁` is **bounded** (models A1/A2), the growth exponent of `r₁` is exactly `I₀ = 0.0793`.
* If `Δ₁` carries a **persistent linear drift** `b·N` (model B), the exponent becomes `I₀ + b`.

The largest decline anywhere in this data is about `−0.01` bits per step. Taken at face value
and extrapolated forever, that gives an exponent
```
I₀ + b  ≈  0.0793 − 0.01  =  0.069  >  0 ,
```
still exponential growth, and still `r₁(N) → ∞` at a rate `2^{εN}` with `ε ≈ 0.069`. That is
consistent with **Open Problem C** for any `ε > 0`, and it is what the measured fit already
says: §2.2's empirical law `log₂r₁ ≈ 0.0811·N + 10.25` sits slightly *above* `I₀` because of the
`(3/2)log₂N` term, not below it.

> **Nothing in this data suggests the growth rate could reach `0`.** For `r₁(N)` to stop growing
> one would need `b ≤ −I₀ = −0.0793` bits per step, eight times the largest decline observed and
> of the opposite character (a drift that never levels off). The Q5 result below, whichever way
> it goes, does not bear on (DE) or on Open Problem C; it is a statement about how well a
> Poisson null describes the extreme order statistic over the range that can be computed.

