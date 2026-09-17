# Practice issues for `shelf`

This catalog holds nine issues for [`shelf`](../shelf/README.md), the practice project of this guide. The labs use them to practice planning, parallel tracks of work, merging and code review on code small enough to read in five minutes.

- **S1 to S6** are small and independent. You can run them at the same time.
- **C1 and C2** conflict with each other. Both change the format of the shelf file.
- **S7** is short but deliberately vague. It is there to practice discussing before building.

## How the labs use this catalog

| Lab | Issues | What you do with them |
| --- | --- | --- |
| [Lab 0: the whole game](../../content/en/00-start-here/lab.md) | S1, S2 | One session implements S1. While it runs, a second session implements S2 in a worktree. A third, fresh session reviews the S1 pull request. |
| [Lab 2: one agent, done well](../../content/en/02-one-agent-done-well/lab.md) | S3 | Take one issue through discuss → plan → build → verify, and log every correction you make. |
| [Lab 3: close the loop](../../content/en/03-close-the-loop/lab.md) | S6 | Write S6's tests first, add a Stop hook that runs the tests, and watch it send an agent back to fix its implementation. |
| [Lab 4: context is infrastructure](../../content/en/04-context-is-infrastructure/lab.md) | C1, C2 | No code. Decide which of the two merges first and record it as decision `D-0001`. |
| [Lab 5: decompose into tracks](../../content/en/05-decompose-into-tracks/lab.md) | All | Create the issues that don't exist yet on GitHub, spot the overlaps and the conflicting pair, reuse `D-0001` for the merge order and write kickoff prompts for three tracks: S4 and S5, C1, and C2. |
| [Lab 6: run sessions in parallel](../../content/en/06-run-sessions-in-parallel/lab.md) | S4, S5, C1, C2 | Run the three tracks in three worktrees, merge S4 and S5 first, then C1 and C2 in the order `D-0001` sets, and resolve their conflict. |
| [Lab 7: agents review agents](../../content/en/07-agents-review-agents/lab.md) | A pull request from lab 6, preferably C1 or C2 | Review it with a fresh-context reviewer and a reviewer from another vendor, then triage the findings. |

If you skip a lab, its issues stay open. Labs 5 and 6 say where they go.

S7 has no lab of its own. Use it whenever you want to practice turning a vague request into concrete work. In lab 5, watch whether your agent schedules it or asks questions first. The Day 2 [parallel sprint](../../workshops/en/README.md#the-parallel-sprint) of the intensive workshop is built on it: discuss it, split it into new issues, then run those in parallel.

> [!TIP]
> This catalog also exists in Spanish: [practice/issues/es.md](es.md). Create the GitHub issues in the language your team writes its artifacts in. Your agent understands your instructions in either language.

## How each issue is written

Each issue is ready to paste into GitHub:

- **Title:** starts with the issue ID, so you can find it in any tool.
- **Problem:** what is missing and why a user cares.
- **Acceptance criteria:** checks that a reviewer, or an agent, can verify. Where a test needs an exact message or exit code, the issue gives it.
- **Likely touches:** the files a good implementation probably changes. It is a hint, not a rule.
- **Out of scope:** what not to do in this issue.
- **Parallel safety:** whether the issue can run at the same time as the others.

> [!NOTE]
> **At The Agile Monkeys** we write issues so that a fresh agent session can pick one up with no other context. The issue is the prompt. If a new session needs you to explain the issue, the issue is not finished.

The parallel safety lines use two words on purpose:

- A **textual overlap** means two branches edit the same lines. Git stops and asks you to choose. Resolving it takes a minute and needs no product decision.
- A **semantic conflict** means two branches change the same contract, here the shelf file format. Git may even merge them without complaint, and the result can still be wrong. Someone has to make a decision.

[Module 5](../../content/en/05-decompose-into-tracks/README.md) explains how to use this when you split work into tracks.

## S1: Filter `shelf list` by status

**Title:** `S1: Filter shelf list by status`

### Problem

`shelf list` prints every book. Once your shelf has more than a handful of books, you can't quickly see what you are reading now or what comes next.

### Acceptance criteria

- [ ] `shelf list --status reading` prints only the books whose status is `reading`, one per line, in the same format and order as `shelf list`.
- [ ] `--status` accepts exactly `to-read`, `reading` and `done`. Any other value exits with code 2 and prints an error to stderr that names the valid values.
- [ ] When no book matches, including on an empty shelf, the command prints `No books with status reading.` (with the requested status) and exits with code 0.
- [ ] `shelf list` without `--status` behaves exactly as before.
- [ ] `python -m unittest` passes, with new tests for the filter, the no-match message and an invalid status.

### Likely touches

- `shelf/commands/list_books.py` (reuse `STATUSES` from `shelf/models.py`; that file doesn't need to change)
- `tests/test_cli.py`, in the `ListCommandTest` class

### Out of scope

- Filtering by anything other than status.
- Changing the output format of `shelf list`.

**Parallel safety:** Independent of S2–S6 and C2. C1 also changes `shelf list` (it adds `--tag`), so S1 and C1 edit the same lines of `shelf/commands/list_books.py`: a small textual overlap. Merge S1 first.

## S2: Search books by title or author

**Title:** `S2: Search books by title or author`

### Problem

To check whether a book is already on your shelf, you have to read through the whole output of `shelf list`.

### Acceptance criteria

- [ ] `shelf search TEXT` prints every book whose title or author contains `TEXT`, one per line, in the same format and order as `shelf list`.
- [ ] Matching ignores case, including accented letters: `shelf search GARCÍA` finds `One Hundred Years of Solitude by Gabriel García Márquez`.
- [ ] When nothing matches, the command prints `No books match "TEXT".` (with the text you searched for) and exits with code 0.
- [ ] `shelf search` without `TEXT` is a usage error and exits with code 2.
- [ ] The shelf file is not modified.
- [ ] `python -m unittest` passes, with new tests for a title match, an author match, case and accents, and no match.

### Likely touches

- `shelf/commands/search.py` (new)
- `tests/test_search.py` (new)

### Out of scope

- Fuzzy matching, regular expressions, or searching by status or tag.

**Parallel safety:** Independent. It only adds new files.

## S3: Show reading statistics

**Title:** `S3: Show reading statistics`

### Problem

There is no way to see how your reading is going: how many books are waiting, how many you are reading and how many you finished this year.

### Acceptance criteria

- [ ] `shelf stats` prints exactly these four lines, in this order, and exits with code 0:

  ```text
  to-read: 2
  reading: 1
  done: 3
  finished this year: 2
  ```

- [ ] Every status appears, even when its count is 0. An empty shelf prints the four lines with zeros.
- [ ] `finished this year` counts the books with status `done` whose `finished_at` falls in the current calendar year, in UTC (the time zone of the stored timestamps).
- [ ] The tests don't depend on today's date: a book finished last year is not counted, whatever year the tests run in. For example, a test can write the shelf file with chosen timestamps, or the command can take the current date as a parameter.
- [ ] The shelf file is not modified.
- [ ] `python -m unittest` passes, with new tests for the counts, the empty shelf and the year boundary.

### Likely touches

- `shelf/commands/stats.py` (new)
- `tests/test_stats.py` (new)

`shelf finish` already records `finished_at`, so no other file needs to change.

### Out of scope

- Statistics by author or tag, reading speed, charts, choosing a different year.

**Parallel safety:** Independent. It only adds new files.

## S4: Export the shelf as CSV or Markdown

**Title:** `S4: Export the shelf as CSV or Markdown`

### Problem

Your reading list is locked inside a JSON file. You want to paste it into a spreadsheet or a Markdown document.

### Acceptance criteria

- [ ] `shelf export --format csv` writes CSV to stdout: a header row `id,title,author,status,added_at,finished_at`, then one row per book, in id order. A missing `finished_at` is an empty cell.
- [ ] Titles and authors that contain commas, quotes or line breaks survive: reading the output back with Python's `csv.reader` returns the original values.
- [ ] `shelf export --format markdown` writes a Markdown table with the columns `ID`, `Title`, `Author` and `Status`, in id order. A `|` inside a title or author is written as `\|`, so the table doesn't break.
- [ ] `--format` is required and accepts only `csv` and `markdown`. Anything else exits with code 2.
- [ ] On an empty shelf, CSV prints only the header row, and Markdown prints only the header row and the separator row.
- [ ] The command writes only to stdout. The shelf file is not modified.
- [ ] `python -m unittest` passes, with new tests for both formats, the tricky characters and the empty shelf.

### Likely touches

- `shelf/commands/export.py` (new)
- `tests/test_export.py` (new)

### Out of scope

- Writing to a file. The shell already does that: `shelf export --format csv > ~/shelf.csv`.
- JSON export, importing, exporting tags.

**Parallel safety:** Independent. It only adds new files.

## S5: Remove a book, with confirmation

**Title:** `S5: Remove a book, with confirmation`

### Problem

A book added by mistake stays on the shelf forever. Removing is destructive, so it has to be hard to do by accident.

### Acceptance criteria

- [ ] `shelf remove ID --yes` removes the book, prints `Removed` followed by the book line (for example `Removed #3 [to-read] Dune by Frank Herbert`) and exits with code 0.
- [ ] `shelf remove ID` without `--yes` removes nothing. It prints `Would remove #3 [to-read] Dune by Frank Herbert. Run again with --yes to confirm.` to stderr and exits with code 1.
- [ ] An unknown id prints `shelf: error: no book with id 42` to stderr and exits with code 1, with or without `--yes`. The shelf file is not modified.
- [ ] The remaining books keep their ids.
- [ ] `python -m unittest` passes, with a test proving the book is still there after `shelf remove ID` without `--yes`.

### Likely touches

- `shelf/commands/remove.py` (new)
- `shelf/store.py` (a `remove` method next to `move`)
- `tests/test_remove.py` (new)

### Out of scope

- Interactive prompts such as `Are you sure? [y/N]`, undo, removing several books at once.
- Id reuse. New ids are the highest id plus one, so removing the newest book lets the next `shelf add` reuse its id. That is acceptable in this issue: fixing it means storing a counter, which changes the file format.

**Parallel safety:** Independent. It adds a method to `shelf/store.py`, which C1 and C2 also change, but in a different part of the file, so git merges them cleanly.

## S6: Reject empty titles and unknown statuses

**Title:** `S6: Reject empty titles and unknown statuses`

### Problem

`shelf add` accepts anything. `shelf add "" "Frank Herbert"` stores a book with no title, and `shelf add "Dune" "Frank Herbert" --status finished` stores a status no other command understands. Bad data gets into the file without a word.

### Acceptance criteria

- [ ] `shelf add` with an empty or whitespace-only title exits with code 2, prints an error to stderr saying the title must not be empty, and saves nothing.
- [ ] `shelf add` with a `--status` other than `to-read`, `reading` or `done` exits with code 2, prints an error to stderr that lists the valid statuses, and saves nothing.
- [ ] Both errors use the same format as other usage errors: the `usage: shelf add …` line, then `shelf add: error: …`.
- [ ] "Saves nothing" is tested: if the shelf file didn't exist before the command, it still doesn't exist after it.
- [ ] Valid input works exactly as before.
- [ ] `python -m unittest` passes, with new tests for both errors.

### Likely touches

- `shelf/commands/add.py` (validate at the command-line boundary; leave `shelf/models.py` and `shelf/store.py` unchanged)
- `tests/test_cli.py`, in the `AddCommandTest` class

### Out of scope

- Validating books that are already in the shelf file.
- Trimming whitespace from titles, validating authors.

**Parallel safety:** Independent of S1–S5 and C2, because it doesn't touch the model or the storage. C1 also changes `shelf add` (it adds `--tag`), so S6 and C1 edit neighboring lines of `shelf/commands/add.py`: a small textual overlap. Merge S6 first.

## C1: Tag books

**Title:** `C1: Tag books`

### Problem

A status says where a book is in your reading, not what the book is about. You want to group books by topic (`sci-fi`, `work`, `book-club`) and list one group.

### Acceptance criteria

- [ ] `shelf add TITLE AUTHOR --tag sci-fi --tag classics` stores the tags. `--tag` is optional and can be repeated.
- [ ] Tags are stored in lowercase, without surrounding spaces and without duplicates, in the order first given: `--tag Sci-Fi --tag " sci-fi "` stores `["sci-fi"]`.
- [ ] `shelf list` shows a book's tags after the author, in parentheses: `#1 [to-read] Dune by Frank Herbert (sci-fi, classics)`. Books without tags look exactly as before.
- [ ] `shelf list --tag sci-fi` shows only the books with that tag, ignoring case. If `shelf list --status` (S1) already exists when you start, the two filters combine: a book must match both.
- [ ] Each book in the shelf file has its tags as a list of strings.
- [ ] Shelf files written before this change, without tags, still load. Their books have no tags.
- [ ] `python -m unittest` passes, including the test in `tests/test_store.py` that pins the stored fields of a book, updated for `tags`.

### Likely touches

- `shelf/models.py` (a `tags` field, and the tags in the book line)
- `shelf/store.py` (`Store.add` accepts tags)
- `shelf/commands/add.py` and `shelf/commands/list_books.py`
- `tests/test_store.py` and `tests/test_cli.py`

### Out of scope

- Tagging books that are already on the shelf, renaming or removing tags.
- Tags in `shelf export` or `shelf search`.

**Parallel safety:** Conflicts with C2. Both change what a book looks like in the shelf file, both edit `shelf/models.py` and `shelf/store.py`, and both must change the stored-format test in `tests/test_store.py`. Run them in parallel and decide the merge order before either starts: whichever merges second merges `origin/main` into its branch and adapts. C1 also has small textual overlaps with S1 (`shelf list`) and S6 (`shelf add`).

## C2: Version the shelf file format

**Title:** `C2: Version the shelf file format`

### Problem

The shelf file is a bare JSON list with no version. The first time the format changes, the program can't tell an old file from a new one, and an older copy of `shelf` could misread or overwrite a newer file without noticing.

### Acceptance criteria

- [ ] Every save writes a JSON object, `{"version": 2, "books": [...]}`, where `books` holds the same book objects the file holds today.
- [ ] A version 1 file (a bare JSON list) still loads. Reading doesn't rewrite it: after `shelf list`, the file is byte-for-byte unchanged. The next command that saves writes version 2.
- [ ] A file with a version this program doesn't know, such as `{"version": 99, "books": []}`, makes every command exit with code 1 and print `shelf: error: unsupported shelf file version 99` to stderr. The file is not modified.
- [ ] The current version is one named constant, `SCHEMA_VERSION`, defined in `shelf/models.py` next to `Book`, so whoever changes the book fields sees it.
- [ ] A test pins the stored fields of a book for each schema version. Adding or removing a `Book` field without bumping `SCHEMA_VERSION` makes the suite fail.
- [ ] A test loads a version 1 fixture file, written exactly as the current program writes it, saves, and checks that the result is version 2 with the same books.
- [ ] `python -m unittest` passes.

### Likely touches

- `shelf/store.py` (`Store.load`, `Store.save`, the migration from version 1, an error for unknown versions based on `ShelfError`)
- `shelf/models.py` (`SCHEMA_VERSION`)
- `tests/test_store.py`, and a version 1 fixture file under `tests/`

### Out of scope

- Backups of old files, a `shelf migrate` command, downgrading a file to version 1.

**Parallel safety:** Conflicts with C1. Both edit `shelf/models.py`, `shelf/store.py` and the stored-format test in `tests/test_store.py`, and whoever merges second has to decide whether tags belong in version 2.

## S7: Make shelf more useful for book clubs

**Title:** `S7: Make shelf more useful for book clubs`

### Problem

"Our book club started using shelf. Make it more useful for book clubs."

That is the whole request. This issue is vague on purpose: don't write code for it yet.

### Acceptance criteria

- [ ] A comment on this issue lists the questions that need an answer before building. For example: who uses it, the organizer or every member? One shared shelf or one per person? Does it need a network, given that `shelf` uses only the standard library? What would "more useful" look like a month from now?
- [ ] The same comment proposes two or three options. Each option names the problem it solves, the commands it would add, the files it would touch and whether it changes the shelf file format.
- [ ] A human picks one option, or none, and says so in a comment.
- [ ] The chosen option is filed as one or more new issues written like S1–S6, linked from this issue, and this issue is closed.

### Likely touches

Unknown until someone decides. Anything that stores new data (meetings, votes, members) changes the shelf file format.

### Out of scope

- Any code change in this issue.

**Parallel safety:** Vague: discuss first. Don't put it in a parallel batch. Once it is split into concrete issues, check each one against C1 and C2, because most book-club ideas change the file format.

## Create the GitHub issues with your agent

Lab 5 asks you to do this. Open an agent session in your own copy of `shelf` (see [Use it for the labs](../shelf/README.md#use-it-for-the-labs)), replace `PATH_TO_GUIDE` with the folder where you cloned this guide, and paste:

```text
Read PATH_TO_GUIDE/practice/issues/en.md. It describes nine practice issues for the shelf project in this repository: S1 to S6, C1, C2 and S7.

First run `gh repo view` and tell me which GitHub repository you are about to create issues in. Wait for my OK.

Then create one GitHub issue per entry with `gh issue create`:
- Title: the text after "Title:", exactly as written.
- Body: the Problem, Acceptance criteria, Likely touches and Out of scope sections, in Markdown. Leave out the "Parallel safety" line: deciding which issues can run in parallel is a separate step.
- Write each body to a temporary file and pass it with --body-file, so backticks and quotes survive the shell.
- No labels, assignees or milestones.

When you finish, run `gh issue list --state all` and show me a table with each ID, its issue number and its title, so we can check that nothing is missing or duplicated. Do not start implementing any issue.
```

What to look for in the response:

- It stops after `gh repo view` and waits for you. If it creates issues first, you have learned something about your agent's permission settings.
- The final table has nine rows, with no duplicates.
- The issue bodies on GitHub have no "Parallel safety" line.

> [!TIP]
> For lab 0 or lab 2 you only need one or two issues. Change "one GitHub issue per entry" to "one GitHub issue for S1 and one for S2", or simply paste the issue text into your session.

## Answer key: tracks and conflicts

Read this after you have done lab 5, or if you are facilitating a workshop.

<details>
<summary>Show the answer key</summary>

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

</details>
