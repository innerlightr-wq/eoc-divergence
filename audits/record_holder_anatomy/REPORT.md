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

## Phase 2 onward — not started

No computation has been run. Phase 2 (record-holder data: `r₁, r₂, r₃` by an exact pruned search
over zero-confined residue classes, with residue mod 12, `v₃(m+1)`, lineage and gaps) and Phase 3
(M1–M4 with controls C1–C4) await approval.

### M1's ceiling: the derivation the brief asks for, done now — and two corrections

The brief pre-registers a square-poorness ceiling `≈ 2.41·log₂m_k` and says any violation "is a
bug or a counterexample to the derivation". Both halves need fixing before a single measurement
is taken.

**The derivation. PROVED.** Let the parity word of `m` have a prefix `u u` with `|u| = ℓ`, `k`
ones, and let `m` be the integer realizing it, so `Φ` of the word is `m` and the height is
`H = m`. Suppose `u` is **balanced**. Then, exactly as in the paper's Liouville step with the
balanced height bound of Remark 4.3,
```
2^{2ℓ} ≤ |M| ≤ m·(1+3ℓ)·max(2^ℓ, 3^k) ,
```
and with `θ := (k/ℓ)·log₂3`, `max(2^ℓ,3^k) ≤ 2^{max(1,θ)·ℓ + log₂3}`, giving

> **`(2 − max(1,θ))·ℓ ≤ log₂ m + log₂(1+3ℓ) + log₂3`.**

**Correction 1 — the constant is per block, and it is `1`, not `2.41`, in the regime that
matters.** Write `θ_W = (k/ℓ)·log₂3` for the block `W` of the square actually found, so the
ceiling reads `ℓ ≤ (log₂m_k + O(log ℓ))/(2 − θ_W)`. For a
*zero-confined* prefix, `2^{S_k} ≤ 3^k` says exactly `k/ℓ ≥ β`, hence
```
θ = (k/ℓ)·log₂3 ≥ β·log₂3 = 1 ,
```
so `max(1,θ) = θ` and the ceiling is `ℓ ≤ (log₂m + O(log ℓ))/(2 − θ)`. The brief's `2.41` is
`1/(2 − log₂3) = 2.4094…`, which is the value at `θ → log₂3`, i.e. at ones-density `→ 1`.
Zero-confinement pushes the *other* way: record holders sit just above density `β`, so `θ ≈ 1`
and the correct ceiling is
```
ℓ ≲ log₂ m_k + O(log log m_k) ,
```
a factor `2.41` tighter than pre-registered. Using `2.41` would report spurious slack, and the
slack is precisely what M1 and Q2 are supposed to measure. **The constant must be computed per
prefix from its own `θ`, not fixed in advance.**

**Correction 2 — there is no ceiling at all without balance.** The bound above uses
`c_u ≤ 3ℓ·max(2^ℓ,3^k)`, which holds for balanced `u` and **fails unboundedly otherwise**
(`audits/sturmian_irrationality/REPORT.md` §1.3: for `u = 0^a1^a`, `c_u = 2^a(3^a−2^a) ≈ 2^{1.29ℓ}`
against `max(2^ℓ,3^k) = 2^ℓ`). With only the trivial bound `c_u ≤ ℓ·3^k·2^{ℓ−1}` the inequality
becomes `(1 − θ)ℓ ≤ log₂m + O(log ℓ)`, and since `θ ≥ 1` on zero-confined prefixes the left side
is `≤ 0`: **vacuous**. So a "violation" of the ceiling is *not* prima facie a bug or a
counterexample — the first thing to check is whether the repeated block is balanced. M1 must
therefore record, for every square it finds, the block's **discrepancy**
`max_j |k_j(u) − j·k/ℓ|` alongside the exponent, and the ceiling must be applied only where that
discrepancy is bounded.

Both corrections are pre-registered here, before any data.

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

## 2.1 Cross-check against the published `N ≤ 200` table

**VERIFIED. PASS — all 200 values agree** with the record-holder table of
`audits/descent/DESCENT_AUDIT.md`, recomputed from scratch by the new method.

**One immediate correction, from the same `10⁸` range.** The published table stops at `N = 200`
because *the scan* stopped there, not because the number did: `r₁ = 63728127` has confinement
depth **236**, so it is `r₁(N)` for **`N = 194 … 236`**, not merely `194 … 200`.

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

> **The single sharpest number in Phase 2.** A permutation of a record holder's own valuation
> word — preserving density and total drift exactly — has a least realizer around `2^{370}`
> where the record holder itself is `2^{25}`. The spread across draws is at most **5 bits**, so
> the surrogates are not a distribution with the record holder in its tail; they sit at the
> class modulus, which is where a generic word's least realizer sits. **Whatever makes a record
> holder small is destroyed by re-ordering its valuations, and is therefore not a property of
> the density or of the drift endpoint.**

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

