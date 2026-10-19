# Running the checks

Pure Python 3, standard library only (`math`, `fractions`, `itertools`, `collections`).
No dependencies, no data files required. Exact integer / rational arithmetic throughout;
floating point is used only for the drift `H_j = jα − S_j` and the reported exponents,
and every confinement test is the exact integer comparison `2^{S_j} ≤ 3^j`.

```sh
python3 scripts/eoc_switch.py     >  data/eoc_switch.out       # ~1 min
python3 scripts/eoc_precision.py  >  data/eoc_precision.out    # ~12 min
python3 scripts/eoc_tree.py       >  data/eoc_tree.out         # ~6 min
```

The committed outputs in [`../data`](../data) are the results of exactly these commands.

| script | lemmas checked (see [`../LEMMAS.md`](../LEMMAS.md)) |
|---|---|
| `eoc_switch.py` | 1 (switch decomposition), 2 (margin–switch), 3 (mechanical extremal) |
| `eoc_precision.py` | 5 (bit loss), 6 (precision budget), 7 (minimal automaton), and pinning |
| `eoc_tree.py` | 8 (tree conservation / duality), 10 (exponent identity), and the selection ratio `Q` with the `3x−1` control |

Each script prints the size of every enumeration it performs and the number of
violations found, so the counts quoted in `LEMMAS.md` can be checked directly against
the output rather than taken on trust.
