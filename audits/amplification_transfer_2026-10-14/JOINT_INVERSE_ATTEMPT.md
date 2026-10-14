# JOINT_INVERSE_ATTEMPT.md — the transformation, and the multiplicity accounting

The brief's eight required questions, answered in order, with the attempted
transformation written out and its inverse multiplicity computed. The outcome is
negative and the reason is structural: **the multiplicity that Lemma 4.8 exists
to remove does not exist in EOC.**

---

## 1. The candidate transformation, written out

The only operation available that preserves finite-depth confinement and acts on
genuine integer realizers is **prefix/suffix recombination at a branch node**.
It is already the object of the previous round's Theorem D
(`the growing-scale-pairs round (local scratch, not published)ARITHMETIC_PROOF_ATTEMPT.md`
§5), recovered rather than reconstructed.

Fix a depth `N`. For a `0`-confined word `w` of length `N` write `S_w = S_N(w)`
and let `r_w in [0, 2^{S_w+1})` be its unique least realizer
(`leastRealizer_unique`). Fix a branch node: a common prefix `P` of length `j`
with sum `S_j`, and two continuations. Theorem D, verified on all `14 878` pairs
at `N = 8` and all `461 280` at `N = 10` with 0 violations, states

```
   u_w = r_{P||e} + 2^{sigma} c ,   u_{w'} = r_{P||e'} + 2^{S_j+e'} c' ,
   sigma = S_j + e ,   beta = r_{P||e'} - r_{P||e} ,   v_2(beta) = sigma - 1 ,
   dt = u_{w'} - u_w = beta + 2^{sigma} ( 2^{e'-e} c' - c ) ,
```
`c, c'` ranging over the suffix realizer sets below the two children.

**The transformation `Phi`** (the EOC analogue of §4.2's splice): given a
`0`-confined word `w = P || e || t` and a *second* confined suffix `t'` drawn
from the sibling subtree, output the recombined word `P || e || t'`, and
correspondingly the realizer `r_{P||e} + 2^{sigma} c'`.

This is the closest arithmetic object to "splicing an independent cluster into a
distinguished one": the prefix plays the role of the big cluster `A`, the suffix
the role of the inserted chain, and `sigma` the role of the seam.

## 2. The eight questions

**(1) Is there a nontrivial transformation between confined arithmetic
objects?** Yes — `Phi` above, and it is nontrivial: it is not the identity and
not a relabelling of a single cylinder.

**(2) Does it preserve confinement, or introduce a controlled defect?**
Partially, with an *explicit* defect, and the defect is the whole problem.
Confinement of `P||e||t'` at positions `<= j+1` is inherited from `P||e`.
Beyond that it requires, for every `i`,

```
   S_j + e + S_i(t')  <=  alpha (j + 1 + i) + 0 ,
```
whereas `t'` was only known to satisfy the condition relative to *its own*
origin, `S_j + e' + S_i(t') <= alpha(j+1+i)`. The defect is therefore exactly
`e - e' < 0` when `e < e'`, i.e. **recombining onto the smaller first digit
*tightens* the constraint by `e' - e >= 1` bits and confinement can fail**; and
recombining onto the larger digit loosens it by `e'-e`, which is a confinement
budget drift of exactly the kind priced in `ASYMPTOTIC_BUDGET.md` §6. So `Phi`
is confinement-preserving only on the sub-family where the suffix has that much
slack, and that family is not all of the sibling subtree.

**(3) Does it preserve positive-integer realizability?** **Yes, and this is the
one genuinely good property.** The output is `r_{P||e} + 2^{sigma} c'` with `c'`
an integer realizer of `t'`, so by `realizerCongruence` the output is an actual
odd positive integer whose orbit has the recombined word. Realizability is not
merely symbolic or `2`-adic. (Verified on every confined word at `N <= 14`:
`scripts/bridge.py`.)

**(4) Can the inputs be reconstructed from the outputs plus a little auxiliary
data?** Yes, and **with no auxiliary data at all.** Given the output integer
`u = r_{P||e} + 2^{sigma} c'` and the node `(P, e)`, one recovers
`c' = (u - r_{P||e})/2^{sigma}` exactly, and hence `t'`. Reconstruction is
division. There is no code, no seam list, no gap sequence.

**(5) Can two transformations be reconstructed jointly with substantially less
multiplicity than separate inverse counting?** **The question is void here,
because separate inverse counting already has multiplicity one.** This is the
decisive point and it is a theorem:

> **Theorem 3 (there is no multiplicity to remove).** For every `N`, the map
> ```
>    { 0-confined words of length N }  ->  { odd residue classes mod 2^{S_N+1} } ,
>    w  |->  r_w ,
> ```
> is injective, and every fibre of the inverse map (residue class `->` its word)
> is a single point. In the common modulus `Q_N = 2^{sN(N)+1}`,
> `#C_N = Σ_w 2^{sN - S_w}` with the classes of distinct words **disjoint**.
>
> *Proof.* Injectivity and single-valuedness are `leastRealizer_unique`
> (`EOC/Realizer.lean` l. 478) together with `residue_pinning` (l. 543): a
> residue class determines the valuations, hence the word; a word determines
> exactly one class. Disjointness and the count are Theorem B of
> `EOC_DIVERGENCE_TARGET.md`. ∎
>
> **Verified by brute force at `N = 1..14`:** maximum fibre `= 1` at every
> depth, `#distinct (S_N, r mod 2^{S_N+1})` equal to `#words` at every depth,
> 0 violations (`scripts/bridge.py`, `results/bridge.log`).

Lemma 4.8 removes a factor `W^{2k} = 2^{Theta(k log M)}`. That factor exists in
percolation because the forward splice is **not** injective: many input bit
tuples give the same output field, so the inverse must be *coded* (selected
indices and seam gaps), and the code count is the multiplicity. In EOC the
forward correspondence is a **bijection**; the inverse is division; the code is
empty; the multiplicity is `1 = 2^0`. **There is nothing for the technique to
save.** It solves a problem EOC does not have.

**(6) Are there interacting and noninteracting classes of transformations?**
Yes, and the dichotomy is real but points the wrong way. Two recombinations at
branch nodes `(P_1,e_1)`, `(P_2,e_2)` are *noninteracting* when neither prefix
extends the other, in which case they act on disjoint digit ranges and commute —
the exact analogue of §4.4's "disjoint and graph-nonadjacent" class. They
*interact* when one prefix extends the other, the analogue of "nested". But in
percolation the noninteracting class is where the `W^{2k}` saving happens, and
by Theorem 3 there is no saving to be had; while in EOC the noninteracting class
is precisely where the two recombinations are *independent coordinates of the
node*, which is the previous round's recorded obstruction: "the two suffix sets
are *independent* coordinates of the node, not successive terms of a single sum
… the problem reproduces itself one level down."

**(7) Can the total inverse multiplicity be bounded by `2^{o(N)}` rather than
`2^{cN}`?** Yes — it is `1`. And that is exactly why the route fails: by
`(AMP*)` a fibre bound of `2^{o(N)}` is useful **only** if the index set has size
`2^{(g+delta)N}`. With fibres equal to `1`, the index set is in bijection with
its image inside `C_N`, so `#I_N <= n_N = 2^{gN+o(N)}` and `delta <= 0`. The
fibre bound and the index-set bound are the *same* bound here, and they cancel.

**(8) Does this create additional confined residue mass, or merely rearrange
existing residues?** **It rearranges.** `Phi` maps confined realizers to
confined realizers; its image is a subset of `C_N`; by Theorem 1
(`AMPLIFICATION_CRITERION.md` §2) the mass of any such image is at most
`mu(C_N) = 2^{-I_0N+o(N)}`. No duplicate counting is even possible, because by
Theorem 3 each output class is hit by at most one input. Recombination is a
partially defined **injection of `C_N` into itself**, and it creates nothing.

## 3. Why the independence step cannot be imported

Lemma 4.8's injectivity rests on an exchange that preserves the *total number of
open bits* between two **identically distributed independent fields**, so input
and output have exactly the same product probability. The EOC analogue would
require a second, independent copy of the arithmetic from which to draw a suffix
whose realizer is *not already* a realizer of this arithmetic. There is no such
copy: the sibling subtree's suffixes are suffixes of the same confined tree, and
their realizers are already counted in `C_N`. Formally, the "exchange" is
`c |-> c'`, a bijection between two subsets of `C_N`, and
`mu(image) <= mu(C_N)` with equality only for a bijection of `C_N` onto itself.
The brief's prohibition on "measure-preserving swaps without an exact accounting
identity" is therefore not merely a methodological caution here: the exact
accounting identity exists (Theorem B), and it says the swap is mass-neutral.

## 4. Does this reduce to a previously closed argument?

Partly yes, and it is reported promptly as the brief requires.

* The transformation `Phi` **is** the object of Theorem D of the growing-scale
  pair round. Its residual is a "near-solution count for a two-set difference
  equation between two shifted confined-realizer sets", and the round's
  Theorem E is a proved **power-law barrier**: every bound of the derivable shape
  `U_N(x) <= C N^B n_N (2x)^{1-c}` yields localization exponent
  `>= 2alpha - g - I_0 = alpha` identically, because `g = alpha - I_0`. The
  present route adds a *new* reason to stop short of that barrier (Theorem 3,
  no multiplicity) but does not evade it.
* The attempt to manufacture new confined words symbolically is closed
  independently: the repository's word-shadow analysis establishes that there
  are uncountably many zero-confined *words* with the drift going to `-infinity`
  which satisfy every word shadow and are nonetheless **unrealizable**. So word
  production is free and worthless; only realizers count, and Theorem 3 caps
  those.
* The three things already ruled out for the pair count — absolute values per
  pair, per-pair `O(1)` errors, and any pure power of `|J|` — are not retried
  here.

## 5. What was refuted, deliberately, on exact examples

**A claim of mine was refuted by the first exact test and is corrected here, not
redefined.** I first asserted that the recombination defect should be charged to
the *smaller* first digit, and that this would fail for most suffixes. Both
halves were wrong, and the direction was backwards.

`scripts/recombine.py` enumerates every branch node `(P, e<e')` of the depth-`N`
confined tree and every suffix, exactly, for `N = 3..12`:

| `N` | conf. words | nodes | down-shifts `e'->e` | survive | rate | up-shifts `e->e'` | survive | rate | max defect |
|---|---|---|---|---|---|---|---|---|---|
| 4 | 7 | 5 | 9 | 9 | **1.0000** | 13 | 9 | 0.6923 | 1 |
| 8 | 173 | 106 | 562 | 562 | **1.0000** | 1194 | 562 | 0.4707 | 4 |
| 12 | 8045 | 4195 | 46723 | 46723 | **1.0000** | 115897 | 46723 | 0.4031 | 6 |

* The **down-shift** (recombining a suffix onto the *smaller* digit) is **total
  and defect-free at every `N`**, survival rate exactly `1.0000`. The reason is
  one line and I had it inverted: lowering a digit lowers *every* later partial
  sum, so `2^{S_i} <= 3^i` is inherited automatically. There is no defect to
  control.
* The **up-shift** is the one that fails, at rate `0.40–0.69`, with a
  confinement budget defect growing roughly like `N/2` (`1,1,2,2,3,4,4,5,5,6`).
* My worked "smallest example" was fabricated: at `N = 4` the root has a
  **single** child (every `0`-confined word of length `4` begins with `d_1 = 1`),
  so the node `(P = (), e = 1, e' = 2)` I described does not exist.

So the transformation is *better* than I claimed — it is total, defect-free and
realizability-preserving — and it still fails, for a different and much more
instructive reason, which is §6.

## 6. The real accounting: index surplus and fibre cost are one number

Instantiate `(AMP*)` with the down-shift. Take

```
   I_N = { (P, e, e', t) : e < e' both children of P, P||e'||t 0-confined } ,
   Phi_N(P,e,e',t) = P||e||t  in  C_N      (total, by the paragraph above).
```

`scripts/fibres.py` measures `#I_N`, `n_N`, and every fibre exactly:

| `N` | `n_N` | `#I_N` | `#I_N/n_N` | `delta_N` | max fibre | `log2(maxfib)/N` |
|---|---|---|---|---|---|---|
| 8 | 173 | 562 | 3.249 | 0.21247 | 17 | 0.51093 |
| 10 | 961 | 4075 | 4.240 | 0.20842 | 27 | 0.47549 |
| 12 | 8045 | 46723 | 5.808 | 0.21150 | 40 | 0.44349 |
| 14 | 51033 | 350347 | 6.865 | 0.19852 | 55 | 0.41295 |

`delta_N = (log_2 #I_N - log_2 n_N)/N` looks encouragingly stable near `0.21`
over this range. **It is a finite-size artifact.** The ratio `#I_N/n_N` is
growing *linearly* in `N` (`3.25, 4.24, 5.81, 6.87` at `N = 8,10,12,14`, i.e.
about `N/2`), and `log_2(N/2)/N` varies so slowly on `8 <= N <= 14` that it
mimics a constant: it equals `0.2005` at `N = 14`, `0.0564` at `N = 100`,
`0.0090` at `N = 1000`. The max fibre `2,4,6,9,13,17,22,27,33,40,47,55` is
growing like `N^2/3.5` — polynomially.

Both observations are consequences of a bound that can be proved outright.

> **Theorem 4 (the surplus is polynomial).** For the down-shift, every fibre
> satisfies
> ```
>    #Phi_N^{-1}(y)  <=  (alpha - 1) N (N+1) / 2 ,      alpha - 1 = 0.584962500721 ,
> ```
> hence `#I_N <= (alpha-1) N(N+1)/2 · n_N = O(N^2) · n_N`.
>
> *Proof.* Index positions `1..N`. A preimage of `y` is a pair `(j, e')` with
> `e' > y_j` such that `y` with its `j`-th letter replaced by `e'` is still
> `0`-confined. Confinement of the modified word **at position `j` alone**
> already forces
> ```
>    2^{S_{j-1}(y) + e'} <= 3^j ,   i.e.   e' <= sN(j) - S_{j-1}(y) <= alpha j - S_{j-1}(y) .
> ```
> So the number of admissible `e'` at that `j` is at most
> `alpha j - S_{j-1}(y) - y_j = alpha j - S_j(y) <= alpha j - j = (alpha-1) j`,
> using `S_j(y) >= j` (every letter is at least `1`). Summing over `j = 1..N`
> gives the bound; summing over the image gives the statement for `#I_N`. ∎
>
> **Tightness, audited.** `scripts/check_thm4.py` recomputes every fibre and the
> relaxation separately. The bound holds and is tight to about `11%`: at
> `N = 10, 12, 14` the measured maxima are `27, 40, 55` against
> `32.17, 45.63, 61.42`. Moreover the position-`j`-only relaxation
> `Σ_j (sN(j) - S_{j-1}(y) - y_j)` is **exactly attained**, with value
> `27, 40, 55`, and the argmax is the all-ones word `(1,1,…,1)` at every depth —
> the word with the most confinement slack, as one would expect.
>
> **Consequence.** `delta_N <= log_2((alpha-1)N(N+1)/2)/N = O(log N / N) -> 0`.
> `(AMP*)` needs `delta >= delta_0 > 0` fixed. **The down-shift route fails by an
> exponential margin, not a constant.**

## 7. Why this is not a defect of one transformation

> **Theorem 5 (surplus = fibre, identically).** For *any* map
> `Phi_N : I_N -> C_N` (or into the confined words),
> ```
>    #I_N  =  sum_{y in Im Phi_N} #Phi_N^{-1}(y)  <=  n_N · max_y #Phi_N^{-1}(y) ,
> ```
> so `delta_N <= (log_2 max fibre)/N` always. `(AMP*)`'s two hypotheses —
> a large domain and small fibres — are therefore not independent: they are
> upper and lower bounds on the *same* quantity, separated only by `n_N`.
>
> *Proof.* Counting. ∎

Theorem 5 is why the route is closed in general rather than for this one `Phi`.
To satisfy `(AMP*)` one must know `#I_N >= 2^{(g+delta)N}` **independently of the
confined population** — from the index set's own construction, never by counting
its image. And the only resource a persistent seed supplies is *one orbit*: at
depth `N` that is one word, one residue class, and `O(N)` digits of data.
Theorem 4 is the general shape of what `O(N)` digits buy when you are allowed to
rewrite **one** of them: a quadratic factor. Getting `2^{delta N}` requires
rewriting `Omega(N/log N)` digits, and a map that rewrites that many digits and
still lands in `C_N` is, by Theorem 3, just a re-enumeration of `C_N`, whose
total size is `n_N` — the cap again.

**So the gap between what a persistent seed provides and what `(AMP*)` consumes
is `poly(N)` against `2^{delta N}`. That is the whole of the failure, and it is
exponential.**
