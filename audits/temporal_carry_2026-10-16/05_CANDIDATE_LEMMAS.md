# 05_CANDIDATE_LEMMAS.md

## Lemma T — the low bits of the odd part are position-determined `[PROVED]`

> For the `S_N`-preserving swap `(i,k)`, the intrinsic odd part satisfies
> ```
> u ≡ −3^{−(i+2)}   (mod 2^{d_{i+1}}) ,
> ```
> independent of `N`, `S_N`, `k`, and every digit except `d_{i+1}`.

*Proof.* `W_{i,k} = 2^{S_{i+1}} V`, `V = 3^{N−2−i} + Σ_{j=i+2}^{k} 3^{N−1−j} 2^{S_j − S_{i+1}}`.
The first omitted term has valuation `S_{i+2} − S_{i+1} = d_{i+1}`, so `V ≡ 3^{N−2−i}
(mod 2^{d_{i+1}})`.  With `Δr_N ≡ −W 3^{−N}`, `u ≡ −3^{N−2−i}3^{−N} = −3^{−(i+2)}`. ∎

**Verified on 22 456 swaps, 0 failures** (`results/run_odd.txt`, P5).

## Lemma T+ — there is no residual odd component at all `[PROVED]`

> ```
> u ≡ −V_{i,k} · 3^{−N}  (mod 2^{S_N − S_{i+1}}) ,     V_{i,k} = Σ_{j=i+1}^{k} 3^{N−1−j} 2^{S_j − S_{i+1}} ,
> ```
> **exactly**.  `u` is a closed form in `(N, i, k, d_{i+1..k−1})`; Lemma T is its first block.

**Verified on 36 712 swaps, 0 failures** (`results/run_closed.txt`).

> **This answers the brief's primary question, and the answer is no.**  Once the valuation
> `v_2 = S_{i+1}` is removed, what remains is not a residual carrying new information — it is an
> explicit function of the word.  Temporal position enters only as *the index range of a sum*.

## Assessment against the brief's six tests

| | Lemma T | Lemma T+ |
|---|---|---|
| 1. exact statement | above | above |
| 2. proved? | yes, 3 lines from the carry formula | yes, 2 lines |
| 3. already follows from known results? | **yes** — immediate from `C_N = Σ3^{N−1−j}2^{S_j}` | **yes**, likewise |
| 4. finite counterexamples? | none in 22 456 | none in 36 712 |
| 5. aggregate or individual? | individual pairs | individual pairs |
| 6. stronger pointwise information? | **no** (§4 below) | **no** (§4 below) |

Per the brief's §9 instruction, a statement that follows immediately from the defining formula is
**not** a new theorem.  Both are recorded as *closed forms*, not advances.

## §4  Why neither touches realizability `[PROVED]`

`r_N` is itself a nonnegative integer satisfying every congruence of the prefix.  Hence **every
finite word is realized** — confined, Sturmian, periodic, random or orbit alike.  Measured
(`results/run_final.txt`, P10): the Sturmian/Beatty prefix at `N = 30`, `S_N = 47` has
`r_30 = 71106568281083`, which reproduces the first 30 valuations of the word as a genuine
positive-integer orbit; `m₀ = 27` and `703` return `r_30 = 27`, `703`.

> Temporal differentiation is a statement about **pairs of finite prefixes**.  Positive-integer
> realizability is a statement about **one infinite word**.  Exact control of the former cannot
> bear on the latter, because the former is never obstructed.

## §5  Consistency with the October 14 Theorem D

Theorem D states the odd part "is not determined by any `(j,S)` information" — for **free**
suffixes.  Lemma T+ determines it for the **controlled** swap.  No contradiction: the swap fixes
the continuation.  Tested directly (`results/run_final.txt`, P9): over free-suffix pairs with
matched `S_N`, the odd part mod 8 spreads across all four odd classes
(`j = 3`: `{1:24, 3:12, 5:11, 7:14}`; `j = 6`: `{1:18, 3:21, 5:15, 7:10}`).  **Theorem D is
confirmed and Lemma T+ is seen to be strictly weaker in scope than it may first appear:** it buys
determination only by giving up the freedom that made the problem hard.

## Candidates considered and rejected

| | target | outcome |
|---|---|---|
| A | bound on odd-part placement given first-difference position | **achieved but trivial** (Lemma T/T+); follows from the carry formula |
| B | nontrivial carry-interaction identity | **achieved and structureless**: `Δ_iΔ_k C = Δ_iC·Δ_kC/T_i`, exactly separable |
| C | constraint on realizer distribution in a valuation class | **not obtained**; free suffixes spread it (P9), reconfirming Theorem D |
| D | relation between residue-change events and episode structure | **not attempted** — would require an effect to explain, and §06 shows there is none |
| E | arithmetic separation for a class of aperiodic confined sequences | **not obtained**; every finite prefix is realized (§4) |
| F | conditional realizer-exclusion theorem from a temporal invariant | **not obtained**, and §4 shows why no prefix-local invariant can give one |
