# 05_COMPUTATIONAL_TESTS.md

Exact integer and modular arithmetic throughout (`int`, `pow(·,-1,m)`, `fractions.Fraction`).
No floating point enters any claim; `math.log2` is used only to print `ρ_N` for display.
CPython standard library only; one worker; every run under an explicit `timeout`.

## Methods

`scripts/eoc.py` implements the accelerated map, `S_n`, `C_n` by the recurrence
`C_{n+1} = 3C_n + 2^{S_n}`, the canonical residues `r_n = (−C_n·3^{−n}) mod 2^{S_n}`, the
confinement predicate `2^{S_n} ≤ 3^n`, and `ρ_N = log₂max(C_N,3^N)/S_N`.

## Results

**T1 — aggregate identity and forward characterization** (`results/run_char.txt`).
`2^{S_n}m_n = 3^n m_0 + C_n` verified exactly to `n = 40` for
`m₀ = 7, 27, 97, 703, 10087, 159487, 270271`.  In every case `r_n = m₀` from the first `n` with
`2^{S_n} > m₀` (respectively `n = 3,4,5,8,12,16,14`) onward.  **`[COMPUTATIONALLY VERIFIED]`**

**T2 — the gap, exhibited** (`results/run_char.txt`).  The Beatty/Sturmian zero-corridor word
`d_j = ⌊(j+1)α⌋ − ⌊jα⌋`, `α = log₂3`, is confined (`2^{S_n} ≤ 3^n` for all `n ≤ 60`), its
residues are mutually compatible, and `r_60` has **93 bits against `S_60 = 95`** — no
stabilization.  A 2-adic realizer exists; a nonnegative-integer one does not.
**`[COMPUTATIONALLY VERIFIED]`**

**T3 — `ρ_N ≥ 1` on the confined sector** (`results/run_rho2.txt`).  `ρ_N` at `N = 10,20,40,60`:

| word | confined | `ρ_10` | `ρ_20` | `ρ_40` | `ρ_60` |
|---|:--:|---|---|---|---|
| orbit `m₀=27` | no | `1.1792` | `1.1684` | `0.9870` | `1.0000` |
| Beatty word | **yes** | `1.1455` | `1.0971` | `1.0585` | `1.0417` |
| periodic `[1,2]` | **yes** | `1.1336` | `1.1163` | `1.0929` | `1.0820` |
| periodic `[2,1,1,2]` | no | `1.1544` | `1.1256` | `1.0976` | `1.0850` |
| random confined ×3 | **yes** | `≈1.134` | `≈1.092` | `≈1.070` | `≈1.045` |

and `2^{S_N}/H − 1` at `N = 60` is negative on every confined word.  Consistent with Lemma O,
which proves it rather than samples it.  **`[COMPUTATIONALLY VERIFIED]`, and `[PROVED]` as Lemma O**

**T4 — periodic collapse** (`results/run_rho2.txt`).  For a purely periodic word,
`m₀ = C_{Np}/(2^{Nσ} − 3^{Np})` exactly and independently of `N`: `[1,2] → −5`,
`[2,1,1,2] → −103/17`, `[1,1,3] → 19/5`.  Periodic words are decided by horn **one** of the
dichotomy, never needing the size branch.  **`[COMPUTATIONALLY VERIFIED]`**

**T5 — no odd-prime constraint** (`results/run_primes.txt`).  Beatty word, `N = 40`, modulus
`2^63`: the realizer set `{r_N + k·2^{S_N}}` hits **all** residue classes mod
`q = 3, 9, 27, 81, 243, 5, 7, 11, 13`.  **`[COMPUTATIONALLY VERIFIED]`** (and immediate from
`gcd(2,q)=1`, so really `[PROVED]`).

## A correction to my own run

My first `ρ` script printed "periodic words have `ρ_N → 0` and the branch is useful".  **My own
table in the same output contradicted it** (periodic `[1,2]` gives `ρ_60 = 1.0820`).  The claim
conflated the generic representation `(C_N, 3^N)` with the periodic collapse, which uses a
different and much smaller height.  **Retracted and replaced** by T4, which shows periodic words
are handled by the first horn instead.  `results/run_rho2.txt` is the corrected run; the
superseded script is not included.

## Limitations

* Depths are modest (`N ≤ 70`).  Nothing here needs more: T3 and T5 are proved, and T1/T2 are
  illustrations of a proved characterization.
* "Random confined" words are greedily generated and are not uniform on the confined sector; they
  are a sanity check, not a sample.
* No Lean was run and **no Lean verification is claimed**.
* No comparison against the full EOC experiment suite was attempted; T3 and T5 deliberately
  reproduce known repository findings (Obs. 5.9, §4b) as independent checks, not as new data.
