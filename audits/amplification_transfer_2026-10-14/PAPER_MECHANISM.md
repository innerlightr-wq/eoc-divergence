# PAPER_MECHANISM.md — what the percolation paper proves, and what is borrowable

```
Nonuniqueness of percolation on nonamenable quasi-transitive graphs
OpenAI, September 24, 2026.   53 pages, A4, pdfTeX-1.40.29, LaTeX with hyperref.
file    ~/Downloads/paper.pdf        (located by title, not by filename)
size    649525 bytes
sha256  46a78d044d2713e48cb3faa9b0b9d22da9480193e2202fe63d8e0daa7d8a3dbb
```

Read firsthand in this session: §4.1–4.5 in full (Lemmas 4.1, 4.4–4.9,
Definition 4.2, Proposition 4.3) plus §1.2, §2.2–2.5, and the statements opening
§5–§9. Sections read are quoted below only to the extent needed to state what is
and is not transferable. **Nothing in this paper proves anything about Collatz,
and nothing below claims it does.**

---

## 1. What the paper proves

Headline: every infinite connected, locally finite, nonamenable quasi-transitive
graph has a nonempty interval of `p` for which Bernoulli bond percolation a.s.
has infinitely many infinite clusters — the Benjamini–Schramm nonuniqueness
conjecture — and Hutchcroft's stronger operator-threshold conjecture
`p_c < p_{2->2} <= p_u`.

The architecture relevant here is a **proof by contradiction against a heavy
tail**. Under the temporary assumption

```
   (4.1)        E_{p_c}[ s_o^alpha ] = infinity     for some 0 < alpha < 1/2 ,
```
`s_o` the cluster size at the root, §4 manufactures very efficient *local
endpoint maps*, and §5–§9 show that such maps force susceptibility growth and
spectral deformation that contradict (4.1). The quantity being amplified is an
**operator norm**.

## 2. The amplification engine, as actually written

**Definition 4.2.** A *local endpoint map* on a vertex orbit `O` is a randomized
rule at each `x in O` reading percolation bits in a deterministic finite ball
about `x`, plus auxiliary randomness independent of those bits, covariant under
automorphisms, outputting `y in C_x ∩ O` or failing; with integer cap `M` it
requires `s_x <= M` and `C_x` good for cap `M` on every successful pattern. Its
parameters are

```
   u = success probability,   K(x,y) = P(output y | success at x),   r = ||K|| ,
   U = log(1/u),   m = log M,   H = log(1/r) .
```
Invariance makes `u` independent of `x`; `K` has row sums one, and **transport
restricted to `O x O` gives column sums one as well**, so `0 < r <= 1`.

**Proposition 4.3.** Under (4.1), for every `eta > 0` there is such a map with
`M >= 2`, `H > 1` and `(U+m)/H < eta`, and `H` can be driven to infinity.

**Lemma 4.4 (the seed).** Start from a length-`ℓ` walk with kernel `P`,
requiring all distinct traversed edges open. Before the cluster cap the endpoint
mass kernel is exactly `p_c^ℓ P^ℓ|_{O x O}`, with row sum `>= c_1 p_c^ℓ` and
norm `<= p_c^ℓ ρ^ℓ`. Fixing `ℓ` with `2ρ^ℓ/c_1 < e^{-1}` gives `r <= 2ρ^ℓ/c_1
< e^{-1}`, i.e. `H > 1`.

> **This is where nonamenability enters, and it is the only place the seed comes
> from.** `ρ < 1` is the spectral radius of the symmetric walk of §2.4, which
> exists *because* the graph is nonamenable. On an amenable graph `ρ = 1` and
> Lemma 4.4 yields nothing.

**§4.2 (splicing).** Fix an old map `(u,M,r)`, `k >= 1`, a scale `n` with
`kM <= n/2`. In a **distinguished independent field `D`** require
`A = C_x(D)` with `n <= |A| < 2n`; **independently**, from `z` take `k` old-map
steps, *each using a new independent percolation field and new seeds*. A
switching procedure then exchanges `D` and `E_i` bits on explicit masks,
inserting a chain of pieces `B_i` each attached by a single open bridge `e_i`
(Lemma 4.5), yielding `z in C_x(D')` with `s_x(D') <= M' = 2n + kM`.

**§4.3 (coding the inverse).** Lemma 4.6: a valid switching input is specified
by the selected indices and the positive gaps locating the seams among the
bridges separating `z` from `x`; each code determines at most one input tuple;
after integrating the fresh contact uniforms the total mass of valid codes is at
most `W^k` with `W = 1 + Σ_{l<=M} min{1, 2M^s/l} <= C M^s log M`. The *load*
`L_x(z,D')` is the density of the switched mass at `z`, and
`0 <= L_x(z,D') <= W^k/n`.

**§4.4 (Lemma 4.8 — the technique the brief asks about).** `E L^2 <= Q(k,M) π
u^{2k}` for a fixed polynomial `Q`. The proof splits `L^2` into three classes.
The decisive one is *hanging components disjoint and graph-nonadjacent*, where

> "joint undoing is injective **without retaining either code**. This stronger
> assertion removes the factor `W^{2k}` from this class."

Its proof needs, in order:
1. **disjointness of the exchange masks**, which follows from *graph*
   nonadjacency of `B^1, B^2` — not merely from disjointness of the components;
2. **exact probability preservation**: "at fixed seeds, the exchanges preserve
   the total number of open bits among equally distributed fields", so each
   input tuple and its output have *exactly* the same product probability;
3. a **replay** argument: running the forward switching procedure from the
   jointly restored field reselects the same index, component, contact and mask,
   proved by induction using graph nonadjacency at each step;
4. a final **reference product experiment** in which the two old chains are
   conditionally independent given the root cluster — and the paper is explicit
   that this independence "is invoked in this reference experiment only, after
   the injective comparison."

**§4.5 (Lemma 4.9, iteration).** One step gives `u' >= c'π/Q(k,M)`,
`r' <= 2 r^k`, `M' = 2n + kM`. With `t = U + (s+ξ)m` the proof of Prop. 4.3
obtains `U' <= k(β+ξ)t`, `m' <= k(1+ξ)t`, `H' >= k(1-ξ)H`, hence
`t'/H' <= c_ξ t/H` with `c_ξ = (β+ξ+(s+ξ)(1+ξ))/(1-ξ) < 1`, possible **because
`β + s < 1`** with `s = 1/2 + ε` — so `β < 1/2` is forced.

## 3. The exact accounting that makes it work

Gain and cost are both linear in `k`; the ratio contracts by a fixed factor:

```
   gain:  H' >= k(1-ξ) H           (norms multiply:  r' <= 2 r^k)
   cost:  U' <= k(β+ξ) t ,  m' <= k(1+ξ) t
   net:   t'/H' <= c_ξ · t/H ,   c_ξ < 1   ==>  (U+m)/H -> 0 .
```

`β` is the exponent in `π = P_{p_c}(n <= s_o < 2n) >= n^{-β}` from Lemma 4.1 —
the **polynomial** heaviness of the seed object. The whole construction is
financed by it.

## 4. What is borrowable, and what is not

| ingredient | status for EOC |
|---|---|
| the *shape* "efficient local maps contradict a tail/rate" | borrowable as a template; instantiated as `(AMP*)` in `AMPLIFICATION_CRITERION.md` §4 |
| **Lemma 4.8's joint inverse reconstruction** = a fibre/multiplicity bound | the *idea* (count two inverses jointly, not separately) is borrowable; `JOINT_INVERSE_ATTEMPT.md` shows there is no multiplicity in EOC to remove |
| independent percolation fields `D, E_1,…,E_k` | **not available.** There is one arithmetic world and one orbit; there is no second i.i.d. copy to splice in |
| bit-count-preserving exchange giving *exact* equality of probabilities | **not available.** Its analogue would be an exact measure-preserving bijection between confined populations, which `AMPLIFICATION_CRITERION.md` Theorem 1 shows cannot increase mass |
| invariant mass transport (`O x O` column sums one) | partially: the dyadic mass has an exact transport identity (`Theorem B`), but it *caps* rather than finances |
| spectral gap `ρ < 1` from nonamenability | **not available.** `ASYMPTOTIC_BUDGET.md` §4 proves `||K|| = 1` for every doubly stochastic kernel on the finite residue space |
| conditional independence of the two chains in the reference experiment | **not importable.** The brief forbids it and the paper itself confines it to a post-injection reference model |
| polynomial heaviness `π >= n^{-β}`, `β < 1/2` | available **in the aggregate** (`β_eff = I_0 = 0.0793 < 1/2`), **not pointwise** (`β_eff = alpha = 1.585`). This is the quantitative statement of the gap — `ASYMPTOTIC_BUDGET.md` §5 |

## 5. One honest observation about the paper's own structure

The paper's contradiction is against a **heavy tail of a random variable under a
product measure**. Its hypothesis (4.1) is a statement about a *measure*, and
its conclusion contradicts that same measure. The EOC target is **pointwise**:
one fixed integer. The paper never has to pass from an aggregate to an
individual, because its conclusion is itself aggregate. That asymmetry is not a
detail of constants — it is the reason the architecture does not transfer, and
it is independent of every other obstruction listed above.
