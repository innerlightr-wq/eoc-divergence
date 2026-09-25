# audits/sturmian_all_words

**Verdict: PROVED.** `Φ(s) ∉ Q` for **every** Sturmian word `s` — every irrational
slope, every intercept, both mechanical words.

| file | contents |
|---|---|
| [`REPORT.md`](REPORT.md) | I1–I4 with proofs and citations, verification tables, controls, novelty, verdict |
| [`DRAFT_SECTION.md`](DRAFT_SECTION.md) | draft §9 "All Sturmian words" in LaTeX, bibliography entries, implied edits elsewhere — **not inserted in the paper** |
| `scripts/` | exact-arithmetic verification (slopes/intercepts over `2^512`; certified floors) |
| `data/` | script outputs |

## Route

| step | content | status |
|---|---|---|
| I1 | every Sturmian word begins in infinitely many squares, so `ice ≥ 2` | **CITED** (ADQZ 2001; DKL 2000; quoted from BHZ 2006 §1) |
| I2 | the primitive root of an initial square is a conjugate of a standard word, so `W^∞` is balanced | **CITED** (BHZ 2006, Prop. 3.2) |
| I3 | `0 < c_W ≤ 3·ℓ·max(2^ℓ, 3^k)` for `W` a Christoffel conjugate | **PROVED** (`C = 3`); `C = 1` **VERIFIED** for `ℓ ≤ 40` |
| I4 | Liouville: `c(γ)·ℓ ≤ log₂H + log₂(2+3ℓ) + log₂3`, `c(γ) ≥ 2 − log₂3` | **PROVED** |

## Reproducing

```bash
python3 scripts/i1_squares.py       # I1 across 4 slopes x 6 intercepts
python3 scripts/i1_adversarial.py   # I1 over 12 000 random intercepts
python3 scripts/i2_i3_i4.py         # I2 (48/48), I3 (max ratio 0.4394), I4 margins
python3 scripts/controls.py         # rational slope, Thue-Morse, 0^a1^a, balance witnesses
```

Standard library only. Every decision is exact integer arithmetic;
`safety_margin` certifies each floor (≥ 496 bits of margin in every run).

**The paper was not edited.**
