# COUNTEREXAMPLES.md — exact witnesses to the invalid bridges

Every word below has all letters `>= 1` (admissible as a valuation word) and its
`0`-confinement is decided **exactly** by `2^{S_j} <= 3^j` on Python integers.
No floating-point logarithm decides confinement anywhere.
Script: `scripts/counterexamples.py`; log: `results/counterexamples.log`.

---

## 1. The four symbolic witnesses

| | word | 0-confined | `liminf Delta/N` | `limsup Delta/N` | `max Delta/log_2 N` | `max Delta` |
|---|---|---|---|---|---|---|
| **W1** | `d_j = 1` for all `j`, `N = 3000` | **yes** | `0.584963` | `0.584963` | `151.9` | `1754.89` |
| **W2** | geometric climb(`d=1`)/descend(`d=2`) stages, `N = 6000` | **yes** | `0.000093` | `0.209963` | `85.0` | `1066.78` |
| **W3** | `Delta_N ~ sqrt(N)`, `N = 4000` | **yes** | `0.015713` | `0.099814` | `5.32` | `63.68` |
| **W4** | `d_j = 2` whenever confinement allows, else `1`, `N = 4000` | **yes** | `0.000000` | `0.008386` | `0.137` | `1.00` |

**What each refutes** (`A..G` as in `TWO_CLOCK_TRANSLATION.md` §2):

* **W1 refutes `A ==> D`, `A ==> C`, `A ==> E`, `A ==> F`, `A ==> G`, and
  `B ==> C`.** Zero confinement alone gives `Delta_N/N = alpha - 1` **constant**;
  the ordinary odd density is `1`, not `beta`.
* **W2 refutes `D ==> E` and `C ==> E`.** `liminf Delta_N/N -> 0` while
  `limsup Delta_N/N = 0.21`: the orbit returns near-critically along a
  subsequence and departs linearly in between. Its ordinary `liminf h/l`
  is `0.630952`, against `beta = 0.630930`.
* **W3 refutes `E ==> F`.** `Delta_N = o(N)` with `Delta_N/log_2 N -> infinity`.
  **This is the specific witness the brief asks for:** it shows that
  `liminf Delta_N/N = 0` — indeed the stronger `Delta_N = o(N)` — yields **no**
  `O(log N)` and **no** `O(sqrt N)` return corridor.
* **W4** shows `G` is **non-empty symbolically**: a bounded-deficit confined word
  exists. It is excluded for positive-integer orbits only by the repository's
  bounded-drift theorems, i.e. **arithmetically, never symbolically**.

The two-clock identity of Lemma C1 was checked on all four:
`liminf_l h(l)/l`, `min_N N/S_N` and `1/limsup_N(S_N/N)` agree to all printed
digits in every case (`equal = True` four times).

## 2. The `-1` warning control — a confined word realized by no positive integer

The brief asks for this control and it is the sharpest item in the file.

The accelerated word `d_j = 1` for all `j` (**W1**) is `0`-confined with
`Delta_N = (alpha-1)N -> infinity` **linearly**. Its ordinary parity vector is
`111...`, whose 2-adic realizer is `Phi(111...) = -1`, and `T(-1) = -1`: a
**fixed point**, negative, with a finite orbit.

> **Proposition X1 [P, verified].** For a positive odd `m_0`, the number of
> leading letters `d_j = 1` is **exactly `v_2(m_0 + 1) - 1`**.
>
> *Proof.* `d_j = 1` means `m -> (3m+1)/2`, whose iterates are
> `m_j = (m_0+1)(3/2)^j - 1`. Then
> `3 m_j + 1 = 2[(m_0+1) 3^{j+1}/2^{j+1} - 1]`, so `d_{j+1} = 1` iff
> `(m_0+1)3^{j+1}/2^{j+1} - 1` is odd, iff `j+1 < v_2(m_0+1)`. ∎
>
> **Verified, 0 violations**, on `m_0 = 1,3,5,7,15,31,63,127,255,1023,4095,65535,
> 27,703,10087` (`scripts/realizability.py`). *An earlier version of this
> proposition stated `v_2(m_0+1)` and was off by one; the exact check caught it
> and the statement was corrected, not the test.*

So **every** positive integer leaves W1 after finitely many steps, and the
infinite word W1 is realizable **only** by `-1`. A `0`-confined symbolic word
with unbounded linear deficit therefore need not come from a positive seed at
all — the warning the brief asks for, in its strongest form.

## 3. Rational 2-adics whose category blocks the transfer

* `-1 = 111...`: ordinary density `h/l = 1 > beta`, rational (`in Q_odd`), orbit
  **finite** (`{-1}`). It does not contradict [2021] Theorem 1, whose hypothesis
  is a divergent (infinite) orbit — but it is the reason the "`> beta`" branch
  cannot be read as "density `> beta` implies aperiodic": `111...` is periodic.
* `1 = 1000...`: `T(1) = 2, T(2) = 1`, parity `1,0,1,0,...`, density `1/2 < beta`.
  Every terminating positive orbit ends here, so every terminating orbit has
  `liminf h/l = 1/2 < beta` and falls in [2021]'s **branch 2** (Monks-Yazinski),
  the branch that survives audit. Consistently, `sum_j 1/m_j = infinity` for such
  an orbit (the tail is `1 + 1 + ...`), so `Phi_R(v) = -infinity` — matching
  [2021]'s own remark that a non-existent limit means divergence to `-infinity`.
  **Verified**: for `m_0 = 27` and `703` the quantity `sum_{i<N} 2^{-Delta_i}`
  jumps from `16.1` and `442.8` at the injective depth to `1.29e7` and `3.38e8`
  by `N = 82, 103` (`scripts/return_count.py` control block).

## 4. Why a congruence check can never close the gap

> **Proposition X2 [P, verified].** Every admissible word `d` of length `N` has
> exactly one odd residue `r < 2^{S_N+1}` with
> `3^N r + q_N ≡ 2^{S_N} (mod 2^{S_N+1})`, and iterating the accelerated map from
> `r` reproduces `d`.
>
> **Verified, 0 violations**, recomputing `r` from the carry and checking by
> direct iteration on seven words (`[1,1,1,1] -> 31`, `[1,2,1,2] -> 123`,
> `[2,1,2,1] -> 121`, `[1,1,2,2] -> 71`, `[2,2,1,1] -> 97`,
> `[1,2,2,1,2] -> 107`, `[3,1,1,1] -> 125`).

Because this residue exists for **every** admissible word and **every** `N`, a
congruence or realizer check validates **finite prefixes only**. The residues
`r_N` live in moduli `2^{S_N+1}` that grow without bound, and nothing in the
congruence forces a **common positive representative** — which is exactly what
"realizable by a positive integer forever" would require. W1 is the explicit
instance: every prefix has a least realizer (`[1,1,1,1] -> 31`), the realizers
are `2^{N+1}-1 -> infinity`, and the limit object is `-1`.

> **This is the symbolic-to-arithmetic gap, exhibited rather than described:
> finite-prefix realizability is automatic and carries no information about the
> infinite word.** It is the same wall that `MASS_CONCENTRATION.md` §4 reaches
> from the measure side.
