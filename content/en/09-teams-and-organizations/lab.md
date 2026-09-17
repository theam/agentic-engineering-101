---
title: "Lab 9 — Write your team's working agreement"
module: 9
kind: lab
minutes: 60
level: advanced
last_reviewed: 2026-09-17
---

# Lab 9 — Write your team's working agreement

## Goal

Write, with an agent, a one-page working agreement for how a team uses coding agents: board columns and gates, review policy, security rules and disclosure. Then turn one of its rules into a deterministic check, have a fresh session attack the document, and open a pull request with it.

The agreement is the "build tools" lever from [module 9](README.md) in its simplest form. It's a shared, reviewed file that agents and people both read.

## Before you start

- You have done labs 5–7, or you are comfortable with issues, worktrees and review loops.
- You have a repository to work in:
  - **Practice project:** your copy of [`practice/shelf`](../../../practice/shelf/). Most answers in the inventory will be "none yet". That's fine: the agreement defines them.
  - **On your own repo:** a repository your team really uses. You'll find out things you didn't know (a bot on a personal token is a common one). Agree with your team lead before you open the PR.
- The GitHub CLI (`gh`) is authenticated if your repository is on GitHub.
- Optional but valuable: one teammate who can give you 10 minutes at the end.

## Steps

1. **Inventory how things work today.** Open a session at the root of the repository and type:

   ```text
   Let's discuss before writing anything. I want a one-page working agreement
   for how our team uses coding agents in this repository.
   First, inventory how things work today, as facts with evidence (file paths,
   config files, command output). Cover: who can merge and whether the default
   branch is protected, which bots or automations exist and which credentials
   they use, where agents run, which instruction files exist, and how PRs get
   reviewed. Mark anything you could not verify as "unknown".
   Do not propose changes yet.
   ```

   **Checkpoint:** every item has a source (a path, a command and its output) or says "unknown". If the agent states something without evidence, reply "Show me where you found that" before moving on. On your own repo, check the "unknown" items with a teammate.

2. **Map the lethal trifecta.** In the same session:

   ```text
   For every agent or automation in the inventory, plus two we plan to add
   (a PR reviewer and an issue-triage agent), build a table:
   agent | private data? | untrusted content? | external communication? | identity and permissions
   For any row with three "yes", propose the smallest change that removes one leg.
   ```

   **Checkpoint:** no row has three "yes" without a mitigation next to it. The issue-triage agent should come out with untrusted content marked "yes". If it doesn't, ask the agent who can write issue text in your repository.

3. **Choose the board and the gates.** Ask for options, not a document:

   ```text
   Give me two or three options for our board columns and gates. Constraints:
   agents act only in a planning column and an implementation column; humans
   move cards, accept plans and merge. For each option list the columns, who
   acts in each, the exit gate, and how we tell "PR still in CI" apart from
   "PR ready for a human". Recommend one. Don't write the agreement yet.
   ```

   **Checkpoint:** you picked an option and can say why in one sentence. If none fits, say what's wrong ("we have no separate Ready column; plans are accepted in the issue thread") and ask again.

4. **Draft the agreement.** Paste this skeleton into the session:

   ```markdown
   # Working agreement: agentic engineering
   Last reviewed: YYYY-MM-DD

   ## 1. Board and gates
   | Column | Who acts | Leaves when |
   - Agents act only in:
   - A human is assigned before an agent starts.
   - "Ready for a human" means:

   ## 2. Review policy
   - Every PR gets: (fresh-context reviewer, second model or vendor)
   - Always-fix categories:
   - Review loops close by decision when:
   - Humans read line by line:

   ## 3. Security rules
   - Untrusted input:
   - Agent identities and permissions: (table from step 2, or a link to it)
   - Secrets:
   - Production-privileged commands:

   ## 4. Disclosure and signatures
   - Commits:
   - Agent posts:
   - Anything leaving the team:

   ## 5. Asking for decisions

   ## 6. Learning and architecture

   ## 7. Changing this agreement
   ```

   Then type:

   ```text
   Write docs/agentic-working-agreement.md using this skeleton and the decisions
   from this conversation. One page: at most 100 lines. Where we haven't decided
   something, write "OPEN:" followed by the question. Do not invent rules
   we didn't discuss.
   ```

   **Checkpoint:** read the whole file. It takes three minutes. Every rule should be something you actually decided. Anything else should be an `OPEN:` line. Correct in short sentences ("agents never merge, not 'rarely'"). Don't edit the file by hand.

5. **Make one rule deterministic.**

   ```text
   Pick the rule in the agreement that is easiest to check mechanically and
   most likely to be forgotten. Implement the smallest deterministic check for
   it: a script, a hook or a CI step. Show me the check failing on a bad example
   and passing on a good one. Then add one line to the agreement that says
   where the check lives.
   ```

   Good candidates: agent commits carry an `Assisted-by:` trailer; agents can't read `.env` files (a permission rule or a [hook](https://code.claude.com/docs/en/hooks)); every PR description has an "AI assistance" section.

   **Checkpoint:** you saw the failing output and the passing output with your own eyes, not just the agent saying so.

6. **Attack it from a fresh session.** Close the session or open a new one. The reviewer must not remember writing the document. Type:

   ```text
   Read docs/agentic-working-agreement.md as a skeptical senior engineer who
   just joined this team. Do not rewrite it. Report:
   1. the three rules most likely to be ignored in practice, and why;
   2. any contradictions between rules;
   3. one gap an attacker could use, given that agents read issues and PRs.
   For each finding give a verdict, FIX_NOW, DEFER_TO_ISSUE or DISCARD, with
   one line of reasoning.
   ```

   **Checkpoint:** you have a small ledger with a verdict per finding. Apply the `FIX_NOW` items. For each `DEFER_TO_ISSUE`, add an `OPEN:` line or file an issue. Security gaps are never discarded.

7. **Get a human read, then open the pull request.** Show the file to a teammate, or reread it tomorrow morning if you work alone, and ask two questions: "Would you follow this tomorrow?" and "Which rule would you break first?" Adjust. Then ask the agent to draft the PR description:

   ```text
   Draft a pull request description for this change: what the agreement covers,
   the deterministic check and how to run it, the OPEN questions, and an
   "AI assistance" section that says what the agent did and what I decided.
   Do not create the PR; give me the text.
   ```

   Commit, push the branch and create the PR yourself with `gh pr create`.

   **Checkpoint:** `gh pr view` shows the PR, and its description has the AI assistance section.

## Done when

- [ ] `docs/agentic-working-agreement.md` exists and `wc -l docs/agentic-working-agreement.md` prints 100 or less.
- [ ] `grep -c "^## " docs/agentic-working-agreement.md` prints at least 5 (board, review, security, disclosure and at least one more).
- [ ] The trifecta table has no agent with all three legs and no mitigation.
- [ ] One rule has a deterministic check, and you watched it fail on a bad example and pass on a good one.
- [ ] The fresh-session review is triaged, and its `FIX_NOW` items are applied.
- [ ] `gh pr view` shows the PR with an "AI assistance" section.
- [ ] Practice project only: if you touched code, `python -m unittest` still passes from the `shelf` directory.

## Reflect

- Which rule will you break first under deadline pressure? What would make breaking it hard instead of just discouraged?
- Which rules are still prose that should become guards?
- What did the inventory reveal that you didn't know?
- Which `OPEN:` question needs a person with authority, and how will you ask it well: what you need, why now, and the degraded path?
- If a regulated client asked for this agreement, what would they find missing?

## Stretch

- Run a 30-minute session with your team. Walk through the agreement, ask each person to name one rule they disagree with, and record each decision in the document or in your knowledge base.
- Link the agreement from `AGENTS.md` with one line, so agents find it on demand. Link it instead of pasting it in, so your always-loaded context stays small.
- Share a sanitized version, or the one rule that turned out most useful, as a practice for this guide: see [CONTRIBUTING](../../../CONTRIBUTING.md).
