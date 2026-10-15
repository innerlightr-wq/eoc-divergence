# VERDICT.md

## Decision

**The classification is exhaustive and sound, and it adds no arithmetic control
beyond prior results.** One new estimate was proved (Theorem D) and its content
is a **negative** answer: in the two-run class the minimum-seed cost **factors**,
so the runs can be charged separately with no cross term. Two things were
refuted — one of them a lemma I myself proposed at the end of the previous round.

Per the brief this is an acceptable outcome: *"a precise finding that the proposed
classification adds no arithmetic control beyond prior results."* It is recorded
as that, not dressed up.

## The six required answers

### 1. Which decomposition types are already controlled, and by what exact theorem?

| type | controlled by |
|---|---|
| non-injective orbits (`R_N → +∞`, eventually outside) | Rev 8 **Lemma 4.2** |
| divergent orbits (`R_n → −∞`, eventually one infinite episode) | Rev 8 **Prop. 4.8**, resting on **Thm 4.7** (García–Tal / Curry) — **external, cited, unformalised** |
| infinite alternation (case (ii) of the trichotomy) | **excluded** by the two above, *within that dependency chain* |
| bounded drift | `EOC/BoundedDrift.lean` |
| log floors, `B < 8/9` | Rev 8 **Thm 4.4** (unconditional) |
| log floors, `B < 1/β* ≈ 1.0359` | Rev 8 **Thm 4.9** (external dependency) |
| periodic / eventually periodic anchors | Rev 8 **Thms 5.4, 5.5** |
| `F_k` at fixed `k`, all states `> 1` | **Theorem C** here: `N ≤ F(k)log_2(m_0+1)`, `F(k) = Θ(α^{⌈(k+1)/2⌉})` |
| one maximal ones-run `1^u` | **Lemma A/B**: `x ≥ 2^{u+1} − 1`, sharp |
| `1^u q 1^v` | **Theorem D** here: `r+1 = 2^{u+1}A_min`, `2^{u+1}−1 ≤ r < 2^{u+q+v+2}` |

Explicitly **not** controlled, and kept out of the proved column: Rev 8
Prop. 5.6 (the finite-defect sector) — stated, never proved, status withdrawn in
Rem. 5.7 and retained here as conditional.

### 2. Did this investigation add a nonautomatic quantitative constraint beyond one-run chaining?

**No — and Theorem D proves that none exists in the chosen class.**

The candidate was that two long ones-runs separated by a recovery step would
force a combined congruence/height cost exceeding the separate one-run bounds.
They do not. Writing `x + 1 = 2^{u+1}A` with `A` odd, the word begins
`1^u q 1^v` with both runs maximal **iff** `A` lies in the single residue class
`3^{−(u+1)}(1 − 2^{q−1})` mod `2^{q+v}`. So

```
   r + 1  =  2^{u+1} · A_min ,      A_min < 2^{q+v+1} ,
```

which is exactly (first-run 2-adic cost) × (second-run congruence cost), **with
no cross term**. The only interaction is the invertibility of `3` modulo a power
of `2`. Verified against brute force on all 60 triples tested, 0 failures.

Theorem C — the chaining baseline — is genuinely new *as a stated inequality with
explicit constants*, and it **corrects** the brief's candidate from
`O((k+1)α^{k+1})` down to `Θ(α^{⌈(k+1)/2⌉})`, because only the ones-runs
compound and there are about `k/2` of them. But the brief is right that this is
the baseline, not the advance, and I record it as such.

### 3. Does the new bound use the original seed, the entry seed, or a least-realizer parameter?

All three appear, and they must be kept apart:

* **Theorem C** is in terms of the **original seed**, `log_2(m_0+1)`, and
  concerns a **finite prefix**.
* **Lemma A/B** are in terms of the **entry state** of the run, `x`.
* **Theorem D** is a **least-realizer** statement: `r(1^u q 1^v)` is the least
  odd realizer of the word, and the bound `2^{u+1}−1 ≤ r < 2^{u+q+v+2}` is a
  statement about that minimum, not about any particular orbit's seed.

Control A is the reason this matters: the word, its direction runs, `k`, its
episodes and its `W` are **realizer-class invariants** (verified on four lifts of
one word), while the absolute seed is not. So making *some* realizer large is no
evidence that the *least* realizer grows — and conversely a least-realizer floor
is not obtained from any single orbit.

### 4. How do constants depend on run/turn complexity, and what happens when it grows?

`F(k) = (α^{⌈(k+1)/2⌉} + α − 2)/((α−1)(2−α))`, i.e. coefficients of
`log_2(m_0+1)` equal to `4.82, 8.64, 14.69, 39.49` at `j = 1,2,3,5` ones-runs.
**Exponential in `k`.** A bound uniform in each fixed `k` is not uniform as
`k → ∞`, and the union over `k` proves nothing without controlling how `k` grows.

What happens when it grows is the decisive measurement. Over **all** odd
`3 ≤ m_0 < 60001` at `c = 1`, across 7301 complete episodes of length `≥ 10`:

```
   mean k/ℓ  =  0.4537 ,      max ℓ with k ≤ 2  =  15 ,     max ℓ with k ≤ 4  =  22
```

and the Loeb episodes have `k = 7, 1, 3, 25, 0, 3, 1` — the length-`64` one lies
in `F_25`. So `k` is **linear** in `ℓ` in the real population: a fixed-`k` class
contains only **bounded-length** episodes, and at the Loeb seed's own `j = 28`
the baseline reads `N ≤ 2.98×10^7` against `N = 138`. **The hierarchy is
astronomically vacuous exactly where the population lives.** Corollary C1 forces
only `k ≳ 3.01·log_2(N/L)`, far below the observed linear growth.

### 5. What, if anything, follows for a single infinite confined episode or total occupation?

**Nothing, and the reason is structural.**

By Rev 8 Prop. 4.10 a divergent orbit restarted at its last drift maximum is
**one infinite zero-corridor episode**. Every result here is either a finite-prefix
bound (Theorem C, which needs all states `> 1` and a fixed `k`), a finite-word
least-realizer bound (Theorem D, Lemma A/B), or an exclusion of a *tail* shape
already covered by prior work. Proposition I shows an infinite episode must have
**infinitely many** turns, which is precisely the case where `F_k` says nothing.

Nor does anything here bound total occupation. An upper bound on each episode in
terms of `log m_{a_i}` does not control `Σℓ_i` in terms of `log m_0` without an
amortization theorem — and the previous round proved there is no amortizable
resource (Rev 8 Rem. 13.3's scope is preserved verbatim).

### 6. What explicit class remains, and what is the smallest noncircular next estimate?

**Remaining:** infinitely many internal direction changes, with positive-integer
realization at every depth — not assumed Sturmian, periodic, typical or
low-complexity, and consistent with the measured `k/ℓ ≈ 0.45`.

> **Next estimate (REGENERATION-COST).** There exist `C, θ > 0` such that for
> every odd `x > 1` with `v_2(x+1) = 1`, writing `x' = (3x+1)/2^{v_2(3x+1)}` for
> the next state,
> ```
>    #{ x < X : v_2(x'+1) − 1 ≥ w }  ≤  C·X·2^{−w}      and      — the content —
>    Σ_{n<N} ( v_2(m_n+1) − 1 )  ≤  θ·N + O(log m_0)
> ```
> along every orbit with distinct states: the **total 2-adic resource consumed by
> ones-runs in the first `N` steps is linear in `N` with an explicit constant
> `θ < 1`, plus the seed's contribution.**

**Why this one.** Lemma A identifies the exact resource: `v_2(m+1)` is spent one
unit per `d = 1` step and **regenerated** by each `d ≥ 2` step to a new value.
Theorem C compounds precisely because the regeneration is unbounded — that is the
single mechanism behind the `α^{k/2}`. A linear bound on the *total* regeneration
would replace `α^{⌈(k+1)/2⌉}` by a constant and make the hierarchy uniform in
`k`, which is the only way a `F_k` theorem can reach the residual.

**Why it is not circular.** It mentions no corridor, no occupation, no `R_n`, and
no lifetime; it is a statement about the distribution of `v_2(m+1)` along an
orbit, in the same currency as the mod-3 packing of Rev 8 Lemma 4.3. It is not
EOC or lifetime control rewritten, and it does not presuppose divergence.

**Why it is not free, and the honest risk.** The first half is a counting
statement about one step and is plausibly provable; the second half is a pathwise
statement about an actual orbit and may be exactly as hard as the problem. The
measured `k/ℓ ≈ 0.45` says the regeneration behaves like a geometric variable of
mean `≈ 2`, consistent with `θ ≈ 1`, so the useful range `θ < 1` is not
guaranteed. Deciding that is the next concrete step.

## Refuted in this round

| item | status |
|---|---|
| **(DEPTH–DURATION)**, the lemma I proposed last round: `max_{n∈I}(c − R_n) ≤ K log_2 ℓ + C` with `K < 1` | **REFUTED** by `D_L`, verified at `L = 1..16`: `w_max = (α−1)(L+1) − 1` is **linear** in `ℓ = L` while `W_L < 16/3`. The cost moves into the seed (`2^{L+4} \| m_0+3`). *It does not refute the version restricted to globally divergent orbits — `D_L` seeds reach `1`.* |
| the brief's candidate `F(k) = O((k+1)α^{k+1})` | **CORRECTED** to `Θ(α^{⌈(k+1)/2⌉})` |
| a combined cross-run cost in `1^u q 1^v` | **REFUTED** by Theorem D: the cost factors exactly |
| my `j = 1` sharpness panel for Mersenne seeds | **mis-specified** (those seeds have `j > 1`); corrected |
| my `D_L` episode assertion | **mis-specified** (time zero counts, so `[0,1)` is a genuine initial episode); corrected |
| my brute-force test for Theorem D | **mis-specified** (omitted the trailing `d ≥ 2` maximality test, so longer second runs passed); corrected |

## Scope

Nothing here proves, advances, weakens or conditionally establishes EOC, Open
Problem F, `(DE)`, divergence exclusion, cycle exclusion, or the Collatz
conjecture. No corridor-uniform lifetime hypothesis is assumed. Rev 8 Thm 4.7 /
Prop. 4.8 / Thm 4.9 / Prop. 4.10 carry an **external, unformalised** dependency
(García–Tal, Curry) which is retained wherever used. Rev 8 Prop. 5.6 remains
**unproved** and is not promoted. **No Lean verification is claimed**: no
`lake build` was run, and every Lean reference is source-backed by reading the
named file. No ordinary-parity Sturmian theorem is applied to the drift word
`s_n`, because the translation was not proved.
