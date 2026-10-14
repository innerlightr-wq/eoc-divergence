# VERDICT.md

## Decision

**The joint-budget construction does not close, and the failure is a theorem, not
a shortfall of ingenuity.** Three independent reasons, in increasing order of
finality — and two of the three were already established in Phase 6, which I
report before anything else.

The round produced one genuinely new per-episode estimate (the toll), one new
diagnostic fact about the carry pot (gap domination), one new reduction (the
local-time stratification) with a measurement that refutes what the reduction
needs, and a second independent confirmation of Phase 6's `Θ(m_0)` versus
`Θ(log m_0)` verdict. It did **not** produce a cross-episode bound on combined
duration.

## The six required answers

### 1. What arithmetic relation, if any, was obtained beyond the existing coordinate identities?

**One, and it is small.** From Prop. 13.1, at every re-entry `a_i > 0`,

```
   z_{a_i} = 2^{R_{a_i}} > 2^c·2^{1−α} = (2/3)2^c ,
   hence   W_i = Σ_{n∈I_i} z_n > (2/3)2^c ,   equivalently   η_i ℓ_i > 2/3 ,
```

**independently of `ℓ_i` and of how deep the episode goes.** So the
carry-*weighted* duration has a universal positive floor per episode even though
the duration itself has none. Verified at all re-entries tested (0 violations).
I did not find this in Phase 6 or in Rev 8.

Everything else in `JOINT_EPISODE_ARGUMENT.md` §1 — `W_i = 3(𝓑_{b_i}−𝓑_{a_i})`,
`0<η_i≤1`, the block matrix and its composition law, terminal oddness — is an
**exact regrouping of Lemmas 2.2 and 2.4**. It is preparation, and the brief is
right that it is not the objective. Proposition J (the two-sided allowance pin)
*is* a clean exact statement, with integral form
`1 ≤ 2^{2c}m_a^2/(m_0𝓑_a) < (9/4)𝓑_a/m_0`, but its two halves are precisely
carry positivity and the entry lemma, so it is a rearrangement of two known
facts — and its corollary is **Phase 6's answer 8** ("all charges are the same to
within a small additive constant").

### 2. Does it couple different episodes with an affordable total cost, or only bound them separately?

**It couples them — and the coupling is affordable only in a sector that is
already closed.**

The coupling is real: the toll is paid out of **one** shared pot,
`Σ_i W_i = 3Σ_i(𝓑_{b_i}−𝓑_{a_i}) ≤ 3(𝓑_H − m_0)`, with no per-episode seed
allowance refreshed. That is the amortized charge the brief asked for, and it
gives `P − 1 < (9/2)2^{−c}m_0(2^{E_H}−1)`.

But the pot is in the wrong place. Measured gap share of the pot: **`0.9994`** at
`m_0 = 285175, c = 1` (occupied `53.31` against gap `96115.13`), and `≥0.998` in
every escaping case. On the corridor `z_n ≤ 2^c`; in a gap `z_n > 2^c` and grows
geometrically. **So amortizing against the pot constrains gap time, not corridor
time:** with `G = H − O_c`, `2^cG < pot` rearranges to `O_c > H − 2^{−c}pot`, a
**lower** bound on occupation. At the Loeb seed it yields `O_c > −47946`.

Where the bound *is* non-vacuous is sharp and decisive: on the Prop. 13.2
oscillator, whose drift is confined to a bounded **two-sided** window, the slack
is a stable **`3.5×`** across `c = 0,1,2` and `N = 60,120,200`; on seeds whose
drift escapes it degrades like `2^{R_max−c}` to `10^4–10^7`. **Bounded two-sided
drift is exactly the sector `BoundedDrift.lean` already closes.** This is the
brief's stopping condition, met.

### 3. Does it control the small-eta problem without reproducing the known `2^w` loss?

**No.** It replaces the `2^w` loss with an equivalent one, and the measurement
says the replacement is no better.

Stratify by depth below the corridor top,
`L_w = #{n<H : c−w−1 < R_n ≤ c−w}`. Exactly
`Σ_w L_w 2^{−w} < 2^{1−c}·pot` while `O_c = Σ_w L_w`. So the pot bounds `O_c`
only if the profile decays fast enough to beat `2^w` — concretely it needs a
depth bound `w_max ≤ K log_2 O_c` with `K < 1`. Measured over 8 cases:

```
   w_max = 7 … 13 ,   mean depth 3.14 (at O_c = 98) → 7.09 (at O_c = 259) ,
   w_max / log_2 O_c  ∈  [1.16, 1.73] ,     exact inverse-η loss  2.6 … 12.9 .
```

**`K < 1` is not supported by the data**, so the required depth bound is
empirically false in the form the route needs. This reproduces, from a different
direction, Phase 6's one open item — *"long episodes always had depth `≈ ℓ/10`
(`corr = +0.923`)"* — and converts it into the exact obstruction to the pot
route. Linear depth-in-length is precisely what kills a `2^{−w}`-weighted budget.

### 4. What class of actual positive-integer orbit segments does it cover?

Covered, unconditionally: **finite prefixes `[0,H)` of any odd seed with pairwise
distinct states, on which the drift stays in a bounded two-sided window.** On
those, `C1` bounds the episode count to within `3.5×`, and the toll holds at
every re-entry.

Not covered: everything else. Specifically the bound is vacuous as soon as
`R_max − c` grows, which is the generic case for a real seed (`R_max = 18.3` at
`285175`, `26.2` at `63728127`). And the covered class is the one already handled
by bounded-drift exclusion, so the net gain over the existing literature on
actual orbit segments is **nil**.

Controls A, B, E matter here. Control A: the prefix of `285175` at `N=12` has
prefix weight `W = 8.603527014` **identical** across the lifts
`23031, 154103, 285175, 416247, 547319` while `log_2 m_0` runs `14.49 → 19.06` —
so occupation, `W_i` and `η_i` are realizer-class invariants and `log_2 m_0` is
not. Control E: the whole argument survives running the same word over positive
**reals** with no integer ray, since `𝓑_a ≥ m_0` holds for any positive real
start and the entry lemma is symbolic. **Proposition J is therefore not an
integer obstruction, and I classify it as positivity-only.**

### 5. Does it say anything about one infinite zero-corridor episode, or only separated finite returns?

**Only separated finite returns. It is exactly silent on one infinite episode.**

A hypothetical infinite zero-confined orbit is a **single** episode: `P = 1`, so
the toll contributes `(2/3)2^c(P−1) = 0`. This is visible in the data rather than
argued: every single-episode seed tested (`27, 703, 10087, 35655, 381727` at
`c = 1`) shows toll exactly `0.000000`. The `H`-dependence of `C1` does not
permit passage to all `H`, and its `H^{1/9}` form dies at the first repeated
state, so it may not be applied past the injective prefix.

**Classification: separated-return control, not divergence exclusion.** No
corridor-uniform lifetime hypothesis was assumed (§7.1's warning respected);
Theorem 6.14's external sparsity dependency is untouched; and no cycle-exclusion
is claimed. Phase 6 reached the same verdict — *"nothing here bears on an
infinite final corridor episode, which remains possible, nor on cycles."*

### 6. What is the single smallest remaining lemma, and why is it not just EOC or lifetime control rewritten?

> **(DEPTH–DURATION).** There exist `C ≥ 1` and `K < 1` such that for every odd
> `m_0`, every integer `c ≥ 0`, and every episode `I = [a,b)` of the corridor
> `R_n ≤ c` with `m_a, …, m_{b−1}` pairwise distinct,
> ```
>    max_{n ∈ I} ( c − R_n )  ≤  K·log_2 ℓ  +  C ,       ℓ = b − a .
> ```

**Why it is the smallest.** It is the *only* missing input of the pot route. With
it, `Σ_w L_w 2^{−w} ≥ 2^{−C}ℓ^{1−K}/(w_max+1)` and the exact pot inequality
closes to an upper bound on `ℓ`, hence on `O_c = Σ_i ℓ_i` through the shared pot.
Everything else in the chain — the toll, the telescoping, the gap split — is
proved above.

**Why it is not EOC rewritten.** EOC and the single-window lifetime theorem are
statements about **duration** (`O_c`, `L_c`) in terms of the **seed** (`log_2 m_0`).
(DEPTH–DURATION) is a statement about **depth** in terms of **duration**, with no
reference to `m_0` at all. It is a shape constraint on the drift path inside one
episode, it is invariant under the realizer lifts of Control A (which is the
right invariance for a prefix statement, and the one `log_2 m_0` fails), and it
has no `m_0` to re-levy, so it is immune to Remark 13.3's mechanism.

**Why it is not free.** The measurements above say `K ≈ 1.16–1.73 > 1` on real
seeds, and Phase 6's independent measurement says depth `≈ ℓ/10` with
`corr = +0.923` — i.e. depth appears **linear** in length, not logarithmic. So
the lemma as stated is most likely **false**, and the honest next step is to
decide that: either prove depth `= Ω(ℓ)` for some explicit family, which would
close the pot route permanently and for all resources of this shape, or find the
sector where `K < 1` holds. **Deciding the sign of this one question is worth
more than another resource.**

## Stopping statement

Per the brief's stopping rule: **the proposed gain reduces to (i) a
reparameterization of Lemmas 2.2/2.4 for the accounting part, and (ii) a resource
of the wrong scale for the bounding part — `Θ(m_0)` against an `O(log m_0)`
target, with overshoot `Θ(m_0/log m_0)`, which is Phase 6's verdict for the entry
gate now confirmed for a second, independent resource.** I state this as an
obstruction to **this specific joint-budget mechanism** — amortizing a
per-episode toll against the global carry pot — and **not** to episode methods in
general. Per-episode estimates that avoid `log_2 m_0` entirely, such as
(DEPTH–DURATION), are untouched by everything here.

## Next single justified mathematical question

> Is the depth of a corridor episode logarithmic or linear in its length?
> Precisely: does there exist `K < 1` and `C` with
> `max_{n∈I}(c − R_n) ≤ K log_2 ℓ + C` for all episodes of all odd seeds with
> distinct states — or is there an explicit family with
> `max_{n∈I}(c − R_n) = Ω(ℓ)`?

Both outcomes are decisive: the first closes the pot route's only gap, the second
closes the route permanently and, with it, every amortization against a
`2^{−w}`-weighted budget.
