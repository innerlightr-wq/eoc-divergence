# Lean baseline validation

## Committed base and pinned environment

| item | value |
|---|---|
| repository | `~/GitHub/eoc-lean-verification` |
| **committed base** | `14dea46ae5af816754cf3883475fa73dea598130` ("Isolate power-of-two digit sparsity frontier in Lean") |
| toolchain | `leanprover/lean4:v4.34.0-rc1` (**unchanged**) |
| `lake-manifest.json` md5 | `ed63ad5bdf0dcba26e8d3bcd0b666043` (**unchanged**) |
| mathlib rev | `38e9c3ce15cbb63c92e90bb9a92e4eb82131f669` (manifest), `rev = "v4.34.0-rc1"` (lakefile) |
| default target | `defaultTargets = ["EOC"]` — the `EOC` lean_lib |

**Choice of base.** `14dea46` is the tip of the ordinary checkout's branch
`research-sparse-visits-2026-09-16`, i.e. the newest committed revision available locally. It
already contains every definition the new modules need (`Mathlib.Combinatorics.Enumerative.DoubleCounting`,
`Mathlib.Data.Finset.*`, `Mathlib.Data.ZMod.Basic`, `Mathlib.Data.Real.Basic`); no uncommitted
definition is used. This is the revision the previous round reported, and it was re-verified, not
assumed.

## Three distinct states, kept apart

| state | location | contents |
|---|---|---|
| **committed baseline** | worktree `…/scratchpad/lean-baseline` at `14dea46` (detached, then branch `research/carry-domination-lemma`) | committed files only; `git status --untracked-files=no` reported **0** modifications |
| **ordinary dirty snapshot** | `~/GitHub/eoc-lean-verification` | `14dea46` **plus** 3 tracked modifications (`EOC.lean`, `docs/LITERATURE_CONTEXT.md`, `docs/RESEARCH_STATUS.md`) and 50 untracked files — **not used, not copied** |
| **formalization worktree** | the same isolated worktree, after adding 2 new files | baseline + `EOC/CarryDomination.lean`, `EOC/Occupancy.lean` |

The dirty snapshot was never copied in. Verified by `diff` of the worktree's `EOC.lean` against
`git show 14dea46:EOC.lean`: identical. **A successful baseline build certifies the committed
revision only, not the dirty snapshot.**

**Dependency reuse, non-destructive.** `.lake/packages` in the worktree is a *symlink* to the
ordinary checkout's already-built packages (mathlib: 8323 `.olean`). The worktree keeps its own
`.lake/build`. No other worktree's artifacts were overwritten, no `lake clean`, no cache
re-download, no manifest edit.

## Commands, in order, with outcomes

| # | command | exit | result |
|---|---|---|---|
| 1 | `lake build EOC.ShellWeyl` (**before** any new file) | 0 | `Build completed successfully (3294 jobs)`, **0 errors** |
| 2 | `lake build EOC.CarryDomination` | 0 | `Build completed successfully (1219 jobs)` |
| 3 | `lake build EOC.Occupancy` | 0 | `Build completed successfully (853 jobs)` |
| 4 | `lake env lean AxiomCheck.lean` | 0 | 9 theorems, each `[propext, Classical.choice, Quot.sound]`; **no `sorryAx`** |
| 5 | `lake build EOC.ShellWeyl` (**after**) | 0 | **0 errors** — no regression |
| 6 | `lake build` (default target, committed baseline) | 0 | `Build completed successfully (8803 jobs)`, **0 errors** — the full `EOC` library at `14dea46` builds clean |

Only pre-existing style-linter warnings appear (`Copyright too short!`, line-length, unreferenced
binder). These were present in the baseline before any change.

## Limitations, stated explicitly

1. **`defaultTargets = ["EOC"]` and `EOC.lean` does NOT import the two new modules** (checked:
   0 matches). The default build therefore **does not discover them**. They were compiled
   explicitly (commands 2–3) and exercised through the committed driver `AxiomCheck.lean`
   (command 4), as the brief's §9 permits. Integrating them into `EOC.lean` is deliberately
   deferred: it would change the root import file and make every future default build depend on
   them, which should follow a validated full build rather than precede it.
2. No dependency download or cache bootstrap was attempted; the existing built packages were
   reused read-only. Consequently **no environment/dependency failure was encountered**, and none
   is being reported as a proof failure.
3. **Command 6 is a genuine full default-target build and it passed** (8803 jobs, 0 errors). Its
   scope is the committed `EOC` library **only**: by (1) it excludes `EOC/CarryDomination.lean` and
   `EOC/Occupancy.lean`, which were built separately by commands 2–3. So "the full project builds"
   and "the new modules build" are two separate verified facts, not one.
