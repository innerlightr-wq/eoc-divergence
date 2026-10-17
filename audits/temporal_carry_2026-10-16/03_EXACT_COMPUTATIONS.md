# 03_EXACT_COMPUTATIONS.md

Exact integer and modular arithmetic throughout (Python `int`, `pow(·,−1,m)`).  No floating
point enters any claim.  CPython standard library only; one worker; every run under an explicit
`timeout`.  Scripts in `scripts/`, frozen outputs in `results/`.

| test | definition | size | conditioning | outcome | null / control | survives controls? | predicted by known formulas? |
|---|---|---|---|---|---|---|---|
| **P0** | `C_N` closed form vs recurrence; aggregate identity | 400 words + 4 orbits to `N=25` | — | **0 failures** | two independent implementations | — | yes (Lemma 2.4) |
| **P1** | `Δ_i C_N = (2^ε−1)T_i` | 15 000 triples | `ε ∈ {1,2,3}` | **0 failures** | — | — | **yes** |
| **P2a** | `Δ_iΔ_k C_N = (2^{ε_i}−1)(2^{ε_k}−1)T_k` | 66 600 tuples | `i<k` | **0 failures** | — | — | **yes** |
| **P2b** | `Δ_iΔ_k C_N = Δ_iC·Δ_kC/T_i` | 7 200 pairs | `i<k` | **0 failures** | — | — | **yes** |
| **P3a** | swap: `ΔC_N = W_{i,k}` | 19 774 swaps | `S_N` fixed | **0 failures** | — | — | yes |
| **P3b** | `v_2(W_{i,k}) = S_{i+1}` | 19 751 swaps | `S_N` fixed | **0 failures** | — | — | yes (Thm D analogue) |
| **P5** | Lemma T: `u ≡ −3^{−(i+2)} mod 2^{d_{i+1}}` | 22 456 swaps | `S_N` fixed | **0 failures** | — | — | **yes** |
| **P8′** | Lemma T+: `u ≡ −V 3^{−N}` exactly | 36 712 swaps | `S_N` fixed | **0 failures** | — | — | **yes** |
| **P6** | terminal tip, absolute vs relative | **exact enumeration**, all 154 518 words with `N=11`, `S_N=22`, digits 1–4 | `N`, `S_N` both fixed | **absolute flat at 2.0000; relative 0.10→1.00** | — | **effect vanishes** | **yes** |
| **P7** | eligible-swap profile | same enumeration | — | counts **decrease** 0.1818→0.0182 | — | — | yes |
| **P9** | free-suffix odd part mod 8 | 61 + 64 matched-`S_N` pairs | prefix length `j` | spreads over all 4 odd classes | — | — | yes (Thm D) |
| **P10** | `r_N` realizes the prefix | 5 families at `N=30` | — | yes for admissible words | Sturmian, periodic, random, 2 orbits | — | yes |

## The terminal-tip measurement in full (P6)

Exact enumeration of **all 154 518 words** with `N = 11`, `S_N = 22`, digits `1..4` — so `N` and
`S_N` are *both* held fixed by construction, the control the brief demands.

| `i` | `τ = i/N` | eligible | window `w = S_N−S_{i+1}` | **absolute bits determined** | relative fraction |
|---|---|---|---|---|---|
| 0 | 0.000 | 154 518 | 20.000 | **2.0000** | 0.1000 |
| 2 | 0.182 | 154 518 | 16.000 | **2.0000** | 0.1250 |
| 4 | 0.364 | 154 518 | 12.000 | **2.0000** | 0.1667 |
| 6 | 0.545 | 154 518 | 8.000 | **2.0000** | 0.2500 |
| 8 | 0.727 | 154 518 | 4.000 | **2.0000** | 0.5000 |
| 9 | 0.818 | 154 518 | 2.000 | **2.0000** | 1.0000 |

The absolute amount determined is **exactly flat** — it is `E[d_{i+1}] = S_N/N = 2`, the mean
digit.  The relative fraction rises to 1 **solely** because `w` shrinks linearly to 0.

## Retraction of one of my own results

My first terminal-tip script (P8, superseded) tested whether the bit above the Lemma-T block is
"balanced" and **printed the conclusion "balanced within noise at every position" directly
beneath a table showing `P(bit=1) = 0.0000` at `i=0`, `1.0000` at `i=1`, and `|z| = 152.8`.**
The printed conclusion was flatly contradicted by its own data and is **retracted**.

The error was in the test design, not the arithmetic: that bit is *determined*, not random, and
pooling across words made a deterministic bit look like a degenerate distribution.  The correct
statement is the stronger Lemma T+ — *every* bit of `u` is determined — which is what
`run_closed.py` establishes on 36 712 swaps.  The superseded script is not included; its output
is retained inside `results/run_tip.txt` with this note.

## Limitations

* Word lengths are modest (`N ≤ 15`); the identities are proved, so depth adds nothing.
* The exact enumeration uses digits `1..4`; larger alphabets change the mean digit but not the
  flatness of the absolute curve, which equals `E[d_{i+1}]` by construction.
* P9 uses 61 and 64 matched pairs — small, and used only to confirm a prior proved theorem, not
  to establish anything.
* No Lean was run and **no Lean verification is claimed**.
