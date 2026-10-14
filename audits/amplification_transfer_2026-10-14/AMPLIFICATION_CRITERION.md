# AMPLIFICATION_CRITERION.md — the abstract criterion, and why it is vacuous

The brief asks that the proposed contradiction criterion be proved carefully,
with its quantifiers, **before** any transformation is attempted. That is done
here. The result is negative and it is the main finding of this investigation:
**the criterion is a true implication whose hypothesis is unconditionally
false.** It is therefore not a reduction of the divergence problem but a
restatement of it, and no arithmetic amplification mechanism can satisfy it.

Section 4 then gives the repaired criterion, which is non-vacuous, and says
exactly what it demands.

Notation and all inputs: `EOC_DIVERGENCE_TARGET.md`. Throughout,
`alpha = log_2 3`, `I_0 = alpha(1 - H_2(1/alpha)) = 0.079318612775`,
`g = alpha - I_0 = 1.505643887946`, `Q_N = 2^{sN(N)+1}`, `mu` is normalized
counting measure on the odd residues mod `Q_N`, and `C_N` is the set of
`0`-confined-to-depth-`N` odd residue classes, with `mu(C_N) = p(N,0)`
(Theorem B, exact) and `p(N,0) = 2^{-I_0 N + o(N)}`
(`Occupation.confined_mass_rate`, source-backed).

---

## 1. The criterion as proposed

> **(AMP).** Let `m` be a fixed positive odd integer whose accelerated orbit is
> `0`-confined forever. Suppose there are `eps < I_0`, `c_m > 0` and, for
> arbitrarily large `N`, families `B_N(m)` of **pairwise distinct** `0`-confined
> residue classes at depth `N` with
> ```
>    B_N(m) subseteq C_N        and        mu(B_N(m)) >= c_m · 2^{-eps N} .
> ```
> Then the confinement mass rate is contradicted, so no such `m` exists.

The implication itself is immediate, and is worth stating with its quantifiers
because the quantifier order is where the trouble is.

> **Proposition A1 (the implication).** Fix `eps` with `0 <= eps < I_0` and
> `c > 0`. If there is an infinite set `S` of depths and, for each `N in S`, a
> family `B_N subseteq C_N` with `mu(B_N) >= c·2^{-eps N}`, then
> `confined_mass_rate` fails.
>
> *Proof.* `B_N subseteq C_N` gives `mu(B_N) <= mu(C_N) = p(N,0)`, so for
> `N in S`,
> ```
>    -(1/N) log_2 p(N,0)  <=  -(1/N) log_2 ( c 2^{-eps N} )  =  eps - (log_2 c)/N .
> ```
> Along `S` the right side tends to `eps < I_0`, so
> `limsup_{N in S} ( -(1/N) log_2 p(N,0) ) <= eps < I_0`, contradicting
> convergence to `I_0`. ∎

So (AMP) is valid. The difficulty is Proposition A2.

## 2. The criterion is vacuous

> **Theorem 1 (vacuity).** Let `0 <= eps < I_0` and `c > 0`. There is **no**
> infinite set of depths `S` and no families `B_N subseteq C_N` (`N in S`) with
> `mu(B_N) >= c·2^{-eps N}` — *regardless of whether a persistent seed exists,
> and for every `m`.*
>
> *Proof.* `mu(B_N) <= mu(C_N) = p(N,0) = 2^{-I_0 N + o(N)}`, so
> `c·2^{-eps N} <= 2^{-I_0 N + o(N)}`, i.e.
> `2^{(I_0 - eps) N} <= c^{-1} 2^{o(N)}`. Since `I_0 - eps > 0` is a fixed
> positive constant, the left side grows exponentially and the right side
> subexponentially; this fails for all large `N`, so `S` is finite. ∎

Theorem 1 uses only the mass rate — no assumption about `m`, no structure of
`B_N` beyond `B_N subseteq C_N` and the classes being distinct (which is what
makes `mu(B_N)` the sum of their measures and hence `<= mu(C_N)`).

**The same statement in counting form**, which is the more useful one:

> **Corollary 1a (the hard cap).** Every family of pairwise distinct
> `0`-confined residue classes at depth `N` has measure at most
> `2^{-I_0 N + o(N)}`, and every family of pairwise distinct `0`-confined
> *words* of length `N` has cardinality at most `n_N = 2^{g N + o(N)}`,
> `g = 1.505643887946`.
>
> Consequently the demand `mu(B_N) >= c 2^{-eps N}` with `eps < I_0` is a demand
> for
> ```
>    #B_N  >=  c · 2^{(alpha - eps) N}     with     alpha - eps > alpha - I_0 = g ,
> ```
> i.e. for **strictly more confined classes than there are confined classes.**

## 3. What this means, stated carefully

(AMP) has the logical form `P => F` where `F` is unconditionally false
(Theorem 1). Such an implication is equivalent to `not P`. Therefore:

1. **(AMP) is not a reduction.** Proving it is *logically equivalent* to proving
   the divergence target outright. It decomposes nothing, and it supplies no
   intermediate statement that is easier than the goal. This is exactly the
   failure mode the brief asks to avoid — "a conditional proof whose hypothesis
   is essentially the original conjecture in different notation" — except that
   here it is the *criterion*, not the hypothesis, that is the restatement.
2. **No amplification mechanism can satisfy it, and none can be exhibited.**
   The objects `B_N` do not exist. One cannot construct them, verify them on an
   example, or compute with them. Any argument for (AMP) must be a proof by
   contradiction carried through from `P`, which leaves the actual difficulty
   untouched.
3. **It answers §4's decisive question in the strongest form.** The brief asks:
   "Does this create additional confined residue mass, or merely rearrange
   existing residues? A permutation of an existing confined population does not
   amplify its mass." Theorem 1 says more: **no injection whatsoever into the
   confined population can amplify its mass** — not permutations, not lifts, not
   renamings, not any map at all. The cap is the rate itself. Mass inside `C_N`
   is a conserved budget and `confined_mass_rate` is precisely its accounting.

**The structural reason**, in one line: `confined_mass_rate` is a statement about
the **total** confined population, and anything a single seed generates is a
**sub**population. A subpopulation cannot outweigh its parent. Any route whose
conclusion is "here are many confined objects" is capped before it starts.

## 4. The repaired criterion

To get a non-vacuous contradiction one must count something that is *not* a
subset of `C_N`, and compare it to `C_N` through a map with controlled fibres.
That is exactly the shape of Lemma 4.8 of the percolation paper, whose entire
achievement is the removal of a multiplicity factor.

> **(AMP\*) — the multiplicity criterion.** Suppose there are `delta > 0`,
> `B >= 0`, `C > 0`, an infinite set of depths `S`, and for each `N in S`
> * an index set `I_N` with `#I_N >= 2^{(g + delta) N}`, and
> * a map `Phi_N : I_N -> C_N` (or into the set of `0`-confined words)
>
> such that every fibre satisfies `#Phi_N^{-1}(y) <= C N^B`. Then
> `confined_mass_rate` is contradicted.
>
> *Proof.* `#I_N = Σ_{y} #Phi_N^{-1}(y) <= C N^B · n_N = C N^B 2^{g N + o(N)}`,
> so `2^{(g+delta)N} <= C N^B 2^{gN+o(N)}`, i.e. `2^{delta N} <= C N^B 2^{o(N)}`
> — false for large `N`. ∎

`(AMP*)` is **not** vacuous: both halves of its hypothesis are statements about
objects one can actually construct and inspect, and the content sits entirely in
the fibre bound. A fibre bound `2^{o(N)}` in place of `C N^B` suffices
identically.

**What `(AMP*)` demands of the arithmetic, itemised.** For a persistent seed `m`
to drive it, one needs

| requirement | what it means for EOC |
|---|---|
| an index set of size `2^{(g+delta)N}`, `g = 1.5056` | more than `1.5` bits of fresh choice per step of the orbit, manufactured from one fixed integer |
| the index set must **not** be a set of confined objects | otherwise Corollary 1a caps it at `2^{gN+o(N)}` and `delta <= 0` |
| `Phi_N` must land in `C_N` | the outputs must be genuine `0`-confined *integer realizers*, not merely symbolically admissible words or `2`-adic points |
| fibres `<= 2^{o(N)}` | the inverse of `Phi_N` must be reconstructible from its output plus `o(N)` bits of auxiliary data |

`JOINT_INVERSE_ATTEMPT.md` shows that the third and fourth requirements are in
direct conflict in EOC: the only maps available that land in `C_N` are already
injective, so they carry no index set larger than `n_N`; and the only way to get
a larger index set is to leave `C_N`, at which point `Phi_N` is not defined.

## 5. The one escape, and its exact price

Theorem 1 and `(AMP*)` both use the mass rate at a **fixed** confinement
parameter. If an amplification produced classes that are confined only with a
budget `c = c(N)` growing with `N`, `confined_mass_rate` does not apply, because
`c` is bound outside its limit. The brief flags this, and it is the only gap in
Theorem 1's coverage.

`ASYMPTOTIC_BUDGET.md` §6 prices it exactly: for `c = theta N`,

```
   -(1/N) log_2 p(N, theta N)  ->  J(alpha + theta) ,   J(a) = a(1 - H_2(1/a)) ,
```
for `0 <= theta < 2 - alpha`, and `-> 0` for `theta >= 2 - alpha = 0.415037…`.
So:

* **`c = o(N)` keeps the rate at `I_0`** and Theorem 1 applies verbatim (the
  `o(N)` enters the `2^{o(N)}` already present).
* **`c = theta N` with `theta > 0` strictly lowers the rate** to
  `J(alpha+theta) < I_0`, so the `eps` an amplification must beat becomes
  *smaller*, not larger. A controlled linear defect makes the target harder, not
  easier.
* **`theta >= 2 - alpha` destroys the rate entirely** (`J = 0`), but a budget
  growing at `>= 0.415` bits per step is no longer a confinement condition in
  any useful sense, and the resulting objects say nothing about zero
  confinement, which is the target.

So the escape is closed in the only direction that would have helped.
