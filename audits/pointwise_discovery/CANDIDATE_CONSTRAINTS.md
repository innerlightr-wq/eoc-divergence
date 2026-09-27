# CANDIDATE CONSTRAINTS

Every relation that survived to the point of being written down, with the full
audit trail required by `PHASE0.md` Part II §6.

**Summary: no candidate pointwise constraint was found.** What follows is
(i) three exact identities that were *verified* here and are recorded because
they organise the problem, all of them restatements of known mathematics; and
(ii) one *measured contrast* that is new as a measurement, is not a constraint,
and is negative for (DE).

---

## C1 — the finite-height reduction (EXACT; a restatement)

> For a rare-side word `w` of length `n` with total `S`, let
> `r(w) = q^{-n}(2^S - r C_n(w)) mod 2^{S+1}` be its least realizer and
> `delta(w) = S + 1 - log2 r(w)`. Then for every `B`,
> ```
>   { odd m < 2^B : m is n-confined }  <->  { w : delta(w) > S(w) + 1 - B }
> ```
> is a bijection whenever `n >= B - 1`, and
> ```
>   #{odd m < 2^B : n-confined} = 2^{B-1} p_n(0)   exactly, whenever A[n] + 1 <= B.
> ```

* **How discovered.** Written down in §1 of the design before any measurement, as
  the exact answer to *After the Reduction* §(f)'s question.
* **Domain tested.** Brute force at `(B,n) = (12,12), (14,14), (13,14)` — the
  bijection, 0 violations; and the counting identity on 216 grid cells of
  `B = 8..32`, `n = 1..280`, 0 violations (`data/m1_lambda_grid.txt`).
* **Is `B` essential?** Yes, but only through the single scalar threshold
  `S+1-B`.
* **Symbolic reduction.** It **is** the Terras–Everett correspondence plus the
  aggregate identity. **REJECT — RESTATEMENT (Filter 1).**
* **Interpretation, and why it is worth recording.** It says precisely what
  finite height can and cannot do. All of the content of `m < 2^B` at depth `n`,
  beyond the word itself, is the one number `delta(w)`. Consequently:
  * the regime `lambda = n/B <= 1/log2 3 = 0.6309` is **provably vacuous** — finite
    height imposes nothing there (and this is the repository's own §5.6 fact on
    the `lambda` axis);
  * the regime `lambda >= 1 - 1/B` is where one integer realizes one word;
  * and **the missing law of §(f) is exactly a law for the joint distribution of
    `(S(w), delta(w))`.** Nothing else can carry it.

## C2 — the `+/-` realizer involution (EXACT; new as a statement, trivial as mathematics)

> For every odd `q`, every word `w` of total `S`:
> `r_{q,+1}(w) + r_{q,-1}(w) = 2^{S+1}`, hence
> `2^{-delta_-} = 1 - 2^{-delta_+}`.

* **Verified** for `q = 3, 5, 7` over 900 random words, 0 violations
  (`data/v_structure.txt`).
* **Consequence.** The uniform-class null is invariant under `r -> -r`, so the
  `3x+1` / `3x-1` pair carries **no independent realizer information**; a claim
  about one is a claim about the other. It also explains why the `5x+1` and
  `5x-1` rows of the dependence tables are exact mirror images when the same
  words are drawn.
* **Filters.** Restatement of the aggregate identity (the carry changes sign).
  **REJECT — RESTATEMENT.** Recorded because it collapses two of the mandatory
  controls into one and is one line to prove.

## C3 — the L1/L2 chain law in the `delta` coordinate (EXACT; a restatement of L1/L2)

> If `3 | r(w)+1` then `r(1.w) = (2 r(w) - 1)/3` exactly, and
> `delta(1.w) = delta(w) + log2 3 - log2(1 - 1/(2 r(w)))`.
> Otherwise `delta(1.w) <= log2 3`.

* **Verified**: 1319 inheritance cases, 1319 exact; 2681 non-inheritance cases,
  all with `delta(1.w) <= log2 3`; inheritance frequency 0.3297 against the
  predicted `1/3` (`data/v_structure.txt`).
* **Filters.** This is (L1) and (L2) of the `Descent` library, rewritten.
  **REJECT — RESTATEMENT.**
* **Why it matters here.** It is the *only* known mechanism coupling word shape
  to realizer size, and it is what every measurement below had to be residualized
  against. And it explains the cleanliness of the nulls: inheritance to depth `L`
  has probability `3^{-L}` over the class, while the uniform null gives
  `P(delta > L log2 3) = 2^{-L log2 3} = 3^{-L}`. **The known mechanism reproduces
  the null exactly**, so it leaves no marginal signature. *(The identity is
  verified; the reading is* **HEURISTIC**.*)*

---

## M1 — the size fingerprint, measured (NOT a constraint; a negative contrast)

This is the one genuinely new *measurement*. It is not a candidate constraint —
it constrains nothing — but it is the sharpest thing this experiment produced.

> **Statement.** At depth `n = 140`, over a complete enumeration of the
> rare-side-persistent odd integers below `2^36` (`3x+1`) and `2^32` (`5x-1`),
> the aggregate letter law of the integer cohort, tested against the **exact**
> rational ensemble law with a word-level bootstrap:
>
> | map | cohort | max \|z\| over `d = 1..10` | `P(a=1)`: observed − exact |
> |---|---|---|---|
> | `3x+1` (chain roots) | 55 665 | **1.98** | `+1.3e-4 ± 1.1e-4` |
> | `3x-1` (all) | 5 143 | 4.82 | `+5.3e-5 ± 3.6e-4` |
> | `5x-1` (all) | 406 761 | **465.7** | `-8.5e-2 ± 1.8e-4` |
> | `5x-1`, already cycled | 140 504 | 1167.9 | — |
> | `5x-1`, still injective | 266 257 | 177.7 | — |

* **How discovered.** M7–M9, after M2–M6 returned null; the `5x-1` run was
  pre-registered as the power calibration, not as a hypothesis.
* **Mechanism, and it is proved, not fitted.** For `5x-1` persistence forces
  `m_n < m_0` at every `n` (Proposition 5x−1, the pigeonhole step), so the orbit
  is trapped in `[1, m_0]`; measured here, **34.54 %** of the cohort has already
  repeated an orbit value by depth 140. For `3x+1` the rare side is the growth
  side: **0** of 83 587 confined orbits repeat a value (forced —
  `Divergence.not_zeroConfined_of_repeat`) and **100 %** have the seed as their
  minimum through depth 140 (`data/m9c_3x1_no_capture.txt`).
* **Controls.** This *is* the control battery. The map on which an elementary
  archimedean argument settles the question shows the effect at ~470 sigma; the
  map on which the question is open shows it at < 2 sigma, on a cohort with
  comparable power.
* **Is `B` essential?** Yes — the effect is entirely a finite-height effect. That
  is the point: it exists on `5x-1` and is absent on `3x+1`.
* **Symbolic reduction.** The `5x-1` side reduces to Proposition 5x−1. The `3x+1`
  side is a null and reduces to nothing.
* **Holdout.** Null on the pre-registered holdout (`n = 100,150,200,300`,
  `B = 24,26,28`) and on the extended range (`n = 140,160,180,200`, `B` to 36),
  declared after the primary holdout returned null.
* **Interpretation.** The programme states, qualitatively, that the difficulty of
  (DE) is that for `3x+1` the rare side is the growth side, so no bounded orbit is
  available and pigeonhole cannot be run (*After the Reduction*,
  Remark "what the obstruction does not explain"). This measures that statement:
  the archimedean channel through which size acts on `5x-1`'s word data is
  **quantitatively absent** for `3x+1`, by a factor of ~650 in effect size and
  ~235 in significance, on cohorts of comparable size at the same depth.
* **Verdict.** **Negative for (DE).** It closes a route rather than opening one:
  any tool hoping to read finite height out of `3x+1` deep word statistics has to
  find it below the `1.1e-4` level at which the letter law is now measured to be
  exactly generic.

---

## Nothing else reached this file.

Everything measured in M2, M3, M3b, M4, M4b, M4c, M4d, M4e, M6 was consistent
with the uniform-class null. The quantitative bounds are in [`REPORT.md`](REPORT.md) §4
and the attempted relations that looked promising and failed are in
[`REJECTED_CANDIDATES.md`](REJECTED_CANDIDATES.md).
