---
title: "Lab 5 — From a backlog to parallel tracks"
module: 5
kind: lab
minutes: 60
level: intermediate
last_reviewed: 2026-09-17
---

# Lab 5 — From a backlog to parallel tracks

## Goal

Have an agent turn the practice issue catalog into GitHub issues, find the overlaps between them on its own (including the one conflict that needs a human decision), apply the decision you already recorded for that conflict in [Lab 4](../04-context-is-infrastructure/lab.md), group the issues into tracks, and write kickoff prompts for three tracks that you will run at the same time in [Lab 6](../06-run-sessions-in-parallel/lab.md).

You practice the skills of [module 05](README.md): issues as prompts, sizing by blast radius, planning a merge order, and kickoff prompts that settle decisions before a session starts.

## Before you start

- **Your copy of the practice project on GitHub.** If you did [Lab 0](../00-start-here/lab.md) you already have one. Otherwise follow "Use it for the labs" in the [practice project README](../../../practice/shelf/README.md) (it uses `~/code/shelf`). This lab calls that folder "your repository".
- **GitHub CLI logged in:** `gh auth status`.
- **A clean, current `main`:** `git fetch origin && git status` in your repository says you're on `main`, up to date, with nothing to commit.
- **Recommended:** [Lab 4](../04-context-is-infrastructure/lab.md), so your repository has an AGENTS.md, a `kb/ACTIVE.md` and the C1/C2 decision record `kb/decisions/D-0001-storage-change-order.md`. The lab works without them: skip the `ACTIVE.md` parts, and make the decision in step 3.
- **Earlier work:** keep any issues you already opened for S1, optional S2, S3 or S6. Step 1 reuses them, including closed issues.

**On your own repo:** collect 6 to 12 upcoming pieces of work (backlog items, roadmap notes, a list from a meeting) in one file the agent can read. Include at least one pair you suspect will collide. Where this lab uses `gh`, use your tracker's CLI, or have the agent write drafts you paste in yourself.

## Steps

### 1. Create the issues from the catalog (10 minutes)

Open your agent in your Shelf folder. In Academy, choose **Copy task for my agent** and paste it into the session. It includes the nine issue descriptions. If you are reading on GitHub, paste the prompt and then the linked catalog into the same message.

```text
Use the nine Shelf issues below. Run gh repo view and show me the owner and repository. Wait for my confirmation before creating or changing any issues.

After I confirm, list the open and closed issues. Match each catalog ID to its existing issue, including closed ones. Create only the missing issues with gh issue create. Use the exact title and the Problem, Acceptance criteria, Likely touches and Out of scope sections. Write each body to a temporary file and use --body-file to preserve its Markdown. Leave labels, assignees and milestones empty.

If I completed Lab 3, ask me for the S6 pull request URL. Once I provide it, link the PR in a comment and close S6 if it is still open. If I skipped Lab 3, leave S6 as it is.

Show me a table of the nine IDs, issue numbers, titles and states. Stop there so I can check the result.
```

[Nine Shelf issue descriptions](../../../practice/issues/en.md "copy-task")

**Look for:** the agent stops after `gh repo view` and waits for your OK. If your setup asks permission for every `gh issue create`, that's the guardrail from [module 03](../03-close-the-loop/README.md) doing its job: creating issues is an outward action, and you're the gate.

**Checkpoint:** `gh issue list --state all --limit 30` shows exactly one issue for each of S1–S7, C1 and C2. Deciding what can run in parallel is your job in step 2.

### 2. Find the overlaps before planning (10 minutes)

In the same session:

```text
Read AGENTS.md, the shelf/ package and the tests, then read every open issue
with gh issue view. Don't create or change anything. Tell me:
1. For each issue: the files it will likely touch, the shared contracts it
   changes (data formats, public functions, command output), and a size
   (S, M or L).
2. Every pair of issues that overlaps. Say whether each overlap is textual
   (same lines, git will stop) or semantic (same contract, git may merge it
   and the result can still be wrong), and why.
3. Any issue that isn't ready to implement as written.
```

**Checkpoint:** save the agent’s proposed overlaps and its evidence before continuing. Check one claim against the code yourself. If the analysis misses a shared contract, ask which issues change the stored file format and note whether that changes the answer. `git status` should still be clean.

### 3. Apply the decision you already made (5 minutes)

C1 and C2 can merge in either order, with different consequences:

- **C1 first:** C2 adapts, and version 2 of the file includes `tags`. One version, less code.
- **C2 first:** C1 adapts, bumps the file to version 3 and adds a migration from version 2. More code, but it's what a real project does once version 2 has shipped.

Only a human can choose, and you already did: Lab 4 recorded the choice as `D-0001`. Don't decide twice. Point the agent at the record:

```text
Our C1/C2 decision is in kb/decisions/D-0001-storage-change-order.md. Add a
"Coordination" section to the bodies of C1 and C2: the semantic conflict, the
merge order, the decision with its date and a link to D-0001, and what the
second one must do to adapt. If S1 or S6 is still open, add its textual
overlap with C1 to both issues (it merges before C1). Use gh issue edit with
--body-file, then re-read each issue with gh issue view and confirm the edit
landed.
```

If you skipped Lab 4, pick one order now, and replace the prompt's first sentence with `Decision: <C1 first | C2 first>, because <one sentence>. First record it, dated today, in kb/decisions/D-0001-storage-change-order.md.`

**Look for:** the re-read. Tools sometimes fail silently, and a write isn't done until you've read it back.

**Checkpoint:** `gh issue view` on C1 and on C2 shows a Coordination section naming the other issue by number, with the decision from `D-0001` and its date.

### 4. Group into tracks and plan the merges (10 minutes)

```text
Group the open issues into tracks. A track is work that one session can do in
one worktree without editing files another track owns. Rules: one issue, one
PR (don't phase issues); issues that aren't ready are not tracks; use the
merge order in D-0001. For each track give: its issues, the files it owns,
its merge constraints, and a priority computed as
(business value + time criticality + risk reduction) / effort,
with one sentence justifying each score.
Write it to kb/tracks.md with a small mermaid flowchart where an arrow means
"merges before". If kb/ACTIVE.md exists, add one row per track.
```

**Look for:** C1 and C2 in separate tracks (or combined, with a good reason), S7 left out, any open issue that overlaps C1 (S1, S6) merging before it, a note about a follow-up for "export includes tags", and priority scores you would defend. Correct any score you disagree with in one sentence.

**Checkpoint:** `kb/tracks.md` exists and states the C1/C2 order from `D-0001`. If you have an `ACTIVE.md`, `wc -l kb/ACTIVE.md` is still under 100 lines.

### 5. Write kickoff prompts for three tracks (15 minutes)

Lab 6 runs these three tracks at the same time:

- **Track A:** S4 and S5, independent issues that add files (plus S5's `remove` method in `shelf/store.py`).
- **Track B:** C1.
- **Track C:** C2.

If you skipped earlier labs and S1, S2, S3 or S6 is still open, add it to Track A, which merges first. S2 and S3 only add files, and S1 and S6 have to merge before C1 anyway. If one of them already has an open pull request from its lab, merge that pull request instead of starting the issue again.

```text
Write kickoff prompts for three tracks that will run at the same time:
A (<issues>), B (C1, #<number>) and C (C2, #<number>).
Each prompt needs these sections: goal; what I already checked (facts with
file:line from your analysis, so the session doesn't re-derive them); do this
first: prove the premise; decisions already made, don't re-open them; scope
and "report, don't fix"; repo rules that will fail the build; environment
notes; coordination with the other two tracks; if you find yourself making
design decisions, stop and report; done when; report back.
Track A does its issues one after the other, one branch and one PR each.
Worktrees: ../shelf-a, ../shelf-c1 and ../shelf-c2. Branches: one per issue,
named after it (for example s4-export, c1-tags, c2-file-version).
Each session uses its own SHELF_PATH. Save the prompts as kb/kickoffs/a.md,
kb/kickoffs/c1.md and kb/kickoffs/c2.md.
```

(If you have [the kickoff prompt template](README.md#the-kickoff-prompt) open, paste it after the prompt.)

**Look for:**

- `D-0001` under "decisions already made" in both B and C.
- In the prompt for the track that merges second: "when told the other one has merged, merge `origin/main` and adapt", with what adapting means.
- In Track A: it can merge at any time and must not touch `models.py` or `store.py` (S5 excepted, for its `remove` method).
- Every "done when" includes `python -m unittest`.

**Checkpoint:** `ls kb/kickoffs/` shows the three files.

### 6. Test one prompt cold (5 minutes)

Open a **new** session with no memory of this one. Paste the contents of the kickoff prompt for the track that merges *second* (C1 or C2), then:

```text
Before doing anything (don't change files, don't create a worktree),
answer in bullets: what will you do first, which decisions are already made,
what is out of scope, what will you do when the other track merges, and how
will you know you're done? Then list every question you'd need answered
before starting.
```

**Look for:** answers that come straight from the prompt. Every question on its list is a gap in your prompt, not a flaw in the agent. Fix the file for each real gap, then close this session.

**Checkpoint:** the question list is empty, or every question is now answered in the file.

### 7. Commit the plan (5 minutes)

Run these yourself:

```bash
git add kb/
git commit -m "Plan tracks and kickoff prompts for lab 6"
git push
```

**Checkpoint:** `git status` is clean, and `git log -1 --stat` lists the files under `kb/`.

## Done when

- [ ] `gh issue list --state all --limit 30` shows one issue per catalog entry (S1–S7, C1, C2), with no duplicates.
- [ ] `gh issue view` on C1 and on C2 shows a Coordination section that names the other issue, the merge order and the dated decision from `D-0001`.
- [ ] S7 has no implementation plan.
- [ ] `kb/tracks.md` lists the tracks, the files each one owns, priorities with justifications and a mermaid diagram.
- [ ] `ls kb/kickoffs/` shows `a.md`, `c1.md` and `c2.md`, and the second-to-merge prompt passed the cold test.
- [ ] `git status` is clean and the commit is pushed.

## Reflect

- Did the agent find the C1/C2 conflict without help? Did it call it semantic, or only notice the shared test file? What in the code could have made it more obvious?
- Which decisions did you make in a single sentence today? Where are they written now, and will a session in Lab 6 find them without you?
- How much time did you spend reading issue bodies, and how much reviewing the plan the agent explained? What would you skip next time?
- Look at one kickoff prompt. Which section would you drop for a one-line fix, and which would you never drop?

[Compare my plan with the solution](../../../practice/issues/en-solution.md). Which differences would change your merge order?

## Stretch

- **Discuss S7.** Follow its acceptance criteria: ask the agent for the questions that need answers and two or three options, each naming the commands it adds, the files it touches and whether it changes the file format. Pick one, record the decision in `kb/decisions/`, and create issues for the first slice only.
- **Write a handoff pack** for this planning session, as if you were leaving for a week. Use [the handoff pack template](README.md#handoff-packs). Tomorrow, open a fresh session, paste only the bootstrap prompt, and see whether it carries on correctly.
