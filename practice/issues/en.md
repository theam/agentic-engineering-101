# Practice issues for `shelf`

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
