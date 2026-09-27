# REJECTED CANDIDATES

Relations that looked worth pursuing and did not survive. Each entry records the
exact reason, in the vocabulary of `PHASE0.md` Part II §6.

---

### R1 — "`m_n = 2^{-R_n}(m_0 + r G_n)` couples height to drift"

`G_n = C_n/q^n = (1/q) sum_{i<n} 2^{R_i}`, so the identity reads
`log2 m_n = -R_n + log2(m_0 + r G_n)`, with `G_n <= n/q` under confinement. It
looks like a bound linking the seed's size to the whole drift path.

**REJECT — RESTATEMENT (Filter 1).** It is the aggregate identity divided by
`2^{S_n}`, i.e. the programme's drift identity with the error term
`E_N = sum_k log2(1 + r/(q m_k))` written in closed form. It is an *identity*, so
it constrains nothing: every quantity in it is determined by the others.

### R2 — "the vacuous/active threshold at `lambda = 1/log2 3` is a new law"

The occupancy `E_B(n)` is exactly 1 below `lambda = 1/alpha = 0.6309` and departs
above it (Figure 1).

**REJECT — RESTATEMENT (Filter 1) and already in the repository.** It is
`audits/record_holder_anatomy` §5.6's exact fact ("for `j >= A[N]+1` the ratio is
identically 1") read on the `lambda` axis. Verified here on 216 cells with 0
violations, which is a pipeline check, not a finding.

### R3 — "the deficit band in the occupancy grid"

At fixed `n`, `E_B(n)` dips to `0.65-0.90` for `B` a few bits above
`log2 r_min(n)` and rises to `1.05-1.50` further out (Figure 1, and the detailed
table in `data/m1b_bitlength.txt`).

**REJECT — three reasons, any one sufficient.**
1. **Forced (Filter 1).** The cumulative count is exactly `2^{B-1} p_n(0)` once
   `B >= A[n]+1`, so `sum_b 2^b (E_b(n) - 1) = 0` identically: a deficit somewhere
   *must* be paid for by an excess elsewhere. The existence of both signs is a
   theorem, not an observation.
2. **Not significant (Filter 5).** Per-bitlength `z`-scores span `-3.4 .. +3.4`
   over ~200 cells with both signs and no organisation in `lambda`.
3. **Known where it is real.** The one systematic part — the excess immediately
   above `r_min(n)` at large `n` — is the clustering already **VERIFIED** in
   `audits/record_holder_anatomy` §5.6, and chain-root thinning removes it at
   `n=160` (`E = 1.43, z = +2.9` → `E_root = 1.07, z = +0.4`).

### R4 — "leading `1`-runs predict a small realizer"

Predicted in advance from L1/L2: prefixing a `1` multiplies the realizer by `2/3`
and raises `delta` by `log2 3`, so words with long leading `1`-runs should have
small realizers.

**REJECT — EQUIVALENT TO A KNOWN LEMMA (Filter 1), and invisible anyway.**
The identity is exact (C3) but the *inheritance* branch has probability `3^{-L}`
over the class, which is exactly the null's `P(delta > L log2 3)`. Measured:
`rho(lead1, delta)` is `-0.010, +0.005, +0.022` at `n = 40, 60, 200`, against
`4 SE = 0.020-0.028`. No signal. **The known mechanism reproduces the null
exactly and therefore cannot be detected in the marginal.**

### R5 — "confined integers are compressible: their block entropy is lower"

The letter-block entropy of the 83 587 confined integers below `2^36` came out
below the generic confined ensemble by `-0.0008 / -0.0016 / -0.0025` bits at block
lengths 1/2/3 — apparently the terminating tail showing up as compressibility.

**REJECT — ARTEFACT OF THE L1/L2 CHAINS (Filter 4/5), traced and quantified.**
Chain members share 139 of 140 letters with a shift of their parent, so the
plug-in entropy of the cohort is biased down by the reduced effective sample size.
Restricting to chain roots shrinks the gap to `-0.00029 / -0.00055 / -0.00095`,
against a null spread of `0.00016 / 0.00033 / 0.00050` measured from four
independent generic samples of matched size. The residue was then settled
decisively against the **exact rational letter law** with a word-level bootstrap:
`max |z| = 1.98` over `d = 1..10` (`data/m8_aggregate_letters.txt`). There is
no compression signal.

### R6 — "small confined integers have different words from large ones"

Coarse bit-length strata of the `n`-confined cohort showed `|t|` up to `5.7`
(`n_a4`, `n_a3`, `D_max`) — apparently size acting on word shape.

**REJECT — BINNING PLUS CHAIN CORRELATION (Filter 5).** A chain descends by
`log2(3/2) = 0.585` bits per step, so chains straddle bit-length boundaries and
the nominal Welch `t` is anticonservative. Replacing the strata with the
continuous statistic `rho(word statistic, log2 m)`, restricting to chain roots,
and taking the error bar from a chain-level bootstrap gives
`max |z| = 2.7, 1.7, 2.0` at `n = 140, 160, 180`
(`data/m4e_roots.txt`). Nothing survives.

### R7 — "the low bits of `m` are visible in deep letters"

`chi^2` between `m mod 32` and `a_k` is astronomically large at `k <= 4` and
decays; the decay looked as if it might not reach the null.

**REJECT — EXACTLY WHAT TERRAS–EVERETT PREDICTS (Filter 1).** `m mod 32`
*determines* the first few letters, and the residual dependence at intermediate
`k` is the confinement conditioning coupling the prefix to the future — present
in the ensemble law too. On chain roots with the degrees of freedom computed from
the non-empty cells, `z = 4.78, 2.69, 0.13, 0.09, -0.65` at `k = 10, 20, 50, 100,
139` (`data/m6_tail_propagation.txt`). It reaches the null by `k ~ 50` and
stays there.

### R8 — "`delta` has a non-uniform marginal"

**REJECT — measured, and it does not.** `P(delta > t)` against `2^{-t}` for
`t = 1..10`, 25 datasets, 4 maps, `n = 20..300`, `K = 20 000-40 000` each: not one
`|z| > 4` (`data/m2_delta_law.txt`, Figure 2).

### R9 — "some word statistic predicts `delta` at matched `S`"

**REJECT — measured, and none does.** Spearman `rho` with `S` partialled out, 27
statistics × 25 datasets: `max |rho| = 0.023`, not one exceeding `4 SE`
(`data/m3_dependence.txt`). Multivariate `R^2` on all 27 statistics sits at or
below the chance level `p/K` in every dataset, ratio `0.49-1.60`
(`data/m3b_tail.txt`).

### R10 — "the smallest realizers are word-atypical" (the record-holder question, at scale)

The 1 % of sampled words with the smallest realizers were compared with the rest,
standardised within each `S`-stratum.

**REJECT — they differ in `S` and in nothing else.** `t(S) = -34` to `-59` (which
H0 predicts exactly: a small realizer means a small class modulus), and
`max |t| = 2.4` over 27 other statistics × 25 datasets
(`data/m3b_tail.txt`). This is the record-holder anatomy conclusion — "the
extremes are generic" — reproduced with thousands of points instead of 24, at the
`1 %` tail.

### R11 — "a forbidden region or envelope in `(feature, delta)` space"

**REJECT — NONE EXISTS (Filter 5).** The apparent envelope per bin tracks
`log2 K_bin + 0.833`, the extreme-value prediction for `K_bin` i.i.d. draws, to
within `z in [-2.1, +6.9]` over ~200 bins per dataset — i.e. a sample-size
artefact. The only exact envelopes are the trivial `0 < delta <= S+1` and
`log2 r(w) < S+1` (`data/m4b_envelopes.txt`).

### R12 — "`delta_N <= c` uniformly would give the missing bound"

**REJECT — CIRCULAR (Filter 3), declared in advance.** A uniform bound on the
frontier deficit is the lower half of Sharp EOC, which implies
`r_min(N,0) -> infinity`, which is (DE). Measured here; never reported as a
finding.

---

## A correction to a control dataset, found on the way

Not a rejected candidate — a defect in an existing measurement that this audit had
to reproduce and therefore caught. It is written up in [`REPORT.md`](REPORT.md) §6
and carried out in [`../cross_map/CORRECTION_2026-09-25.md`](../cross_map/CORRECTION_2026-09-25.md).
