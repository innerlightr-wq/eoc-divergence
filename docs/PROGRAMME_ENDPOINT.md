# Programme endpoint: the two-sided status

> **A narrative account of everything below, written for a reader new to the programme, is the
> synthesis note** *After the Reduction: Proved Statistics, Excluded Structure, and the Missing
> Pointwise Tool in the Accelerated 3x+1 Problem*
> ([`papers/synthesis`](../papers/synthesis); [doi:10.5281/zenodo.22925399](https://doi.org/10.5281/zenodo.22925399)).
> This file is the ledger; the note is the argument.

Both sides of the EOC programme have now reached the same shape. The *statistics* are theorems.
The *exact reductions* are theorems. What is open on each side is the placement of specific
integers inside a population whose size is known.

Every row is labelled **formalized** (machine-checked in this repository), **paper-proved**
(proved on paper, not formalized here), or **open**.

## Divergence side

| Item | Content | Status |
|---|---|---|
| Windowed sparsity | A collision-free set meets `[a, a+2^N)` in `≤ 4(N+1)θ^N` points, `θ < 2` | **formalized** (`Divergence.exists_window_sparsity`) |
| Reciprocal summability | A divergent orbit has `Σ 1/m_n < ∞` | **formalized** (`Divergence.summable_inv_orbit`) |
| Exact reduction | divergence `⇔` a zero-confined positive odd seed | **formalized** (`Divergence.divergent_iff_zeroConfined`) |
| **(DE)** universal drift exit | No positive odd `m` has `2^{S_n(m)} ≤ 3^n` for every `n` | **open** |

The reduction is unconditional: Garcia–Tal's collision-free window theorem, in Curry's explicit
form, is proved here rather than assumed.

## Occupation side

| Item | Content | Status |
|---|---|---|
| Confined-mass rate | `-(1/N)·log₂ p(N,c) → I₀ = α(1 − H₂(1/α))` | **formalized** (`Occupation.confined_mass_rate`) |
| Cycle lemma | A negative-total periodic sequence has an all-negative rotation | **formalized** (`Occupation.exists_rot_neg`) |
| Exact reduction | Residue–time duality: the least-realizer frontier is the inverse of the confinement lifetime | **paper-proved** (Revision 7, Props. 6.4–6.6; not formalized here) |
| **Open Problem C** | The pointwise realizer problem | **open** |

## Why the two open problems are the same kind of question

Each side now knows the *size* of the relevant population exactly:

* on the divergence side, how sparse a collision-free orbit must be in every dyadic window;
* on the occupation side, how much dyadic mass the `c`-confined words of length `N` carry.

Neither open problem asks for a better count. Both ask where **specific integers** — the actual
orbit values, the actual least realizers — sit inside a population whose size is already
determined. That is the common obstruction, and it is why improving either statistical estimate
does not touch either open problem.

## A signed conjecture strictly between (DE) and Lagarias

`K` denotes the zero-confined points of `ℤ₂^×`: those with `2^{S_n} ≤ 3^n` for every `n`.

> **(PosPC), the positive-side Periodicity Conjecture.** `K` contains no positive rational.

| statement | relation | status |
|---|---|---|
| (LPC) Lagarias's Periodicity Conjecture | **⇒ (PosPC)** | **open** |
| **(PosPC)** | **⇒ (DE)** | **open** |
| (DE) universal drift exit | — | **open** |

Both implications are proved in
[`audits/record_holder_anatomy/REPORT.md`](../audits/record_holder_anatomy/REPORT.md), P2. They
rest on the **signed marker**: every *eventually periodic* point of `K` is a **negative**
rational, because periodicity turns the aggregate identity into `m(2^{S_L} − 3^L) = C_L` with
`C_L > 0` and, by confinement plus unique factorisation, `2^{S_L} − 3^L < 0`.

**(PosPC) is strictly stronger than (DE)** as far as anything known: it also excludes positive
*non-integer* rationals. Concretely, (PosPC) holds **iff** for every odd `v ≥ 1` no positive odd
integer has a zero-confined orbit under `n ↦ (3n+v)/2^{v₂(3n+v)}` — an exact,
valuation-by-valuation conjugacy. So (PosPC) is (DE) asserted for the whole family `3x+v` at
once. **It is therefore *not* listed in [`EQUIVALENT_FORMS_OF_DE.md`](EQUIVALENT_FORMS_OF_DE.md),
which records statements that are equivalent to (DE).**

**What the marker does not do.** It classifies the eventually periodic points only, and it is
sign-sensitive in a way that is easy to over-read: for `3x−1` the identical argument gives
`m = C'_L/(3^L − 2^{S_L})` and therefore **positivity**, with `+1` a zero-confined positive
periodic point. Hence the corollary recorded with it: *no argument using only the aggregate
identity, the confinement condition and the sign of the denominator can separate the positive
integers from the rest of `K`* — the two systems agree on all three inputs and disagree on the
answer.

**Open Problem C at any rate implies (DE).** If least realizers grow at all, realizers cannot
stay bounded, and a bounded realizer is exactly what an infinitely confined orbit would supply.
This implication is **paper-level and not formalized here**; see
[`EQUIVALENT_FORMS_OF_DE.md`](EQUIVALENT_FORMS_OF_DE.md).

## The sharp form of the frontier

`r_min(N,0)` is the least positive odd integer that is zero-confined for `N` steps — the
realizer frontier of `EQUIVALENT_FORMS_OF_DE.md` form (b), and the object (DE) asks to be
unbounded.

> **CONJECTURE (sharp EOC).**
> ```
> log₂ r_min(N,0)  =  I₀·N  +  (3/2)·log₂N  +  O(1) ,       I₀ = α(1 − H₂(1/α)) = 0.0793186… ,
> ```
> with `α = log₂3`. Equivalently: the frontier sits at the *exact* density of the confined
> words, with no polynomial correction beyond the one the word count already carries.

**Where each piece stands.**

| piece | status |
|---|---|
| `−(1/N)·log₂p_N(0) → I₀` | **formalized** (`Occupation.confined_mass_rate`) |
| `p_N(0) ≍ 2^{−I₀N}·N^{−3/2}` | **paper-proved**, *Three Scales of Confinement*; **not** formalized. Confirmed on the exact `p_N(0)` (integer arithmetic, transfer recursion): `log₂(1/p_N) − I₀N − (3/2)log₂N` settles to `−3.28 ± 0.05` over `N = 100…300` |
| `log₂r_min(N,0) − log₂(1/p_N(0)) = O(1)` | **open** — this is the conjecture |

**The data. VERIFIED**, from an exact scan of every odd `m ≡ 3 (mod 4)` below `10^12`
(`audits/record_holder_anatomy/`): `r_min(N,0)` is certified for **`N = 1 … 346`**, with **24
distinct record holders**, the largest `r_min(345) = 898 696 369 947`. Against the exact
density, the residual `Δ₁(N) = log₂r_min(N,0) − log₂(1/p_N(0))` gives

> **empirical growth exponent `0.0737`, block-bootstrap 95 % CI `[0.061, 0.087]`, which contains
> `I₀ = 0.0793` and is bounded away from `0` at both ends.**

A persistent drift and a bounded residual cannot be separated on this range: the two models are
`ΔAICc = 0.29` apart at an effective sample size of `≈ 7` (the record holders are strongly
serially correlated). **CONJECTURE** for the statement; **VERIFIED** for the data behind it.

**Why the frontier is not a Poisson process.** Two measurements, both **VERIFIED**:

* `Δ₁(N) > 0` at every one of the 24 holders — the **first** confined integer is 1.9–2.5 bits
  *further out* than random placement predicts;
* the direct count `#{odd m ≤ 2^j : N-confined}` against the exact `2^{j−1}p_N(0)` shows an
  **excess immediately above `r_min(N,0)` and nowhere else** — `1.78×` at `X = 2^{28}` for
  `N = 200`, `5.45×` at `X = 2^{35}` for `N = 300` (12 observed against 2.2 expected), decaying
  to `≈1` by `2^{40}`, while in the well-populated regime the null is right to a few parts in a
  thousand.

Those are the two signatures of a **clustered** point process, and the cause is **L1/L2**: a
confined `m ≡ 2 (mod 3)` has a smaller, more-confined backward image, so confined integers come
in chains of length `v₃(m+1)`. Thinning to chain roots accounts for about **a quarter to a
third** of the offset at `k = 2, 3` and no more.

> **PROVED: root-thinning cannot move `Δ₁` at all.** `r_min(N,0)` is always a chain root — that
> is **L4** — so the least confined integer and the least confined *root* are the same number,
> and the thinned null differs from the unthinned one by exactly the constant `log₂(3/2)`.
> Verified at every `N ≤ 346`.

## Closed routes

Routes examined and closed, with the reason each closes.

| Route | Finding | Status |
|---|---|---|
| Descent via inheritance + well-ordering | Sign-sensitive: the backward fixed point is `−1` for `3x+1` but `+1` for `3x−1`, so L1's strict decrease `p < m` is unconditional in the first case and fails at `m = 1` in the second. But **L7** shows forward motion cannot accumulate 3-adic budget — a `d = 1` step raises `v₃(m+1)` and the round-trip requirement by exactly one, and even `d` destroys the budget. Any descent statement over `Z` is moreover *equivalent* to (DE). | **STOP** |

| Record-holder anatomy — signed markers, Sturmian proximity, a Markov-type spectrum of the dust | Every candidate pattern reduces to a proved lemma (**L4**, **L4′**, **L1/L2**, the last-maximum structure), to a control artefact, or to a **selection effect**: the record holders are the minimum over all confined words, so comparing them against a single typical word measures the size of the family. The record holders are **not** Sturmian-adjacent (1–3 shared valuations out of depths to 236); the approximation spectrum has **one** isolated level — the rational points of `K`, all negative by the signed marker — and then a continuum in which they are undistinguished; the signed border oscillates with no trend. | **STOP** |

Full record: [`audits/descent/DESCENT_AUDIT.md`](../audits/descent/DESCENT_AUDIT.md) and
[`audits/record_holder_anatomy/REPORT.md`](../audits/record_holder_anatomy/REPORT.md).
The three results retained from the descent audit are formalized in the `Descent` library
(L1, L2, L4, L7); the record-holder audit retains **L4′** and the signed marker **P1**, neither
yet formalized.

**Optional follow-up, and what it would and would not do.** `r_min(N,0)` could be pushed past
`N ≈ 390` by a search over the class tree instead of a linear scan (the scan doubles every
`+12.3` in `N`, so `N ≈ 446` is already ~2.5 days). Roughly doubling the 24 distinct record
holders is what it would take to separate a persistent drift from a bounded residual.
**That would change the constants in the sharp conjecture above, not the exponent:** the
interval `[0.061, 0.087]` is bounded away from `0` at both ends, and even the largest decline
anywhere in the data would leave a growth exponent near `0.069`. Nothing in this route bears on
(DE).
