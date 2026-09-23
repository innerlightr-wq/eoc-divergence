# After the reduction — the synthesis note

> De Jesús, Elias (2026). *After the Reduction: Proved Statistics, Excluded Structure, and the
> Missing Pointwise Tool in the Accelerated 3x+1 Problem*. Zenodo.
> [doi:10.5281/zenodo.22925399](https://doi.org/10.5281/zenodo.22925399)

A standalone expository research note reporting what the programme has proved, what it has
excluded, and what kind of tool the remaining problem would require. It is written for a reader
who has not seen the programme before.

**It makes no claim of progress toward the Collatz conjecture**, and says so in the abstract, in
the introduction, and in the closing line of the open-problems section.

## Contents

| | |
|---|---|
| `main.tex`, `refs.bib` | the note; `make` builds `main.pdf` |
| `CHECKPOINT1.md` | the outline, the exact wording of every numbered statement, and a 41-row ledger giving each claim's label and source |
| `SELF_AUDIT.md` | the self-audit: labels, sources, non-claims, citations, and a record of every correction made during drafting |

## Claim labels

Every substantive claim in the note carries one of **proved (lean)** · **proved (paper)** ·
**cited** · **verified** · **heuristic** · **conjecture** · **open**. `SELF_AUDIT.md` records the
census and confirms that no other label is used.

## Building

```bash
make            # pdflatex, bibtex, pdflatex x2
```

`main.pdf` is not tracked.
