# RUN_ARITHMETIC.md — the elementary baseline, then the actual proof attempt

Labels: **[PRIOR]** · **[E]** elementary derived consequence · **[P]** new proved
estimate · **[V]** exact finite check · **[R]** refuted.

---

## 1. Lemma A — the 2-adic characterisation of direction **[E]**

> **Lemma A.** For odd `m`, write `e(m) = v_2(m+1) ≥ 1`. Then
> ```
>    d = v_2(3m+1) = 1   ⟺   e(m) ≥ 2 ,          d ≥ 2   ⟺   e(m) = 1 ,
> ```
> and a `d = 1` step sends `e ↦ e − 1` exactly. Consequently the **maximal**
> `d = 1` run starting at `x` has length exactly
> ```
>    u_max(x) = v_2(x+1) − 1 .
> ```
>
> *Proof.* Put `t = m+1 = 2^e s`, `s` odd. Then `3m+1 = 3t − 2 = 2(3·2^{e−1}s − 1)`.
> If `e = 1` the inner factor is `3s − 1`, even, so `d ≥ 2`. If `e ≥ 2` it is
> `3·2^{e−1}s − 1`, odd, so `d = 1` exactly. Under a `d = 1` step
> `m+1 ↦ 3(m+1)/2`, and `3` is odd, so `e ↦ e − 1`. The run continues while
> `e ≥ 2` and stops when `e = 1`, i.e. after exactly `e(x) − 1` steps. ∎

**[V]** All odd `3 ≤ m_0 ≤ 60001`, `n < 12`: **0 violations** of either
equivalence, of the decrement, or of `u_max = v_2(x+1) − 1`.

This is the engine of everything below: **the ones-run length is a 2-adic
resource, consumed one unit per step, and a `d ≥ 2` step regenerates it to an a
priori unbounded new value.** There is no conservation law, which is why the
baseline of §3 compounds.

## 2. Lemma B — the two run estimates **[E, standard]**

> **(a)** `u` consecutive `d = 1` steps from `x` give, **exactly**,
> `y + 1 = 3^u(x+1)/2^u`; realizability forces `2^{u+1} | x+1` for a maximal run
> (Lemma A), hence `x ≥ 2^{u+1} − 1`.
> **(b)** `v` consecutive `d ≥ 2` steps with all states `> 1` give
> `y − 1 ≤ (3/4)^v (x−1)`, since one step gives `y ≤ (3x+1)/4` and so
> `y − 1 ≤ (3/4)(x−1)`. At `x = 1` the step is `d = 2`, `y = 1`, and the
> contraction stalls with equality.

**[V]** `0` violations of (a) on every maximal leading ones-run and of (b) on
every maximal twos-run with states `> 1`, over all odd `3 ≤ m_0 ≤ 40001`.

**This is standard run arithmetic and is not claimed as new.**

## 3. Theorem C — the chained fixed-turn lifetime bound **[P, but a baseline]**

Write `h = log_2(m+1)`, `φ = log_2(3/2) = α − 1`, `ψ = log_2(4/3) = 2 − α`, so
`φ + ψ = 1` and `1 + φ = α`. A ones-run of length `u` sends `h ↦ h + uφ`
**exactly**; a twos-run of length `v` sends `h ↦ h'` with `h' ≤ h − vψ + 1`,
using `m−1 ≤ m+1 ≤ 2(m−1)` for `m ≥ 3`.

With `u_i ≤ h_i − 1` (Lemma A) and `v_i ≥ 1`,

```
   h_{i+1} ≤ h_i + (h_i − 1)φ − ψ + 1 = α h_i ,
```

so `h_i ≤ α^{i−1}L` with `L = log_2(m_0+1)`, and over `j` ones-runs
`Σu_i ≤ L(α^j − 1)/(α−1) − j`. Staying above `m = 1` forces
`(Σv_i)ψ ≤ L + (Σu_i)φ + j' − 1`, and `1 + φ/ψ = 1/ψ` gives

> **Theorem C.** Let `m_0 ≥ 3` be odd, and let the first `N` accelerated steps
> have `j` maximal `d=1` runs, `j'` maximal `d≥2` runs, and all states `> 1`.
> Then
> ```
>    N  ≤  (1/(2−α)) [ Σu_i + L + j' − 1 ]  ≤  (L/(2−α))·(α^j + α − 2)/(α−1) .
> ```
> With at most `k` direction changes, `j ≤ ⌈(k+1)/2⌉`, so
> ```
>    N ≤ F(k)·log_2(m_0+1) ,     F(k) = Θ( α^{⌈(k+1)/2⌉} ) .
> ```
> **No corridor hypothesis is used.**

**Correction to the brief's candidate.** The brief proposed
`F(k) = O((k+1)α^{k+1})`. That overshoots: **only the ones-runs compound**, and
there are about `k/2` of them, so the truth is `Θ(α^{⌈(k+1)/2⌉})` — smaller by a
factor about `(k+1)α^{(k+1)/2}`. Explicit coefficients of `L`:
`4.818842` (`j=1`), `8.637683` (`j=2`), `14.690404` (`j=3`), `39.488817` (`j=5`).

**[V]** Holds on 11 real seeds up to arrival at `1`, with the actual `j`:
`0` failures. *An earlier version of this panel compared `N` against the `j = 1`
bound for Mersenne seeds and reported three failures; those seeds have `j > 1`
(e.g. `m_0 = 2^{21}−1` has `j = 24`), so the test was mis-specified, not the
theorem. Corrected.*

> **Corollary C1 [E].** Inverting Theorem C, a prefix of length `N` with all
> states `> 1` needs `α^j ≥ N(2−α)(α−1)/L − α + 2`, so the number of direction
> changes grows at least like
> ```
>    k ≥ 2j − 1 ≳ (2/log_2 α)·log_2(N/L) = 3.0100·log_2(N/L) .
> ```
> **This is not divergence exclusion.** It says only that turn counts must grow
> logarithmically; the measured growth is *linear* (`k/ℓ ≈ 0.45`), far above the
> forced floor.

**Per the brief: proving `O_k(log m_0)` for fixed `k` is the baseline, not the
advance.** Theorem C is recorded as that baseline.

## 4. The `D_L` family — verified, and it refutes my own prior proposal **[V, R]**

> `D_L = (3, 1^L, L+2)`, `c = 1`, `L ≥ 1`.

Independently derived here and checked by the exact realizer congruence **and**
direct orbit iteration at `L = 1,2,3,5,8,12,16` — **0 failures** on every
predicted item:

```
   episodes = [0,1) ∪ [2, L+2) ,   the later episode has ℓ = L
   R_n = 2 − (α−1)n   for 1 ≤ n ≤ L+1 ,        R_{L+2} = 1 + (2−α)(L+2) > 1
   w_max = (α−1)(L+1) − 1                       (exact, matched to 6 d.p.)
   W_L  = Σ_{n∈I} 2^{R_n} = (16/3)(1 − (2/3)^L) < 16/3   (exact as a rational)
   seed: 2^{L+4} | m_0 + 3 ,  so  m_0 ≥ 2^{L+4} − 3 ;  least r = 221, 573, 1405,
         50685, 3772413, 516489213, 13145997309 at L = 1,2,3,5,8,12,16
```

*Time zero counts (Rev 8 Def. 6.1), so `[0,1)` is a genuine initial episode and
the prediction concerns the later one. An earlier version of this check demanded
`episodes = [(2,L+2)]` and compared `w_max`/`W_L` over all episodes, producing
seven spurious failures; corrected.*

**Classification:** long (`ℓ = L`), **linearly deep** (`w_max ≈ 0.585L`),
**carry-cheap** (`W_L < 16/3` uniformly), **seed-expensive**
(`log_2 m_0 ≥ L + 4 − o(1)`).

> **Consequence [R].** A seed-independent bound `w_max ≤ K log_2 ℓ + C` is
> **FALSE** for complete finite positive-orbit episodes. This **refutes the
> (DEPTH–DURATION) lemma I proposed at the end of the previous round**
> (`audits/joint_episode_budget_2026-10-14/VERDICT.md` §6). The cost does not
> vanish — it moves into the seed, linearly in the depth.
>
> **It does not refute the statement restricted to globally divergent orbits**:
> every `D_L` seed reaches `1`, so by Rev 8 Lemma 4.2 its drift tends to `+∞`.
> And it does not refute EOC.

## 5. Theorem D — the main attempt, and its negative answer **[P]**

Class: `1^u q 1^v` with `q ≥ 2` and **both ones-runs maximal**.

Let `x` be the entry state, so by Lemma A `x + 1 = 2^{u+1}A` with `A` odd. Then,
exactly:

```
   after u ones-steps:   x_1 + 1 = 2·3^u A ,          so  e(x_1) = 1 ,
   the next valuation:   q = 1 + v_2(Z − 1) ,         Z := 3^{u+1}A  (odd) ,
   the next state:       x_2 = M ,  where  Z − 1 = 2^{q−1}M ,  M odd ,
   the next ones-run:    v = v_2(M + 1) − 1 .
```

> **Theorem D.** The word begins `1^u q 1^v` with both runs maximal **iff**
> ```
>    Z ≡ 1 − 2^{q−1}  (mod 2^{q+v})   and   Z ≢ 1 − 2^{q−1}  (mod 2^{q+v+1}) ,
> ```
> i.e. iff `A` lies in the single residue class
> ```
>    A ≡ 3^{−(u+1)}(1 − 2^{q−1})   (mod 2^{q+v}) ,
> ```
> with that one exactness condition. Hence the realizing set is
> `{ x : x+1 = 2^{u+1}A, A odd, A in that class }`, the least realizer is
> ```
>    r + 1 = 2^{u+1}·A_min(u,q,v) ,       A_min < 2^{q+v+1} ,
> ```
> and therefore
> ```
>    2^{u+1} − 1  ≤  r(1^u q 1^v)  <  2^{u+q+v+2} .
> ```
> The floor is attained **iff** `A_min = 1`, i.e. iff `3^{u+1} ≡ 1 − 2^{q−1}`
> mod `2^{q+v}`, i.e. iff `x = 2^{u+1} − 1` — the Mersenne seeds, for which `q`
> and `v` are **determined** by `u` and are not free parameters.
>
> *Proof.* The four displayed identities are Lemma A applied twice with the
> single intervening step, computed above. `v_2(M+1) = v+1` with
> `Z − 1 = 2^{q−1}M` is equivalent to `Z − 1 ≡ −2^{q−1}` mod `2^{q+v}` together
> with the non-congruence mod `2^{q+v+1}`; and `v_2(Z−1) = q−1` is then
> automatic because `q − 1 < q + v`. Since `3` is invertible mod `2^{q+v}`, this
> is one class for `A`. The bounds follow from `1 ≤ A_min < 2^{q+v+1}` (the
> exactness condition removes at most one of the two candidates
> `a_0, a_0 + 2^{q+v}`). ∎

**[V]** Verified on **60** triples `(u,q,v)`, `u ∈ {1,2,3,5,8}`,
`q ∈ {2,3,4}`, `v ∈ {1,2,3,5}`: the predicted `x = 2^{u+1}A_min − 1` reproduces
the word with both runs maximal **and equals the brute-force minimum in every
case** — `0` failures. *An earlier version of the brute force omitted the
trailing `d ≥ 2` test, so seeds whose second run is longer than `v` passed
spuriously (e.g. `x = 27` for `(1,2,1)`, whose second run is actually `v = 4`),
producing 28 reported failures. The test was mis-specified, not the theorem.*

### What Theorem D answers

> **The two growth runs do NOT force a combined cost greater than charging each
> run separately.** The minimum seed **factors**:
> ```
>    r + 1  =  (first-run 2-adic cost)  ×  (second-run congruence cost)
>           =  2^{u+1}  ×  A_min ,          A_min < 2^{q+v+1} ,
> ```
> with **no cross term**. The first run contributes a power of `2`; the second
> contributes a residue class modulo a power of `2`; and the interaction is
> exactly the invertibility of `3` modulo that power. There is no extra
> arithmetic obstruction to be had.

This is the negative answer to the brief's primary question for this class, and
it is proved rather than observed.

### What integrality supplies, and what it does not

Control E runs the **same prescribed word** over positive reals,
`x ↦ (3x+1)/2^{d_n}`, from `x_0 ∈ {285175, 1/7, 10^9}`: the `R`-profile, the
episodes, `k`, the run structure, `w_max` and `W` are **identical** for every
real `x_0 > 0`, because they are functions of the word alone. So a positive-real
trajectory has **no minimum-seed cost at all**, and everything in Theorem D —
the divisibility `2^{u+1} | x+1` and the residue class mod `2^{q+v}` — comes
from **integrality alone**. That is the precise content of "what integrality
supplies": two independent 2-adic conditions, which multiply.

### General `B`: why the dimension grows

For `1^u B 1^v` with `B = (q_1,…,q_b)` a maximal twos-run, the same computation
telescopes and the condition remains a single class for `A`, now modulo
`2^{Σq_i + v}`, giving
`2^{u+1} − 1 ≤ r < 2^{u + Σq_i + v + 2}`. But the **parameter count grows with
`b`**: the `q_i` are `b` independent valuations, not one. Per the brief, no
fixed-dimensional Diophantine input may be invoked — the state dimension is not
bounded. This is recorded, not exploited.
