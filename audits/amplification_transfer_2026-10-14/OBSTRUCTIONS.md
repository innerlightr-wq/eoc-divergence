# OBSTRUCTIONS.md — counterexamples, circular arguments, failed transfers

---

## 1. Refuted in this session, on exact examples

**(R1) "Recombination onto the smaller digit fails for most suffixes."**
*Mine, asserted before testing; refuted immediately.* The down-shift is **total
and defect-free at every depth** — survival rate exactly `1.0000` for
`N = 3..12`, every branch node, every suffix (`scripts/recombine.py`). Lowering
a digit lowers every later partial sum, so confinement is inherited. The
direction was inverted: it is the **up-shift** that fails, at rate `0.40–0.69`,
with budget defect growing like `N/2`. Recorded, not redefined.

**(R2) "At `N = 4` the root node has children `e = 1, e' = 2`."**
*Mine; fabricated.* Every `0`-confined word of length `4` begins with `d_1 = 1`
(all `7` of them: `1111, 1112, 1113, 1121, 1122, 1211, 1212`), so the root has a
single child and the example does not exist. The habit this punishes is writing
a "worked example" from the shape of a formula instead of from the enumeration.

**(R3) "The down-shift has a stable positive index surplus `delta ≈ 0.21`."**
*Refuted by extending the proof rather than the table.* The measured
`delta_N` is `0.2125, 0.2084, 0.2115, 0.1985` at `N = 8,10,12,14` and looks
constant. It is not: `#I_N/n_N` grows **linearly** (`3.25, 4.24, 5.81, 6.87`),
and `log_2(N/2)/N` is `0.2005` at `N = 14` but `0.0564` at `N = 100` and
`0.0090` at `N = 1000`. Theorem 4 of `JOINT_INVERSE_ATTEMPT.md` proves fibres
are `O(N^2)`, hence `delta_N = O(log N / N) -> 0`. **A plateau over seven
consecutive even depths was a finite-size artifact of a slowly varying
logarithm.** This is the one place in this session where numerics alone would
have produced a false positive.

## 2. The structural obstructions, each independent of the others

**(O1) The mass criterion is vacuous.** Any family of pairwise distinct
`0`-confined residue classes has measure `<= mu(C_N) = 2^{-I_0 N + o(N)}`, so the
demand `mu(B_N) >= c 2^{-eps N}` with `eps < I_0` is unsatisfiable for every `m`,
persistent or not — it asks for more confined classes than exist
(`AMPLIFICATION_CRITERION.md` Theorem 1, Corollary 1a). The implication
"persistence `=>` such a family" is therefore logically equivalent to the target
and decomposes nothing. **No injection into the confined population can amplify
its mass — not permutations, not lifts, not any map.**

**(O2) There is no multiplicity to remove.** Lemma 4.8's whole achievement is
deleting a factor `W^{2k} = 2^{Theta(k log M)}` from an inverse count. That
factor exists because the percolation splice is non-injective and its inverse
must be *coded*. In EOC the correspondence
`0-confined word <-> odd residue class mod 2^{S_N+1}` is a **bijection**
(`leastRealizer_unique`, `residue_pinning`; verified max fibre `= 1` for
`N = 1..14`, 0 violations): the inverse is a division, the code is empty, the
multiplicity is `1 = 2^0`. **The technique solves a problem EOC does not have.**

**(O3) Index surplus and fibre cost are the same number.** For any
`Phi_N : I_N -> C_N`, `#I_N <= n_N · max fibre` identically
(`JOINT_INVERSE_ATTEMPT.md` Theorem 5). So `(AMP*)`'s two hypotheses are not
independent, and satisfying it requires knowing `#I_N >= 2^{(g+delta)N}` from the
index set's own construction, never by counting its image. A persistent seed
supplies one orbit = one word = `O(N)` digits per depth; rewriting `O(1)` digits
buys `poly(N)` (Theorem 4), and buying `2^{delta N}` requires rewriting
`Omega(N/log N)` digits, at which point the map is a re-enumeration of `C_N` and
(O1) applies. **Gap: `poly(N)` against `2^{delta N}`.**

**(O4) The spectral seed does not exist.** Proposition 4.3 needs
`H = log(1/||K||) > 1`, obtained in Lemma 4.4 from `rho < 1`, i.e. from
**nonamenability**. Every kernel with row and column sums `1` on a **finite**
set has `||K||_{l^2} = 1` exactly (`ASYMPTOTIC_BUDGET.md` Proposition S), and the
EOC state space at depth `N` must be the finite residue space for `p(N,c)` to
mean what the rate says. Leaving it for an infinite space discards `mu`, `Q_N`
and the rate itself.

**(O5) Polynomial heaviness is available in the aggregate and not pointwise.**
In the paper's currency (`pi >= n^{-beta}`, `beta < 1/2` forced by `beta+s<1`),
the whole confined population has `beta_eff = I_0 = 0.0793 < 1/2` and **would**
finance the construction; one seed's cylinder has `beta_eff = alpha = 1.5850`
and does not, short by `n^{1.085} = 2^{1.085 N}`
(`ASYMPTOTIC_BUDGET.md` §3). **Exponential, not a constant.**

**(O6) The architecture is aggregate-to-aggregate.** The paper's hypothesis
(4.1) is about a measure and its conclusion contradicts that same measure; it
never passes from an aggregate to an individual. The EOC target is one fixed
integer. This obstruction is independent of all of (O1)–(O5) and would survive
their repair.

## 3. Imports explicitly refused

The brief forbids a list; each is recorded as not used.

* **Independent suffixes after conditioning on a shared realizer** — not used.
  The sibling suffix sets are coordinates of the branch node, not independent
  fields; the previous round recorded this ("the two suffix sets are
  *independent* coordinates of the node, not successive terms of a single sum").
* **Uniform random orbit anchors** — not used. Every seed here is an explicit
  integer or an explicitly enumerated residue class.
* **Product-measure factorization for actual Collatz carries** — not used.
  Proposition W is an identity about the product law on *letter strings*, where
  the dyadic mass literally *is* that probability; it is never applied to a
  particular orbit, and §5 of `ASYMPTOTIC_BUDGET.md` says so explicitly.
* **Measure-preserving swaps without an exact accounting identity** — not used.
  Here the exact accounting identity exists (Theorem B) and it says the swap is
  mass-neutral, which is (O1).
* **Mixing or spectral gaps from symbolic growth alone** — not used; (O4) proves
  the opposite for the relevant kernels.
* **The paper's conditional-independence step** — not imported. The paper itself
  confines it to a reference experiment invoked *after* its injective
  comparison, and there is no injective comparison here to invoke it after.

## 4. Circularity checks

* **Is `(AMP*)` circular?** No — but it is also not a reduction unless the index
  set is constructed independently of `C_N` (O3). Stated without that
  requirement it is a restatement.
* **Does Proposition W prove anything pointwise?** No. Asserting that a fixed
  orbit's valuations follow the Geometric(1/2) law is the open Tao-type input.
  The identity is exact at the level of the sum over all words and carries no
  pointwise content.
* **Does Theorem B smuggle in the rate?** No. Theorem B is an exact finite
  identity (`mu(C_N) = p(N,0)`) proved from `leastRealizer_unique` and verified
  by brute force at `N <= 14`. The rate is imported separately and only from
  `confined_mass_rate`.
* **Does the `r_min` picture of §5 assume equidistribution?** No — it *measures*
  it, and the measurement is the finding.

## 5. Routes that reduce to previously closed work — reported promptly

* The recombination transformation **is** the object of **Theorem D** of
  the growing-scale-pairs round (local scratch, not published), and its residual is
  that round's "near-solution count for a two-set difference equation between
  two shifted confined-realizer sets". That round's **Theorem E** is a proved
  power-law barrier: every bound of the derivable shape
  `U_N(x) <= C N^B n_N (2x)^{1-c}` yields localization exponent
  `>= 2alpha - g - I_0 = alpha` *identically*, because `g = alpha - I_0`. The
  present round adds a new and independent reason to stop (O2, O3) but does not
  evade that barrier, and does not retry the three things ruled out for it
  (per-pair absolute values; per-pair `O(1)` errors; any pure power of `|J|`).
* **Symbolic word production is already closed.** There are uncountably many
  zero-confined *words* whose drift tends to `-infinity` that satisfy every word
  shadow and are nonetheless **unrealizable**. Making more words is free and
  worthless; only realizers count, and (O2) caps those.
* **The `r_min` route is the target itself.** Lemma T of
  `EOC_DIVERGENCE_TARGET.md` §2 makes "persistent seed" literally equivalent to
  "`r_min(N,0)` bounded". Any argument that ends at `r_min` has not reduced
  anything.

**Fairness note.** All of these closures apply to their precise formulations.
None of them is an impossibility claim about Fourier, combinatorial or
probabilistic methods in general, and nothing here should be read as one. In
particular (O1)–(O3) close *amplification against the confinement mass rate*;
they say nothing about a contradiction derived against a different proved
quantity.
