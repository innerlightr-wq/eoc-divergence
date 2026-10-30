# 04_CANDIDATE_LEMMAS.md

Each candidate is given its exact statement, then tested against the six questions of the brief's
§4.  **No candidate survives as an advance.**  I record the failures because the *way* each fails
is the content.

## C1. The residue characterization

> **Proposition R.** `S_n ↑ ∞`.  The word has a nonnegative-integer realizer iff `(r_n)` is
> eventually constant; strictly positive iff that constant is nonzero.

1. Exact statement and hypotheses: `02_EOC_REALIZER_BASELINE.md` §2.
2. **Already known / trivial**: it is "a 2-adic integer is a nonnegative rational integer iff its
   expansion terminates", transported through Lemma 2.4.
3. Correct — proved, and machine-checked on seven orbits.
4. Applies to all words with `S_n → ∞`.
5. **Does not improve the pointwise problem.**  It restates it.
6. **It is a reformulation of the original obstruction.**  Per the brief's §4 instruction, it is
   not progress.

**Status: `[PROVED]`, `[ALREADY KNOWN]`.**

## C2. A new inequality between `C_n` and `2^{S_n}`?

> Sought: an inequality forcing `r_n` to stabilize.

The available relation is Lemma 2.4 itself.  On the confined sector `2^{S_n} ≤ 3^n`, and
`C_n = Σ_{j<n}3^{n-1-j}2^{S_j} ≤ Σ_{j<n}3^{n-1-j}3^j = n·3^{n-1}`, so
`2^{S_n} ≤ 3^n ≤ 3C_n/n`.  **This is a consequence of confinement, not an addition to it**, and
it points the wrong way: it says the modulus is *dominated* by the carry, which is Lemma O.

**Status: `[ALREADY KNOWN]` (follows trivially from the existing congruences).**

## C3. Lemma O — the vacuity of the size branch

> **Lemma O.** On the zero-confined sector, `2^{S_N}/H − 1 ≤ 0` identically, `H = max(C_N, 3^N)`;
> equivalently `ρ_N ≥ 1`.  Hence the size branch of the Rev 8 §5.3 dichotomy is vacuous there.

1. Stated above; hypothesis is zero-confinement alone.
2. **Essentially Rev 8 Observation 5.9**, which states `log₂H = αN ≥ S_N` so `ρ_N ≥ 1`.  My
   contribution is only to note that this is *forced by the definition of confinement*, needing
   no arithmetic input, and that it therefore pre-empts any imported divisibility-to-size tool
   including H10's.
3. Correct; machine-checked.
4. All zero-confined words.
5. **It does not improve the problem — it explains why a class of attacks cannot.**
6. Not circular, but negative.

**Status: `[PROVED]`, substantially `[ALREADY KNOWN]` (Obs. 5.9).**

## C4. A valuation obstruction at an odd prime

> Sought: a prime `q ≠ 2` at which the word constrains the realizer, supplying a second modulus
> and hence a CRT height (the Collatz analogue of H10's contact primes).

**Disproved.**  The realizer set is `{r_N + k·2^{S_N}}`, and `gcd(2^{S_N}, q) = 1` for odd `q`,
so every class mod `q` occurs.  Verified for `q = 3,9,27,81,243,5,7,11,13`
(`results/run_primes.txt`).  This also independently reconfirms the repository's §4b.

**Status: `[DISPROVED]`.**

## C5. A "fixed δ" sink, in the H10 style

> Sought: a nonzero integer `δ`, fixed once the word is fixed, divisible by `2^{S_n}` for every
> `n` — which would immediately give `2^{S_n} ≤ |δ|` and bound `S_n`, contradiction.

**The argument form is valid and the hypothesis is unobtainable.**  If such `δ ≠ 0` existed, then
`S_n ≤ log₂|δ|` for all `n`, contradicting `S_n → ∞`; so **no such `δ` exists** for any word with
`S_n → ∞`, realizable or not.  The quantity it would have to be — `m₀ − r_n` for a hypothetical
integer realizer `m₀` — is unavailable precisely because the existence of `m₀` is what is in
question.  In H10 the corresponding `δ = f(η(a))` exists because `f` and the root are fixed while
`A` varies; **in Collatz the varying object is the congruence index `n` itself, and there is
nothing left fixed to play the role of `δ`.**

**Status: `[DISPROVED]` as stated; the gap it would fill is exactly the circular one.**

## C6. A quantitative lower bound for a positive realizer from a prefix

> Sought: `m₀ ≥ Φ(word prefix)` with `Φ → ∞`, which with `r_N < 2^{S_N}` would force
> non-realizability of long confined prefixes.

Any realizer consistent with the prefix satisfies `m₀ ≡ r_N (mod 2^{S_N})`, so the **least**
nonnegative one is `r_N` itself.  A bound `m₀ ≥ Φ` with `Φ > r_N` would contradict `r_N` being a
realizer of the prefix.  So `Φ ≤ r_N` necessarily, and `r_N` is already the sharp value: the
least-realizer frontier `r_min(N,c)` of Rev 8.  **The only way to beat it is to use information
beyond the prefix — i.e. to use infinitude, which is the problem.**

**Status: `[DISPROVED]` as a prefix-local statement; it is Rev 8's `r_min` frontier otherwise.**

## C7. A relation between successive residues

> `r_{n+1} = r_n + 2^{S_n}·t_n` with `t_n ∈ [0, 2^{d_n})` the "lift digit".

This is the definition of the 2-adic expansion of `x = lim r_n`, read in blocks of `d_n` bits.
Realizability ⟺ `t_n = 0` eventually.  The digits `t_n` are an invertible reparameterization of
the word — Rev 8's own abstract lists "lift digits" among the "invertible reparameterizations".

**Status: `[ALREADY KNOWN]`, a reparameterization.**

---

## Summary

| | candidate | status |
|---|---|---|
| C1 | residue characterization | PROVED but ALREADY KNOWN |
| C2 | new `C_n` vs `2^{S_n}` inequality | ALREADY KNOWN (trivial consequence) |
| C3 | Lemma O (vacuity of the size branch) | PROVED, substantially ALREADY KNOWN |
| C4 | odd-prime valuation obstruction | **DISPROVED** |
| C5 | fixed-`δ` sink | **DISPROVED** |
| C6 | prefix lower bound for a realizer | **DISPROVED** |
| C7 | successive-residue relation | ALREADY KNOWN (reparameterization) |

**No candidate is a genuine advance.**  C4, C5 and C6 are the three that would have been needed
to run H10's argument, and all three are false in this setting — which is why Obstruction 2 of
`03_TRANSFER_ANALYSIS.md` is structural rather than a matter of effort.
