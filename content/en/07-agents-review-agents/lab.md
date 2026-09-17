---
title: "Lab 7 — Two reviewers, one ledger, one decision"
module: 7
kind: lab
minutes: 75
level: advanced
last_reviewed: 2026-09-17
---

# Lab 7 — Two reviewers, one ledger, one decision

## Goal

Take one real pull request through the whole review loop from [the lesson](README.md): an intent statement, a fresh-context reviewer, a second-vendor reviewer, a triage ledger, a batch of fixes, and a closing decision that you make yourself.

You will track two numbers per round, **high-priority findings** and **diff size**, so you can see whether the loop converges.

## Before you start

- **A PR to review that isn't merged yet.** Use a PR from [Lab 6](../06-run-sessions-in-parallel/lab.md) in your copy of the [practice project](../../../practice/shelf/). The C1 (tags) or C2 (file format version) PRs give reviewers the most to find. S5's PR ("Remove a book, with confirmation") is good review material too: its issue puts id reuse after removing the newest book out of scope, so watch whether your reviewers respect that. If you skipped Lab 6, ask an agent in a new worktree to implement S5 from the [issue catalog](../../../practice/issues/en.md), with tests, and open a PR with `gh pr create`. If you already merged every Lab 6 PR, do the same with an issue that is still open, such as one that came out of discussing S7.
- **On your own repo:** pick an agent-written PR with 200 to 1,000 changed lines that isn't merged yet.
- **Two coding agents from different vendors**, for example Claude Code and Codex. If you only have one, run the second review in another fresh session with a different focus (tests and error handling), and note in your reflection that this setup is weaker.
- `gh` signed in. Check with `gh auth status`.
- A log file **outside the repository**, for example `~/review-log.md`, with this table:

```markdown
| Round | High-priority findings (P0+P1) | Additions + deletions | Notes |
| --- | --- | --- | --- |
```

## Steps

1. **Measure the starting point.**

   ```bash
   gh pr view <n> --json additions,deletions,changedFiles
   ```

   **Checkpoint:** your log has a round 0 row with additions + deletions.

2. **Write the intent statement.** Find the PR's worktree with `git worktree list`, open a new session there, and type:

   ```text
   Draft an intent statement for PR #<n> with these fields: Goal, Issue, In scope,
   Out of scope (on purpose), Context that sets the bar, Decisions already made,
   Verified with, Look hardest at. Read the issue, the diff (gh pr diff <n>) and
   the tests. If you aren't sure about Goal or Context, leave them as questions
   for me. Show me the draft; don't change the PR yet.
   ```

   Rewrite **Goal** and **Context that sets the bar** yourself. Those are the lines that do the work. For the practice project, the context is "local single-user CLI; the data file belongs to the person running it; no network". Copy the issue's "Out of scope" list into the statement too, because reviewers can't respect a boundary they can't see. Then:

   ```text
   Put this intent statement at the top of the PR body and keep the rest of the
   body. Then re-fetch the PR with gh pr view <n> and confirm the text is there.
   ```

   **Checkpoint:** `gh pr view <n>` shows the Intent section, and the agent re-fetched the PR instead of trusting the edit command.

3. **Run the fresh-context reviewer.** Open a **new** session in the same worktree. Don't reuse the writer's session or the one from step 2. The same vendor as the writer is fine here.

   ```text
   You are reviewing PR #<n> in a fresh session. You did not write this code.
   Read the intent statement at the top of the PR body (gh pr view <n>) and judge
   every finding against its goal, scope and context. Read the diff
   (gh pr diff <n>) and the code around it; read more code to answer your own
   questions.
   Report only: correctness bugs against the goal, security or data exposure,
   serious performance regressions, duplication this PR introduces, behavior no
   test would catch if reverted, deviations from AGENTS.md. No style, no renames.
   For each finding: priority (P0 blocks merge, P1 fix in this PR, P2 follow-up),
   file:line, a failing scenario, a one-line fix idea.
   If you're unsure whether it's real or in scope, list it under "Questions for
   the human". At most five P2 findings. Don't edit files. An empty review is a
   valid result.
   Post the review as one PR comment starting with
   "Review 1 (fresh context, <agent name>)".
   ```

   **Checkpoint:** `gh pr view <n> --comments` shows the review. Every finding has a file:line and a concrete scenario. Treat findings without a scenario as weak.

4. **Run the second-vendor reviewer.** Open a new session with the other vendor's agent in the same worktree. Paste the same prompt, but label the comment `Review 2 (other vendor, <agent name>)`.

   **Checkpoint:** a second review comment exists. In your log's Notes column, record how many findings appear in both reviews and how many appear in only one.

5. **Build the ledger.** Open a new session (a triage session) and type:

   ```text
   Act as triage lead for PR #<n>. Don't change code yet.
   1. Collect every finding: both review comments plus every unresolved review
      thread from bots or humans. Fetch review threads through the GitHub GraphQL
      API and paginate until hasNextPage is false. Tell me the total count.
   2. Read each finding in full before deciding.
   3. Build a ledger table: ID, Source, Finding, Verdict (FIX_NOW /
      DEFER_TO_ISSUE / DISCARD), Reason tied to the intent statement.
      Always-fix: security or data exposure, serious performance regressions,
      duplication introduced by this PR, missing behavioral coverage, deviations
      from documented architecture. Never DISCARD a security finding.
   4. Mark as ASK anything you're unsure about, and any fix that would add a
      feature or a dependency or noticeably grow the diff.
   Show me the ledger and the ASK list, then stop.
   ```

   Decide each ASK yourself and tell the agent your verdict and your reason.

   **Checkpoint:** every finding has exactly one verdict. No security finding is DISCARD. Your log has round 1's high-priority count (P0 + P1 across both reviews).

6. **Fix round 1 in one batch.**

   ```text
   Apply every FIX_NOW item in one change. Run the tests. Push once.
   Create ONE follow-up issue (gh issue create) listing every DEFER_TO_ISSUE item
   with its reason and a link to this PR. Post the ledger as a PR comment that
   includes the issue link. For each review thread: read it, reply with its
   verdict and reason, then resolve it.
   ```

   **Checkpoint:** `python -m unittest` passes in the practice project folder (or your repo's test command passes). `gh issue list` shows the follow-up issue. `gh pr view <n> --json additions,deletions` gives the round 1 diff size for your log.

7. **Run round 2.** Repeat steps 3, 4 and 5, adding these lines to both reviewer prompts:

   ```text
   A round 1 ledger is posted on this PR. Don't re-raise items already decided
   there unless you have new evidence. If you do, say what is new.
   ```

   Label each round 2 finding: *new problem in the original change*, or *derivative* (a consequence of a round 1 fix, a parked item raised again, a product question, a hypothetical beyond the context, or a contradiction between reviewers).

   **Checkpoint:** your log has round 2's high-priority count, and every finding has a label.

8. **Close by decision.** If high-priority findings didn't fall, or most round 2 findings are derivative, stop, even if findings remain:

   ```text
   Stop the fix loop. Give me a demanding go/no-go assessment of PR #<n> against
   its intent statement: what would break for a user if we merged now? Then
   classify every open finding in one final ledger, reply to and resolve every
   thread with its reason, add deferrals to the existing follow-up issue, and
   confirm no security finding was discarded. Don't push code.
   ```

   If high-priority findings did fall and real FIX_NOW items remain, do one more batch (step 6) first, then close the same way.

   Then **you** decide. Merge the PR, or post a comment explaining why you didn't.

   **Checkpoint:** a final ledger comment exists, no threads are unresolved (see the command below), and your decision is recorded on the PR.

## Done when

- [ ] The PR body starts with an intent statement: `gh pr view <n>`.
- [ ] Two review comments from two different reviewers exist: `gh pr view <n> --comments`.
- [ ] Each round has a ledger in which every finding has one verdict and a reason.
- [ ] No security finding has the verdict DISCARD.
- [ ] All deferred findings live in one follow-up issue: `gh issue list`.
- [ ] Tests pass: `python -m unittest` in the practice project folder, or your repo's test command.
- [ ] No review thread is unresolved. This command prints nothing:

  ```bash
  gh api graphql --paginate -f owner=<owner> -f repo=<repo> -F number=<n> -f query='
  query($owner: String!, $repo: String!, $number: Int!, $endCursor: String) {
    repository(owner: $owner, name: $repo) {
      pullRequest(number: $number) {
        reviewThreads(first: 100, after: $endCursor) {
          pageInfo { hasNextPage endCursor }
          nodes { isResolved path }
        }
      }
    }
  }' --jq '.data.repository.pullRequest.reviewThreads.nodes[] | select(.isResolved == false) | .path'
  ```

- [ ] Your log shows high-priority findings and diff size for every round.
- [ ] You, not an agent, merged the PR or wrote down why you didn't.

## Reflect

- Which finding would you least want to reach production? Would the other reviewer have caught it?
- How much did the diff grow from round 0 to your last round? How much of that growth served the goal, and how much came from reviewers?
- Which ASK was hardest to decide? What missing line in the intent statement would have decided it for you?
- Where did you stop, and which signal told you to stop?
- Which parts of the diff did you read line by line, and why those parts?

## Stretch

- **Specialist reviewer.** Add a subagent with a single question. For C2, for example: "Can a v1 file be lost or silently rewritten during migration?" Trigger it only when `shelf/store.py` changes, and have it report in the ledger format.
- **Rules in the repository.** Encode your review rules so a PR bot applies them on every PR: a `## Code Review Rules` section in `AGENTS.md` for Codex's GitHub reviewer, or a `REVIEW.md` for Claude Code's managed review. See the [tools reference](../reference/tools.md).
- **Prompt request.** Write S7 ("Make shelf more useful for book clubs") as a prompt request: the intent, the prompts you would use and how you would verify the result. Hand it to a fresh session, then compare the PR it produces with one built from the one-line issue.
