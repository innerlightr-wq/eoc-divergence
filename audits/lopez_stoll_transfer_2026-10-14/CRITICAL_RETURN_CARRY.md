# CRITICAL_RETURN_CARRY.md — the carry bridge and a return-count theorem

The central section. It contains the one place where this investigation crosses
from aggregate to deterministic, and the exact extent of the crossing.

---

## 1. The bridge: Lopez-Stoll's real partial sums ARE the EOC carry

`Phi(2^{d_0}+2^{d_1}+...) = -sum_i 2^{d_i}/3^{i+1}` ([2009] eq. (2)) with the
`1`-positions of the parity vector at `d_i = S_i`. So

> **Theorem B1 [P].** `Phi_R(v) = -(1/3) sum_{i>=0} 2^{-Delta_i}`, where
> `2^{-Delta_i}` denotes the **exact rational** `2^{S_i}/3^i`. At the
> accelerated endpoint `l = S_N`, `h = N`,
> ```
>    Phi_R(u^{(S_N)})  =  - sum_{i<N} 2^{S_i}/3^{i+1}  =  - q_N / 3^N ,
> ```
> where `q_N` is the **EOC carry**, `q_0 = 0`, `q_{j+1} = 3 q_j + 2^{S_j}`, whose
> closed form `q_N = sum_{i<N} 3^{N-1-i} 2^{S_i}` is `Carry.lean`'s `q_eq_C`
> **[PRIOR]**.

So the real-valued object whose devil's-staircase behaviour [2009] §4 studies is
literally the normalized EOC carry `q_N/3^N`. This identification appears to be
new; the two ingredients are not.

> **Theorem B2 (master identity) [P; the identity itself is PRIOR].** For every
> odd `m_0` and every ordinary prefix length `l` with height `h`,
> ```
>    Phi_R(u^{(l)})  =  m_0  -  (2^l / 3^h) T^l(m_0)        [exact over Q] ,
> ```
> and at accelerated endpoints, using `2^{S_N} m_N = 3^N m_0 + q_N`,
> ```
>    sum_{i<N} 2^{-Delta_i}  =  3 ( 2^{-Delta_N} m_N - m_0 )  =  3 m_0 ( 2^{E_N} - 1 ) ,
>    E_N = sum_{k<N} log_2(1 + 1/(3 m_k)) ,   2^{E_N} = prod_{k<N}(1 + 1/(3 m_k)) .
> ```
> The drift identity `log_2(m_N/m_0) = alpha N - S_N + E_N` and the carry
> identity are **[PRIOR]** (`HarmonicPacking.lean` defines `carryU`, `carryE`;
> the identity is the manuscript's and Eliahou-Rozier's, **not new**).

**Verified exactly, 0 violations:** `scripts/phi_identity.py` (`l = 0..60`, nine
seeds) and `scripts/carry_bridge.py` (four identities, `N = 1..40`, eight seeds
including `27, 703, 10087, 35655, 381727`). The three expressions for
`sum 2^{-Delta_i}` agree to every printed digit along real orbits.

> **Corollary B3 [P].** The following are **equivalent** for a positive odd seed:
> ```
>   (i)  Phi_R(v) converges in R ;
>   (ii) q_N/3^N converges ;
>   (iii) sum_{i>=0} 2^{-Delta_i} < infinity ;
>   (iv) sum_{k>=0} 1/m_k < infinity   (equivalently E_N bounded) .
> ```
> and then `Phi_R(v) = m_0(1 - 2^{E_infty})`, while `Phi(v) = m_0`. The two
> differ by exactly `m_0 2^{E_infty}` — this is the discrepancy that defeats
> [2021]'s real-to-2-adic step (`LOPEZ_STOLL_SOURCE_AUDIT.md` §3(6)).

**Where this lands.** `(iv)` is **Curry (2026) Proposition 3.1** for divergent
orbits (`PRIOR_DETERMINISTIC_BARRIERS.md` §2), so for a hypothetical divergent
positive integer all four hold. Equivalence `(iii) <=> (iv)` is also exactly
EOC's reciprocal-summability object; it is **not** a new open problem and **not**
a new theorem — it is the same object in three coordinate systems.

## 2. The deficit sum is a return counter — Theorem R

This is the new step, and it is one line.

> **Theorem R [P].** Let `m_0` be odd with `m_0, ..., m_{N-1}` pairwise distinct.
> Then for every `w >= 0`,
> ```
>    #{ i < N : Delta_i <= w }   <=   2^w  sum_{i<N} 2^{-Delta_i}
>                                =   3 m_0 2^w ( 2^{E_N} - 1 )
>                                <=   3 e^{7/9} m_0 2^w N^{1/9} .
> ```
>
> *Proof.* If `Delta_i <= w` then `2^{-Delta_i} >= 2^{-w}`, so the count is at
> most `2^w` times the full sum; the sum is evaluated by Theorem B2. For the last
> step, `sum_inv_orbit_le` (`EOC/HarmonicPacking.lean`, **[PRIOR]**) gives
> `sum_{k<N} 1/m_k <= 7/3 + (1/3) log N` under exactly this distinctness
> hypothesis, so
> `E_N <= (1/(3 ln 2)) sum_k 1/m_k <= 7/(9 ln 2) + (1/(9 ln 2)) log N`
> and `2^{E_N} <= e^{7/9} N^{1/9}`. ∎

`3 e^{7/9} = 6.529890`.

> **Corollary R1 [P + external].** Along a **divergent** orbit, Curry's
> `sum_k 1/m_k < infinity` gives `E_N <= E_infty < infinity`, hence for every
> fixed `w`
> ```
>    #{ i >= 0 : Delta_i <= w }  <=  3 m_0 2^w ( 2^{E_infty} - 1 )  <  infinity .
> ```
> **A divergent positive-integer orbit enters any fixed-width near-critical band
> only finitely often.** (External dependency: Curry 2026, source-reported via
> `eoc-lean-verification/README.md`; not read in this session.)

**Verified, 0 violations**, on nine seeds at their maximal injective depth
(`scripts/return_count.py`): e.g. `m_0 = 626331`, injective through `190`,
`sum_{i<189} 2^{-Delta_i} = 257850.57 = 3 m_0 (2^{E_189}-1)` exactly, bound
`7.32e6`; return counts `#{Delta_i <= 0} = 76`, `<= 1: 84`, `<= 2: 92` against
the `w = 2` bound `1.03e6`.

**The injectivity hypothesis is load-bearing, and the control shows it.** Pushed
past the injective depth the bound fails by orders of magnitude: `m_0 = 27`
injective through `42`, and at `N = 82` the sum is `1.29e7` against a bound of
`288`.

## 3. Exactly how new Theorem R is — and it is a sibling, not an orphan

Put the count equal to `N` and `w = B log_2 N + C`. Theorem R becomes
`N <= 3 e^{7/9} m_0 2^C N^B N^{1/9}`, i.e.

```
   N^{8/9 - B}  <=  3 e^{7/9} 2^C m_0 ,
```

which is **verbatim** `LogCorridor.logFloor_window_bound'`
(`N^(8/9 - B) <= 3 e^(7/9) * 2^C * M`), **including the constant `3 e^{7/9}`.**

> So Theorem R is a **counting generalization of an existing repository theorem,
> by the same pigeonhole and with the same constant.** What is new is only the
> weakening of the hypothesis: `logFloor_window_bound'` needs the drift floor at
> **every** `k < N`; Theorem R needs nothing, and bounds the **number** of
> indices that return. That is exactly the gap the brief's §6 asks about
> ("returns" versus "floors"), and it is the honest extent of the advance.

**It does not reach past the logarithmic barrier.** `sum_i 2^{-Delta_i} < infinity`
fails for `Delta_i <= B log_2 i` with `B <= 1` (the sum dominates `sum i^{-B}`),
so Corollary R1 re-derives the **harmonic** barrier `B = 1` — weaker than the
repository's unconditional `8/9` combined with Curry's `1/beta* = 1.0358567`.
**No new logarithmic obstruction is claimed; the known one is recovered.**

## 4. Which return regimes remain open

From `TWO_CLOCK_TRANSLATION.md` §2 and §§2-3 above, for a hypothetical
permanently zero-confined positive integer:

| regime | status |
|---|---|
| `Delta_N` bounded (**G**) | **EXCLUDED** [PRIOR] — bounded drift (`BoundedDrift.lean`) |
| `Delta_N = O(log N)` (**F**), coefficient `< 8/9` | **EXCLUDED** [PRIOR, unconditional] |
| **F** with coefficient `< 1.0358567` | **EXCLUDED** [PRIOR + Curry, external] |
| constant-width returns, infinitely often | **EXCLUDED** [P, Corollary R1 + Curry]; unconditionally at most `O(m_0 N^{1/9})` up to depth `N` [P, Theorem R] |
| logarithmic-width returns `w(N) = B log_2 N`, i.o. | **OPEN.** Theorem R gives only `#returns <= 3e^{7/9} m_0 N^{B+1/9}`, vacuous once `B >= 8/9` |
| sublinear-width returns `w(N) = N^{1/2}`, i.o. | **OPEN**, and Theorem R is vacuous there (`2^w` swamps `N^{1/9}`) |
| `Delta_N/N -> 0` along a subsequence (**D**) | **OPEN**; and **not** forced — W1 of `TWO_CLOCK_TRANSLATION.md` is a confined word violating it, and [2021]'s claim that it is forced does not survive audit |

**So the regime left open is exactly the one the mass concentration points at**
(`MASS_CONCENTRATION.md` §3: under the conditioned measure the typical deficit
is `o(N)`), and it is where every tool here is vacuous.

## 5. What the carry does NOT give — two recorded dead ends

**(a) No Diophantine leverage from integrality of `q_N`.** `q_N` is a positive
integer and `q_N/3^N -> L := m_0(2^{E_infty}-1)`, so one might hope
`3^N L - q_N` small forces `L` special. But
`3^N L - q_N = 3^{N-1} sum_{i>=N} 2^{-Delta_i}`, and with `Delta_i ~ sqrt(i)`
this is `~ 3^N 2^{-sqrt N} -> infinity`. **There is no small-fractional-part
phenomenon**, so no Diophantine approximation argument applies. Recorded as a
dead end, not as an obstruction in principle.

**(b) The LS conclusion, even granting its lemmas, is only an irrationality
statement.** With `Phi_R(v) = m_0(1-2^{E_infty})`, [2021] Lemmas 24-26 would
give `m_0 2^{E_infty} notin Q_odd`, i.e. `prod_k (1 + 1/(3 m_k))` is not an
odd-denominator rational. That is a genuine arithmetic restriction on a
divergent orbit — **and it is not a contradiction**, which is why branch 1 needs
the invalid transfer step to reach its stated conclusion.
