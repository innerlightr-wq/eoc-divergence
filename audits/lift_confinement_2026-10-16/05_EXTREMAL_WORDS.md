# 05_EXTREMAL_WORDS.md

## Minimum-lift confined words: `min J(N) = 3`, constant

| `N` | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
|---|---|---|---|---|---|---|---|---|
| `min J(N)` | **3** | **3** | **3** | **3** | **3** | **3** | **3** | **3** |
| #achievers | — | 3 | 3 | 3 | 3 | 2 | 2 | 4 |
| `r_N` of achievers | — | **71** | **71** | **71** | **71** | **71** | **71** | **71** |
| longest plateau | — | 2 | 3 | 4 | 5 | 6 | 7 | 8 |

**Every minimiser from `N = 7` to `N = 13` has least realizer `r_N = 71`**, with the zero-lift
plateau growing as `N − 5` while `J` stays at 3.  A representative minimiser at `N = 13` is
`[1,1,2,2,1,2,1,1,2,1,1,1,1]`.

`71`'s own accelerated orbit is genuinely zero-confined for 13 steps (checked
`2^{S_{j+1}} ≤ 3^{j+1}` at every step), with word
`[1,1,2,2,1,2,1,1,2,1,1,1,2,3]` and iterates `71, 107, 161, 121, 91, 137, 103, 155, 233, 175,
263, 395, 593, 445`.

### A correction

I first wrote that the minimisers "are exactly the confined prefixes of the orbits of small
integers".  **My own output contradicted that** at `N = 9` and `N = 13`, where the minimiser word
differs from `71`'s orbit word in the last digit.  Retracted.

The reason is worth stating, because it is a real distinction: the congruence
`r_n ≡ −C_n3^{−n}` forces only `v_2(3m_j+1) ≥ d_j`, **not equality**.  When `v_2 > d_j` the next
iterate is even and the word is a *congruence word*, not an *orbit word*.  Measured
(`results/run_min71.txt`): of the minimisers, only `2/3` (`N = 7..10`), `2/2` (`N = 11,12`) and
`2/4` (`N = 13`) are orbit words of `71`; **none** has all `m_j` odd.

**Corrected statement:** `min J(N)` is pinned by the smallest integer admitting a length-`N`
confined *congruence* word, and over the enumerable range that integer is constant at `71`.

## Maximum-lift confined words: `max J(N) = N − 1`, attained

The all-ones word `d ≡ 1` is zero-confined, has `b_n = 1` for every `n`, and `x = −1`.

## The consequence for every proposed bound

> **Both extremes of the range are occupied at every `N`:**
> ```
> min J(N) = 3   (realizer 71)        max J(N) = N − 1   (all-ones word, x = −1).
> ```
> **Zero confinement therefore imposes no bound on the lift count in either direction**, and no
> lower bound on `J(N)` growing with `N` can hold over all confined words of length `N`.

This is an exact finite statement on a complete enumeration, not a sample.  It is the
counterexample the brief asks to be preserved: **the pair (71-word, all-ones word) falsifies any
proposed confinement-driven lift-density bound.**
