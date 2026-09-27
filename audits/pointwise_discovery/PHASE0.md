# Phase 0 — the ledger, and the design, both fixed before measuring

Part I is the theorem ledger the search had to be residualized against;
Part II is the pre-registered design. Both were written before any
measurement in [`REPORT.md`](REPORT.md) §3 was run.

---

# Part I — what is actually known, and with what status

Reconstructed 2026-09-25 from:

* `~/GitHub/eoc-divergence` @ `fcda91b` — `README.md`, `docs/STATUS.md`,
  `docs/PROGRAMME_ENDPOINT.md`, `docs/EQUIVALENT_FORMS_OF_DE.md`,
  `papers/synthesis/main.tex` (*After the Reduction*, Zenodo
  doi:10.5281/zenodo.22944018), and the four audit reports
  (`descent`, `record_holder_anatomy`, `fingerprint_comparison`, `cross_map`).
* `~/Downloads`. `eoc_rev7.pdf` there is **byte-identical** to
  `docs/eoc_rev7.pdf` (sha256 `a499a3ab…8766560`, the value the repository's
  README records), so the deposited Revision 7 and the repository copy are the
  same file. `DeJesus_after_the_reduction_synthesis_revised.pdf` is the deposited
  synthesis note; **the text below was read from its LaTeX source**
  (`papers/synthesis/main.tex`), which is what the repository ships, not from the
  PDF. `ScalesConfinement (1).pdf` was read for the `N^{-3/2}` statement and its
  stated dependence on a two-sided local ballot theorem (Caravenna 2005), which is
  what §5 labels **PAPER**.
* `~/GitHub/eoc-lean-verification` — the analytic-side Lean library; consulted as
  a reference only, and nothing below depends on it.

**Neither repository was modified.** Every numerical statement labelled
**verified (here)** was re-derived in this scratch project in exact integer
arithmetic and cross-checked against the repository's published value; the log is
`data/verify_core.txt` (13/13 pass).

Status labels used throughout, and never silently upgraded:

| label | meaning |
|---|---|
| **LEAN** | machine-checked in `eoc-divergence`, no hypotheses, axioms `propext`/`Classical.choice`/`Quot.sound` only |
| **PAPER** | proved on paper by the author and audited; not formalized |
| **CITED** | external result, with reference |
| **VERIFIED** | exact computation over a stated finite range — not a proof |
| **HEURISTIC** | a reading or model, not a theorem |
| **OPEN** | conjectural or unproved |

---

## 1. Definitions (fixed for this project)

For odd `q >= 3` and odd `r`, on the odd integers (or on `Z_2^x`):

```
T(m) = (q m + r) / 2^{a(m)},      a(m) = v2(q m + r) >= 1
m_k  = T^k(m_0),   a_k = a(m_k),  S_n = sum_{k<n} a_k,   S_0 = 0
alpha_q = log2 q,  R_n = S_n - n alpha_q            (the drift)
A[n] = floor(n alpha_q) = bitlength(q^n) - 1        (integer form)
```

`(q,r) = (3,1)` is the primary system; `alpha = log2 3 = 1.5849625...`.

**Zero-confinement.** `m` is *zero-confined* if `2^{S_n} <= 3^n` for every `n >= 1`,
equivalently `R_n <= 0` for every `n`, equivalently `S_n <= A[n]` for every `n`.
`r_min(N,0)` is the least positive odd integer zero-confined for `N` steps.
`K` is the set of zero-confined elements of `Z_2^x` (the "confined dust").

**Rare side, general `(q,r)`.** Under Haar measure on `Z_2^x` the letter
`v2(qx+r)` is geometric(1/2) with mean 2 for *every* odd `q` and odd `r`, so `R_n`
drifts at `2 - alpha_q`. The rare side is `R_n <= 0` (i.e. `S_n <= A[n]`) when
`q < 4` and `R_n >= 0` (i.e. `S_n >= A[n]+1`) when `q > 4`. `m` *persists* if its
orbit is on the rare side at every `n >= 1`. **PAPER** + **VERIFIED (here)**.

**Confinement depth.** `N(m)` = the largest `n` such that `m` is on the rare side
at every `1..n`. `N(m) >= n` iff `m` is `n`-confined.

**Bit length.** `B = bitlength(m_0)`, so `2^{B-1} <= m_0 < 2^B`. The seed cohort
`{odd m < 2^B}` has exactly `2^{B-1}` members and is *exactly* a complete set of
odd residues mod `2^B` — the fact that makes every count below exact rather than
asymptotic.

**The ratio under study.** `lambda = n / B`.

---

## 2. The aggregate identity and its consequences

```
2^{S_n} m_n = q^n m_0 + r C_n ,   C_n = sum_{i<n} q^{n-1-i} 2^{S_i} ,  C_{n+1} = q C_n + 2^{S_n}
```

* **LEAN** over `N` for `(3,1)`: `Divergence.aggregate_identity`. **PAPER** over
  `Z_2^x` and for general odd `(q,r)`. **VERIFIED (here)** for all seven maps
  `3x+-1, 5x+-1, 7x+-1, 3x+5`, odd `m_0 < 4000`, `n <= 25`, 0 violations.
* `C_n` depends **only on the word**, not on `m_0`. **PAPER** (immediate).
* Exact rewriting (used below as a bookkeeping device, *not* as a new result):
  with `G_n = C_n / q^n`,
  ```
  m_n = q^{-R_n... }              m_n = 2^{-R_n} ( m_0 + r G_n ),    G_n = (1/q) sum_{i<n} 2^{R_i}
  ```
  which is Proposition "drift identity" of the synthesis note with the error term
  `E_N = sum_k log2(1 + r/(q m_k))` written in closed form. **PAPER**, and a
  restatement — recorded here only so that later sections do not re-derive it.

### Drift identity and the valuation-mean classification

`log2(m_N/m_0) = N log2 3 + E_N - S_N` with `0 < E_N <= N log2(4/3)`; along a
divergent orbit `E_N = O(1)` because `sum 1/m_k < infinity`. Every orbit of odd
`m_0 > 1` has `lim S_N/N = 2` (terminating), `S/L in (log2 3, tau_M]` (cyclic) or
`limsup S_N/N <= log2 3` (injective). **PAPER**.

---

## 3. The exact reduction and (DE)

> **Theorem (exact reduction).** Some odd `M` has a divergent accelerated orbit
> **iff** some odd `m` is zero-confined.

**LEAN**, `Divergence.divergent_iff_zeroConfined`, no hypotheses. The one external
input (Garcia–Tal / Curry windowed sparsity) is proved in the same development, so
the equivalence is unconditional.

> **(DE), universal drift exit.** No positive odd integer is zero-confined.
> **OPEN.**

**Four equivalent forms**, recorded so a reformulation is not mistaken for progress:
(a) (DE) itself — **LEAN** for the reduction; (b) `r_min(N,0) -> infinity`;
(c) escape at any one fixed corridor width `c >= 0` is escape at all of them;
(d) **no zero-confined 2-adic integer has an expansion ending in `0^infinity`**.
(b),(c),(d) **PAPER**.

**Form (d) is the terminating-binary-tail problem.** It is *equivalent to* (DE),
not a route to it. This is the single most important guardrail for the present
experiment.

### Supporting theorems

| statement | status |
|---|---|
| windowed sparsity: collision-free `A` meets `[a,a+2^N)` in `<= 4(N+1) theta^N`, `theta ~ 1.9762 < 2` | **LEAN** |
| reciprocal summability: divergent orbit has `sum 1/m_n < infinity` | **LEAN** |
| cycle drift: `m_i = m_j` forces `3^{j-i} < 2^{S}`; no periodic orbit is zero-confined | **LEAN** |
| signed marker: every eventually periodic point of `K` is a **negative** rational, `m = C_L/(2^S - 3^L)` | **PAPER**; **VERIFIED** on all 1717 zero-confined periodic points of period `<= 10` |
| (LPC) => (PosPC) => (DE), second implication strict as far as known | **PAPER** |

---

## 4. The Terras–Everett correspondence — the hinge of this experiment

> **F3.** For odd `q`, odd `r`, and any word `D = (d_0..d_{n-1})` with `d_i >= 1`
> and total `S`, the set `{x in Z_2^x : a(T^i x) = d_i, i < n}` is **exactly one
> residue class mod `2^{S+1}`**, of odd residues, of Haar measure `2^{-S}`.

**CITED** for `(3,1)` (Terras 1976, Everett 1977); **PAPER** in general
(`audits/fingerprint_comparison/PHASE0.md`, F3). **VERIFIED (here)**: for
`3x+1, 3x-1, 5x+1, 5x-1`, 16 000 (seed, depth) pairs, the least realizer
`r(D)` recomputed from the word by modular inversion reproduces the seed's class
exactly; 0 violations.

**The explicit realizer formula** (used throughout below; **PAPER**, immediate
from the aggregate identity):
```
r(D) = least positive odd solution of   q^n m + r C_n  ==  2^{S}  (mod 2^{S+1})
     = q^{-n} (2^S - r C_n)  mod 2^{S+1}
```
So `r(D) < 2^{S+1}` always, and the map `D -> r(D)` is an explicit arithmetic
function of the word alone.

### Three exact counting consequences

**(T1) Exact class occupancy at a power of two.** For `S + 1 <= B`, the number of
odd `m < 2^B` realizing a given word of total `S` is **exactly** `2^{B-1-S}` — no
boundary term, because `2^B` is a multiple of the modulus `2^{S+1}`.
**VERIFIED (here)** at `B = 16`, `n = 2,4,6`, all words, 0 violations.
(The repository states the general-`X` version with an `O(1)` boundary term as
consequence **C1**, the "exactness window `S <~ log2 X`"; the vanishing of that
term at `X = 2^B` is stated in `record_holder_anatomy` §5.6 as "for `j >= A[N]+1`
the ratio is identically 1".)

**(T2) The exact confined-word mass.** With `A[k] = floor(k log2 3)`,
```
f[0][0] = 1,  f[k+1][S'] = sum_{d>=1} f[k][S'-d]  for S' <= A[k+1]
num_N   = sum_S f[N][S] 2^{A[N]-S},     p_N(0) = num_N / 2^{A[N]}
```
and `num_N` is **also** the exact number of odd `m in [1, 2^{A[N]+1})` that are
`N`-confined. **PAPER** + **VERIFIED**. **VERIFIED (here)**: `num_2 = 3` with
the 2-confined odd `m < 16` exactly `{7,11,15}`; `num_14 = 168807`; `num_N`
equals the direct orbit count for `N = 2..12`.

**(T3) The counting identity that defines the trivial regime.** For every `B` and
every `n` with `A[n] + 1 <= B`:
```
#{odd m < 2^B : m is n-confined}  =  2^{B-1} p_n(0)      exactly.
```
Since `A[n] + 1 <= B` iff `n <= (B-1)/alpha` (up to the floor), finite height
imposes **no constraint whatsoever** below
```
lambda  =  n/B  <=  1/alpha  =  1/log2 3  =  0.6309297...
```
**PAPER** (it is (T1) summed over words); **VERIFIED (here)**. This is the
repository's `record_holder_anatomy` §5.6 exact fact, restated on the `lambda`
axis. *It is known, not new.*

---

## 5. The statistics (finished part of the programme)

| statement | status |
|---|---|
| `-(1/N) log2 p_N(c) -> I_0 = alpha(1 - H_2(1/alpha)) = 0.0793186128...` | **LEAN**, `Occupation.confined_mass_rate` |
| rate as relative entropy: `I(q) = D(beta_q ‖ 1/2)/beta_q`, independent of `r`; `I(5) = 0.0323008158` | **PAPER**, **VERIFIED** |
| polynomial correction `p_N(0) ≍ 2^{-I_0 N} N^{-3/2}`, two-sided, with an `O(1)` renewal phase (Beatty jump sets) | **PAPER** (*Three Scales of Confinement* v3); **not** formalized |
| `log2(1/p_N) - I_0 N - 1.5 log2 N = -3.28 +- 0.05` over `N = 100..300` | **VERIFIED**; **VERIFIED (here)**, reproducing the audit table to `<0.002` at `N = 10,20,50,100,150,200,250,300` |
| `q_N(0) = (2/3) p_N(0)` for chain roots | **PAPER** + **VERIFIED** |

**Sharp EOC (CONJECTURE).** `log2 r_min(N,0) = I_0 N + (3/2) log2 N + O(1)`.
Its **lower half implies (DE)**, so it is at least as hard. Its **upper half**
(existence of *small* confined integers) is open *independently* of (DE); the only
elementary bound is `r_min(N,0) <= 2^{N+1} - 1` (from `m = 2^k - 1`), i.e.
exponent `1` against the conjectured `I_0 = 0.0793`.

**Data (VERIFIED, repository).** Exact scan of every odd `m == 3 (mod 4)` below
`10^12` certifies `r_min(N,0)` for `N = 1..346`, 24 distinct record holders,
largest `r_min(345) = 898 696 369 947`. **VERIFIED (here)**: the ladder below
`4·10^4` is exactly `[3, 7, 27, 703, 10087, 35655]`.

**Clustering (VERIFIED).** `Delta_1(N) = log2 r_min(N,0) - log2(1/p_N(0)) > 0` at
all 24 holders (1.9–2.5 bits beyond random placement); and the direct count
`#{odd m <= 2^j : N-confined}` exceeds `2^{j-1} p_N(0)` **immediately above
`r_min(N,0)` and nowhere else** (1.78x at `N=200, j=28`; 5.45x at `N=300, j=35`),
decaying to ~1 by `2^40`. **HEURISTIC** for the attribution to the L1/L2 backward
chains; root-thinning is **PROVED** unable to move `Delta_1` at all (L4).

---

## 6. Excluded structure

| kind | excluded by | status |
|---|---|---|
| periodic / algebraic | cycle drift + signed marker | **LEAN** / **PAPER** |
| combinatorial density | lower ones-density must be **exactly** `beta = 1/alpha` | **CITED** refereed below `beta` (Monks–Yazinski 2004 Thm 2.7(b)); **CITED unrefereed** above `beta` (López–Stoll 2021 preprint) |
| critical Sturmian | `Phi(1 c_beta)` is irrational; effective to height `2^301973` | **PAPER**; general irrational slope **PAPER, in preparation**, margin `c(gamma) = 2 - max(1, gamma log2 3) >= 2 - log2 3` |
| balanced squares | repetition + height bound, one-sided | **PAPER** |
| descent | L1, L2, L4, L7; the 3-adic budget cannot be accumulated | **LEAN** (`Descent`) |

**Descent lemmas, stated because the experiment must residualize against them.**
(L1) `m` `N`-confined and `m == 2 (mod 3)` implies `p = (2m-1)/3` is odd, `p < m`,
`T(p) = m`, and `p` is `(N+1)`-confined. (L2) the backward `d=1` chain from `x`
has length exactly `v3(x+1)`. (L4) `r_min(N,0) == 3 or 7 (mod 12)`, census over
`N <= 346`: 218 / 128 / 0. (L7) forward motion cannot accumulate 3-adic budget.

---

## 7. Closed routes — do not re-derive

| route | why it closes | status |
|---|---|---|
| descent by inheritance + well-ordering | round-trip criterion is **provably equivalent** to (DE); L7 kills budget accumulation | **PAPER**, verdict STOP |
| transport budgets | collapses to the aggregate identity | **PAPER** |
| time-axis / word-level only | `-1` is zero-confined forever; uncountably many confined words satisfy every word shadow and are realized by no integer | **PAPER** |
| fixed-depth Fourier / triangle | hypothesis open, frequency `lambda = 1` unavoidable | **LEAN** for the implication only |
| parity counting on the cycle side | gives `o(L)` | **PAPER** |
| record-holder anatomy | every pattern reduces to L1/L2/L4/L4', last-maximum structure, or a **selection effect**; holders are **not** Sturmian-adjacent (1–3 shared valuations to depth 236) | **PAPER** + **VERIFIED**, verdict STOP |
| fingerprint comparison `3x+1` vs `3x-1` vs `5x+1` | every A-vs-B difference is **cycle capture** with no free parameter; every A-vs-C difference is a function of `alpha` alone; the sign channel shows cycles and nothing else | **VERIFIED**, verdict STOP |

---

## 8. Mandatory controls

| control | what it is | why it must break a candidate |
|---|---|---|
| `-1` under `3x+1` | zero-confined fixed point | any argument not using positivity kills it too |
| `{-5,-7}` under `3x+1` | zero-confined 2-cycle; `-5` confined forever, `-7` fails at step 1 | confinement is a property of the **point**, not the cycle |
| `+1` under `3x-1` | zero-confined **positive** fixed point; `m -> -m` is an exact conjugacy to `3x+1` on the negatives | **sign obstruction**: identical aggregate identity, confinement, `S_k`; opposite answer. **VERIFIED (here)**, odd `m < 4000`, depth 40, identical words |
| `5x+1`, witness `m = 3` | shelter: a positive cycle sits on the rare side | **VERIFIED (here)** to depth 2000 |
| `5x-1` | **no** positive odd `m` persists — proved by pigeonhole (`m_n < m_0`) + sign alignment | the structural twin of `3x+1`: same sign misalignment, opposite drift. **VERIFIED (here)** for odd `m < 2·10^4` |
| random confined words | least realizers sit at the class modulus `2^{S+1}` | an argument excluding them proves too much |

**Sign-alignment criterion (PAPER).** A positive cycle of `T_{q,r}` with length `L`
and total `S` has `sign(S/L - alpha_q) = sign(r)`; it sits on the rare side iff
`sign(r) = sign(q-4)`. Hence among `3x+-1, 5x+-1` exactly **`3x+1` and `5x-1`**
have a non-trivial rare-side problem. **VERIFIED (here)** for the three witnesses tested: `m = 1` persists under
`3x-1` and `m = 3` under `5x+1` to depth 2000, and no odd `m < 2·10^4` persists
past depth 600 under `5x-1`.

---

## 9. What is stated as missing (the target of this experiment)

From *After the Reduction*, §"What is needed" (f), verbatim in substance:

> The only features an integer possesses that a general element of `Z_2` does not
> are its **finite bit length** — equivalently a terminating `0^infinity` tail —
> and its **archimedean size**. A usable law would bound, as a function of `B` and
> `n`, how much of the parity prefix is *forced* by `m < 2^B`. Every statement of
> that kind available here is either **vacuous** (the constraint is automatic) or
> **equivalent to (DE)**. **OPEN**, with no candidate in the programme.

And Open Problem 10, which is the closest formally posed target:

> Give a formula or model for `Delta_N = log2(r_min(N,0) p_N(0))` in terms of
> **order-sensitive carry statistics of the confined words** — statistics that do
> not take `r_min` as an input — and test it at finite depth against the exact
> `p_N`. **OPEN.** Two cautions attach: the sample is small and strongly
> correlated (`n_eff ~ 7`), and a formula alone would not bear on (DE), since only
> a *uniform lower bound* `Delta_N >= -c` gives `r_min -> infinity`.

**Criterion (three conditions, HEURISTIC).** A tool capable of deciding (DE) must
(i) use 2-adic integrality at unboundedly many depths, (ii) use the sign or
archimedean size of the integer, and (iii) couple (i) and (ii) along a **single**
orbit.

---

## 10. Facts this experiment must not re-sell as new

1. `lambda <= 1/alpha` is the vacuous regime — (T3), already in the repository.
2. `m_n = 2^{-R_n}(m_0 + r G_n)` is the drift identity, already **PAPER**.
3. Any reformulation into forms (b), (c), (d) of (DE) is **not** progress.
4. `Delta_1 > 0` and the count excess just above `r_min` are already **VERIFIED**
   and attributed (heuristically) to the L1/L2 chains.
5. Record holders are generic: not Sturmian-adjacent, no residue structure beyond
   L4/L4', and the apparent word-level "gap" against shuffled surrogates is a
   **selection effect**.
6. Confinement is a property of the **arrangement** of the word, not of its letter
   multiset (shuffle control).
7. The letter law is geometric(1/2) with mean 2 for **every** odd `q`, odd `r`; no
   cross-map difference at the Haar level exists beyond `alpha_q`.


---

# Part II — the design, pre-registered

Written 2026-09-25, after Part I and after the core was validated
(`data/verify_core.txt`, 13/13), and **before** any of the measurements in
§4–§6 were run. Nothing below is tuned to an observed result; where a threshold
changed afterwards it is recorded in [`REJECTED_CANDIDATES.md`](REJECTED_CANDIDATES.md).

---

## 1. The question, made exact

The programme's own statement of what is missing (*After the Reduction*, §(f)) is:

> A usable law would bound, as a function of `B` and `n`, how much of the parity
> prefix is **forced** by `m < 2^B`.

That question has an exact answer, and writing it down is the first step of this
experiment — not because the answer is new, but because it says precisely what is
left to measure.

**The exact reduction of "finite height".** Let `w` be a rare-side word of length
`n` for `T_{q,r}`, with total `S = S_n(w)`, and let

```
r(w)  =  least positive odd m whose length-n word is w
      =  q^{-n} ( 2^{S} - r C_n(w) )   mod 2^{S+1}                 (Terras-Everett)
```

Define the **realizer deficit**

```
        delta(w)  :=  (S + 1)  -  log2 r(w)     in (0, S+1].
```

Because every odd `m < 2^{S_n(m)+1}` *is* the least realizer of its own length-`n`
word (its class mod `2^{S+1}` has no smaller positive member), we have, for every
`B` and every `n >= B - 1`:

> *Correction, made during implementation and recorded rather than silently
> applied.* This paragraph first carried the condition `A[n] + 1 >= B`. That is
> not enough: a confined word can have total as small as `S = n`, and uniqueness
> of the representative below `2^B` needs `S >= B - 1` for **every** confined
> word, i.e. `n >= B - 1`. The brute-force gate S4 caught it (off by exactly the
> all-ones word). The corrected condition is used everywhere below.

```
  #{ odd m < 2^B : m is n-confined }  =  #{ w confined, |w| = n : delta(w) > S(w) + 1 - B }.   (*)
```

So **all** of the content of "`m < 2^B`" at depth `n`, beyond what the word already
says, is carried by the single scalar `delta(w)`. Finite height forces nothing
about the word except through the joint law of `(S(w), delta(w))`.

**The null.** Call H0 the hypothesis that `delta` is independent of the word given
nothing at all, with the uniform-class law

```
        H0:   P( delta > t )  =  2^{-t} ,     delta  independent of  w .
```

H0 is exactly "the realizer is a uniformly random odd residue of its class".
Under H0, `(*)` gives `E[count] = sum_w 2^{B-1-S(w)} = 2^{B-1} p_n(0)`, which is
the repository's exact counting identity (T3). **So H0 reproduces every known
counting fact, and any departure from H0 is, by construction, residual to all of
them.** That is the sense in which this experiment is residualized.

**The target.** A pointwise finite-height law, if one exists, is a departure from
H0 that (i) is a statement about `delta(w)` given computable word statistics,
(ii) is not an artefact of the known L1/L2 chain mechanism, and (iii) behaves
correctly on the control maps.

---

## 2. What is already known to break H0, and must be divided out

**The chain mechanism (L1/L2), stated as an exact law about `delta`.** If
`w = 1 . w'` (first letter 1) then `S(w) = S(w') + 1` and the realizers satisfy
`r(w) = (2 m' - 1)/3` where `m'` is the least element of `r(w')`'s class mod
`2^{S'+1}` with `m' == 2 (mod 3)`. Writing `j in {0,1,2}` for which of
`r(w'), r(w')+2^{S'+1}, r(w')+2^{S'+2}` that is,

```
  j = 0  (i.e. r(w') == 2 mod 3):   delta(w)  =  delta(w') + log2 3          (inheritance)
  j = 1:                            delta(w)  ~  log2 3       ~ 1.585        (reset)
  j = 2:                            delta(w)  ~  log2 3 - 1   ~ 0.585        (reset)
```

each with probability `1/3` over the class. This is (L1) seen in the `delta`
coordinate; it is **known** and it is the announced cause of the clustering
already measured in `audits/record_holder_anatomy`. It is *pre-registered here as
a prediction to be verified*, and everything downstream is measured both on the
full ensemble and on the **chain roots** (`3 ∤ r(w)+1`), where the inheritance
branch is absent.

---

## 3. Datasets

All exact integer arithmetic. `mp` ranges over the maps of `BASELINE.md` §8.

| id | cohort | construction | size |
|---|---|---|---|
| **D1** | integer population | every odd `m < 2^B`, `B = 12..28`; record `N(m)` and, at a grid of depths, the full feature vector | `2^{B-1}` per `B` |
| **D2** | generic rare-side words | exact conditional sampling from the dyadic law `2^{-S(w)}/p_n(0)` via the integer transfer table; `n` in a grid | `>= 2·10^4` per `(map, n)` |
| **D3** | deep cohort | the seeds of D1 with the largest `N(m)`, plus the published record ladder | top ~200 per `B` |
| **D4** | controls | D2 and D1 repeated for `3x-1`, `5x+1`, `5x-1` on their own rare sides | as D1/D2 |
| **D5** | word-level negative control | uniformly random *confined* words ignoring dyadic weight, and shuffled confined words | `10^4` per `n` |

**Sampler correctness requirement (pre-registered gate).** The D2 sampler must
reproduce the exact `p_n(0)` normalisation `g_0(0) = num_n` and, at small `n`, the
exact empirical word frequencies. If it does not, the run is void.

### Variables recorded

*Seed*: `m_0`, `B = bitlength(m_0)`, `m_0 mod 2^k` (`k <= 6`), `m_0 mod 3`, `v3(m_0+1)`.

*Orbit at depth n*: `m_n`, `a_n`, `S_n`, integer deficit `D_n = A[n] - S_n`,
`R_n = S_n - n alpha` (float, reporting only), running `max`/`min` of `D_j`,
`N(m)`, `min`/`max` orbit value, `log2(m_n/m_0)`.

*Aggregate*: `C_n` exactly, `C_n/3^n`, `C_n/2^{S_n}`, `log2 C_n`.

*Prefix (word) statistics* — the "order-sensitive carry statistics" of Open
Problem 10, all functions of the deficit path `D_0..D_n`:
`S_n/n`; counts of `a = 1,2,3,4,>=5`; longest run of `a = 1`; `max D`, `D_n`,
`#{k : D_k = 0}` (critical contacts), `#{k : D_k <= 1}`, `argmax D`,
`argmin_{k>0} D`, first and last `k` with `D_k = 0`, the **carry area**
`Z_n = sum_{k<n} 2^{-D_k}` (`= 3 G_n` up to the fractional part of `k alpha`),
local slopes `(S_{k+W}-S_k)/W` for `W = 8, 16, 32`, and the letter-transition
counts `#(a_k=1, a_{k+1}=1)` etc.

*Height*: `r(w)`, `delta(w)`, chain-root indicator `[3 ∤ r(w)+1]`, `v3(r(w)+1)`.

---

## 4. Measurements, in order

**M1 — the `lambda` grid.** `E(B,n) = #{odd m<2^B : n-confined} / (2^{B-1} p_n(0))`
for `B = 12..28` and a grid of `n`, plotted against `lambda = n/B`. Pre-registered
expectations: `E == 1` identically for `lambda <= 1/alpha` (T3, a theorem, a
correctness check on the pipeline, not a finding); a deviation above `1/alpha`
whose *shape in lambda* is the object of interest. Question: is there a `lambda`
threshold beyond `1/alpha` at which `E` departs systematically, and does the
departure collapse when plotted against `lambda` rather than `n`?

**M2 — the `delta` marginal.** Empirical `P(delta > t)` against `2^{-t}`, per map
and per `n`, on D2 and on D1. Report the exact discrepancy, not a `p`-value alone.

**M3 — conditional dependence (the main test).** Does any word statistic of §3
predict `delta`, at matched `S`? Measured as: (a) the shift in `E[delta]` between
top and bottom decile of each feature, with `S` stratified; (b) mutual information
between the feature and the indicator `[delta > t]` for `t = 1,2,4,8`; (c) the
same on chain roots only.

**M4 — envelopes.** For each feature pair, search for hard one-sided boundaries in
the `(feature, delta)` plane: convex hull of the observed cloud, per-bin extreme
order statistics, and explicit candidate inequalities `delta <= f(feature)` /
`delta >= f(feature)` with **zero observed violations** as the criterion.

**M5 — controls.** M2–M4 on `3x-1`, `5x+1`, `5x-1`. A candidate that behaves
identically on `3x-1` is suspect: `3x-1` on the positives is `3x+1` on the
negatives, so anything shared by the two cannot be using the sign.
A candidate must also be examined on `5x-1`, where persistence is **false** by an
elementary argument, and on `5x+1`/`3x-1`, where it is **true**.

**M6 — the symbolic-reduction test.** Every surviving candidate is pushed through
the aggregate identity and the definitions symbolically (`sympy` if available,
otherwise by hand with an exact numeric certificate) to see whether it is an
identity in disguise.

---

## 5. Holdout, frozen in advance

* **Discovery set**: `3x+1` only; D2 at `n in {20, 40, 60}`; D1 at `B <= 20`.
* **Freeze**: any candidate is written into §5 below with its
  exact formula and its discovery domain **before** the holdout is touched.
* **Holdout**: D2 at `n in {100, 150, 200, 300}`; D1 at `B in {24, 26, 28}`;
  all four maps. Re-tuning after seeing the holdout is permitted only by declaring
  a **new** hypothesis with a **new** holdout, and is recorded as such.

---

## 6. Adversarial filters (applied to every candidate, in this order)

1. **Restatement** — reducible to the aggregate identity / Terras-Everett / the
   definitions. `delta`'s defining formula is itself one of these, so any relation
   that only re-expresses `r(w) = q^{-n}(2^S - rC_n) mod 2^{S+1}` is rejected.
2. **Confinement restatement** — true for every confined object by the corridor
   condition alone. Tested against D5 (random and shuffled confined words).
3. **Circularity** — implies (DE) only by being equivalent to it. In particular
   any statement of the form "`delta(w) <= c` uniformly" is the *lower half of
   Sharp EOC* and is at least as hard as (DE); such a statement may be
   **measured** but must never be reported as a finding.
4. **Control failure** — must fail where the programme says it must:
   `-1` and `{-5,-7}` under `3x+1`; `+1` under `3x-1`; `m=3` under `5x+1`;
   random confined words.
5. **Merely statistical** — describes the population but constrains no specific
   orbit. Recorded separately if interesting.
6. **`B` is inessential** — delete `B` (equivalently, delete `delta`'s dependence
   on the archimedean size) and re-measure. If nothing changes, the candidate does
   not address the missing ingredient.
7. **Out-of-sample** — §5.

---

## 7. Stop rule, pre-registered

> Stop and report **D** (no usable pointwise signal) if, after M1–M6, every
> departure from H0 is reproduced by the L1/L2 chain mechanism, by a selection
> effect, or by the control maps in a way that shows it is not using the sign or
> the size of the integer.
>
> Report **C** if the strongest departure reduces symbolically to a known identity.
>
> Report **B** only if a departure from H0 survives the chain residualization,
> the controls and the holdout, but has not become a clean statement.
>
> Report **A** only if in addition it is a simple explicit inequality with zero
> violations on the holdout and a mathematical interpretation.

A negative result is the expected outcome and is fully acceptable.

---

## 8. Known limitations, stated in advance

* The extreme order statistic (`r_min`) cannot be improved here: the repository
  already scanned every odd `m == 3 (mod 4)` below `10^12` (37 min on 8 cores).
  This project scans to `2^28` only, so **M1 at large `lambda` reproduces known
  data and cannot extend it.** The new territory is the *bulk* of the
  `(S, delta)` law, which the record-holder audit never measured.
* `n_eff` for anything read off the record ladder is `~7` (`3x+1`) and `~3.4`
  (`5x-1`). No ladder-based claim will be made.
  *(The `5x-1` figure quoted here was the published one at the time of
  pre-registration. This search later showed the ladder it came from to be
  defective; the corrected value is `3.0`. Left as written — a pre-registration
  that is edited after the fact records nothing. See
  [`../cross_map/CORRECTION_2026-09-25.md`](../cross_map/CORRECTION_2026-09-25.md).)*
* D2 samples the dyadic law exactly, but a sample of `2·10^4` words at `n = 300`
  resolves `P(delta > t)` only to `t <~ 14`.
