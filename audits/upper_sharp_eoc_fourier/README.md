# Upper-Sharp-EOC Fourier round — consolidation record

> **Verdict: PAUSE — no supported dyadic mechanism.** The Fourier route to the upper half of
> Sharp EOC is not refuted and not supported. Its best possible outcome is `c ≈ 0.832`, not `I_0`.
> The missing input is **Lemma D1**. Nothing here bears on (DE), divergent orbits, or Collatz.

This folder records what one round of research established, so that it is not lost. It is a
**consolidation record, not new research**: nothing was extended, no new route was pursued.

- [`FINDINGS.md`](FINDINGS.md) — every result, one per section, each with a status label
- [`OPEN_PROBLEMS.md`](OPEN_PROBLEMS.md) — Lemmas D1 / D2 and the construction question, stated precisely
- [`NON_ROUTES.md`](NON_ROUTES.md) — routes examined and why they do not work
- [`scripts/`](scripts/) — five standard-library Python checks; [`results/`](results/) — their stored transcripts

---

## Scope

**The target.** Open Problem 8(4) of *After the Reduction* (v2.3,
[doi:10.5281/zenodo.22961534](https://doi.org/10.5281/zenodo.22961534)): is there `c < 1` with
`r_min(N,0) ≤ 2^{cN}` for all large `N`? The elementary bound there gives `c = 1`; the conjectured
value is `c = I_0 ≈ 0.0793`; nothing between the two is known.

**Why the target does not resolve divergence.** It is an **upper** bound on the frontier — an
existence statement about *small* zero-confined integers. (DE) is equivalent to
`r_min(N,0) → ∞`, a **lower** bound. By the synthesis note's Remark 4.9 the upper half does not
imply (DE) and is open independently of it; it is consistent with (DE) being true. An affirmative
answer would establish only that relatively small finite survivors exist at each depth. **It would
not establish `r_min(N,0) → ∞`, universal drift exit, or the absence of divergent orbits.**

**The ensemble.** The terminal shell: `0`-confined positive valuation words of length `N` with
terminal sum exactly `S = A[N]`. Modulus `Q = 2^{S+1}`. Uniform weights — within one shell every
word has geometric density `2^{−S}`, and `D ↦ r(D)` is injective on the shell (verified exactly).
**No shells were mixed anywhere.** Normalization
`F_N(h) = (1/M_N)·sum_D exp(2 pi i·h·r(D)/Q)`, `F_N(0) = 1`.

---

## Conventions, and where each one comes from **in this repository**

Checked against the `Occupation`, `Divergence` and `Descent` libraries of this repo before any
file in this folder was written. **No convention differs.** Two are *absent* here rather than
different, and are marked as such with their external source.

| convention | source in **this** repository | status |
|---|---|---|
| `s_j = d_0 + … + d_{j−1}`, `S = s_N` | [`Occupation/Compositions.lean:37`](../../Occupation/Compositions.lean) `psum`; `:50` `psum_total` | **matches** |
| carry `q_0 = 0`, `q_{j+1} = 3q_j + 2^{s_j}` | [`Divergence/Basic.lean:52`](../../Divergence/Basic.lean) `C`; `:57` `C_succ` (orbit-indexed; evaluated on a prescribed word in the scripts) | **matches** |
| closed form `q_N = sum_{j<N} 3^{N−1−j}·2^{s_j}` | *absent*. Closest here: `Divergence/Basic.lean:138` `aggregate_identity`, `2^{S_n}·orbit m n = 3^n·m + C m n` | **absent here**; external source `EOC/Carry.lean` `q_eq_C` (`eoc-lean-verification`). Verified exactly in `check_additive_formula.py` §2 |
| realizer congruence `3^N·m + q_N ≡ 2^S (mod 2^{S+1})`; least realizer = unique residue below `2^{S+1}` | *absent*. `aggregate_identity` above is its precursor | **absent here**; external source `EOC/Realizer.lean:286` `realizerCongruence`, `:459` `leastRealizer`. Verified exactly in `check_realizers.py` §1 |
| zero confinement: `2^{s_j} ≤ 3^j` for all `j ≤ N`, exact integer test | [`Descent/Basic.lean:29`](../../Descent/Basic.lean) `ConfinedUpTo`; [`Occupation/Compositions.lean:62`](../../Occupation/Compositions.lean) `Confined 0`; [`Divergence/CycleDrift.lean:30`](../../Divergence/CycleDrift.lean) `ZeroConfined` | **matches**, three independent definitions |
| `A[k] = floor(k·log2 3)`, as `(3**k).bit_length() − 1` | [`Occupation/Rate.lean:71`](../../Occupation/Rate.lean) `sN N = Nat.log 2 (3^N)`, pinned by `:73` `two_pow_sN_le` and `:76` `lt_two_pow_sN_succ` | **matches** |

Two further definitions of this repository are used directly as `[P]` inputs:

| fact | source | used for |
|---|---|---|
| every `0`-confined odd `m` has `a m = 1` and `m ≡ 3 (mod 4)` | [`Descent/ResidueLaw.lean:21,33`](../../Descent/ResidueLaw.lean) `a_eq_one_of_confined`, `mod_four_of_confined` | the forced `mod 4` Fourier peak (`FINDINGS.md` §2) |
| `r_min(N,0)` as `IsLeast {m \| Odd m ∧ ConfinedUpTo N m}` | [`Descent/ResidueLaw.lean:55`](../../Descent/ResidueLaw.lean) `least_confined_mod12` (L4) | the direct-scan definition used in `check_realizers.py` §5 |

---

## Label legend

| label | meaning |
|---|---|
| `[P]` | proved, with cited inputs |
| `[V]` | verified by exact computation in this branch's scripts, **for the stated finite range only** |
| `[F]` | float / numerical diagnostic only — not a proof |
| `[C]` | conjectural, or a missing lemma |
| `[R]` | refuted / negative result |
| `[D]` | reported from discussion, not re-checked in this branch |

Labels are never upgraded. Exact integer arithmetic decides every mathematical assertion; floats
appear only in Fourier diagnostics and are always labelled `[F]`.

---

## Running the scripts

```
cd audits/upper_sharp_eoc_fourier/scripts
python3 check_counts.py              # [V] confined-word counts, shell sizes
python3 check_realizers.py           # [V] congruence, injectivity, mod 4, orbit replay, r_min, lift weights
python3 check_additive_formula.py    # [P]/[V] the additive realizer formula; the (1,2)/(2,1) carries
python3 check_dyadic_tower.py        # [V] the dyadic tower identity and the prefix collapse, exactly
python3 fourier_diagnostics.py       # [F] Fourier diagnostics; [V] exact interval hits
```

Standard library only. Nothing is written to disk — every script prints to stdout and exits
non-zero on any failed assertion. `--quick` reduces the range on each;
`fourier_diagnostics.py --cet=3.0` changes the Erdős–Turán constant parameter. Full-run transcripts
are stored in [`results/`](results/); every number quoted in `FINDINGS.md` appears in one of them.
Total runtime for all five, full range: under 15 seconds; peak memory well under 1 GB.

The band-mean figures in `fourier_diagnostics.py` §§4–5 are **seeded Monte-Carlo estimates**
(seed `20261013`): deterministic and reproducible, but not exact. Their third significant figure
moves with the probe count, and the reported Erdős–Turán margins shift by about `±0.1` in the
exponent.

---

## What this does not establish

- **Nothing about (DE)**, divergent orbits, universal drift exit, or Collatz. Nothing about
  `r_min(N,0) → ∞`.
- **No asymptotic law.** The only positive finite result is `r_min(N,0) ≤ 2^{0.9N}` for `N ≤ 16`
  (`[V]`). It certifies neither the Fourier estimate nor any statement for large `N`.
- **Float diagnostics are not proofs.** The DP agrees with brute force to `≤ 5.4e−13`, which bounds
  the *implementation*, not any estimate. No rigorous numerical error bound was established for the
  large-`N` DP values.
- **`C_ET` was not verified against a printed primary source.** It is a stated parameter. The
  verdict is unchanged for any `C_ET ∈ [1,10]` because the margins are `2^5`–`2^8`; a theorem would
  need the constant pinned down.
- **The projections are extrapolations.** The `N ≈ 92 / 132 / 254` figures extrapolate a fitted
  count asymptotic under an unverified uniformity hypothesis. They are feasibility estimates, not
  evidence.
- **Lemma D1's actual range was never probed.** Measurements live at `h ≤ 1024` and sparse random
  probes; D1 quantifies over odd `h` up to `2^{alpha·N}`.
- **Six depths, strongly structured.** `N = 15,…,50` with `log2(M_N)/N` still `0.2` below its
  limit. That is weak evidence about an exponential law.
- **The terminal-shell minimum is not `r_min`.** It overestimates by up to `13.30×` on `N ≤ 14`
  (`[V]`). Combining shells requires the common modulus `2^{A[N]+1}` and the lift weights
  `2^{A[N]−S}`; one least realizer per word is not the uniform measure on survivors.

---

## Novelty

**The additive realizer formula is prior art, not a finding of this round.** It is Lemma 2.1
(with Definition 2.2) of *The Sturmian–Mahler Edge of the Accelerated Collatz Realizer Problem*
(June 2026), used there in the proof of Theorem 4.1, and it is equivalent to Proposition 5.2 of
EOC Revision 8 ([doi:10.5281/zenodo.23146031](https://doi.org/10.5281/zenodo.23146031)). Both
citations were **confirmed in this round** against the local copy
[`audits/sturmian_irrationality/sources/B_Sturmian_Mahler_Edge.pdf`](../sturmian_irrationality/sources/B_Sturmian_Mahler_Edge.pdf).
The only new content here is its *use* as an `O(N²)`-state dynamic program over the whole confined
ensemble. See [`FINDINGS.md`](FINDINGS.md) §1.

**What a keyword scan of the author's own notes found `[D]`.** Reported, not re-run in this branch:
a keyword scan of EOC Rev 8, the Sturmian–Mahler Edge note and its addendum, the *2-Adic Sturmian
Carry Constant* note, *Three Scales of Confinement*, the Sturmian irrationality paper, and *Beyond
Sturmian Words* found the **additive formula already stated**, but **no D1/D2-type Fourier
statement**.

**Nearest relative `[D]`.** *Three Scales of Confinement*, **Conjecture I.1** — phase sensitivity
of confined realizers. Its missing arrow is exactly *"realizer-residue geometry → `r_min(N,c)`"*,
and **Lemma D1 makes that arrow precise**: D1 is a quantitative exponential-sum form of the
residue-geometry side, from which the `r_min` side follows by Erdős–Turán. Cross-referenced in
[`OPEN_PROBLEMS.md`](OPEN_PROBLEMS.md).

**Explicit open TODO — NOT CHECKED.** Still unchecked, and this is the right next step before any
decision to resume, because it costs no computation:

- the **individual notes of the *Structured Sectors* collection** (*Structured Sectors of the
  Collatz Carry Equation: Christoffel towers, 2-adic windows, and shell residents*, including its
  September 2026 citation addendum);
- the **literature beyond the two comparisons actually made** — Wirsching (LNM 1681: series and
  companion-note summaries only; **the volume itself was not consulted**) and Tao's Syracuse
  equidistribution (read for its modulus and for where invertibility of `2` enters).

The strongest statement supported for D1/D2 is **"not located in the searched literature"**, with
the searched set being exactly the two bullets above's complement as listed in this section.

---

## Lean

No Lean file was added. The optional additive-formula lemma was **not attempted**, because Step 8's
precondition — that the existing libraries build cleanly here with `lake build` — is not
satisfiable in this checkout without a large download:

- there is no `.lake/` directory, so Mathlib has never been built here;
- `lean-toolchain` pins `leanprover/lean4:v4.34.0`, and the installed toolchains are
  `v4.33.0` and `v4.34.0-rc1` — the required one is absent.

So `lake build` would first fetch a Lean toolchain and then all of Mathlib. That is outside the
"reasonable effort" bound set for an optional step, and it is a dependency install rather than a
build. **Nothing partial was left behind**; no `.lean` file was created, and the library root was
not touched.

Note also that the formula is prior art (above), so a Lean statement of it would be a
formalization of an existing published lemma, not of a result of this round. The natural home for
it is alongside `Divergence.aggregate_identity`, which is its precursor in this repository.

The Lean libraries were **read only**. No file outside `audits/upper_sharp_eoc_fourier/` was
modified except one cross-reference paragraph in the top-level `README.md`.
