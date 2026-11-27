# Answer key: tracks and conflicts

Compare the plan you wrote in Lab 05 with the results below. For each difference, check the files involved and explain whether your plan would also work.

## Parallel safety by issue

- A **textual overlap** means two branches edit the same lines. Git stops and asks you to choose. Resolving it takes a minute and needs no product decision.
- A **semantic conflict** means two branches change the same contract, here the shelf file format. Git may even merge them without complaint, and the result can still be wrong. Someone has to make a decision.

- **S1.** Independent of S2–S6 and C2. C1 also changes `shelf list` (it adds `--tag`), so S1 and C1 edit the same lines of `shelf/commands/list_books.py`: a small textual overlap. Merge S1 first.
- **S2.** Independent. It only adds new files.
- **S3.** Independent. It only adds new files.
- **S4.** Independent. It only adds new files.
- **S5.** Independent. It adds a method to `shelf/store.py`, which C1 and C2 also change, but in a different part of the file, so git merges them cleanly.
- **S6.** Independent of S1–S5 and C2, because it doesn't touch the model or the storage. C1 also changes `shelf add` (it adds `--tag`), so S6 and C1 edit neighboring lines of `shelf/commands/add.py`: a small textual overlap. Merge S6 first.
- **C1.** Conflicts with C2. Both change what a book looks like in the shelf file, both edit `shelf/models.py` and `shelf/store.py`, and both must change the stored-format test in `tests/test_store.py`. Run them in parallel and decide the merge order before either starts: whichever merges second merges `origin/main` into its branch and adapts. C1 also has small textual overlaps with S1 (`shelf list`) and S6 (`shelf add`).
- **C2.** Conflicts with C1. Both edit `shelf/models.py`, `shelf/store.py` and the stored-format test in `tests/test_store.py`, and whoever merges second has to decide whether tags belong in version 2.
- **S7.** Vague: discuss first. Don't put it in a parallel batch. Once it is split into concrete issues, check each one against C1 and C2, because most book-club ideas change the file format.

## Verified overlaps

| Issue | Main files | Overlaps with |
| --- | --- | --- |
| S1 | `commands/list_books.py` | C1 (textual) |
| S2 | new `commands/search.py` | None |
| S3 | new `commands/stats.py` | None |
| S4 | new `commands/export.py` | None |
| S5 | new `commands/remove.py`, `store.py` | None |
| S6 | `commands/add.py` | C1 (textual) |
| C1 | `models.py`, `store.py`, `commands/add.py`, `commands/list_books.py` | C2 (semantic), S1 and S6 (textual) |
| C2 | `models.py`, `store.py` | C1 (semantic) |
| S7 | Unknown | Discuss first |

We checked this table by implementing S1 to S6, C1 and C2 minimally, each on its own branch from the same starting point, and merging the branches:

- S1 to S6 merge together cleanly, and the tests pass.
- S2, S3, S4 and S5 merge cleanly with C1 and with C2, alone or together, and the tests pass. S1 and S6 merge cleanly with C2.
- S1 with C1 stops on `shelf/commands/list_books.py`. S6 with C1 stops on `shelf/commands/add.py`.
- C1 with C2 stops on `tests/test_store.py`. Git merges `models.py` and `store.py` without complaint. If you resolve the test by taking either side, a stored-format test fails until someone decides what version 2 contains.

We also replayed the labs' order with squash merges. S1 and S2 (lab 0), S3 (lab 2) and S6 (lab 3) landed on `main` first. Then S4, S5, C1 and C2 each branched from that `main`. S4 and S5 merged cleanly, and so did whichever of C1 and C2 went next. The other one, after merging `origin/main` into its branch, stopped only on `tests/test_store.py`, in either order, with the same stored-format failure until we applied the decision.

Your agent's implementation will differ from ours, so treat these results as likely, not guaranteed.

One way to split the work into three tracks for lab 6, once labs 0, 2 and 3 have landed S1, S2, S3 and S6:

1. **Track A:** S4 and S5, one after the other. S4 adds a new command, and S5 adds one plus a `remove` method in `shelf/store.py`.
2. **Track B:** C1.
3. **Track C:** C2.

If S1, S2, S3 or S6 is still open because you skipped a lab, add it to track A.

All three can run at the same time. Merge track A first. Then there are two reasonable ways to land C1 and C2, and lab 4 records the choice as `D-0001`:

- **C1 first.** C2 merges `origin/main` into its branch and adapts: version 2 includes `tags`, and the version 1 migration gives old books an empty tag list. One version, less code.
- **C2 first.** C1 merges `origin/main` and adapts. Adding `tags` now changes a versioned format, so C1 bumps `SCHEMA_VERSION` to 3 and adds a migration from version 2. More code, but it is what a real project does once version 2 has shipped.

Neither is wrong. Choosing is a human decision, and making that decision on purpose is the point of the exercise.

## How the labs use this catalog

| Lab | Issues | What you do with them |
| --- | --- | --- |
| [Lab 0: the whole game](../../content/en/00-start-here/lab.md) | S1 | One agent builds a status filter. S2 and a fresh review are optional after module 03. |
| [Lab 2: one agent, done well](../../content/en/02-one-agent-done-well/lab.md) | S3 | Take one issue through discuss → plan → build → verify, and log every correction you make. |
| [Lab 3: close the loop](../../content/en/03-close-the-loop/lab.md) | S6 | Write S6's tests first, add a Stop hook that runs the tests, and watch it send an agent back to fix its implementation. |
| [Lab 4: context is infrastructure](../../content/en/04-context-is-infrastructure/lab.md) | C1, C2 | No code. Decide which of the two merges first and record it as decision `D-0001`. |
| [Lab 5: decompose into tracks](../../content/en/05-decompose-into-tracks/lab.md) | All | Create the issues that don't exist yet on GitHub, spot the overlaps and the conflicting pair, reuse `D-0001` for the merge order and write kickoff prompts for three tracks: S4 and S5, C1, and C2. |
| [Lab 6: run sessions in parallel](../../content/en/06-run-sessions-in-parallel/lab.md) | S4, S5, C1, C2 | Run the three tracks in three worktrees, merge S4 and S5 first, then C1 and C2 in the order `D-0001` sets, and resolve their conflict. |
| [Lab 7: agents review agents](../../content/en/07-agents-review-agents/lab.md) | A pull request from lab 6, preferably C1 or C2 | Review it with a fresh-context reviewer and a reviewer from another vendor, then triage the findings. |

If you skip a lab, its issues stay open. Labs 5 and 6 say where they go.

S7 has no lab of its own. Use it whenever you want to practice turning a vague request into concrete work. In lab 5, watch whether your agent schedules it or asks questions first. The Day 2 [parallel sprint](../../workshops/en/README.md#the-parallel-sprint) of the intensive workshop is built on it: discuss it, split it into new issues, then run those in parallel.
