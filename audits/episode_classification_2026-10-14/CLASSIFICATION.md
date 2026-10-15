# CLASSIFICATION.md — the hierarchy, its status, and its coverage

Conventions as in `ANALYSIS_PLAN.md`. `s_n = 0` iff `d_n = 1` (falling drift),
`s_n = 1` iff `d_n ≥ 2` (rising drift); `k(D)` = number of changes; `F_k` =
episode blocks with at most `k` changes. Blocks are **boundary-inclusive**:
`D_I = (d_a,…,d_{b−1})` includes the outgoing transition to `b` and excludes the
entry transition `d_{a−1}`, which is stored separately.

**`s_n` is a drift symbol.** It is not the ordinary Collatz parity word, not the
word `d_n − 1` restricted to `d_n ∈ {1,2}`, and not the direction of growth of
`m_n` — above `m_n = 1` falling drift means the orbit *increases*. No Sturmian or
parity theorem is applied to `s_n` anywhere in this package, because the
translation was not proved.

---

## 1. The global trichotomy, and what narrows it

> **Proposition T (elementary).** For an infinite occupancy sequence
> `{n : R_n ≤ c}` exactly one of: (i) it is finite — eventually outside the
> corridor; (ii) it is infinite with infinitely many maximal gaps — infinitely
> many finite episodes; (iii) it is cofinite — eventually one infinite episode.
> *Proof.* Trichotomy on whether the occupied set and its complement are finite. ∎

**Narrowing for actual positive orbits** — *this is a consequence of prior
results, with an external dependency retained; it is not a new theorem and not a
fresh Lean verification.*

* Rev 8 **Lemma 4.2**: if the orbit reaches `1` or enters a nontrivial positive
  cycle then `R_N → +∞`; every non-injective orbit has `R_N → +∞`. Hence
  non-injective ⟹ case (i).
* Rev 8 **Proposition 4.8**, resting on **Theorem 4.7** (García–Tal; explicit
  form Curry) — **external, cited, unformalised**: every divergent (equivalently
  injective) orbit has `Σ 1/m_n < ∞`, so `E_n ↑ E_∞ < ∞`, `m_n → ∞`, and
  `R_n → −∞`. Hence injective ⟹ case (iii).
* Rev 8 **Proposition 4.10** (last-maximum reduction) makes case (iii) concrete:
  a divergent orbit restarted at its last drift maximum has an infinite
  zero-corridor tail. Formalised only under the hypothesis
  `ReciprocalSummable`, i.e. conditional on the external Theorem 4.7.

> **Consequence.** Within that dependency chain, **case (ii) — infinite
> alternation — does not occur for an actual positive orbit.** Every orbit is
> eventually outside the corridor (if it reaches `1` or a cycle) or eventually
> inside one infinite episode (if divergent).

**But arbitrarily many *finite* episodes across different seeds remain possible.**
Rev 8 **Proposition 13.2** is the required control: for every `B` and every bound
`M` there is an odd `m_0 > M` whose realized prefix has `≥ B` re-entries.
Verified here (control C): the oscillator has `83` episodes in `[0,200)` at
`c = 1`, with **internal `k = 0`** in every one, while the **global** change count
over the prefix is `164`. A bound on `k` inside each episode bounds neither the
number of episodes nor the changes in the gaps.

## 2. The infinite-episode baseline

> **Proposition I (elementary).** An infinite episode cannot have finitely many
> internal direction changes.
> *Proof.* Finitely many changes means the tail is constant: either `d_n = 1` for
> all large `n`, or `d_n ≥ 2` for all large `n`. In the first case
> `R_{n+1} − R_n = 1 − α < 0`, so `R_n → −∞`, which is consistent — but by
> Lemma A a `d = 1` step decreases `v_2(m_n+1)` by exactly one, and
> `v_2(m_n+1) ≥ 2` is required at every such step, so the tail is bounded by
> `v_2(m_N+1) − 1 < ∞` steps: contradiction. In the second case
> `R_{n+1} − R_n = d_n − α ≥ 2 − α > 0`, so `R_n → +∞` and the episode ends. ∎

**This is an elementary baseline. It does not exclude infinitely many turns**,
which is exactly the residual of §5.

## 3. The status table

| class | membership | object | fixed / growing | seed parameter | bound | status |
|---|---|---|---|---|---|---|
| non-injective orbits | some `m_i = m_j` | infinite tail | — | — | `R_N → +∞`, case (i) | **[PRIOR]** Rev 8 Lem. 4.2 |
| divergent orbits | injective | infinite tail | — | — | `R_n → −∞`, case (iii) | **[PRIOR + external]** Rev 8 Prop. 4.8 ← Thm 4.7 |
| bounded drift | `\|R_n\| ≤ G` ∀`n` | infinite tail | `G` fixed | `m_0` | excluded | **[PRIOR]** `EOC/BoundedDrift.lean` |
| log floor, `B < 8/9` | `R_k ≥ −B log_2 k` | infinite tail | `B` fixed | `m_0` | excluded | **[PRIOR]** Rev 8 Thm 4.4 |
| log floor, `B < 1/β* ≈ 1.0359` | same | infinite tail | `B` fixed | `m_0` | excluded | **[PRIOR + external]** Rev 8 Thm 4.9 |
| periodic / eventually periodic anchors | `D = X^a` etc. | finite word | `X` fixed | `r(D)` | exponential realizer floor | **[PRIOR]** Rev 8 Thms 5.4, 5.5 |
| finite-defect sector `X^a E X^b` | — | finite word | — | `r(D)` | **claimed, not proved** | **[CONDITIONAL]** Rev 8 Prop. 5.6, status withdrawn in Rem. 5.7 |
| `F_k`, `k` fixed, all states `> 1` | `≤ k` changes | **finite prefix** | `k` fixed | `log_2(m_0+1)` | `N ≤ F(k)·log_2(m_0+1)`, `F(k) = Θ(α^{⌈(k+1)/2⌉})` | **[P]** `RUN_ARITHMETIC.md` Thm C |
| `1^u` (one maximal ones-run) | `v_2(x+1) = u+1` | run | `u` free | entry state `x` | `x ≥ 2^{u+1} − 1`, **sharp** | **[P, elementary]** Lem. A/B |
| `1^u q 1^v` (both runs maximal) | see Thm D | **episode core** | `u,q,v` all free | least realizer | `2^{u+1}−1 ≤ r < 2^{u+q+v+2}`, exact value `2^{u+1}A_min − 1` | **[P]** Thm D |
| `D_L = (3,1^L,L+2)` | — | complete episode | `L` free | `m_0` | `ℓ = L`, `w_max = (α−1)(L+1)−1`, `W_L < 16/3`, `2^{L+4} \| m_0+3` | **[P, verified]** `RUN_ARITHMETIC.md` §4 |
| infinitely many turns | `k = ∞` | infinite tail | — | — | **nothing** | **RESIDUAL** |

**Overlaps, stated because the brief asks.** These families are not disjoint:
bounded drift ⊂ log-floor at `B = 0`; periodic anchors ⊂ finite words; `D_L` ⊂
`F_2`; Mersenne seeds ⊂ `1^u q 1^v` with `(q,v)` determined by `u`. The table is
a status inventory, not a fine partition.

## 4. Coverage: what the `F_k` hierarchy actually contains

Measured over **all** odd `3 ≤ m_0 < 60001` at `c = 1`, every complete episode
before arrival at `1` (`scripts/coverage.py`, 7301 episodes of length `≥ 10`):

```
   mean k/ℓ over ℓ ≥ 10        =  0.4537
   max ℓ with k ≤ 2            =  15
   max ℓ with k ≤ 4            =  22
   of 7301 episodes with ℓ≥10, k ≤ 2 holds for 96 and k ≤ 4 for 971
```

and on the Loeb benchmark the seven episodes have `k = 7, 1, 3, 25, 0, 3, 1` —
the length-`64` episode sits in `F_25`.

> **Coverage verdict.** `k` is essentially **linear** in `ℓ` in the real
> population. A class `F_k` at fixed `k` therefore contains only episodes of
> **bounded length** (`≤ 15` for `k ≤ 2`, `≤ 22` for `k ≤ 4`), so no fixed-`k`
> theorem can reach long episodes, and the baseline `F(k) = Θ(α^{⌈(k+1)/2⌉})` is
> astronomically vacuous exactly where the population lives (at the Loeb seed's
> own `j = 28` ones-runs the bound reads `N ≤ 2.98×10^7`).

## 5. The residual, stated explicitly

> **Infinitely many internal direction changes, with positive-integer
> realization at every depth.**

Nothing in this package touches it. In particular:

* it is **not** assumed Sturmian, periodic, typical, or low-complexity — the
  measured `k/ℓ ≈ 0.45` is consistent with high symbolic complexity;
* by §1 this is the *only* surviving case for an actual positive orbit, and by
  Rev 8 Prop. 4.10 a divergent orbit is **one infinite episode** of exactly this
  type;
* a bound on the number of *completed* episodes is therefore silent on it, and so
  is every statement in §3 restricted to finite words or fixed `k`;
* Rev 8 **Proposition 9.1** blocks the obvious repair: every exact-realizer
  cylinder is nonempty and unbounded, so no property determined by finitely many
  2-adic digits can be equivalent to positivity.
