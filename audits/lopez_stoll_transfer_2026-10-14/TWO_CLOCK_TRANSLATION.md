# TWO_CLOCK_TRANSLATION.md — ordinary parity time vs accelerated time

Conventions fixed once. `T(m) = (3m+1)/2^{v_2(3m+1)}` on odd `m`; `d_j >= 1` the
valuation increments; `S_N = d_1 + ... + d_N`, `S_0 = 0`;
`alpha = log_2 3 = 1.584962500721`, `beta = 1/alpha = 0.630929753571`,
`Delta_N = alpha N - S_N`. Zero confinement: `Delta_j >= 0` for all `j <= N`,
tested **exactly** as `2^{S_j} <= 3^j` on integers.

Ordinary time: one accelerated step from odd `m` is `d_j` ordinary `T`-steps —
one odd step (parity bit `1`) followed by `d_j - 1` even steps (bits `0`). So
after `N` accelerated steps the ordinary clock reads `l = S_N` and the height is
`h = N`. The `i`-th `1` of the parity vector (`i = 0,1,2,...`) sits at ordinary
position `S_i`.

---

## 1. The complete ordinary sequence, not just the endpoints

At accelerated endpoints the odd density is `N/S_N`. The brief asks for the
**complete** ordinary sequence, including the intermediate points, and that is
where the one-sided nature of the statement comes from.

> **Lemma C1 [P].** Inside the `j`-th accelerated block the ordinary density
> `h(l)/l` is **strictly decreasing** in `l` (the numerator is frozen at `j`
> while `l` increases), so its infimum over the block is attained at the block
> **end** `l = S_j`, and its supremum at the block **start** `l = S_{j-1}+1`.
> Consequently
> ```
>    liminf_{l -> inf} h(l)/l  =  liminf_N  N/S_N  =  1 / limsup_N (S_N/N) ,
>    limsup_{l -> inf} h(l)/l  =  limsup_N  N/(S_{N-1}+1) .
> ```

Verified exactly on four admissible words (`scripts/counterexamples.py`, final
block): `liminf_l h/l`, `min_N N/S_N` and `1/limsup(S_N/N)` agree to all digits
in every case.

> **Lemma C2 [P].** `S_N/N = alpha - Delta_N/N`, hence
> ```
>    liminf_l h(l)/l  =  1 / ( alpha - liminf_N Delta_N/N ) .
> ```
> In particular, for a zero-confined word (`Delta_N >= 0`):
> `liminf_l h(l)/l >= beta`, with **equality iff `liminf_N Delta_N/N = 0`.**

> **Lemma C3 [P].** Under zero confinement, `d_N = alpha + Delta_{N-1} - Delta_N
> <= alpha + Delta_{N-1}`, so `Delta_N = o(N)` forces `d_N = o(N)`, and
> therefore
> ```
>    lim_{l} h(l)/l = beta    <=>    Delta_N = o(N) .
> ```
> *Proof.* `lim = beta` needs both `liminf = beta` (Lemma C2: `liminf Delta/N = 0`)
> and `limsup = beta`, i.e. `liminf_N (S_{N-1}+1)/N = alpha`, i.e.
> `limsup_N [Delta_N/N + (d_N-1)/N] = 0`, i.e. `Delta_N = o(N)` and `d_N = o(N)`;
> the second follows from the first by the displayed inequality. ∎

**This is the translation table the brief asks for.** Note which side of the
`liminf`/`lim` distinction each statement lands on:

| ordinary-clock statement | accelerated-clock equivalent |
|---|---|
| `liminf_l h/l >= beta` | `limsup_N S_N/N <= alpha`, i.e. **asymptotic** zero confinement |
| `liminf_l h/l = beta` | `liminf_N Delta_N/N = 0` — **statement D** |
| `lim_l h/l = beta` (limit exists) | `Delta_N = o(N)` — **statement E** |
| `h(l) - beta*l -> +infinity` | `Delta_N -> +infinity` |
| `sum_l` summability of `2^{-(h-beta l)}` | `sum_i 2^{-Delta_i} < infinity` |

## 2. The implication lattice A..G — what is valid

```
A. S_N <= alpha N for all N                 (zero confinement)
B. liminf ordinary odd density >= beta
C. liminf ordinary odd density = beta
D. liminf Delta_N / N = 0
E. Delta_N = o(N)
F. Delta_N = O(log N)
G. Delta_N bounded
```

**Valid implications [P], all immediate from Lemmas C1-C3:**

```
   A ==> B          (Delta_N >= 0 gives S_N/N <= alpha, Lemma C2)
   C <=> D          (Lemma C2)
   E ==> D          (a limit 0 forces liminf 0)
   E <=> "lim_l h/l = beta"   under A    (Lemma C3)
   F ==> E ==> D ==> C ==> B
   G ==> F
```

**Every other implication among A..G is FALSE**, with exact 0-confined
admissible witnesses (all verified by integer comparison,
`scripts/counterexamples.py`, `results/counterexamples.log`):

| claim | status | witness |
|---|---|---|
| `A ==> D` (or `C`, `E`, `F`, `G`) | **FALSE** | **W1**, `d_j = 1` for all `j`: 0-confined, `Delta_N/N = alpha - 1 = 0.584963` **constant**, `liminf Delta_N/N = 0.585 > 0` |
| `B ==> C` | **FALSE** | same W1: `liminf h/l = 1 > beta` |
| `D ==> E` | **FALSE** | **W2**, geometric climb/descend stages: 0-confined, `liminf Delta_N/N = 9.3e-05` (→0) but `limsup Delta_N/N = 0.209963`; `max Delta_N = 1066.78` at `N = 6000` |
| `C ==> E` | **FALSE** | same W2 (`C <=> D`) |
| `E ==> F` | **FALSE** | **W3**, `Delta_N ~ sqrt(N)`: 0-confined, `max Delta_N/N = 0.0157 -> 0` so `E` holds, while `Delta_N/log_2 N = 4.75` at `N = 3000` and `-> infinity`, so `F` fails |
| `F ==> G` | **FALSE** | `Delta_N = log_2 N` is `O(log N)` and unbounded |

**W4** (`d_j = 2` whenever confinement allows, else `1`) realizes **G**:
0-confined with `max Delta_N = 1.00` over `N <= 4000`. So `G` is not empty
symbolically; it is excluded for positive-integer orbits by the repository's
bounded-drift theorems (`PRIOR_DETERMINISTIC_BARRIERS.md` §1), not by anything
symbolic.

## 3. The warning the brief asks for, stated as a consequence

> **The inference `liminf Delta_N/N = 0  ==>  Delta_N = O(log N)` or `O(sqrt N)`
> is invalid**, by W2 and W3 respectively. W2 has `liminf Delta_N/N = 0` and
> excursions to `Delta_N > 1000`; W3 has `Delta_N = o(N)` and `Delta_N/log N
> -> infinity`. A return corridor is a statement about **every** large `N`;
> `liminf` is a statement about **one subsequence**. The gap between them is
> exactly the gap the EOC program is stuck in.

## 4. What Lopez-Stoll would add, if it survived audit — and what it does add

If [2021] Theorem 1 held as printed (`lim(h/l) = beta`), then by Lemma C3 a
divergent positive-integer orbit would satisfy **E**: `Delta_N = o(N)`. That
would be a genuine strengthening of **A** (which by W1 gives nothing beyond
`Delta_N >= 0`).

It does not survive (`LOPEZ_STOLL_SOURCE_AUDIT.md` §3(6)). What the argument
supports, and only via Monks-Yazinski's refereed branch, is `liminf_l h/l >= beta`,
i.e. `limsup_N S_N/N <= alpha` — **statement B, which is asymptotic zero
confinement and is the pre-existing Lagarias/Monks-Yazinski input, not new.**

> **Conclusion of §4 [P].** After the audit, Lopez-Stoll adds **no** restriction
> on a hypothetical permanently zero-confined positive integer beyond `B`, which
> `A` already implies. In particular neither `D` nor `E` is available from
> [2021].
