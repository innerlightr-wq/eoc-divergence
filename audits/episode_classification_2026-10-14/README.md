# Episode classification by drift-direction runs — 2026-10-14

**Question.** Classify Loeb's corridor episodes by internal drift-direction runs
(`s_n = 0` iff `d_n = 1`, `k` = number of changes, `F_k` = at most `k` changes),
populate the classification with what is already proved, and attempt one new
restricted arithmetic estimate just beyond it.

**Verdict: the hierarchy is exhaustive and sound and adds no arithmetic control
beyond prior results.** One new estimate was proved and its content is a
*negative* answer. Two formulations were refuted — one of them a lemma proposed
at the end of [`joint_episode_budget_2026-10-14`](../joint_episode_budget_2026-10-14/).

Read [`VERDICT.md`](VERDICT.md) for the six answers,
[`RUN_ARITHMETIC.md`](RUN_ARITHMETIC.md) for the mathematics,
[`CLASSIFICATION.md`](CLASSIFICATION.md) for the status table and coverage.

## Results

**Lemma A (the engine).** `d_n = 1 ⟺ v_2(m_n+1) ≥ 2`; a `d=1` step sends
`v_2(m+1) ↦ v_2(m+1) − 1` exactly; so the **maximal `d=1` run from `x` has length
exactly `v_2(x+1) − 1`**. The ones-run length is a 2-adic resource, spent one unit
per step and **regenerated to an unbounded new value by each `d ≥ 2` step** — no
conservation, which is why every chaining bound compounds. Verified over all odd
`3 ≤ m_0 ≤ 60001`, 0 violations.

**Theorem C (the baseline).** For a prefix of length `N` with at most `k`
direction changes and all states `> 1`,
`N ≤ F(k)·log_2(m_0+1)` with
`F(k) = (α^{⌈(k+1)/2⌉} + α − 2)/((α−1)(2−α))`, no corridor hypothesis needed.
Only the ones-runs compound, and there are about `k/2` of them. Coefficients
`4.82, 8.64, 14.69, 39.49` at `j = 1,2,3,5`. Holds on 11 real seeds, 0 failures.
Corollary: `k ≳ 3.0100·log_2(N/L)` — **not** divergence exclusion.

**Theorem D (the main attempt, and its negative answer).** For `1^u q 1^v` with
both ones-runs maximal, the word is realized **iff** `x+1 = 2^{u+1}A` with `A` odd
in the single class `A ≡ 3^{−(u+1)}(1 − 2^{q−1}) (mod 2^{q+v})`, so
`r+1 = 2^{u+1}A_min` with `A_min < 2^{q+v+1}` and
`2^{u+1}−1 ≤ r < 2^{u+q+v+2}`; the floor is attained exactly at the Mersenne
seeds. **The minimum-seed cost factors as (first-run 2-adic cost) × (second-run
congruence cost) with no cross term.** Verified against brute force on all 60
triples tested, 0 failures.

**Coverage — the decisive measurement.** Over all odd `3 ≤ m_0 < 60001` at
`c = 1`, across 7301 complete episodes of length `≥ 10`:
`mean k/ℓ = 0.4537`, `max ℓ with k ≤ 2 = 15`, `max ℓ with k ≤ 4 = 22`; the Loeb
episodes have `k = 7, 1, 3, 25, 0, 3, 1`. **`k` is linear in `ℓ`**, so a fixed-`k`
class holds only bounded-length episodes and the baseline is astronomically
vacuous where the population lives.

**`D_L = (3, 1^L, L+2)` — and it refutes a previously published proposal.**
Verified at `L = 1..16` by exact realizer congruence and direct iteration:
episodes `[0,1) ∪ [2,L+2)`, `ℓ = L`, `w_max = (α−1)(L+1)−1`,
`W_L = (16/3)(1−(2/3)^L) < 16/3` exactly, `2^{L+4} | m_0+3`. So
`w_max ≤ K log_2 ℓ + C` is **false** for complete finite positive-orbit episodes,
**refuting the (DEPTH–DURATION) lemma** proposed in
[`joint_episode_budget_2026-10-14/VERDICT.md`](../joint_episode_budget_2026-10-14/VERDICT.md) §6.
The cost moves into the seed, linearly in the depth. It does *not* refute the
version restricted to globally divergent orbits.

## Limits

Nothing here proves, advances or conditionally establishes EOC, Open Problem F,
divergence exclusion, cycle exclusion, or the Collatz conjecture. A divergent
orbit is **one infinite episode with infinitely many turns** (Rev 8 Prop. 4.10
plus Proposition I here), which is exactly where `F_k` says nothing. The external
García–Tal/Curry dependency is retained wherever used; Rev 8 Prop. 5.6 stays
unproved; **no Lean verification is claimed**; and no Sturmian theorem is applied
to the drift word `s_n`, because the translation was not proved.

## Reproduction

CPython standard library only. **Corridor membership is the integer comparison
`2^{S_n} ≤ 2^c·3^n`; carries, realizer congruences and weighted sums are exact
`int`/`Fraction`.** One worker, peak RSS ≤ 17 MiB.

```bash
python3 scripts/run_arithmetic.py   # Lemmas A,B and Theorem C           ~60 s
python3 scripts/two_run.py          # D_L control and Theorem D          ~90 s
python3 scripts/controls.py         # Loeb classifier + controls A-E     ~15 s
python3 scripts/coverage.py         # the F_k coverage measurement       ~90 s
python3 tests/regression.py         # 11 assertions, clean process       ~60 s
```
