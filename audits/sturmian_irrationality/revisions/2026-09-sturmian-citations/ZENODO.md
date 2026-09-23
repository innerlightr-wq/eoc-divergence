# Zenodo — new versions of notes (A) and (B)

**Published 23 September 2026.** DOIs below are filled in and were verified against the Zenodo
API on that date; see *Publication check* at the foot of this file, which records a discrepancy
in the deposited file sets of both records.

Paste-ready text for the two new versions, retained as the record of what was deposited.

**File set for each new version — exactly two files:**

1. the **original PDF, byte-identical**, filename unchanged;
2. the **addendum PDF**.

Do not re-upload a modified original. The whole point of the addendum route is that the deposited
record of record stays as published and the correction travels beside it.

> **Reminder before publishing:** neither addendum mentions the forthcoming irrationality note,
> and neither makes an irrationality claim. That is deliberate and should stay that way until the
> manual Google Scholar / zbMATH cited-by sweep is done.

---

## Record 1 — note (A)

**Record:** `10.5281/zenodo.22916962` — https://doi.org/10.5281/zenodo.22916962
**Concept DOI:** `10.5281/zenodo.20556483` ← **cite this**
**Superseded:** `10.5281/zenodo.22916798` (incomplete file set — addendum only, no note)

**Record title** (as deposited — *not* the note's own title):

```
Structured Sectors of the Collatz Carry Equation:
Christoffel Towers, 2-Adic Windows, and Shell Residents
```

The note itself renders as *The 2-Adic Sturmian Carry Constant in the Collatz Carry Equation*.
Note (A) lives inside this umbrella record, so anyone following the DOI lands on the collection,
not on a record named after the note. Cite it as: De Jesús, E. (2026). *Structured Sectors of the
Collatz Carry Equation: Christoffel Towers, 2-Adic Windows, and Shell Residents.* Zenodo.
https://doi.org/10.5281/zenodo.22916962

**Files:**

| file | note |
|---|---|
| `AdicSturmianCarryConstant.pdf` | original, unchanged |
| `A_addendum.pdf` | new — "Citation addendum and correction", September 2026 |

**Version:** `v2` (or the next in sequence)

**Version description / changelog** — paste into the description field, above the existing
abstract, or into the version notes:

```
Version 2 (September 2026) — citation addendum and one correction. The PDF of the original note
is unchanged; a separate two-page addendum is added.

The addendum:

(1) Supplies a citation the original note omitted: J. López and P. Stoll, "The 3x+1 conjugacy map
    over a Sturmian word", Integers 9 (2009), #A13, 141-162. Their Theorem 1 gives, in Z_2, a
    closed alternating series for the Bernstein-Lagarias conjugacy value of the characteristic
    Sturmian word, indexed by consecutive continued-fraction convergents. In this note's
    coordinates its term exponents are p_n + p_{n+1} - 1, the lower-convergent depths of
    Theorem 7.1. The approximants and the approximation depths are theirs.

(2) Qualifies the note's description of its result as the tower's "first theorem-grade structural
    result". It is not first. Theorem 7.1 remains an independent derivation, and is sharper in one
    respect: it separates the upper (p_n - 1) and lower (p_n + p_{n+1} - 1) convergent cases and
    pins each constant exactly, shell by shell, which the alternating series does not.

(3) Records the dictionary between the two normalizations, including the sign:
    Xi_alpha = -Phi(1c_{ln2/ln3}), where López-Stoll's slope is the ones-density ln2/ln3 = 1/alpha
    and their convergent (p_k, q_k) is this note's shell (q_n, p_n) with numerator and denominator
    exchanged. Verified modulo 2^3000. It also records that only the odd-indexed continued-fraction
    convergents of López-Stoll are periodic cycle values; the even ones carry an extra gap term.

(4) Pins the range of Theorem 7.1. Its proof, through Lemma 5.1, uses q_n >= 2 and q_{n+1} > q_n,
    which hold from the shell (2,3) onward: the theorem holds as proved for n >= 3 in the note's
    own numbering. The two initial shells (1,1) and (1,2) lie outside the proof's scope; the
    formula returns the correct valuations there (2 and 1) by direct computation, as an
    observation only.

(5) Corrects one typographical slip. In the proof of Lemma 5.1, lower case, the line
    "m_{j*} + j*|R_n| = q_n + q_n|R_n| - |R_{n+1}| > q_n" should read
    "m_{j*} + j*|R_n| = q_n + q_n|R_n| - q_n|R_{n+1}| > q_n". The factor q_n was dropped from the
    last term. No statement is affected: the inequality follows from |R_n| > |R_{n+1}|, and
    Lemma 5.1, Theorem 7.1, Proposition 8.1 and the computational ledger of Section 10 are
    unchanged.

No theorem, proof or computed value of the original note changes, and no new mathematical claim is
made.
```

**Related identifiers — add:**

| relation | identifier | resource type |
|---|---|---|
| References | `10.1515/integ.2009.014` | Publication / Journal article |
| References | `arXiv:2101.12747` | Preprint |
| References | `10.4153/CJM-1996-060-x` | Publication / Journal article |
| Is new version of | *(auto-filled by Zenodo)* | |

**Keywords — add:** `conjugacy map`, `Sturmian word`, `2-adic`, `continued fraction`.

---

## Record 2 — note (B)

**Record:** `10.5281/zenodo.22917246` — https://doi.org/10.5281/zenodo.22917246
**Concept DOI:** `10.5281/zenodo.20594173` ← **cite this**
**Superseded:** `10.5281/zenodo.22916849` (note only, no addendum) and
`10.5281/zenodo.22917066` (note deposited twice, addendum missing)

**Record title** (unchanged, matches the note):

```
The Sturmian–Mahler Edge of the Accelerated Collatz Realizer Problem
```

**Files:**

| file | note |
|---|---|
| `SturmianMahlerEdgeAcceleratedCollatzRealizerProblem.pdf` | original, unchanged |
| `B_addendum.pdf` | new — "Citation addendum", September 2026 |

**Version:** `v2` (or the next in sequence)

**Version description / changelog:**

```
Version 2 (September 2026) — citation addendum. The PDF of the original note is unchanged; a
separate two-page addendum is added.

Section 9 of the note audits the literature gate around the 2-adic value Xi_{alpha,beta}, stating
in each case the hypothesis that excludes the Collatz evaluation point. That audit omitted the
closest prior work on the object itself. The addendum:

(1) Adds J. López and P. Stoll, "The 3x+1 conjugacy map over a Sturmian word", Integers 9 (2009),
    #A13, 141-162, and "The 3x+1 periodicity conjecture in R", arXiv:2101.12747, as a further
    bullet in the Section 9 gate, in the same form as the others -- with the hypothesis that
    excludes our point. The 2009 paper gives the 2-adic series and continued-fraction expansion of
    Phi(1c_alpha) for every irrational slope, then proves irrationality of the REAL values
    Phi_R(m_alpha) on Q ∩ (ln2/ln3, 1], with a dual construction below ln2/ln3. The 2021 paper
    proves aperiodicity for ones-density strictly above ln2/ln3. Both are excluded at our slope by
    the domain hypothesis: the real series converges exactly when ln2/ln3 < p/q <= 1, and the
    staircase F diverges at x = ln2/ln3 -- their own Lemma 27 calls it "the divergent series
    -Phi_R(1c_alpha)". This is the same resonance as Theorem 6.5(ii) of the note, reached
    independently by the authors of the closest prior work.

(2) Records the dictionary identifying the note's object with theirs: in parity-vector coordinates
    Xi_{alpha,beta} is a value of the Bernstein-Lagarias conjugacy map on a Sturmian parity word,
    and at beta = 0, Xi_{alpha,0} = +Phi(1c_{ln2/ln3}). Sign checked against the note's own
    Theorem 4.1 and Remark 4.2; identity verified modulo 2^3000.

(3) Qualifies one sentence of Remark 11.1. "Rational 2-adic => eventually periodic valuation word"
    is described there as "the open periodicity conjecture". It is open at our slope, but not
    everywhere: López-Stoll (2021) prove it for ones-density strictly greater than ln2/ln3, and
    their Theorem 1 shows a rational divergent trajectory would have density exactly ln2/ln3. The
    critical density is precisely the case their method does not reach. The rest of Remark 11.1,
    including the 3x+q equivalence and that Corollary 5.6 settles only q = 1, is unaffected.

(4) Adds context to Open Problem 1, which stands verbatim: the archimedean analogue is a theorem
    off the critical slope, and neither López-Stoll result covers alpha = ln2/ln3, where the real
    series diverges. The 2-adic problem is not a corollary of theirs.

No theorem, proof or numerical result of the original note changes, and no new mathematical claim
is made. In particular nothing here bears on irrationality of Xi_{alpha,beta}, which remains
Open Problem 1.
```

**Related identifiers — add:**

| relation | identifier | resource type |
|---|---|---|
| References | `10.1515/integ.2009.014` | Publication / Journal article |
| References | `arXiv:2101.12747` | Preprint |
| References | `10.4153/CJM-1996-060-x` | Publication / Journal article |
| References | `10.1090/S0002-9939-1994-1186982-9` | Publication / Journal article |
| Is new version of | *(auto-filled by Zenodo)* | |

**Keywords — add:** `conjugacy map`, `periodicity conjecture`, `Hecke–Mahler`, `2-adic`.

---

## Two bibliographic details, flagged but not changed

Not part of this revision; decide before or after publishing, as you prefer. Note (B)'s
bibliography gives Bugeaud–Laurent as Acta Arith. **209** (2023), 59–**90** and
Luca–Ouaknine–Worrell as Bull. LMS **57** (2025), 1360–**1368**; the publisher records collected
in `references.bib` give 59–**75** and 1360–**1374**. Reference [20] also runs its DOI URL into
the preceding sentence without a space.

---

## Publication check — 23 September 2026

Every record was read from both `https://zenodo.org/api/records/<id>` and the dedicated `/files`
endpoint, and every file matched by **MD5** against the local artefact, never by size alone.

### Version history

| | superseded | superseded | current | concept DOI |
|---|---|---|---|---|
| (A) | `22916798` addendum only | — | **`22916962`** ✅ | `20556483` |
| (B) | `22916849` note only | `22917066` note twice | **`22917246`** ✅ | `20594173` |

### (A) `10.5281/zenodo.22916962` — ✅ **complete**

| file | size | md5 | is |
|---|---|---|---|
| `AdicSturmianCarryConstant (1).pdf` | 299 604 B | `8064824b9605a0ad26603ed742022842` | the note |
| `A_addendum.pdf` | 403 241 B | `de6e65cfa6fbbddbb7faf062c38fe685` | the addendum |

### (B) `10.5281/zenodo.22917246` — ✅ **complete**

| file | size | md5 | is |
|---|---|---|---|
| `SturmianMahlerEdgeAcceleratedCollatzRealizerProblem (1).pdf` | 327 659 B | `830ff7dc768ed1a692e9b050a5e28fa0` | the note |
| `B_addendum.pdf` | 390 796 B | `3ecb5e274e5603249f9168dddb314125` | the addendum |

Exactly two files, note and addendum, both byte-identical to the local artefacts. The duplicate
is gone.

**One naming note, cosmetic only.** The copy of the note that survived in (B) is the one named
`SturmianMahlerEdgeAcceleratedCollatzRealizerProblem (1).pdf`; `B_Sturmian_Mahler_Edge.pdf` is the
name that disappeared. Both records therefore now serve their note under a `~/Downloads`-style
filename carrying a ` (1)` suffix — (A) as `AdicSturmianCarryConstant (1).pdf`. The content is
right and the MD5s prove it; only the download filename a reader sees is untidy. Renaming would
cost another version of each record, which is not worth it.

### Citation guidance

Cite the **concept DOIs** — `10.5281/zenodo.20556483` for (A), `10.5281/zenodo.20594173` for (B).
They resolve to the latest version, so they survive any future revision, and they are what
`references.bib` carries in the `doi` field of both entries.

### Superseded versions, and why

| version | what was wrong |
|---|---|
| `22916798` (A) | held `A_addendum.pdf` only — the addendum with no note to attach it to |
| `22916849` (B) | held the note only — no addendum, so none of the López–Stoll citations |
| `22917066` (B) | held the note **twice** under two filenames, identical md5; addendum still absent |

Caught by reading each record back and comparing MD5s. A size-only or file-count check would have
passed `22917066`, which had the right number of files and plausible sizes.
