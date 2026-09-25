# Correction, 2026-09-25 — the `q > 4` first-step sieve

**The `5x-1` rare-side record ladder published in this audit was computed over a
sieved population that omits half of the admissible seeds. It is wrong from
`N = 2` onward. Open Problem 11 of the synthesis note, which rested on it, is
FALSE.**

Found while reproducing this audit's controls in
[`../pointwise_discovery`](../pointwise_discovery), whose own scanner sieves
nothing.

---

## 1. The defect

`scripts/scan_rare.c` restricts the scan to the residue class the first step
forces, and steps by that class's modulus. The two sides of the family need
different classes, and only one of them was implemented.

Write `d0 = A[1] + 1`, `A[k] = floor(k log2 q)`.

**`q < 4` (the lower, confinement side).** The condition at `n = 1` is
`S_1 <= A[1] = 1`, and `S_1 >= 1` always, so `v2(qm+r) = 1` **exactly**. One class
modulo 4. The old code used modulus `2^{d0+1} = 4` and the class with
`v2 = d0 = 1` exactly — **correct**, which is why the `3x+1` ladder is unaffected.

**`q > 4` (the upper, anti-confinement side).** The condition is
`S_1 >= d0`, a **lower** bound: every first letter `d >= d0` is admissible. The
union of those classes is
```
        v2(q m + r) >= d0      <=>      m == -r q^{-1}   (mod 2^{d0}) ,
```
**one class modulo `2^{d0}`**. The old code took modulus `2^{d0+1}` and the single
class with `v2(qm+r) = d0` **exactly**, i.e. half of the admissible set. Its own
comment — *"larger first letters live in sub-classes of the same modulus"* — is
false: for `(q,r) = (5,-1)`, `v2(5m-1) = 4` means `5m == 17 (mod 32)`, i.e.
`m == 29 (mod 32)`, i.e. `m == 13 (mod 16)`, a **different** class from the
scanned `5 (mod 16)`, not a sub-class of it.

So the defect is a single off-by-one in the modulus, and it costs exactly half of
the `q > 4` seed population.

**The note had the correct algebra already.** Open Problem 11 states that
"`S_1 >= 3` requires `m == 5 (mod 8)`, which splits into `5` and `13` modulo 16,
and the class 13 is admissible yet never least". The first two clauses are right;
the third is the artefact — the class 13 was never looked at.

## 2. What it affects

| item | affected? |
|---|---|
| `scripts/scan_rare.c`, `q > 4` | **yes** — patched here |
| `data/scan_D_raw/part_*.txt` (`5x-1`, `X = 10^12`) | **yes** — rescanned |
| `data/delta1_D.txt` (`Δ₁`, slopes, CIs, `n_eff`) | **yes** — regenerated |
| `data/residues_D.txt` (the `mod 16` census) | **yes** — regenerated |
| `REPORT.md` Items 3 and 5, the `A`-vs-`D` table, §"New insights" | **yes** — corrected |
| `papers/synthesis` Remark 4.10 (`the same null on 5x-1`), §8 items 10 and 11 | **yes** — corrected; item 11 **retracted** |
| `data/scan_A_raw/*`, `data/delta1_A.txt` (`3x+1`) | **no** — `q < 4`, sieve exact. Re-verified, not assumed: the patched scanner re-run over the whole range `[1, 2·10^11)` reproduces **all eight** committed parts **byte for byte** |
| `Proposition (5x-1)` and the shelter/pigeonhole table | **no** — proofs, not scans |
| `audits/fingerprint_comparison` | **no** — its `records.c` and `records2.c` step by 2 over every odd seed and sieve nothing. Its `5x-1` row (`data/records_2x2.txt`, §6 of its report, 52 holders to `X = 5·10^7`) is **correct**, and agrees entry for entry with the corrected ladder here; see §4 |
| `audits/record_holder_anatomy` | **no** — all its scanners are `q = 3`, where the `m == 3 (mod 4)` sieve is exact |
| every Lean library | **no** |

`7x-1` and `7x+1` carry the identical defect in the scanner (the test below shows
it), but no `q = 7` scan was ever published; the note's `7x±1` rows are proofs.

## 3. The fix, and what guards it

`scripts/scan_rare.c` now derives the sieve from the side:

* `q < 4`: one class mod `4`, `v2(qm+r) = 1` exactly;
* `q > 4`: one class mod `2^{d0}`, `v2(qm+r) >= d0`.

For `(5,-1)` that is `m == 5 (mod 8)` — the class the note's own algebra names —
stepping by 8 rather than by 16. The guard is now counted and reported on stderr,
so a truncated depth cannot pass unnoticed; `stdout` still carries only `N m`
lines, so `delta1.py` is unchanged.

`scripts/test_sieve.py` is the regression test. Standard library only, exit 0 iff
all checks pass:

* **T1** — for `q in {5,7}`, `r = ±1`, the patched sieve's arithmetic progression
  equals, by exhaustion over a full period, the set of odd residues admissible at
  step 1; and the old rule is exhibited missing a nonempty admissible subset. For
  `q = 3`, `r = ±1` the old rule is confirmed to have been exact.
* **T2** — for all six maps the sieved C scanner reproduces, to `X = 2^17`, the
  ladder of an **unsieved** pure-Python orbit scan. The sieve loses nothing.
* **T3** — the corrected small-`N` values are pinned as literals, including
  `r_min(2) = 13` for `5x-1` and the explicit assertion that it is not `21`.

`scripts/ladder_ref.py` holds the two independent reference implementations used
below (`scan`: unsieved direct orbit iteration; `tree`: the Terras–Everett class
tree, which enumerates residue classes and never iterates a seed's orbit).

## 4. The corrected ladder, reproduced by three independent implementations

| implementation | principle | language | range | result |
|---|---|---|---|---|
| `scripts/scan_rare.c`, patched | linear scan over the sieved class `m ≡ 5 (mod 8)`, orbit iteration, `__int128` | C | complete to `10^12` | the published ladder below |
| `scripts/ladder_ref.py tree` | Terras–Everett **class** tree: enumerates residue classes, carries each class's least member, prunes on the class modulus; **never sieves and never scans integers** | Python, stdlib | complete to `2^28` (107 654 295 nodes) | **62 holders, deepest `N = 301`** |
| `scripts/ladder_ref.py scan` | direct orbit iteration over **every** odd seed, no sieve of any kind | Python, stdlib | complete to `2^22` | **42 holders, deepest `N = 192`** |
| `../pointwise_discovery/scripts/depth_scan.c` | linear scan with the sieve **removed** (steps by 2) | C | complete to `2^32` | agrees with all of the above on its range |

Every pair agrees **entry for entry** on the range they share:

* patched C at `2^24` == class tree at `2^24` — 49 holders, identical;
* class tree at `2^28` == unsieved C at `2^32` restricted to `m < 2^28` — 62 holders, identical;
* unsieved Python scan at `2^22` == the same restricted — 42 holders, identical.

So the ladder is confirmed by two implementations at `2^32`, by three at `2^28`,
and by three built on two different principles (orbit iteration and class
enumeration) in two languages. The overflow guard fired **0 times** in every run.

### The `3x+1` regression

The patched scanner was re-run over the entire `3x+1` range `[1, 2·10^11)` with
the same 8-way chunking as `run_scan_A.sh`. All eight output files are **byte for
byte identical** to the committed `data/scan_A_raw/part_*.txt`, and the overflow
guard fired 0 times in every worker. The `q < 4` sieve was not merely argued to be
exact; the whole dataset was regenerated and compared.

### A fourth check that was already in the repository, and had been contradicting this audit

`audits/fingerprint_comparison/data/records_2x2.txt` contains a `5x-1` ladder to
`X = 5·10^7`, computed by `records2.c`, which steps by 2 over every odd seed and
**sieves nothing**. It records **52 holders**, beginning

```
5  13  21  45  77  269  349  397  509  1205  3021  4061  10397  ...
```

The corrected `cross_map` ladder restricted to the same `X` gives **exactly those
52 holders, in that order** — verified here, identical. The **old** `cross_map`
ladder restricted to the same `X` gives **35**, beginning `5, 21, 533, 789, ...`.

**So the refutation was already in the repository, in another audit's data file,
and the two were never compared.** Worse, the first version of Item 3 claimed a
cross-check against exactly that file — *"a cross-check at `X = 5·10^7`
reproduces the fingerprint audit's `N = 264` at `39 090 837`"* — but compared only
the single deepest entry, which the sieve happens not to move. Seventeen missing
holders sat underneath it.

That is the operational lesson, and it is more useful than the arithmetic one:
**a cross-check against another dataset must compare the whole object, not its
extreme.** The two audits used different scanners for the same map and agreed on
the one number that was looked at.

## 5. The corrected ladder and every statistic derived from it

Complete rescan of every odd `m < 10^12` in the correct class `m ≡ 5 (mod 8)`,
8 workers, exact `__int128`, **overflow guard fired 0 times in all 8 workers**.
Regenerated with the unchanged `scripts/delta1.py` and `scripts/residues.py`.

| | published (sieved) | corrected (complete) |
|---|---|---|
| distinct record holders | 66 | **93** |
| deepest | `r_min(459) = 848 537 873 557` | unchanged |
| `r_min(2)` | `21` | **`13`** |
| `r_min(13)` | — (not a holder) | **`21`**, and `Δ₁ = −0.3957` |
| `r_min(16)` | `533` | **`45`** |
| `r_min(22)`, `r_min(25)`, `r_min(32)` | `—`, `—`, `789` | **`77`, `269`, `397`** |
| `r_min(100)` | `284 501` | **`142 445`** |
| `Δ₁ > 0` | 66 of 66 | **92 of 93** |
| `Δ₁` range (median) | `1.98 … 14.74` (`8.55`) | **`−0.40 … 14.74` (`7.95`)** |
| OLS slope | `+0.021080` | **`+0.022401`** |
| Theil–Sen slope | `+0.021928` | **`+0.022357`** |
| bootstrap 95 % CI, blocks 3 / 8 / 16 | `[+0.016,+0.023]` / `[+0.012,+0.023]` / `[+0.008,+0.025]` | **`[+0.017,+0.025]` / `[+0.013,+0.025]` / `[+0.009,+0.025]`** |
| implied growth exponent | `0.0534` | **`0.0547`** |
| lag-one `ρ₁`, `n_eff` | `+0.901`, `3.4` | **`+0.938`, `3.0`** |
| residues mod 8 | `{5: 66}` | **`{5: 93}`** — the proved part, still exact |
| residues mod 16 | `{5: 66}` | **`{5: 27, 13: 66}`** |
| residues mod 32 | `{5: 1, 21: 65}` | **`{5: 1, 13: 38, 21: 26, 29: 28}`** |
| `p_N` at every `N` | — | **identical**; the mass recursion was never involved |

**The qualitative reading survives; the numbers moved.** `Δ₁` is still positive
almost everywhere, still grows, and every bootstrap interval still excludes zero —
so insight 3 of `REPORT.md` (`D`'s frontier departs from the null and `A`'s does
not) stands, with `n_eff ≈ 3.0` rather than `3.4`. What does **not** survive is the
`mod 16` residue law: a clear majority of the holders — 66 of 93 — sit in the class
the old scan never visited.

## 6. What a reader should take from this

Two things, neither of them about `3x+1`.

1. **A `verified` label was attached to a scan whose population was narrower than
   the statement it was testing, and the narrowing was visible in the same
   sentence.** Open Problem 11 derived `m ≡ 5 (mod 8)` correctly and then reported
   a `mod 16` law measured on half of that class. The lesson is mechanical: when a
   scan sieves, the sieve belongs in the statement of what was verified.
2. **The asymmetry that caused it is the same one the programme is about.** For
   `q < 4` the rare-side condition is an upper bound on `S_1` and pins the first
   letter; for `q > 4` it is a lower bound and does not. Sieving as though the two
   sides were symmetric halves the population. That the rare side is a bound *in a
   different direction* on the two sides of `q = 4` is exactly why `3x+1` has no
   pigeonhole and `5x-1` does.

Nothing here bears on (DE), on Open Problem C, or on the Collatz conjecture.
