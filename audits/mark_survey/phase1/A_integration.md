# Phase 1 — Group A: the integration / π side

Reading only. Page/section references are to the PDFs listed in `SOURCES.md`.
`S1` (the quarter-gamma note) has its own file, `phase1/S1_quarter_gamma.md`.

---

## A01. *Local algebraicity and graded global periods on the Thales partition manifold*, Rev. 2 (July 2026)

For the partition `a+b=1` with altitude `h=√(a(1−a))`, the ring `A = Q[a,h]/(h²−a(1−a))` is
free of rank two over `Q[a]`, and the involution `h ↦ −h` grades it into `A⁺ = Q[a]` and
`A⁻ = hQ[a]`. Integration over `[0,1]` respects that grading: `∫A⁺ ⊆ Q` and `∫A⁻ ⊆ πQ`, with
`∫a^k h da = C_{k+1}π/2^{2k+3}`. Two Gaussian-normalized probes sort local Taylor content into
parity-complementary sectors, and the grading then predicts the global period class in advance.
The note is explicit that producing transcendental values by integrating algebraic data is
classical (Kontsevich–Zagier periods); what is claimed is the *graded* transport statement.

**Candidates.**
- **G7 (layer classification of a constant).** Prop. 11.1 [PROVED as a classification]: any constant
  met in exploratory work is exactly one of — a **normalization ghost** (present because of a chosen
  kernel or measure, removed by normalization), a **local structural constant**, or a **global
  period** (appearing only after integration over the constraint space); `√π` is a ghost on the
  differential side and `π` a genuine period on the integral side, and *which* is predictable in
  advance from the altitude parity of the sector. This is the sharpest available template for the
  whole survey: a survival criterion with an a priori grading predictor.
- **G7a (resolution ratio).** `ρ(n) = J(n+½)/J(n) = r_nπ`, `r_n ∈ Q` (Thm. 10.2): the global cost of
  replacing a capacity power by an altitude power is always a rational multiple of `π` — one
  surviving factor, because numerator and denominator sit in opposite graded sectors.

## A03. *Parity-complementary mollifier operators* (April 2026)

Constructs the operator pair `(D_h, D̃_h)` with window scale set by the altitude; `D_h` probes odd
derivatives and `D̃_h` even ones; `D_h y → y′` and `D̃_h y → 0` as `h → 0`. Neither carries a
surviving `√π`: the Gaussian normalization cancels mechanically against the Gaussian even-moment
structure. §8.3 records the by-product: at the apex `a = ½` the pair `(D_h y, D̃_h y)` classifies a
curve as symmetric / antisymmetric / mixed under `a ↔ 1−a`.

**Candidates.**
- **G8 (parity class at the involution's fixed point).** A `Z/2`-valued invariant read off at the
  unique fixed point of the partition involution, reflecting a global symmetry from one point.

## A02. *Structural layers of the Thales semicircle* (May 2026)

Primitive Pythagorean triples give a rational-state skeleton on the semicircle
`h = ½√(1−x²)`; the normalized even moments of the same curve are the Catalan numbers,
`∫x^{2n}ρ = C_n/4^n`. The note's whole point is conservative: neither skeleton counts the other —
they are an *arithmetic, local* skeleton and a *moment-combinatorial, global* skeleton on one host.
The appendix adds two further layers (Wigner density, Hermite amplitudes carrying `π^{−1/4}`).

**Candidates.**
- **G9 (moment skeleton).** The moment sequence of the empirical measure attached to an object:
  survives every limit, and by the note's own thesis carries no information about which rational
  points lie on the curve. The clean statement of the compactness/correspondence failure the brief
  names: moments are exactly the observable that forgets integrality.

## A08. *Two complementary periods, modular self-duality, and a beat frequency* (June 2026)

A Thales–Legendre partition `k²+k′²=1` carries `K(k)` and `K(k′)`, hence `τ = iK′/K ∈ H`; the
duality `k ↔ k′` is the modular inversion `S: τ ↦ −1/τ`, whose fixed point `τ = i` is the self-dual
modulus `k = 1/√2`; the detuning `δ = ln(K′/K)` is the signed hyperbolic distance from that fixed
point; and the beat frequency vanishes linearly in `δ` with slope `1/(4K_sd) = √π/Γ(¼)²`. Two
*distinct* centres are separated: the rapidity rest frame (equipartition) and the self-dual centre.

**Candidates.**
- **G10 (detuning from a self-dual fixed point; log-periodic beat).** A signed hyperbolic distance
  from the fixed point of the duality involution, and — §8, second bullet — the reading that in a
  scale-dependent system such a beat appears "not in a spatial coordinate but in the logarithm of
  scale, as a log-periodic modulation riding on a power law". That is the shape the EOC programme's
  own `O(1)` renewal phase already has.

## A05. *Boundary and interior record chronologies for the two-mode oscillator spectrum* (Aug 2026)

For `E(n₁,n₂)` with frequency ratio `α>1`, states are ordered by height `h = (mα+k)/2` and one asks
which states achieve each successive strict improvement of an observable. Two complete theorems:
the boundary records are the minimum-occupation ladder plus a finite exceptional set, with
`h·ε_edge = ½` exactly; and for `α = √2` the interior balance records are a merged pair of Pell-
automorph orbits. The scaled envelope `E_bal(H) = H²·min_{h≤H}ε_bal` has exact
`liminf = ¼`, `limsup = (57+40√2)/28`, and **is an exactly periodic function of `log H` with period
`log λ`**. A proved rational dichotomy: rational `α` gives a terminating chronology (if `pq` odd) or
a boundary-like one with a *collapsing* envelope and linear counting (if `pq` even); quadratic
irrationals give sparse geometric chronologies with logarithmic counting and non-degenerate
envelope oscillation; `e` and `π` track continued-fraction convergents in runs. The note explicitly
declines to promote the two-regime contrast to a classification by algebraic degree.

**Candidates.**
- **G11 (scaled record envelope).** `E(H) = H^κ · min_{height ≤ H} ε(·)`, its `liminf`/`limsup`, and
  its exact log-periodicity — a normalized quantity that survives the limit and whose *shape*
  (oscillating vs collapsing vs terminating) differs between arithmetic classes of the parameter.
- **G12 (record-counting coefficient).** `lim N(h)/log h = 2/log λ` for the quadratic-irrational
  regime, versus power counting in the rational regime.
- **G13 (defect cycle).** The signed norm defect along records (`−1, +7, −1, +7, …` for `√2`;
  `−1, +1, −5` for `φ`), a finite signed cycle attached to the record ladder.

## A12. *The dual diagonal and reconstruction of orthogonal hyperrectangles* (2026)

Records an alternative invariant basis `(d², d′², V)` for reconstructing box shape. The content
relevant here is the negative half: shape space has dimension `n−1`, so for `n ≥ 3` no single
scale- and permutation-invariant scalar is reconstructive — its level sets are positive-dimensional
(Prop. 5.1, with an explicit 3D counterexample), and once the dimension count is saturated higher
moments add no independent information.

**Candidates.**
- **G14 (aggregate-scalar sufficiency).** Whether a finite family of aggregate invariants determines
  the object. Recorded here mainly as the dimension-count form of the barrier the survey is testing.

## A14. *Spectral coupling and structure-dependent relaxation in first-order consensus networks*, Rev. 2

A phenomenological marker at `λ ≈ 1.7` is replaced by its governing invariant: relaxation is
controlled by the spectral product `αλν_k`, asymptotically by the algebraic connectivity `ν_min`.
Ring and star track each other because they share `ν_min = 1`; the residual ~11 % offset is an
*intercept* effect from how random initial conditions load the slow eigenspace. Summary: "rate is
global algebra; offset is local statistics", and the measured `1.7` feature is shown to be absent.

**Candidates.**
- **G15 (rate versus offset).** The asymptotic *rate* is a global invariant that forgets the
  individual initial condition; the individual survives only in the `O(1)` intercept. A direct
  structural statement about where individuality can live in a limit.

## A15. *The compactness partition on the period dial*, V2 (Aug 2026) · A16. *Compactness as a thermodynamic saturation coordinate*, V2 (May 2026)

A16 records `S_B/S_BH = C` exactly and puts the bounded partition `(C, 1−C)` on the atlas dial.
A15 reorganizes it around the augmented frame `A = (p,d,s,τ)` and supplies two things this survey
uses. Prop. 2: any diagnostic that is a function of the partition coordinate alone is constant on
the fibres of `π`, so it can decide membership in a structure `S` only if `S` is a union of fibres.
§8: the accelerated-Collatz constant `I = D(log₃2‖½)/log₃2 = 0.0793186…` transfers **as a functional
form only**; Correction 1 shows the inverse problem `D(C‖½)/C = I` has **two** roots
(`0.396040` and `log₃2`), so the constant does not even invert uniquely — "functional-form
correspondence ≠ domain-selected constant".

**Candidates.**
- **G16 (entropy-deficit coordinate).** `D(p‖½)/p`, and its value `I₀` at the neutrality density
  `p = log₃2`.
- **G16a (fibre criterion).** Not a mark but the general form of screen S1, stated and proved in
  the author's own work: a diagnostic factoring through a coarse coordinate cannot resolve anything
  finer than that coordinate's fibres.

## A09. *Archimedean compensation on the Thales semicircle*, Rev. 3 (Feb 2026)

Two parameters organize the construction: the radius `R = ½` (contraction rate, variance–deficit
exchange `L² = D(2R−D)`) and the Shannon-optimal asymmetry `χ = 1/e`. The apex is a saddle:
contraction at rate `½` under the iterated harmonic mean, expansion at Lyapunov exponent `ln 2`.
The random-partition baseline `⟨h⟩ = π/8` is offered as a null hypothesis for coupling in the
absence of a selection principle.

**Candidates.**
- **G20 (null baseline and its offset).** A computed no-selection baseline, with the measured
  departure from it as the diagnostic — structurally the same device as the EOC null model `N0`.

## A06. *Strain–vorticity interaction and rotational coherence* (Sept 2026)

Retracts a magnitude-comparison criterion (`ζ`, an affine rescaling of `Q`): the Burgers vortex is
*sustained* by increasing axial strain even as `ζ` moves to its most strain-dominated value. The
replacement is the exact interaction term `P = ω·Sω = |ω|²σ_eff`, i.e. a quantity built from the
*alignment* of two structures, not from their sizes; and the note shows why no universal scalar
threshold or corridor follows from it.

**Candidates.**
- **G17 (coupling rather than magnitude).** A mark must be an interaction/alignment term between
  two structures, not a comparison of two magnitudes. The same demand as Criterion (iii) of the
  synthesis note.

## A10 / A11. *The partition-intrinsic cubic* (Aug 2026, two notes)

`a+b=1` with `a=b³` gives `R* = ψ−1 = 0.465571…`. A11 reports an adversarial test of the
"universal transition" hypothesis across seven domains: **not supported anywhere**; domain
transitions select their own partition geometries, and a systematic exponent comparison shows no
preference for cubic order. In the two genuine domain-generated cubics (van der Waals, principal
stresses) the meaningful event is **root degeneracy**, not the cubic degree. What survives every
test is that the two constraint curves meet *transversally*.

**Candidates.**
- **G18 (degeneracy versus transversality).** Whether a constraint intersection is degenerate
  (repeated root) or transversal — a discrete, limit-stable invariant.

## A13. *The Minkowski interval as a Thales coupling diagnostic* (April 2026)

`ds² = −4c²dt²h²_SR` with `h_SR = ½√(1−β²)`, so `γ = 1/(2h_SR)`: the relativistic response factor
is the reciprocal of the coupling diameter. Recorded as an example of the bounded–unbounded
duality — bounded ratio, bounded altitude, unbounded response.

**Candidates.**
- **G19 (bounded–unbounded duality).** A bounded coordinate whose reciprocal response diverges.

## A04. *√π as a dimensional-reduction and transition-normalization constant* (April 2026)

Records the parity split of the altitude integral family `I(α) = B(α/2+1, α/2+1)` — even altitude
powers rational, odd powers rational multiples of `π` — with `I(−1) = π` the global angular measure,
and classifies `√π = Γ(½)` as the half-gamma completion whose *paired product* gives the full
measure. Local derivative structure stays algebraic; `√π` appears only under global integral
completion. No fast-series construction for `1/√π` is attempted, and none is claimed.

**Candidates.** Same layer classification as **G7**; the pairing `Γ(½)·Γ(½) = π` is the
one-line prototype of the conjugate-stratum collapse of `S1`.
