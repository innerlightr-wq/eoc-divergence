# ANALYSIS_PLAN.md — recorded before any new test

**Objective.** Classify Loeb's corridor episodes by internal drift-direction runs,
populate the classification with what is already proved, and attempt ONE new
restricted arithmetic estimate just beyond it.

**Conventions.** Rev 8 zero-based: `m_{n+1} = (3m_n+1)/2^{d_n}`, `d_n = v_2(3m_n+1)`,
`S_0 = 0`, `R_n = S_n − αn`, `α = log_2 3`. Occupied: `R_n ≤ c`, decided exactly by
`2^{S_n} ≤ 2^c 3^n`. Episode `I = [a,b)` maximal consecutive occupied; `ℓ = b−a`;
complete iff `R_b > c`. Transition block `D_I = (d_a,…,d_{b−1})`
**boundary-inclusive**: includes the outgoing transition to `b`, excludes `d_{a−1}`.
Direction symbol `s_n = 0` iff `d_n = 1`, `s_n = 1` iff `d_n ≥ 2`; `k(D)` = number
of changes; `F_k` = blocks with at most `k` changes. `s_n` is a **drift** symbol —
not the parity word, not the direction of growth of `m_n`.

**Step 1 — the 2-adic characterisation (expected to drive everything).** Prove
`d_n = 1 ⟺ v_2(m_n+1) ≥ 2`, and that a `d=1` step decreases `v_2(m+1)` by exactly
one, so the maximal `d=1` run from `x` has length exactly `v_2(x+1) − 1`. Check
the off-by-one against the brief's `2^{u+1} | x+1`, `x ≥ 2^{u+1}−1`.

**Step 2 — the elementary baseline, derived then corrected.** From
`y+1 = 3^u(x+1)/2^u` and `y−1 ≤ (3/4)^v(x−1)`, chain to a fixed-turn lifetime
bound. The brief's candidate is `F(k) = O((k+1)α^{k+1})`; **derive it rather than
assume it**, and report the correction if the exponent is smaller. Expectation:
only the ones-runs compound, so `F(k) = Θ(α^{⌈(k+1)/2⌉})`. No corridor hypothesis
should be needed. Then record the forced growth of `k` — **not** as divergence
exclusion.

**Step 3 — verify the `D_L` control independently.** `D_L = (3, 1^L, L+2)`,
`c = 1`. Check `I = [2,L+2)`, `ℓ = L`, `R_n = 2−(α−1)n`,
`w_max = (α−1)(L+1)−1`, `W_L = (16/3)(1−(2/3)^L)`, and the seed condition
`2^{L+4} | m_0+3`, via the exact realizer congruence **and** direct iteration.
Expected consequence: it **refutes** the (DEPTH–DURATION) lemma I proposed at the
end of the previous round, for complete finite episodes.

**Step 4 — the main attempt, written before testing.** Class `1^u q 1^v` with
`q ≥ 2`, ones-runs maximal. Candidate: the realizing set factors as
```
   x + 1 = 2^{u+1} A ,  A odd,  A ≡ 3^{−(u+1)}(1 − 2^{q−1})  (mod 2^{q+v}) ,
```
so `r + 1 = 2^{u+1}·A_min` with `A_min < 2^{q+v}`, giving
`2^{u+1} − 1 ≤ r < 2^{u+q+v+1}`. **If this factorisation holds the answer to the
primary question is NO**: the cost is (first-run 2-adic cost) × (second-run
congruence cost) with no cross term, i.e. exactly charging each run separately.
Record that as the finding rather than dressing it up.

**Step 5 — coverage and remainder.** For each class: membership rule, prefix vs
episode vs tail, which parameter is fixed, seed vs entry state vs least realizer,
constant dependence, overlap, and the uncontrolled residual. The residual to keep
explicit: **infinitely many internal direction changes with positive-integer
realization at all depths.**

**Controls (pre-specified).** Loeb `m_0 = 285175, c = 1` direction-run signatures;
least realizer vs lifts; long all-ones (Mersenne) prefixes; `D_L`; the Prop. 13.2
oscillator; eventual fixed-point tail; and the prescribed-word positive-real
affine trajectory with no integer ray (to separate what integrality supplies).

**Stopping rule.** Stop if the only new content is a taxonomy, a
reparameterisation, or a fixed-`k` elementary bound; say so plainly.
