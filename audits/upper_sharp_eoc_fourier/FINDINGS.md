# Findings — Fourier route to the upper half of Sharp EOC

One result per section. Every statement carries exactly one status label.

| label | meaning |
|---|---|
| `[P]` | proved, with cited inputs |
| `[V]` | verified by exact computation in this branch's scripts, **for the stated finite range only** |
| `[F]` | float / numerical diagnostic only — not a proof |
| `[C]` | conjectural, or a missing lemma |
| `[R]` | refuted / negative result |
| `[D]` | reported from discussion, not re-checked in this branch |

Labels are never upgraded. Conventions and their Lean sources in this repository: see
[`README.md`](README.md).

Throughout: `alpha = log2 3 = 1.584963…`; `A[N] = floor(N·alpha)`; `W_0(N)` is the set of
`0`-confined positive valuation words of length `N` with terminal sum exactly `S = A[N]`
(the *terminal shell*); `M_N = |W_0(N)|`; `Q = 2^(S+1)`; `r(D)` is the least realizer of `D`;
and

```
F_N(h) = (1/M_N) · sum_{D in W_0(N)} exp(2 pi i · h · r(D) / Q),      F_N(0) = 1.
```

`h ≈ 1.505644` denotes the confined-word growth exponent and `I_0 = alpha − h ≈ 0.079319`.
Both are external inputs to this branch, labelled `[D]` wherever used.

---

## 1. The additive realizer formula — PRIOR ART — and its new use as an `O(N²)` DP

**Statement.** For every positive valuation word `D` of length `N` with prefix sums `s_j` and
terminal sum `S`,

```
r(D)  ==  3^(-N)·2^S  −  sum_{j=0}^{N-1} 3^(-(j+1))·2^(s_j)      (mod 2^(S+1))
      ==         2^S  −  sum_{j=0}^{N-1} 3^(-(j+1))·2^(s_j)      (mod 2^(S+1)).
```

**Status `[P]` — and it is NOT new.** It is prior art of this programme, in two places:

- **"The Sturmian–Mahler Edge of the Accelerated Collatz Realizer Problem"** (De Jesús, June 2026),
  **Lemma 2.1** (Terras–Everett class): the odd `m` whose word begins with `D` form the single
  residue class `{m : 3^N·m + C_N(D) ≡ 2^{S_N} (mod 2^{S_N+1})}`, stated there equivalently as
  `m ≡ 3^{−N}(2^{S_N} − C_N(D)) (mod 2^{S_N+1})`, with **Definition 2.2** `r(D)` = the least
  positive element of that class. The summand-by-summand form is the identity
  `3^{−N}·C_N = sum_{i<N} 3^{−i−1}·2^{S_i}`, which is what drives the proof of that note's
  **Theorem 4.1** (where `Ξ_{α,β} = −(1/3)·sum_i 3^{−i}·2^{S_i} = −sum_i 3^{−i−1}·2^{S_i}`).
  **Citation confirmed in this round** against the local copy in this repository,
  [`audits/sturmian_irrationality/sources/B_Sturmian_Mahler_Edge.pdf`](../sturmian_irrationality/sources/B_Sturmian_Mahler_Edge.pdf)
  (source [B] of that audit's `SOURCES.md`).
- **EOC Revision 8, Proposition 5.2**, [doi:10.5281/zenodo.23146031](https://doi.org/10.5281/zenodo.23146031)
  — the same statement, to which the form above is **equivalent** because
  `3^{−N}·2^S ≡ 2^S (mod 2^{S+1})`: `3^{−N}` is odd, so `3^{−N} = 1+2k` and
  `3^{−N}·2^S = 2^S + 2^{S+1}·k`. That simplification is verified exactly — `[V]`,
  `check_additive_formula.py` §4, together with the reduced form of the formula itself, 0 mismatches
  at `N = 5, 8, 11, 13`. (The DOI is cited as given; it was not resolved in this round.)

**Verified `[V]`.** Exact integer agreement with the least realizer for **every** terminal-shell
word at `N = 5, 8, 11, 13` (7 / 85 / 961 / 8045 words), **0 mismatches**, in both the
`3^{−N}·2^S` and the `2^S` form. Script: `check_additive_formula.py` §§1, 4. The carry recursion
(`Divergence.C_succ`) is independently checked against the closed form on the same words (§2).

**The only new content of this round `[P]`: its use as an `O(N²)`-state DP over the whole confined
ensemble.** The `j`-th summand depends on the path only through the pair `(j, s_j)`. Hence for any
frequency `h` the twisted sum `sum_D exp(2 pi i·h·r(D)/Q)` factorizes through a forward DP on that
state, and confinement bounds `s_j` by `A[j]`, so the state space has size `O(N²)` rather than
`O(2^{1.5N})`. This is the only reason depths `N = 40, 50` were reachable in this round **without
enumerating any word set** at those depths.

**Validation of the DP `[F]`.** Against brute-force enumeration over 9 frequencies including
`Q/8, Q/4, Q/2`: max relative deviation `8.3e−15` at `N = 10`, `5.4e−13` at `N = 15`.
Script: `fourier_diagnostics.py` §1. This bounds the *implementation*, not any estimate.

### 1b. The Hensel-truncation reformulation of the target

**Cited `[P]`.** Same note, **Proposition 7.1** ("Realizers are Hensel truncations"):
`r(D_N) = sum_{j≤S_N} ε_j·2^j`, the integer formed by the **first `S_N+1` Hensel bits** of the
word's 2-adic point; it is odd (`ε_0 = 1`); and if `2^k ≤ r(D_N) < 2^{k+1}` then
`ε_{k+1} = … = ε_{S_N} = 0` — a **zero-run of length `S_N − k`** below depth `S_N+1`, with
`S_N − k = ⌈E_N⌉ + O(1)`, `E_N := S_N − log2 r(D_N)`. Confirmed against the local PDF above.
(The note states it for the mechanical/Sturmian point `Ξ_{α,β}`; its proof uses only the congruence
and leastness, so the truncation statement is not special to that case. Recorded here as cited, for
the mechanical case, with the generalization flagged rather than claimed.)

**Consequence — the target restated.** `r_min(N,0) ≤ 2^{cN}` holds **exactly when** some
`0`-confined word of length `N` has `r(D)` whose Hensel bits vanish from position about `cN` up to
`S` — i.e. a **zero-run of length about `(α − c)·N`** below depth `S+1`. This is a genuinely
different reading of the same problem: the question is not "is some residue small" but "does some
confined word's 2-adic point have a long enough zero-run at the right depth".

**Verified `[V]`** as the elementary bit identity `r < 2^k ⟺ bit_j(r) = 0 for every j ∈ [k, S]`,
on every terminal-shell word at `N = 14, 15, 16` for `c = 0.90, 0.95` — identity holds in all six
cases. Longest zero-run actually present in the shell: `14` at `N = 14`, `16` at `N = 15`, `18` at
`N = 16`, against the `≈ (α−c)N` needed (`≈ 11` at `N = 16`, `c = 0.90`). Script:
`check_additive_formula.py` §5.

---

## 2. The forced `mod 4` peak: `|F_N(Q/4)| = 1` identically

**Statement.** Zero confinement at `j = 1` forces `2^{s_1} ≤ 3`, hence `d_0 = 1`, hence
`v₂(3r+1) = 1`, hence `r ≡ 3 (mod 4)` for every realizer. Therefore
`exp(2 pi i·(Q/4)·r/Q) = exp(2 pi i·r/4) = −i` is **constant** over the ensemble and

```
|F_N(Q/4)| = 1   for every N.
```

**Status of the arithmetic input `[P]`** — and it is proved **in this repository**:
`Descent.a_eq_one_of_confined` and `Descent.mod_four_of_confined`
([`Descent/ResidueLaw.lean`](../../Descent/ResidueLaw.lean), lines 21 and 33), with no `sorry`.
`Descent.least_confined_mod12` (L4) is the `mod 12` refinement.

**Measured `[F]`.** `|F_N(Q/4)| = 1.000000` and `|F_N(Q/2)| = 1.000000` at `N = 12, 14, 15, 16`;
`|F_N(Q/8)| = 0.604, 0.616, 0.620, 0.625` — **rising**, not decaying.
Script: `fourier_diagnostics.py` §2. Exact residue counts: `check_dyadic_tower.py` §5.

**Methodological consequence.** `sup_{h≠0} |F_N(h)|` **cannot** decay. Any criterion of the form
"the largest nontrivial Fourier coefficient tends to zero" is false by construction here and
**must never be used as a go/no-go test** for this ensemble. It was not used in this round.

---

## 3. The dyadic tower identity

**Statement.** For every `t ≥ 0` and every odd `u`,

```
|F_N(2^t·u)|  =  | normalized DFT of ( r mod 2^(S+1−t) ) at u |.
```

**Status `[V]`**, by **exact integer arithmetic** — no float enters the verification. The identity
is term by term, because `exp(2 pi i·2^t·u·r/2^(S+1)) = exp(2 pi i·u·r/2^(S+1−t))`, so the check is
the integer statement `(2^t·u·r) mod Q == 2^t·((u·(r mod m)) mod m)` with `m = 2^(S+1−t)`.
Verified at `N = 14` for **all** `t = 0…S−1` (`S = 22`) and `u ∈ {1,3,5,7}`: 1,552,056 exact
integer comparisons, **0 mismatches**, plus an exact multiset comparison of the two exponent sets
for every `(t,u)` — so the two sums agree as exact sums of roots of unity.
Script: `check_dyadic_tower.py` §§1–2. A float evaluation of both sides agrees to `0.000e+00` (§3),
recorded as a `[F]` sanity line only.

**Mechanism `[V]`.** By §1, reducing `r` modulo `2^k` kills every summand with `s_j ≥ k` (and the
constant too, once `S ≥ k`). Multiplying the *frequency* by `2^t` is that same reduction with
`k = S+1−t`. So `r mod 2^k` is a function of the path **prefix** alone. Checked exactly at
`N = 12` and `N = 14`: the number of distinct values of `r mod 2^k` equals the number of distinct
truncated prefix profiles `{(j, s_j) : s_j < k}`, for every `k = 1…14`, and the profile determines
the residue. Script: `check_dyadic_tower.py` §4.

**The resulting coarse-scale skew `[V]`** (`N = 14`, exact counts): modulo `2^k` for
`k = 2,…,7` only `1, 2, 3, 4, 8, 13` of the `2^{k−1}` odd classes are occupied, with maximum class
share `1.0000, 0.8080, 0.6159, 0.4239, 0.2714, 0.1585` against the uniform-on-odd values
`0.5000, 0.2500, 0.1250, 0.0625, 0.0312, 0.0156`. In particular only **3 of the 8** odd classes
modulo `16` are occupied at all. Script: `check_dyadic_tower.py` §5.

**Empirical law `[F]`.**

```
|F_N(2^t·u)|  ≈  max( M_N^(−1/2),  2^(−(S+1−t)/2) ),      u odd,
```

with crossover at `t* = S + 1 − log2 M_N`, which is asymptotically `(alpha − h)·N = I_0·N`.
Measured mean `|F_N(2^t·u)|` over random odd `u` (256 per level), as a ratio to `M_N^{−1/2}`:

| N | `t*` predicted | t=0 | t=2 | t=8 | t=12 | t=16 | t=20 | t=S−1 |
|---|---|---|---|---|---|---|---|---|
| 20 | 9.5 | 0.647 | 0.301 | 1.317 | 4.381 | 16.18 | 63.99 | 2437 |
| 25 | 10.4 | 0.473 | 0.259 | 1.011 | 3.527 | 12.54 | 47.33 | 28640 |
| 30 | 11.7 | 0.315 | 0.480 | 0.747 | 2.070 | 10.85 | 31.44 | 290072 |

The transcript prints `2^{−(S+1−t)/2}` alongside for direct comparison; above `t*` the two agree
to within a factor of about `2`, and `|F|` reaches `1.000e+00` exactly at `t = S−1`.
Script: `fourier_diagnostics.py` §3b. This is a float diagnostic over sampled `(t,u)`; it is
**not** a proved estimate. It is the measured shape that Lemma D2 in
[`OPEN_PROBLEMS.md`](OPEN_PROBLEMS.md) abstracts.

---

## 4. The tower is harmless under Erdős–Turán weighting

**Statement `[F]`.** Summed against the `1/h` weight of the Erdős–Turán inequality, the entire
dyadic resonance tower contributes `O(Q^{−1/2}) = O(2^{−alpha·N/2}) = O(2^{−0.792·N})`.

**Reason (heuristic summation of the measured law of §3, not a proof).** Split the weighted sum by
`t = v₂(h)`: level `t` contributes `≈ 2^{−t} · 2^{−(S+1−t)/2} = 2^{−(S+1)/2}·2^{−t/2}`, and
`sum_{t≥0} 2^{−t/2} = O(1)`.

**Why this matters.** `2^{−0.792·N}` already beats the target `H/Q ≈ 2^{−(alpha−c)N}` for every
`c > alpha/2 = 0.792481`. So the resonances — including the identically-`1` peak at `Q/4` — are a
fatal obstruction to the **unweighted** criterion of §2 and a **non-obstruction** to the weighted
one. It would be easy to get this backwards; the measurement says the opposite of the first guess.

**Numerical confirmation `[F]`.** Unbiased band-mean sampling (uniform random `h` within each
dyadic band weights high-`v₂` frequencies at their true density `2^{−t}`) gives a total weighted sum
at `N = 30` (for `c = 0.90`, `K* = 2^21`) of `1.999e−05`, against
`½·ln(K*)·M_N^{−1/2} = 2.51e−05` — i.e. the total is **entirely** the `t = 0` term. Script: `fourier_diagnostics.py` §§4–5.

**Caveat.** The band means are seeded Monte-Carlo estimates (seed `20261013`, 128 probes per band),
reproducible but not exact; across runs with different probe counts the third significant figure
moves and the reported margins shift by about `±0.1` in the exponent.

---

## 5. The binding term is the odd-frequency (`t = 0`) term, and it fails at `N ≤ 30`

**Measured square-root cancellation at low frequencies `[F]`.** Mean `|F_N(h)|` over
`h = 1…1024`, against `M_N^{−1/2}`:

| N | S | M_N | `M_N^{−1/2}` | mean `\|F\|` | ratio | `B_N(1024)` |
|---|---|---|---|---|---|---|
| 15 | 23 | 51,033 | 4.427e−3 | 2.497e−3 | 0.564 | 1.766e−2 |
| 20 | 31 | 5,936,673 | 4.104e−4 | 2.016e−4 | 0.491 | 2.133e−3 |
| 25 | 39 | 820,236,724 | 3.492e−5 | 1.371e−5 | 0.393 | 1.086e−3 |
| 30 | 47 | 84,141,805,077 | 3.447e−6 | 1.445e−6 | 0.419 | 9.857e−4 |
| 40 | 63 | 2.029e15 | 2.220e−8 | 6.129e−9 | 0.276 | 9.766e−4 |
| 50 | 79 | 5.203e19 | 1.386e−10 | 2.713e−11 | 0.196 | 9.766e−4 |

`log2(mean|F|)` slope over `N = 40→50` is `−0.7820` against the square-root target
`−h/2 = −0.7528` — i.e. slightly *better* than square root over that step. Six depths, one
frequency window; this is weak evidence about an exponential law, and it is `[F]`.
For `N ≥ 30`, `B_N(1024)` has saturated at the truncation term `1/K = 9.766e−4`: the Fourier part
is already negligible there and `B` is all truncation. Script: `fourier_diagnostics.py` §3.

**The Erdős–Turán test fails `[F]`.** Form used
`D_N ≤ C_ET·(1/K + sum_{h≤K} |F_N(h)|/h)`; rounding `H = 2^floor(c·N)`, `K* = ceil(Q/H)`; success
condition `C_ET·B_N(K*) < H/Q`. With `C_ET = 4` (a **stated parameter** — see
[`README.md`](README.md)):

| N | c | H | H/Q | K* | est `sum \|F\|/h` | verdict |
|---|---|---|---|---|---|---|
| 20 | 0.90 | 2^18 | 6.104e-5 | 16,384 | 1.790e-3 | **FAIL by 2^6.9** |
| 20 | 0.95 | 2^19 | 1.221e-4 | 8,192 | 1.671e-3 | **FAIL by 2^5.9** |
| 20 | 0.99 | 2^19 | 1.221e-4 | 8,192 | 1.671e-3 | **FAIL by 2^5.9** |
| 25 | 0.90 | 2^22 | 3.815e-6 | 262,144 | 2.038e-4 | **FAIL by 2^7.8** |
| 25 | 0.95 | 2^23 | 7.629e-6 | 131,072 | 1.953e-4 | **FAIL by 2^6.7** |
| 25 | 0.99 | 2^24 | 1.526e-5 | 65,536 | 1.857e-4 | **FAIL by 2^5.7** |
| 30 | 0.90 | 2^27 | 4.768e-7 | 2,097,152 | 1.999e-5 | **FAIL by 2^7.4** |
| 30 | 0.95 | 2^28 | 9.537e-7 | 1,048,576 | 1.911e-5 | **FAIL by 2^6.4** |
| 30 | 0.99 | 2^29 | 1.907e-6 | 524,288 | 1.798e-5 | **FAIL by 2^5.4** |

The verdict is unchanged for any `C_ET ∈ [1,10]`, since the margins are `2^5`–`2^8`.

**Which estimate failed, precisely `[F]`.** Not `|F(Q/4)|` — weighted away (§4). Not the dyadic
tower — `O(Q^{−1/2})`, comfortably sufficient (§4). The failure is the **`t = 0` term**
`sum_{h≤K*, h odd} |F_N(h)|/h ≈ ½·ln(K*)·M_N^{−1/2}`, because `M_N^{−1/2}` itself still exceeds
`H/Q` at reachable depths. Up to the `N`-factor, success requires

```
log2(M_N)/N  >  2·(alpha − c).
```

| N | `log2(M_N)/N` | `c=0.90` needs 1.3699 | `c=0.95` needs 1.2699 | `c=0.99` needs 1.1899 |
|---|---|---|---|---|
| 15 | 1.0426 | SHORT | SHORT | SHORT |
| 20 | 1.1251 | SHORT | SHORT | SHORT |
| 25 | 1.1845 | SHORT | SHORT | SHORT |
| 30 | 1.2097 | SHORT | SHORT | **OK** |
| 40 | 1.2713 | SHORT | **OK** | OK |
| 50 | 1.3099 | SHORT | OK | OK |

`log2(M_N)/N` is still `1.21` at `N = 30` because it approaches its limit `h ≈ 1.5056` only through
the `N^{−3/2}` correction. **The failure at `N ≤ 30` is a finite-size effect, not a structural
refutation of the mechanism at `c = 0.90`.** Script: `fourier_diagnostics.py` §§5–6.

---

## 6. The `c = 0.832` threshold

**Statement `[F]`/`[D]`.** Under square-root cancellation at odd frequencies, the asymptotic form of
the condition in §5 is

```
c  >  alpha − h/2  =  0.832141…
```

All three tested exponents `c = 0.90, 0.95, 0.99` clear it asymptotically; none clears it at
`N ≤ 30`. The threshold depends on `h ≈ 1.505644`, an external input, hence the `[D]` component.

**This is a limit of the method, not of the truth.** `0.832141` is what the sup-norm Fourier /
discrepancy route can deliver *at best*, even granting Lemma D1/D2 in full. The conjectured truth
is `c = I_0 ≈ 0.0793` (Sharp EOC). In particular:

- the achievable prize on this route is an affirmative answer to Open Problem 8(4) at
  `c ≈ 0.8322` — real, but leaving the overwhelming majority of the gap from `1` to `0.0793`
  untouched;
- **no equidistribution method of this kind can go below `alpha − h = I_0 ≈ 0.079319`**, since an
  interval of length `2^{cN}` out of a modulus `2^{alpha·N}` holds on average
  `M_N·2^{(c−alpha)N}` residues, which is below `1` once `c < alpha − h`. Below that exponent the
  statement is not a discrepancy statement at all and needs a construction.

---

## 7. The estimate is not numerically verifiable

**Statement `[F]`, an extrapolation.** Projecting with
`M_N ≈ 0.4·2^{−3.28}·2^{h·N}·N^{−3/2}` — the fitted count asymptotic of the synthesis note's
Proposition 4.7, an external input `[D]` — the Erdős–Turán bound first becomes true at:

| c | `alpha − c` | first `N` | `K*` at that depth |
|---|---|---|---|
| 0.99 | 0.5950 | ≈ 92 | `2^55.7` ≈ 10^17 frequencies |
| 0.95 | 0.6350 | ≈ 132 | `2^84.8` ≈ 10^26 frequencies |
| 0.90 | 0.6850 | ≈ 254 | `2^175.0` ≈ 10^53 frequencies |

So the estimate is of a kind that can **never** be validated numerically: it first bites at depths
where its hypothesis ranges over `10^17`–`10^53` frequencies. Finite experiments at `N ≤ 50` bear
on the hypothesis only through the `h ≤ 1024` window and sparse random probes; they can neither
establish nor refute an eventual exponential law. Script: `fourier_diagnostics.py` §7.
**This row is an extrapolation of a fitted asymptotic under an unverified uniformity hypothesis —
a feasibility estimate, not evidence.**

---

## 8. Shell caution: the terminal shell is an upper bound, and shells must not be naively mixed

**Statement `[V]`.** The terminal-shell minimum overestimates the true `r_min(N,0)` by up to
**13.30×** on `N ≤ 14`:

| N | `r_min(N,0)` (direct scan) | terminal-shell min | ratio |
|---|---|---|---|
| 5 | 27 | 47 | 1.741 |
| 9 | 27 | 359 | **13.296** |
| 12 | 27 | 319 | 11.815 |
| 13 | 27 | 283 | 10.481 |
| 14 | 27 | 283 | 10.481 |

`r_min(N,0) = 3, 7, 7, 27, 27, …, 27` for `N = 1…14`, by a direct scan of every odd
`m < 2^{A[14]+1} = 2^23` using the actual accelerated map — matching the reference values.
Script: `check_realizers.py` §5. In this repository `r_min(N,0)` is natively
`IsLeast {m | Odd m ∧ Descent.ConfinedUpTo N m}` (`Descent/ResidueLaw.lean`).

A hit in the terminal shell is nonetheless **sound** as an upper bound: each shell realizer is a
genuine odd `0`-confined integer, re-verified by direct orbit iteration (§9).

**Mixing shells requires the common modulus and the lift weights `[V]`.** A word of terminal sum
`S` has exactly `2^{A[N]−S}` lifts modulo `2^{A[N]+1}`, so

```
sum_S |W(N,S)| · 2^(A[N]−S)  ==  #{ odd m < 2^(A[N]+1) : 0-confined for N steps },
```

verified exactly at `N = 8, 10, 12, 14`: `367 / 2,114 / 27,328 / 168,807`, matching both the
weighted sum and the independent brute scan. Script: `check_realizers.py` §6.
**One least realizer per word is therefore *not* the uniform measure on surviving residues.**
No shells were mixed anywhere in this round.

---

## 9. The finite fact that was established

**Statement `[V]`.** `r_min(N,0) ≤ 2^{0.9·N}` for `N ≤ 16`.

Exact integer interval-hit counts in the terminal shell, `H = 2^floor(c·N)`:

| N | M_N | min r | `#{r < 2^{⌊0.90N⌋}}` | `#{r < 2^{⌊0.95N⌋}}` | uniform prediction `M·H/Q` |
|---|---|---|---|---|---|
| 14 | 17,637 | 283 | 5 | 15 | 8.6 / 17.2 |
| 15 | 51,033 | 251 | 18 | 46 | 24.9 / 49.8 |
| 16 | 108,950 | 251 | 21 | 57 | 26.6 / 53.2 |

Hits are plentiful and within about `1.5×` of the uniform prediction, so the ensemble does look
archimedean-uniform at this scale. **The Fourier bound fails by `2^5`–`2^8` at exactly the depths
where the direct computation succeeds easily.** Script: `fourier_diagnostics.py` §8.

For all `N ≤ 16` the per-shell checks also hold exactly (`check_realizers.py` §§1–4): the realizer
congruence, injectivity of `D ↦ r(D)` on the shell, `r ≡ 3 (mod 4)` for every realizer, and
re-verification of every realizer by direct accelerated-orbit iteration (actual valuation word
equals `D`, exact `0`-confinement for `N` steps, seed odd).

**Nothing asymptotic follows.** These are finite facts. They certify neither the Fourier estimate
nor any statement for large `N`.

---

## 10. Finite-ensemble results from the same day's discussion

Recorded for preservation. Not research output of this branch.

### 10.1 The `(1,2)` / `(2,1)` blocks — partly `[V]`, partly `[D]`

**`[V]`** (reproduced here directly from the carry recursion `Divergence.C_succ`,
`q_0 = 0, q_{j+1} = 3q_j + 2^{s_j}`): the words `(1,2)` and `(2,1)` have the **same** total
valuation `S = 3` and **different** carries `q_2 = 5` and `q_2 = 7`. Prefix sums
`(0,1,3)` and `(0,2,3)` respectively. Script: `check_additive_formula.py` §3.

**`[D]`** — not re-checked in this branch: that these different modular phases can *force*
cancellation when both blocks carry comparable weight, which is what supports the finite-modulus
estimate for the confined-word model.

### 10.2 Separation plus weight, versus sign changes alone — `[D]`

Reported from discussion, not re-checked here: the operative condition is
**"quantitative separation + appreciable weight ⇒ cancellation"**. Sign changes alone do **not**
force cancellation — there are constructions exhibiting a sign change at every step and
arbitrarily little cancellation. Recorded because it blocks the tempting shortcut of reading a
sign alternation as evidence of cancellation.

### 10.3 Modulus 11 — `[D]`

Reported from discussion, not re-checked here: modulo `11` the full hypercuboid sum **vanishes**,
but the natural scaling family built from Collatz carry differences has character average exactly
`−1`. Recorded as a caution that vanishing of a full sum does not transfer to a structured
subfamily.

---

## Reproduction

```
cd audits/upper_sharp_eoc_fourier/scripts
python3 check_counts.py
python3 check_realizers.py
python3 check_additive_formula.py
python3 check_dyadic_tower.py
python3 fourier_diagnostics.py            # optional: --cet=3.0
```

Each exits non-zero on any failed assertion; add `--quick` for a reduced range. Standard library
only; nothing is written to disk. Stored transcripts of the full runs are in
[`results/`](results/). Every number in this file appears in one of those transcripts.
