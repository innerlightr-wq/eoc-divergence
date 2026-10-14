# LOPEZ_STOLL_SOURCE_AUDIT.md

```
[2009]  J. Lopez, P. Stoll, "The 3x+1 conjugacy map over a Sturmian word",
        INTEGERS 9 (2009), 141-162, #A13.  DOI 10.1515/INTEG.2009.014.
        file ~/Downloads/j13.pdf   22 pp
        sha256 e6901bbe7b84af724575afd8d1b21674df3ced39c70f8c2aef6ac312d5dedf0b
        REFEREED (Received 12/1/08, Revised 2/25/09, Accepted 3/5/09).

[2021]  J. Lopez, P. Stoll, "The 3x+1 periodicity conjecture in R",
        arXiv:2101.12747v1 [math.NT], 29 Jan 2021.  51 pp
        file ~/Downloads/2101.12747v1.pdf
        sha256 e4c5bccec262d8fdb001d7970dee56c347c03d789796c165e79a18dc2d584b9a
        PREPRINT, v1.  No journal reference in the file.
```

Read firsthand: [2009] abstract, §1, Theorem 1, Corollary 2; [2021] abstract,
§1 (incl. eqs. (11)-(16) and Theorem 1), §5 statements, §6 in full (Lemmas
19-26 and the proof of Theorem 1), Lemmas 39-40.

---

## 1. What [2009] proves — refereed, and narrower than often quoted

With `Phi` the Bernstein-Lagarias conjugacy (`Phi o S o Phi^{-1} = T`) and
`Phi(2^{d_0}+2^{d_1}+...) = -sum_i 2^{d_i}/3^{i+1}` (eq. (2), attributed there
to [1]):

* **Theorem 1 / Corollary 2 [PRIOR, refereed].** For `1c_alpha` the mechanical
  word of irrational slope `alpha` and intercept `0`, an explicit generalized
  continued-fraction expansion of `-1/Phi(1c_alpha)`, convergent in the 2-adic
  metric, with coefficients in the convergents `p_k/q_k` of `alpha`.
* §4: the associated **real-valued** `Phi_R(1c_alpha)` is a devil's staircase;
  `F` strictly increasing on the rationals (Lemmas 23, 27).

**What [2009] does NOT prove, in its own words.** Its abstract states "It is
unknown if there exists any aperiodic `v` with an eventually periodic
`Phi(v)`", and that "The given examples **suggest** that `Phi` always maps
Sturmian words to infinite words of full complexity." There is **no**
critical-density theorem in [2009]. Any citation of [2009] for a density
statement is a citation beyond what it proves.

## 2. What [2021] claims

> **Theorem 1 [2021].** If the trajectory of some `zeta in Q_odd` is divergent
> (the orbit is an infinite set), then `lim (h/l) = ln2/ln3`, where `h` is the
> number of 1's in the first `l` digits of the parity vector of `zeta`.

Proof architecture (§6), verbatim in structure:

1. `lim(h/l) > beta` ==> `Phi_R(v)` exists (Lemma 23) ==> the orbit of
   `Phi_R(v)` has accumulation points (Lemma 26) ==> `Phi_R(v) notin Q_odd`
   ==> "From (15) and (16) it follows that the 2-adic `Phi(v)` is aperiodic."
2. `lim(h/l) < beta` ==> `Phi(v) notin Q_odd`, citing **Monks-Yazinski [8],
   Theorem 2.7 b** (2004).
3. "Hence `lim(h/l) = beta` is the only remaining possibility."

## 3. The seven audit points, answered

**(1) Definition of density.** `h/l` where `h = #{1's among the first l digits}`
of the parity vector. **Ordinary parity time**, not accelerated time. ✓ (audit
point 4 answered: ordinary.)

**(2) liminf or limsup?** The paper writes `lim` throughout, including in the
abstract and Theorem 1. **But the proofs use `liminf`.** Lemma 23's proof reads:
"There is an irrational `alpha` such that `lim(h/l) > alpha > ln2/ln3`. There is
a `L in N` such that `h/l > alpha` for all `l >= L`." The quantifier "for all
`l >= L`" is exactly `liminf(h/l) >= alpha`. So branch 1 is a **liminf**
statement, and correctly so. Lemma 26 inherits it, using Monks-Yazinski Lemma
4.1 for shift-invariance (which does hold for `liminf h/l`: `h(k+l)-h(k))/l` and
`h(m)/m` have the same `liminf`).

**(3) Is the limit required to exist?** **Yes — by the trichotomy, and this is
the first real gap.** Step 3 ("hence `= beta`") is exhaustive only if
`lim(h/l)` exists. If `h/l` oscillates with `liminf < beta < limsup`, none of
the three cases applies as written. The conclusion that *is* supported by steps
1-2, with no existence assumption, is

> **liminf (h/l) = beta** (branch 1 excludes `liminf > beta`; branch 2, via
> Monks-Yazinski, excludes `liminf < beta`),

with `limsup(h/l)` entirely unconstrained. **The unqualified "`lim = beta`" of
Theorem 1 overstates what the argument gives.**

**(4) Ordinary parity time?** Yes, see (1).

**(5) `Phi` in R or in `Z_2`?** **Lemmas 19, 20, 21, 23, 24, 25, 26 are all
statements about `Phi_R` in R** and about the *real* pseudo-trajectory
`T_u(x) = T_u(0) + (3^h/2^l)x` of Lemma 2. Only the final sentence of branch 1
leaves R.

**(6) The passage to aperiodicity / irrationality of the 2-adic value.**
**This is the decisive gap, and it does not survive.** The paper's justification
is (15)-(16) plus: *"If `Phi_R(v)` is an irrational number, then the inverse
limit `lim_<- Phi_R(v)` is a 2-adic integer which is aperiodic, because the
irrational `Phi_R(v)` does not admit an eventually periodic 2-adic expansion."*

What (15)-(16) actually say is only that the 2-adic digits of `Phi(v)` are read
off from the partial sums reduced mod `2^l` — true, and true whether or not the
real series converges, because `Phi_R(u^(l))` and `Phi(u^(l))` are *the same
rational number*. They give no identification of the two **limits**, which are
taken in different topologies. A real irrational has no 2-adic expansion at all;
the quoted sentence conflates the real number `Phi_R(v)` with the 2-adic
`Phi(v)`.

**The two limits are provably different, and the discrepancy is explicit.**
Proved and verified here (`scripts/phi_identity.py`, `scripts/carry_bridge.py`,
0 violations over 8 seeds and `N <= 40`; see `CRITICAL_RETURN_CARRY.md` §1):

```
   Phi_R(u^(l))  =  m_0 - (2^l / 3^h) * T^l(m_0)        [exact over Q, every l]
```
so for a positive odd seed `m_0` whose parity vector is `v`,

```
   Phi(v)   = m_0                                   (the 2-adic value), while
   Phi_R(v) = m_0 ( 1 - 2^{E_infty} ),   E_infty = sum_j log2(1 + 1/(3 m_j)) ,
```
whenever the real series converges. These differ by exactly `m_0 2^{E_infty}`.
For `m_0 = 27` at `N = 8` the real partial sum is `-1.405426002` while the
2-adic value is `27`. **`Phi_R(v) notin Q_odd` therefore says nothing about
`Phi(v) in Q_odd`**, and `Phi_R(v) = m_0(1-2^{E_infty})` is in general
irrational *while* `Phi(v) = m_0` is an integer — the two facts are perfectly
consistent. Branch 1's conclusion does not follow.

Lemma 24 is affected by the same conflation in its `zeta in Q_odd` sub-case:
"Thus the function `T_{v_i}` does the same as the map `T`, and `v` is the
aperiodic parity vector of `zeta`" requires `v_i = T^i(zeta) mod 2`, i.e.
exactly `Phi_R(v) = Phi(v)`.

**(7) Assumptions for the rational 2-adic non-cyclic statement.** Branch 2
rests entirely on **Monks-Yazinski (2004), Theorem 2.7 b**, quoted by [2021] as:
if the trajectory of `zeta in Q_odd` is divergent then (12) `lim(h/l) >= beta`.
That paper was **not read in this session**; the statement is recorded as
**source-reported via [2021]'s quotation**, and [2021] itself attributes the
integer case to Lagarias ([2], Relation 2.31). Its `lim` is presumably `liminf`
for the same reasons as above, but that is not verified here.

## 4. Verdict on each piece

| statement | status |
|---|---|
| [2009] Theorem 1 / Corollary 2 (2-adic CF expansion) | **[PRIOR, refereed]** |
| [2009] devil's staircase `F`, `F*` | **[PRIOR, refereed]** |
| [2009] "`Phi` always maps Sturmian words to full complexity" | the paper's own word is **"suggest"** — not a theorem |
| [2021] Lemma 23 (`liminf > beta` ==> `Phi_R(v)` exists) | **sound**, and immediate from the series form: `Phi_R(v) = -(1/3) sum_i 2^{-Delta_i}` (see §5) |
| [2021] Lemmas 25, 26 (real orbit bounded, infinite, accumulation point) | sound as **statements about R** |
| [2021] step `Phi_R(v) notin Q_odd ==> Phi(v) notin Q_odd` | **INVALID.** Explicit discrepancy `Phi(v) - Phi_R(v) = m_0 2^{E_infty}` |
| [2021] Lemma 24, `zeta in Q_odd` sub-case | **same conflation** |
| [2021] trichotomy / existence of `lim(h/l)` | **unjustified**; correct form is about `liminf` |
| [2021] **Theorem 1** | **UNAUDITED / INCOMPLETE DEPENDENCY.** Not used below to support any conclusion |
| Monks-Yazinski 2.7 b (branch 2) | **[PRIOR, refereed 2004], source-reported** — not read here |

**What is securely covered is the `liminf < beta` side only** (Monks-Yazinski /
Lagarias), i.e. in EOC terms `limsup_N (S_N/N) <= alpha`. The `> beta` side,
which is where [2021]'s new content lies, does not survive the audit as a
statement about `Phi`.

## 5. The repair, and what it is worth

The sound residue of branch 1, restated in R only and translated exactly:

> **Proposition L (repaired branch 1).** For an aperiodic parity vector `v`,
> `Phi_R(v)` converges **iff** `sum_{i>=0} 2^{-Delta_i} < infinity`, where
> `Delta_i = alpha i - S_i`. If `liminf Delta_N/N > 0` then it converges.
> For a positive odd seed `m_0` this is **equivalent to `sum_j 1/m_j < infinity`.**

(Proof: §1 of `CRITICAL_RETURN_CARRY.md`; `Phi_R(v) = -(1/3) sum_i 2^{-Delta_i}`
is immediate from eq. (2) with `d_i = S_i`.)

So branch 1, repaired, says: *a near-critically-confined orbit has summable
reciprocals.* That is **already a theorem** for divergent orbits —
Curry (2026), Proposition 3.1, as recorded in
`eoc-lean-verification/README.md` — so the repaired branch adds nothing, and
its unrepaired conclusion is unavailable. **[2021] does not strengthen the EOC
picture.** The direction that *does* carry content is the reverse one, and it is
the subject of `CRITICAL_RETURN_CARRY.md`.
