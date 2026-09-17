---
title: "Lab 4 — Give the project a memory"
module: 4
kind: lab
minutes: 45
level: intermediate
last_reviewed: 2026-09-17
---

# Lab 4 — Give the project a memory

## Goal

Build the context layer for the practice project, then measure what it changes. You will:

1. ask a fresh session three questions about the project and save its answers,
2. write an `AGENTS.md` contract and a `CLAUDE.md` that imports it,
3. create `kb/ACTIVE.md` and one decision record, and commit them,
4. ask a new fresh session the same three questions and compare,
5. plant a false fact in the knowledge base and check that the agent trusts the code over the snapshot.

## Before you start

- Your own copy of the practice project, set up as in [Lab 0](../00-start-here/lab.md), with a clean `main`. The steps assume it lives in `~/code/shelf`; use your own path if it differs. The Stop gate from [Lab 3](../03-close-the-loop/lab.md) is useful but not required.
- Claude Code or Codex, and the GitHub CLI signed in.
- A notes file **outside** the repository, for example `~/notes/lab-4.md`.
- About 45 minutes.

**On your own repo:** use the tracks you really have in flight (two to five), and pick one decision that someone, human or agent, has already tried to re-open. That decision is the most valuable record you can write today.

## Steps

### 1. Ask the questions before there is any context (5 minutes)

```bash
cd ~/code/shelf
git switch main && git pull
git switch -c lab-4-context
```

Start a fresh session and paste:

```text
Answer from what you can find in this repository and on GitHub, and say where
each answer comes from:
1. What are we working on right now, and why?
2. Issues C1 (tags) and C2 (versioning the file format) both change how books
   are stored. Which one goes first, and what does the other one then have to do?
3. What must be true before you call a change to this project done?
Don't change any files.
```

Copy the three answers into your notes under **Before**, then exit the session.

**Look for:** answers built from guesses. The agent may find open issues with `gh issue list`, but it can't know your priorities, your decision on C1 and C2, or your definition of done. Note every answer that sounds confident but has no source.

**Checkpoint:** your notes have three "Before" answers, and `git status` is clean.

### 2. Write down what only you know (5 minutes, no agent)

In your notes, write five short bullets:

- **Objective:** what the project is working toward now. For example: "get shelf ready for book clubs (S7), starting with tags".
- **Tracks:** the work in flight and its next gate. Use your real state from earlier labs (open pull requests, merged ones, issues you created).
- **Decision:** C1 or C2 first. Both change the stored fields that `tests/test_store.py` pins exactly, so they conflict. Pick one:
  - *C1 first:* tags ship sooner, and C2's version 2 of the format includes tags from day one.
  - *C2 first:* the file gets a version before anything else changes, and C1 becomes version 3 with its own migration.
- **Why:** one sentence for your choice.
- **Done means:** for example, "`python3 -m unittest` passes, the Stop gate passes, and a new behavior has a test that fails when the change is reverted".

**Checkpoint:** five bullets, including a decision with a reason. You record this decision as `D-0001` in step 5. [Lab 5](../05-decompose-into-tracks/lab.md) reuses that record when it plans the merge order, and [Lab 6](../06-run-sessions-in-parallel/lab.md) applies it, so you decide only once.

### 3. Write the contract with the agent (10 minutes)

The practice project ships a deliberately minimal `AGENTS.md`. Start a session and paste, with your bullets at the end:

```text
Replace AGENTS.md with a short contract for agents working on shelf, under 60
lines. Read README.md, the shelf/ package and the tests first. Include only what
can't be derived from the code:
- first, a pointer to kb/ACTIVE.md (read it before anything else) and kb/decisions/,
- a map of where things live, one line per entry,
- the commands to run the tool and the tests,
- the rules a change must follow (standard library only; new commands go in
  shelf/commands/; tests use a temporary SHELF_PATH),
- what "done" means.
Leave out file-by-file descriptions and anything the tests already enforce.
Then create CLAUDE.md containing only the line @AGENTS.md.
My notes:
<paste your five bullets>
```

**Look for:** commands that really exist (run them), no invented tooling (a lint command the project doesn't have, a `make` target), and a "done" section that matches your notes. If something is wrong, correct it in one sentence ("there is no linter; remove that line") instead of editing the file yourself.

**Checkpoint:**

```bash
wc -l AGENTS.md          # under 60
head -1 CLAUDE.md        # @AGENTS.md
python3 -m unittest      # still OK
```

**Codex:** Codex reads `AGENTS.md` directly. Keep `CLAUDE.md` anyway, so teammates on Claude Code get the same contract.

### 4. Create the ACTIVE index (5 minutes)

In the same session:

```text
Create kb/ACTIVE.md as an index of work in flight, under 40 lines, with these
sections: Current objective, Next step, Active tracks, Blockers, Links.
Active tracks is a table with columns Track | Issue | PR | State | Next gate,
one row per track. Use my notes and the real state on GitHub (gh issue list,
gh pr list). No history, no CI counts, no commit hashes.
```

**Look for:** rows that state a state and a gate, not a story. If a row reads like a diary ("started, then fixed, then…"), ask: "Rewrite that row as a state and a next gate."

**Checkpoint:** `wc -l < kb/ACTIVE.md` prints a number under 40, and every issue and pull request number in the table exists (`gh issue view <n>`, `gh pr view <n>`).

### 5. Record the decision (5 minutes)

```text
Record our C1/C2 decision in kb/decisions/D-0001-storage-change-order.md, with
front matter (id, title, status: accepted, decided_on) and the sections Context,
Options considered, Decision and Consequences. In Context, cite the evidence in
the code: tests/test_store.py pins the exact stored fields, so both issues must
change it. Link the record from the ACTIVE row it affects.
```

**Checkpoint:**

```bash
grep -n "status: accepted" kb/decisions/D-0001-*.md
grep -n "D-0001" kb/ACTIVE.md
```

### 6. Commit the knowledge base (2 minutes)

An uncommitted knowledge base change did not happen. Commit it before you test it:

```bash
git add AGENTS.md CLAUDE.md kb
git commit -m "Add the agent contract and a knowledge base"
git status --short       # prints nothing
```

Exit the session.

### 7. Ask the same questions in a fresh session (5 minutes)

Start a **new** session and paste exactly the prompt from step 1. Copy the answers into your notes under **After**.

**Look for:**

- Answer 1 names your objective and cites `kb/ACTIVE.md`.
- Answer 2 gives *your* decision and its reason, and cites `D-0001`, instead of general reasoning.
- Answer 3 matches your definition of done.
- It got there faster, with fewer files read. If the session shows context or token usage, compare it with step 1.

**Checkpoint:** under "After", write one sentence about what changed and one about what is still missing.

### 8. Plant a false fact (5 minutes)

A knowledge base is a snapshot. Check that the agent treats it as one. Add this row to the tracks table in `kb/ACTIVE.md`, and **don't commit it**:

```markdown
| CSV export | S4 | — | Merged | — |
```

Start a new session and ask:

```text
Can I export my shelf to CSV today? Show me the exact command.
```

**Look for:** a good answer checks the code or `python3 -m shelf --help`, finds no `export` command, and tells you the knowledge base disagrees with the code. A weak answer invents a command because `ACTIVE.md` says it shipped.

If the answer is weak, add this rule to `AGENTS.md`, start another session, and ask again:

```markdown
- The knowledge base is a snapshot. When it disagrees with the code, `--help`
  or GitHub, trust those and tell me about the disagreement.
```

Then remove the fake row:

```bash
git restore kb/ACTIVE.md
```

If you added the rule, commit it: `git commit -am "AGENTS.md: live systems win over the knowledge base"`.

**Checkpoint:** a session flagged the disagreement, with or without the new rule, and `git status --short` prints nothing.

Push the branch and open a pull request with `gh pr create --fill`. Merge it when you're happy, so every later session starts with this context.

## Done when

- [ ] `head -1 CLAUDE.md` prints `@AGENTS.md`, and `wc -l < AGENTS.md` prints a number under 60.
- [ ] `kb/ACTIVE.md` is under 100 lines and has a table with the columns Track, Issue, PR, State and Next gate.
- [ ] `ls kb/decisions/` lists one record, and it contains `status: accepted`.
- [ ] `git status --short` prints nothing, and `gh pr list` shows your pull request (or it is already merged).
- [ ] Your notes have "Before" and "After" answers to the same three questions.
- [ ] A fresh session flagged the planted `CSV export` row as wrong.

## Reflect

- Which answer improved most between "Before" and "After"? Which didn't, and what context was missing?
- Read your `AGENTS.md` line by line and ask of each one: "Would removing this cause the agent to make mistakes?" Which lines would you delete?
- What did you correct in more than one session during labs 0 to 3? Is it a memory entry, an `AGENTS.md` rule or a guard?
- Step 8 is the reason live systems win. Where in your own repository does a document still claim something the code no longer does?

## Stretch

- **Load ACTIVE deterministically.** Add a `SessionStart` hook that prints `kb/ACTIVE.md`, so it is in context even after compaction. In Claude Code, `.claude/settings.json` then holds both hooks from labs 3 and 4:

  ```json
  {
    "hooks": {
      "SessionStart": [
        {
          "matcher": "startup|resume|clear|compact",
          "hooks": [{ "type": "command", "command": "cat \"${CLAUDE_PROJECT_DIR}/kb/ACTIVE.md\"" }]
        }
      ],
      "Stop": [
        {
          "hooks": [{ "type": "command", "command": "python3 \"${CLAUDE_PROJECT_DIR}/scripts/stop_gate.py\"", "timeout": 120 }]
        }
      ]
    }
  }
  ```

  In Codex, add the same `SessionStart` entry to `.codex/hooks.json`, with `cat "$(git rev-parse --show-toplevel)/kb/ACTIVE.md"` as the command, and trust it with `/hooks`.
- **Supersede a decision.** Strategy changed: book clubs need the other order after all. Ask the agent to record `D-0002` that reverses `D-0001`, mark `D-0001` as superseded with `superseded_on`, `superseded_by` and a banner under its title, and update the ACTIVE row. Check that nothing was deleted: `git diff --stat` shows `D-0001` modified, not removed.
- **Write one memory entry.** Take a correction you gave an agent in labs 0 to 3 and ask the agent to save it as `kb/memory/<slug>.md` with **Rule**, **Why** and **How to apply**, plus a one-line entry in `kb/memory/README.md`. Commit both.
- **Guard the budget.** Extend the Stop gate from Lab 3 so it also fails when `kb/ACTIVE.md` has more than 100 lines, with a message that tells the agent what to remove.
- **On your own repo:** repeat steps 1 and 7 with your real tracks and your most re-opened decision. Share the before and after answers with a teammate.
