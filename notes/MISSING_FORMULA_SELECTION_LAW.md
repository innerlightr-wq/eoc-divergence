# The finite-height selection law

**Research record, 2026-09-26. Not a revision of the synthesis paper, and not a claim
of progress toward (DE) or the Collatz conjecture.**

Six mechanism imports were run against the missing pointwise tool. All six stopped,
and all six terminate at the same object: the placement of specific integers inside a
population whose size is already known. This note records what each contributed, the
exact statements worth preserving, and an isolation of the remaining gap as a single
ratio.

Reproduction: [`../audits/missing_formula_selection`](../audits/missing_formula_selection),
with the captured run in
[`repro.txt`](../audits/missing_formula_selection/repro.txt).

---

## 1. Six-audit convergence

| route | contributed | stopped at | why the same gap |
|---|---|---|---|
| **Rozier / abc** (arXiv:2306.15284v2) | exact cost calibrations; the dictionary `c_w = C_n`; abc applies to the one-defect stratum | `d ≥ 2` gives a ≥4-term relation, needing the `n`-conjecture, not abc | the one stratum it reaches is exited by a fixed seed in ≈3 steps, so it bounds `min N(j)` per `j`, never one orbit |
| **switch / `S`-unit** | the switch decomposition and the margin–switch tradeoff (§2) | the relation has `S`-unit *interior* terms but two free integer endpoints `m_0+σ_1`, `m_n+σ_ℓ` | fixing the seed removes one endpoint; `m_n+σ_ℓ` is the orbit value, whose factorisation is exactly what placement would control |
| **Sturmian / Liouville** | the square criterion transported to accelerated coordinates; the automatic height bound (§2.3) | confinement does not force long squares: confined near-critical words avoid squares of period ≥ 12 from band width 2 upward | the mechanism bites on square-rich words, already closed; entry is not forced |
| **imaginary hypotenuse** | the exact two-angle identity `m_n/m_0 = cot²(θ_D/2)·sec²(θ_C/2)` | `θ_D` is monotone in `H_n`, `θ_C` in `R_n`; the system is a skew product with no feedback | a reparameterisation of `(H_n, R_n)`; the descent boundary is the conclusion |
| **inherited membership** | the bit-loss law and minimal-automaton saturation (§2.4) | no finite-state membership is inheritance-stable; the only closed one (`m mod 3`) restricts nothing | the smallest closing state is the realizer cylinder, i.e. the placement datum itself |
| **micro / macro fibers** | cylinder conservation and the precision/multiplicity duality (§2.5–2.6) | the aggregate law closes, but its one free parameter is `Q` | `Q` is a monotone re-encoding of the frontier residual `Δ_N` |

The convergence is the content: six mechanisms with genuinely different inputs all
reduce to arithmetic selection among cylinders whose symbolic mass is already known.

## 2. Exact results worth preserving

Statements and verification counts below; proofs and enumerations in the scripts.

### 2.1 Switch decomposition
For a `{1,2}`-word with runs `R_1…R_ℓ`, boundaries `0 = p_0 < ⋯ < p_ℓ = n`,
`σ_t = ±1` for letter `1`/`2`, and `B_t := 2^{S_{p_t}} 3^{n−p_t}`:
```
C_n = σ_1 B_0 + Σ_{t=1}^{ℓ−1} 2σ_{t+1} B_t − σ_ℓ B_ℓ,
```
with **exactly `r+2` terms** (`r` = number of switches), coefficients `±1` at the ends
and `±2` inside, all monomials distinct. *Verified: all 65,534 words of length ≤ 15;
0 mismatches in value, term count, or distinctness; coefficients `{−2,−1,+1,+2}` only.*
Refines the defect bound `2d+2`: `1^a2^b` has `d = Θ(n)` but `r = 1`.

### 2.2 Margin–switch tradeoff
With `κ := (α−1)(2−α) = 0.2427814…`, a `{1,2}`-word with `0 ≤ H_j ≤ W` for all `j`
satisfies
```
r + 1 ≥ 2κ·n/W − (α−1).
```
*Verified: all 34,125 zero-confined words of length ≤ 16; 0 violations.* Bounded switch
count and narrow confinement are incompatible.

### 2.3 Automatic confined-height bound
On any zero-confined word, `2^{S_i} ≤ 3^i` gives
```
C_n/3^n = Σ_{i<n} 2^{S_i}/3^{i+1} ≤ n/3,   hence   C_n ≤ (n/3)·max(2^{S_n}, 3^n),
```
with **no balance hypothesis**. *Verified: 34,125 words; 0 violations; max `C_n/3^n = 3.987`.*

### 2.4 Bit-loss law
If `m ≡ m′ (mod 2^K)` with common determined valuation `a`, then
`T(m) ≡ T(m′) (mod 2^{K−a})` and no finer, so retained precision obeys
```
K_{n+1} = K_n − a_n,   i.e.   K_n = K_0 − S_n.
```
*Verified: every odd class mod `2^K` splits under one step, `K = 6,8,10,12,14` —
fraction 1.0000 in each case.* Companion facts: the first `L` valuations are fixed by
`m mod 2^{S_L+1}` and no smaller modulus (70,000 pairs, 0 failures); and the quotient
of odd residues mod `2^N` by `L`-step futures saturates at the full `2^{N−1}` states.
**No nontrivial finite-state compression exists.**

### 2.5 Precision–multiplicity duality
With odd-Haar mass `μ(w) = 2^{−S_n}`, the child `wa` has `μ(wa)/μ(w) = 2^{−a}` and
`Σ_{a≥1} 2^{−a} = 1`. Hence
```
precision lost per step = a_n = log₂( 1 / relative child mass ).
```
*Verified: 255 words, 0 failures as exact truncated geometric sums.* Nothing is
destroyed: what the forward map consumes in resolution, the tree carries as mass
subdivision.

### 2.6 Cylinder conservation
`C(w) = r_w + 2^{S_n+1}ℤ`, and every `m ∈ C(w)` has a well-defined next valuation, so
```
C(w) = ⊔_{a≥1} C(wa),   hence   N_M(w) = Σ_{a≥1} N_M(wa)   for every height M.
```
*Verified: 728 tree nodes at `M = 10^4, 10^6`; 0 partition failures, tested by direct
partition with no truncation.*

## 3. The finite-height count

```
A_{N,M} = #{ m odd, 1 ≤ m ≤ M : m is zero-confined for N steps }     (integer)
O_M     = #{ m odd, 1 ≤ m ≤ M } = ⌈M/2⌉
p_N     = Σ_{w confined, |w| = N} 2^{−S_N(w)}                        (exact rational)
```
and the **selection ratio**
```
Q_{N,M} := A_{N,M} / (O_M · p_N),        so        A_{N,M} = Q_{N,M} · O_M · p_N.
```

> **This is a definitional identity, not a theorem about the behaviour of `Q`.**

## 4. Interpretation

- `p_N` — the exact confined Haar/density mass. **Solved**: the rate
  `−(1/N)log₂ p_N → I₀ = α(1−H₂(1/α)) = 0.0793186…` is formalized
  (`Occupation.confined_mass_rate`), with the polynomial correction also proved.
- `O_M` — the finite archimedean population. **Trivial.**
- `Q_{N,M}` — the finite-height arithmetic selection/placement ratio. **Unexplained.**

`Q` is **not** an independent dynamical law. It is the target quantity whose
nontrivial behaviour remains unexplained, written in a form that isolates it from the
two factors that are understood.

Why the obvious bound fails: `N_M(w) ≤ 1 + M/2^{S_N+1}` summed over confined words
gives `A_{N,M} ≤ #W_N^{conf} + O_M p_N`. With `h := αH₂(1/α) = 1.5056439…` and the
identity `h + I₀ = α`, the count `#W_N^{conf} ≈ 2^{hN}` makes the union bound useless.
The `+1` per word is the obstruction: one must know *which* cylinders are occupied.

## 5. Relation to `Δ_N`

At `M = r_min(N,0)` we have `A_{N,M} = 1`, and `M` is odd so `O_M = (M+1)/2`. Hence
```
Q_{N,M} = 2 / ((M+1) p_N),
```
and with `Δ_N := log₂ r_min(N,0) − log₂(1/p_N)`,
```
Δ_N = 1 − log₂ Q_{N,M} − log₂(1 + 1/M).
```
*Both relations verified on exact rationals at `N = 4,8,…,36`: 0 mismatches, including
`A_{N,M} = 1` at each.* `Q` therefore **globalises** `Δ_N`, which is its specialisation
to the single frontier value of `M`.

> **Caution, and it matters.** `Q ≈ 1` is a statement about *large* finite-height
> ensembles. At the frontier specialisation `M = r_min(N,0)` the same `Q` **grows**:
> `0.352, 0.797, 1.370, 2.310, 3.710, 5.437, 8.160, 12.051, 16.722` at
> `N = 4,8,…,36`, because `r_min(N,0) = 27` is frozen while `log₂(1/p_N)` rises. The
> two regimes are the same object at different `M`, and neither licenses a claim about
> the other.

The practical advantage of the global form is conditioning: `Δ_N` is a min-statistic
driven by rare record replacements, whereas `Q_{N,M}` for large `M` averages over
thousands of surviving seeds.

## 6. Extinction criterion — conditional mechanism only

`A_{N,M} ∈ ℤ_{≥0}`. Therefore any rigorous estimate giving
```
Q_{N,M} · O_M · p_N < 1        forces        A_{N,M} = 0.
```
Since `p_N ≍ N^{−3/2} 2^{−I₀N}`, a bound `Q_{N,M} ≤ poly(N)` uniform in `M` would give
`A_{N,M} = 0` for `N` large depending on `M`; as every positive odd integer lies below
some `M`, that is (DE).

> **Strength.** Such a bound **implies (DE)**. It is therefore at least as strong as
> (DE), and belongs with the exponential realizer floor and `Δ_N = O(1)` among
> sufficient statements — not among weaker intermediate targets. This note claims no
> route to it.

The integrality step is the only part doing real work, and it is why the integer count
`A_{N,M}` is the right object rather than a mass.

## 7. The `3x−1` control

`3x−1` shares `α`, the confined-word count and `p_N` with `3x+1`: the symbolic side is
identical. It differs in that `m = 1` is a zero-confined positive fixed point.
Measured at `M = 2^16 − 1`, `O_M = 32768`:

| `N` | `A(3x+1)` | `A(3x−1)` | `O_M·p_N` | `Q(3x+1)` | `Q(3x−1)` |
|---|---|---|---|---|---|
| 8 | 2936 | 2936 | 2.9360e3 | 1.000 | 1.000 |
| 24 | 436 | 425 | 4.3053e2 | 1.013 | 0.987 |
| 48 | 26 | 66 | 5.1089e1 | 0.509 | 1.292 |
| 80 | 2 | 4 | 4.5730e0 | 0.437 | 0.875 |
| 100 | **0** | 3 | 1.1310e0 | 0.000 | 2.653 |
| 140 | 0 | 3 | 7.9550e−2 | 0.000 | 37.712 |
| 180 | 0 | 3 | 6.4104e−3 | 0.000 | **467.992** |

`3x+1`: last `N` with `A > 0` is **84**; `A = 0` from `N = 85`. `3x−1`: still `A = 3` at
`N = 190`. Extinction depths for `3x+1` at smaller heights: `M = 2^8` at `N = 37`,
`2^{10}` at `51`, `2^{12}` at `51`, `2^{14}` at `66`, `2^{16}` at `85`.

For `3x+1`, `Q` is of order 1 across the tested pre-extinction regime
(`Q ∈ [0.92, 1.12]` for `M = 2^{16}…2^{22}`, `N = 8…48`) and the selected ensembles
eventually empty. For `3x−1` the positive anchor prevents extinction while the
symbolic mass shrinks identically, so `Q` grows strongly.

> **Any future useful bound on `Q` must be sign-sensitive and must fail on the `3x−1`
> positive anchor.** A bound blind to the sign of the anchor would falsely exclude
> `m = 1` under `3x−1`.

This is a constraint on proofs, not evidence that `Q` is a powerful coordinate: `Q`
separates the two maps because it is *defined from* `A_{N,M}`, which is the quantity
that differs. No values outside the tables above are claimed or extrapolated.

## 8. Epistemic status

**PROVED / EXACT**
- the switch decomposition (§2.1) and margin–switch tradeoff (§2.2);
- the automatic confined-height bound (§2.3);
- the bit-loss law `K_n = K_0 − S_n` and the precision budget (§2.4);
- the precision–multiplicity duality (§2.5);
- cylinder mass conservation (§2.6);
- the definition `A_{N,M} = Q_{N,M} O_M p_N` (§3) and the exponent identity `h + I₀ = α`;
- the relation `Q = 2/((M+1)p_N)` and `Δ_N = 1 − log₂Q − log₂(1+1/M)` at `M = r_min(N,0)` (§5).

**VERIFIED (finite range, exhaustive, exact arithmetic)**
- `Q ∈ [0.92, 1.12]` for `M = 2^{16}…2^{22}`, `N = 8…48`;
- the frontier-specialisation values of `Q` at `N = 4…36` (§5);
- extinction depths for `M = 2^8…2^{16}` (§7);
- the `3x+1` / `3x−1` control table (§7).

**OPEN**
- boundedness of `Q_{N,M}`;
- polynomial or subexponential growth of `Q_{N,M}`, uniform in `M`;
- any pointwise exclusion following from either.

No claim of progress toward the Collatz conjecture is made or implied. Nothing in this
note revises the synthesis paper.
