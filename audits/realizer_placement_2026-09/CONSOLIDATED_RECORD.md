# Consolidated record — realizer placement beyond the fresh-bit boundary

Scratch `~/scratch/collatz-prefix-suffix-20260926-215500/` (this round) and
`~/scratch/collatz-partial-counting-20260926-205246/` (the audit round).
**Overall verdict: USEFUL LOCAL LEMMA, GLOBAL GAIN STILL OPEN.**

Three status classes are kept strictly apart below. Nothing is Lean-verified; no novelty is claimed
for the rotation, entropy, or cycle-lemma arguments.

**Nine statements is not nine novel results.** Correctness, role in this programme, and novelty
relative to the literature are three separate questions; only the first two are addressed here. A1
and A8 are refinements of classical parity-vector/lcp facts (Terras 1976, Everett 1977,
Lagarias 1985, Bernstein 1994); A5 is a cycle-lemma argument in the Dvoretzky–Motzkin tradition; A4
and A9 are elementary counting. No literature search for priority was conducted.

---

## A. Paper proofs (DERIVED HERE, argument written out, finitely cross-checked)

| # | statement | cross-check |
|---|---|---|
| A1 | **Independent failure offset.** `t*_w ≡ −((3x_w+1)/2)·3^{−(N+1)} (mod 2^K)`, from `3m_N(t)+1 = 2(y + 3^{N+1}t)` with `x_w` odd; and `K = ⌊(N+1)α − S⌋ ≥ 1` on every confined word. | 311,844 cylinders, 0 offset disagreements; `K<1` in 0 of 12,447 words |
| A2 | **Exact top-block split at any split point.** `T_w = (P_hi(u) + Q_hi(v) + c) mod 2^d`, `c = ⌊(P_lo+Q_lo)/2^B⌋ ∈ {0,1}`, and `r_w mod 2^B = (P_lo+Q_lo) mod 2^B`. | 33,948,325 `(w,j)` checks, 0 violations |
| A3 | **Concatenation law.** `r_{uv} ≡ 3^{−j}(2^a r_v − C_u) (mod 2^{a+b+1})`. Not present in the Lean sources. | 14,405 word/split checks, 0 mismatches |
| A4 | **Carry-robust counting.** `T = Z + c ⟹ H(t) ≤ H₀(t) + H₀(t−1)`; `\|H₀(t) − L/q\| ≤ R = √(E_A E_B)/q` uniformly in `t`; hence `H(0) ≤ 2L/q + 2R`, `\|D\| ≤ L/q + 2R`, and `σ = min(1,τ)`. Since `σ* < 1`, an arbitrary binary carry costs only a constant. | 0 domination and 0 `R` violations over all residues and all `j`, both κ |
| A5 | **Rotation bound.** `L_s ≥ C(s−1,N−1)/N`. | 32 shells, 0 violations; ratio → 1.213 at the top shell |
| A6 | **Thin-band lemma.** With `κ=13/20`, `δ=1/10`, band `min{k,e−k} ≤ ⌊δN⌋`: `H_s^thin/(L_s/q) ≤ 2^{−γB+O(log B)}`, `γ = 1 − κ[α − Δ_δ(α)] = 0.054816179871361`, uniformly over unresolved shells — granting **every** thin word a below-cutoff realizer. Top shell is worst, proved via `d/dθ[θ−Δ_δ] = log₂[2(θ−1)(θ−½−δ)/(θ(θ−1−δ))]` and `(θ−1)²+δ(2−θ) > 0`. | exact binomial evaluation: 0.691825 / 0.0375106 / 0.000161790 / 1.72629e−09 at `B = 100/200/320/640`, argmax always the top shell |
| A7 | **Singleton characterisation.** For `ℓ ≥ 3` under `S_m ≤ αm+A`, the family is a singleton iff `b = ℓ`. Hence `\|U_a\|=1 ⟺ a=j`, `\|V_a\|=1 ⟺ b=N−j` — the two band endpoints. | 186 families, 35 singletons, 0 mismatches |
| A8 | **LCP valuation law and its collision consequence.** `v₂(r_v − r_{v'}) = S_L + min(v_{L+1},v'_{L+1}) =: t`; a high-block collision forces `t < B−a`. | 0 violations of either |
| A9 | **LCP-rejection cannot beat capacity.** With `n_z ≤ q` (distinctness) and `t < B−a ⟺ y_v ≢ y_{v'} (mod H)`, the surviving ordered-pair count is `P_LCP = n + n² − Σ_z n_z² ≥ n(n+1−q)`, while capacity gives `Σ_x h(x)² ≤ nH/2`. So **`n+1 > q + H/2` ⟹ LCP-rejection alone provably loses to capacity**, for any arrangement of low residues. | `n_z ≤ q` and the equivalence: 0 violations; `n+1 > q+H/2` in every tested bulk class, `P_LCP/capacity` = **4.50–21.15** |

## B. Finite computational checks only (no asymptotic content)

- `Q_{⌈0.65B⌉,2^B−1}` = 1.008174, 0.994797, 1.000408, 1.000816, 0.999991 at `B` = 12…28 — but
  `N` exceeds `N*(B)` by only 1–2 steps there, so this cannot separate `η = 0` from `η > 0`.
- Best finite proved constant, keeping `min` of both valid bounds on every class:
  `C = 2.0000` (κ=0.65), `C = 3.0762` (κ=0.90), at `B = 20`.
- `τ_bulk ≈ 0.9655–0.9703` at the binding shell, `B = 20`, κ=0.90.
- Exact cylinder decomposition `A_{N,M} − (X/2)p_N = Σ_{q_w>X}(1_{r_w<X} − X/q_w)`: 0 failures at
  five `(B,N)` pairs.
- The frozen band is **not** numerically effective at `B = 20` (`γB ≈ 1.1` bits against `O(log B)`).
  **Presentation safeguard:** A6's asymptotic conclusion rests on the analytic proof *together with
  uniform control of the remainder*; the exact evaluations at `B = 100, 200, 320, 640` **cross-check
  the finite bound** and nothing more. They do not establish validity for every `B ≥ 100`, and they
  do not identify `100` as a threshold. Asserting `B₀ = 100` in
  `H_s^thin ≤ C·2^{−B/20}·L_s/q  (B ≥ B₀)` would require a further explicit bound on the
  `O(log B)` term, which is not supplied here.

## C. Open

> **(\*)** `Σ_{a ∈ bulk} L_{s,a}√(χ_{U,a}χ_{V,a}) ≤ C(B+1)^p·L_s·q^{1/25}`, `C,p` independent of `B`
> and of the permitted shell, with the suffix constrained only by its inherited corridor
> `S_v(m) ≤ αm + A`, `A = αj − a`. This is a **weighted** requirement: a few unfavourable classes
> are acceptable if their weights are controlled, and a favourable representative class establishes
> nothing.

Conditional payoff, verified to 4.8e−16: exponent `1 − I₀κ + η = 0.949651926715094` with
`η = (ακ−1)/25 = 0.001209025018750`, against baseline `H₂(1/α) = 0.949955527188331` — an improvement
of **0.000303600473237**, delivered through
`ResidueDiscrepancy.exceptional_count_le_of_leastRealizerBound` (`hC : 1 ≤ C`, upper count against
cylinder mass) with **no** absolute-value Weyl hypothesis.

**No improvement to the exceptional-set exponent has been obtained.**

## D. What A9 tells the next attempt

`LCP law → exact divisibility of a difference`; the estimate needs `which pairs share an ordinary
interval`. A9 shows that bridging them by counting everything satisfying the divisibility-necessary
condition is *provably* insufficient at these cardinalities. A new ingredient must constrain the
**location or magnitude** of the transformed difference, or how the family populates intervals.

Two places where a relation might exist, neither a mechanism yet:
- the **full carry equations** relating `r_v` across a class — distinct from the binary top-block
  carry of A2/A4, which is already settled, so this is not reopening that;
- the **inherited corridor `A`** used as an active arithmetic constraint rather than a side
  condition.

## E. Identified next action, not attempted here

Targeted formalization of the established reductions. Formalization-ready, in dependency order:
**A7** (singleton characterisation — pure combinatorics on `Fin ℓ → ℕ`), **A4** (two-class
domination plus Parseval/Cauchy–Schwarz — the Fourier machinery already exists in
`ShellWeyl.lean`), **A5** (rotation bound), then **A6**.

I did not attempt a Lean build: `eoc-lean-verification` is on `v4.34.0-rc1` with 3 pre-existing
tracked modifications and 50 untracked files, and I have not validated its current build state, so I
cannot distinguish a pre-existing failure from one I would introduce. That check should precede any
formalization.
