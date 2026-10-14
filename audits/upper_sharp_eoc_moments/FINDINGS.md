# Findings — moment / localization routes to the upper half of Sharp EOC

One result per section, each with exactly one status label. Gates and thresholds were fixed in
[`PREREGISTRATION.md`](PREREGISTRATION.md) and committed before any script was run
(commit `226f38a`); **no gate was changed after seeing data**.

| label | meaning |
|---|---|
| `[P]` | proved, with cited inputs |
| `[V]` | verified by exact computation in this branch, **for the stated finite range only** |
| `[F]` | float / sampled diagnostic only |
| `[C]` | conjectural / missing lemma |
| `[R]` | refuted / negative result |
| `[D]` | reported from earlier discussion or an earlier branch, not re-checked here |

**Labels are never upgraded.** Throughout: `alpha = log2 3 = 1.5849625…`; `A[N] = floor(N alpha)`;
`Q = 2^{A[N]+1}`; `Z_N = {m < Q : m odd, zero-confined through N steps}`; `M = |Z_N|`;
`X_y = #(Z_N cap [y, y+H))`; `E = M H/Q`; `F(h) = (1/M) sum_{m in Z_N} e(h m/Q)`.
`h = 1.505644…` and `I_0 = alpha - h = 0.0793186…` are **external inputs, `[D]`**; every
statement whose numerical value depends on them inherits that `[D]`.

---

## 0. Conventions — all match this repository

Checked before anything was written; **no convention differs** from the brief. `[V]`

| convention | source in this repository |
|---|---|
| `s_j = d_0+…+d_{j-1}`, `S = s_N` | [`Occupation/Compositions.lean:37`](../../Occupation/Compositions.lean) `psum`, `:50` `psum_total` |
| zero confinement `2^{s_j} <= 3^j`, `j <= N` | [`Occupation/Compositions.lean:62`](../../Occupation/Compositions.lean) `Confined 0`; [`Descent/Basic.lean:29`](../../Descent/Basic.lean) `ConfinedUpTo`; [`Divergence/CycleDrift.lean:30`](../../Divergence/CycleDrift.lean) `ZeroConfined` |
| carry `q_0 = 0`, `q_{j+1} = 3 q_j + 2^{s_j}` | [`Divergence/Basic.lean:52`](../../Divergence/Basic.lean) `C`, `:57` `C_succ` |
| `A[k] = (3**k).bit_length() - 1` | [`Occupation/Rate.lean:71`](../../Occupation/Rate.lean) `sN k = Nat.log 2 (3^k)`, pinned by `:73`, `:76` |

Absent here and taken from outside, as in the previous round: the realizer congruence and least
realizer (external `EOC/Realizer.lean`), re-verified exactly here; and the **additive form**
`r(D) == 2^S - sum_{j<N} 3^{-(j+1)} 2^{s_j} (mod 2^{S+1})`, which is **prior art** — Lemma 2.1 /
Definition 2.2 of *The Sturmian–Mahler Edge* (June 2026) and EOC Rev 8 Proposition 5.2. `[P]`/`[D]`

## 0b. The object `Z_N`, and that its minimum is `r_min(N,0)`

**`[P]`** Zero confinement through `N` steps depends on `m` only through `m mod 2^{A[N]+1}`,
because `S = s_N(m) <= A[N]` for a confined `m`; and `Z_N` is nonempty. Hence the least
zero-confined odd integer is `< Q`, lies in `Z_N`, and

```
r_min(N,0)  =  min Z_N .
```

**`[V]`** `Z_N` is built **from words with lift weights** — a word of terminal sum `S` contributes
the `2^{A[N]-S}` lifts of `r(D)` to the common modulus `Q`. **No single terminal shell is used
anywhere in this audit.** Validation, all passing (`scripts/check_zn.py`,
`results/check_zn.txt`):

- the weighting identity against an independent brute orbit scan at `N = 8, 10, 12, 14`:
  **367 / 2114 / 27328 / 168807**, matching the reference counts, *and* `Z_N` equals the
  brute-scan set **elementwise** at those depths; all elements odd, distinct, `< Q`;
- `min Z_N == r_min(N,0)` from an independent direct ascending orbit scan;
- the exact all-shift histogram against a brute all-`y` computation, with the invariants
  `sum counts = Q` and `sum_y X_y = M H`;
- exact pair statistics against brute `O(M^2)`, and the exact identity of §A3;
- `[F]` the word-level Fourier DP against direct exponential sums: max deviation **2.6e-16**
  (preregistered tolerance `1e-9`).

## 0c. New structural fact: for odd `h`, `F(h)` lives on the terminal shell alone

**`[P]`** The `2^{A-S}` lifts of one word contribute
`sum_{t<2^{A-S}} e(h(r + t 2^{S+1})/Q) = e(hr/Q) 2^{A-S} [2^{A-S} | h]` — a geometric sum that
**vanishes unless `2^{A-S} | h`** — and when `2^{A-S} | h`, writing `h = 2^{A-S} h'` gives
`e(hr/Q) = e(h' r/2^{S+1})`. Hence

```
F(h) = (1/M) sum_{S >= A[N]-v2(h)} 2^{A[N]-S} T_S(h/2^{A[N]-S}),
T_S(u) = sum_{D : s_N(D)=S} e(u r(D)/2^{S+1}),
```

and in particular **for odd `h` only the terminal shell `S = A[N]` contributes**, with `h' = h`.

**`[V]`/`[F]`** Verified against the direct sum over `Z_N` at `N = 8, 10, 12` over 128 odd `h`:
max deviation `6.9e-17`. The shell's share `M_shell/M` is `0.2316 / 0.2252 / 0.0970`.
`check_zn.py` §6. This is why the terminal shell is the primary ensemble of Test C, and it
explains the measured odd-`h` share of the low-frequency mass in §A4 (`0.07`–`0.24`).

---

## 1. The `c_k` formula — re-derived, and the brief's version is CORRECT

**`[P]` Exceptional-set step.** For even `k` every term of `sum_y (X_y-E)^k` is `>= 0` and each
bad shift (`X_y = 0`) contributes exactly `E^k`, so with `B = #{y : X_y = 0}`

```
B  <=  Q mu_k / E^k .
```

**`[P]` Localization step.** Among the `B+1` shifts `y = 0,…,B` not all are bad, so some window
starting at `y <= B` contains a seed, and by §0b

```
r_min(N,0)  <=  B + H .
```

**Optimization.** With `mu_k ≍ E^{k/2}`, `Q = 2^{alpha N}`, `M = 2^{hN}`, `H = 2^{cN}`,
`E = 2^{(c-I_0)N}`: `log2 B ≈ alpha N + (k/2)(alpha - h - c)N`, which decreases in `c` while
`log2 H = cN` increases, so the optimum balances them:

```
c_k  =  alpha - k h/(k+2)  =  (2 alpha + k I_0)/(k+2) .
```

**The two forms are algebraically identical**, so **the brief's formula is correct as stated**
(`(2 alpha + k I_0)/(k+2) = (alpha(k+2) - k h)/(k+2)`), and reproduces `c_2 = 0.832141`,
`c_4 = 0.581225`, `c_6 = 0.455727`, `c_8 = 0.380493`, `c_k -> I_0`. Numerical values inherit
`[D]` from `h`.

**Two caveats, recorded in the preregistration before any run.** (i) The argument needs
`mu_k ≍ E^{k/2}` at `H = 2^{c_k N}`, where `E = 2^{(c_k - I_0)N}` is *exponentially large*; this
audit tests the hypothesis only at `E ≈ 10^1`–`10^2`. (ii) Only even `k` is admissible.

---

## Test 0 — the anchor gate

### 0.1 `r_min(N,0) = 27` across the entire audit range `[V]`

`scripts/test0_anchor.py` §1, `scripts/rmin_orientation.py`.

| N | 8 | 10 | 12 | 14 | 16 | 18 | 20 |
|---|---|---|---|---|---|---|---|
| `M = \|Z_N\|` | 367 | 2,114 | 27,328 | 168,807 | 1,037,374 | 6,385,637 | 41,347,483 |
| `log2 M/N` | 1.0650 | 1.1046 | 1.2282 | 1.2404 | 1.2490 | 1.2559 | 1.2651 |
| `r_min(N,0)` | 27 | 27 | 27 | 27 | 27 | 27 | 27 |
| `log2 r_min/N` | 0.5944 | 0.4755 | 0.3962 | 0.3396 | 0.2972 | 0.2642 | 0.2377 |

Extended past the audit range, exactly `[V]` (`rmin_orientation.py`): `r_min(N,0) = 3` (`N=1`),
`7` (`N=2–3`), **`27` (`N=4–36`)**, `703` (`N=37–50`), `10087` (`N=51–65`), `35655` (`N=66–70`);
the zero-confinement depths of `27, 703, 10087` are `36, 50, 65`. `log2 r_min/N` at plateau ends:
`0.1321, 0.1891, 0.2046, 0.2160`.

**Consequence for the whole audit.** The audit depths `N = 8…20` lie **entirely inside the
`r_min = 27` plateau**. At those depths `r_min(N,0) <= 2^{cN}` holds for every `c >= 0.2377`, so
the finite data **cannot discriminate between candidate exponents at all**. What this audit can
measure is each **method's loss**, never the truth.

### 0.2 Gate 0 as preregistered: FAIL — and the gate is ill-posed `[R]`/`[F]`

`test0_anchor.py` §4. OLS slope of `log2 rho_0` against `N`, `rho_0 = X_0/E`:

| c | slope `N=8…18` | slope `N=10…18` | `#(X_0=0)` | `max\|log2 rho_0\|` | verdict(c) |
|---|---|---|---|---|---|
| 0.70 | −0.09425 | −0.15727 | 0 | 1.1283 | depleted |
| 0.80 | −0.09244 | −0.12065 | 0 | 0.9356 | depleted |
| 0.90 | −0.06940 | −0.05697 | 0 | 0.6503 | depleted |

All three slopes clear the `-0.02` gate in both fits, so **by the preregistered criterion Gate 0
FAILS** and `[R]` is recorded for *"the window at zero is typical"*. **This verdict stands as
recorded.**

**The gate is nevertheless ill-posed for the shape the data actually has**, and this is reported
rather than repaired. `rho_0` starts **above** 1 and **relaxes to 1**:

| c | `rho_0`, N=8 | N=10 | N=12 | N=14 | N=16 | N=17 | N=18 | N=19 | N=20 |
|---|---|---|---|---|---|---|---|---|---|
| 0.70 | 1.3951 | 1.9376 | 1.9485 | 1.4559 | 0.9476 | 1.0041 | 1.0058 | 1.0312 | 1.0207 |
| 0.80 | 1.3951 | 1.6954 | 1.3489 | 1.0191 | 0.9476 | 0.9762 | 0.9853 | 0.9924 | 1.0033 |
| 0.90 | 1.5695 | 1.2715 | 1.1616 | 0.9827 | 0.9792 | 0.9901 | 0.9955 | 0.9924 | 1.0053 |

An OLS slope taken across that transient cannot distinguish *"relaxes to 1 from above"* from
*"decays exponentially"*: both give a negative slope. The failure is therefore an artifact of
the gate's functional form, not evidence of depletion.

### 0.3 Post-hoc variant — NOT PREREGISTERED — the window at zero is typical `[F]`

`test0_anchor.py` §5. Criteria stated in the script before being read: late-depth slope,
`|log2 rho_0|` at `N >= 16`, and the two extension depths (excluded from every fit).

| c | slope `N=14…18` | `max\|log2 rho_0\|`, `N>=16` | `rho_0` at `N=19,20` |
|---|---|---|---|
| 0.70 | −0.12546 | 0.0776 | 1.0312, 1.0207 |
| 0.80 | −0.00911 | 0.0776 | 0.9924, 1.0033 |
| 0.90 | **+0.00963** | 0.0303 | 0.9924, 1.0053 |

Supporting exact quantities: the percentile of `X_0` in the exact all-shift distribution falls
from `0.97`–`0.999` at `N <= 12` to `0.3808`–`0.5227` at `N = 18` — `X_0` moves from being a high
outlier to being typical; and over the 64 aligned windows `y = kH` (`k = 0…63`) at `N = 18`,
`c = 0.90`, the counts run `729`–`816` against `E = 779.50`, with no empty window
(`test0_anchor.py` §3).

**Reading `[F]`.** At `N = 16…20` the window at zero is **typical**, not depleted: `rho_0` is
within `0.95`–`1.01` for every `c`. Finite range `N <= 20`; this does not exclude depletion at
large `N`.

---

## Test A — pair collisions and low-frequency mass

### A1 The variance identity `[P]`, verified exactly `[V]`/`[F]`

**`[P]`** Writing the window indicator in characters,
`X_y = (1/Q) sum_h M F(h) W(h) e(-hy/Q)` with `W(h) = sum_{t<H} e(-ht/Q)`, `W(0) = H`, so the
`h = 0` term is exactly `E` and Parseval over `y` gives

```
sum_{y mod Q} (X_y - E)^2  =  (M^2/Q) sum_{h != 0} |F(h)|^2 |W(h)|^2 ,
      |W(h)| = |sin(pi h H/Q)/sin(pi h/Q)| ,
```

together with the normalization `sum_{h mod Q} |F(h)|^2 = Q/M`, i.e. **mean `|F(h)|^2 = 1/M`**
(this is the brief's Parseval statement; re-derived and confirmed). Since `|W(h)|^2 ≈ H^2` for
`|h| <~ Q/H` and decays above, the variance **is** the low-frequency mass.

**`[V]`/`[F]`** Verified over **all** `h` by FFT against the exact integer variance at
`N = 8, 10, 12`, `H = 2^4, 2^6`: relative deviation `<= 2.8e-15`; Parseval deviation `<= 1.1e-16`.
`testA_pairs.py` §1. (`numpy.fft` uses the `e^{-2pi i}` convention, the conjugate of `F`; noted in
the script after it caused a false alarm in the DP cross-check.)

### A2 `R_2` does not grow `[F]`

`R_2(N,K) = (M/K) sum_{0<h<=K} |F(h)|^2`, over **all** `h` in `(0,K]` (odd and even — the dyadic
tower is included), `K = ceil(Q/H)`. No subsampling was needed: `K <= 2^17` throughout. Under
near-independence `R_2 = O(poly N)`; measured values are `O(1)` and **slightly decreasing**:

| c | `R_2`, N=8 | N=12 | N=14 | N=16 | N=18 | OLS slope `log2 R_2` |
|---|---|---|---|---|---|---|
| 0.70 | 0.73449 | 0.59873 | 0.59624 | 0.49202 | 0.51798 | −0.03413 |
| 0.80 | 0.51015 | 0.53630 | 0.44182 | 0.42552 | 0.49350 | −0.02980 |
| 0.90 | 0.42761 | 0.38831 | 0.33741 | 0.38293 | 0.47556 | −0.00808 |

Odd-`h` share of the mass: `0.07`–`0.24`, consistent with `M_shell/M` of §0c.

### A3 Exact pair counts: the seed set is **underdispersed** `[V]`

`P(N,H) = #{(m,m') in Z_N^2, m != m', circular |m-m'| < H}` (ordered), against the preregistered
independence prediction `M^2(2H-1)/Q`; and the dispersion index `mu_2/E` (`= 1` for Poisson).
Exact integers / Fractions, all depths `N = 8…18`, all three `c` (`testA_pairs.py` §4):

| quantity | range over the 33 `(N,c)` cells | at `N = 18` |
|---|---|---|
| `ratio_P` | 0.6758 … **0.9993**, **never above 1** in any of the 33 cells | 0.9917 / 0.9977 / 0.9993 |
| `mu_2/E` | **0.2602 … 0.5455** | 0.4994 / 0.4845 / 0.4486 |

Also verified exactly at every cell: `sum_y X_y^2 = M H + sum_{m != m'} (H - d)_+` with `d` the
circular distance (valid as `H <= Q/2`). **Pairs of seeds within distance `H` are *rarer* than
independence predicts, and window counts fluctuate at *about half* the Poisson variance or less.**
(The commit message of `6507c3b` quotes this range as `0.30`–`0.50`; the exact range over all 33
cells is `0.2602`–`0.5455`, as printed in `results/testA_pairs.txt`. The table here is the
authoritative one.)

### A4 Gate A: not refuted — `[C]`

`testA_pairs.py` §5. The gate fires only if, for **every** `c`, the slope of `log2 R_2` **or** of
`log2 ratio_P` reaches `+0.03`:

| c | slope `log2 R_2` | slope `log2 ratio_P` | fires? |
|---|---|---|---|
| 0.70 | −0.03413 | +0.04114 | yes |
| 0.80 | −0.02980 | +0.02290 | no |
| 0.90 | −0.00808 | +0.01271 | no |

So **Gate A does not fire: the pair-collision bound is marked `[C]`, supported at the tested
depths only.** Note the positive `ratio_P` slopes are the approach to `1` **from below** (A3), not
clustering; reading them as growth would be the same artifact as Gate 0's.

---

## Test B — higher moments of window counts

All moments **exact over all shifts** as `Fraction`s, `N = 8…18`; the gate series is the window
with `E` closest to `64` (preregistered). `testB_moments.py`.

### B1 Gate B as preregistered: `[R]` — and the gate is ill-posed in the same way

| N | 8 | 11 | 13 | 15 | 16 | 17 | 18 |
|---|---|---|---|---|---|---|---|
| `E` | 45.88 | 58.56 | 45.52 | 69.97 | 63.32 | 53.78 | 48.72 |
| `tau_2 = mu_2/E` | 0.0926 | 0.2778 | 0.3361 | 0.3613 | 0.3994 | 0.4619 | 0.4994 |
| `tau_4 = mu_4/E^2` | 0.0260 | 0.2580 | 0.3384 | 0.3844 | 0.4682 | 0.6243 | 0.7313 |
| `tau_4 / tau_4^{Pois}` | 0.0086 | 0.0855 | 0.1120 | 0.1275 | 0.1552 | 0.2068 | **0.2421** |
| `tau_6 = mu_6/E^3` | 0.0110 | 0.4003 | 0.5676 | 0.6711 | 0.8997 | 1.3751 | 1.7461 |
| `tau_6 / tau_6^{Pois}` | 0.0007 | 0.0260 | 0.0365 | 0.0437 | 0.0584 | 0.0889 | **0.1126** |

OLS slope of `log2 tau_4` over the gate series: **+0.47056 >= 0.03**, so **by the preregistered
criterion Gate B records `[R]`** for "Gaussian-sized fourth moment", and with it for the
`c_4 ≈ 0.581` route. **This verdict stands as recorded.** (The second trigger did *not* fire:
`tau_4 = 0.624, 0.731` against `10 x` Poisson `= 30.19, 30.21` at the two largest depths.)

**The gate is ill-posed in exactly the way Gate 0 was**: `tau_4` rises `0.026 -> 0.731` while its
Poisson reference is `≈ 3.02`, i.e. it **relaxes upward toward** the Gaussian scale from far below
and **never exceeds it**. A slope on `log2 tau_4` across that transient cannot distinguish
"approaches the predicted constant" from "diverges".

### B2 Post-hoc variant — NOT PREREGISTERED — the fourth moment is Gaussian-shaped `[F]`

`testB_moments.py` §5. Criteria stated before being read: `tau_4` versus its Poisson reference at
every depth; the shape ratio `tau_4/(3 tau_2^2)`, which is `1` for a locally Gaussian field of
*any* dispersion; and the slope over the last five depths.

- `tau_4 <= tau_4^{Pois}` at **every** tested depth (ratio `0.0086`–`0.2421`): it is never above.
- `tau_4/(3 tau_2^2) = 0.8498 … 1.1145` over all 11 depths (`0.9774` at `N = 18`).
- slope of `log2 tau_4` over the last five depths: `+0.35341`.

**Reading `[F]`.** The fourth moment is **Gaussian-shaped**, with a dispersion `tau_2` that is
itself still rising toward `1` (`0.093 -> 0.499`). At these depths the data are **consistent with
the Gaussian-sized fourth moment the `c_4` route needs**, not with its failure. Finite range
`N <= 18`.

### B3 The exceptional set is empty, and the bound is loose `[V]`

| N | `H` | `B = #{y : X_y = 0}` | `B + H` | `r_min` | largest cyclic gap `G` | `(B+H)/r_min` |
|---|---|---|---|---|---|---|
| 8 | 1024 | 0 | 1024 | 27 | 92 | 37.9 |
| 13 | 2048 | 0 | 2048 | 27 | 340 | 75.9 |
| 18 | 4096 | 0 | 4096 | 27 | 1056 | 151.7 |

`B = 0` at **every** depth and every gate window (Poisson predicts `Q e^{-E} <= 3.7e-13`), so
`r_min <= B + H` holds trivially and **every** window of length `H` contains a seed. The
consistency check `r_min <= B + H` passes at every cell, loose by `37.9`–`151.7x`.

### B4 Post-hoc `[V]` — the covering-radius exponent, which is what the route is really bounding

`r_min(N,0) <= G - 1` holds exactly (`G` = largest cyclic gap of `Z_N`), so `log2 G/N` upper-bounds
what **any** localization argument of this shape could deliver:

| N | 8 | 10 | 12 | 14 | 16 | 17 | 18 |
|---|---|---|---|---|---|---|---|
| `G` | 92 | 168 | 232 | 400 | 640 | 840 | 1056 |
| `log2 G/N` | 0.8154 | 0.7392 | 0.6548 | 0.6174 | 0.5826 | 0.5714 | **0.5580** |

OLS slope of `log2 G/N` against `N`: `-0.02510` per step `[F]`. **At `N = 18` the measured
covering radius is already `0.5580`, below `c_4 = 0.5812` and far below the Fourier ceiling
`c_2 = 0.8321`** — and the truth, `log2 r_min/N = 0.2642`, is far below both. Finite range only.

---

## Test C — swap-only cancellation

### C1 The swap phase, derived `[P]`

A swap at position `j` exchanges `(d_j,d_{j+1}) = (1,2) <-> (2,1)`. It leaves `s_j` and
`s_{j+2} = s_j+3` fixed and moves `s_{j+1}` by one, so in the additive form **exactly one summand
changes** — the one with index `j+1` — and `r` moves by `-3^{-(j+2)} 2^{s_j+1} (mod 2^{S+1})` in
the `(1,2) -> (2,1)` direction; `S`, hence the modulus, is unchanged. Averaging over the two
orientations multiplies the character by `(1 + e(phi_j))/2`, of modulus `|cos(pi phi_j)|`, with
`Q_S = 2^{S+1}` and

```
phi_j(h)  =  ( - h * 3^{-(j+2)} * 2^{s_j+1}  mod  Q_S ) / Q_S ,
bits(D,h) =  -(1/N) sum_{j in J(D)} log2 |cos(pi phi_j(h))| .
```

A site is **usable** iff `{d_j,d_{j+1}} = {1,2}` and both orientations are zero-confined, which —
since only `s_{j+1}` moves — is exactly **`s_j + 2 <= A[j+1]`**.

### C2 Structural facts, and a correction to my own first derivation `[P]`

- For a usable site `s_j + 3 = s_{j+2} <= S`, so `S - s_j >= 3`; and for **odd** `h`,
  `v2(h 3^{-(j+2)} 2^{s_j+1}) = s_j+1`, so `phi_j` is an **odd multiple of `2^{-(S-s_j)}` with
  `S - s_j >= 3`**. In particular `phi_j` is never `0` and never `1/2`: **one swap can neither
  leave the character untouched nor annihilate it.** (Both asserted exactly in the script.)
- **Correction.** My first draft asserted a universal per-site ceiling of
  `-log2 cos(3 pi/8) = 1.386` bits, on the ground that `phi_j` has denominator `>= 8`. **That is
  wrong** — an odd multiple of `2^{-k}` can lie within `2^{-k}` of `1/2` (`7/16`) — and the
  assertion duly failed at `N = 30`. The corrected statement: `|cos(pi phi_j)|` is bounded below
  only by `sin(pi 2^{-(S-s_j)})`, so per-site bits are bounded only by about
  `(S - s_j) - log2 pi`, i.e. **not `O(1)`**. That heavy right tail is why the gate statistic is
  the **median**.
- **Disjointness** gives at most `N/2` disjoint sites: density `nu <= 0.5` per step.
- For `phi` uniform on `[0,1)`, `E[-log2|cos(pi phi)|] = 1` bit exactly (because
  `int_0^1 log|2 cos(pi x)| dx = 0`) and the **median is `0.5` bits** (`|cos(pi phi)| < 2^{-1/2}`
  on a set of measure exactly `1/2`).
- **Hence, for equidistributed phases, swap-averaging delivers about `nu <= 0.5` bits per step in
  the mean — short of the `alpha - 1 = 0.58496` needed merely to beat `c = 1`, even at the
  maximal site density.** This is a structural ceiling, independent of measurement.

### C3 Measurements `[F]` — and they match the structure

256 base words per depth per ensemble (seed `20261013`); all 512 odd `h <= 1024` plus 256 random
odd `h < Q_S` (seed `20261014`). Primary ensemble = the terminal shell (where odd-`h` Fourier
coefficients live, §0c); secondary = all terminal sums.

| N | usable pairs/word | disjoint sites/word | `nu` | mean bits/step | **median** | p10 | p90 | max | per-site median |
|---|---|---|---|---|---|---|---|---|---|
| 20 | 5.555 | 3.891 | 0.1945 | 0.1910 | **0.1613** | 0.0324 | 0.3891 | 1.2874 | 0.5044 |
| 30 | 8.484 | 5.844 | 0.1948 | 0.1941 | **0.1742** | 0.0573 | 0.3574 | 0.9863 | 0.5032 |
| 40 | 11.395 | 7.570 | 0.1893 | 0.1886 | **0.1735** | 0.0706 | 0.3264 | 0.9081 | 0.5012 |

Secondary ensemble agrees to within `0.01` on every statistic (`nu = 0.1953, 0.1960, 0.2019`;
medians `0.1613, 0.1744, 0.1850`). The **per-site median is `0.501`–`0.504` against the
uniform-phase prediction `0.5`**, and the **mean bits per step equals `nu x 1 bit`** to three
decimals — the phases behave as equidistributed, exactly as §C2 assumes.

### C4 Gate C: `[R]` — the swap mechanism is closed as a sufficient route

| N | median bits/step | fraction of `alpha-1 = 0.58496` | fraction of `h/2 = 0.75282` |
|---|---|---|---|
| 20 | 0.1613 | 0.2758 | 0.2143 |
| 30 | 0.1742 | 0.2978 | 0.2314 |
| 40 | 0.1735 | 0.2966 | 0.2305 |

Median bits per step is below `0.3` at **every** tested depth, so **`[R]` is recorded for "local
swaps alone supply the needed cancellation"**. The measured rate is `≈ 30%` of what is needed
merely to beat `c = 1` and `≈ 23%` of full square root; the binding constraint is the **site
density** `nu ≈ 0.19`, which is itself capped at `0.5` by disjointness.

**This does NOT refute Lemma D1.** It closes only this mechanism for it. `h/2 = 0.75282` inherits
`[D]`.

---

## Items still `[C]` or `[D]`

| item | label | note |
|---|---|---|
| Lemma D1 (square-root cancellation at odd `h`) | `[C]` | untouched by this audit; inherited from the previous round |
| Lemma D2 (graded dyadic version) | `[C]` | untouched |
| the pair-collision bound / near-independence | `[C]` | Gate A did not fire; supported at `N = 8…18` only (§A2–A4) |
| Gaussian-sized `mu_4` (the `c_4` route's hypothesis) | `[C]` | preregistered Gate B recorded `[R]`; the post-hoc reading supports it at `N <= 18` (§B1–B2) |
| `h = 1.505644…`, `I_0 = 0.0793186…` | `[D]` | external inputs; `c_k`, `0.58496`, `0.75282`, `0.8321`, `0.5812` all inherit it |
| the additive realizer formula as prior art | `[P]`/`[D]` | Sturmian–Mahler Edge Lemma 2.1 / EOC Rev 8 Prop. 5.2, cited not re-confirmed here |
| realizer congruence / least realizer in Lean | `[D]` | external `EOC/Realizer.lean`; the arithmetic is re-verified exactly here, the Lean statement is not |
| the previous round's Fourier findings (ceiling `c ≈ 0.832`, `13.3x` shell overestimate, `C_ET`) | `[D]` | not re-checked here, except the lift-weighting identity, which is re-verified `[V]` |
| the `N^{-3/2}` count asymptotic and the `log2 M/N -> h` limit | `[D]` | used only as context for finite-size bias |

## Reproduction

```
cd audits/upper_sharp_eoc_moments/scripts
python3 check_zn.py           # [V] construction + machinery validation   (~14 s)
python3 test0_anchor.py       # Test 0, the anchor gate                   (~11 s)
python3 testA_pairs.py        # Test A, pairs and low-frequency mass      (~9 s)
python3 testB_moments.py      # Test B, higher moments                    (~4 s)
python3 testC_swaps.py        # Test C, swap cancellation                 (~3 s)
python3 rmin_orientation.py   # [V] exact r_min plateaux, orientation     (~0.2 s)
```

Python 3 standard library plus `numpy` (1.26.4, already installed — nothing was installed). Each
script takes `--quick`, prints to stdout only, writes nothing, and exits non-zero on any failed
assertion. Measured peak resident set (`/usr/bin/time -l`), all **under the 1 GB budget**:

| script | time | peak RSS |
|---|---|---|
| `check_zn.py` | 2.0 s | 252 MB |
| `test0_anchor.py` | 4.0 s | 691 MB |
| `testA_pairs.py` | 10.1 s | 959 MB |
| `testB_moments.py` | 6.7 s | 785 MB |
| `testC_swaps.py` | 2.9 s | 145 MB |
| `rmin_orientation.py` | 0.1 s | 32 MB |

Reaching that needed three fixes made **after** the results were first produced; all of them are
memory-only and **every transcript except `check_zn.txt` is byte-identical before and after**
(`check_zn.txt` changed only because the brute `O(M^2)` pair check, which cost 6.9 GB at `N = 12`,
was restricted to `M <= 2500`, i.e. to `N <= 10`, where it had already passed):
`window_hist` now sorts one packed `position*2 + tag` array in place and assembles the histogram
from position differences (1.35 GB → 0.2 GB at `N = 18`); `pair_stats` streams over `Z_N` in
chunks instead of holding a dozen full-length arrays; and `build_Z` writes residues straight into
preallocated per-shell arrays. The extension depths `N = 19, 20` never build `Z_N` at all —
`M` comes from the counting DP and `X_0`, `r_min` from direct orbit scans, which also gives an
**independent cross-check of `X_0` at every primary cell** (`test0_anchor.py` §2, passing).
`window_hist` was re-verified against a brute all-`y` reference on every `(N, H)` with
`N <= 12`, `H = 2^2…2^9`, after the rewrite.

The all-shift histogram is computed only for `M <= 8e6`, the documented budget rule. Full
transcripts: [`results/`](results/) — every number quoted above appears in one of them.
