# 06_EOC_TRANSFER.md

Each established EOC structure, tested for whether it controls the lift sequence.

| structure | does it control `J`? | why |
|---|---|---|
| **Carry budget / `C_n`** | **no — it *is* the lift sequence** | `b_n ≡ −(3m_n+1)3^{−(n+1)}` with `m_n = (3^n r_n + C_n)/2^{S_n}`.  The lift sequence is a repackaging of the carry, not an independent handle.  Per the separability identity of the October 16 audit, no difference of `C_N` carries new information either. |
| **Confinement slack `g_n`** | **no** | `04_...`: the apparent effect is a continuation-count weighting artefact; after counting each prefix once, `P(lift)` matches `1−2^{−d_n}` to `±0.021`. |
| **Occupation bounds `O_c`** | **not applicable** | `O_c` counts corridor visits of the *drift*; `J` counts valuation overdrafts of the *realizer*.  No implication either way was found, and `b_n`'s dependence on `(d_0..d_n)` only means `J` cannot see the drift's future. |
| **Future-minimum behaviour** | **no** | under infinite confinement `2^{S_n}m_n = 3^n m_0 + C_n > 3^n m_0 ≥ 2^{S_n}m_0`, so `m_n > m_0` always (Rev 8).  That is a statement about the *orbit*, and holds whether or not lifts occur. |
| **Episode entrances/exits** | **no connection established** | Target C was not reached: `05_...` shows `J` is unconstrained by confinement, so there is no lift-side quantity for an episode inequality to bound.  I did not pursue it further; see `07_...` Target C. |
| **Drift / tail estimates** (Garcia–Tal, Curry) | **not transferable as used** | these bound the drift `R_n` along *divergent orbits*; they say nothing about the congruence-word population, which contains the all-ones word with `x = −1`. |
| **`r_min` frontier** | **yes, and this is the honest connection** | `05_...`: `min J(N)` is pinned by the least integer admitting a length-`N` confined congruence word — i.e. by the `r_min` frontier, whose envelope the programme has already measured (stuck at `10.2953`) and **retired**.  The lift route reaches the same quantity by a different name. |
| **Lemma O** (confinement vs height) | **not needed and not retried** | no divisibility-to-size step appears anywhere above; the obstruction here is different and prior. |

## The one genuine transfer

The lift criterion L2 gives a clean dictionary entry:
```
J(N) = # { n < N : v_2(3 m_n + 1) < d_n } ,     m_n = (3^n r_n + C_n)/2^{S_n} ,
```
i.e. **the number of times the word demands a deeper valuation than its running least realizer
supplies.**  This is a correct and, I think, clarifying way to say what the realizer sequence is
doing.  It is a *definition made explicit*, not a new inequality, and §07 classifies it
accordingly.
