# Closed Pointwise Routes — October 2026 additions

**Compiled 2026-10-14.** Three further audited negative results for the pointwise
problem, continuing [`CLOSED_POINTWISE_ROUTES_2026-09-29.md`](CLOSED_POINTWISE_ROUTES_2026-09-29.md).
Same discipline, repeated here because it is the point of the document: each
entry says *this specific route, under the hypotheses currently proved in this
programme, does not yield a pointwise separator*, and gives the exact
obstruction. **No entry claims that no conceivable variant of the idea can ever
work**, and none of this bears on the Collatz conjecture, on `(DE)`, or on
`(PosPC)`, all of which remain exactly as open as before.

Repository states audited: this repository at `ec581e6`
(`origin/main` when these audits were written), `eoc-lean-verification` at
`6057a0d`, and the Revision 8 manuscript on that repository's `eoc-revision8`
branch at `b2dcae2`.

**Novelty discipline.** Where a conclusion was already on record it is credited,
and in one case (§3) the principal obstruction had already been established in an
earlier unpublished round, which is stated in the entry rather than discovered by
the reader.

---

## 1. Arithmetic amplification from the percolation method

Full package: [`audits/amplification_transfer_2026-10-14/`](../audits/amplification_transfer_2026-10-14/).

**Scope.** Whether the amplification and joint inverse-reconstruction method of a
September 2026 percolation preprint can show that one permanently zero-confined
positive odd integer forces an arithmetic amplification contradicting
`Occupation.confined_mass_rate`.

**The criterion is vacuous.** Writing `C_N` for the `0`-confined-to-depth-`N` odd
residue classes mod `Q_N = 2^{⌊N log₂3⌋+1}` and `μ` for normalized counting
measure on odd residues, `μ(C_N) = p(N,0)` **exactly** — the symbolic-mass ↔
residue-density bridge is an identity, verified by brute force over every odd
residue for `N ≤ 14`, 0 violations. Hence any family of pairwise distinct confined
classes has `μ ≤ 2^{−I₀N+o(N)}`, so the demand `μ(B_N) ≥ c·2^{−εN}` with
`ε < I₀` asks for **more confined classes than exist**. It is unsatisfiable for
every seed, persistent or not, so the implication is vacuously true and
decomposes nothing.

> **No injection into the confined population can amplify its mass** — not
> permutations, not lifts, not any map. `confined_mass_rate` is the accounting of
> a conserved budget, and anything one seed generates is a subpopulation of its
> own parent.

**Three further independent obstructions.** (i) *No multiplicity to delete* — the
percolation Lemma 4.8 exists to remove an inverse-code factor `W^{2k}`, but
`word ↔ least-realizer class` is a **bijection** (`EOC/Realizer.lean`
`leastRealizer_unique`, `residue_pinning`; max fibre `= 1` for `N ≤ 14`), so the
inverse is a division and the technique has nothing to save. (ii) *Index surplus
and fibre cost are the same number* — `#I_N ≤ n_N·max fibre` for any map into
`C_N`, so the two halves of a multiplicity criterion are bounds on one quantity.
(iii) *No spectral seed* — the construction needs `‖K‖ < e^{−1}` from
nonamenability, and every row-and-column-stochastic kernel on a **finite** set
has `‖K‖_{ℓ²} = 1` exactly, while the state space must be finite for `p(N,c)` to
mean what the rate says.

**Reusable positives.** `p(N,c) = P[S_j ≤ αj + c ∀ j ≤ N]` for i.i.d.
Geometric(1/2) letters — the dyadic mass *is* that probability, whence
`I₀ = J(α)` with `J(a) = a(1−H₂(1/a))`. And a drifting budget `c = θN` has rate
`J(α+θ)`, vanishing at `θ ≥ 2−α = 0.4150375`: **a linear confinement defect makes
a mass target strictly harder**, so the fixed-`c` scope of `confined_mass_rate`
is not a usable escape.

**Where the difficulty actually is.** The bulk of the confined population obeys
equidistribution to within `1.6 %` (`N ≤ 24`, all odd `m < 2^17`), while
`ρ(N)/r_min(N)` with `ρ(N) = 2/p(N,0)` peaks at `17.34` and drops *below* `1` at
each record transition. **The aggregate statistics are correct, and that is why
they say nothing: the whole problem is one atypical integer per range, beating
the mean by a bounded factor, invisible to every exponential-rate argument.**

**Next lemma.** `r_min(N,0) ≥ C^{−1}N^{−B}/p(N,0)` for some `C, B` — sufficient
for the pointwise target, and its content is exactly the *absence of an additive
term*. Measured true with `B = 0`, `C ≈ 17` to `N = 108`.

---

## 2. The López–Stoll critical-density bridge

Full package: [`audits/lopez_stoll_transfer_2026-10-14/`](../audits/lopez_stoll_transfer_2026-10-14/).

**Scope.** Whether the exact confined-mass machinery strengthens the
critical-density arguments of López and Stoll, and whether their conjugacy
analysis bridges symbolic density to positive-integer realizability.

**The two frameworks are the same object.** With `Δ_i = αi − S_i`, `q_N` the
carry, and `Φ` the Bernstein–Lagarias conjugacy
(`Φ(2^{d_0}+2^{d_1}+…) = −Σ_i 2^{d_i}/3^{i+1}`, `d_i = S_i`):

```
    Φ_R(v) = −(1/3) Σ_{i≥0} 2^{−Δ_i} ,          Φ_R(u^{(S_N)}) = − q_N / 3^N ,
    Φ_R(u^{(ℓ)}) = m₀ − (2^ℓ/3^h) T^ℓ(m₀)             [exact over Q, 0 violations]
```

so **López–Stoll's real devil's-staircase object is the normalized EOC carry**,
and `Φ_R` converges ⟺ `q_N/3^N` converges ⟺ `Σ 2^{−Δ_i} < ∞` ⟺ `Σ 1/m_k < ∞`.
The identity is the carry identity (Rev 8 Lemma 2.4) in different coordinates; the
identification appears to be new.

**The 2021 preprint's main theorem has an invalid step.** Its Theorem 1 concludes
that a divergent rational 2-adic must have parity density exactly
`β = log2/log3`, via *"`Φ_R(v)` irrational ⟹ `Φ(v)` aperiodic"*. The real and
2-adic limits of the same series are different numbers, and the dictionary gives
the discrepancy exactly: for a positive odd seed `Φ(v) = m₀` while
`Φ_R(v) = m₀(1 − 2^{E_∞})` — for `m₀ = 27` the real partial sum at `N = 8` is
`−1.405426` against the 2-adic value `27`. So `Φ_R(v) ∉ Q_odd` says nothing about
`Φ(v)`. Its equations (15)–(16) only say that the 2-adic *digits* of `Φ(v)` are
read off the partial sums, which holds whether or not the real series converges.
Two further issues: the proof's trichotomy presupposes that `lim h/ℓ` **exists**
(what the argument supports is a statement about `liminf`), and the repaired
branch reduces to Curry's reciprocal summability, already a theorem.

> **Theorem 1 of the 2021 preprint is recorded as an unaudited / incomplete
> dependency.** The theorem may still be true; its proof as written does not
> establish it. The 2009 refereed paper is sound and contains **no** density
> theorem — its own word for full complexity is *"suggest"*. Securely covered is
> only the `liminf < β` branch, which is Monks–Yazinski (2004) and Lagarias.
> **After the audit López–Stoll adds nothing to the restrictions on a confined
> positive integer.**

**Two-clock facts, for reuse.** `liminf_ℓ h/ℓ = liminf_N N/S_N = 1/limsup(S_N/N)`
(the in-block infimum sits at the block *end*). Under confinement,
`liminf_ℓ h/ℓ = β ⟺ liminf Δ_N/N = 0`, and `lim_ℓ h/ℓ = β ⟺ Δ_N = o(N)`. Exact
`0`-confined witnesses show `A ⇏ D/E/F/G` (the all-ones word has
`Δ_N/N = α−1` constant), `D ⇏ E` and `E ⇏ F`: **`liminf Δ_N/N = 0` yields no
`O(log N)` and no `O(√N)` return corridor.**

**A warning control worth keeping.** The all-ones accelerated word is
`0`-confined with unbounded linear deficit yet realizable by **no** positive
integer — every positive `m₀` leaves it after exactly `v₂(m₀+1) − 1` steps, and
its only realizer is `−1`, a fixed point. Finite-prefix realizability is
automatic and carries no information about the infinite word.

**New estimate, honestly placed.**
`#{i<N : Δ_i ≤ w} ≤ 3m₀2^w(2^{E_N}−1) ≤ 3e^{7/9}m₀2^wN^{1/9}` for `m₀` odd with
distinct states. Putting the count equal to `N` and `w = B log₂N + C` gives
`N^{8/9−B} ≤ 3e^{7/9}2^Cm₀` — **verbatim** `EOC/LogCorridor.lean`'s
`logFloor_window_bound'`, constant included. The advance is only the weakened
hypothesis: *floors at every prefix* becomes *count the returns*.

---

## 3. Joint episode budgets against the carry pot

Full package: [`audits/joint_episode_budget_2026-10-14/`](../audits/joint_episode_budget_2026-10-14/).

**Scope.** Whether two or more *actual* corridor episodes (`R_n ≤ c`, one-sided)
can be jointly charged so as to bound their **combined duration**, rather than
each being given its own single-window lifetime allowance — the amortization
that Rev 8 Remark 13.3 shows the naive surrogate fails to achieve.

**Credit first.** The two principal findings below — that the per-episode charges
are *pinned* and therefore not amortizable, and that the resource is `Θ(m₀)`
against an `O(log m₀)` target with overshoot `Θ(m₀/log m₀)` — were **already
established** in the earlier Phase 6 return-gate round (local scratch, not
published), for the *entry gate*. This audit re-derives them for a different
resource (the **carry pot**) and adds the exact integral form. The episode-count
bound here is **strictly weaker** than Phase 6's attained bound and is not
offered as an improvement.

**What is new, and it is small.** From Rev 8 Prop. 13.1, at every re-entry
`a_i > 0` the entry depth is pinned, so `z_{a_i} = 2^{R_{a_i}} > (2/3)2^c` and

```
    W_i := Σ_{n∈I_i} z_n  >  (2/3)2^c ,        equivalently   η_i ℓ_i > 2/3 ,
```

**independently of `ℓ_i` and of how deep the episode goes.** The carry-*weighted*
duration has a universal per-episode floor although the duration has none.

**The joint charge exists and points the wrong way.** Telescoping gives one
shared pot, `Σ_i W_i = 3Σ_i(𝓑_{b_i}−𝓑_{a_i}) ≤ 3(𝓑_H − m₀)` with
`𝓑_n = m_n 2^{R_n} = m₀ + C_n/3^n`, so no per-episode seed allowance is
refreshed. But on the corridor `z_n ≤ 2^c` while in a gap `z_n > 2^c` and grows
geometrically, and the pot is measured at **99.94 %** gap weight at the Loeb seed
(`53.31` occupied against `96115.13` in gaps). Amortizing against it therefore
constrains **gap** time: with `G = H − O_c`, `2^cG < pot` rearranges to
`O_c > H − 2^{−c}·pot`, a **lower** bound on occupation.

**Non-vacuity is localized to an already-closed sector.** The resulting bound
`P − 1 < (9/2)2^{−c}m₀(2^{E_H}−1)` has a stable slack of `3.5×` on the Rev 8
Prop. 13.2 oscillator (bounded two-sided drift) across `c = 0,1,2` and
`N = 60,120,200`, and degrades like `2^{R_max−c}` to `10^4–10^7` on seeds whose
drift escapes. Bounded two-sided drift is exactly what
`eoc-lean-verification`'s `EOC/BoundedDrift.lean` already closes.

**The small-`η` problem in exact form.** Stratifying the occupied times by depth,
`L_w = #{n<H : c−w−1 < R_n ≤ c−w}`, exactly `Σ_w L_w 2^{−w} < 2^{1−c}·pot` while
`O_c = Σ_w L_w`. The route needs a depth bound `w_max ≤ K log₂ O_c` with `K < 1`;
measured `w_max/log₂O_c ∈ [1.16, 1.73]` over eight cases, so **`K < 1` is not
supported**. This independently reproduces Phase 6's one open item (depth
`≈ ℓ/10`, `corr = +0.923`): depth looks **linear** in length, which is precisely
what kills a `2^{−w}`-weighted budget.

**Silence on divergence, stated.** A hypothetical infinite zero-confined orbit is
a **single** episode: `P = 1`, so the toll contributes exactly `0`. Visible in the
data rather than argued — every single-episode seed tested (`27, 703, 10087,
35655, 381727` at `c = 1`) shows toll `0.000000`. **Classification:
separated-return control, not divergence exclusion.** No corridor-uniform
lifetime hypothesis is assumed (Rev 8 §7.1), Theorem 6.14's external sparsity
dependency is untouched, and no cycle-exclusion is claimed.

**Benchmark replicated.** Rev 8 Remark 6.2's example is reproduced from scratch
in exact integer arithmetic: `O₁(285175) = 98`, `L₁ = 14`, `τ₁ = 15`, and all
seven occupied runs `[0,15), [16,20), [21,27), [31,95), [98,99), [100,105),
[108,111)` with lengths `15+4+6+64+1+5+3`, on a horizon **certified** by the
fixed-point drift rather than a scan cutoff.

**Next question.** Is the depth of a corridor episode logarithmic or linear in
its length — does `max_{n∈I}(c − R_n) ≤ K log₂ℓ + C` hold with `K < 1`, or is
there an explicit family with `Ω(ℓ)`? The first closes the pot route's only gap;
the second closes the route permanently and, with it, every amortization against
a `2^{−w}`-weighted budget.

---

## Common scope note

All three audits are documentation of negative results. Nothing in them proves,
advances, weakens or conditionally establishes EOC, Open Problem F, `(DE)`,
divergence exclusion, cycle exclusion, or the Collatz conjecture. **No Lean
verification is claimed anywhere**: no `lake build` was run in any of the three
rounds, and every Lean reference is source-backed by reading the named file.
External results (Monks–Yazinski 2004, Lagarias, García–Tal 1999, Curry 2026, and
the percolation preprint) are **source-reported, not independently read**, and are
cited only where a dependency is actually used.
