---
title: "Lab 2 — One agent, done well"
module: 2
kind: lab
minutes: 60
level: foundation
last_reviewed: 2026-09-17
---

# Lab 2 — One agent, done well

## Goal

Implement issue **S3** of the practice project (`S3: Show reading statistics`) with one agent, going through explore → discuss → plan → build → verify → commit.

While you work, keep a **correction log**: one line every time you have to correct the agent. The pull request is the visible result, but the log is the real output of this lab. Each correction tells you something that was missing: context, a check, a decision or a better question. [Lab 4](../04-context-is-infrastructure/lab.md) turns some of those lines into rules.

S3 looks trivial: print four lines of counts. It isn't. The issue fixes the output and the time zone, but it leaves decisions open that are easy to miss: how to test "this year" without depending on the day the tests run, and what to do with data the issue doesn't mention. The point of this lab is to find those in the conversation, not in the diff.

## Before you start

- You have your own copy of the practice project from [lab 0](../00-start-here/lab.md), and `python -m unittest` passes on `main`. (Use `python3` wherever this lab says `python` if that is how Python 3 is called on your machine.)
- Start from an up-to-date `main`, in a new worktree:

  ```bash
  cd ~/code/shelf
  git fetch origin
  git worktree add --no-track -b s3-stats ../shelf-s3 origin/main
  cd ../shelf-s3
  ```

- If S3 isn't an issue in your repository yet, run `gh issue create` and paste its title and body from the [practice issue catalog](../../../practice/issues/en.md), without the "Parallel safety" line. Note its number; the prompts below use `#3`.
- Create `corrections.md` in your notes (not in the repository):

  ```markdown
  | # | Stage | What I corrected | What was missing | What would have prevented it |
  |---|---|---|---|---|
  ```

  "What was missing" is one of: **context** (the agent couldn't know), **verification** (it could have checked and didn't), **decision** (a product choice nobody had made), **instruction** (it knew and ignored it) or **model** (a plain mistake).

- Open one session in the worktree (`claude` or `codex`). Use the strongest model you have access to.

**On your own repo:** pick a small feature that touches two to five files and hides a definition question: a count, a date range, an "active" or "recent", a rounding rule, a time zone. Make sure the repository has tests the agent can run. Everything below applies with your names instead of shelf's.

## Steps

### 1. Explore (5 minutes)

```text
We're going to work on issue #3 (read it with gh issue view 3).
Don't write code yet. Read shelf/models.py, shelf/store.py, the modules in
shelf/commands/ and the tests. Then tell me in under 150 words: how a book's
status changes, when finished_at is set, in which time zone timestamps are
stored, and what shelf add accepts as a status.
```

**Look for:** answers that cite files. In the current code, `finished_at` is set whenever a book moves to `done`, which includes `shelf add … --status done`; timestamps are ISO 8601 strings in UTC; and `shelf add` doesn't validate `--status` yet (that is issue S6), so a shelf file can already contain a status like `finished`. If the agent asks you something the code answers, reply "Read more code to answer your own questions." and log it as a correction.

**Checkpoint:** you can name two kinds of data S3 will meet that the issue doesn't mention.

### 2. Discuss (10 minutes)

```text
Let's discuss before building. The issue fixes the output and says UTC.
Give me options, with trade-offs, for two open questions:
1. How to test "finished this year" so the tests pass whatever year they run in.
2. What stats should do with data the issue doesn't mention, such as a book
   added directly as done, or a status that isn't to-read, reading or done.
Recommend one option for each. Don't write code until I say build.
```

**Look for:** for question 1, real options, such as tests that write the shelf file with fixed timestamps, a function that takes the current date as a parameter (not a command-line option; choosing a year is out of scope), or both. For question 2, an agent that notices the issue says "every status appears" but says nothing about unknown statuses, and asks instead of deciding silently.

If the agent misses a case you can see, don't hand it the answer yet. Ask: "What data would make these counts wrong?" If it still misses it, tell it, and log a correction.

Decide in one or two sentences. For example:

```text
Tests write the shelf file with fixed finished_at values, and the counting
function takes today's date as a parameter that defaults to now in UTC.
A book added as done counts like any other done book, because the issue
defines it by finished_at. Unknown statuses don't appear in any line; say so
in the pull request.
```

**Checkpoint:** your decision is written down, and `git status` shows no changes.

### 3. Plan (5 to 10 minutes)

```text
Write the plan in under 25 lines: files you'll add or change, the exact output
for a sample shelf, the tests you'll add and why each would fail without the
change, how the tests avoid depending on today's date, and what you will not
do. Then wait.
```

Review it against this checklist:

- [ ] It adds `shelf/commands/stats.py` and `tests/test_stats.py`, and changes nothing else. The issue says no other file needs to change.
- [ ] The output is exactly the four lines from the issue, in order, with zeros on an empty shelf.
- [ ] A test covers the year boundary with fixed timestamps (a book finished last year is not counted), and no test reads the real clock to decide what to expect.
- [ ] It says how unknown statuses are handled, matching your decision.
- [ ] It lists what's out of scope: no statistics by author or tag, no charts, no option to choose a year.

Correct the plan with one-sentence messages. Log each correction.

> [!TIP]
> If your agent has a plan mode (see [permission modes](https://code.claude.com/docs/en/permission-modes) in Claude Code, or plan mode in the [Codex best practices](https://learn.chatgpt.com/guides/best-practices)), try steps 1–3 in it and compare with the conversation approach. Note which one kept *you* reviewing intent instead of code.

**Checkpoint:** you replied "ok" to a plan that passes the checklist.

### 4. Build (10 to 15 minutes)

```text
Build it. Write the tests first and run them to show they fail. Then
implement. Then run the whole suite with python -m unittest and paste the
output. For any manual run of the command, set SHELF_PATH to a temporary file.
```

Don't watch. Come back when it reports.

**Look for:** a failing run before the implementation, a passing run after, and output pasted rather than summarized. Then check the scope yourself:

```bash
git status
git diff --stat
```

**Checkpoint:** `python -m unittest` ends with `OK`, you saw the new tests fail first, and only the planned files changed.

### 5. Verify beyond the tests (5 minutes)

```text
Do we have any side effects? Check that stats never writes the shelf file,
and think about the year boundary in UTC.
```

Then ask for real output:

```text
Set SHELF_PATH to a temporary file. Add three books, start book 1, finish
book 2, add a fourth book with --status done, then run shelf stats.
Show me the exact commands and output.
```

**Look for:** with the example decisions from step 2, exactly this output:

```text
to-read: 1
reading: 1
done: 2
finished this year: 2
```

If you decided differently (for example, not counting books added directly as done), work out the expected output yourself *before* you read the agent's. If they differ, ask why before accepting any explanation.

**Checkpoint:** you've seen the command's real output, and it matches.

### 6. Ask for hindsight (3 minutes)

```text
Now that you built it, what would you have done differently?
```

Decide for each suggestion: do it now (small and inside the scope), file a follow-up issue with `gh issue create`, or drop it. Don't let hindsight grow the pull request.

**Checkpoint:** each suggestion has a decision.

### 7. Commit and open the pull request (5 minutes)

```text
Commit with a message that explains how "finished this year" is tested and
how unknown statuses are handled. Push, and open a pull request with
gh pr create that closes #3. In the description, state both decisions and
their trade-offs.
```

**Checkpoint:** `gh pr view` shows the pull request, and its description contains both decisions.

### 8. If two corrections failed: restart (optional, 10 minutes)

If at any point you corrected the agent twice on the same problem and it was still wrong, stop and practice the restart:

```text
Stop. List in at most 10 bullets what we learned: constraints we found,
approaches that failed and why. Don't change any files.
```

Copy the bullets. Discard the work and create a clean worktree:

```bash
cd ~/code/shelf
git worktree remove --force ../shelf-s3
git branch -D s3-stats
git worktree add --no-track -b s3-stats ../shelf-s3 origin/main
```

Open a fresh session there. Start it with the bullets, your decisions from step 2, and "plan first, then wait". Log the restart as a correction. It counts as a success.

**Checkpoint:** the new session produced an acceptable plan with fewer corrections than the first one.

### 9. Classify your correction log (5 minutes)

For each row, fill in "What would have prevented it":

- a line in the instruction file (**context** or **instruction**) → [module 04](../04-context-is-infrastructure/README.md),
- a check the agent runs itself (**verification**) → [module 03](../03-close-the-loop/README.md),
- a better question during discussion (**decision**) → this module,
- nothing: it was a genuine judgment call.

**Checkpoint:** every row has a stage, a cause and a prevention.

## Done when

- [ ] `python -m unittest` ends with `OK` on the `s3-stats` branch.
- [ ] You saw the new tests fail before the implementation.
- [ ] `gh pr view` shows a pull request for S3 whose description states how the year is tested and how unknown statuses are handled.
- [ ] `git diff --stat origin/main` lists only `shelf/commands/stats.py` and `tests/test_stats.py`, or the description explains why not.
- [ ] `corrections.md` has one row per correction, each with stage, cause and prevention.

## Reflect

- **Where did most corrections happen?** In discussion and plan, or in build and verify? The earlier a correction happens, the cheaper it is.
- **Which cause dominated?** Many "context" rows mean your repository needs better instructions. Many "verification" rows mean the agent needs better checks. Many "decision" rows mean you are delegating choices that are yours.
- **What was your longest message?** Was it making up for context the session should already have had?
- **Did the agent find the open questions, or did you?** If you did, what would it have needed to find them itself?

## Stretch

- **Draw the system.** Ask for `docs/architecture.md` with a Mermaid flowchart of how a command reaches the file and a sequence diagram for `shelf finish`, citing files and lines. Find one thing that's wrong or unclear and correct it in one sentence. Don't edit the document yourself.
- **Discuss without building.** Take S7 ("Make shelf more useful for book clubs"). Under-prompt: "Give me three very different directions." Pick one, ask the agent to write it as a stand-alone issue like S1–S6, and stop there.
- **Compare vendors.** Repeat S3 from scratch with a different vendor's agent and compare the two correction logs row by row.
