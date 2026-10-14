# THEOREM_LEDGER.md

Labels as the brief prescribes: **[P]** proved here · **[PRIOR]** earlier EOC or
external literature · **[V]** verified by exact finite computation, with range ·
**[F]** numerical/floating diagnostic · **[C]** conditional or missing ·
**[R]** refuted or blocked.

---

## 1. [P] Proved in this investigation

| # | statement | where | uniform / pointwise |
|---|---|---|---|
| **C1** | within a block `h(l)/l` decreases, so `liminf_l h/l = liminf_N N/S_N = 1/limsup_N(S_N/N)` | `TWO_CLOCK_TRANSLATION.md` §1 | exact identity |
| **C2** | `liminf_l h/l = 1/(alpha - liminf_N Delta_N/N)`; under confinement `= beta` iff `liminf Delta_N/N = 0` | §1 | exact |
| **C3** | under confinement, `lim_l h/l = beta  <=>  Delta_N = o(N)` | §1 | exact |
| lattice | `A=>B`, `C<=>D`, `E=>D`, `F=>E`, `G=>F`; **all other implications among A..G are false** | §2 | with witnesses |
| **M3** | `P[S_N <= sN] = 2^{-N J(s)+o(N)}`, `J(s)=s(1-H_2(1/s))` | `MASS_CONCENTRATION.md` §2 | fixed `s in (1,2)` |
| **M4** | `P[S_N <= (alpha-eps)N | C_N] <= 2^{-N[J(alpha-eps)-I_0]+o(N)}`, exponent `> 0` | §3 | **fixed** `eps`, `alpha-eps>1`; average, **not pathwise** |
| **U2** | explicit moving-band form with prefactor `c_1 N^2` | `MOVING_CORRIDOR.md` §2 | all `0<eps<=alpha-1` |
| **U3** | U2 is non-vacuous exactly for `eps_N >> log N/N`; `kappa = -J'(alpha) = 0.438032659` | §2 | — |
| **B1** | `Phi_R(v) = -(1/3) sum_i 2^{-Delta_i}`; `Phi_R(u^{(S_N)}) = -q_N/3^N` — **LS's real partial sums are the EOC carry** | `CRITICAL_RETURN_CARRY.md` §1 | exact |
| **B2** | master identity `Phi_R(u^{(l)}) = m_0 - (2^l/3^h)T^l(m_0)`; hence `sum_{i<N}2^{-Delta_i} = 3m_0(2^{E_N}-1)` | §1 | exact over `Q` |
| **B3** | `Phi_R(v)` converges `<=>` `q_N/3^N` converges `<=>` `sum 2^{-Delta_i}<inf` `<=>` `sum 1/m_k<inf`; and `Phi_R(v)=m_0(1-2^{E_inf})` while `Phi(v)=m_0` | §1 | pointwise, per seed |
| **R** | `#{i<N : Delta_i <= w} <= 3 m_0 2^w(2^{E_N}-1) <= 3e^{7/9} m_0 2^w N^{1/9}` | §2 | needs `Odd m_0` + distinct states on `[0,N)`; **pointwise** |
| **R1** | along a divergent orbit, `#{i : Delta_i <= w} < infinity` for each fixed `w` | §2 | uses Curry (external) |
| **S** | `(w,G)`-regular near-critical returns force `N^{8/9} <= 3e^{7/9} m_0 2^w G`; no divergent orbit has them for fixed `w,G` | `RESTRICTED_THEOREM_ATTEMPT.md` §2 | **pointwise**, arithmetic |
| **X1** | the number of leading `d_j=1` is exactly `v_2(m_0+1)-1` | `COUNTEREXAMPLES.md` §2 | exact |
| **X2** | every admissible word has exactly one least realizer residue, for every `N` | §4 | exact |

**Scope notes carried on the proofs.** M3 is a lower-order-sharp Stirling
argument, not a sharp-constant theorem. M5 (`MASS_CONCENTRATION.md` §5) has a
**proved upper bound and a sketched lower bound**, labelled as such. B2's
*identity* is `PRIOR` (it is the carry identity); what is `[P]` is its
identification with LS's `Phi_R` and its use as a return counter.

## 2. [PRIOR] Source-backed

| statement | source | note |
|---|---|---|
| `confined_mass_rate (c)`: `-(1/N)log_2 p(N,c) -> I_0 = 0.079318612775` | `eoc-divergence@938dcc0` `Occupation/Rate.lean:478` | **fixed `c`**, no uniformity in `c` |
| `p N c = sum_{confined} 2^{-S_N}`; `Confined c d <-> ∀j<=N, 2^{S_j} <= 2^c 3^j` | `Occupation/Compositions.lean:217` | integral form used throughout |
| `le_p`, `p_le` sandwich `tt/N <= p <= (sN+1)tt` | `Occupation/Rate.lean` | **[V]** 0 violations, `N=4..96` |
| `realizerCongruence`, `leastRealizer_unique`, `residue_pinning` | `eoc-lean-verification@6057a0d` `EOC/Realizer.lean:286,478,543` | modulus `2^{S_N+1}` |
| carry identity / closed form `q_N = sum 3^{N-1-i}2^{S_i}` | `Carry.lean` `q_eq_C` | **[V]** here |
| drift identity `log_2(m_N/m_0) = alpha N - S_N + E_N`; `carryU`, `carryE` | `HarmonicPacking.lean` | manuscript's / Eliahou-Rozier; **not new** |
| `sum_inv_orbit_le`: distinct states `=> sum_{k<N}1/m_k <= 7/3 + (1/3)log N` | `HarmonicPacking.lean` | the pigeonhole behind R and S |
| bounded-drift exclusion (Cases A, B; realizer escape) | `BoundedDrift.lean` | closes **G** arithmetically |
| finite-prefix drift-depth bound, coefficient `2-log_2 3 = 0.4150374993` | `FinitePrefixPacking.lean` | needs floor at **every** prefix |
| `logFloor_window_bound'`: `N^{8/9-B} <= 3e^{7/9} 2^C M` | `LogCorridor.lean` | **Theorem R reduces to this** when the count is `N` |
| `exits_logCorridor`: no log corridor for `B<8/9` unconditionally | `LogCorridor.lean` | |
| `R_le_of_nondescent_harmonic` | `HarmonicFloor.lean` | coefficient `1/9` |
| [2009] Theorem 1 / Corollary 2 (2-adic CF expansion), devil's staircase | Lopez-Stoll, INTEGERS 9 (2009) 141-162 | **refereed** |
| Monks-Yazinski (2004) Thm 2.7 b; Lagarias Relation 2.31 | quoted by [2021] | **source-reported, not read here** |
| Garcia-Tal (1999); Curry (2026) Thm 2.3, Prop 3.1 (`sum 1/m_n<inf`), Thms 4.1-4.3 (`B<1/beta* = 1.0358567`) | `eoc-lean-verification/README.md` | **source-reported, not read here**; enters Lean only as the `Prop` `LogFloorExclusion` |

> **No claim of Lean verification.** No `lake build`, no toolchain invocation, no
> dependency audit in this session. Every Lean entry is "source-backed" by
> reading the file.

## 3. [V] Exact finite computation

| check | range | result | script |
|---|---|---|---|
| master identity `Phi_R(u^{(l)}) = m_0 - (2^l/3^h)T^l(m_0)` | `l = 0..60`, 9 seeds | **0 violations** | `phi_identity.py` |
| four carry identities (recurrence = closed form; `Phi_R = -q_N/3^N`; `2^{S_N}m_N = 3^N m_0+q_N`; `sum 2^{-D_i} = 3(2^{-D_N}m_N-m_0)`) | `N=1..40`, 8 seeds | **0 violations** | `carry_bridge.py` |
| three expressions for `sum 2^{-Delta_i}` agree | `N=10,30,60`, 5 seeds | all digits | `carry_bridge.py` |
| Theorem R | 9 seeds at maximal injective depth | **0 violations** | `return_count.py` |
| Theorem R control: drop injectivity | `m_0=27,703` past injective depth | **bound fails** (1.29e7 vs 288) — hypothesis is load-bearing | `return_count.py` |
| Theorem S inequality | 14 rows, 7 seeds, `w=0,2` | **0 violations** | `theorem_s.py` |
| Lean sandwich `tt/N <= p <= (sN+1)tt` | `N=4,8,...,96` | **0 violations** | `clocks_and_rate.py` |
| `J(s)` rate | 7 values of `s`, `N=50..1000` | monotone convergence | `clocks_and_rate.py` |
| two-clock identity C1 | 4 words | exact agreement | `counterexamples.py` |
| 0-confinement of W1-W4 | `N` up to 6000 | exact, by integer comparison | `counterexamples.py` |
| X1 (`v_2(m_0+1)-1`) | 15 seeds | **0 violations** after correction | `realizability.py` |
| X2 (least realizer reproduces the word) | 7 words | **0 violations** | `realizability.py` |

## 4. [F] Floating diagnostics only

`Delta_N`, `liminf/limsup Delta_N/N`, `Delta_N/log_2 N`, the `J`-tables and
`kappa`. **Every confinement and congruence decision is exact integer
arithmetic**; floats appear only in printed summaries.

## 5. [C] Conditional or missing

| item | status |
|---|---|
| Curry (2026) `sum_n 1/m_n < infinity` | external, source-reported; **Corollary R1 depends on it** |
| Monks-Yazinski 2.7 b | external, source-reported; underlies the only surviving LS branch |
| lower bound in M5 (`p(N,theta N)` rate) | **sketch**, numerically confirmed |
| moderate-deviation estimate in `log N << Delta_N << N` | **not derived**; the regime has no estimate here |
| `Delta_N = o(N)` (**E**) or `liminf Delta_N/N = 0` (**D**) for a divergent orbit | **OPEN, and not forced** |
| log-width and sublinear-width returns i.o. | **OPEN**; all tools here vacuous |

## 6. [R] Refuted or blocked in this session

| item | status |
|---|---|
| [2021] Theorem 1's step `Phi_R(v) notin Q_odd ==> Phi(v) notin Q_odd` | **REFUTED as a valid step.** `Phi(v)=m_0` while `Phi_R(v)=m_0(1-2^{E_inf})`; they differ by exactly `m_0 2^{E_inf}` (verified). The theorem may still be true; **its proof as written does not establish it** |
| [2021] Theorem 1's trichotomy (existence of `lim h/l`) | **unjustified**; correct form is about `liminf` |
| "LS strengthens the restriction on a confined positive integer" | **REFUTED.** After audit it adds nothing beyond `B`, which `A` already gives |
| Diophantine leverage from integrality of `q_N` | **BLOCKED**: `3^N L - q_N = 3^{N-1} sum_{i>=N}2^{-Delta_i} -> infinity` |
| Theorem R past the logarithmic barrier | **BLOCKED**: it re-derives the harmonic `B=1`, weaker than the known `8/9` + `1.0358567` |
| iterating Theorem R into a self-improving bound | **BLOCKED**: reproduces the same inequality |
| first version of Theorem S using `liminf Delta_N/N=0` | **WITHDRAWN**: circular (source was [2021]) and insufficient (`2^{o(N)}` swamps `N^{1/9}`) |
| my own X1 as first stated (`v_2(m_0+1)`) | **off by one, corrected** to `v_2(m_0+1)-1` by the exact check |
| my own `kappa = 1.3195` in the moving-corridor draft | **wrong, corrected** to `0.438032659` via the closed form `J'(s)=1+log_2((s-1)/s)` |
