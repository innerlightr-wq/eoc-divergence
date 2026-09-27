# Scope correction: the thin-band finite evaluations

**The corrected statement.** A6's asymptotic conclusion rests on the analytic proof **together with
uniform control of the remainder**. The exact evaluations at `B = 100, 200, 320, 640` **cross-check
the finite bound** `q·N·T_δ(N,s,j)/C(s−1,N−1)` and nothing more.

They do **not**:
- prove any statement for every `B ≥ 100`;
- establish `B₀ = 100`, or identify any threshold.

**Explicit versus existential.** For

```
H_s^thin ≤ C · 2^{−B/20} · (L_s/q)      for B ≥ B₀,
```

the constants are **existential only**, in both cases:

| constant | status |
|---|---|
| `C` | **existential.** It absorbs the `2^{O(log N)}` polynomial factor from the binomial entropy bounds and the floor/ceiling slack in `N = ⌈κB⌉`, `j = ⌊N/2⌋`, `⌊δN⌋`. No explicit value is derived. |
| `B₀` | **existential.** It is the point beyond which `γB` dominates that polynomial factor. No explicit value is derived, and in particular **`B₀ = 100` is not claimed**. |

What *is* explicit is the exponent: `γ(13/20, 1/10) = 1 − κ[α − Δ_δ(α)] = 0.054816179871361`, with
`Δ_{0.1}(α) = 0.130833546677096`, and the exponent `−B/20 = −0.05B` is a convenient weakening of
`−γB` since `0.05 < γ`. The certification of `γ > 0` by rational arithmetic rather than decimals is
listed as step 4 of A6 in `DEPENDENCY_PLAN.md` and is **not** done.

**Kept separate.** The open weighted bulk estimate `(*)` and its conditional numerical payoff
(exponent `0.949651926715094`, improvement `0.000303600473237`) are recorded in
`PROVENANCE.md` under "Open" and must not be read as established results. **No exceptional-set
exponent improvement has been obtained.**
