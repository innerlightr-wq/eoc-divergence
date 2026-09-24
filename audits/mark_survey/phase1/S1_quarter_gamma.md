# Phase 1 — S1. Shared quarter-gamma lattice / Thales–Ramanujan (the 1/π ghost)

Reading only. No computation was run. Labels: PROVED / CITED / HEURISTIC / OPEN.

## Summary (5 lines)

The note compares two objects that share the residue lattice {1/4, 1/2, 3/4} (mod 1):
Ramanujan's coefficient A_n = (4n)!/(n!)^4, whose generating function is
3F2(1/4,1/2,3/4; 1,1; 256z) and which factors by Clausen as 2F1(1/8,3/8;1;256z)^2,
and the Thales beta family J(s) = ∫_0^1 [a(1-a)]^s da = B(s+1,s+1) = Γ(s+1)²/Γ(2s+2).
It proves that J's arithmetic type depends only on s mod 1 (four strata), that the
quarter stratum is a lemniscatic period, and that conjugate strata multiply to a
rational multiple of π by Euler reflection. Its thesis is explicitly negative and
organizational: the shared lattice is **not a mechanism**, and the modular data that
actually produces 1/π (singular moduli, multipliers, Legendre relation, quasi-periods)
is absent — with the Clausen failure turned into a demonstrated no-go in Appendix A.2.

## The transient / disappearing 1/π structure, located

**One sentence.** In each individual conjugate stratum a transcendental CM period
appears — J(1/4) = (1/3)K(1/√2), with J(3/4) proportional to its reciprocal — and that
period **disappears** under the reflection involution s ↦ 1−s (the conjugate-stratum
*product*, not a depth limit), leaving behind only an algebraic residue: a rational
number times cot(πs), i.e. π/20 at the self-complementary residue s = 1/4.

### What appears

- p. 2, eq. (11) [PROVED, Lemma 2 + Γ-recurrence, proved p. 3]:
  > "J( 1/4 ) = Γ(1/4)² / (12 √π),   J( 3/4 ) = 3 Γ(3/4)² / (10 √π)."
- p. 2, eqs. (7)–(10) [PROVED]: the stratum law. Because
  "J(s + 1)/J(s) = (s + 1)/(2(2s + 3)) is rational in s … the arithmetic nature of J(s)
  is governed by the residue of s modulo 1", giving s ∈ Z ⟹ J ∈ Q; s ∈ Z+1/2 ⟹ J ∈ Qπ;
  s ∈ Z+1/4 ⟹ J ∈ Q·Γ(1/4)²/√π; s ∈ Z+3/4 ⟹ J ∈ Q·Γ(3/4)²/√π.
- p. 3–4, eqs. (14)–(15) [PROVED here, period value CITED to Whittaker–Watson,
  Borwein–Borwein]: K(1/√2) = Γ(1/4)²/(4√π), hence
  > "J( 1/4 ) = (1/3) K(1/√2),   J( 3/4 ) = 3π / (20 K(1/√2))."
  p. 4: "the quarter Thales stratum is a lemniscatic gamma layer … only the period
  K(1/√2), equivalently the CM period Γ(1/4) of the elliptic curve y² = x³ − x with
  complex multiplication by Z[i]."

### What disappears, and under what operation

- p. 3, Proposition 1, eq. (12) [PROVED]:
  > "J(s) J(1 − s) = π s(1 − s) cot(πs) / (2 (2s + 1)(1 − 2s)(3 − 2s))",
  and eq. (13), "since cot(π/4) = 1":  J(1/4) J(3/4) = π/20.
  The proof cancels Γ(s+1)Γ(2−s) against Γ(2s+2)Γ(4−2s) by Euler reflection.
- p. 4, immediately after (15) [the erasure stated in the author's own words]:
  > "Thus J(1/4) is proportional to the lemniscatic period K(1/√2) and J(3/4) to its
  > reciprocal; **the product identity (13) eliminates the period and returns π/20.**"
- p. 3, Remark 1: "The collapse (13) to a rational multiple of π is a manifestation of
  Euler reflection: in the product the values Γ(1/4) and Γ(3/4) cancel through
  Γ(1/4)Γ(3/4) = π√2. The distinguishing feature of the quarter case is that 1/4 is the
  self-complementary residue, cot(π/4) = 1."

So the operation under which the structure vanishes is **pairing with the complementary
stratum**, i.e. the reflection s ↦ 1−s. What is erased is the transcendental period
(the only stratum-individuating datum); what survives is algebraic — a rational
prefactor and cot(πs).

### The same appearance/erasure one level up (derivative layer)

- p. 4, eq. (18), Lemma 4 [PROVED]: the mirror tilt A_s(α)/I_s(α) = α/(s+1), which p. 5
  notes "is algebraic in (s, α) **even when the normalizing mass I_s(α) lies in a
  transcendental gamma stratum**" — a normalized quantity that survives but forgets the
  stratum.
- p. 5, eq. (19) [PROVED]: the honest response ∂_α log I_s(α) = ψ(s+α+1) − ψ(s−α+1),
  which *is* transcendental.
- p. 7, eq. (23) [PROVED via Gauss digamma, CITED]: ψ(3/4) − ψ(1/4) = π — "the genuine
  first-order parameter response of the beta family reproduces π through reflection of ψ,
  structurally the same reflection phenomenon as the conjugate-stratum collapse".
- p. 7–8, eq. (24): ψ'(1/4) = π² + 8G, so Catalan's G "enters one derivative deeper",
  at second order. Hierarchy: π at order 1, 2 − 2 log 2 on the diagonal, G at order 2.

### Why the structure is a *ghost* and not a route to 1/π (the paper's own no-go)

- p. 7, Proposition 3 [PROVED; a demonstrated negative]: G_beta(z) = Σ J(n) z^n =
  2F1(1,1;3/2;z/4) and G_arc(z) = Σ 4^{-n} C(2n,n) z^n = (1−z)^{−1/2} = 1F0(1/2;;z);
  neither satisfies the Clausen condition c = a + b + 1/2 (G_beta has c = 3/2 where the
  condition demands 5/2; for G_arc the condition does not apply and the square
  (1−z)^{−1} "carr[ies] no modular content"). Hence "the Clausen square that underlies
  (1) does not arise from any single-measure Thales moment generating function."
  Repo `README.md` qualifies the scope: it is a negative "for those functions",
  "*not* a proof that every conceivable construction is ruled out".
- p. 6–7, Prop. 2 and Remark 2 [PROVED]: J(1/3)J(2/3) = π√3/35 and J(1/6)J(5/6) =
  15π√3/512, so the construction reaches a **second** CM field Q(√−3) at no cost. The
  obstruction therefore "lies one level deeper: in every stratum, in either field, π is
  produced by reflection and never by the Legendre relation, and no stratum supplies the
  multiplier or quasi-period response".
- p. 4, on the arcsine witness: A_n = C(4n,2n) C(2n,n)² (eq. 17) and each central
  binomial is an arcsine moment (Lemma 3, eq. 16) — but "A product of three moments is
  not itself a moment", so this is a witness, not a generator.

## Candidate marks G extracted from this paper (one sentence each)

- **G1 (period residue / the primary candidate).** G = the transcendental CM period
  carried by a single stratum, J(1/4) = (1/3)K(1/√2) = Γ(1/4)²/(12√π); computed as one
  beta integral at a quarter residue; it "leaves a mark" in the sense that it survives
  inside any *unpaired* stratum but is annihilated the moment it is paired with its
  complement.
- **G2 (reflection residue).** G = the value of J(s)J(1−s) divided by its rational
  prefactor, i.e. the surviving π·cot(πs); computed by pairing conjugate strata; it
  survives the erasure of the period and is the only thing that does.
- **G3 (stratum class).** G = the residue s mod 1 read off from which transcendence
  field J(s) lands in (Q, Qπ, Q·Γ(1/4)²/√π, Q·Γ(3/4)²/√π); computed by identifying the
  field of a limit value; it marks a Z/4-valued invariant that normalization by rationals
  cannot erase.
- **G4 (normalized tilt).** G = A_s(α)/I_s(α) = α/(s+1); computed as a normalized first
  coordinate moment; it survives normalization exactly and is algebraic — the paper's own
  example of a quantity that survives but *forgets* the transcendental stratum.
- **G5 (parameter-response order).** G = the least order k at which ∂_α^k log I_s(α)
  leaves the rationals, with the observed hierarchy π (k = 1), G (k = 2); computed by
  differentiating the log-normalizer in the deformation parameter; it marks a family by
  *where* transcendence first enters rather than by a value.
- **G6 (Clausen defect).** G = c − (a + b + 1/2) for the hypergeometric parameters of an
  orbit's moment generating function; computed from the generating function's parameters;
  it is an exactly-zero/nonzero invariant that separates objects with a modular square
  root from those without.

OPEN: whether any of G1–G6 has an analogue computable along a Collatz orbit at all.
That is the Phase 2 question; nothing in this paper asserts one.
