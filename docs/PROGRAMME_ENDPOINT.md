# Programme endpoint: the two-sided status

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

**Open Problem C at any rate implies (DE).** If least realizers grow at all, realizers cannot
stay bounded, and a bounded realizer is exactly what an infinitely confined orbit would supply.
This implication is **paper-level and not formalized here**; see
[`EQUIVALENT_FORMS_OF_DE.md`](EQUIVALENT_FORMS_OF_DE.md).
