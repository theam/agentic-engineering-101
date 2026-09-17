---
title: "Lab 8 — Your cost per merged PR and your top token sinks"
module: 8
kind: lab
minutes: 60
level: advanced
last_reviewed: 2026-09-17
---

# Lab 8 — Your cost per merged PR and your top token sinks

## Goal

Measure one real week of agentic work in the units from [the lesson](README.md): **cost per merged PR**, **rework rate** and **human minutes per PR**. Then find your **top three token sinks**, each backed by a number, and choose one change for each that you can measure next week.

## Before you start

- **A week of real agent work.** Your own repository gives the most useful numbers. On the [practice project](../../../practice/shelf/), use the week you did Labs 5 to 7. The numbers will be small, but the method is the same.
- **Your baseline** from [Lab 1](../01-from-chatbot-to-system/lab.md).
- **Access to what you pay for**: plan usage screens, invoices, the API console for any keys, and bills for review services.
- `gh` signed in (`gh auth status`).
- **A place to record results** in your knowledge base from [Lab 4](../04-context-is-infrastructure/lab.md), for example `kb/metrics/economics-<YYYY-MM-DD>.md`.

> [!WARNING]
> Spend numbers are private. If your knowledge base lives in a public repository, keep this file somewhere else.

## Steps

1. **Fix the window.** Pick seven days that ended at least a week ago, so every PR merged in them has had its 7 days to need rework. Create the results file and write the start and end dates (`START` and `END`, formatted `YYYY-MM-DD`) at the top. In a workshop, or if you can't wait, use the seven days ending today and mark the rework rate as provisional.

   **Checkpoint:** the file exists with the date range.

2. **Count merged PRs (N).**

   ```bash
   gh pr list --state merged --author @me --search "merged:START..END" --limit 200 \
     --json number,title,additions,deletions,mergedAt
   ```

   `gh pr list` returns only 30 results by default, so `--limit` matters. It's the same truncation trap as in module 7. If your agents open PRs under a different account, change `--author`. Save the JSON, and add `--jq length` to get the count.

   **Checkpoint:** N is recorded, and the list is saved.

3. **Classify rework (R).** Give the saved list to a fresh session:

   ```text
   Here are the PRs I merged between START and END (JSON below). A PR counts as
   reworked if a later PR fixed or reverted it within 7 days of its merge.
   For each PR, look for such a follow-up among the PRs merged since START
   (gh pr list --state merged --search "merged:>=START"), and read PR bodies
   and linked issues with gh pr view when a title is ambiguous. Mark each PR
   reworked or not, give the follow-up PR as evidence for every reworked one,
   and output a table and the count.
   ```

   Cross-check reverts with a search:

   ```bash
   gh pr list --state merged --search "revert in:title merged:>=START" --limit 200 --json number,title
   ```

   **Checkpoint:** R = PRs from the window that needed a follow-up fix or revert within 7 days, with the follow-up PR as evidence on every one. You checked at least two classifications yourself.

4. **Collect AI spend (S) for the window.**
   - Subscriptions: monthly fee × 12 ÷ 52 gives the weekly share of each one.
   - Extra usage beyond your plans, API keys used by bots and CI, and per-review services: take the amounts for the window from each billing page.
   - Plan headroom: note the share of your limits you used, or how many times you hit a limit. A flat fee hides this.

   In Claude Code, `/usage` shows plan usage and a breakdown by skills, subagents, plugins and MCP servers ([costs documentation](https://code.claude.com/docs/en/costs)). For other tools, see the [tools reference](../reference/tools.md) or the vendor's usage page.

   **Checkpoint:** a table of spend lines, each with its source, and the total S.

5. **Estimate human minutes (M) and thrown-away work (U).** Pick five merged PRs, mixing small and large. For each, estimate the minutes you spent reading, deciding and unblocking, rounded to 5. Use your calendar, notifications and memory. Average the five to get M. Then count the PRs you closed without merging:

   ```bash
   gh pr list --state closed --author @me --search "is:unmerged closed:START..END" --limit 200 --json number,title
   ```

   **Checkpoint:** M and U are recorded.

6. **Compute the unit numbers.** Fill in this table in your results file:

   ```markdown
   | Metric | Formula | Value |
   | --- | --- | --- |
   | Cost per merged PR | S ÷ N | |
   | Rework rate | R ÷ N | |
   | Cost per net merged PR | S ÷ (N − R) | |
   | Human minutes per merged PR | M | |
   | Human minutes for the week | M × N | |
   | PRs closed without merging | U | |
   ```

   The lesson has a [worked example](README.md#a-worked-example) if you want to check your arithmetic.

   **Checkpoint:** every value is filled in. Next to the table, write one sentence comparing these numbers to your Lab 1 baseline.

7. **Gather evidence of token sinks.**
   - **Review rounds.** For your five largest merged PRs, run `gh pr view <n> --json reviews --jq '.reviews | length'`.
   - **Always-loaded context.** Run `wc -l AGENTS.md CLAUDE.md`, or the equivalent for your instruction files. Then check how much context a new session uses before your first message (in Claude Code, `/context`).
   - **Session habits.** In Claude Code, `/insights` writes a report about friction in your recent sessions ([costs documentation](https://code.claude.com/docs/en/costs)). Also note any session you kept open all day.

   Then ask a fresh session:

   ```text
   Help me find my top 3 token sinks for the week. Evidence:
   - merged PRs: N, reworked PRs: R, closed without merging: U
   - review rounds on my 5 largest PRs: <numbers>
   - instruction files: <wc -l output>; context used before my first message: <value>
   - usage breakdown and flags: <paste>
   - other observations: <for example "one session stayed open all Tuesday">
   Consider these common sinks: review loops chasing scope creep, bloated
   always-loaded context, too many tools or skills, re-deriving known facts, long
   sessions, verbose tool output, a model doing what code should, background usage,
   thrown-away work.
   Rank the top 3 by likely cost. For each give: the evidence (a number), one
   change, and the metric that will show next week whether the change worked.
   Don't suggest changes that move work from agents to me.
   ```

   **Checkpoint:** three sinks, each with a number, a change and a metric. Reject any sink whose only evidence is an adjective ("sessions feel long").

8. **Record and commit.** Add the three sinks and a short "next week I will…" paragraph to the results file. Commit it to your knowledge base.

   **Checkpoint:** `git log -1 --stat` shows the file.

## Done when

- [ ] N, R, U, S and M are recorded, each with its source (a command or a billing page).
- [ ] Cost per merged PR, rework rate, cost per net merged PR and human minutes are computed, with the formulas shown.
- [ ] Three token sinks are listed, each backed by a number.
- [ ] Each sink has one change and a metric to check next week.
- [ ] The results are compared with your Lab 1 baseline.
- [ ] The file is committed to your knowledge base: `git log -1 --stat`.
- [ ] No spend numbers were committed to a public repository.

## Reflect

- Which dominated your week, AI spend or human minutes? Did that surprise you?
- Where would you gladly spend more tokens to save minutes of your own?
- Which of your numbers do you trust least, and why?
- Did any of your work look productive by lines of code but not by merged, non-rework PRs?

## Stretch

- **Model A/B.** In the practice project, implement S3 (`shelf stats`) twice, in two worktrees, with the same prompt: once with the strongest model and once with a cheaper one. Compare whether tests pass, how many corrections each needed, what the Lab 7 reviewer finds, tokens used and wall time. Look for gamed work, such as edited tests or hardcoded output, and check the issue's trickiest criterion: tests that don't depend on today's date.
- **Filter test output.** Add a hook that trims test output down to failures (the [costs documentation](https://code.claude.com/docs/en/costs) has an example). Compare the context used on a test-heavy task before and after.
- **Team view.** Run the same formulas for each person on your team, then discuss the unit numbers together rather than the bills.
