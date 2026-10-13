# Preregistration — moment / localization routes to the upper half of Sharp EOC

**Committed before any test was run.** Every threshold, depth, sample size and seed below is
fixed here. Gates are not changed after seeing data; if a gate turns out to be ill-posed, the
original stays and a clearly labelled post-hoc variant is added in `FINDINGS.md`.

This is a **falsification-first pilot**. A clean negative result is a success. Nothing here bears
on (DE), divergent orbits, or Collatz; nothing here bears on the lower half of Sharp EOC.

Status labels: `[P]` proved · `[V]` verified by exact computation in this branch, for the stated
finite range only · `[F]` float / sampled diagnostic only · `[C]` conjectural / missing lemma ·
`[R]` refuted / negative result · `[D]` reported from earlier discussion, not re-checked.
**Labels are never upgraded.**

---

## 0. Conventions, and their source in this repository

Checked against the Lean libraries **before** this file was written. **No convention differs**
from the brief.

| convention | source in this repository | status |
|---|---|---|
| `s_j = d_0 + … + d_{j-1}`, `S = s_N` | `Occupation/Compositions.lean:37` `psum`, `:50` `psum_total` | matches |
| zero confinement `2^{s_j} <= 3^j` for all `j <= N` | `Occupation/Compositions.lean:62` `Confined 0`; `Descent/Basic.lean:29` `ConfinedUpTo`; `Divergence/CycleDrift.lean:30` `ZeroConfined` | matches, three independent definitions |
| carry `q_0 = 0`, `q_{j+1} = 3 q_j + 2^{s_j}` | `Divergence/Basic.lean:52` `C`, `:57` `C_succ` | matches |
| `A[k] = floor(k log2 3)` as `(3**k).bit_length() - 1` | `Occupation/Rate.lean:71` `sN k = Nat.log 2 (3^k)`, pinned by `:73`, `:76` | matches |
| realizer congruence `3^N m + q_N == 2^S (mod 2^{S+1})`, least realizer `r(D) < 2^{S+1}` | *absent here*; external `EOC/Realizer.lean` (`eoc-lean-verification`). Re-verified exactly in this branch | absent-here, verified `[V]` |
| additive form `r(D) == 3^{-N} 2^S - sum_{j<N} 3^{-(j+1)} 2^{s_j} (mod 2^{S+1})` | prior art: Lemma 2.1 / Def. 2.2 of *The Sturmian–Mahler Edge* (June 2026); EOC Rev 8 Prop. 5.2 | `[P]` prior art, re-verified `[V]` |

Constants: `alpha = log2 3 = 1.5849625…`; `h = alpha·H2(1/alpha) = 1.505644…` (**external input,
`[D]`**); `I_0 = alpha - h = 0.0793186…` (`[D]`, inherited from `h`).

## 0b. The object: `Z_N`

`Q = 2^{A[N]+1}`; `Z_N = { m < Q : m odd, m zero-confined through N steps }`; `M = |Z_N|`.

Built **from words, not by scanning integers**: each zero-confined word `D` of length `N` and
terminal sum `S` contributes the `2^{A[N]-S}` lifts of its least realizer `r(D)` to the common
modulus `Q`. Validation (preregistered, must pass or the run aborts):

- the weighting identity `sum_S |W(N,S)| · 2^{A[N]-S} == #{odd m < Q : confined N steps}` against an
  independent brute scan at `N = 8, 10, 12, 14`, with the reference counts
  **367 / 2114 / 27328 / 168807**;
- `Z_N` as built equals the brute-scan set, elementwise, at `N = 8, 10, 12, 14`;
- `min Z_N == r_min(N,0)` from an independent direct orbit scan, same depths.

**No single terminal shell is used for anything in this audit.** (The terminal-shell minimum
overestimated `r_min` by up to ~13x; prior round, `[V]`.)

`r_min(N,0) = min Z_N` is used throughout. Justification `[P]`: confinement through `N` steps
depends on `m` only through `m mod 2^{A[N]+1}` (since `S = s_N(m) <= A[N]`), and `Z_N` is nonempty,
so the least zero-confined odd integer is `< Q` and lies in `Z_N`.

---

## 1. Re-derivation of the moment exponent `c_k` (analytic; done before any computation)

Let `X_y = #(Z_N ∩ [y, y+H))` for `y` mod `Q`, `E = M H / Q`, `mu_k = mean_y (X_y - E)^k`, and let
`B = #{y : X_y = 0}`.

**Exceptional-set step `[P]`.** For even `k` every term of `sum_y (X_y - E)^k` is `>= 0`, and each
bad `y` contributes exactly `E^k`. Hence `B · E^k <= Q · mu_k`, i.e.

```
B  <=  Q · mu_k / E^k .
```

**Localization step `[P]`.** Among the `B+1` shifts `y = 0, 1, …, B` not all can be bad, so some
`y <= B` has `X_y >= 1`, giving an element of `Z_N` below `y + H <= B + H`. With
`r_min(N,0) = min Z_N` this is

```
r_min(N,0)  <=  B + H .
```

**Optimization step.** Assume Gaussian-sized moments `mu_k ≍ E^{k/2}` (`k` even) and write
`Q = 2^{alpha N}`, `M = 2^{h N}`, `H = 2^{cN}`, so `E = 2^{(c - I_0) N}`. Then

```
log2 B  ≈  alpha N + (k/2)(alpha - h - c) N .
```

`log2 B` decreases in `c` and `log2 H = cN` increases, so the optimum is where they are equal:

```
c (1 + k/2)  =  alpha (1 + k/2) - (k/2) h
c_k          =  alpha - k h / (k + 2)  =  (2 alpha + k I_0) / (k + 2) .
```

**The two forms are identical** — `(2 alpha + k(alpha - h))/(k+2) = (alpha(k+2) - k h)/(k+2)`.
**The brief's formula is therefore CORRECT as stated**, and reproduces:

| k | `c_k` |
|---|---|
| 2 | 0.832141 (the Fourier/Erdős–Turán ceiling of the previous round) |
| 4 | 0.581225 |
| 6 | 0.455727 |
| 8 | 0.380493 |
| → ∞ | `I_0 = 0.079319` |

**Two caveats recorded now, not after the fact.** (i) The argument needs `mu_k ≍ E^{k/2}` at
`H = 2^{c_k N}`, where `E = 2^{(c_k - I_0)N}` is *exponentially large*; the finite depths of this
audit test the hypothesis only at `E` of order `10`–`10^2`. (ii) Only even `k` is admissible
(odd central moments can be negative), so `k = 2, 4, 6` is the right test set.

## 1b. The variance identity to be verified (Test A.1)

To be stated `[P]` and checked numerically at small `N`:

```
sum_{y mod Q} (X_y - E)^2  =  (M^2 / Q) · sum_{h != 0} |F(h)|^2 · |W(h)|^2 ,
W(h) = sum_{t<H} e(-h t / Q),   |W(h)| = |sin(pi h H / Q) / sin(pi h / Q)| ,
F(h) = (1/M) sum_{m in Z_N} e(h m / Q) .
```

with the Parseval normalization `sum_{h mod Q} |F(h)|^2 = Q / M`, i.e. mean `|F(h)|^2 = 1/M`.
Pair form to be checked against it exactly: `sum_y X_y^2 = M H + sum_{m != m'} (H - d(m,m'))_+`,
`d` the circular distance, valid because `H <= Q/2` throughout.

---

## 2. Depths, windows, and how all-shift statistics are computed

**Primary depth set (fixed): `N = 8, 9, 10, …, 18`.** All gate fits use exactly this set.
**Extension depths `N = 19, 20`**: computed only if the script stays inside the budget
(< 10 min, < 1 GB); reported separately and **excluded from every fit**.

`c ∈ {0.70, 0.80, 0.90}`, `H = 2^{floor(cN)}`.

**All-shift statistics are computed EXACTLY at every depth, for every `Q`, by the event method:**
`X_{y+1} - X_y = [ (y+H) mod Q ∈ Z_N ] - [ y ∈ Z_N ]`, so `X_y` is piecewise constant in `y` with
at most `2M` breakpoints; walking the merged breakpoint list gives the exact integer histogram
`{ value v : #{y : X_y = v} }`, summing to `Q`. Cost `O(M log M)`, independent of `Q`.

This **supersedes** the brief's fallback ("all shifts if `Q <= 2^26`, otherwise `>= 10^6` random
shifts"): the fallback is not needed, since the exact all-shift distribution is reachable at every
depth in range. Moments `mu_2, mu_4, mu_6`, the bad-shift count `B`, `max_y X_y` and the percentile
of `X_0` are therefore **exact rationals** (`Fraction` with `E = MH/Q`), labelled `[V]`, not `[F]`,
and **no sampling enters Tests 0, A or B**. Sampling enters only Test C (word and frequency
samples) and the `R_2` frequency subsampling of §4, both labelled `[F]` with seed and size.

---

## 3. Gate 0 — is the window at zero typical? (anchor gate, run first)

Computed per `(N, c)`: exact `X_0 = #(Z_N ∩ [0,H))`; `E = MH/Q`; `rho_0 = X_0/E`; the exact
all-shift distribution of `X_y` and the exact percentile of `X_0` in it; exact `X_{kH}` for
`k = 0…63`; and `r_min(N,0)` with `log2 r_min / N`.

Fit: ordinary least squares of `log2 rho_0` against `N`, over the primary set `N = 8…18`, for each
`c` separately. Depths with `X_0 = 0` have `log2 rho_0` undefined and are **excluded from that
fit**, and their number is reported. Robustness refit: `N = 10…18` (drops the two smallest depths).

**Gate 0 outcome (three-way, fixed now):**

- **FAIL — "the window at zero is systematically depleted"**, record `[R]` for *"the window at zero
  is typical"*, iff `slope_c <= -0.02` for **every** `c ∈ {0.70, 0.80, 0.90}` in **both** the full
  (`8…18`) and trimmed (`10…18`) fits. Then the verdict for `r_min` on **all** moment routes is
  **STOP**: Tests A and B become moot for `r_min` and their numbers, if already computed, are
  recorded as statements about *typical* windows only.
- **PASS** iff `slope_c > -0.02` for every `c` in both fits.
- **MIXED** otherwise. Treated as PASS-with-flag (moment routes not stopped), and reported as
  MIXED with the individual slopes.

Additional reported quantity (not a gate): `max_N |log2 rho_0|` per `c`, as the "bounded factor"
diagnostic.

## 4. Gate A — pair collisions / low-frequency mass

`R_2(N,K) = (M/K) · sum_{0 < h <= K} |F(h)|^2`, over **all** `h` (odd and even, so the dyadic tower
is included), `K = ceil(Q/H)` for each `c`.

`F(h)` is computed by a **word-level DP with lift weights included**, vectorized over `h`
(complex128 → `[F]`). Preregistered exact structure to be used and verified: the lifts of a word of
terminal sum `S` contribute `2^{A-S}` times a geometric sum that **vanishes unless
`2^{A-S} | h`**, so

```
F(h) = (1/M) · sum_{S >= A[N] - v2(h)} 2^{A[N]-S} · T_S(h),
T_S(h) = sum_{D confined, s_N(D)=S} e(h r(D) / 2^{S+1}).
```

In particular for **odd** `h` only the terminal shell `S = A[N]` contributes. DP validation
(preregistered): against direct brute-force exponential sums over `Z_N` at `N = 8` and `N = 10`,
all `h <= 512` plus `h ∈ {Q/8, Q/4, Q/2}`; tolerance `1e-9` absolute on `|F(h)|`.

Frequency range: all `0 < h <= K` when `K <= 2^17`; otherwise a uniform random subsample of
`2^17` frequencies in `(0, K]`, **seed 20261014**, labelled sampled `[F]` with its size.

Pair counts, exact `[V]`: `P(N,H) = #{(m,m') ∈ Z_N^2, m != m', circular |m-m'| < H}` (ordered),
against the independence prediction `M^2 (2H-1)/Q`; excess ratio
`ratio_P = P(N,H) / (M^2 (2H-1)/Q)`.

**Gate A (fixed now):** record `[R]` for the pair-collision hypothesis iff, for **every**
`c ∈ {0.70,0.80,0.90}`, the OLS slope of `log2 R_2` against `N` over `N = 8…18` is `>= 0.03`
**or** the OLS slope of `log2 ratio_P` against `N` over the same set is `>= 0.03`. Otherwise mark
the pair-collision bound `[C]`, supported at the tested depths only.

## 5. Gate B — higher moments of window counts (only if Gate 0 passes)

Window choice rule, fixed now: for each `N`, let `w` range over integers with
`E(w) = M 2^w / Q ∈ [8, 512]`. All such `w` are reported. **The single series used for the gate fit
is the `w` whose `E` is closest to `64` in `log2`** (ties → the larger `w`).

Computed exactly over all shifts: `mu_2, mu_4, mu_6`; `tau_k = mu_k / E^{k/2}`; `max_y X_y / E`;
`B = #{y : X_y = 0}` against the Poisson prediction `Q e^{-E}`. Poisson reference central moments
of mean `E`: `mu_2 = E`, `mu_4 = E + 3E^2`, `mu_6 = E + 25E^2 + 15E^3`; hence
`tau_4^{Pois} = 3 + 1/E`, `tau_6^{Pois} = 15 + 25/E + 1/E^2`.

**Gate B (fixed now):** record `[R]` for "Gaussian-sized fourth moment", and with it for the
`c_4 ≈ 0.581` route, iff the OLS slope of `log2 tau_4` against `N` over `N = 8…18` (gate series) is
`>= 0.03` **or** `tau_4 > 10 · tau_4^{Pois}` at **both** of the two largest depths. Otherwise mark
it `[C]`, supported at the tested depths only.

Consistency check `[V]`, not a gate: at each depth confirm `r_min(N,0) <= B + H` and report the
slack `(B + H) / r_min`.

## 6. Gate C — swap-only cancellation rate

Swap `(1,2) <-> (2,1)` at position `j` leaves `s_j` and `s_{j+2}` fixed and moves `s_{j+1}` by one,
so by the additive form exactly one term changes and the realizer moves by
`-3^{-(j+2)} · 2^{s_j+1} (mod 2^{S+1})` for the `(1,2) -> (2,1)` direction. Hence, with `Q_S = 2^{S+1}`,

```
phi_j(h)  =  ( - h · 3^{-(j+2)} · 2^{s_j + 1}  mod  Q_S ) / Q_S    ∈ [0,1),
bits(D,h) =  -(1/N) · sum_{j in J(D)} log2 |cos(pi phi_j(h))| .
```

A site `j` is **usable** iff `{d_j, d_{j+1}} = {1,2}` and **both** orientations are zero-confined,
which (since only `s_{j+1}` moves) is exactly `s_j + 2 <= A[j+1]`. `J(D)` is a maximal disjoint set
of usable sites chosen **greedily left to right** (take the leftmost usable `j`, then continue from
`j+2`).

Ensemble, fixed now: **primary** — uniform over zero-confined words of length `N` with terminal sum
`S = A[N]` (the terminal shell, modulus `Q_S = 2^{A[N]+1}`), sampled by the counting DP. The
terminal shell is the primary ensemble because, by §4, the **odd-frequency** Fourier coefficients of
`Z_N` are supported there exactly. **Secondary** — uniform over zero-confined words of length `N`
of *any* terminal sum, each with its own modulus `2^{S+1}`; same seed and sample size, reported
alongside.

Depths `N ∈ {20, 30, 40}`; **256 base words** per depth per ensemble (`>= 200`), **seed 20261013**;
frequencies: **all 512 odd `h <= 1024`** plus **256 random odd `h < Q_S`**, **seed 20261014**.
Reported: mean, median and 10th percentile of `bits(D,h)` per step, and the average number of
usable disjoint sites per step.

**Gate C (fixed now):** record `[R]` for "local swaps alone supply the needed cancellation" iff the
**median** `bits` per step is `< 0.3` at **every** tested depth (about half of the `alpha - 1 =
0.585` needed merely to beat `c = 1`; full square-root is `h/2 = 0.753`). The Tao-style swap
mechanism is then closed as a *sufficient* route. This **does not refute Lemma D1** — only this
mechanism for it.

---

## 7. Budget and reproducibility

Python 3 standard library plus `numpy` (already installed, 1.26.4 — nothing is installed). Each
script: `--quick` flag, under ~10 minutes, under ~1 GB, prints to stdout only, exits non-zero on
any failed assertion. Transcripts of full runs in `results/`.

Exact integer (or `Fraction`) arithmetic decides every membership, count, congruence and moment.
Floats appear only in: Fourier values `|F(h)|` and `R_2` (§4), the `bits` statistics of §6, and OLS
slopes — all `[F]`.

Seeds: **20261013** (word sampling, Test C), **20261014** (frequency sampling, Tests A and C).

## 8. No novelty claims

Nothing in this audit bears on (DE), on divergent orbits, on universal drift exit, or on Collatz;
nothing bears on the lower half of Sharp EOC. The additive realizer formula is prior art (§0).
Finite depths do not establish exponential laws.
