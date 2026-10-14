# RESTRICTED_THEOREM_ATTEMPT.md — the proof attempt, including what failed

The brief asks for one restricted deterministic theorem, chosen only after
comparing the candidate class against the existing periodic, bounded-drift,
Sturmian and finite-prefix-packing results, and with failed steps recorded.

---

## 1. Class selection, and why the others were rejected

| candidate class | verdict |
|---|---|
| low-complexity (Sturmian / mechanical) valuation words | **rejected — already covered.** Monks-Yazinski 2.7(b) subsumes the whole low-density ladder, and the author's own published work handles density `< beta`, `> beta` and `= beta` for Sturmian words. Nothing left at `N = 4`-style small complexity |
| periodic valuation patterns | **rejected — closed.** `BoundedDrift.evPeriodic_of_noninj`, `PeriodicCore`, `Periodic.lean` |
| bounded-drift mechanical words | **rejected — closed.** `BoundedDrift.lean` §1 of `PRIOR_DETERMINISTIC_BARRIERS.md`; statement **G** |
| returns with an explicit carry budget | **rejected as circular.** "Carry budget" is `E_N` bounded, i.e. `sum 1/m_k < infinity`, i.e. Curry's conclusion — assuming it assumes the divergence structure |
| suffix-realizer configurations | **rejected — reduces to a closed route.** This is the previous round's Theorem D two-set difference equation, barred by its Theorem E power-law barrier |
| **near-critical returns with controlled spacing** | **SELECTED.** Not covered: every existing barrier needs a drift floor at *every* prefix (`PRIOR_DETERMINISTIC_BARRIERS.md` §2), whereas controlled spacing constrains only a subsequence |

## 2. The theorem

> **Theorem S [P].** Let `m_0` be a positive odd integer, `w >= 0` and `G >= 1`.
> Suppose the accelerated orbit of `m_0` has **`(w,G)`-regular near-critical
> returns through depth `N`**: for every `n` with `0 <= n <= N-G` there exists
> `i in [n, n+G)` with `Delta_i <= w`. If the states `m_0, ..., m_{N-1}` are
> pairwise distinct, then
> ```
>     N^{8/9}  <=  3 e^{7/9} * m_0 * 2^w * G ,        3 e^{7/9} = 6.529890 .
> ```
> Consequently an orbit with `(w,G)`-regular returns is injective for at most
> ```
>     N_max = ( 3 e^{7/9} m_0 2^w G )^{9/8}
> ```
> steps; beyond that it repeats a state and is eventually periodic. **No
> divergent — in particular no permanently zero-confined — positive-integer
> orbit has `(w,G)`-regular near-critical returns for fixed `w` and `G`.**
>
> *Proof.* Regularity gives at least `floor(N/G)` indices `i < N` with
> `Delta_i <= w`. Theorem R of `CRITICAL_RETURN_CARRY.md` bounds that count by
> `3 e^{7/9} m_0 2^w N^{1/9}`. So `N/G <= 3 e^{7/9} m_0 2^w N^{1/9}`, which is
> the display. The last clause: if the orbit were injective for all `N` the
> display would fail for large `N`; a repeated state gives eventual periodicity
> by `BoundedDrift.evPeriodic_of_noninj`, and an eventually periodic orbit is
> not divergent. ∎

**It involves both `Delta_N` and the carry**, as the brief asks: the return
hypothesis is about `Delta`, and the bound comes through the carry identity
`sum_{i<N} 2^{-Delta_i} = 3 m_0 (2^{E_N} - 1)` plus harmonic packing of the
integer states. The seed `m_0` appears explicitly — it is an arithmetic bound,
not a probabilistic one.

**Verified** against real orbits at their maximal injective depth
(`scripts/theorem_s.py`): 14 rows, 0 violations of the inequality, e.g.
`m_0 = 626331` injective through `190` with 76 returns at `w = 0`, measured
maximal gap `111`, `N^{8/9} = 105.57 <= 4.54e8`. The caps are explicit:
`m_0 = 27` with `(w,G) = (0,1)` gives `N_max = 336.6`; with `(2,5)`,
`N_max = 9788.4`.

## 3. Honest scope — this is narrow, and it is a sibling of a known theorem

* Setting the return count to `N` (i.e. `G = 1`, `w = B log_2 N + C`) turns
  Theorem R into `N^{8/9-B} <= 3 e^{7/9} 2^C m_0`, which is **verbatim**
  `LogCorridor.logFloor_window_bound'`, constant included. **Theorem S is a
  counting wrapper around an existing repository theorem**, with the hypothesis
  weakened from "floor at every prefix" to "a return in every window of length
  `G`". That is the entire advance.
* `w` and `G` must be **fixed** (or grow slower than `log N` and `N^{8/9}`
  respectively). With `w(N) = B log_2 N`, `B >= 8/9`, the bound is vacuous. So
  Theorem S does **not** touch the log-width or sublinear-width regimes, which
  are the open ones.
* It is **not** a divergence-exclusion result. It excludes one *regularity
  pattern*, not divergence.

## 4. Failed steps, recorded

**(F1) Diophantine leverage from integrality of the carry — FAILED.** `q_N` is a
positive integer with `q_N/3^N -> L = m_0(2^{E_infty}-1)`, suggesting that `L`
is forced to be Diophantine-special. But
`3^N L - q_N = 3^{N-1} sum_{i >= N} 2^{-Delta_i}`, and with `Delta_i ~ sqrt(i)`
this is `~ 3^N 2^{-sqrt N} -> infinity`. There is **no small-fractional-part
phenomenon** and no approximation argument applies. Abandoned.

**(F2) Turning the Lopez-Stoll conclusion into a contradiction — FAILED, and
for an instructive reason.** Granting [2021] Lemmas 23-26 and using
`Phi_R(v) = m_0(1 - 2^{E_infty})`, the conclusion `Phi_R(v) notin Q_odd` becomes
`prod_k (1 + 1/(3 m_k)) notin Q_odd`. That is a genuine arithmetic restriction
but **not a contradiction**: `Phi(v) = m_0` is an integer and
`Phi_R(v) != Phi(v)`. Exactly the gap of `LOPEZ_STOLL_SOURCE_AUDIT.md` §3(6).

**(F3) A first version of Theorem S used `liminf Delta_N/N = 0` as the return
hypothesis — WITHDRAWN as circular and as insufficient.** Insufficient because
`liminf = 0` gives one subsequence with `Delta_{N_k} = o(N_k)`, and
`o(N_k)`-width returns make `2^{w}` superpolynomial, so Theorem R is vacuous.
Circular because the only available source for `liminf Delta_N/N = 0` was
[2021] Theorem 1, which fails audit. Replaced by the explicit `(w,G)` hypothesis,
which is checkable.

**(F4) Attempt to iterate Theorem R into a self-improving bound — FAILED.**
Theorem R's output (`few returns`) does not feed back into its input (`sum 1/m_k`
small), because the harmonic packing bound already uses all the distinctness
available; iterating reproduces the same inequality. Recorded so it is not
retried.
