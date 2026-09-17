---
title: "Lab 0 — The whole game"
module: 0
kind: lab
minutes: 45
level: foundation
last_reviewed: 2026-09-17
---

# Lab 0 — The whole game

## Goal

Ship one real change with agents in about 45 minutes, and run a second one in parallel while you do it. You will:

1. have an agent explain a codebase it has never seen,
2. discuss, plan and implement issue S1 with tests, and open a pull request,
3. while that runs, start issue S2 in a separate git worktree with a second session,
4. review the first pull request from a third, fresh session that didn't write it.

You will do every step shallowly, on purpose. Nothing is explained in depth here. Each step ends with a pointer to the module that explains it. The point is to see the whole game once, so the rest of the guide has somewhere to land.

## Before you start

**Check the prerequisites** from [module 00](README.md#prerequisites):

```bash
git --version
gh auth status
python --version   # or: python3 --version
claude --version   # or: codex --version
```

In this lab, use `python3` wherever it says `python` if that is how Python 3 is called on your machine.

**Make your own copy of the practice project.** You need a repository you own, so the agents can push branches and open pull requests. From the root of your local copy of this guide (cloned or downloaded), follow the recipe in the [practice project's README](../../../practice/shelf/README.md):

```bash
mkdir -p ~/code
cp -r practice/shelf ~/code/shelf
cd ~/code/shelf
git init -b main
git add .
git commit -m "Start from the Agentic Engineering 101 practice project"
gh repo create shelf --private --source=. --remote=origin --push
python -m unittest
```

**Checkpoint:** the test output ends with `OK` (13 tests at this point), and `gh repo view` shows your new repository. If you already have a repository called `shelf`, pick another name.

**Create two issues.** Open the [practice issue catalog](../../../practice/issues/en.md). Run `gh issue create` twice, and paste the title and body of **S1** (`S1: Filter shelf list by status`) and **S2** (`S2: Search books by title or author`). Leave out their "Parallel safety" lines. **Checkpoint:** `gh issue list` shows both, as #1 and #2. [Lab 5](../05-decompose-into-tracks/lab.md) creates the rest.

**On your own repo:** pick two small issues that touch different files, that you could each finish by hand in under an hour, and where the repository has tests the agent can run. Avoid code that handles money, authentication or production data for this first run.

> [!TIP]
> The tests point `SHELF_PATH` and `HOME` at a temporary folder, so they never touch your real `~/.shelf.json`. When an agent tries the command by hand, ask it to do the same: set `SHELF_PATH` to a temporary file first.

Rough timing: 5 minutes to explain, 10 to discuss and start S1, 10 to start S2, 15 to review, 5 to decide and clean up.

## Steps

### 1. Ask the agent to explain the project (5 minutes)

Open a session in `~/code/shelf` (`claude` or `codex`) and type:

```text
Read README.md, AGENTS.md, the shelf/ package and the tests before you answer.
Then explain in under 200 words: what this tool does, how a command travels
from the command line to the JSON file, and how to run the tests.
Run the tests to confirm. Don't change any files.
```

**Look for:** the four commands (`add`, `list`, `start`, `finish`); one module per command under `shelf/commands/`, found automatically; `cli.py` parsing arguments and turning errors into exit codes; `store.py` reading and writing one JSON file, `~/.shelf.json` unless `SHELF_PATH` says otherwise; and a real test run ending in `OK`. If it describes a feature that doesn't exist, note it. Invented details are a symptom of missing context.

**Checkpoint:** you can say in one sentence how `shelf finish 3` reaches the file.

Explained in: [module 02](../02-one-agent-done-well/README.md) (talk to it like a coworker) and [module 04](../04-context-is-infrastructure/README.md) (context).

### 2. Discuss and plan S1 before any code (5 minutes)

The issue already fixes the behavior: the valid statuses, exit code 2 with an error naming them, and the exact no-match message. What's left to discuss is how to build it. In the same session:

```text
Let's discuss issue #1 before building anything. Read it with gh issue view 1.
Give me two options for implementing it within the acceptance criteria, with
their trade-offs, and quote the exact exit codes and messages the tests must
check. Recommend one. Don't write code until I say build.
```

**Look for:** the exact strings from the issue (`No books with status reading.`, exit code 2 for an invalid status), and real options. For example: let `argparse` validate the value with a fixed list of choices built from `STATUSES` in `shelf/models.py`, or validate it by hand inside the command. If the agent starts editing files, stop it and repeat "don't write code yet".

Pick one option in a single sentence, for example: "Option A: argparse choices from STATUSES, so the usage error comes for free."

**Checkpoint:** you agreed on the approach in no more than three short messages, and no file has changed (`git status` is clean).

Explained in: [module 02](../02-one-agent-done-well/README.md) (discuss, plan, build).

### 3. Build S1 with tests and open a pull request (starts now, runs on its own)

```text
Build it. Work on a new branch named s1-status-filter.
Write the tests first and run them to show they fail. Then implement.
Run the whole suite with python -m unittest and show me the output.
Then commit, push, and open a pull request with gh pr create whose
description says "Closes #1".
```

**Look for:** a failing test run before the implementation, a passing run after, and a pull request URL at the end. Don't watch it work. Go to step 4.

Explained in: [module 03](../03-close-the-loop/README.md) (the agent checks its own work) and [module 05](../05-decompose-into-tracks/README.md) (one pull request, end to end).

### 4. While S1 runs, start S2 in a worktree (10 minutes)

Open a second terminal. A worktree is a second working folder on the same repository, with its own branch, so the two sessions never edit the same files on disk:

```bash
cd ~/code/shelf
git fetch origin
git worktree add --no-track -b s2-search ../shelf-s2 origin/main
cd ../shelf-s2
claude   # or: codex
```

`--no-track` keeps the new branch from tracking `origin/main`, which would confuse `git status` and `git push`. [Module 06](../06-run-sessions-in-parallel/README.md#a-worktree-recipe-that-doesnt-bite) explains why.

> [!TIP]
> In Claude Code, `claude --worktree s2-search` creates the worktree and starts the session in one step, under `.claude/worktrees/` ([worktree docs](https://code.claude.com/docs/en/worktrees)). Add `.claude/worktrees/` to `.gitignore` if you use it.

This session knows nothing about the first one. Give it a short prompt:

```text
Implement issue #2 (read it with gh issue view 2). Before writing code, tell me
in five bullets what you'll change, which files you'll touch, and how you'll test it.
Wait for my ok.
```

Read the five bullets. The issue suggests a new `shelf/commands/search.py` and a new `tests/test_search.py`, and asks for case-insensitive matching that also works with accented letters (`GARCÍA` must find `García`). If the bullets cover that, answer:

```text
ok, build it: tests first, run python -m unittest, then open a pull request that closes #2.
```

When the first session needs you (a question, a permission prompt, a finished pull request), switch to it, answer, and come back. That back-and-forth is the real skill of the outer loop.

**Checkpoint:** `git worktree list` shows two entries, on different branches. S1 changes `shelf/commands/list_books.py` and `tests/test_cli.py`; S2 adds new files. They don't touch the same files, which is what makes them safe to run in parallel.

Explained in: [module 05](../05-decompose-into-tracks/README.md) (independent tracks) and [module 06](../06-run-sessions-in-parallel/README.md) (worktrees and switching between sessions).

### 5. Review the S1 pull request from a fresh session (15 minutes)

Wait until step 3 has opened its pull request. Find its number with `gh pr list`. Then open a **third** session in a worktree of that pull request, so the reviewer shares neither the writer's memory nor its folder:

```bash
cd ~/code/shelf
git fetch origin
git worktree add --detach ../shelf-review origin/s1-status-filter
cd ../shelf-review
claude   # or: codex
```

(In Claude Code, `claude --worktree "#<number>"` does the same from the pull request number.)

```text
You are reviewing a pull request you did not write. Run gh pr view <number>
and gh pr diff <number>, and read the issue it closes. Check, in this order:
1. Does it meet every acceptance criterion, with the exact messages and exit
   codes? Does it do anything the issue doesn't ask for?
2. Would the new tests fail if the change were reverted? Read them, then run
   python -m unittest.
3. Edge cases: an invalid status, no matching books, an empty shelf, and
   shelf list without --status.
Report only problems that affect correctness or the issue's requirements,
most serious first, each with a file and line. If you find none, say so and
show the test output. Don't change any files.
```

**Look for:** findings with a file and line, or a clear "no correctness problems" backed by a test run. A review that only praises the code, or only lists style preferences, is not a review.

For each finding, decide one of three things: **fix now** (paste it into the first session: "Here's review feedback: … Fix what is a real correctness problem, push, and tell me what you changed"), **file an issue** for later, or **discard** it with a one-line reason.

> [!TIP]
> Codex has a built-in `/review` command that can review against a base branch, uncommitted changes or a commit ([Codex best practices](https://learn.chatgpt.com/guides/best-practices)). If you have both tools, try reviewing with the one that didn't write the code.

**Checkpoint:** every finding has a decision next to it, written down.

Explained in: [module 07](../07-agents-review-agents/README.md) (agents review agents, triage by decision).

### 6. Decide, merge and clean up (5 minutes)

If the S1 pull request is good, merge it yourself on GitHub. An agent can prepare everything, but the merge is your decision. Leave S2 running or finished; you can merge it now or later.

Remove the review worktree. It has no changes, so this is safe:

```bash
cd ~/code/shelf
git worktree remove ../shelf-review
git worktree list
```

Keep `../shelf-s2` until its pull request is merged, then remove it the same way.

Explained in: [module 06](../06-run-sessions-in-parallel/README.md) (session hygiene) and [module 09](../09-teams-and-organizations/README.md) (humans at the gates).

## Done when

- [ ] `gh pr list --state all` shows a pull request for S1, with passing tests shown in the session or in the pull request.
- [ ] S2 has a pull request, or `git worktree list` still shows `shelf-s2` with work in progress.
- [ ] You have the fresh reviewer's findings, and each one has a decision: fix now, issue, or discard.
- [ ] `git worktree list` no longer shows `shelf-review`.
- [ ] For each of the six steps, you can name the module that explains it.

## Reflect

Write three lines in a notes file. You will reuse them in [lab 1](../01-from-chatbot-to-system/lab.md).

- **Where did you wait?** Count the moments you watched an agent work instead of doing something else.
- **What did you check yourself that the agent could have checked?** Every one of those is work for [module 03](../03-close-the-loop/README.md).
- **Did the fresh reviewer find anything the writer missed?** If it did, ask yourself why the writer didn't. If it didn't, was the review too gentle, or the change genuinely fine?
- **When did you lose track** of which session was doing what? That feeling is the bottleneck this guide keeps coming back to: your attention.

## Stretch

- Ask the S1 session: "Now that you built it, what would you have done differently?" Decide whether the answer is worth a follow-up issue.
- Merge S2 after S1. They add and change different files, so you shouldn't get a conflict. If you do, ask the S2 session to merge `origin/main` into its branch, adapt, run the tests again and push (no force-push needed), and ask it why the files overlapped.
- Repeat step 5 with an agent from a different vendor, and compare what each reviewer found.
