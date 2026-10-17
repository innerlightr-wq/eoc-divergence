# 06_POINTWISE_REALIZER_IMPLICATIONS.md

## What the findings imply: nothing, and the reason is structural

The brief's secondary question is whether temporal differentiation can constrain positive-integer
realizability in the zero-confined sector.  It cannot, for a reason that is visible before any
computation:

> **`r_N` is a nonnegative integer satisfying every congruence imposed by the prefix.**
> Therefore **every finite word is realized**, and no prefix-local statement can exclude anything.

Measured (`results/run_final.txt`, P10) at `N = 30`: the Sturmian/Beatty confined prefix has
`r_30 = 71 106 568 281 083`, which reproduces its first 30 valuations as a genuine
positive-integer orbit; `m₀ = 27` and `703` return `r_30 = 27` and `703`.

Lemma T and Lemma T+ are statements about `Δr_N` for a **pair** of prefixes.  Realizability is a
statement about **one infinite** word — specifically, by Proposition R, about whether `(r_n)`
eventually stabilizes.  A closed form for the difference between two prefix-realizers says
nothing about whether either sequence stabilizes, because both are realized at every finite
stage by construction.

## Why this is not merely a limitation of these particular lemmas

The brief (§7) asks for an invariant independent of the generic height comparison.  Lemma T+ is
indeed independent of it — it never invokes `2^{S_N} ≤ 3^N` — but it fails for a different and
more basic reason: **it is prefix-local**.  The following is the general obstruction:

> Any function `Φ(d_0,…,d_{N−1})` of a finite prefix takes the same value on a realizable
> infinite word and on an unrealizable one sharing that prefix.  Since every confined prefix
> extends both to a realizable word (take the orbit of `r_N`) and — by the word-shadow
> cardinality barrier already recorded in this programme — to unrealizable ones, **no
> prefix-local invariant can separate them.**

Temporal differentiation is prefix-local by construction.  So is the carry, the drift path, the
valuation word, and every statistic in the October 14 suite.  This is the same wall the closed
routes index records, reached from a new direction.

## What would be needed instead

A quantity that is **not** determined by any finite prefix.  Two shapes are available in
principle:

1. a **tail** statement — a property of the infinite continuation, e.g. a bound on
   `#{n : r_{n+1} ≠ r_n}` (the count of nonzero lift digits).  This is the direction the October
   16 package already flagged as the one place Lemma O does not apply, because a *count* is not
   a *size*;
2. a **uniformity-in-`N`** statement — a bound holding for all `N` with a constant independent of
   the word, which would convert prefix-local data into a tail conclusion.  Lemma T+ is the
   opposite: its content is entirely local to `(i,k)`.

Neither is supplied by anything in this investigation.

## Explicit statement of what is *not* claimed

* No new constraint on positive-integer realizability.
* No conditional exclusion theorem.
* No progress on `(DE)`, `(PosPC)`, Sharp EOC, or Open Problem C — all unchanged.
* No claim that the late-stage hypothesis revealed hidden structure; it did not.
