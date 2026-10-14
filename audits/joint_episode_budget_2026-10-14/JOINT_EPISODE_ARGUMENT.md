# JOINT_EPISODE_ARGUMENT.md

Rev 8 conventions throughout (`PROVENANCE.md` §1 for the manuscript identity):
`m_{n+1} = (3m_n+1)/2^{d_n}`, `d_n = v_2(3m_n+1)`, `S_0 = 0`, `R_n = S_n − αn`,
`α = log_2 3`. Occupation is the **one-sided** corridor `R_n ≤ c`, `c` a
nonnegative integer, decided exactly by `2^{S_n} ≤ 2^c 3^n`. Time zero counts.
The full forward orbit continues past `m = 1` (`d = 2`, `R` rising by `2 − α`).
`Δ_n = −R_n` is the earlier deficit notation. This is **not** the two-sided band
`c − w ≤ R_n ≤ c` and **not** the moving-width SUBLINEAR-RETURN problem.

---

## 1. The accounting dictionary — verified, and preparation only

`C_0 = 0`, `C_{n+1} = 3C_n + 2^{S_n}`; `z_n = 2^{S_n}/3^n = 2^{R_n}`;
`𝓑_n = m_n z_n = m_0 + C_n/3^n = m_0 2^{E_n}`, `E_n = Σ_{j<n} log_2(1+1/(3m_j))`.

Episodes: `I_i = [a_i, b_i)` the maximal occupied integer intervals in `[0,H)`,
`ℓ_i = b_i − a_i`, with the initial episode (`a_0 = 0`) and the final truncated
episode distinguished from the complete ones. For each nonempty episode

```
   W_i = Σ_{n∈I_i} z_n = 3(𝓑_{b_i} − 𝓑_{a_i}) ,
   η_i = W_i/(2^c ℓ_i) ∈ (0,1] ,
   ℓ_i = (3/2^c)(𝓑_{b_i} − 𝓑_{a_i})/η_i .
```

Global accounting, gaps included — `𝓑` is **not** conserved, it receives `z_n/3`
at every step, and there is no leakage:

```
   3(𝓑_H − m_0) = Σ_{n<H, R_n≤c} z_n + Σ_{n<H, R_n>c} z_n .
```

Blocks: `u_{[a,b)} = C_{[a,b)}/3^t`, `v_{[a,b)} = 2^s/3^t`,
`(𝓑_b, z_b)^T = [[1,u],[0,v]](𝓑_a, z_a)^T`, `m_b = (m_a+u)/v`,
`2^s m_b = 3^t m_a + C_{[a,b)}`, `u_tot = u_1 + v_1u_2`, `v_tot = v_1v_2`, and
terminal oddness `3^t m_a + C_{[a,b)} ≡ 2^s (mod 2^{s+1})`.

**Verified exactly** (`scripts/dictionary.py`, 9 seeds, all `n ≤ 60`, six blocks
and three block compositions each): **11/11 identities, 0 violations.** `W_i` is
a newly named carry-weighted occupation, not the manuscript's occupation
functional; every formula above is a regrouping of Lemmas 2.2/2.4, **not a new
estimate**. The triangular matrices are a coordinate representation whose
diagonal contains the eigenvalue `1`; no full-space contraction is asserted.

## 2. The already-known loss, located before anything new

`ℓ_i = (3/2^c)(𝓑_{b_i}−𝓑_{a_i})/η_i` contains `1/η_i`. A long deep episode has
small `η_i` and costs little weighted carry per unit time, so a bound on
`Σ_i W_i` alone does not bound `Σ_i ℓ_i`. On a **two-sided** band the elementary
`η_i ≥ 2^{−w}` is available and reproduces the known exponential-in-width loss;
that is the baseline, not progress.

At a re-entry, Lemma 2.2 gives
`log_2 m_{a_i} + c_i = log_2 m_0 − c + E_{a_i} + 2c_i`. Since `E_{a_i} ≥ 0` and
`c_i ≥ 0`, **every** per-episode charge is at least `log_2 m_0 − c`: charging each
episode independently levies the initial seed scale `P` times. That is
Remark 13.3's mechanism, whose precise conclusion is preserved here — it refutes
the efficiency of *that particular surrogate*, not every episode argument, and
`Q_K` upper-bounds occupation only once `K` is shown admissible for every
episode it is used on.

## 3. The candidate inequality, written before testing

Two ingredients, combined so that no per-episode seed allowance is refreshed:

* **global pot (telescoping).** `Σ_i W_i = 3Σ_i(𝓑_{b_i}−𝓑_{a_i}) ≤ 3(𝓑_H − m_0)`
  — **one** budget shared by all episodes.
* **per-episode toll (new as stated; from Prop. 13.1).** At a re-entry `a_i > 0`,
  `c − α + 1 < R_{a_i} ≤ c`, hence
  ```
     z_{a_i} > 2^c·2^{1−α} = (2/3)2^c ,     so    W_i ≥ z_{a_i} > (2/3)2^c
  ```
  **independently of `ℓ_i` and of how deep the episode goes.** Equivalently
  `η_i ℓ_i > 2/3`: the carry-weighted duration has a universal positive floor
  per episode even though the duration does not.

> **Candidate (C1).** `P − 1 < (3/2)·2^{−c}·3(𝓑_H − m_0) = (9/2)·2^{−c}m_0(2^{E_H}−1)`,
> `P = #episodes in [0,H)`; and under distinctness of `m_0..m_{H−1}`,
> `2^{E_H} ≤ e^{7/9}H^{1/9}` (`EOC/HarmonicPacking.lean sum_inv_orbit_le`), giving
> `P ≤ 1 + (9/2)e^{7/9}2^{−c}m_0H^{1/9}`.

Domain: `m_0` odd, `c ∈ Z_{≥0}`, `H` any horizon; the `H^{1/9}` form additionally
requires `m_0,…,m_{H−1}` pairwise distinct — **it may not be applied after the
first repetition.** Constants absolute.

**Which relation is not already a definition.** The toll is the only ingredient
that is not a regrouping: it converts Prop. 13.1's *entry-depth* statement into
a *weighted-carry* floor. The pot is pure telescoping.

## 4. The test, and the exact reason it fails

**(C1) holds in every case tested and is vacuous in every case where the drift
escapes** (`scripts/joint.py`): slack `1.2×10^4` at `m_0 = 285175, c = 1`,
`4.8×10^4` at `626331`, `1.3×10^7` at `63728127`.

**Diagnosis, exact.** Split the pot by corridor membership. On the corridor
`z_n ≤ 2^c`; in a gap `z_n > 2^c` and grows geometrically. Measured gap share of
the pot:

| `m_0` | `c` | occupied part | gap part | gap share |
|---|---|---|---|---|
| 285175 | 1 | 53.309737 | 96115.130 | **0.999446** |
| 285175 | 2 | 87.279624 | 96081.160 | 0.999092 |
| 10087 | 1 | 13.805562 | 7444.093 | 0.998149 |
| 35655 | 1 | 11.928665 | 21791.993 | 0.999453 |

> **The pot is `99.9%` gap weight.** Amortizing an episode toll against it
> therefore constrains **gap** time, not corridor time: with `G = H − O_c` and
> `z_n > 2^c` on gaps, `2^cG < pot`, which rearranges to
> `O_c > H − 2^{−c}·pot` — a **lower** bound on occupation. The mechanism points
> the wrong way. (Checked: at `m_0 = 285175, c = 1` it yields `O_c > −47946`.)

**Where (C1) *is* non-vacuous** (`scripts/where_nonvacuous.py`): exactly where
the drift is confined to a bounded **two-sided** window. On the Prop. 13.2
oscillator (`max R_n − min R_n ≈ 1.0–2.4`) the slack is a stable `3.5×` across
`N = 60,120,200` and `c = 0,1,2`; on seeds whose drift escapes it degrades like
`2^{R_max−c}`. **That sector is already closed by `BoundedDrift.lean`.** This is
the brief's stopping condition, met.

## 5. Why no amortization of the single-window charge exists — the obstruction

The candidate's failure above is about the *pot*. The deeper obstruction is about
the *charge*, and it is a theorem.

> **Proposition J (two-sided allowance pin).** Let `a > 0` be a re-entry and
> `A_a := log_2 m_a + c_a`, `c_a = c − R_a`. Then
> ```
>    log_2 m_0 − c  ≤  A_a  <  log_2 m_0 − c + E_a + 2(α−1) ,   2(α−1) = log_2(9/4) ,
> ```
> equivalently, **with no logarithm and over Q exactly**,
> ```
>    1  ≤  2^{2c} m_a^2 / (m_0 𝓑_a)  <  (9/4)·𝓑_a/m_0 .
> ```
> *Proof.* `2^{A_a} = m_a·2^c/z_a = 2^c m_a^2/𝓑_a` since `z_a = 𝓑_a/m_a`. The
> left half is `𝓑_a ≥ m_0`, i.e. `C_a > 0` (Lemma 2.4). The right half reduces,
> after cancelling `m_a`, to `z_a > (2/3)2^c`, i.e. exactly Prop. 13.1. ∎

**Verified exactly at all 17 re-entries across 11 `(m_0,c)` cases, 0 violations**
(`scripts/pin_and_controls.py`), including the exact identity
`2^{A_a−(log_2 m_0−c)} = 2^{E_a}·2^{2c_a}`. At `m_0 = 285175, c = 1` the floor is
`17.121488`, `E_H = 0.153687`, so for `i ≥ 1` all `A_i` lie in
`[17.1215, 18.4451]` (width `1.3236`); measured `17.840, 17.690, 17.389, 17.774,
18.114, 17.474`. The initial episode (`A_0 = 19.121`) lies outside because
`c_0 = c`, and Prop. 13.1 does not apply to it.

> **Proposition J is a rearrangement of carry positivity and the entry lemma, not
> an independent restriction.** Stated plainly because the brief requires it: two
> rearrangements of one equation must not be intersected and called independent.

> ### PRIOR ART — Proposition J and its corollary are already established
>
> `the Phase 6 return-gate round (local scratch, not published)VERDICT.md` (Phase 6) answer 8 already records
> that the surrogate is **pinned**: *"the surrogate total is pinned at
> `Q = N(1 + K(log_2 m_0 − c)) + O(NK log_2((3/2)P))`"*, and answer 8 closes the
> route *"rather than improving it, because **all charges are the same to within
> a small additive constant**"*. Answer 7 states *"None of the five available
> inputs … supplies a quantity that decreases"*. Phase 6 also has the correct
> two-sided entry bound with the Eliahou–Rozier product,
> `m_0 2^{−c}P_a ≤ m_a < (3/2)m_0 2^{−c}P_a`, and notes that the lower half
> *"is Rev 8 `rem:episodescope`'s own step, so it was never new."*
>
> **So Proposition J and Corollary J1 below are a re-derivation of Phase 6's
> conclusion by a different route, not new results.** What this round adds at
> this point is only the exact integral form (`1 ≤ 2^{2c}m_a^2/(m_0𝓑_a) < (9/4)𝓑_a/m_0`,
> with the explicit width `E_H + log_2(9/4)`) and the identification of the two
> halves with carry positivity and Prop. 13.1 respectively. Reported promptly, as
> the brief requires.

Its value is the corollary, which is what closes the mechanism:

> **Corollary J1 (no amortizable resource).**
> `A_a − (log_2 m_0 − c) = E_a + 2c_a` with **both terms `≥ 0`**, and `E_a` is
> **monotone increasing** in `a`. So the single-window allowance available to the
> `i`-th episode never falls below its floor `log_2 m_0 − c`, and the only
> monotone ingredient enters with the **wrong sign** — it *increases* the later
> allowances. An amortized charge needs a resource that is consumed; there is
> none.

My own working hypothesis — that `A_i` would be non-decreasing, so that the
repeated charging would at least be *attributable* to a monotone quantity — was
**refuted** on 2 of 7 cases (`A_i` for `285175, c=1` goes
`19.12, 17.84, 17.69, 17.39, 17.77, 18.11, 17.47`: it drops off the initial
episode and then oscillates). The correct statement is the two-sided pin: the
allowances are neither consumed nor growing, they are **pinned in a window of
width `E_H + 1.169925` just above `log_2 m_0 − c`**, i.e. they are the *same*
resource measured `P` times. That makes Remark 13.3's `Ω(log m_0)` over-count
exact and two-sided, and shows no choice of `K` repairs it — for the structural
reason that there is nothing to amortize.

## 6. The irreducible scale gap

Even granting a perfect solution of the small-`η` problem, the resource is the
wrong size.

```
   pot = 3(𝓑_H − m_0) = 3m_0(2^{E_H} − 1) = Θ(m_0)         (measured pot/m_0 = 0.34 … 0.74)
   EOC target (manuscript §15): O_c ≤ K log_2 m_0,  certified max O_c/log_2 m = 11.3402
```

| `m_0` | `O_c` | `O_c/log_2 m_0` | `pot/m_0` | `pot/log_2 m_0` | overshoot |
|---|---|---|---|---|---|
| 285175 | 98 | 5.408 | 0.3372 | 5306.9 | `981×` |
| 626331 | 122 | 6.336 | 0.4117 | 13390.3 | `2114×` |
| 63728127 | 259 | 9.990 | 0.5503 | 1352600.6 | `135393×` |
| 1234567891 | 5 | 0.166 | 0.6006 | 24552899.0 | `1.5×10^8` |

> **Obstruction (scale).** The carry pot has size `Θ(m_0)`; EOC needs
> `Θ(log m_0)`. The overshoot grows like `m_0/log m_0`, i.e. exponentially in the
> seed's bit length. **No amortization of a `Θ(m_0)` pot can yield a
> `Θ(log m_0)` bound**, independently of how `η` is handled.

> ### PRIOR ART — this verdict is Phase 6's, for a different resource
>
> Phase 6 answer 3 proves the entry-gate episode bound is `Θ(m_0 2^{−c})`,
> **attained**, and states: *"the observed maximum episode count is 12 at
> `m_0 ≈ 2·10^5` (`≈ 0.68 log_2 m_0`) against a bound of `≈ m_0/9`. **The gate
> overcounts by `Θ(m_0/log m_0)`.**"* Answer 7: *"the **prefactor** `N` must
> already be `O(log m_0)`, and the gate gives `Θ(m_0)`."*
>
> **The carry pot is a different resource from the entry gate, and it lands on the
> same `Θ(m_0)` versus `Θ(log m_0)` verdict with the same `m_0/log m_0`
> overshoot.** That coincidence is the content of this section: it is now known
> for two independent resources, which is evidence that the obstruction is to the
> *shape* of resource-amortization arguments and not to a particular choice of
> resource. The episode-count bound (C1) derived here is strictly **weaker** than
> Phase 6's attained bound and is not offered as an improvement.

## 7. Residual terms, stated

Nothing above is dropped or renormalized. The three residuals that would have to
be supplied, in increasing order of difficulty:

1. **the `1/η_i` loss** — Phase 6 already recorded the relevant dichotomy as its
   one open item: *"long episodes always had depth `≈ ℓ/10` (`corr = +0.923`), and
   no episode of length `≥ 20` with depth `< 1` was found"*, status `[O]`. The
   stratification here reproduces that independently and converts it into the
   exact obstruction to the pot route. The local-time profile `L_w = #{n<H : c−w−1 < R_n ≤ c−w}`
   satisfies `Σ_w L_w 2^{−w} < 2^{1−c}·pot` exactly, while `O_c = Σ_w L_w`.
   Measured profiles spread to `w_max = 7…13` with mean depth growing
   (`3.14` at `O_c = 98`, `7.09` at `O_c = 259`), and the exact inverse-`η` loss
   `O_c/Σ_wL_w2^{−w}` is already `2.6 … 12.9`. Measured
   `w_max/log_2 O_c ∈ [1.16, 1.73]`, so a depth bound `w_max ≤ K log_2 O_c` with
   `K < 1` — which is what the pot route would need — is **not supported by the
   data**;
2. **the gap direction** — the pot constrains gaps, so an *independent upper*
   budget on gap weight is required before a gap's carry increment counts as a
   penalty. None is proved here, and none is assumed;
3. **the scale gap of §6**, which is fatal to this resource whatever is done
   about 1 and 2.

## 8. What this does and does not say

* **It is silent on one infinite episode.** A hypothetical infinite zero-confined
  orbit is a **single** episode: `P = 1`, so the toll contributes
  `(2/3)2^c(P−1) = 0`. In the data every single-episode seed shows toll
  `0.000000` exactly. So nothing here is divergence exclusion; it is
  **separated-return control**, and it applies to finite truncations only through
  `H`, with `H`-dependence that does **not** permit passage to all `H` (the
  `H^{1/9}` form additionally dies at the first repeated state).
* **No corridor-uniform lifetime hypothesis is assumed.** §7.1 of the manuscript
  warns that such a hypothesis may already contain a strong pointwise lifetime
  claim; none is used.
* **No divergence or cycle consequence is drawn.** Theorem 6.14's external
  sparsity dependency is untouched, and no cycle-exclusion follows from the
  drift-exit argument.
* **The pointwise example `O_c > L_c`** (the Loeb seed) does not prove the
  corresponding universal conjectures inequivalent; Remark 10.1's withdrawal of
  that stronger reading is preserved.
