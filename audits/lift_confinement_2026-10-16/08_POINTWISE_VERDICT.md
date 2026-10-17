# 08_POINTWISE_VERDICT.md

## Verdict

**E — proposed lift mechanism obstructed** (Targets A and B), with **D — existing identities
explain the results** for the statistical findings.  No new arithmetic restriction is established.

Per the brief's allowance for separate verdicts:

| mechanism | verdict |
|---|---|
| Target A — confined lift-density lower bound | **E** (counterexample `min J(N) = 3`; and circular) |
| Target B — plateau obstruction | **E** (both extremes confined) |
| Target C — episode–lift connection | **not reached** |
| Target D — pointwise conditional theorem | **not obtained** |
| lift statistics (density, slack, plateaus) | **D** (uniform blocks + weighting artefacts) |
| L1 / L2 / L3′ | **PROVED**, but definitions made explicit |

## The final research question, answered

> *Does zero confinement constrain the temporal pattern of canonical realizer lifts strongly
> enough to produce a new arithmetic theorem?*

**No.**  Zero confinement constrains the lift count in **neither** direction:
```
min J(N) = 3   for every N = 6..13   (least realizer 71, plateau N−5)
max J(N) = N−1 for every N           (all-ones word, x = −1)
```
both on complete exact enumerations.  The full range is occupied at every length.  And after
the correct control — each confined prefix counted once, since `b_n` depends only on
`(d_0,…,d_n)` — the lift blocks behave exactly like uniform blocks on `[0,2^{d_n})`, matching
`P(b_n=0) = 2^{−d_n}` to `±0.021`.

## Where a global argument would be required `[the brief's §10]`

`J(N)` is prefix-local: `b_n` is a function of `(d_0,…,d_n)`.  By the prefix-locality obstruction
already established, every finite confined prefix is realized, so no finite-`N` statement about
`J` distinguishes two infinite words sharing that prefix.  A pointwise theorem would need a
statement of the form

> there exists `c > 0` and `N₀` such that **for every** `N ≥ N₀` **and every** infinite
> zero-confined word, `J(N) ≥ cN`,

i.e. an estimate **uniform in `N` and over the whole sector**, not verified for finitely many
lengths.  `L4` shows this exact form is false (`min J(N) = 3`).  A weaker uniform statement
restricted to a subfamily might survive, but the subfamily would have to exclude the orbits of
small integers — and specifying it without assuming the conclusion is precisely the open problem.

## What this does and does not imply

**Does:** it closes the lift-density route cleanly, with an exact finite counterexample pair that
can be checked in seconds, and it supplies a correct and useful dictionary entry (L2): `J(N)`
counts the word's valuation overdrafts against its running least realizer.

**Does not:** improve positive-integer realization control in any way.  `(DE)`, `(PosPC)`,
Sharp EOC and Open Problem C are unchanged and open.

## Three next steps, ranked by provability

1. **Add the counterexample pair to the closed-routes index.**  `min J(N) = 3` via `71` against
   `max J(N) = N−1` via the all-ones word is a two-line refutation of any future
   confinement-driven lift bound.  It also generalises the existing index entries: *both extremes
   of a proposed statistic being occupied within the confined sector* is a reusable test, and it
   is cheap to apply.  Certain to complete.
2. **Formalise L2 in Lean** alongside the aggregate identity.  `b_n = 0 ⟺ 2^{d_n} | 3m_n+1`
   is a `ring`/`omega`-level statement given the existing `C_{n+1} = 3C_n + 2^{S_n}`
   formalisation, and it converts the realizer-lift notion into a checked definition.  Low risk.
3. **Reconsider whether any non-prefix-local quantity exists at all.**  Three consecutive audits
   (H10 transfer, temporal carry, this one) have each terminated on prefix-locality or on an
   exact-identity collapse.  Rather than test a fourth candidate, the higher-value step is to try
   to **prove** that every quantity definable from `(d_0,…,d_N)` and the aggregate identity is
   prefix-local — which would convert a repeatedly rediscovered wall into a theorem and stop the
   cycle.  Harder than 1–2, but it is the step that would actually change the programme.

## Operational compliance

No repository modified; nothing committed, pushed, published or uploaded.  All work in this
scratch directory.  **No Lean build was run and no Lean verification is claimed.**  No numerical
correlation is interpreted as a theorem.  The H10 height method was not retried.  The
terminal-tip hypothesis was not revived — the correctly confined enumeration that the brief asked
for is in `03_...`, and it supersedes the earlier unconfined run.

**Three of my own claims were retracted during this session**, each caught by its own data:
L3 and its corollary `J(N) ≤ S_N − N`; "minimisers are orbit prefixes of small integers"; and
"`P(lift)` is essentially flat in the slack".  All three are recorded at the point of use.
