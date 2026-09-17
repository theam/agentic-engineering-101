---
title: "Lab 6 — Three tracks at once"
module: 6
kind: lab
minutes: 90
level: intermediate
last_reviewed: 2026-09-17
---

# Lab 6 — Three tracks at once

## Goal

Run the three tracks you planned in [Lab 5](../05-decompose-into-tracks/lab.md) at the same time, each in its own worktree with its own data. Handle the sessions round-robin as they need you, merge in the planned order, and resolve the C1/C2 conflict by applying the decision you already made.

Along the way, keep an attention log. The code is the practice project's; the log is about you.

## Before you start

- **Lab 5 done:** the issues exist, `kb/tracks.md` records your C1/C2 merge order from `D-0001` (the decision you recorded in [Lab 4](../04-context-is-infrastructure/lab.md)), and `kb/kickoffs/` holds `a.md`, `c1.md` and `c2.md`, pushed to `main`. If you skipped Lab 5, use the answer key at the end of the [issue catalog](../../../practice/issues/en.md) and write three short kickoff prompts with at least a goal, the merge order, the decision about version 2 and a "done when". If you skipped Lab 4 too, make that decision now and write it down.
- **If you skipped earlier labs,** any of S1, S2, S3 or S6 that is still open belongs to Track A, which merges first, as [Lab 5](../05-decompose-into-tracks/lab.md) step 5 explains.
- **Your repository** is up to date on `main`: `git fetch origin && git status`. The commands below assume it lives at `~/code/shelf`; adjust if yours is elsewhere.
- **Screen space for six panes:** one agent and one plain shell per track. Split panes in your terminal, tmux, or an agent-aware terminal all work (see [module 06](README.md#managing-many-sessions)).
- **Notifications on** in your agent or terminal, so a session that finishes or needs input tells you.
- **An attention log** outside the repository, for example `~/lab6-log.md`.
- **About 90 minutes.** Most of it is agent time. Your job is decisions.

**On your own repo:** pick three tracks from your own decomposition, including at least one pair with a planned merge order. Instead of `SHELF_PATH`, give each worktree its own port and database (see [module 06](README.md#isolate-resources-not-just-files)).

## Steps

### 1. Write the merge order at the top of your log (2 minutes)

```text
Merge order: A (S4, then S5)  ->  C1  ->  C2      (or C2 before C1: follow D-0001)
Decision (D-0001): <version 2 includes tags | C1 bumps to version 3>
Log: time | session | what it needed | my minutes | could the prompt have avoided it?
```

Put the sessions on screen in the same order: the track that merges first at the top.

**Checkpoint:** the order in your log matches `kb/tracks.md` and `D-0001`.

### 2. Create three worktrees (5 minutes)

From your repository:

```bash
cd ~/code/shelf
git fetch origin
git worktree add --no-track -b s4-export ../shelf-a origin/main
git worktree add --no-track -b c1-tags ../shelf-c1 origin/main
git worktree add --no-track -b c2-file-version ../shelf-c2 origin/main
git worktree list
```

Use the branch name of Track A's *first* issue (here S4). The session creates the branch for its second issue later.

**Checkpoint:** `git worktree list` shows four entries, each on its own branch, and `git -C ../shelf-c1 status -sb` prints `## c1-tags` with no upstream after it.

### 3. Give each track its own data (5 minutes)

The tests already use temporary files. Manual runs don't, so give each track its own shelf file. In each track's **plain shell**:

```bash
mkdir -p ~/shelf-lab-data
cd ~/code/shelf-c1                               # ../shelf-a, ../shelf-c2 in the others
export SHELF_PATH=~/shelf-lab-data/c1.json       # a.json, c2.json in the others
python -m unittest
```

Now prove the isolation. In the C1 shell run `python -m shelf add "Dune" "Frank Herbert"`. In the C2 shell run `python -m shelf list`.

**Checkpoint:** the C2 shell prints `Your shelf is empty. Add a book with: shelf add TITLE AUTHOR`, and the tests pass in all three worktrees.

### 4. Launch the sessions (10 minutes)

In each track's **agent pane**, start the agent from the worktree with the same variable, and name the session after the track:

```bash
cd ~/code/shelf-c1
export SHELF_PATH=~/shelf-lab-data/c1.json
claude -n c1-tags        # or: codex
```

Paste the track's kickoff prompt (`kb/kickoffs/c1.md` is in the worktree too, because you pushed it before creating the worktrees). Add this at the end:

```text
Before changing anything, tell me in five bullets what you'll do first and
which files you'll touch. Then wait for my ok.
```

For Track A, also add:

```text
When the PR for the first issue is open, start the second issue on a new
branch from a fresh main in this same worktree:
git fetch origin && git switch --no-track -c <branch> origin/main
```

**Look for:** in each five-bullet plan, files that belong to another track. If C2's plan mentions `shelf/commands/add.py`, or Track A's mentions `models.py`, stop and correct it before saying ok.

**Checkpoint:** three named sessions, each waiting with a plan. Write down each session's name or ID in your log.

### 5. Run the round-robin (30 to 50 minutes)

Say ok to the plans from top to bottom. Then follow these rules until every track has reported a PR:

1. **Don't watch the streams.** If nothing needs you, re-read the next kickoff prompt, prepare the merge checks, or do nothing.
2. **When a notification arrives,** finish the decision you're making, then go to the *highest* session that's waiting, not the one that pinged last.
3. **Log every interaction** in one line:

   ```text
   10:42 | c2 | asks whether an unknown version exits with 1 or 2 | 1 min | yes: the issue says 1, the prompt didn't point to it
   ```

4. **Decide in one sentence, and make it stick.** If a session asks something the issue and prompt don't settle, answer, then add the answer to that track's kickoff file so a restarted session would know it.
5. **Keep sessions inside their lanes.** No session stops processes it didn't start, edits another track's worktree or pushes to `main`.

**Look for:** sessions that report back with a PR URL, the commands they ran and anything they had to decide. A session that says "done" without test output isn't done.

**Checkpoint:** `gh pr list` shows an open PR for each issue in the three tracks, and your log has an entry for every interaction.

### 6. Merge Track A (5 minutes)

The full review is [Lab 7](../07-agents-review-agents/lab.md). Before merging here, do the minimum in Track A's plain shell, for each PR:

```bash
gh pr diff <number> --name-only
python -m unittest
```

**Look for:** only files that Track A owns (new files under `shelf/commands/` and `tests/`, plus `shelf/store.py` for S5's `remove` method). Anything else is a question for the session before you merge.

```bash
gh pr merge <number> --squash
```

> [!TIP]
> **Going on to Lab 7?** It reviews a PR from this lab before it merges. The preferred one is the second C-track PR: when you reach step 9, leave it open, do Lab 7 on it, and come back for steps 9 and 10 afterwards. If you also want to practice on S5's out-of-scope edge case (reusing an id after removing the newest book), leave S5's PR open here too: it merges cleanly with C1 and C2, so it can wait. The merge order still applies to everything else.

**Checkpoint:** `gh pr view <number> --json state --jq .state` prints `MERGED` for each Track A PR, except S5's if you kept it open for Lab 7.

### 7. Merge the first of C1 and C2 (5 minutes)

Same checks, in that track's plain shell: `gh pr diff <number> --name-only`, then `python -m unittest`, then `gh pr merge <number> --squash`. Then tell the other session:

```text
<C1 or C2> has merged into main.
```

Don't give more instructions yet. The kickoff prompt already says what to do. Watch whether it does.

**Checkpoint:** the first PR shows `MERGED`, and you logged how long the second session took to start adapting.

### 8. Resolve the conflict in the second track (15 minutes)

If the session didn't start on its own, or went straight to editing, send this:

```text
Merge origin/main into your branch. Don't rebase and don't force-push.
Before resolving any conflict, explain each one: what each side changed, and
what our decision says the result must be. Remember that git can merge a
file cleanly and still leave it wrong. Then resolve, run python -m unittest,
and show me the stored-format tests and their output. Push when they pass.
```

We merge `origin/main` into the branch instead of rebasing so that nobody has to force-push. Force-push is one of the commands [module 03](../03-close-the-loop/README.md) keeps away from agents, and the squash merge at the end makes the branch history irrelevant anyway.

**Look for:**

- Git stops on `tests/test_store.py`, while `models.py` and `store.py` merge "cleanly". The explanation should say why the clean merge isn't enough.
- **If C1 merged first:** version 2 includes `tags`, and loading an old bare-list file gives every book an empty tag list. Check one edge case yourself: a bare-list file written *after* C1 merged already contains tags. Does the migration keep them?
- **If C2 merged first:** C1 bumps `SCHEMA_VERSION` to 3, adds a migration from version 2, and the stored-fields test pins both versions.

**Checkpoint:** `python -m unittest` passes in the worktree, and `gh pr view <number> --json mergeable --jq .mergeable` prints `MERGEABLE`. (If it prints `UNKNOWN`, GitHub is still computing it; run it again in a few seconds.)

### 9. Merge and check `main` (5 minutes)

```bash
gh pr merge <number> --squash
cd ~/code/shelf
git pull
python -m unittest
git log --oneline -6
```

Then try the result by hand with a fresh file:

```bash
export SHELF_PATH=~/shelf-lab-data/main.json
python -m shelf add "Dune" "Frank Herbert" --tag sci-fi
python -m shelf list
cat "$SHELF_PATH"
```

**Checkpoint:** the tests pass on `main`, `git log` shows the merges in your planned order, `list` prints `#1 [to-read] Dune by Frank Herbert (sci-fi)`, and the file is a JSON object with a `version` and a `books` list whose book has `tags`.

### 10. Clean up (5 minutes)

First confirm what merged: `gh pr list --state merged`. Then, from your main checkout, remove only the worktrees whose PRs have merged:

```bash
git worktree remove ../shelf-a
git worktree remove ../shelf-c1
git worktree remove ../shelf-c2
git branch -D s4-export s5-remove c1-tags c2-file-version
git worktree prune
git worktree list
rm -rf ~/shelf-lab-data
```

Adjust the branch names to the ones your tracks used. `-D` is needed because squash merges leave the branch commits outside `main`; it's safe once `gh` says the PR merged. If you kept a PR open for Lab 7, keep its worktree and branch too. If you have a `kb/ACTIVE.md`, delete the rows of the tracks that shipped.

**Checkpoint:** `git worktree list` shows only your main checkout, plus any worktree you kept on purpose.

## Done when

- [ ] `gh pr list --state merged` shows the PRs of all three tracks (except any you kept open for Lab 7).
- [ ] `git log --oneline` on `main` shows the merges in the order you planned in Lab 5.
- [ ] `python -m unittest` passes on an up-to-date `main`.
- [ ] A shelf file written by `main` has a `version`, and books with `tags`; a test loads a file in the old bare-list format.
- [ ] `git worktree list` shows only your main checkout, plus any worktree you kept on purpose.
- [ ] Your attention log has one line for every time a session needed you.

## Reflect

Use your log to answer:

- How many times did a session need you? How many of those could a better issue or kickoff prompt have avoided? Update the prompt templates now, while you remember.
- What was the longest a session waited for you, and why? What was the longest *you* waited with nothing to decide?
- Did git's conflict show you the real problem in C1/C2, or did you need the decision? What would have happened if each session had decided on its own?
- Did notifications help, or did they interrupt? Would [Hashimoto's advice](https://mitchellh.com/writing/my-ai-adoption-journey) to turn them off have worked better with three sessions? With ten?
- Was three the right number for you today? What would have to be true to run five?

## Stretch

- **Try the one-folder model.** Pick two small issues that are still open (S3 and S6 if you skipped labs 2 and 3; otherwise two issues that came out of discussing S7, as in Lab 5's stretch) and implement them in one shared checkout at the same time, with each agent committing only the files it changed. Log every surprise and compare with the worktree tracks.
- **Use a subagent.** Run Track A as a subagent in its own worktree, launched from a planning session, instead of a window of its own. Compare what you could see and steer.
- **Hand off mid-track.** Stop the second-to-merge session halfway, have it write a handoff pack ([module 05](../05-decompose-into-tracks/README.md#handoff-packs)), and finish the track from a fresh session given only the bootstrap prompt.
- **Try the other merge order.** On a scratch branch, land C1 and C2 in the opposite order and compare the amount of code and tests each order produced.
