# Irrationality of the 2-adic Sturmian carry constant

*Draft, 23 September 2026. The literature check (Phase 3 of the audit) is **complete**: no prior
proof was found across OpenAlex, Google Scholar and zbMATH. Novelty statement, as approved:*

> *No prior proof is known; the question is stated as open in López–Stoll (2009) and treated as
> open in López–Stoll (2021).*

*This is a "no prior proof found" verdict across three indexes, not a proof of priority; journal
literature off arXiv is narrowed by the zbMATH and Scholar passes but not formally exhausted. The
wording above says exactly that, and should not be strengthened.*

## Statement

Let `α = log₂3`, let `c_α` be the characteristic Sturmian valuation word of slope `α` — the word
with partial sums `s_j = ⌊jα⌋` — and let

```
Ξ_α  =  Σ_{j≥0} 3^{−(j+1)} 2^{s_j(c_α)}  ∈  ℤ₂ .
```

> **Theorem.** `Ξ_α ∉ ℚ`.

Equivalently `Ξ_{α,0} = −Ξ_α ∉ ℚ`, where `Ξ_{α,β} = −⅓ Σ_{i≥0} 3^{−i}2^{⌊iα+β⌋}` is the 2-adic
Hecke–Mahler value of [B]. This settles [B]'s Open Problem 1 at intercept `β = 0`; other
intercepts are open.

## Background

For the accelerated map `T(m) = (3m+1)/2^{v₂(3m+1)}` on odd integers, an orbit emits a valuation
word `D = (d_0, …, d_{N−1})`, `d_i = v₂(3m_i+1) ≥ 1`, with partial sums `s_j` and carry
`C_N(D) = Σ_{i<N} 3^{N−1−i}2^{s_i}`. By Terras–Everett the odd `m` with a given prefix form one
residue class mod `2^{s_N+1}`, so an infinite word determines a single 2-adic integer — for the
mechanical word of slope `α`, the constant above.

For a finite block `X` with `|X| = q`, `S(X) = S`, write `δ_X = 3^q − 2^S` (odd) and
`Q(X) = −C(X)/δ_X`. Summing the 2-adic geometric series over periods gives the **periodic-carry
identity** `Ξ(X^∞) = C(X)/δ_X = −Q(X)` [A, Thm 4.2].

Let `(q_n, p_n)` be the convergents of `α` and `X_n` the lower Christoffel block of the shell,
`|X_n| = q_n`, `S(X_n) = p_n`, `C_n = C(X_n)`, `δ_n = 3^{q_n} − 2^{p_n}`,
`x_n = −C_n δ_n^{−1} = Q_n`. Call the shell **upper** if `R_n = p_n − q_nα > 0` and **lower**
if `R_n < 0`; the signs alternate, and `R_0 = 1 − α < 0`.

## The input: an exact valuation law

> **Proposition** [A, Thm 7.1]. For `n ≥ 2`,
> ```
> v₂(x_n + Ξ_α)  =  p_n − 1                (upper),
> v₂(x_n + Ξ_α)  =  p_n + p_{n+1} − 1      (lower).
> ```

The proof compares the floor sequences of the rational rotation `θ_n = (p_n−q_n)/q_n` and the
irrational `θ = α−1`, locating the first partial-sum disagreement at `j* = q_n` (upper) and
`j* = q_n + q_{n+1}` (lower), then applies ultrametric dominance: the first disagreement has
2-adic valuation `min` of the two depths, and later terms are strictly deeper because all letters
are `≥ 1`. It uses only `gcd(p_n−q_n, q_n) = 1`, `q_n ≥ 2`, `q_{n+1} > q_n`, and the classical
estimates `1/(q_n+q_{n+1}) < |R_n| < 1/q_{n+1}`, `q_{n+1}|R_n| + q_n|R_{n+1}| = 1`.

**The asymmetry is the whole point.** `c_α` is the limit of *lower* mechanical words, so a
lower-convergent periodic extension agrees with it for one further continued-fraction level, and
the approximation depth jumps from `≈ p_n` to `≈ p_n + p_{n+1}`.

## Proof of the Theorem

Suppose `Ξ_α ∈ ℚ`. Since `Ξ_α ∈ ℤ₂`, write `Ξ_α = u/v` in lowest terms with `v` odd; set
`H = max(|u|, v)`. For `n ≥ 2` put

```
M_n  :=  u·δ_n − v·C_n  ∈ ℤ ,        so    x_n + Ξ_α  =  M_n /(v δ_n).
```

*`M_n` is a nonzero integer.* Both `v` and `δ_n` are odd, so `v₂(M_n) = v₂(x_n + Ξ_α)`, which the
Proposition makes **finite**; hence `x_n + Ξ_α ≠ 0` and `M_n ≠ 0`.

*Archimedean size.* `|δ_n| < 3^{q_n}` in both cases, using `|R_n| < 1`. For the carry,
`s_j(X_n) = ⌊j p_n/q_n⌋ ≤ j·p_n/q_n` and `p_n/q_n = α + R_n/q_n`, so
`2^{s_j} ≤ 3^{j}2^{|R_n|} < 2·3^{j}` for `0 ≤ j ≤ q_n`, whence `C_n < 2q_n3^{q_n−1}`. Therefore

```
0 < |M_n| < (|u| + v q_n)·3^{q_n} ≤ 2H q_n · 3^{q_n} .
```

*Contradiction.* Let `n ≥ 2` be a **lower** convergent. A nonzero integer satisfies
`|M_n| ≥ 2^{v₂(M_n)}`, so `2^{p_n+p_{n+1}−1} < 2Hq_n3^{q_n}`. Taking `log₂` and using
`q_nα = p_n + |R_n|`,

```
p_n + p_{n+1} − 1  <  log₂(2Hq_n) + p_n + |R_n| ,     hence     p_{n+1} < 2 + log₂(2H) + log₂ q_n .
```

But `p_{n+1} > q_{n+1} > q_n`, so this fails once `q_n` exceeds an explicit bound depending only
on `H`. There are infinitely many lower convergents and `q_n → ∞`. ∎

*Upper convergents contribute nothing:* there the same chain reads `0 < 1 + |R_n| + log₂(2Hq_n)`.

**Effectivity.** The contradiction appears at the first lower convergent with
`q_n ≳ 2log₂(2H)` — continued-fraction depth `O(log log H)`. **No property of the continued
fraction of `log₂3` is used beyond `q_n → ∞`**: no irrationality measure for `α`, no bound on its
partial quotients.

## Verification

The valuation law was checked exactly (integer and 2-adic arithmetic only, no floating point) at
every shell `n = 2…12`, i.e. through `(q,p) = (111202, 176251)`, modulus `2^{480000}`: eleven
exact matches, upper and lower. Independently, the argument was confirmed **not** to fire on
rational points: for the periodic value `x_2 = −5` (the word `(1,2)^∞`), `v₂(x_n + 5)` freezes at
`10 = p_2 + p_3 − 1` from `n = 4` onward, and likewise at `83` and `568` for the shells
`(12,19)` and `(53,84)` — bounded depth against linearly growing height, so no contradiction is
produced, exactly as it must not be.

The finite shadow of the theorem: level `n = 12` alone shows `Ξ_α` is **not a rational of height
`≤ 2^{301975}`**.

## Consequence, and what it does not touch

By [B, Remark 11.1], if `Ξ_{α,β} = p/q` in lowest terms with `q` odd then `n_j = q·T^j(Ξ_{α,β})`
is an integer orbit of the generalized map `n ↦ (3n+q)/2^{v₂(3n+q)}` realizing the mechanical
word; rationality is *equivalent* to such an orbit. [B, Cor 5.6] settled `q = 1`. Hence:

> **No generalized `3x+q` system, for any odd `q ≥ 1`, has an integer orbit whose valuation word
> is exactly the characteristic mechanical word of slope `log₂3`.**

**This has no bearing on divergence exclusion (DE).** Mechanical words have drift confined to a
window of width one, `R_j ∈ (β−1, β]`; the zero-confined seeds that (DE) is about have
`ρ_n = 2^{S_n}/3^n → 0`, i.e. `R_n → −∞`. The Sturmian edge is the *bounded*-drift extreme and was
already closed for positive integers, unconditionally, by [B, Cor 5.6]. The present theorem
strengthens the exclusion from `ℤ` to `ℚ` on that edge; it says nothing about the divergent
regime, and nothing about the sub-line, high-complexity words where the realizer minimizers
actually live.

## References

[A] E. De Jesús, *The 2-Adic Sturmian Carry Constant in the Collatz Carry Equation*, 5 June 2026.
[B] E. De Jesús, *The Sturmian–Mahler Edge of the Accelerated Collatz Realizer Problem*, June 2026.
[LS09] J. López and P. Stoll, *The 3x+1 conjugacy map over a Sturmian word*, Integers **9** (2009),
#A13, 141–162. `doi:10.1515/integ.2009.014` — the 2-adic series and continued fraction for
`Φ(1c_α)`, and irrationality of the **real** values off the critical slope; the 2-adic question is
left open.
[LS21] J. López and P. Stoll, *The 3x+1 periodicity conjecture in ℝ*, `arXiv:2101.12747` (2021) —
aperiodicity for ones-density strictly above `ln2/ln3`; the critical density is treated as open.

*Note (A) is cited here for its Theorem 7.1. Per the September 2026 citation revision, the
approximants and the approximation depths that theorem recovers originate in [LS09]; (A)'s own
contribution is the separated, exact, shell-by-shell form (`p_n − 1` upper, `p_n + p_{n+1} − 1`
lower). **Indexing:** this draft numbers the shells from `0` (`R_0 = 1 − α < 0`), so the range
`n ≥ 2` used above is the right one here; the same restriction reads `n ≥ 3` in (A)'s own
numbering, where `(q_1,p_1) = (1,1)`. Both name the same first shell, `(2,3)`.*
