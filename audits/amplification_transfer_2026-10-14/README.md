# Arithmetic amplification and the divergence problem — 2026-10-14

**Question.** Could the amplification and joint inverse-reconstruction method of
a September 2026 percolation preprint show that a single permanently
zero-confined positive odd integer forces an arithmetic amplification
contradicting the proved exponential decay of confined-residue mass?

**Verdict: no, and the obstruction is provable and specific.** The percolation
Lemma 4.8 exists to delete an inverse multiplicity; the EOC word ↔ realizer
correspondence is a **bijection**, so there is no multiplicity to delete. And the
proposed mass criterion is **vacuous**: it asks for more confined residue classes
than exist, so no mechanism of any kind can satisfy it.

Read [`VERDICT.md`](VERDICT.md) for the five answers,
[`AMPLIFICATION_CRITERION.md`](AMPLIFICATION_CRITERION.md) for the vacuity proof,
[`OBSTRUCTIONS.md`](OBSTRUCTIONS.md) for the catalogue.

## The four obstructions, each independent

1. **The mass criterion is vacuous.** Any family of pairwise distinct
   `0`-confined residue classes has `μ ≤ μ(C_N) = 2^{−I_0N+o(N)}`, so demanding
   `μ(B_N) ≥ c·2^{−εN}` with `ε < I_0` asks for **more confined classes than
   exist** — unsatisfiable for every seed. **No injection into the confined
   population can amplify its mass** — not permutations, not lifts, not any map.
2. **No multiplicity to delete.** `word ↔ least-realizer class` is a bijection
   (`EOC/Realizer.lean` `leastRealizer_unique`, `residue_pinning`; verified max
   fibre `= 1` for `N ≤ 14`). The inverse is a division; the code is empty.
3. **Index surplus `=` fibre cost, identically.** `#I_N ≤ n_N · max fibre` for any
   map into `C_N`. The percolation engine works because gain and cost are both
   linear in `k` while their *ratio* contracts; here the ratio is `1`.
4. **No spectral seed.** Every row-and-column-stochastic kernel on a **finite**
   set has `‖K‖_{ℓ²} = 1` exactly — and the state space must be finite for
   `p(N,c)` to mean what `Occupation.confined_mass_rate` says.

## Reusable positives proved here

* **`μ(C_N) = p(N,0)` exactly** — the symbolic-mass ↔ residue-density bridge is
  an identity, not an asymptotic. Verified by brute force over all odd residues
  mod `Q_N` for `N ≤ 14`, 0 violations.
* **`p(N,c) = P[S_j ≤ αj + c ∀ j ≤ N]`** for i.i.d. Geometric(1/2) letters. The
  dyadic mass *is* that probability; hence `I_0 = J(α)`, `J(a) = a(1−H_2(1/a))`.
  No pointwise content.
* **The drifting budget priced:** `c = θN` gives rate `J(α+θ)`, and **0** once
  `θ ≥ 2−α = 0.4150375`. A linear defect makes the target *strictly harder*, so
  the fixed-`c` scope of `confined_mass_rate` is not a usable escape.
* In the percolation paper's own currency (`π ≥ n^{−β}`, needs `β < 1/2`): the
  whole confined population has `β_eff = I_0 = 0.079` and **would** finance the
  construction; one seed's cylinder has `β_eff = α = 1.585` and does not, short
  by `2^{1.085N}`. **That pair of numbers is the aggregate/pointwise gap in
  percolation variables.**

## The measurement that locates the difficulty

The bulk of the confined population obeys equidistribution to within **1.6 %**
(`N ≤ 24`, all odd `m < 2^17`), while `ρ(N)/r_min(N)` with `ρ = 2/p(N,0)` peaks
at **17.34** and then drops *below* 1 at each record transition. **So the
aggregate statistics are correct, and that is exactly why they say nothing: the
whole problem is one atypical integer per range, beating the mean by a bounded
factor, invisible to any exponential rate.**

Live target: **(LEFT-TAIL)** `r_min(N,0) ≥ C^{−1}N^{−B}/p(N,0)`. It implies
`r_min → ∞`, hence no persistent seed. Its content is exactly the **absence of an
additive term**. Measured true with `B = 0`, `C ≈ 17` to `N = 108`.

## Reproduction

CPython standard library only. **Every confinement decision is the integer
comparison `2^{S_j} ≤ 2^c·3^j`.**

```bash
python3 scripts/mass.py          # exact confined-word counts and dyadic mass  ~3 min
python3 scripts/rate_checks.py   # Rate.lean sandwich; walk identity; drift   ~12 min
python3 scripts/bridge.py        # mass<->density bridge, multiplicity, N<=14  ~6 min
python3 scripts/recombine.py     # down/up-shift survival, every node, N<=12   ~2 min
python3 scripts/fibres.py        # index surplus vs fibre cost, N<=14          ~3 min
python3 scripts/placement.py     # W(N,X) vs the fair value, all odd m < 2^17  ~4 min
python3 scripts/tail_ratio.py    # rho(N)/r_min(N) on the record ladder         ~1 s
python3 scripts/check_thm4.py    # audits the fibre bound against exact fibres ~1 min
```

`SOURCE_HASHES.txt` records the percolation preprint by sha256; the PDF is not
redistributed, and **no theorem of it is transferred or relied upon**.

## Scope

Nothing here proves, advances or conditionally establishes the Collatz conjecture
or EOC's pointwise divergence exclusion. The percolation preprint is **not**
claimed to prove anything about Collatz; it was read for its mechanism. **No Lean
verification is claimed.** Every closure applies to its precise formulation and
none is an impossibility claim about Fourier, combinatorial or probabilistic
methods in general.
