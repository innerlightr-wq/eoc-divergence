# 02_TEMPORAL_MODEL.md

## Conventions (Rev 8 Lemma 2.4, re-verified)

Word `d = (d_0,…,d_{N−1})`, `d_j ≥ 1`.  `S_0 = 0`, `S_j = Σ_{i<j} d_i`, so `S_N` is the total.
```
C_N = Σ_{j=0}^{N−1} 3^{N−1−j} 2^{S_j} ,    C_0 = 0 ,    C_{n+1} = 3C_n + 2^{S_n} ,
2^{S_N} m_N = 3^N m_0 + C_N ,              r_N = (−C_N 3^{−N}) mod 2^{S_N} ∈ [0, 2^{S_N}) .
```
Two independent implementations of `C_N` (closed form and recurrence) agree on all words tested,
and the identity holds on genuine orbits `m₀ = 7, 27, 703, 159487` to `N = 25`
(`results/run_derive.txt`, P0).

## The three sources of structure, separated as the brief asks

* **(A) exponential weighting by `3^{N−1−j}`** — a fixed geometric weight, independent of the word;
* **(B) accumulated `2^{S_j}`** — the only place the word enters, and it enters **multiplicatively**;
* **(C) modular reduction and least-residue selection** — this is where representative choice
  matters, and it is the one genuine trap (§3 below).

**Which nonlinearity is genuine.**  The map `d ↦ C_N` is nonlinear in `d`, but only through
`2^{S_j}`, i.e. through the single identity `2^{a+b} = 2^a 2^b`.
`04_NONLINEAR_INTERACTIONS.md` shows this makes every higher difference multiplicatively
separable, so the nonlinearity is **real but structureless**: it is exponentiation, not coupling.

## Temporal differentiation variables

* first differing position `i`, relative position `τ = i/N`;
* **tail carry** `T_i = Σ_{j>i} 3^{N−1−j} 2^{S_j}` — the carry mass strictly after `i`;
* **window carry** `W_{i,k} = Σ_{j=i+1}^{k} 3^{N−1−j} 2^{S_j}`;
* the **available window** `w = S_N − S_{i+1}`, the number of bits in which two matched
  realizers can differ.

## §3  Normalisation — the matched comparison, and the representative trap

**Bumping a single `d_i` changes `S_N`.**  The two realizers then live in different moduli and
their difference is not an intrinsic invariant — exactly the brief's warning.  The comparison
with a common modulus is the **`S_N`-preserving swap**
```
d_i → d_i + 1 ,   d_k → d_k − 1   (k > i, d_k ≥ 2) ,
```
under which only `S_j` for `i < j ≤ k` change, each by `+1`.

Even then, `Δr_N := r(d′) − r(d)` is defined only modulo `2^{S_N}`.  Its valuation is
well defined (being `< S_N`), but its **odd part is not**: for `d = [2,1,3,1,2,2,1,3]`,
`i = 1`, `k = 5`, `Δr_N = 5032` gives `oddpart = 629`, while the equally valid representative
`Δr_N − 2^{S_N}` gives `−3467` (`results/run_odd.txt`, P4).  The intrinsic object is therefore
```
u := (Δr_N / 2^{S_{i+1}})  mod  2^{S_N − S_{i+1}} ,     an odd residue,
```
and every statement below is made about `u`, never about a chosen integer odd part.
