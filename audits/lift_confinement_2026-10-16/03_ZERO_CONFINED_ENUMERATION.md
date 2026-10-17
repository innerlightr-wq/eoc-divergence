# 03_ZERO_CONFINED_ENUMERATION.md

## Confinement enforced exactly, at every prefix

`confined(d)` tests `(1<<S[k]) <= 3**k` for **every** `k = 1..N` with Python integers — no
floating point.  `cap(k)` is computed by integer doubling, not by `floor(k*log2(3))`.

`d_0 = 1` is forced at every length: `d_0 ≥ 1` and `2^{d_0} ≤ 3`.

| `N` | cap `S_N` | **# zero-confined words** | `S_N` range |
|---|---|---|---|
| 4 | 6 | 7 | 4..6 |
| 6 | 9 | 30 | 6..9 |
| 8 | 12 | 173 | 8..12 |
| 10 | 15 | 961 | 10..15 |
| 11 | 17 | 2 652 | 11..17 |
| 12 | 19 | 8 045 | 12..19 |
| 13 | 20 | 17 637 | 13..20 |
| 14 | 22 | 51 033 | 14..22 |

**For contrast:** the superseded October 16 run used `N = 11`, `S_N = 22` — outside the table
entirely, since the cap at `N = 11` is `17`.

## Lift statistics on the full enumeration

`J(N) = Σ_{n=1}^{N−1} ℓ_n`, every confined word of that length counted once.

| `N` | #words | mean `J` | `J/N` | `J/S_N` | mean max plateau | **min `J`** | **max `J`** |
|---|---|---|---|---|---|---|---|
| 7 | 85 | 5.082 | 0.847 | 0.514 | 0.729 | **3** | **6** |
| 9 | 476 | 6.336 | 0.792 | 0.491 | 1.254 | **3** | **8** |
| 11 | 2 652 | 7.601 | 0.760 | 0.478 | 1.641 | **3** | **10** |
| 13 | 17 637 | 8.883 | 0.740 | 0.466 | 1.872 | **3** | **12** |

> **`min J(N) = 3` for every `N = 6..13`, and `max J(N) = N−1` at every `N`.**

## Negative control: the all-ones word `[PROVED]`

For `d ≡ 1`: `S_n = n`, `C_n = Σ_{j<n}3^{n−1−j}2^j = 3^n − 2^n`, so
`r_n ≡ −(3^n−2^n)3^{−n} ≡ −1 (mod 2^n)`, i.e. `r_n = 2^n − 1`, `b_n = 1` for all `n`,
`J(N) = N−1`, and `x = −1` — **not** a nonnegative integer.  It is zero-confined
(`2^n ≤ 3^n` always).  Verified to `N = 20`: `r_n = 2^n−1` ✓, all `b_n = 1` ✓, `J(20) = 19` ✓.

This is the maximal-lift confined word, and it is the 2-adic fixed point `−1`.

## Verification

Two independent `C_N` implementations (closed form, recurrence) agree; the aggregate identity
holds on genuine orbits; `m_n` integrality is asserted at every step; all residue arithmetic uses
`pow(·,−1,m)`.  Scripts: `scripts/lift.py`, `scripts/run_enum.py`, `scripts/run_controls.py`.
