# DEPENDENCY_LADDER.md — what each stronger conclusion would additionally need

Four levels, kept apart. Every bridge is proved here, cited to a tracked file, or
named as missing.

---

## LEVEL A — a two-run exponential floor

> **DONE, unconditionally.** `r(1^u q 1^v) + 1 ≥ 2^{(log₆2)S}`,
> `log₆2 = 0.38685280723…` (`TWO_RUN_FLOOR.md` Theorem U; 2912 triples, 0
> violations). No digit input.

Raising the exponent towards `1` needs a **pointwise** lower bound on the least
positive residue of `3^{−(u+1)}c` mod `2^{n+1}` along a diagonal, and only on the
band `u+1 ≍ 0.39S`, `n ≍ 0.61S` (`TWO_RUN_FLOOR.md` §3). Threshold:
`κ < 1/log₂3 = log₃2 = 0.63093`, exponent `= 1 − κ log₂3`.

## LEVEL B — all confined words, i.e. `L_c(m) = O(log m)`

**The equivalence is already on record.** Rev 8 Prop. 6.4:
`r_min(N,c) = min{m odd : L_c(m) ≥ N}`. So an exponential realizer floor for
**all** `c`-confined words of length `N` is equivalent to `L_c(m) = O(log m)`.

**Level A contributes nothing uniform to it.** Level A covers words with **two**
runs. Real confined episodes have `k ≍ 0.45·ℓ` direction changes — measured over
7301 complete episodes in
[`episode_classification_2026-10-14`](../episode_classification_2026-10-14/CLASSIFICATION.md)
§4: `mean k/ℓ = 0.4537`, and `k ≤ 2` forces `ℓ ≤ 15`, `k ≤ 4` forces `ℓ ≤ 22`. The
two-run family is a bounded-length sliver of the population.

> **Missing theorem (B).** A lower bound on the least positive residue of
> `3^{−N}C_N(D) mod 2^{S+1}`, uniform over all `c`-confined words `D` of length
> `N` — i.e. control of the **moving anchor** `ξ_N(D) = −C_N(D)·3^{−N}`.

Rev 8 Remark 5.8 is explicit that for a general confined word this anchor
**changes with `N`**: "there is no single fixed rational whose periodicity can be
invoked. This is the moving-anchor sector, and it is where actual Collatz orbits
live." That is Rev 8's Open Problem C/D.

**The three structural routes all fail**, and the reasons are recorded rather
than asserted:

* **bounded number of runs** — vacuous: `k ≍ 0.45ℓ`, so the class is empty for
  long words;
* **`k = o(N)`** — also false in the measured population: `k/ℓ` is bounded
  *below* by a constant, not above;
* **decomposition into two-run blocks with bounded overlap** — the *bit count*
  composes (Theorem D: the class modulus is `2^{u+1}·2^{n+1}`, a product with no
  interaction term), but **the placement does not**: `A*` of a concatenation is
  not a function of the `A*`s of the blocks, because the anchor is a global
  function of the whole carry `C_N(D)`.

> **Level A is not a stepping stone to Level B. It is the smallest instance of
> the same difficulty**, and the bit-count/placement split is exactly why finer
> decompositions cannot help.

## LEVEL C — exclusion of one infinite zero-confined positive orbit

Suppose `m_0` is zero-confined at every depth. By `EOC/Realizer.lean`'s
`residue_pinning` (in `eoc-lean-verification`), for every `N` with
`m_0 < 2^{S_N+1}` — i.e. every `N > log₂m_0`, since `S_N ≥ N` — `m_0` **is** the
least realizer of its own depth-`N` word. Hence
```
   r(D_N) = m_0   for all large N ,      so   log₂(r(D_N)+1)  is BOUNDED ,
```
and by the bit accounting of `TWO_RUN_FLOOR.md` §1 the placement must save
`≥ S_N − log₂(m_0+1) + 2` bits at **every** depth.

> **Verdict: no clean Level-C statement exists.** The candidate — "along every
> infinite zero-confined word the placement saving is `< S_N − C` infinitely
> often" — is *literally* "`r(D_N) > 2^C` infinitely often", i.e. `r(D_N) → ∞`,
> i.e. no fixed positive integer realizes the infinite word. That is the
> conclusion itself.
>
> A weaker *qualitative* statement cannot substitute, because the requirement is
> not that some saving be impossible but that the **total** saving fail
> infinitely often — a condition on every depth simultaneously, which is the
> pointwise problem.

So **Level C is not reachable by strengthening Level A**, and any statement
strong enough to reach it is a transcription of positive realizability failing.

## LEVEL D — full fixed-corridor EOC, including separated returns

Full EOC bounds `O_c = Σ_i ℓ_i` over **all** episodes. Levels A–C concern a
single word or a single window.

> **Even a complete solution of the two-run placement problem would not by itself
> prove full EOC.**

The reasons are already on record. Rev 8 Remark 6.2: `m_0 = 285175` has
`L_1 = 14` but `O_1 = 98`, so `83` of the `98` occupation times lie in later
episodes a single-window theory cannot see. Rev 8 Remark 13.3 shows the natural
per-episode surrogate overcounts by `Ω(log m_0)`. And
[`joint_episode_budget_2026-10-14`](../joint_episode_budget_2026-10-14/VERDICT.md)
proved there is **no amortizable resource** — the per-episode allowance is pinned,
not consumed — and that the carry pot is `Θ(m_0)` against an `O(log m_0)` target.

> **Additional theorem required for Level D.** A recurrence/amortization theorem
> bounding `Σ_i ℓ_i` in terms of `log m_0`. No placement theorem at the two-run or
> single-window level bears on it, because placement concerns one word while
> `O_c` sums over disjoint words at different entry heights.

## The ladder in one line each

```
   A   two-run floor, exponent log_6 2                 DONE, unconditional
   A+  exponent -> 1                                   needs pointwise control of
                                                       3^{-(u+1)} c mod 2^{n+1} on the
                                                       0.39/0.61 band
   B   all confined words  (= L_c = O(log m))          needs the MOVING-ANCHOR theorem
                                                       (Rev 8 Open Problem C/D);
                                                       A does not reduce it
   C   no infinite zero-confined positive orbit        NO clean formulation: any
                                                       sufficient statement restates
                                                       positive realizability
   D   full EOC incl. separated returns                needs an amortization theorem in
                                                       addition; no placement theorem
                                                       bears on it
```
