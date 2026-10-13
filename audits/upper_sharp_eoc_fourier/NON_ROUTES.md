# Routes examined and why they do not work

Status legend as in [`FINDINGS.md`](FINDINGS.md). Each entry is short: the route, and the reason.

---

## 1. Tao-style Syracuse equidistribution at modulus `2^{S+1}` — `[R]` for the transfer

**Route.** The carry `q_N = sum_j 3^{N−1−j}·2^{s_j}` has exactly the algebraic shape of the
Syracuse random variable `sum_m 3^{n−m}·2^{−(a_m+…+a_n)}` whose equidistribution is known. Reuse
that cancellation machinery at the modulus this problem needs.

**Why not.** The known statement is **modulo `3^n`**, where `2` is a **unit**: every summand is
invertible and the Fourier analysis runs on characters of `Z/3^n Z`. The modulus needed here is
`Q = 2^{A[N]+1}` — a power of **2**, exponentially large in `N` — in which the `2^{s_j}` are
precisely the **nilpotent** directions. A character with `v₂(h) = t` annihilates every summand
with `s_j ≥ A[N]+1−t`, collapsing the sum to a function of the path prefix; that collapse is
verified **exactly** in [`scripts/check_dyadic_tower.py`](scripts/check_dyadic_tower.py) §4 and is
the mechanism of the entire resonance tower ([`FINDINGS.md`](FINDINGS.md) §3). This is a
**failure of hypothesis, not of constants**: substituting `Q = 2^{A[N]+1}` into that framework is
invalid, not merely lossy. The repository's own dyadic machinery is likewise no help — it concerns
restarted-state mixing inside a cylinder and relies on `3^t` being a unit mod a power of `2`, not
on the realizer-residue distribution over a confined-word ensemble.

---

## 2. The `sup |F| → 0` criterion — `[R]`, false by construction

**Route.** Show the largest nontrivial normalized Fourier coefficient decays, then conclude
equidistribution.

**Why not.** `|F_N(Q/4)| = 1` **identically**, for every `N`. Zero confinement forces `d_0 = 1`,
hence `r ≡ 3 (mod 4)` for every realizer (proved in this repository:
`Descent.a_eq_one_of_confined`, `Descent.mod_four_of_confined`,
[`Descent/ResidueLaw.lean`](../../Descent/ResidueLaw.lean) — `[P]`), so the character at `Q/4` is
constant on the ensemble. `|F_N(Q/2)| = 1` trivially, and `|F_N(Q/8)| ≈ 0.62` and **rising** with
`N`. Measured: [`FINDINGS.md`](FINDINGS.md) §2. **`sup_{h≠0}|F_N(h)|` cannot decay**, so this
criterion must never be used as a go/no-go test for this ensemble. It was not used.

*Important nuance, lest this be read backwards:* the same resonances are **harmless** once the
`1/h` weight of Erdős–Turán is applied — they contribute `O(Q^{−1/2}) = O(2^{−0.792N})`, which
beats the target for every `c > alpha/2` ([`FINDINGS.md`](FINDINGS.md) §4, `[F]`). The
unweighted criterion is dead; the weighted one is not killed by the tower.

---

## 3. The Subspace Theorem, for the **upper** bound — `[R]` for this direction

**Route.** Use the Subspace Theorem / S-unit machinery on the carry equation to control realizer
size.

**Why not, two independent reasons.**

1. **Wrong direction.** The Subspace Theorem bounds S-unit sums **from below** — it yields
   *non-smallness*. That supports **lower** floors (the periodic and one-defect realizer floors,
   Lemma H style), i.e. the half of Sharp EOC that is at least as hard as (DE). It gives no
   mechanism for the **existence of small** realizers, which is what Open Problem 8(4) asks for.
2. **Wrong number of terms.** It needs a **bounded** number of S-unit terms. A generic confined
   word contributes about `N` terms to `q_N = sum_{j<N} 3^{N−1−j}·2^{s_j}`, growing with the
   depth, so the hypothesis is not met except on the structured (periodic / few-defect)
   subfamilies.

**`[D]`** — reported, not located here: the conjugacy-repetition paper (number-theory repo, branch
`conjugacy-repetition-final-20261011-124955`) itself lists *"no bound on approximation by positive
integers"* as **not claimed**, which is the same limitation seen from the other side. That branch
is not present in any local checkout inspected in this round, so the citation is recorded as given
and **not verified here**.

---

## 4. Block rotation and pair collisions — `[R]`, already refuted

**Route.** Exploit the word-level symmetries (feasible cyclic rotation; shared-prefix collision
groups) to move realizers, or to amplify one survivor into many.

**Why not.** Already refuted, cleanly, in the earlier pair/collision audit
(`docs/PAIR_COLLISION_AMPLIFICATION_AUDIT.md` §§6.2–6.4 in
`innerlightr-wq/eoc-lean-verification`): feasible cyclic rotation is a genuine word-**count**
symmetry but is realizer-arithmetically **inert** — rotated words' realizers bear no numerical
relationship to the original's; and the one genuine coupling that exists (shared-prefix words
share a residue class) demonstrably does **not** translate into archimedean closeness, with
measured realizer gaps *within* a collision group about `1455×` **larger** than the ensemble
average. `[D]` — cited, read, not reproduced in this branch. Nothing in this round revises it.
This round avoided the issue structurally by never leaving a single terminal shell, so no
block-swap or rotation weighting entered.

---

## 5. More depth on `h ≤ 1024` — `[R]` as a use of effort

**Route.** Push the low-frequency Fourier measurements to larger `N`, or to larger `K`, to build
confidence in Lemma D1.

**Why not.** D1 quantifies over **odd `h` up to `2^{alpha·N}`**. Every measurement in this round
lives at `h ≤ 1024` or at sparse random probes. The gap is not one of effort: the Erdős–Turán
bound first becomes true at `N ≈ 92 / 132 / 254` for `c = 0.99 / 0.95 / 0.90`, where its
hypothesis ranges over about `10^17` to `10^53` frequencies
([`FINDINGS.md`](FINDINGS.md) §7, `[F]`, extrapolated). More depth on a window that is not the
window the lemma is about buys nothing. Note also that `B_N(1024)` has already **saturated** at
the truncation term `1/K` for `N ≥ 30`, so additional depth at fixed `K` changes nothing
measurable.

---

## 6. Wirsching, LNM 1681 — `[R]` as a source for D1/D2 (different object)

**Route.** Import the predecessor-density machinery of Wirsching, *The Dynamical System Generated
by the 3n+1 Function* (Lecture Notes in Mathematics 1681, Springer, 1998), already cited in this
repository's reading list.

**Why not.** Different object. Wirsching's construction concerns the **predecessor set**
`{b : T^ν(b) = a}` and its lower asymptotic density, developed through an averaging construction on
the **3-adic** integers, with a limiting operator whose essential part is a Markov chain on `[0,1]`
having a base-3 Fabius-type invariant density. That is a **3-adic backward** distribution. The
object here is the **dyadic forward** distribution of confined-word realizer residues modulo
`2^{A[N]+1}`. No identification between the two is available: Wirsching's counting variable is a
backward path count in the predecessor graph; ours is the image of a forward confined word under
the realizer congruence.

**Exactly what was read, and nothing more:** the Springer volume's series description and the
companion note *On positive predecessor density in 3n+1 dynamics* (summary level only, via web
search), plus the Tao comparison in §1 above (the blog post *Equidistribution of Syracuse random
variables and density of Collatz preimages*, read for its modulus, its definition of the Syracuse
random variable, and where invertibility of `2` enters). **LNM 1681 itself was not consulted.**
No D1/D2-shaped statement was located in what was read. This is "not located in the searched
literature", nothing stronger; see the novelty TODO in [`README.md`](README.md).
