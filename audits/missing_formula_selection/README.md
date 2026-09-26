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
```

The captured output of exactly these four commands is [`repro.txt`](repro.txt).

| script | what it checks |
|---|---|
| `bit_loss.py` | bit-loss law `K_n = K_0 − S_n`; precision budget `m mod 2^{S_L+1}`; minimal-automaton saturation |
| `cylinder_mass.py` | switch decomposition; margin–switch tradeoff; automatic confined-height bound; cylinder conservation; precision/multiplicity duality; exponent identity `h + I₀ = α` |
| `qratio.py` | the identity `A_{N,M} = Q_{N,M} O_M p_N`; extinction depths; the exact relation to `Δ_N`, checked on exact rationals |
| `control_3xminus1.py` | `3x+1` versus `3x−1` at `M = 2^16 − 1` |

Each script prints the size of every enumeration it performs and the number of
violations found, so the counts quoted in the note can be checked against the output
rather than taken on trust.

Runtimes on a commodity machine: `bit_loss.py` ≈ 12 min, `cylinder_mass.py` ≈ 4 min,
`qratio.py` ≈ 3 min, `control_3xminus1.py` ≈ 2 min.

**Scope.** Nothing here proves anything about (DE) or the Collatz conjecture. The
identity defining `Q` is definitional; the measurements are finite-range; the
boundedness of `Q` is open and is at least as strong as (DE). See the note.
