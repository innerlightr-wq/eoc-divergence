# The López–Stoll critical-density bridge — 2026-10-14

**Question.** Can the exact EOC confined-mass machinery strengthen López and
Stoll's critical-density arguments, and — the real target — bridge symbolic
density to positive-integer realizability?

**Verdict.** The mass law does not strengthen their analysis; it turns out to
**contain their real-analytic object exactly**. That dictionary then does two
things: it **refutes the real-to-2-adic step** of the 2021 preprint's main
theorem, and it yields one new deterministic return-count theorem — which proves
to be a counting generalization of a theorem already in `eoc-lean-verification`,
with the same constant.

Read [`VERDICT.md`](VERDICT.md) for the six answers,
[`LOPEZ_STOLL_SOURCE_AUDIT.md`](LOPEZ_STOLL_SOURCE_AUDIT.md) for the audit, and
[`CRITICAL_RETURN_CARRY.md`](CRITICAL_RETURN_CARRY.md) for the bridge.

## The bridge

With `Δ_i = αi − S_i` and `q_N` the EOC carry, and `Φ` the Bernstein–Lagarias
conjugacy with `Φ(2^{d_0}+2^{d_1}+…) = −Σ_i 2^{d_i}/3^{i+1}`, `d_i = S_i`:

```
   Φ_R(v) = −(1/3) Σ_{i≥0} 2^{−Δ_i} ,        Φ_R(u^{(S_N)}) = − q_N / 3^N ,
   Φ_R(u^{(ℓ)}) = m_0 − (2^ℓ/3^h) T^ℓ(m_0)          [exact over Q, 0 violations]
```

**López–Stoll's real devil's-staircase object is the normalized EOC carry.**
Hence `Φ_R` converges ⟺ `q_N/3^N` converges ⟺ `Σ 2^{−Δ_i} < ∞` ⟺ `Σ 1/m_k < ∞`.

## The refutation

The 2021 preprint's Theorem 1 concludes that a divergent rational 2-adic must
have parity density exactly `β = log2/log3`, arguing *"`Φ_R(v)` irrational ⟹
`Φ(v)` aperiodic"*. But the real and 2-adic limits of the same series are
different numbers, and the dictionary says exactly how different: for a positive
odd seed `Φ(v) = m_0` while `Φ_R(v) = m_0(1 − 2^{E_∞})`. For `m_0 = 27` the real
partial sum at `N = 8` is `−1.405426` against the 2-adic value `27`. So
`Φ_R(v) ∉ Q_odd` says nothing about `Φ(v)`.

Two further issues: the proof's trichotomy presupposes that `lim h/ℓ` **exists**
(the supported statement is about `liminf`), and the repaired branch reduces to
Curry's reciprocal summability, already a theorem. **After the audit López–Stoll
adds nothing to the restrictions on a confined positive integer.** The 2009
refereed paper is sound and contains no density theorem — its own word for full
complexity is *"suggest"*.

Theorem 1 is recorded as an **unaudited / incomplete dependency**; the theorem
may still be true, but its proof as written does not establish it. Monks–Yazinski
(2004) Thm 2.7(b) and Curry (2026) are **source-reported, not read** here.

## The new estimate, honestly placed

```
   #{ i < N : Δ_i ≤ w } ≤ 3 m_0 2^w (2^{E_N} − 1) ≤ 3 e^{7/9} m_0 2^w N^{1/9}
```

for `m_0` odd with distinct states through `N`. Setting the count to `N` and
`w = B log_2 N + C` gives `N^{8/9−B} ≤ 3e^{7/9}·2^C·m_0` — **verbatim**
`EOC/LogCorridor.lean`'s `logFloor_window_bound'`, constant included. The advance
is only that the hypothesis drops from "a floor at every prefix" to "count the
returns".

## Reproduction

CPython standard library only. **Every confinement and congruence decision is
exact integer arithmetic (`2^{S_j} ≤ 2^c·3^j`)**; floats appear only in printed
diagnostics.

```bash
python3 scripts/phi_identity.py      # the master identity, l = 0..60         ~5 s
python3 scripts/carry_bridge.py      # four carry identities, N = 1..40      ~20 s
python3 scripts/return_count.py      # the return bound + injectivity control ~15 s
python3 scripts/theorem_s.py         # the restricted theorem vs real orbits   ~8 s
python3 scripts/counterexamples.py   # the four confined witnesses W1-W4      ~25 s
python3 scripts/realizability.py     # the -1 control; least-realizer checks   ~3 s
python3 scripts/clocks_and_rate.py   # Occupation/Rate.lean sandwich; J(s)    ~4 min
```

`SOURCE_HASHES.txt` records both papers by sha256; neither PDF is redistributed.

## Scope

Nothing here proves, advances or conditionally establishes the Collatz conjecture
or EOC's pointwise divergence exclusion. The geometric model, the conjugacy
formula, the carry and drift identities, the Cramér rate and the harmonic packing
bound are all **prior**; the 2009 expansion is refereed and is López and Stoll's.
**No Lean verification is claimed.**
