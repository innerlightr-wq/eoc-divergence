# Open problems left by this round

Status legend as in [`FINDINGS.md`](FINDINGS.md). Nothing here is claimed as proved.

## Notation

Fixed exactly as in the scripts ([`scripts/`](scripts/)):

- `alpha = log2 3`; `A[N] = floor(N·alpha)`, computed as `(3**N).bit_length() - 1`
  (`Occupation.sN` in this repository);
- `W_0(N)` = the `0`-confined positive valuation words of length `N` with terminal sum exactly
  `S = A[N]` — the *terminal shell*. `0`-confined means `2^{s_j} ≤ 3^j` for every `j ≤ N`
  (`Descent.ConfinedUpTo` / `Occupation.Confined 0`);
- `M_N = |W_0(N)|`;
- `Q = 2^{A[N]+1}`;
- `r(D)` = the least realizer of `D`: the unique residue `< Q` with
  `3^N·r + q_N ≡ 2^S (mod Q)`, where `q` is the carry `q_0 = 0`, `q_{j+1} = 3q_j + 2^{s_j}`
  (`Divergence.C_succ`);
- `F_N(h) = (1/M_N)·sum_{D ∈ W_0(N)} exp(2 pi i·h·r(D)/Q)`;
- `h ≈ 1.505644` = the confined-word growth exponent, `I_0 = alpha − h ≈ 0.079319`. Both are
  external inputs, labelled `[D]`.

---

## Lemma D1 — square-root cancellation at odd frequencies `[C]`

> **`[C]` MISSING.** There are absolute constants `C, B` such that for every `N ≥ 1` and every
> **odd** `h` with `1 ≤ h < Q`,
> ```
> | sum_{D ∈ W_0(N)} exp(2 pi i·h·r(D)/Q) |   ≤   C · N^B · M_N^{1/2}.
> ```

Equivalently `|F_N(h)| ≤ C·N^B·M_N^{−1/2}` for odd `h`.

**Evidence, and exactly what it covers.** Measured at `h ≤ 1024` for `N = 15,…,50`
(ratio to `M_N^{−1/2}`: `0.564, 0.491, 0.393, 0.419, 0.276, 0.196`) and at random odd `h`
across 2-adic level `t = 0` for `N = 20, 25, 30` (ratios `0.647, 0.473, 0.315`).
`log2(mean|F|)` slope over `N = 40→50` is `−0.7820` against the target `−h/2 = −0.7528`.
All of that is `[F]`, over six depths and one frequency window. **It does not touch the range
`h ≤ 2^{(alpha−c)N}` that any proof would need** — see [`FINDINGS.md`](FINDINGS.md) §7.

---

## Lemma D2 — the graded dyadic version `[C]`

> **`[C]` MISSING.** With the same `C, B`: for every `t ≥ 0` and every **odd** `u`,
> ```
> | F_N(2^t·u) |   ≤   C · N^B · max( M_N^{−1/2},  2^{−(A[N]+1−t)/2} ).
> ```

D2 contains D1 (take `t = 0`, and note `M_N^{−1/2} ≥ 2^{−(A[N]+1)/2}` for all `N` in range).
D2 is the abstraction of the measured law of [`FINDINGS.md`](FINDINGS.md) §3, whose *exact*
structural half — the identity
`|F_N(2^t·u)| = |`DFT of `r mod 2^{A[N]+1−t}` at `u|`, and the fact that `r mod 2^k` is a function
of the path prefix alone — is `[V]` at `N = 14` (`check_dyadic_tower.py`). What is missing is the
**quantitative** bound on the DFT at each coarse scale.

---

## Consequence `[C]`, conditional on D2

> D2 together with the Erdős–Turán inequality would give, for every fixed
> `c > alpha − h/2 ≈ 0.832141` and all large `N`,
> ```
> r_min(N, 0)  ≤  2^{c·N},
> ```
> an **affirmative answer to Open Problem 8(4)** of *After the Reduction* (v2.3,
> [doi:10.5281/zenodo.22961534](https://doi.org/10.5281/zenodo.22961534)) — "the upper half alone,
> at any exponent: is there `c < 1` with `r_min(N,0) ≤ 2^{cN}` for all large `N`?" — **with no
> input on (DE)** whatever.

Open Problem 8(4) is, by the synthesis note's own Remark 4.9, the one item on its list that does
not require progress on universal drift exit; it is consistent with (DE) being true. The
elementary bound there gives only `c = 1`; the conjectured value is `c = I_0 ≈ 0.0793`; nothing
between the two is known. This route, at best, would supply `c ≈ 0.8322`.

Soundness of the shell restriction: a hit `r < 2^{cN}` in the terminal shell bounds `r_min(N,0)`
because each shell realizer is a genuine odd `0`-confined integer — re-verified by direct orbit
iteration for every shell word at `N ≤ 16` (`[V]`, `check_realizers.py` §§1–4). The terminal-shell
minimum is only an upper bound on `r_min` (`[V]`, overestimate up to `13.30×`; `FINDINGS.md` §8).

---

## Why D1/D2 are not available

**Not a corollary of Tao-style Syracuse equidistribution.** The closest known cancellation theorem
of this exact algebraic shape concerns `sum_m 3^{n−m}·2^{−(a_m+…+a_n)}` — structurally the same
object as the carry `q_N = sum_j 3^{N−1−j}·2^{s_j}` — but **modulo `3^n`**, where `2` is a
**unit**: every summand is invertible, the Fourier analysis runs on characters of `Z/3^n Z`, and
the cancellation comes from the law of the `a_m` inside that unit group. Here the modulus is
`Q = 2^{A[N]+1}`, a power of **2**, exponentially large in `N`, in which the `2^{s_j}` are
precisely the **nilpotent** directions. This is a **failure of hypothesis, not of constants**: a
character with `v₂(h) = t` annihilates every summand with `s_j ≥ A[N]+1−t`, which is exactly the
collapse verified exactly in `check_dyadic_tower.py` §4 and the mechanism of the whole resonance
tower. See [`NON_ROUTES.md`](NON_ROUTES.md) §1.

**D1 is the Fourier form of an already-named gap.** The missing arrow — that counting confined
words says nothing about where their least realizers land among the naturals, i.e.
**anti-concentration of the least-realizer / moving-anchor map** — is recorded as the central gap
in `explorations/confined_shell_consolidation/PAUSE_CHECKPOINT_2026-09-12.md` §9 of
`innerlightr-wq/eoc-lean-verification`. D1 is that gap stated as an exponential-sum bound.
Cited, not copied. `[D]` for the content of that checkpoint, which was read but is not reproduced
here.

**D1 is also the precise form of an already-conjectured arrow `[D]`.** *Three Scales of
Confinement*, **Conjecture I.1** (phase sensitivity of confined realizers) has as its missing arrow
exactly *"realizer-residue geometry → `r_min(N,c)`"*. D1 **makes that arrow precise**: it is a
quantitative exponential-sum statement about the residue geometry, from which the `r_min` side
follows by Erdős–Turán (see the Consequence above). Reported from the same day's discussion and
**not re-checked in this branch** — Conjecture I.1 was not read here; the cross-reference is
recorded so the two statements are not developed independently.

**Shape of the difficulty.** Via the additive formula (`FINDINGS.md` §1) the twisted sum is an
`N`-fold product of twisted transfer operators on the state `(j, s_j)`, whose dimension is
`O(N)`, not exponential. Square-root cancellation demands that the `h`-twisted operator's growth
rate be **half, in bits, per step** of the untwisted one — `2^{0.753}` against `2^{1.506}` — a
quantitative spectral-gap statement for a **non-stationary** family: the twist phase
`h·3^{−(j+1)}·2^{s_j} mod 2^{A[N]+1}` depends on `j` through `3^{−(j+1)}` and on the barrier
through the irrational slope `alpha`. Standard mixing and large-deviation inputs give the wrong
scale on an `O(N)`-dimensional state space. `[C]`.

**A possibly separable sub-lemma.** The `t ≥ t*` half of D2 — where `t* = A[N]+1 − log2 M_N`, and
where the measured law is governed by `2^{−(A[N]+1−t)/2}` rather than by `M_N^{−1/2}` — has a
clean combinatorial handle: by the exact collapse, `r mod 2^{A[N]+1−t}` is a function of a
**short** path prefix, so that half is a statement about a small, explicitly described object.
The `t = 0` half (= D1) has no such handle, and it is the half that actually binds
(`FINDINGS.md` §5). `[C]`, unexplored.

---

## Below `0.832` — two unexplored questions

Both `[C]`, and both **unexplored in this round**. Neither is a conjecture of this branch; they
are recorded as the only directions identified that could in principle go below the sup-norm
Fourier ceiling of `alpha − h/2 ≈ 0.832141`.

1. **Explicit construction `[C]`, unexplored.** Is there an explicit construction of small
   `0`-confined seeds — a family `m_N` with `m_N ≤ 2^{cN}` and `ConfinedUpTo N m_N`, for some
   `c < alpha − h/2`? The elementary family `m = 2^k − 1` of the synthesis note's Remark 4.9 gives
   only `c = 1`. A construction is not subject to the discrepancy ceiling at all, and the
   observed behaviour of `r_min` on this range — constant at `27` for `N = 4…14`
   (`[V]`, `check_realizers.py` §5) — is at least consistent with much smaller survivors
   existing far beyond where any discrepancy argument could find them.
   **Equivalent form, which may be the more tractable one to attack:** by the Hensel-truncation
   reformulation ([`FINDINGS.md`](FINDINGS.md) §1b, cited from Proposition 7.1 of the
   Sturmian–Mahler Edge note), this asks for a `0`-confined word of length `N` whose 2-adic point
   has a **zero-run of length about `(alpha − c)·N`** ending at depth `S = A[N]`. Constructing a
   long zero-run is a digit-pattern question, not a discrepancy question, and is therefore not
   subject to the `alpha − h/2` ceiling.

2. **Bilinear estimate `[C]`, unexplored.** The additive formula splits `r` as
   `prefix + 3^{−k}·(suffix)` at any cut `k`: with `s_k = sigma`,
   ```
   r  ==  −sum_{j<k} 3^{−(j+1)}·2^{s_j}  +  3^{−k}·( 3^{−N+k}·2^S − sum_{j≥k} 3^{−(j−k+1)}·2^{s_j} )
   ```
   modulo `Q`, where the second bracket depends only on the suffix word and on `sigma`. Could a
   **bilinear** (Cauchy–Schwarz / large-sieve style) estimate over the prefix × suffix
   factorization, conditioned on `sigma`, beat the sup-norm bound and so push `c` below
   `alpha − h/2`? Not attempted here. Note the known obstruction in the neighbourhood: the
   prefix-sharing coupling is real but was already shown to carry **no** archimedean closeness
   (see [`NON_ROUTES.md`](NON_ROUTES.md) §4), so any bilinear gain would have to come from the
   modular structure alone.

**Hard ceiling, for both.** Neither can be pushed below `alpha − h = I_0 ≈ 0.079319` by an
equidistribution argument of any kind: an interval of length `2^{cN}` inside a modulus
`2^{alpha·N}` holds on average `M_N·2^{(c−alpha)N} < 1` residues once `c < alpha − h`, so below
that exponent the statement is not a discrepancy statement. `[F]` for the arithmetic of the
ceiling, `[D]` for `h`.
