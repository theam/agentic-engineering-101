---
title: "Lab 10 — Capstone: four weeks on your own code"
module: 10
kind: lab
minutes: 90
level: intermediate
last_reviewed: 2026-09-17
---

# Lab 10 — Capstone: four weeks on your own code

## Goal

Plan, run and close the 30-day plan from [module 10](README.md). At the end you'll have a plan file, four weekly check-ins, a capstone checklist backed by evidence, a retrospective that compares your practice with your module 01 baseline, and one practice shared back.

The 90 minutes in the front matter are the lab's own time: about 30 minutes to set up and about 60 for the final measurement and retrospective. The weekly check-ins take 15 minutes each. The practice itself happens during your normal work.

## Before you start

- **Your baseline** from [Lab 1](../01-from-chatbot-to-system/lab.md). If you don't have one, measure one working week first, before week 1.
- **A repository:**
  - **On your own repo** (recommended): one you'll work in every day for the month. For the first weeks, pick one where a bad PR is an inconvenience, not an incident.
  - **Practice project:** if you can't use real code yet, compress the plan into four 1–2 hour sessions on your copy of [`practice/shelf`](../../../practice/shelf/). Session 1 is lab 4, session 2 is lab 3, session 3 is lab 6 (three tracks: S4 with S5, C1 and C2, including the conflict between C1 and C2), and session 4 is labs 7 and 8. The numbers will be tiny. The goal is the habit and the templates.
- The GitHub CLI (`gh`) authenticated, and a place for your knowledge base (`kb/`) that your agent can read and that you commit.
- Optional: access to a second model or vendor for week 4, and a buddy doing the same plan.

## Steps

1. **Draft the plan file.** Open a session where your knowledge base lives and paste this skeleton:

   ```markdown
   # 30-day plan — <repository>, <start date> to <end date>

   ## Baseline (from lab 1)
   | Metric | Value | How I measured it |
   | --- | --- | --- |

   ## Week 1 — Context
   Goal:
   Deliverables (each with how to verify it):
   Metric:
   Risks in this repository:

   ## Week 2 — Verification and guards
   Goal:
   Deliverables (each with how to verify it):
   Metric:
   Risks in this repository:

   ## Week 3 — Parallel tracks
   Goal:
   Deliverables (each with how to verify it):
   Metric:
   Risks in this repository:

   ## Week 4 — Review and economics
   Goal:
   Deliverables (each with how to verify it):
   Metric:
   Risks in this repository:

   ## Check-ins
   Day and time:
   Buddy:
   ```

   Then type:

   ```text
   Read my baseline notes at <path>. Then read this repository and draft
   kb/30-day-plan.md from the skeleton above. The four weeks are: context,
   verification and guards, parallel tracks, review and economics.
   For each week, list deliverables that can be verified with a command or a
   file, and the risks specific to this repository (slow or flaky tests,
   missing docs, shared databases, ports). Ask me about anything you can't
   find out from the code. Don't invent baseline numbers.
   ```

   **Checkpoint:** every deliverable says how to verify it, and every baseline row says how it was measured. If a baseline row has no method, fix it now. You'll need the same method in week 4.

2. **Set up the check-ins.** Create `kb/checkins/`, put a recurring 15-minute block in your calendar, and save the check-in template from the [module 10 lesson](README.md#the-weekly-check-in) as `kb/checkins/week-1.md`.

   **Checkpoint:** `ls kb/checkins/` shows `week-1.md`, and the event is in your calendar.

3. **Run the four weeks, and verify each one against the checklist.** Work through the plan during your normal work. At the end of each week, before the check-in, type:

   ```text
   Verify the week N items of the capstone checklist below. For each item,
   run the command or open the file and show me the evidence. Mark an item
   done only if the evidence supports it. List what's missing, without fixing it.
   ```

   Paste the checklist for that week along with the prompt.

   **Checkpoint:** each check-in file links to the evidence for the items you marked done.

   ### The capstone checklist

   **Week 1 — Context**

   - [ ] `AGENTS.md` exists. If you use Claude Code, `grep -n "@AGENTS.md" CLAUDE.md` finds the import.
   - [ ] `wc -l kb/ACTIVE.md` prints 100 or less, with one row per live track.
   - [ ] At least three decision records exist for decisions made this week.
   - [ ] A fresh session answered "what are we working on, and why?" correctly, and its answer is saved in the check-in.
   - [ ] `git status` in the knowledge base is clean at the end of each session.

   **Week 2 — Verification and guards**

   - [ ] One gate command is documented in `AGENTS.md` and passes on the default branch.
   - [ ] A guard blocked a session: you broke a test on purpose, the session couldn't finish, and you saved the output.
   - [ ] Permission tiers are configured, and reading secrets and force-pushing are denied.
   - [ ] At least one test fixture varies the way production data varies.

   **Week 3 — Parallel tracks**

   - [ ] 5+ sessions ran in parallel on at least two days, with session IDs recorded in the check-in. Or you stopped at a lower level because module 06's signals didn't hold, and the check-in says which signal and what you fixed.
   - [ ] Every live track has a row in `ACTIVE.md` with its state and next gate, and shipped tracks were removed.
   - [ ] `git worktree list` at the end of the week shows only live tracks.
   - [ ] A kickoff prompt template is saved where the next session can find it.
   - [ ] Module 09's security baseline holds: no permission-bypass mode outside a sandbox, and no team automation on a personal token.

   **Week 4 — Review and economics**

   - [ ] At least three PRs have an intent statement, a fresh-context review and a triage ledger. `gh pr view <number> --comments` shows a reply on every review thread.
   - [ ] Cost per merged PR is computed, with the formula and data sources written down.
   - [ ] Each of your top three token sinks has one change applied.

4. **Take the final measurement.** Use the same metrics, method and window length as the baseline: PRs merged, cycle time, human minutes per PR, cost per merged PR and rework, next to the session and usage numbers. Rework counts merged PRs that needed a follow-up fix or revert within 7 days, so fill in that row a week after week 4 ends. Type:

   ```text
   Create kb/retrospective.md with a before/after table:
   Metric | Baseline | Week 4 | Change | Source | Confounders.
   Use the same method as the baseline in kb/30-day-plan.md. For merged PRs run
   gh pr list --state merged --author "@me" --search "merged:>=YYYY-MM-DD"
   and show me the output. Take every number from a source you can show me.
   Leave a cell empty when there is no source. Do not estimate.
   ```

   Fill in by hand what the agent can't reach, such as plan usage from your account page and your waiting-time tally.

   **Checkpoint:** every filled cell has a source, and the Confounders column isn't empty.

5. **Write the retrospective.** Restructure `kb/retrospective.md` with this template, and move the table from step 4 into its place:

   ```markdown
   # 30-day retrospective — <repository>, <start> to <end>

   ## Context
   - Repository (kind, size, language) and team size:
   - Agents and plans used:
   - What else happened this month that affects the numbers:

   ## Before and after
   (the table from step 4)

   ## What the PRs changed
   One line per important PR: what it changed for users or for the team.

   ## Deliverables
   Link each weekly deliverable. Mark any you dropped, and why.

   ## Keep

   ## Change

   ## Drop

   ## Surprises

   ## Promotions
   Corrections that became a memory entry, a rule, a skill or a guard.

   ## Costs
   Money, attention, sleep.

   ## Next 30 days
   Three commitments, each with a metric.
   1.
   2.
   3.

   ## One practice to share
   ```

   Let the agent pre-fill **Context**, **Deliverables** and **Promotions** from your check-ins. Write **Keep**, **Change**, **Drop**, **Surprises**, **Costs** and **Next 30 days** yourself. That's where the judgment is.

   **Checkpoint:** Keep, Change and Drop each have at least one item in your own words.

6. **Challenge your conclusions in a fresh session.** Open a new session with no memory of the month and type:

   ```text
   Read kb/retrospective.md and kb/30-day-plan.md as a skeptical reviewer.
   Which conclusions don't follow from the numbers? Which changes could be
   explained by the confounders listed, or by a different mix of tasks?
   Don't rewrite anything. List at most five points.
   ```

   **Checkpoint:** you qualified or changed at least one conclusion, or wrote down why each point doesn't apply.

7. **Share one practice back.** Type:

   ```text
   Draft a "Share your practice" submission from kb/retrospective.md with:
   context, what I did (the prompt, rule or guard, verbatim), evidence marked
   as indicative, and what didn't work. Remove client names, internal URLs,
   secrets and people's names. Give me the text; don't submit anything.
   ```

   Read the draft for anything confidential, then submit it yourself through the issue form described in [CONTRIBUTING](../../../CONTRIBUTING.md).

   **Checkpoint:** the retrospective links to the issue you opened.

## Done when

- [ ] `kb/30-day-plan.md` exists, with a baseline table that states each method and four weeks of goals.
- [ ] `ls kb/checkins/` shows four check-in files.
- [ ] Every capstone checklist item is checked with evidence, or marked as dropped with a reason.
- [ ] `kb/retrospective.md` has the before/after table, with a source for every filled cell.
- [ ] You wrote Keep, Change and Drop yourself.
- [ ] The fresh-session challenge is done, and at least one conclusion was revisited.
- [ ] One practice is shared, and the retrospective links to it.
- [ ] `git status` in the knowledge base is clean: everything is committed and pushed.

## Reflect

- Which layer made the biggest difference, and which the smallest? Is that what you expected on day 1?
- Where did your review capacity top out, and what limited it?
- Which number surprised you? Which confounder could explain it?
- What would you tell a teammate starting this plan next Monday?
- Which of your practices should become a team rule (see [lab 9](../09-teams-and-organizations/lab.md))?

## Stretch

- Measure again in 30 days without following the plan. Did the numbers hold?
- Run the plan alongside a teammate on a shared repository and compare your retrospectives.
- Propose your most useful practice as a change to your team's working agreement from lab 9.
