# Audit corrections

Four alleged issues investigated. **Two upheld and fixed in code, one upheld as an overclaim in
prose, one correct mathematics attributed to the wrong parameter range.** The prior review was
treated as a list of claims; every one was checked against the files.

## A1 — circular failure offset in `per_cylinder_survival.py`: **UPHELD, FIXED**

**The concern is correct.** The committed code read

```python
cls = {t % (1 << K) for t in fails}      # <- from OBSERVED failures
assert len(cls) == 1
ts = cls.pop()
pred = n - ((n - 1 - ts) // (1 << K) + 1) if ts < n else n
```

so the offset `ts` was extracted from the observed failure labels and the counting formula was
then checked against that same offset. What the old code genuinely verified was (i) that the
failures form **one** residue class mod `2^K` and (ii) the floor arithmetic. The **offset itself
was fitted**, and the no-failure branch (`else: pred = n`) was a tautology.

**Independent derivation (DERIVED HERE).** For a prefix `w` of length `N` with `S = S_w`,
`C = C_w`, `q_w = 2^{S+1}`, least exact realizer `r_w`, put `x_w = (3^N r_w + C_w)/2^S`. Lifted
seeds `r_w + q_w t` have endpoint `m_N(t) = x_w + 2·3^N t`. Since `x_w` is **odd** (terminal
parity — verified, 0 exceptions on 12,447 words), `3x_w+1 = 2y` with `y = (3x_w+1)/2`, so
```
3 m_N(t) + 1 = 2 (y + 3^{N+1} t),    v₂(3m_N(t)+1) = 1 + v₂(y + 3^{N+1} t),
failure ⟺ v₂(3m_N(t)+1) > K ⟺ y + 3^{N+1}t ≡ 0 (mod 2^K) ⟺ t ≡ t*_w := −y·3^{−(N+1)} (mod 2^K).
```
`K` comes from zero confinement at step `N+1`: `K = max{a : 2^{S+a} ≤ 3^{N+1}} = ⌊(N+1)α − S⌋`.
Since confinement gives `S ≤ ⌊Nα⌋`, `(N+1)α − S ≥ α > 1`, so **`K ≥ 1` always** — asserted, not
assumed, and verified on all 12,447 confined words of length ≤ 12 (0 violations). The `K = 0`
boundary case therefore cannot arise for confined words; had it arisen, every lift would fail
(`3m+1` is always even).

**The brief's proposed formula is correct.** Verified with the offset computed *before* any
failure label was consulted: 3,241 `(w,B)` cylinder cases, **0** failure-count mismatches, **0**
cases where the observed failure class differed from the predicted `t*_w`. Every listed edge case
was reached, none skipped: no failures with `t* ≥ n` (2,437), exactly one failure (617), multiple
failures (187), `t*` outside the sampled interval (2,437), **extinction at the next depth (405)**,
`n = 1` (2,504). `repro/a1.out`.

**Code change** (commit `b57b152`): the offset is now predicted from the closed form and the
observed class is compared against it; `x_w` integrality and oddness and `K ≥ 1` are asserted; a
new counter reports disagreements. Re-run: 311,844 cylinders, 0 survival-formula failures,
**0 predicted-offset disagreements**.

**Limitation.** The verified statement is still finite-range (`B ≤ 20`, all depths). The exact
per-cylinder law in the note is unaffected — it is now non-circularly verified rather than
partially fitted.

## A2 — incomplete word verification in `shell_discrepancy.py`: **UPHELD, FIXED**

**The concern is correct.** The committed forward check was
`if not ok or Ssum != S: mismatch += 1` — only zero-confinement and the **total** valuation
`S_N`, never the word — and it ran on a 1-in-`⌈n/400000⌉` sample (408,251 of 13,472,296 at
`N = 20`).

**Code change** (commit `b57b152`): the DFS now carries the word, and the check asserts
letter-by-letter equality plus an odd terminal endpoint, **exhaustively** (`verify_cap = None`).
Re-run: 8,045/8,045 (`N=12`), 312,455/312,455 (`N=16`), **13,472,296/13,472,296** (`N=20`),
0 mismatches. Independent cross-check against brute-force least-seed search for `N ≤ 12`:
0 mismatches (`repro/a2a3a4.out`).

**Limitation.** On the tested range the weaker `(confinement, S_N)` test happened to agree with
full-word equality (0 words distinguished them), so the defect was a verification gap rather than
a latent wrong number. The exact-identity results of §5.1 are unchanged.

## A3 — "every non-2-adic feature is exactly uninformative": **UPHELD as an overclaim**

**The brief's finite example is correct**, verified exactly: `w = (1)` gives `S = 1`, `C = 1`,
`q_w = 4`, `r_w = 3`, `K = 2`; seeds `≤ 15` are `3, 7, 11, 15`; next odd states `5, 11, 17, 23`;
following valuations `4, 1, 2, 1`; only the first exceeds `K = 2`; and `m_1 ≡ 0 (mod 5)` selects
exactly that one.

**Why, and the correct statement (DERIVED HERE).** `m_N(t) = x_w + 2·3^N t`, so for odd `u` the
feature `m_N mod u` determines `t mod u` (`2·3^N` is invertible mod `u`). Uninformativeness
requires `t mod u` to be independent of `t mod 2^K`, which needs the lift sample to cover a
complete period of the **joint** modulus `u·2^K` — not of `2^K`.

I first tested this over a `2^K` period and got a **large** deviation (0.875), which is correct
and instructive: over one `2^K` period there is exactly **one** failing `t`, so its residue mod
`u` is determined and the feature *is* informative. Over a `u·2^K` period the deviation is
**exactly 0** for `u = 3,5,7,9` (`repro/a3_fixed.out`). `u = 3` is uninformative over any period
because `m_N ≡ x_w (mod 3)` is constant on the cylinder — consistent with the note's §2.4
statement that `m mod 3` restricts nothing.

**Verdict.** The note's sentence *"every non-2-adic feature is exactly uninformative"* overclaims.
The strongest supported replacement:

> `a_N` is a function of `t mod 2^K` alone. Hence any feature is informative only insofar as it
> reveals `t mod 2^K`. Over a lift sample covering a complete period of the joint modulus
> `u·2^K`, a feature `m_N mod u` (`u` odd) is exactly uninformative; on a truncated cylinder it
> can be informative, but only through the truncation, and it reveals nothing beyond `t` itself.

**This is not a new mechanism and no feature sweep was restarted.** A finite correlation arising
from truncation is not an exclusion mechanism. The note's §2.7(d) *measurements* (held-out
anti-transfer, `3x−1` control) are unaffected; only the parenthetical universal claim is wrong.
**Prose change deliberately NOT made** in this task: editing `notes/` was out of scope here; the
correction is recorded for the note's next revision.

## A4 — all-shell absolute-Fourier obstruction: **correct mathematics, wrong range**

Verified under `ShellWeyl`'s actual normalization:
- `shell U N s` with `s = N` contains **exactly one** word, `1^N` (`#shell = 1` at `N = 4…20`).
- Its exact least realizer is `2^{N+1}−1` (verified `N = 4…20`, and `N = 1…24` in the script).
- `n = s+1−K = N+1−K`; a singleton `T` gives `‖blockWeyl g‖ = 1` for **every** `g`, so
  `Σ_{g≠0}‖shellWeyl g‖ = 2^n − 1`.
- `WeylBound` then forces `(C−1) ≥ 2^n − 1`, i.e. **`C ≥ 2^d`**, `d = N+1−K`. The brief's claim
  is confirmed.
- And `r_w(1^N) = 2^{N+1}−1 < 2^K ⟺ d ≤ 0`. So whenever the shell is in scope (`d ≥ 1`) the true
  below-cutoff count is **0** while the main term is `#shell/2^n = 2^{−d} > 0`: the exact signed
  discrepancy is `−2^{−d}`, **favourable**, and destroyed by taking absolute values.

**But `WeylBound` quantifies only over `s ≥ K`.** With `K = B` and `N = ⌈κB⌉`:

| `κ` | `N` (at `B=100`) | `s=N ≥ K`? | `d = N+1−K` | forces |
|---|---|---|---|---|
| 0.65 | 65 | **no** | −34 | — |
| 0.95 | 95 | **no** | −4 | — |
| 1.00 | 100 | yes | 1 | `C ≥ 2` |
| 1.20 | 120 | yes | 21 | `C ≥ 2^{21}` |

**Verdict.** The obstruction is real and bites **only for `κ ≥ 1`**, where it rules out a
uniform constant `C` in the absolute-value form of `WeylBound`. At the Phase B target `κ = 0.65`
the shell `s = N` has `s < K` and is already fully resolved as a complete cylinder, so the
obstruction does not apply. It does **not** invalidate the conditional Lean theorems
(`leastRealizerBound_of_weyl`, `exceptional_count_le_of_weyl`), which are correct implications
from a hypothesis; it constrains the parameter range in which that hypothesis can hold with a
constant. It also confirms the brief's methodological warning: the `| · |` step in
`card_filter_lt_le` discards favourable negative terms, so any route at `κ ≥ 1` must keep the
discrepancy **signed**.
