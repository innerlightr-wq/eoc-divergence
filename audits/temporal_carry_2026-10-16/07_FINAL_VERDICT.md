# 07_FINAL_VERDICT.md

## Verdict: **D — existing structure fully explains the effect**, with **E** for the tip hypothesis

The observed temporal differentiation follows from the carry formula alone.  The specific
late-stage ("terminal tip") hypothesis is **disproved** under normalization.

## The two primary questions, answered

**Q1. Does the temporal position of a parity/exponent difference produce arithmetic information
about realizers beyond the 2-adic valuation of their difference?**

**No.**  For the only comparison with a common modulus — the `S_N`-preserving swap — the entire
difference has an exact closed form:
```
Δ r_N ≡ −2^{S_{i+1}} V_{i,k} 3^{−N} (mod 2^{S_N}) ,   V_{i,k} = Σ_{j=i+1}^{k} 3^{N−1−j} 2^{S_j−S_{i+1}} ,
```
verified on **36 712 swaps with 0 failures**.  Once `v_2 = S_{i+1}` is removed, what remains is
not a residual carrying new information — it is an explicit function of the word.  **Temporal
position enters only as the index range of a sum.**

**Q2. Can it constrain positive-integer realizability in the zero-confined sector?**

**No, and not for want of sharpness.**  `r_N` is itself a nonnegative integer realizing the
prefix, so **every finite word is realized**.  Any prefix-local invariant — and temporal
differentiation is prefix-local by construction — takes the same value on realizable and
unrealizable infinite words sharing that prefix.

## The terminal-tip hypothesis: disproved, with the mechanism identified

Exact enumeration of **all 154 518 words** with `N = 11`, `S_N = 22` (both controls fixed by
construction):

* the **absolute** information determined at position `i` is **exactly flat at 2.0000 bits**
  across all `τ = i/N` — it is `E[d_{i+1}] = S_N/N`, the mean digit;
* the **relative** fraction rises `0.10 → 1.00` **solely** because the available window
  `w = S_N − S_{i+1}` shrinks linearly to zero;
* the number of eligible swaps **decreases** monotonically with `i` (`0.1818 → 0.0182`).

> **The terminal effect is the denominator, not the numerator.**  Late differences look
> informative because there is less left to say, not because more is being said.

This answers the brief's §10 falsification list affirmatively on every item that applies: the
effect follows automatically from the carry formula; it disappears after normalizing by window
size; it is unchanged after conditioning on `N` and `S_N`; and it is independent of
positive-integer realizability.

## The nonlinearity: real, but structureless

```
Δ_i Δ_k C_N = (2^{ε_i} − 1)(2^{ε_k} − 1) · T_k ,     equivalently    Δ_i Δ_k C_N = Δ_i C_N · Δ_k C_N / T_i .
```
Verified on 66 600 and 7 200 cases respectively, 0 failures.  The interaction between temporal
positions is **nonzero but multiplicatively separable** — it is the identity `2^{a+b} = 2^a 2^b`
and nothing more.  The second difference is a function of the two first differences.  **The
hypothesis anticipated irreducible coupling; the coupling is exactly reducible.**

## What is new

Honestly: **two closed forms, no theorem.**

* **Lemma T+** (`u ≡ −V_{i,k} 3^{−N}` exactly) and its first block **Lemma T**
  (`u ≡ −3^{−(i+2)} mod 2^{d_{i+1}}`) are correct, exactly verified, and — so far as I can tell —
  not written down before in this programme.  But both follow in two or three lines from
  `C_N = Σ 3^{N−1−j} 2^{S_j}`, which by the brief's own §9 standard disqualifies them as new
  theorems.
* The **separability identity** `Δ_iΔ_k C = Δ_iC·Δ_kC/T_i` is the most useful thing here, because
  it closes the "nonlinear interaction" axis prospectively rather than case by case.
* The **prefix-locality obstruction** (`06_...` §2) is a clean general statement of why this
  whole class of approaches cannot work, reached from a new direction but agreeing with the
  closed-routes index.

Lemma T+ does **not** contradict the October 14 Theorem D: that theorem concerns **free**
suffixes, where the odd part genuinely is undetermined (confirmed here — it spreads over all odd
classes mod 8).  Lemma T+ buys determination only by removing the freedom that made the problem
hard.

## Classification

| result | class |
|---|---|
| `Δ_i C_N = (2^ε−1)T_i` | **PROVED**, already implied by the carry formula |
| `Δ_iΔ_k C_N = (2^{ε_i}−1)(2^{ε_k}−1)T_k` and separability | **PROVED**, already implied |
| `v_2(W_{i,k}) = S_{i+1}` | **PROVED**, the Theorem D datum in swap coordinates |
| Lemma T, Lemma T+ | **PROVED** but **ALREADY KNOWN in substance** (immediate from the carry formula) |
| terminal-tip hypothesis | **DISPROVED** (E) |
| "residual odd component carries extra information" | **DISPROVED** for the matched comparison |
| any constraint on positive-integer realizability | **UNRESOLVED**, and shown structurally out of reach of prefix-local methods |
| `(DE)`, `(PosPC)`, Sharp EOC, Open Problem C | **UNRESOLVED**, unchanged |

## Recommended next steps

1. **Stop testing prefix-local statistics.**  `06_...` §2 gives the general reason none can work:
   every confined prefix extends both to a realizable and (by the word-shadow cardinality
   barrier) to unrealizable words.  This deserves to be added to the closed-routes index as a
   *prospective* criterion, so the next candidate is tested against it in one line rather than
   by another experiment suite.
2. **The count, not the size.**  `#{n : r_{n+1} ≠ r_n}` — the number of nonzero lift digits —
   remains the one quantity flagged in the October 16 package for which Lemma O does not apply,
   because it is a count rather than a magnitude.  It is also not prefix-local.  That is the only
   direction here I would expect to behave differently.
3. **Formalize the separability identity** in Lean alongside the aggregate identity.  It is a
   `ring`-level statement, it closes an axis prospectively, and it is the only item here certain
   to complete.

## Operational compliance

No repository modified; nothing committed, pushed, published or uploaded.  All work in this
scratch directory.  **No Lean build was run and no Lean verification is claimed.**  No Collatz
proof is asserted from numerical patterns.  One of my own printed conclusions was contradicted
by its own data, independently re-checked, and retracted — recorded in `03_EXACT_COMPUTATIONS.md`.
