# H10/ℚ ⟶ Collatz pointwise realizer: transfer study

**2026-10-16.  Verdict: D — no useful transfer.  Nothing modified, nothing published.**

## Question

Can any mechanism in the OpenAI *Hilbert's tenth problem over the rational numbers* manuscript
distinguish a genuine positive-integer Collatz realizer from a parity sequence realizable only
in `ℤ₂`?

## Answer

**No** — and the conclusion does not depend on whether that manuscript is correct.

H10 forces standard-from-nonstandard using (i) one fixed nonzero integer `δ` that every local
obstruction divides, (ii) a height estimate `h(s) ≤ H·M(s)^c` over **many** contact primes, and
(iii) a **quadratic** canonical height that beats the resulting linear bound.  In the Collatz
realizer setting (i) and (ii) are **provably absent** and (iii) has no analogue:

* no nonzero integer is divisible by `2^{S_n}` for every `n` when `S_n → ∞`;
* the realizer set `{r_N + k·2^{S_N}}` hits **every** class mod every odd `q` — verified for
  `q = 3,9,27,81,243,5,7,11,13` — so there is no second modulus and nothing for `M(s)` to be;
* the structure is the affine reduction `m₀ ↦ m₀ mod 2^{S_n}` on `(ℤ₂,+)`, which carries no
  positive-definite quadratic form.

**And there is a prior reason.**  H10's step `M^K | δ, δ ≠ 0 ⟹ M^K ≤ |δ|` is verbatim the tool
EOC Rev 8 §5.3 names as "the only general tool converting divisibility into a size statement",
which Revision 7 §5.3 already proved evaluates to a restatement of Lemma 2.4 on the confined
sector.  Quantitatively — **Lemma O, proved here**: zero-confinement *is* `2^{S_n} ≤ 3^n` while
the height is `H ≥ 3^N`, so `2^{S_N}/H − 1 ≤ 0` identically and `ρ_N ≥ 1`.  *The hypothesis that
defines the interesting sector is exactly what voids the tool.*

On the aperiodic confined sector **both horns of the §5.3 dichotomy fail simultaneously**: no
periodic collapse to pin `χ` (horn one), vacuous size branch (horn two).  Periodic words are
decided by horn one — `[1,2] → m₀ = −5`, `[2,1,1,2] → −103/17`, `[1,1,3] → 19/5`, each exact and
`N`-independent — which is why they were never the hard case.

## The gap, exhibited

The Beatty/Sturmian zero-corridor word `d_j = ⌊(j+1)log₂3⌋ − ⌊j log₂3⌋` is zero-confined, its
canonical residues are mutually compatible, and `r_60` has **93 bits against `S_60 = 95`** — no
stabilization.  A 2-adic realizer exists; a nonnegative-integer one does not.

## What was gained

Not a theorem.  A sharper statement: forcing standard-from-nonstandard is achievable given a
fixed integer sink, a many-prime height, and a quadratic form — and the Collatz realizer problem
demonstrably has no sink and no second prime.  Three open objects, two now known not to exist.

## Documents

| file | contents |
|---|---|
| `01_SOURCE_AUDIT.md` | H10 architecture, §2.7 height contradiction, external inputs, verification concerns |
| `02_EOC_REALIZER_BASELINE.md` | Rev 8 definitions re-verified, Proposition R with hypotheses, the §5.3 meta-theorem |
| `03_TRANSFER_ANALYSIS.md` | the two obstructions; the brief's routes A–F answered |
| `04_CANDIDATE_LEMMAS.md` | seven candidates, each classified; C4/C5/C6 disproved |
| `05_COMPUTATIONAL_TESTS.md` | exact tests T1–T5, limitations, **and one retraction of my own** |
| `06_FINAL_VERDICT.md` | classification table, verdict, three next steps |

## Reproducing

```
cd scripts
python3 run_char.py    # identity, stabilization on orbits, the Beatty gap
python3 run_rho2.py    # the dichotomy: rho_N >= 1, and the periodic collapse
python3 run_primes.py  # no odd prime is constrained; why the quadratic is missing
```
Exact integer/modular arithmetic; stdlib only; frozen outputs in `results/`.
