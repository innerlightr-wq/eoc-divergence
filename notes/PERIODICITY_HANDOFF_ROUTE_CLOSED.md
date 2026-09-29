# Periodicity-bridge handoff: route closed

**Status: ROUTE CLOSED / CIRCULAR.** Recorded 2026-09-29, from a falsification-first
cross-program audit of this repository against
[`innerlightr-wq/periodicity-conjecture-bridge`](https://github.com/innerlightr-wq/periodicity-conjecture-bridge)
and `innerlightr-wq/eoc-lean-verification`.

**Index:** this is one of three closed pointwise routes; the consolidated view, with a
negative-results table, is [`CLOSED_POINTWISE_ROUTES_2026-09-29.md`](CLOSED_POINTWISE_ROUTES_2026-09-29.md).

This note changes no conclusion of the programme. It records the exact reason **symbolic
periodicity and repetition are not the missing pointwise separator**, so that the route is not
re-opened.

**Novelty discipline.** The qualitative conclusion was already on record here: Revision 7 §5.3
and **Observation 5.9** — *"the separating invariant is height amortization, not symbolic
complexity"* — plus Remark 9.5 (the one word-level invariant sharp enough to decide
realizability is a restatement of realizability) and the abstract's "words of non-critical
density are excluded by density alone". The companion repository's `LADDER.md` records the same
from its side. *This audit supplies the exact identity, the quantified obstruction, and certified
verification — not the original qualitative observation.* Nothing below is claimed as new
mathematics beyond that.

---

## 1. Audit setup

Tested chain:

```
    divergent integer orbit
        ↓                         Thm 6.14 / Divergence.divergent_iff_zeroConfined
    zero-confined positive odd seed m₀,  2^{S_n} ≤ 3^n for every n
        ↓                         ← the step under test, not assumed
    periodic approximants W_n with unbounded bridge surplus
        ↓                         Periodicity Bridge abstract criterion
    Φ(s) ∉ ℚ
        ↓
    contradiction, since Φ(s) = m₀ ∈ ℚ
```

Frozen inputs: this repository at `de2fdea`, the bridge repository at `e4708a2`,
`eoc-lean-verification` at `6cb67e7`. Verification: 8 scripts, standard library only, exact
integer / `Fraction` arithmetic for every pass/fail decision; survivor data taken from the
existing certified record holders of `audits/record_holder_anatomy/` (`r_min(N,0)` certified
`N = 1…346`), not newly invented.

**Notation bridge.** The standard (Lagarias) parity word of an odd `m` is
`concat_i (1 0^{a_i − 1})`, so at accelerated depth `n` one has `ℓ = S_n`, `k = n`, and the
bridge's periodic numerator `c_W` **is** this programme's aggregate carry `C_n`. Zero
confinement is exactly `2^ℓ ≤ 3^{k_ℓ}` at every 1-position, i.e. asymptotic one-density
`≥ β = 1/log₂3 = 0.6309297535714575` — the bridge's own critical-density branch point.

## 2. The strongest proved cross-program identity

Both directions are exact, and the `⟹` half is already Lean in this repository
(`Divergence.modEq_of_parity_prefix`); the `⟸` half is Terras / Bernstein–Lagarias bijectivity
of `Q_L : ℤ/2^L → {0,1}^L`:

```
    x_i ≡ x_j (mod 2^L)      ⟺      s[i : i+L] = s[j : j+L]
    lcp(s, W_ℓ^∞)            =      ℓ + v₂( m₀ − T^ℓ(m₀) ),      W_ℓ := s[0:ℓ]
```

Verified exactly: 400 random odd seeds below `10¹²` × 12 000 `(i,j,L)` triples, and every
zero-confined checkpoint of 17 record holders — **0 failures**.

So residue recurrence **is** symbolic repetition. The translation costs nothing. That is why it
does not help: the obstruction is entirely arithmetic.

## 3. The exact surplus cap

> **Theorem H1.** Let `m₀ ≥ 1`, `ℓ ≥ 1`, `W = s[0:ℓ]`, `k = |W|₁`, `d = 2^ℓ − 3^k`,
> `F(W) = |d| + c_W`, and `x_ℓ := T^ℓ(m₀) ≠ m₀`. Then
>
> 1. `M := m₀ d − c_W = 2^ℓ (m₀ − x_ℓ)` — this is `aggregate_identity` (Lemma 2.4), rearranged;
> 2. `lcp(s, W^∞) = ℓ + v₂(m₀ − x_ℓ)`;
> 3. with `h_eff := |M|/F(W) ∈ (0, m₀]`,
>    ```
>        S(W) := lcp(s, W^∞) − log₂ F(W)  =  log₂ h_eff − log₂ oddpart(x_ℓ − m₀);
>    ```
> 4. hence **`S(W) ≤ log₂ m₀` for every `ℓ`**, strictly when `m₀ > 1`;
> 5. on the zero-confined sector (`d < 0 < c_W`) the archimedean step is an *equality*,
>    `|M| = m₀|d| + c_W`.

Verified exactly at **1 862** zero-confined checkpoints across 15 certified record holders, plus
400 random odd seeds × 130 prefix lengths: 0 failures.

Equivalent quantified form, with `R_n = S_n − nα`:

```
    S(W)  =  v₂(m₀ − m_n)  −  |R_n|  +  O(log n).
```

**Reading.** The bridge's surplus, restricted to a realizable word, is a two-term function of the
aggregate identity alone; the criterion's hypothesis `limsup S = +∞` is **unsatisfiable** on the
realizable sector, not merely unproved. This is the exact form of Observation 5.9: there,
`ρ_N = log₂H/S_N ≥ 1` makes the divisibility-to-size branch vacuous for arbitrary confined
words; here the same branch is evaluated in closed form.

Measured: max surplus over all prefix roots is 2.0–8.7 across the record holders, against the
ceiling `log₂ m₀` of 2.8–25.9, and it regresses on `log₂ m₀` with slope `0.176` — it tracks the
**seed**, never the window length.

## 4. Zero-confinement countermodels

Construction: for any bit stream `b`, set `a_i = 1 + b_i` when `S_i + 1 + b_i ≤ ⌊(i+1)α⌋`, else
`a_i = 1`. The budget grows at rate `α − 1 = 0.585` per step, so a positive density of bits is
transmitted. Every output word is zero-confined by construction.

| driver | confined | one-density | `p(6), p(10), p(14), p(18)` | longest initial square | max surplus |
|---|---|---|---|---|---|
| random | ✔ | 0.6707 | 21, 144, 970, 4 171 | 3 | 9.18 |
| binary Champernowne | ✔ | 0.6535 | 21, 144, 922, 3 543 | 3 | 8.42 |
| Thue–Morse | ✔ | 0.6667 | 13, 30, 40, 56 | — | — |

Exact count of zero-confined valuation words of length `N` (transfer recursion, exact integers)
rises to `2^{1.364 N}` at `N = 60`, toward `α H₂(1/α) = 1.50564` bits per accelerated step, i.e.
**`H₂(1/α) = 0.949956` bits per standard letter** — this repository's own baseline exceptional
exponent.

> Zero confinement alone forces nothing: not bounded complexity, not repetition, not balance,
> not positive surplus — and not low complexity either (the Thue–Morse-driven instance is
> confined and has linear complexity). It is a positive-entropy symbolic set.

## 5. Survivor windows are highly complex and essentially unbordered

Full zero-confined prefixes of the certified record holders, standard coding:

| `m₀` | depth `N` | `|W|` | longest initial square | longest proper border | shortest period | `p(12)` | max surplus |
|---|---:|---:|---:|---:|---:|---:|---:|
| 27 | 36 | 56 | 1 | 0 | 56 | 45 | 3.26 |
| 703 | 50 | 77 | 3 | 0 | 77 | 66 | 5.11 |
| 1 126 015 | 140 | 217 | 3 | 0 | 217 | 195 | 6.00 |
| 8 088 063 | 154 | 243 | 4 | 0 | 243 | 219 | 8.72 |
| 13 421 671 | 180 | 283 | 5 | 0 | 283 | 256 | 6.07 |
| 63 728 127 | 236 | 373 | 4 | 1 | 372 | 314 | 8.00 |

Longest proper border is **0 in 13 of 18** windows and never exceeds 6; shortest period equals
the full window length almost always; `p(12)` sits at **87–100 %** of the combinatorial ceiling
`|W| − 11`. The best periodic witness is a root of length 1–16 in most cases. This is the same
finding as the existing Sturmian-proximity measurement in
`audits/record_holder_anatomy/REPORT.md` §3.1 (best lcp with any shift of the critical Sturmian
word: **1–3 valuations** at depths to 236), seen from the periodic-approximation side.

## 6. Rote density mismatch

Complementary symmetric Rote sequences — the bridge's headline class, factor complexity exactly
`2n` — have one-density **exactly `1/2`**. That is not incidental: it is the bridge's own
load-bearing structural fact (`theorems/phase4/REQUIRED_EXPONENT.md`), the one that drops the
required repetition exponent from `2 log₂3 ≈ 3.17` to `2` and makes the bounded-type theorem
close.

Since `1/2 < β = 0.63093`, **no CS Rote sequence is `c`-confined for any fixed `c`**, at any
slope, either seed, any shift. Measured over 2 000 shifts × both seeds × 4 slopes: best confined
depth 5–13 at `c = 0`, 317–333 at `c = 64` — widening the corridor by 64 bits buys `~320` letters
and then stops, exactly as a constant density mismatch predicts.

> The bridge's genuinely new theorems (its Phases 2–7) are **vacuous** on this programme's
> survivor sector. The rungs that *do* meet the sector — eventually periodic words, Sturmian
> words, sub-threshold-complexity words — were already excluded here: the signed marker **P1**,
> `audits/sturmian_all_words` (`Φ(s) ∉ ℚ` for *every* Sturmian word), and Revision 7's density
> exclusion. Net effect on `F_EOC ∩ A_ℚ`: **zero**.

## 7. The Dubickas threshold has zero spare margin

The transported counting bound (source paper Prop. 9.2) gives, for any `s` with `Φ(s) ∈ ℚ` of
height `H₀`: `p_s(L) ≥ ⌊(L − 1 − log₂ H₀)/log₂(3/2)⌋ + 1`. Corollary 9.3 then excludes
`liminf p_s(L)/L < 1/log₂(3/2) = 1.7095112913514547`. **The hypothesis of Cor. 9.3 is the exact
negation of the conclusion of Prop. 9.2, with the same constant.**

Specialising to `H₀ = m₀` and using `injective_iff_divergent` gives a genuine, proved, effective
statement:

> The standard parity word of a divergent `3x+1` orbit with seed `m₀` satisfies
> `p_s(L) ≥ ⌊(L − 1 − log₂ m₀)/log₂(3/2)⌋ + 1` for every `L`.

**This is a specialization of Proposition 9.2, not a new theorem.** It constrains divergent
orbits; it cannot exclude them, because its constant *is* the threshold that would be needed.

## 8. Why the proposed lemma is circular

The bridge's most general sufficient condition is "arbitrarily long initial squares suffice,
unconditionally". Under §2's dictionary and the elementary growth bound `x_{t+1} ≤ (3x_t+1)/2`:

> **Theorem H2a.** If the parity word of an integer `n₀ ≥ 1` begins in a square `WW` with
> `|W| = L` and `T^L(n₀) ≠ n₀`, then `4^L ≤ 3^L(n₀+1)`, i.e. `L ≤ 2.4094 log₂(n₀+1)`.

Measured on the record holders: actual half-lengths **1–8** against caps 7–63 — the cap is loose
and reality is far below it.

Hence the step under test,

> **(LEMMA X)** every zero-confined positive odd integer admits some depth `n` with
> `v₂(m₀ − T_acc^n(m₀)) > log₂ m₀ + |R_n| + C log n`
> — equivalently, an initial square of half-length exceeding `2.4094 log₂(m₀+1)` —

holds **iff** no zero-confined positive odd integer exists:

```
        LEMMA X   ⟺   (DE)   ⟺   no divergent 3x+1 orbit.
```

> **A "large repetition surplus" lemma would already imply divergence exclusion. It is therefore
> circular — equivalent in strength to the desired conclusion, not weaker than it.** Every
> theorem of the shape "EOC conditions ⟹ long repetitions ⟹ `Φ(s) ∉ ℚ`" inherits this, because
> the middle term is unavailable for a realizable word.

## 9. Two further routes checked and closed

**Carry bounds are already optimal, and that is what closes the route.** Confinement gives, in
one line, `3^{n−1} ≤ C_n ≤ n·3^{n−1}` (verified at all 1 862 confined checkpoints, 0
violations), so `log₂ F(W) = αn + O(log n)`, two-sided. The lower bound is what forbids further
improvement, and with an optimal height the surplus becomes `v₂(m₀ − m_n) − |R_n| + O(log n)`:
the deficit lives entirely in the depth term, which carry control cannot touch. Note `c_W = C_n`
exactly — there is no mismatch to fix.

**Realizer congruences cannot force repetition.** The word ↔ residue correspondence is a
bijection (`EOC.realizerCongruence`, `leastRealizer_unique` in `eoc-lean-verification`), so a
congruence condition on the realizer *is* a condition on the word and vice versa. Neither forces
structure in the other; there is no realizer-to-repetition lemma to find.

**Band rigidity is the one genuine EOC ⟹ low-complexity implication, and it is vacuous here.**
Revision 7 App. A (= Revision 5 Thm A.1): a unit drift band forces every letter into `{1,2}` and
the word to be a Sturmian factor of slope `θ = α − 1`, with exactly `ℓ+1` admissible words. The
standard parity word is then the image of a Sturmian word under the Sturmian morphism
`0 ↦ 1, 1 ↦ 10`, hence Sturmian, hence `Φ(s) ∉ ℚ` by `audits/sturmian_all_words`. But a
divergent orbit has `R_n → −∞` and leaves every fixed unit band; measured unit-band windows on
the certified survivors are **4–9 accelerated letters** long. Proved implication, empty
hypothesis on the target sector — consistent with App. A's own note that narrow corridors are
not automatically easier.

## 10. Consequence for the search for the missing pointwise tool

> **The missing EOC pointwise tool should not be sought as:**
> * a **low-complexity theorem** — the survivor sector has entropy `0.949956` bits per standard
>   letter and its certified windows sit at 87–100 % of the complexity ceiling;
> * a **generic long-repetition theorem** — Theorem H2a caps initial squares at
>   `2.4094 log₂(n₀+1)` for *every* integer, divergent or not, and the countermodels of §4 show
>   confinement forces no repetition at word level;
> * a **periodic-approximation surplus theorem** — Theorem H1 evaluates the surplus in closed
>   form and caps it at `log₂ m₀`; all packagings (squares, general powers, low-discrepancy
>   roots, near-critical resonance) enter through the same `lcp` and the same `F(W)`, and both
>   are pinned.

More generally, **every tool whose only arithmetic input is "a nonzero multiple of `2^m` has
absolute value at least `2^m`", applied to the aggregate identity, is now known to evaluate on
this sector to `log₂ h_eff − log₂ oddpart(m_n − m₀)` — a restatement of Lemma 2.4.** Any future
candidate can be tested in seconds against the one-line requirement
`v₂(m₀ − m_n) > log₂ m₀ + |R_n|`.

> **The remaining direction is height / amortization / arithmetic realizability** — the
> `ρ_N = log₂H/S_N` axis of Revision 7 §5.3, the endpoint depth `δ = S + 1 − log₂ r`, and the
> realizer frontier `r_min(N,0)`. Revision 7 §5.9 already identifies this as the separating
> invariant; this audit confirms it from the Periodicity side, and notes that the one
> intermediate case (Proposition 5.6, one-defect words) is recorded in Rem. 5.7 as **unproved**,
> so that axis is genuinely open ground rather than a restatement.

Nothing here bears on the Collatz conjecture, and no claim of progress toward it is made or
implied. (DE) and (PosPC) remain open exactly as before, and the Periodicity Bridge is not a
route to either.

## 11. Controls

The method passes the full control battery — by being silent everywhere in the survivor sector.

| control | obligation | result |
|---|---|---|
| periodic parity words / known rational `Φ` | silent | ✔ (`s = W^∞` fails the standing hypothesis) |
| `3x−1`, where `+1` **is** a zero-confined positive point | silent | ✔ — as the programme's proved sign-symmetry obstruction predicts |
| `5x+1`, `7x+1`, where divergence occurs | no false proof | ✔ — the squares threshold is `log₂ q > 2`, and the elementary cap constant `2 − log₂ q < 0` |
| random zero-confined words | silent | ✔ (max surplus 2.53–11.48 over 20 words) |
| Sturmian words | exclude | ✔ — already this repository's own theorem |
| bounded-type CS Rote | exclude | ✔ — but disjoint from the survivor sector (§6) |

## 12. Pointers

* Companion note on the bridge side:
  [`docs/EOC_HANDOFF_CLOSED.md`](https://github.com/innerlightr-wq/periodicity-conjecture-bridge/blob/main/docs/EOC_HANDOFF_CLOSED.md).
* Formalization plan for Theorem H2a:
  [`docs/PERIODICITY_HANDOFF_FORMALIZATION.md`](https://github.com/innerlightr-wq/eoc-lean-verification/blob/main/docs/PERIODICITY_HANDOFF_FORMALIZATION.md)
  in `eoc-lean-verification`. Everything it needs is already in this repository's
  `Divergence/RawMap.lean`; no Lean file was changed by the audit.
* Existing programme statements this note is the exact form of: Revision 7 §5.3, Observation 5.9,
  Remark 9.5; `docs/PROGRAMME_ENDPOINT.md` (closed routes).
