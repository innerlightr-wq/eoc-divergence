# TWO_RUN_FLOOR.md

`α = log₂3`, `n = q+v`, `S = u+n`, `c := 1 − 2^{q−1} + 2^n`. The word is
`1^u q 1^v` with `q ≥ 2`, `u,v ≥ 0`, **both ones-runs maximal** (the first
automatically, since it is followed by `q ≥ 2`; the second by requiring the next
letter `≥ 2`).

---

## 1. The input, from the published Theorem D

[`episode_classification_2026-10-14/RUN_ARITHMETIC.md`](../episode_classification_2026-10-14/RUN_ARITHMETIC.md)
§5 proves: an odd `m` realizes `1^u q 1^v` **iff** `m+1 = 2^{u+1}A` with `A` odd
and `Z := 3^{u+1}A` satisfying
```
   Z ≡ 1 − 2^{q−1}  (mod 2^{n}) ,      Z ≢ 1 − 2^{q−1}  (mod 2^{n+1}) .
```

> **Corollary D′ (a restatement).** Those two conditions together say exactly
> ```
>    3^{u+1}A ≡ c  (mod 2^{n+1}) ,       c = 1 − 2^{q−1} + 2^n ,
> ```
> because "`v_2(Z − 1 + 2^{q−1}) = n` exactly" is the same as
> "`≡ 2^n (mod 2^{n+1})`". So `A` lies in a **single** residue class mod `2^{n+1}`,
> and with `A*` its least positive representative,
> ```
>    r(1^u q 1^v) = 2^{u+1}A* − 1 ,       0 < A* < 2^{n+1} .
> ```

**[V]** `r = 2^{u+1}A* − 1` reproduces the word and equals the brute-force
minimum on all 120 triples `u<6, 2≤q<6, v<5` — 0 failures.

The bit accounting is therefore completely transparent:
`log₂(r+1) = (u+1) + log₂A*` with `0 ≤ log₂A* < n+1`. The first run costs exactly
`u+1` bits; the rest of the word costs a modulus of `n+1` bits; the generic size
is `S+2`. **The run structure fixes the bit count and says nothing about the
placement `A*/2^{n+1} ∈ (0,1)` — that is the whole difficulty.**

## 2. Theorem U

> **Theorem U (unconditional).** For all `u ≥ 0`, `q ≥ 2`, `v ≥ 0`:
> ```
>    log₂(r+1)  ≥  max( u+1 ,  S − (u+1)·log₂3 )  ≥  S/(1 + log₂3) ,
> ```
> hence
> ```
>    r(1^u q 1^v) + 1  ≥  2^{(log₆2)·S} ,      log₆2 = 1/log₂6 = 0.38685280723… ,
> ```
> with **no error term and no hypothesis of any kind.**
>
> *Proof.* Two bounds on `A*`.
> **(i)** `A*` is odd (if it were even, `3^{u+1}A*` would be even, but
> `c` is odd for `q ≥ 2`), hence `A* ≥ 1`, hence `log₂(r+1) ≥ u+1`.
> **(ii)** `3^{u+1}A* > 0` and `≡ c (mod 2^{n+1})` with `0 < c < 2^{n+1}`, so the
> least positive member of that class is `c` itself and `3^{u+1}A* ≥ c`. Since
> `v ≥ 0` gives `q ≤ n`, we have `2^{q−1} ≤ 2^{n−1}` and therefore
> `c = 1 − 2^{q−1} + 2^n > 2^{n−1}`. Hence `A* > 2^{n−1}/3^{u+1}` and
> `r+1 = 2^{u+1}A* > 2^{u+n}/3^{u+1} = 2^{S}/3^{u+1}`, i.e.
> `log₂(r+1) > S − (u+1)α`.
> Bound (i) is increasing and (ii) decreasing in `u`, so with `b = (u+1)/S` the
> maximum is `S·max(b, 1 − bα)`, minimised where `b = 1 − bα`, i.e.
> `b = 1/(1+α)`, with value `S/(1+α)`. ∎

**[V]** Every step — `c > 2^{n−1}`, `3^{u+1}A* ≥ c`, bound (ii) in exact
integers, and the conclusion — verified over `u<14`, `2≤q<10`, `v<26` (2912
triples): **0 violations**. Worst observed `log₂(r+1)/S = 0.400000` at
`(u,q,v) = (1,4,0)`, just above the floor `0.386853`.

**Constant audit.** `1/(1+log₂3) = 1/log₂6 = log₆2`; the two bounds meet exactly
and there is no additive slack to lose, which is why the statement carries no
`O(1)`.

## 3. Where digit input is, and is not, needed

Write `b = (u+1)/S`. The guaranteed exponent is `max(b, 1 − bα)`, so

* `b → 0` (`u = o(S)`, `n ≍ S`): bound (ii) gives exponent `→ 1` **free**;
* `b → 1` (`n = o(S)`): bound (i) gives exponent `→ 1` **free**;
* the **only** binding band is `b` near `1/(1+α) = 0.386853`, i.e.
  `u+1 ≍ 0.39·S` and `n ≍ 0.61·S`.

> **So any `×2,×3` input is needed only on that band, and only to improve the
> placement bound `A*/2^{n+1} > 2^{−1}·3^{−(u+1)}` of step (ii) towards `A*`
> being a positive proportion of `2^{n+1}`.** Quantitatively: an exponent `ε`
> follows from a bound of the form `A* ≥ 2^{n+1}·3^{−κS−C}`, with
> `ε = 1 − κ·log₂3`; the exponent is nontrivial exactly while
> `κ < 1/log₂3 = log₃2 = 0.63092975357…`, and step (ii) already supplies
> `κ = (u+1)/S`.

**What the required statement is, in the right currency.** `A*` is the least
positive residue of `3^{−(u+1)}c` modulo `2^{n+1}`. Improving the exponent
therefore needs a **pointwise** lower bound on that residue along a diagonal
`u, n → ∞` — i.e. pointwise control of powers of `3` modulo powers of `2`, with
an explicit multiplier `c` depending on `(q,v)`.

**Why available `×2,×3` methods do not supply it.** The methods in that circle —
rigidity and disjointness results, and exceptional-set or Cantor-set estimates
for digit patterns — are **measure-theoretic or exceptional-set** statements:
they bound the set of bad exponents, or classify invariant objects. The present
application needs the value at the *specific* `(u,n)` a word generates, which is
a single sequence — a null set for every invariant measure and possibly inside
any density-zero exceptional set.

> **Population/exceptional-set sparsity ≠ pointwise extremal placement.** No
> averaged statement may be promoted to a least-realizer floor, and none is
> promoted here. The two binding deficiencies are **pointwiseness** and the fact
> that the modulus **grows with the exponent** (a diagonal, not a fixed modulus).

*No external theorem is cited as supplying anything, and no claim is made about
which named results do or do not exist for this exact diagonal.*

## 4. The quantifier trap: no absolute floor on `A*` exists

`A*_u` is the least positive residue of `3^{−(u+1)}c` mod `2^{n+1}`, and
`ord_{2^{n+1}}(3) = 2^{n−1}` for `n ≥ 2` (the subgroup `⟨3⟩ ≤ (Z/2^{n+1})^×` has
index 2 and equals `{x ≡ 1, 3 mod 8}`). Hence:

> **Observation P.** For fixed `(q,v)` the sequence `u ↦ A*_u` is **periodic with
> period `2^{n−1}`**, and over one period `A*` ranges over the coset `c⟨3⟩`, so it
> dips to `O(1)`. **No lower bound on `A*_u` holds uniformly in `u` for fixed
> `(q,v)`.**

**[V]** At `(q,v) = (3,1), (2,3), (3,4), (2,6)`: periodic with the predicted
period `8, 16, 64, 128`, and `min A* = 5` over each period.

**This is harmless for Theorem U** — for fixed `n`, bound (i) alone gives
`log₂(r+1) ≥ u+1 = S−n+1`, so the ratio tends to `1` — but it is fatal to any
hypothesis phrased as "`A*` is large". A usable hypothesis must be stated for
`A*/2^{n+1}`, or equivalently relative to `S`, **and must let `n` grow with `u`.**

## 5. The corridor-admissible cone, and why it does not help

For the word `1^u q 1^v`, with `R_j = S_j − αj`:
```
   R_j       = −(α−1)j              for j ≤ u        (≤ 0 always)
   R_{u+1}   = q − α − (α−1)u                         ← the MAXIMUM
   R_{u+1+i} = R_{u+1} − (α−1)i     for 1 ≤ i ≤ v     (strictly decreasing)
```

> **Proposition A.** The word is confined at level `c` (`R_j ≤ c` for every
> `j ≤ u+1+v`) **iff** the single inequality
> ```
>    q ≤ c + α + (α−1)u ,        exactly   2^{u+q} ≤ 2^c · 3^{u+1} ,
> ```
> holds. In particular `u` is unrestricted and **`v` is unrestricted** — a long
> second ones-run only drives `R` further down.

**[V]** Checked against a per-index test for `c ∈ {0,1,2}`, `u<12`, `2≤q<14`,
`v ∈ {0,1,5,20}` — 0 violations.

Since `q = 2` satisfies Proposition A for every `u ≥ 0` already at `c = 1`
(`2 ≤ 2.585`), and `v = n−2` is then free, **every** `b ∈ (0,1)` is realised
inside the cone — including the critical `b = 0.386853`. **[V]** at `S = 50` for
`b ∈ {0.2, 0.3, 0.3869, 0.45, 0.6}`: all admissible at `c = 1`.

> **Conclusion.** Corridor confinement caps `q` relative to `u` and imposes
> nothing on `v`. The binding band is fully admissible, so **the input required
> on the admissible diagonal is exactly the input required in general.** No
> reduction in difficulty follows from Collatz-specific structure at the two-run
> level.

**Scope note.** Proposition A confines the block standing alone. Inside a longer
confined word the block inherits a drift offset `R_a ≤ c`, and the cap becomes
`q ≤ (c − R_a) + α + (α−1)u`, never tighter; at a re-entry, where
`0 ≤ c − R_a < α−1` (Rev 8 Prop. 13.1), it is `q ≤ α + (α−1)(u+1)`, still
satisfied by `q = 2` for every `u ≥ 0`. The conclusion is unchanged.
