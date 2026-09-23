# Sources for the Sturmian irrationality audit

Third-party papers are **not** committed to this repository, which is public.
Local copies live in this directory and are git-ignored; this file records where
each one came from, so the audit is reproducible from the URLs. The audit
reports quote only the passages they discuss.

Retrieved 2026-09-22/23 unless noted. `pdftotext -layout <file>.pdf <file>.txt`
reproduces the text extractions that the reports cite by line number.

## Third-party (local only, git-ignored)

| local file | work | where |
|---|---|---|
| `LopezStoll_2009_Integers9_A13.pdf` | J. López and P. Stoll, *The 3x+1 conjugacy map over a Sturmian word*, **Integers 9** (2009), #A13, 141–162. doi:[10.1515/integ.2009.014](https://doi.org/10.1515/integ.2009.014) | open access, <https://math.colgate.edu/~integers/vol9.html> |
| `LopezStoll_2021_2101.12747.pdf`, `ls.txt` | J. López and P. Stoll, *The 3x+1 Periodicity Conjecture in R*, arXiv:2101.12747**v1**, 29 Jan 2021, 51 pp. Unpublished: no journal reference, no later version. doi:[10.48550/arXiv.2101.12747](https://doi.org/10.48550/arXiv.2101.12747) | <https://arxiv.org/abs/2101.12747> (CC BY 4.0) |
| `Lagarias_bibliography_II.pdf`, `lag.txt` | J. C. Lagarias, *The 3x+1 Problem: An Annotated Bibliography, II (2000–2009)*, arXiv:math/0608208**v6**, 12 Feb 2012 | <https://arxiv.org/abs/math/0608208> |

Phase 1c-B adds two more, recorded in
[`../phase1cB/sources/SOURCES.md`](../phase1cB/sources/SOURCES.md): Monks &
Yazinski, *The autoconjugacy of the 3x+1 function*, Discrete Math. **275**
(2004) 219–236, doi:[10.1016/S0012-365X(03)00125-0](https://doi.org/10.1016/S0012-365X(03)00125-0);
and Yazinski, *Pseudoperiodicity and the 3x+1 conjugacy function*.

## The author's own notes (tracked)

| file | work |
|---|---|
| `A_2adic_Sturmian_Carry_Constant.pdf` | E. De Jesús, *The 2-adic Sturmian carry constant* — cited as `[A]` / `DeJesusA` |
| `B_Sturmian_Mahler_Edge.pdf` | E. De Jesús, *The Sturmian Mahler edge* — cited as `[B]` / `DeJesusB` |

## History

These three third-party files were tracked between the start of the audit and
this commit. They are untracked here going forward; the history is **not**
rewritten, so they remain reachable in earlier commits.
