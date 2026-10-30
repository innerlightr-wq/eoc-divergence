# Temporal differentiation and nonlinear carry structure in EOC

**2026-10-16.  Verdict: D (existing structure explains it), with E for the terminal-tip
hypothesis.  No repository modified; nothing published.**

## Question

Does the temporal position of a parity/exponent difference produce arithmetic information about
realizers beyond the already-known 2-adic valuation of their difference — and can it constrain
positive-integer realizability?

## Answer: no, twice

**The residual odd component does not exist.**  For the only comparison with a common modulus
(the `S_N`-preserving swap `d_i→d_i+1`, `d_k→d_k−1`),
```
Δ r_N ≡ −2^{S_{i+1}} V_{i,k} 3^{−N}  (mod 2^{S_N}),   V_{i,k} = Σ_{j=i+1}^{k} 3^{N−1−j} 2^{S_j−S_{i+1}},
```
exact, **36 712 swaps, 0 failures**.  Remove the valuation `v_2 = S_{i+1}` and what is left is an
explicit function of the word.  Temporal position enters only as *the index range of a sum*.

**The nonlinearity is real but structureless.**
```
Δ_i Δ_k C_N = (2^{ε_i}−1)(2^{ε_k}−1) T_k      ⟺      Δ_i Δ_k C_N = Δ_i C_N · Δ_k C_N / T_i
```
(66 600 and 7 200 cases, 0 failures).  The interaction between temporal positions factorises
exactly: it is `2^{a+b} = 2^a 2^b`.  The hypothesis anticipated irreducible coupling; the
coupling is exactly reducible.

## The terminal tip is the denominator

Exact enumeration of **all 154 518 words** with `N = 11`, `S_N = 22` (both controls fixed):

| `τ = i/N` | 0.000 | 0.182 | 0.364 | 0.545 | 0.727 | 0.818 |
|---|---|---|---|---|---|---|
| window `w` | 20.0 | 16.0 | 12.0 | 8.0 | 4.0 | 2.0 |
| **absolute bits determined** | **2.0000** | **2.0000** | **2.0000** | **2.0000** | **2.0000** | **2.0000** |
| relative fraction | 0.100 | 0.125 | 0.167 | 0.250 | 0.500 | **1.000** |

Absolute information is **exactly flat** (it is `E[d_{i+1}] = S_N/N`); the relative fraction rises
to 1 only because the window shrinks.  Eligible swap counts *decrease* with `i`
(`0.1818 → 0.0182`).  **Late differences look informative because there is less left to say.**

## Why realizability is untouched

`r_N` is itself a nonnegative integer realizing the prefix, so **every finite word is realized** —
the Sturmian/Beatty prefix at `N = 30` has `r_30 = 71106568281083`, a genuine orbit reproducing
all 30 valuations.  Temporal differentiation is prefix-local; any prefix-local invariant takes the
same value on realizable and unrealizable infinite words sharing that prefix.  **That is a general
obstruction, not a limitation of these lemmas.**

## What is new

Two closed forms, no theorem.  Lemma T+ and the separability identity are correct and exactly
verified, but both follow in two or three lines from `C_N = Σ3^{N−1−j}2^{S_j}` — which by the
brief's own standard disqualifies them.  The genuinely useful output is the **prefix-locality
obstruction**, which closes this class of approaches prospectively.

Lemma T+ does not contradict the October 14 Theorem D: that concerns **free** suffixes, where the
odd part really is undetermined (confirmed — it spreads over all odd classes mod 8).

## Documents

| file | contents |
|---|---|
| `01_BASELINE_AUDIT.md` | prior results reconciled against their scripts; novelty boundary |
| `02_TEMPORAL_MODEL.md` | conventions, the matched comparison, the representative trap |
| `03_EXACT_COMPUTATIONS.md` | full test table, the enumeration, **and one retraction of my own** |
| `04_NONLINEAR_INTERACTIONS.md` | perturbation calculus and the separability identity |
| `05_CANDIDATE_LEMMAS.md` | Lemma T, Lemma T+, assessment, consistency with Theorem D |
| `06_POINTWISE_REALIZER_IMPLICATIONS.md` | the prefix-locality obstruction |
| `07_FINAL_VERDICT.md` | classification and three next steps |

## Reproducing

```
cd scripts
python3 run_derive.py   # perturbation calculus, separability
python3 run_odd.py      # swap, valuation, Lemma T, the representative trap
python3 run_closed.py   # Lemma T+ : no residual exists
python3 run_tip.py      # terminal-tip enumeration (contains the superseded P8)
python3 run_final.py    # Theorem D consistency; realizability
```
Exact integer/modular arithmetic; stdlib only; frozen outputs in `results/`.
