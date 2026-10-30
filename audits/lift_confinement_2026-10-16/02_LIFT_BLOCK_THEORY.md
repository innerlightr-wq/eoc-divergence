# 02_LIFT_BLOCK_THEORY.md

Conventions re-verified against Rev 8: `S_0 = 0`, `S_n = Σ_{j<n}d_j`, `C_0 = 0`,
`C_{n+1} = 3C_n + 2^{S_n}`, `2^{S_n}m_n = 3^n m_0 + C_n`, `r_n = (−C_n3^{−n}) mod 2^{S_n}`,
`r_{n+1} = r_n + b_n2^{S_n}` with `0 ≤ b_n < 2^{d_n}`, `ℓ_n = 1_{b_n≠0}`,
`J(N) = Σ_{n=1}^{N−1} ℓ_n`.

## Theorem L1 — the lift sequence is a base-2 expansion `[PROVED]`

`C_n/3^n = Σ_{j<n} 2^{S_j}3^{−(j+1)}`, so in `ℤ₂` (convergent since `S_j → ∞`)
```
x := lim r_n = − Σ_{j≥0} 3^{−(j+1)} 2^{S_j} ,        b_n = (x >> S_n) mod 2^{d_n} .
```
**The lift sequence is literally the binary expansion of the 2-adic realizer, read in windows
cut by the partial sums `S_n`.**  This makes `J(∞) < ∞ ⟺ x` has finitely many nonzero bits
`⟺ x ∈ ℤ_{≥0}` — Proposition R, recovered as a triviality rather than reproved.

## Theorem L2 — the lift criterion `[PROVED]`

Let `m_n = (3^n r_n + C_n)/2^{S_n}` (an integer by the congruence).  Then
```
3^{n+1} r_n + C_{n+1} = 3(3^n r_n + C_n) + 2^{S_n} = 2^{S_n}(3m_n + 1) ,
```
so `r_{n+1} = r_n ⟺ 2^{S_{n+1}} | 3^{n+1}r_n + C_{n+1} ⟺ 2^{d_n} | 3m_n + 1`.  More precisely
```
b_n ≡ −(3m_n + 1)·3^{−(n+1)}   (mod 2^{d_n}) ,
```
so `v_2(b_n) = v_2(3m_n+1)` when that is `< d_n`, and `b_n = 0` otherwise.

> ### Reading
> **A nonzero lift occurs exactly where the word demands a deeper 2-adic valuation than the
> current prefix-realizer's own orbit supplies.**  `J(N)` counts the word's "valuation
> overdrafts" against its running least realizer.

**Verified on 7 100 positions** across random words (`N = 12, 16`) and genuine orbits
`m₀ = 7, 27, 703, 159487, 270271`, 0 failures, both the equivalence and the congruence
(`results/run_theory.txt`).

## Theorem L3′ — parity control `[PROVED]`  *(replaces a false L3, see below)*

```
(i)  m_n even          ⟹ v_2(3m_n+1) = 0 < d_n ⟹ b_n ≠ 0  for every d_n ≥ 1 ;
(ii) m_n odd, d_n = 1  ⟹ v_2(3m_n+1) ≥ 1 = d_n ⟹ b_n = 0 .
```
So `ℓ_n = [m_n even] ∨ [m_n odd ∧ v_2(3m_n+1) < d_n]`.
**Verified on 18 010 positions, 0 failures** (`results/run_fix.txt`).

### Retraction of L3

I first asserted: *"`r_n` is the least residue, so `2^{S_n}` exactly divides `3^n r_n + C_n`,
hence `m_n` is odd"*, and deduced `d_n = 1 ⟹ b_n = 0` unconditionally, and from that a bound
`J(N) ≤ S_N − N`.

**All three are false.**  Being least modulo `2^{S_n}` says nothing about divisibility by
`2^{S_n+1}`.  Measured: `m_n` is even at **4 914 of 8 480** positions, and
`d_n = 1 ∧ b_n ≠ 0` occurs **2 063** times.  Minimal counterexample found by exhaustive search:
`d = [1]`, `n = 0`, `r_0 = 0`, `m_0 = 0` (even), `b_0 = 1 ≠ 0`.
**The bound `J(N) ≤ S_N − N` is withdrawn.**

## Which information is where (the brief's A–D)

* **A — already in the exponent word:** `S_n`, `C_n`, `T_n`, and hence `r_n`, `m_n`, `b_n`.
  `b_n` is a **deterministic function of `(d_0,…,d_n)`** and does not depend on the future at
  all.  This single fact disposes of several apparent effects (§04).
* **B — produced by modular reduction:** the least-residue choice, which is what makes `m_n`'s
  parity non-trivial (L3′).
* **C — useful only under confinement:** nothing found.  §04 shows the confinement slack has no
  effect after control.
* **D — genuine constraints excluding positive-integer realization:** none found; §08 explains
  why the class of statements available here cannot contain one.
