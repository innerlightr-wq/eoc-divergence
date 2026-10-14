# CLAIMS_AND_CONTROLS.md

Labels: **[PRIOR]** manuscript / repository / earlier scratch phase ·
**[P]** proved here · **[V]** exact finite computation, range stated ·
**[F]** floating diagnostic · **[R]** refuted or closed · **[C]** conditional.

---

## 1. [PRIOR] Inputs used, with their actual hypotheses

| statement | source | hypotheses |
|---|---|---|
| Lemma 2.2 (Eliahou–Rozier): `m_n 2^{R_n} = m_0∏_{i<n}(1+1/(3m_i))`, `R_n = log_2(m_0/m_n)+E_n`, `E_n ≥ 0` | Rev 8, due to Eliahou and Rozier; no novelty claimed | `m_0` odd `≥ 1`, `n ≥ 0` |
| Lemma 2.4 (aggregate): `2^{S_n}m_n = 3^n m_0 + C_n`, `C_0=0`, `C_{n+1}=3C_n+2^{S_n}>0` | Rev 8; elementary, formalized §14 | none beyond the recurrence |
| Definition 6.1 (`L_c`, `O_c`, `τ_c`), full-forward-orbit convention | Rev 8 §6.1 | time zero counts; orbit continues past `m=1` |
| Remark 6.2: `O_1(285175)=98`, `L_1=14`, `τ_1=15`, `15+4+6+64+1+5+3` | Rev 8 (count corrected in Rev 8; computed independently [25]) | — |
| Prop. 13.1 (entry lemma): re-entry `a>0` ⟹ `d_{a-1}=1` and `0 ≤ c−R_a < α−1` | Rev 8; formalized §14 | `a > 0`; **bounds entry depth, not depth inside** |
| Prop. 13.2 (episode counts unbounded) | Rev 8; formalized §14 | conclusions concern the **realized prefix** `[0,N)` only |
| Remark 13.3 (the surrogate `Q_K` is lossy by `Ω(log m_0)`) | Rev 8 | refutes *that* surrogate, **not** per-episode methods in general |
| §7.1 reclassification of the corridor-uniform hypothesis | Rev 8 | may already contain a strong pointwise lifetime claim — **not assumed here** |
| Thm 6.14 (divergence equivalence) | Rev 8 | external sparsity dependency; **used for no claim here** |
| `m_n ≥ m_0 2^{−c}` on the corridor | Rev 8 `rem:episodescope`'s own step | `R_n ≤ c`, `C_n > 0` |
| `sum_inv_orbit_le`: `Σ_{k<N}1/m_k ≤ 7/3 + (1/3)log N` | `eoc-lean-verification` `EOC/HarmonicPacking.lean` | `m_0` odd, `m_0..m_{N−1}` **pairwise distinct** |
| bounded two-sided drift is excluded for positive-integer orbits | `EOC/BoundedDrift.lean` | Case A non-injective / Case B injective |
| **the surrogate is pinned: all charges equal to within a small additive constant; `Q = N(1+K(log_2m_0−c)) + O(NK log_2((3/2)P))`** | **`the Phase 6 return-gate round (local scratch, not published)VERDICT.md` (Phase 6) answers 7–8** | — |
| **the entry gate overcounts by `Θ(m_0/log m_0)`; the prefactor must be `O(log m_0)` and the gate gives `Θ(m_0)`** | **Phase 6 answers 3, 7** | attained at `m_0=43, c=2` |
| two-sided entry bound `m_0 2^{−c}P_a ≤ m_a < (3/2)m_0 2^{−c}P_a` | Phase 6 answer 1 (Phase 5's T3 refuted there) | `P_a = ∏_{j<a}(1+1/(3m_j))` |
| `m_a ≡ 5 (mod 6)`; `m_a ≡ 11,17 (mod 18)` for `a ≥ 2`; `m_{a−1} ≡ 3 (mod 4)` | Phase 6 answer 2 | verified 207615/207615 there |
| depth-vs-length dichotomy: long episodes had depth `≈ ℓ/10`, `corr = +0.923`, status `[O]` | Phase 6 secondary findings | finite band-length measurement |

the Phase 7 gate-placement round (absent from the machine) is **ABSENT** from this machine; the placement
result is recovered instead from
`audits/lopez_stoll_transfer_2026-10-14/` and the EOC
memory record (placement `=` Open Problem C; the obstruction is the additive
term). Recorded as a limitation, not worked around.

## 2. [P] Proved here

| # | statement | status |
|---|---|---|
| **D1** | the 11-identity accounting dictionary of `JOINT_EPISODE_ARGUMENT.md` §1, including `W_i = 3(𝓑_{b_i}−𝓑_{a_i})`, `0<η_i≤1`, the block matrix, its composition law, and terminal oddness | exact regrouping of Lemmas 2.2/2.4 — **preparation, not an advance** |
| **T (toll)** | at every re-entry `a_i>0`: `z_{a_i} > (2/3)2^c`, hence `W_i > (2/3)2^c` and `η_iℓ_i > 2/3`, **independently of `ℓ_i` and of the depth reached** | new as stated; a one-line consequence of Prop. 13.1. I did not find it in Phase 6 |
| **C1** | `P − 1 < (9/2)2^{−c}m_0(2^{E_H}−1)`; with distinct states `P ≤ 1 + (9/2)e^{7/9}2^{−c}m_0H^{1/9}` | **strictly weaker** than Phase 6 answer 3's attained `Θ(m_0 2^{−c})` bound; not offered as an improvement |
| **G (gap domination)** | the pot `Σ_{n<H}z_n = 3(𝓑_H−m_0)` is `≥99%` gap weight, and amortizing against it yields `O_c > H − 2^{−c}·pot`, a **lower** bound | new; specific to the carry-pot resource |
| **J** | two-sided allowance pin, exact integral form `1 ≤ 2^{2c}m_a^2/(m_0𝓑_a) < (9/4)𝓑_a/m_0`, left half `=` carry positivity, right half `=` Prop. 13.1 | **re-derivation of Phase 6 answers 7–8** by a different route; only the integral form and the width `E_H+log_2(9/4)` are added |
| **J1** | `A_a − (log_2m_0−c) = E_a + 2c_a`, both `≥0`, `E` monotone increasing ⟹ no amortizable resource | **Phase 6 already states this** ("all charges are the same to within a small additive constant"; "none … supplies a quantity that decreases") |
| **S (scale)** | pot `= Θ(m_0)` against an `O(log m_0)` target; overshoot `Θ(m_0/log m_0)` | **Phase 6's verdict for the entry gate**, reproduced here for a second, independent resource |
| **L (local time)** | `Σ_w L_w 2^{−w} < 2^{1−c}·pot` exactly, with `O_c = Σ_w L_w`; so the pot route needs a depth bound `w_max ≤ K log_2 O_c` with `K<1` | new as a reduction; the measurement refutes `K<1` (see §3) |

## 3. [V] Exact finite computation

All corridor, carry, matrix-product and weighted-sum decisions are exact
`int`/`Fraction`; corridor membership is `2^{S_n} ≤ 2^c 3^n`, never a float
logarithm. Horizons are **certified** by the fixed-point drift (`d=2` at `m=1`,
`R` strictly increasing), not by a scan cutoff.

| check | range | result | script |
|---|---|---|---|
| 11 dictionary identities | 9 seeds, all `n ≤ 60`, 6 blocks + 3 compositions each | **0 violations** | `dictionary.py` |
| Loeb replication `m_0=285175, c=1` | certified `H = 138`, `n_one = 138` | `O_1 = 98` ✓, `L_1 = 14` ✓, `τ_1 = 15` ✓, all **seven** displayed runs `[0,15),[16,20),[21,27),[31,95),[98,99),[100,105),[108,111)` ✓, lengths `15+4+6+64+1+5+3` ✓; no occupied index in `[H,H+40)` | `loeb.py` |
| `W_i = 3(𝓑_{b_i}−𝓑_{a_i})`, `0<η_i≤1`, toll | the 7 Loeb episodes | exact; `η_i ∈ [0.1658, 0.7976]`; toll holds at all 6 re-entries | `loeb.py` |
| gap accounting `occupied + gap = total` | Loeb | exact equality | `loeb.py` |
| **C1** | 10 `(m_0,c)` cases | holds everywhere; slack `1.2×10^4 … 1.3×10^7` where drift escapes | `joint.py` |
| gap share of the pot | 6 cases | `0.377 … 0.9995` (`0.9994` at Loeb) | `joint.py` |
| **J** exact integral form + the identity `2^{A_a−(log_2m_0−c)} = 2^{E_a}2^{2c_a}` | **17 re-entries**, 11 cases | **0 violations** | `pin_and_controls.py` |
| C1 non-vacuity localization | oscillator `c=0,1,2`, `N=60,120,200` vs 3 escaping seeds | slack **`3.5×`** on the oscillator (bounded two-sided drift), `10^4–10^7` otherwise | `where_nonvacuous.py` |
| local-time profiles `L_w` | 8 cases | `w_max = 7…13`, mean depth `3.14`→`7.09` as `O_c` `98`→`259`; inverse-`η` loss `2.6…12.9` | `localtime.py` |
| `w_max/log_2 O_c` | 8 cases | `1.16 … 1.73` — **`K<1` is not supported**, so the pot route's required depth bound is empirically false | `localtime.py` |
| scale gap | 11 cases | `pot/m_0 = 0.34…0.74`; overshoot `0.4×`…`1.5×10^8`, growing like `m_0/log m_0` | `scale_gap.py` |

## 4. Controls

**A. Least realizer vs larger lifts in one realizer class [V].** Prefix of
`285175`, `N=12`, word `(1,1,3,2,1,1,1,2,1,1,1,1)`, `S=16`, class
`23031 mod 131072`. Lifts `23031, 154103, 285175, 416247, 547319`: word and
`R`-profile identical, prefix `W = 8.603527014` **identical**, while
`log_2 m_0` runs `14.49 → 19.06`. **So occupation, `W_i`, `η_i` and drift of a
prefix are class invariants and `log_2 m_0` is not** — any charge containing
`log_2 m_0` is not a function of the prefix, which is exactly Remark 13.3's
mechanism and the reason it cannot be repaired by sharpening the per-episode
estimate.

**B. All-ones prefixes [V].** Least realizer `2^{k+1}−1`, `#leading d=1 = k`,
`R_k = k(1−α)`, prefix `W → 3` and mean weight `W/k → 0` (`0.602, 0.360, 0.248,
0.187, 0.150` at `k = 4,8,12,16,20`). **Small mean corridor weight does not make
an episode cheap in seed scale**: the least realizer is `2^{k+1}−1`, and that
height stays in the accounting.

**C. The Prop. 13.2 oscillator [V].** Digit `2` when `R_n ≤ c`, digit `1`
otherwise. At `c=1, N=200`: `P = 83` episodes of lengths `{1,2,3}`, occupation
`118`, `82` exits, least realizer `318` bits, and the realizer **reproduces the
word exactly**. `P` grows linearly in `N`, so no bound `P ≤ const(c,m_0)` can
exist — Prop. 13.2, confirmed. *My first implementation of this control was
wrong* (it tested `S_n+2` instead of membership at `n`, giving one episode of
length 200); corrected, not reinterpreted.

**D. The `−1` all-ones trajectory [V].** `T(−1) = −1`, `d=1` forever,
`R_n = n(1−α) → −∞`, so **every** `n` is occupied for every `c ≥ 0`: one
infinite episode, `O_c = ∞`. It satisfies the corridor condition with no
positivity. **The hypothesis the argument actually needs is `m_n ≥ 1` — the
positivity of the *states*, used in `𝓑_a ≥ m_0` and in `m_n ≥ m_0 2^{−c}` — not
positivity of the seed alone.**

**E. The affine recurrence over positive reals [V].** Fixing the word of
`285175` and running `x_{n+1} = (3x_n+1)/2^{d_n}` from
`x_0 ∈ {285175, 1/2, 10^6, 10^{−6}}`: the `R`-profile is prescribed by the word,
so corridor membership, `W_i` and `η_i` are **identical for every real `x_0`**.
`𝓑_a ≥ m_0` (i.e. `C_a > 0`) holds for every positive real start, and the entry
lemma is purely symbolic. **Therefore Proposition J is not an integer
obstruction** — it survives the relaxation unchanged, and is recorded as
symbolic/positivity-only, exactly as the brief requires.

## 5. [R] Refuted or closed in this round

| item | status |
|---|---|
| the joint carry-pot amortization (C1 as a route to Open Problem F) | **CLOSED.** Vacuous outside bounded two-sided drift (slack `3.5×` there, `10^4–10^7` elsewhere); that sector is already closed by `BoundedDrift.lean` |
| amortizing the pot to bound `O_c` from above | **REFUTED by direction.** The pot is `≥99%` gap weight, so the inequality it supports is `O_c > H − 2^{−c}pot`, a lower bound |
| the pot as a resource for EOC-strength conclusions | **CLOSED by scale.** `Θ(m_0)` resource against an `O(log m_0)` target |
| my working hypothesis that `A_i` is non-decreasing in `i` | **REFUTED** on 2 of 7 cases; replaced by the two-sided pin (which is Phase 6's statement) |
| a depth bound `w_max ≤ K log_2 O_c` with `K<1`, which the pot route requires | **not supported**: measured `w_max/log_2 O_c ∈ [1.16, 1.73]` |
| my control C as first written | **buggy, corrected** (tested `S_n+2`, not membership at `n`) |
| claiming J / J1 / the `Θ(m_0/log m_0)` scale verdict as new | **withdrawn**: all three are Phase 6 answers 3, 7, 8 |

## 6. Limitations

* Nothing here is Lean-verified. No `lake build` was run, no Lean installed. The
  Lean entries are **source-backed** by reading the files named.
* the Phase 7 gate-placement round (absent from the machine) is absent; its content is recovered only
  indirectly.
* The Downloads copy of `eoc_rev8.tex`/`.pdf` **differs** from the repository
  branch copy; the branch copy (`b2dcae2`) is the authoritative Rev 8 and is the
  one used — see `PROVENANCE.md` §1.
* `H`-dependence: `C1`'s `H^{1/9}` form requires pairwise distinct states and
  therefore **may not be applied after the first repetition**; it is not a
  total-occupation theorem.
* No claim about total occupation of the Prop. 13.2 seeds (their orbits beyond
  `N` are not analysed), preserving Remark 13.3's scope note.
