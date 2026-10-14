# Report — moment / localization routes to the upper half of Sharp EOC

Branch `audit/upper-sharp-eoc-moments`, branched from `audit/upper-sharp-eoc-fourier` at
`527e0cf`. Falsification-first pilot. Gates were fixed in
[`PREREGISTRATION.md`](PREREGISTRATION.md) and committed (`226f38a`) **before any script ran**;
**no gate was changed after seeing data.** Full evidence, with labels, in
[`FINDINGS.md`](FINDINGS.md); transcripts in [`results/`](results/).

## Verdicts

| route | verdict | reason |
|---|---|---|
| **Test 0: window at zero typical** | **FAIL** as preregistered · **PASS** post-hoc | The preregistered slope gate fires (`-0.094 / -0.092 / -0.069 <= -0.02` for all three `c`, in both fits), so `[R]` is recorded for "the window at zero is typical". **But the gate is ill-posed for this data shape**: `rho_0 = X_0/E` starts *above* 1 (`1.40`–`1.95` at `N = 8…12`) and *relaxes to* 1 (`0.95`–`1.01` at `N = 16…18`; `0.992`–`1.005` at the excluded extension depths `N = 19, 20`), and an OLS slope across that transient cannot tell relaxation from decay. The labelled post-hoc variant, plus the exact percentile of `X_0` falling from `0.98+` to `0.38`–`0.52`, reads the window at zero as **typical** at `N <= 20`. |
| **A: pair-collision bound** (typical windows, `c > I_0`) | **CONTINUE** | Gate A does not fire. `R_2(N,K) = O(1)` and slightly *decreasing* (slopes `-0.034, -0.030, -0.008`); the exact pair excess `ratio_P` is **below 1 in all 33 cells** (`0.676`–`0.9993`) and the exact dispersion index is `mu_2/E = 0.26`–`0.55`. The seed set is **underdispersed / mildly repulsive** — better than the independence the route assumes. Marked `[C]`, supported at `N = 8…18` only. The route's own conclusion is about *typical* windows and **says nothing about `r_min`**. |
| **B: 4th-moment localization** (`c ≈ 0.581`) | **CONTINUE** (with a reduced prize) | Preregistered Gate B records `[R]` (slope of `log2 tau_4 = +0.47`), but that gate is ill-posed in the same way: `tau_4` rises `0.026 -> 0.731` *toward* its Poisson value `≈ 3.02` and is **below it at every depth** (ratio `0.0086`–`0.2421`), while `tau_4/(3 tau_2^2) = 0.85`–`1.11` — the fourth moment is **Gaussian-shaped**. So the hypothesis the route needs is *supported* at the tested depths. The prize is smaller than it looks: the exact covering-radius exponent `log2 G/N` is already **`0.5580` at `N = 18`**, i.e. *below* `c_4 = 0.5812`. |
| **C: swap-only cancellation** | **STOP** | `[R]`. Median bits per step `0.1613 / 0.1742 / 0.1735` at `N = 20/30/40` — below the `0.3` gate at every depth, and only `28`–`30%` of the `alpha-1 = 0.585` needed merely to beat `c = 1` (`21`–`23%` of full square root). The binding constraint is structural: the density of usable disjoint swap sites is `nu ≈ 0.19`, capped at `0.5` by disjointness, and each site supplies `1` bit in the mean / `0.5` bits in the median for equidistributed phases — so even the maximal density gives `≈ 0.5 < 0.585`. **This does not refute Lemma D1; it closes only this mechanism for it.** |

## Overall recommendation

**One route deserves a proof attempt: B, the higher-moment localization — and it should be run at
`k = 6` or general even `k`, not `k = 4`.** Reasons:

1. Its two non-analytic steps are already `[P]` and elementary: the exceptional-set bound
   `B <= Q mu_k/E^k` and the localization step `r_min(N,0) <= B + H`, the latter resting on
   `r_min(N,0) = min Z_N`, which is proved here (`FINDINGS.md` §0b).
2. It is the only route whose missing hypothesis is **positively supported by exact
   all-shift computation** rather than merely unrefuted: `tau_4` and `tau_6` are Gaussian-shaped
   and sit *below* their Poisson references at every tested depth.
3. What it needs is a **moment** bound, which is a strictly weaker object than Lemma D1's
   sup-norm-over-all-odd-`h` bound — the estimate that the previous round could not supply and
   that `c_2 = 0.832` was the ceiling for. A moment bound tolerates bad individual frequencies,
   including the forced `|F(Q/4)| = 1` resonance, as long as they are rare.
4. `c_4 = 0.5812` is barely better than the *measured* covering radius `0.5580` at `N = 18`, so
   `k = 4` is not worth the work on its own; `c_6 = 0.4557` and `c_k -> I_0` are. The `k`-dependence
   is where the value is.

Route A is worth stating as a theorem about typical windows if the pair bound is provable, but it
is **not** a route to `r_min` and should not be sold as one. Route C is closed.

### The single most precise missing lemma

> **Lemma M_k (moment bound at window scale) `[C]`.** There are constants `C_k` and an absolute
> `B_0` such that for every even `k`, every `N`, and every `H = 2^w` with `E = M H/Q >= 1`,
> ```
> mu_k(N,H)  =  (1/Q) sum_{y mod Q} (X_y - E)^k   <=   C_k · N^{B_0} · E^{k/2}.
> ```

Given `M_k` for one even `k`, the two `[P]` steps of `FINDINGS.md` §1 yield
`r_min(N,0) <= 2^{c N}` for every `c > c_k = alpha - k h/(k+2)`, with no input on (DE).

Equivalent forms, for whichever is easier to attack:

- **Fourier.** By the same character expansion that gives the `k = 2` identity
  (`FINDINGS.md` §A1, `[P]`, verified to `2.8e-15`),
  `mu_k = (M/Q)^k sum_{h_1+…+h_k ≡ 0 (mod Q), h_i != 0} prod_i F(h_i) W(h_i)`.
  For `k = 4` this is an **additive-energy** bound on `Z_N` at scale `H`.
- **Combinatorial.** `sum_y X_y^k` counts `k`-tuples of seeds lying in a common window, weighted
  by `(H - diam)_+`; so `M_k` is a bound on the number of `k`-tuples of seeds of diameter `< H`.
  The exact `k = 2` case is already measured here and is *below* the independence prediction in
  every cell (`FINDINGS.md` §A3).

The right first target is `M_4` in the additive-energy form, since the `k = 2` case is an exact
identity and its measured value is favourable.

## What this does not establish

- **Finite depths only.** Tests 0, A, B live at `N = 8…18` (extension `19, 20`), Test C at
  `N = 20, 30, 40`. Nothing here is an asymptotic statement.
- **Moment behaviour at `N <= 18` says little about exponential laws.** `log2 M/N` reaches only
  `1.2559` at `N = 18` against its limit `h ≈ 1.5056` (`[D]`), so small-depth exponents are
  biased; the confined count is still deep in its `N^{-3/2}` transient. Every fitted slope in this
  audit is a finite-range diagnostic.
- **The audit depths cannot discriminate between exponents at all.** `r_min(N,0) = 27` for
  `N = 4…36` (`[V]`), so the whole primary range sits inside one plateau and
  `r_min <= 2^{cN}` holds there for every `c >= 0.2377`. What was measured is each **method's
  loss**, never the truth.
- **Two preregistered gates turned out to be ill-posed, in the same way.** Gates 0 and B both fire
  on a series *relaxing toward* its reference constant. Both verdicts stand as recorded and both
  carry a clearly labelled post-hoc variant. The methodological lesson: over an 11-depth window
  with a strong finite-size transient, an OLS slope on `log2` of a normalized statistic cannot
  separate "approaches the predicted constant" from "diverges"; a gate should test a **level**
  against a reference, or a slope **after** the transient, and should be specified with the
  expected transient in mind.
- **Sampled statistics are not proofs.** Only Test C samples (256 words per depth per ensemble,
  seed `20261013`; 512 odd `h <= 1024` plus 256 random odd `h`, seed `20261014`). Tests 0, A and B
  carry **no** sampling: all shift statistics are exact over all `Q` shifts by the event method,
  and all moments are exact `Fraction`s. Fourier values are floats, labelled `[F]`.
- **Nothing about (DE), divergent orbits, universal drift exit, or Collatz.** The target is an
  **upper** bound on the frontier — an existence statement about small zero-confined integers —
  while (DE) is equivalent to `r_min(N,0) -> infinity`. Nothing here bears on that, and nothing
  here bears on the **lower** half of Sharp EOC.
- **No novelty claims.** The additive realizer formula is prior art (Sturmian–Mahler Edge
  Lemma 2.1; EOC Rev 8 Prop. 5.2). Lemmas D1 and D2 are untouched and remain `[C]`. The one
  structural statement new to this branch is the shell-support fact of `FINDINGS.md` §0c (for odd
  `h`, `F(h)` is supported on the terminal shell alone), which is a short consequence of the lift
  geometric sum, not a result.
- **Not verified by this audit:** the external Lean statements of the realizer congruence and least
  realizer (their arithmetic is re-verified exactly here, the Lean is not); the previous round's
  Fourier findings, including the `c ≈ 0.832` ceiling and `C_ET` (`[D]`); and `h`, `I_0`
  themselves, which are external inputs on which every `c_k` value depends.
