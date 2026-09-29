# Closed Pointwise Routes

**Consolidated 2026-09-29.** Central index of the audited negative results for the pointwise
problem. This is documentation: no theorem statement is changed, no proof is rewritten, and no
new mathematics is claimed.

Repository states audited: this repository at `5efd521`, `eoc-lean-verification` at `7866e5c`,
[`periodicity-conjecture-bridge`](https://github.com/innerlightr-wq/periodicity-conjecture-bridge)
at `d9d45ab`.

---

## 1. Why this document exists

Three independent falsification-first audits in September 2026 closed three natural routes to
the missing pointwise separator. Each closure is scoped precisely and each is reproducible. The
point of collecting them is to save the next reader — including the author — from rediscovering
them.

**What "closed" means here, and what it does not.** Each entry says: *this specific route, under
the hypotheses currently proved in this programme, does not yield a pointwise separator*, and
gives the exact obstruction. **No entry claims that no conceivable variant of the idea can ever
work**, and none of this bears on the Collatz conjecture, on `(DE)`, or on `(PosPC)`, all of
which remain exactly as open as before.

**Novelty discipline.** The qualitative closure of the symbolic and amortization routes was
already on record in this programme — Revision 7 §5.3 and **Observation 5.9**
(*"the separating invariant is height amortization, not symbolic complexity"*), Remark 9.5, and
the abstract's density exclusion — and the realizer-deficit route was already measured in
`audits/pointwise_discovery/`. The audits supply **an exact identity, a quantified obstruction,
and/or a larger-scale verification**, not the original qualitative observation.

---

## 2. Symbolic periodicity / the Periodicity Bridge

**Scope.** Whether the periodic-approximation and arithmetic-height mechanism of the
Periodicity-Bridge programme can exclude the surviving divergence sector.

**The dictionary is exact and free.** `x_i ≡ x_j (mod 2^L) ⟺ s[i:i+L] = s[j:j+L]`
(`Divergence.modEq_of_parity_prefix` one way, Terras / Bernstein–Lagarias bijectivity the other),
and for prefixes `lcp(s, W_ℓ^∞) = ℓ + v₂(m₀ − T^ℓ m₀)`. Verified on 400 random odd seeds below
`10¹²` × 12 000 triples and on every confined checkpoint of 17 record holders, 0 failures.

**The obstruction.** On an integer-realizable zero-confined orbit the bridge surplus *evaluates*:
with `F(W) = |2^ℓ−3^k| + c_W` and `h_eff := |M|/F(W) ∈ (0, m₀]`,

```
    M = m₀(2^ℓ−3^k) − c_W = 2^ℓ(m₀ − T^ℓ m₀) ,
    S(W) = lcp(s,W^∞) − log₂F(W) = log₂ h_eff − log₂ oddpart(T^ℓ m₀ − m₀)  ≤  log₂ m₀ ,
```
verified at **1 862 confined checkpoints, 0 failures**. So `limsup S = +∞` is **unsatisfiable**
on the realizable sector, not merely unproved.

**Confinement forces no repetition.** The zero-confined sector carries entropy
`H₂(1/α) = 0.949956` bits per standard letter; an explicit construction turns any bit stream
into a confined word (the Champernowne instance: `p(18) = 3 543`, longest initial square
half-length **3**). Survivor windows are essentially unbordered (longest proper border 0 in 13
of 18) with `p(12)` at 87–100 % of the combinatorial ceiling. Max surplus over 20 random
confined words: **2.53 … 11.48**; over certified survivor windows: **2.000 … 8.717**, tracking
`log₂ m₀` rather than window length.

**The bridge's headline class misses the sector by density.** CS Rote sequences have one-density
**exactly 1/2** — the bridge's own load-bearing fact, the one that drops the required repetition
exponent to 2 — while confinement forces one-density `≥ β = 0.6309297535714575`. Over 2 000
shifts × both seeds × 4 slopes the best confined depth is **5–13** at `c = 0` and **317–333** at
`c = 64`.

**Why the gap is circular.** An initial square of half-length `L` in the parity word of an
integer `n₀` forces `4^L ≤ 3^L(n₀+1)`, i.e. `L ≤ 2.4094 log₂(n₀+1)` (measured on record
holders: **1–8** against caps 7–63). Hence *"EOC constraints ⟹ arbitrarily long initial
squares"* holds **iff** `(DE)` holds.

Full record: [`notes/PERIODICITY_HANDOFF_ROUTE_CLOSED.md`](PERIODICITY_HANDOFF_ROUTE_CLOSED.md).
Companion on the bridge side:
[`docs/EOC_HANDOFF_CLOSED.md`](https://github.com/innerlightr-wq/periodicity-conjecture-bridge/blob/main/docs/EOC_HANDOFF_CLOSED.md).

---

## 3. Drift / carry / amortization

**Scope.** Whether the carry, in drift coordinates, supplies a reproducible constraint curve.

**Exact identities** (sign convention `R_n = nα − S_n ≥ 0`, the **opposite** of this
repository's own `R_n = S_n − nα`; this is the likeliest transcription error):

```
    C_n / 3^n  =  (1/3) Σ_{j<n} 2^{−R_j}  =:  U_n / 3                     (I3, 779 ✓)
    U_{n+1} − U_n  =  2^{−R_n}                                            (662 pairs ✓)
    U_n  =  3 m₀ ( Q_n − 1 ) ,   Q_n = ∏_{i<n}(1 + 1/(3 m_i))             (I4/I5, 779 ✓)
    A_n := log₂ m_n − R_n = log₂ m₀ + log₂ Q_n                            (I6, 779 ✓)
```

**Why it is not an independent separator.** `Q` is the **Eliahou–Rozier carry product**, already
defined, formalized and attributed in `Divergence/LastMaximum.lean` (`rho_mul_orbit`,
`Q_le_exp`). So the "amortization residual" is `log₂` of an existing object, and
`A_n = log₂(m₀ + (1/3)Σ2^{−R_j})` is a deterministic functional of `(m₀, R_0…R_{n−1})` — no
independent degree of freedom. Numerically it degenerates: `A_N − log₂ m₀ < 10⁻⁶` for every
certified seed above `10⁶`, down to `3.3·10⁻¹²` at `m₀ = 8.99·10¹¹`.

**The cumulative cost converges.** `E_n := log₂ Q_n` is strictly increasing, exactly telescoping
(`E_n − E_{n−1} = log₂(1 + 1/(3m_{n−1}))`), and **bounded** on divergent orbits by
`Divergence.summable_inv_orbit` + `Q_le_exp`. One bit of cost needs `≈ 3m₀` corridor steps;
certified record holders spend **2–9**.

**New but inconsequential inequality.** `3^n − 2^n ≤ C_n ≤ 3^{n−1}Σ_{j<n}2^{−{jα}}`, the upper
bound attained only by the critical Sturmian word, verified at **3 444 checkpoints, 0
violations**. It improves the previously recorded `3^{n−1} ≤ C_n ≤ n·3^{n−1}` by ×3 below and
`1/(2 ln 2) = 0.7213` above — `0.47` bits. Saturation `U_N/V_N` falls from **0.2615** at
`N = 36` to **0.0248** at `N = 346`: record holders recede from the envelope.

**No realizability effect.** Rank test, 22 record holders each against 400 uniform confined
words of its own length: **mean rank 0.482** (null 0.500, sd of the mean 0.062), **z = −0.30**,
10/22 below 0.5. Null — reproducing, in a new coordinate, the M1 finding of
`audits/pointwise_discovery/`.

Full record: `~/scratch/eoc-amortization-constraint-curve-2026-09-29/AMORTIZATION_CURVE_VERDICT.md`.

---

## 4. Realizer deficit `δ`

**Definition** (this repository's own, `audits/pointwise_discovery/PHASE0.md`; `r(w)` is
Lean-formalized as `EOC.leastRealizer`, the logarithm is not):

```
    r(w) = 3^{−n}( 2^S − C_n )  mod 2^{S+1} ,  least positive representative
    δ(w) := (S + 1) − log₂ r(w)   ∈ (0, S+1] .
```

**It does add modular information.** `U_n` reads `C_n` archimedeanly, `δ` reads it 2-adically;
neither determines the other. Over 4 000 distinct confined permutations of one fixed letter
multiset — identical `N`, `S_N`, density and letter counts — `δ` ranges over **[0.000, 12.32]**.

*(Correction: an earlier audit note said `δ` is "not a functional of the drift path". That is
wrong as stated — the drift path determines the word, hence everything. `δ` is a **different**
function of the word than `U_n` is.)*

**But it is structureless.** Marginal law against the null `P(δ>t) = 2^{−t}` (mean
`1/ln2 = 1.442695`, median 1): two sampling laws × `N = 40, 80, 150`, **96 000 words**,
**max |z| = 1.83 over 36 tail tests**. Joint with the amortization coordinate:

```
    ρ(U_N, δ) = +0.0097 (z=+1.38),  +0.0023 (z=+0.32),  +0.0108 (z=+0.96)
    S-partialled: all |z| < 1.4;   conditional median δ by U-quintile: 0.97 … 1.10 (null 1, flat)
```

This repository's own **M3** had already done the equivalent against 27 word statistics × 25
datasets with `S` partialled out (`max|ρ| = 0.023`, zero exceedances of 4 SE) — and its feature
list contains `logZ = log₂ Σ 2^{−D_k}`, which *is* the amortization coordinate.

**No envelope beyond `0 < δ ≤ S+1`.** Both ends attained (`min δ = 0.000` inside the permutation
class), no gap, no forbidden interval, no residue-class exclusion (stratifying by `r mod 8`
(populations 3 341 : 16 659), `r mod 12`, `v₃(r+1)` gives conditional means **1.429–1.488**
against the null 1.443).

**Conditioning does not distinguish actual realizers, and the question is partly ill-posed.** At
finite depth every confined word is realized by its own least realizer, and "actual realizer
below `2^B`" is *identical* to `δ(w) > S(w)+1−B` by the finite-height reduction of
`audits/pointwise_discovery/`. The non-circular residue — the shape of the truncated law — was
tested by complete enumeration of all **14 487** odd `m < 2^{22}` that are 30-confined:
`z = −3.68, −1.53, +0.73, −0.32, +0.04, −0.48`; after chain-root thinning (9 747 of 14 487)
`z = −3.29, −1.54, +0.48, −0.64, −0.11`. One bin of six at `|z| ≈ 3.3`, at `B = 22` against
`A[30]+1 = 48` where the identity is a heuristic and not a theorem, and inside the `[−3.4,+3.4]`
spread M1 documents over ~200 comparable cells. **Not a signal.**

**Along an actual orbit `δ` is the height, relabelled.** `δ(w_n) = S_n + 1 − log₂ m₀` once
`m₀ < 2^{S_n+1}` (`EOC.residue_pinning`): a straight line of slope `≈ α` (measured 1.44–1.61),
gap to the ceiling constant at `log₂ m₀`, no saturation. Record-holder `δ`: **52.245 … 512.490**.

**Extremal behaviour is the null's.** Exhaustive enumeration of all confined words to `N = 16`
(**312 455** words at `N = 16`): `max_w δ(w) ≈ log₂(#confined words)` to within 0.8 for
`N = 9…16` — the extreme order statistic of an iid geometric(1/2) — hence
`log₂ r_min(N) ≈ I₀N`. The same search independently reproduces `r₁(N) = 27` for `N ∈ [9,16]`,
agreeing with the certified scan by a different route.

**Circularity.** `δ` is defined through `r`, and `r` is a least positive representative, i.e. a
height. A uniform bound on it is `r_min(N,0) → ∞` — form **(b)** of
[`docs/EQUIVALENT_FORMS_OF_DE.md`](../docs/EQUIVALENT_FORMS_OF_DE.md), the file that states
*"A reformulation into any of (b), (c) or (d) is **not** progress on (DE)."*

Full record: `~/scratch/eoc-realizer-defect-audit-2026-09-29/DELTA_VERDICT.md`.

---

## 5. Control systems

The accelerated **`3x−1`** map is the decisive control throughout, and its role is the same in
all three audits. It shares with `3x+1` the aggregate identity, the confinement condition, the
carry recurrence `C_{n+1} = 3C_n + 2^{S_n}`, the modulus `2^{S+1}` and the residue structure. It
differs in one sign: `2^{S_n}m_n = 3^n m₀ − C_n`.

| audit | what the control does |
|---|---|
| periodicity | `+1` is a zero-confined **positive** point of `3x−1`; its parity word is `(1)^∞ = W^∞`, so the bridge is correctly **silent** — but that also means it adds nothing the proved sign obstruction did not predict |
| amortization | `m_n = 2^{R_n}(m₀ − U_n/3)`: the amortization term enters with the **opposite sign**, so every candidate "cost" becomes a credit, and `m = 1` has `m₀ − U_n/3 = (2/3)^n` exactly and survives forever |
| realizer deficit | `m = 1` has word `1^n`, `r(w) = 1`, hence **`δ = S+1`, the maximum possible value, at every depth, forever** — which kills the whole *"large `δ` ⟹ escape"* family in one line |

This is exactly the scope of this programme's **proved** sign-symmetry obstruction
([`docs/PROGRAMME_ENDPOINT.md`](../docs/PROGRAMME_ENDPOINT.md)): *no argument using only the
aggregate identity, the confinement condition and the sign of the denominator can separate the
positive integers from the rest of `K`*. All three closed coordinates are built from those three
inputs.

---

## 6. Negative-results table

| ROUTE | KEY QUANTITY | WHAT IT ADDS | WHY IT FAILS | CONTROL | STATUS |
|---|---|---|---|---|---|
| **Low symbolic complexity** | `p_s(L)` | a proved complexity floor for divergent orbits, `p_s(L) ≥ ⌊(L−1−log₂m₀)/log₂(3/2)⌋+1` (a specialization of the source paper's Prop. 9.2, **not** new) | the confined sector has entropy `H₂(1/α) = 0.949956` bits/letter — exponential vs linear; and the Dubickas threshold `1/log₂(3/2) = 1.7095112913514547` is *exactly* the constant the floor already supplies, so the counting rung has zero margin | silent on `3x−1`; correctly silent on `5x+1` where `log₂5 > 2` | **CLOSED** |
| **Periodic-approximation surplus** | `S(W) = lcp(s,W^∞) − log₂F(W)` | an exact evaluation on the confined sector | `S(W) = log₂ h_eff − log₂ oddpart(m_n−m₀) ≤ log₂ m₀`, an identity with the aggregate identity; and the required lemma is equivalent to `(DE)` (`4^L ≤ 3^L(n₀+1)`) | `3x−1`'s `+1` is periodic, so the criterion is correctly silent | **CLOSED (circular)** |
| **Amortization / drift** | `U_n = Σ_{j<n}2^{−R_j} = 3C_n/3^n = 3m₀(Q_n−1)` | the exact carry integral and the increment identity `ΔU_n = 2^{−R_n}` | `U_n` is a functional of the drift path; `E_n = log₂Q_n` converges on divergent orbits (`summable_inv_orbit`); one bit of cost needs `≈3m₀` corridor steps against 2–9 observed; rank test **0.482**, `z = −0.30` | sign flips in `3x−1`: cost becomes credit, `m=1` survives forever | **CLOSED (identity only)** |
| **Realizer deficit `δ`** | `δ(w) = (S+1) − log₂ r(w)` | genuine 2-adic information: range `[0.000, 12.32]` at fixed drift statistics | marginal is the null geometric(1/2) (`max|z| = 1.83` / 36 tests; M2: no `|z|>4` over 25 datasets); `ρ(U,δ)` `|z| < 1.4`; no envelope past `0 < δ ≤ S+1`; along an orbit it is `S_n+1−log₂m₀`, the height relabelled | `3x−1`'s `m = 1` sits at `δ = S+1`, the **maximum**, forever | **CLOSED as a separator** |
| **Sign-symmetric carry-cost ideas** | any cumulative cost built from `C_n` | — | `3x+1` and `3x−1` share the aggregate identity, confinement and the carry recurrence, and differ only in the sign of `C_n`; a cost in one is a credit in the other | this *is* the control | **CLOSED by a proved obstruction** |

---

## 7. What remains

The missing pointwise separator must use information **not already functionally determined by**:

* parity/symbolic complexity of the valuation word;
* periodic-approximation surplus (any packaging: squares, general powers, low-discrepancy roots,
  near-critical resonance — they all enter through the same `lcp` and the same `F(W)`);
* the drift path `(R_j)`;
* the carry / amortization integral `U_n` (equivalently `C_n/3^n`, `Q_n`, `A_n`, `E_n`);
* the least-realizer deficit `δ` alone.

Equivalently, in this programme's own words (Revision 7 §5.3): every tool whose only arithmetic
input is *"a nonzero multiple of `2^m` has absolute value at least `2^m`"*, applied to the
aggregate identity, is now known to evaluate on the confined sector to a restatement of
Lemma 2.4.

`(DE)`, `(PosPC)`, Sharp EOC and Open Problem C are **unchanged and open**.

**One unverified external direction, recorded without endorsement.** arXiv:2607.10041 attaches
to each accelerated exponent code a *2–3–∞ diagnostic*: drift, a 2-adic start representative
(= `r(w)`, i.e. `δ`), **and a 3-adic endpoint representative `M_k`** — the only coordinate none
of the three audits used. It is **UNVERIFIED**: that paper is explicitly *"not a verification
method … but a symbolic diagnostic approach"*, and its 2-adic unconditional result appears
immediate from `residue_pinning`. Before any computation, the question to settle by reading is
whether `M_k` reduces to `Descent` **L7** (*forward motion cannot accumulate 3-adic budget*),
given that [`audits/descent/DESCENT_AUDIT.md`](../audits/descent/DESCENT_AUDIT.md) marks the
descent route **STOP** and notes that any descent statement over `ℤ` is equivalent to `(DE)`.

---

## 8. Reproducibility

Audit workspaces (not committed here; local scratch, each self-contained):

| workspace | verdict file | scripts |
|---|---|---|
| `~/scratch/eoc-periodicity-handoff-audit-2026-09-29/` | `HANDOFF_VERDICT.md` | `scripts/{bridgecore,integer_collapse,complexity_handoff,confinement_structure,sector_intersection,shift_robust_and_windows,controls,ladder_and_carry}.py` |
| `~/scratch/eoc-amortization-constraint-curve-2026-09-29/` | `AMORTIZATION_CURVE_VERDICT.md` | `scripts/{amort,verify_identities,checkpoints,envelope_search,rank_test,control_and_critical}.py` |
| `~/scratch/eoc-realizer-defect-audit-2026-09-29/` | `DELTA_VERDICT.md` | `scripts/{delta,verify_delta,compute_delta_joint,extremal_and_controls,integer_cohort}.py` |
| `~/scratch/eoc-negative-results-consolidation-2026-09-29/` | `SOURCE_OF_TRUTH.md` (+ `NEGATIVE_RESULTS_REPO_FREEZE.md`) | — |

All scripts are standard-library Python, every pass/fail decision is exact integer or `Fraction`
arithmetic, and outputs are saved under each workspace's `data/`. Run any of them with
`python3 <script>.py` from its own `scripts/` directory.

In-repository sources the audits read:
[`Divergence/Basic.lean`](../Divergence/Basic.lean) (`a`, `T`, `S`, `C`, `aggregate_identity`),
[`Divergence/CycleDrift.lean`](../Divergence/CycleDrift.lean) (`ZeroConfined`),
[`Divergence/LastMaximum.lean`](../Divergence/LastMaximum.lean) (`rho`, `Q`, `rho_mul_orbit`,
`Q_le_exp`), [`Divergence/RawMap.lean`](../Divergence/RawMap.lean)
(`modEq_of_parity_prefix`, `U_iter_shift`), `Divergence/Summable.lean`
(`summable_inv_orbit`), [`audits/pointwise_discovery/`](../audits/pointwise_discovery/)
(`PHASE0.md`, `CANDIDATE_CONSTRAINTS.md`, `REPORT.md`, `scripts/words.py`, M1–M9),
[`audits/record_holder_anatomy/REPORT.md`](../audits/record_holder_anatomy/REPORT.md)
(the certified `r_min(N,0)` table, `N = 1…346`),
[`audits/descent/DESCENT_AUDIT.md`](../audits/descent/DESCENT_AUDIT.md) (L1/L2/L4/L7);
and `EOC/Realizer.lean`, `EOC/Carry.lean` in `eoc-lean-verification`.

Formalization targets for these closures:
[`docs/CLOSED_ROUTES_FORMALIZATION.md`](https://github.com/innerlightr-wq/eoc-lean-verification/blob/main/docs/CLOSED_ROUTES_FORMALIZATION.md).
