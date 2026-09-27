# Arithmetic lemma attempt

## The exact decomposition (DERIVED HERE, COMPUTATIONALLY VERIFIED)

With `X = 2^B`, `M = X−1`, `q_w = 2^{S_w+1}`, `r_w` the least **exact** realizer (odd):

- `q_w ≤ X` ⟹ `|C(w) ∩ [1,M]| = X/q_w` **exactly**. (Proof: the count is
  `⌊(X−1−r_w)/q_w⌋+1`; `r_w` is odd and `q_w` even so `r_w ≤ q_w−1`, giving exactly `X/q_w`.
  The oddness of `r_w` is what makes this exact and is the role of the `+1` in the modulus.)
- `q_w > X` ⟹ `|C(w) ∩ [1,M]| = 1_{r_w < X}`.

Since `(X/2)p_N = Σ_w X/q_w`, subtracting gives
```
A_{N,M} − (X/2) p_N  =  Σ_{w : q_w > X} ( 1_{r_w < X} − X/q_w ).                      (★)
```
Writing `d = S_w+1−B ≥ 1` and `T_w = ⌊r_w/2^B⌋ ∈ [0,2^d)` (so `r_w < X ⟺ T_w = 0`) and grouping
by shell `s = S_w` (on which `d` is constant):
```
A_{N,M} − (X/2) p_N  =  Σ_{s ≥ B} ( #{w ∈ shell(s) : T_w = 0} − #shell(s)·2^{−d} )  =  Σ_{s≥B} D_s.   (★★)
```
**Verified exactly** (Fractions, no floats) at all five `(B,N)` pairs of the ladder: both forms of
(★) and (★★) equal `A − (X/2)p_N` with 0 failures, and every per-word contribution matched the
claimed `X/q_w` or `1_{r_w<X}` (assertions in `scripts/phaseC_decomp.py`). `repro/phaseC.out`.

## The exponent budget — why the needed saving is exactly `2^{−d}`

With `h := α H₂(1/α) = 1.505643888` and the repository identity **`h + I₀ = α`** (verified to
`1e−12`):

- `P := (X/2)p_N ~ 2^{B(1−I₀κ)}` (up to `poly`, using `p_N ≍ N^{−3/2}2^{−I₀N}`);
- `T := Σ_{s≥B} #shell(s) ≤ #W_N ~ 2^{hκB}`;
- `d ≈ (ακ−1)B`.

Then `log₂(T/P) = hκB − B(1−I₀κ) = B(κ(h+I₀) − 1) = B(ακ − 1) = d`. That is an **exact identity,
not an estimate**: the trivial bound `|Σ D_s| ≤ T` overshoots `P` by precisely `2^d`. Hence

> **The target requires a relative-discrepancy saving of exactly `2^{−d}` (times `poly(B)`).**

This is precisely the power saving named in `ShellWeyl.weylBound_of_pointwise`
("a power saving `2^{-n}` over the trivial bound"). The Lean interface already asks for the right
strength; nothing weaker in the same shape can work.

## Two candidate mechanisms

**Direction 1 (chosen): cutoff-sensitive lift arithmetic with signed discrepancy retained.**
`ShellWeyl.topBlock_eq_suffix` (LEAN VERIFIED) gives, for `j ≤ N`,
`⌊r_N/2^{S_j+1}⌋ = Σ_{j≤i<N} 2^{S_i−S_j} τ_i` with lift digits `τ_i ∈ {0,1}`. Taking
`j = j(w) := min{j : S_j+1 ≥ B}` makes the top block **suffix-determined**: its bits sit only at
the positions `S_i − S_{j}` of the word's own valuation grid.

**Direction 2 (alternative, not pursued): the `ArithmeticFrontier` interface**, with the digit
conditions on `2^{−a} mod 3^b` and the deterministic `λ=1` environment. Not pursued because the
bridge to (★★) is not derived: `ArithmeticFrontier` constrains `3^b`-adic digits of powers of 2,
whereas (★★) needs `2`-adic top blocks of realizers. **I did not derive a bridge and do not
assume one.**

## The lemma

> **Lemma C1 (shell-level square-root cancellation).** There is an absolute constant `K` such that
> for every `B`, every `N`, and every zero-confined shell `s ≥ B`,
> ```
> | #{w ∈ shell(s) : T_w = 0} − #shell(s)·2^{−(s+1−B)} |  ≤  K · (s+1) · #shell(s)^{1/2}.
> ```

**How it would deliver the target (DERIVED HERE).** Substituting into (★★),
`|Σ_{s≥B} D_s| ≤ K(s_max+1)^2 max_s #shell(s)^{1/2} ≤ poly(B)·2^{hκB/2}`, so
`|Q − 1| ≤ poly(B)·2^{hκB/2 − B(1−I₀κ)}`, which tends to 0 — giving `(T_κ,0)`, i.e. `η = 0` and
the **full** gain `I₀(κ−1/α)` — provided

> `hκ/2 < 1 − I₀κ`  ⟺  `κ < 1/(α − h/2) = 1.201720`.

Verified numerically: at `κ = 0.65`, `hκ/2 = 0.48933` against `ακ−1 = 0.03023`, so the
requirement is met with a margin of `0.459` in the exponent — square-root cancellation is far
more than enough. It remains sufficient up to `κ = 1.2017` and fails from `κ = 1.5` on.

**Circularity check (required by the brief).** *Lemma C1 is NOT a proof ingredient — it is the
target in Fourier-free notation.* `#{T_w = 0}` is exactly the below-cutoff realizer count, so C1
is an equidistribution hypothesis about realizer placement, which is what `(T_κ,η)` asks for. It
is *weaker* than `WeylBound` with constant `C` (which demands
`Σ_{g≠0}‖shellWeyl g‖ ≤ (C−1)#shell`, i.e. `2^d ≲ √#shell` under a square-root heuristic — amply
true at `κ=0.65` where `2^{0.0302B} ≪ 2^{0.4893B}`), and it is **stated in signed form**, so it
avoids the A4 loss. But it is a hypothesis of the same kind, not a step toward one.
**I therefore claim no progress on proving it**, and record that wrapping it would be exactly the
"wrapper around the final counting hypothesis" the brief forbids counting as progress.

## Proof attempt, and the precise obstruction

**What is unconditionally proved here.** (★) and (★★) (exact, verified); the exactness of the
complete-cylinder contribution and the role of terminal parity; the identity
`log₂(T/P) = d` from `h + I₀ = α`; `K ≥ 1` on every confined word; and the independent failure-offset
formula of A1.

**Where the proof of C1 stops.** By `topBlock_eq_suffix`, `T_w` is determined by the suffix lift
digits `τ_i` at grid positions `S_i`. Two facts block the obvious routes:

1. *The support is word-dependent.* `T_w`'s bits live only at positions `{S_i − B}` of `w`'s own
   grid, and distinct words in a shell have distinct grids. So `T_w` is not a sum of independent
   digits over a fixed index set, and no CRT or product structure applies. A2's A3 analysis makes
   the same point one level down: independence needs a complete **joint**-modulus period, which a
   height-truncated cylinder never supplies.
2. *The lift digits are not free.* `τ_i` is determined by `w` through the carry recursion
   `C_{k+1} = 3C_k + 2^{S_k}`, so `w ↦ (τ_i)` is a deterministic injection, not a random vector.
   Assuming otherwise would be exactly the "assume randomness/mixing of the deterministic
   arithmetic environment" the brief forbids.

**Adversarial checks run.** The singleton shell `s = N` (word `1^N`, `r_w = 2^{N+1}−1`) is the
extreme adversarial case: `#shell = 1`, `T_w = 2^{d}−1 ≠ 0`, so `D_s = −2^{−d}` and C1 holds
trivially with `K ≥ 1` — it is *not* a counterexample to C1, only to `WeylBound`'s
absolute-value form. Measured shell discrepancies at `B=24, N=16`: `D_24 = +530.0` on 108,950
words (`D/√# = +1.61`), `D_25 = −318.5` on 108,950 (`D/√# = −0.96`); total `+211.5` against
`P = 259,343.5`. Both are of square-root size and of **opposite sign**, i.e. there is genuine
signed cancellation between shells that an absolute-value bound would discard. Realizer top-block
positions showed no shell with `|z| > 3` against the uniform null across `N = 12,16,20` (from the
hardened `shell_discrepancy.py`).

**Net quantitative gain achieved: zero.** No unconditional improvement on `η` was proved. What
was established is the exact shape of the remaining obligation and the exact size of the saving
it must produce.
