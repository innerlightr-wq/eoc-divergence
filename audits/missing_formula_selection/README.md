# Reproduction: the finite-height selection factor

Scripts backing [`../../notes/MISSING_FORMULA_SELECTION_LAW.md`](../../notes/MISSING_FORMULA_SELECTION_LAW.md).
Pure Python 3, standard library only (`math`, `fractions`, `itertools`, `collections`).
No dependencies, no input data, no arguments. Exact integer and rational arithmetic
throughout; floating point appears only in reported logarithms and in the drift
`H_j = jα − S_j`, and every confinement test is the exact integer comparison
`2^{S_j} ≤ 3^j`.

```sh
python3 bit_loss.py
python3 cylinder_mass.py
python3 qratio.py
python3 control_3xminus1.py
python3 per_cylinder_survival.py
python3 hazard_null.py
python3 shell_discrepancy.py
```

The captured output of exactly these seven commands, in this order, is
[`repro.txt`](repro.txt).

| script | what it checks | note |
|---|---|---|
| `bit_loss.py` | bit-loss law `K_n = K_0 − S_n`; precision budget `m mod 2^{S_L+1}`; minimal-automaton saturation | §2.4 |
| `cylinder_mass.py` | switch decomposition; margin–switch tradeoff; automatic confined-height bound; cylinder conservation; precision/multiplicity duality; exponent identity `h + I₀ = α` | §2.1–2.6 |
| `qratio.py` | the identity `A_{N,M} = Q_{N,M} O_M p_N`; extinction depths; the exact relation to `Δ_N`, checked on exact rationals | §3, §5 |
| `control_3xminus1.py` | `3x+1` versus `3x−1` at `M = 2^16 − 1` | §7 |
| `per_cylinder_survival.py` | the exact `Q = 1` plateau and `N*(B)`; the per-cylinder survival formula and its converse; the all-ones realizer `2^{N+1} − 1`; the barrier-cell counterexamples behind the retraction | §2.7a–c, §8 |
| `hazard_null.py` | barrier-conditioned feature sweep (`m_N mod q`, valuations, height) with shuffle and `3x−1` controls; held-out heights; the `g = g_comp + g_arith` split | §2.7d–e |
| `shell_discrepancy.py` | the closed-form realizer verified forward; the sawtooth count and null rate `u = (t+1)/q_w`; the shell identity `A − O_M p_N = Σ_S n_S D_S`; realizer-position uniformity | §5.1 |

Each script prints the size of every enumeration it performs and the number of
violations found, so the counts quoted in the note can be checked against the output
rather than taken on trust. `per_cylinder_survival.py` and `shell_discrepancy.py` use
`assert` for their structural claims, so a broken invariant stops the run rather than
printing a wrong number.

Measured runtimes (single core, CPython 3, whole suite ≈ 1 min 50 s):
`bit_loss.py` 4 s, `cylinder_mass.py` 3 s, `qratio.py` 2 s, `control_3xminus1.py` < 1 s,
`per_cylinder_survival.py` 5 s, `hazard_null.py` 43 s, `shell_discrepancy.py` 50 s.
(Earlier revisions of this file quoted minutes per script; those figures were wrong and
are corrected here against a timed run.)

`shell_discrepancy.py` enumerates 13,472,296 confined words at `N = 20` and is the
longest run; it forward-verifies every realizer at `N = 12` and `N = 16` and a uniform
1-in-33 sample (408,251 realizers) at `N = 20`.

**Scope.** Nothing here proves anything about (DE) or the Collatz conjecture. The
identity defining `Q` is definitional; the measurements are finite-range; the
boundedness of `Q` is open and is at least as strong as (DE). See the note.
