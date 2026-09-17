---
title: "Lab 1 — Baseline yourself"
module: 1
kind: lab
minutes: 60
level: foundation
last_reviewed: 2026-09-17
---

# Lab 1 — Baseline yourself

## Goal

Measure one normal week of how you work with coding agents today, write down your starting point, and set one target. You will need this baseline in [module 10](../10-your-30-day-plan/README.md), when you compare your own before and after.

Why bother: in [METR's 2025 study](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/), experienced developers believed AI had made them 20% faster when it had made them 19% slower. Your impression of your own speed is not data. A week of simple logging is.

This lab takes about an hour of active time, spread over a week: 15 minutes to set up, two minutes a few times a day to log, and about 40 minutes at the end to compute and write. The rework count needs one more five-minute check a week later.

## Before you start

- **Pick a normal week.** Not a holiday week, not an incident week, not the week you change tools. Measure how you work *now*, before applying anything from later modules.
- **Know where your usage shows up.** Each agent reports plan usage or spend in its own way, through a usage view in the tool or the vendor's account page. The [tools reference](../reference/tools.md) lists where to look for common agents; for Claude Code, see [managing costs](https://code.claude.com/docs/en/costs).
- **Check the GitHub CLI** with `gh auth status`. You'll count pull requests with it.
- **Choose a private place for your notes**, outside any work repository. Your baseline may include spend, and it is yours, not a performance report.

**With the practice project:** if you don't write much code in a normal week, use [shelf](../../../practice/shelf/) as your "work". Take issues S3 to S6 from the [issue list](../../../practice/issues/en.md), one or two per day, working the way you do today, and log exactly as below. Do it in a second copy of the project, for example `~/code/shelf-baseline` published as its own repository, because labs 2, 3 and 6 implement those issues in your main copy. The numbers will be less realistic, but you'll still see your habits.

**On your own repo:** this is the better option. Log your real work on your real repositories.

## Steps

### 1. Write your guesses first (5 minutes)

Before measuring anything, create `baseline.md` and write your honest guesses:

```markdown
## Guesses (written before measuring)
- Pull requests I merge in a typical week:
- Agent sessions I run at the same time, most of the day:
- Maximum sessions at the same time:
- Minutes per day I spend waiting for or watching an agent:
- Times per day I check something the agent could have checked itself:
- Times per day I re-explain project context to an agent:
```

**Checkpoint:** six guesses written down, dated.

### 2. Set up a log (10 minutes)

Create `baseline-log.csv` next to it, with this header:

```text
date,time,repo,task,kind,parallel,waited_min,i_verified,re_explained
```

Add one row each time you start an agent session:

| Column | What to write |
|---|---|
| `kind` | `plan`, `implement`, `review`, `question` or `other` |
| `parallel` | How many other agent sessions were active when you started this one |
| `waited_min` | Minutes you spent watching or waiting for this session, instead of doing something else (estimate when the session ends) |
| `i_verified` | How many times you ran tests or checked output the agent could have checked itself |
| `re_explained` | How many times you explained project context the agent should already have |

Example row:

```text
2026-09-21,10:40,billing-api,fix rounding bug,implement,1,12,2,1
```

> [!TIP]
> Keep the log open in a split pane, or dictate rows at the end of each session. If you forget a session, many tools let you list past sessions (in Claude Code, `/resume` shows them), which helps you fill gaps at the end of the day. A roughly right log beats a perfect log you abandon on Wednesday.

**Checkpoint:** by the end of day one, the log has a row for every session you remember starting.

### 3. Record your plan usage and spend at the start and end of the week (5 minutes total)

On day one and on the last day, write down for each tool: the plan and its monthly fee, the usage or spend shown, any extra usage or API spend, and whether you hit a limit during the week (and when).

**Checkpoint:** two readings per tool, or a note saying the tool doesn't show usage, and a fee or spend figure for every tool you pay for.

### 4. Count your pull requests and your minutes at the end of the week (15 minutes)

In each repository you worked on, save the merged pull requests with their timestamps next to your notes, and list the open ones:

```bash
gh pr list --author "@me" --state merged --search "merged:>=YYYY-MM-DD" --limit 100 \
  --json number,title,createdAt,mergedAt > ~/baseline/merged-prs-REPO.json
gh pr list --author "@me" --state open
```

Replace `YYYY-MM-DD` with the first day of your week, `REPO` with the repository's name, and `~/baseline` with the private folder where you keep `baseline.md`. If you work across many repositories, GitHub's web search accepts the same filter: `is:pr author:@me is:merged merged:>=YYYY-MM-DD`. The script in step 5 turns the saved files into a count and a median **cycle time**, from opening a pull request to merging it. Keep that start event: module 10 compares against it.

Estimate **human minutes per merged pull request**. Pick five merged pull requests, mixing small and large. For each one, estimate the minutes you spent reading, deciding and unblocking, rounded to 5, using your calendar, notifications and memory. Average the five.

Also count **rework**: merged pull requests from this week that needed a follow-up fix or a revert within 7 days of merging. Pull requests merged late in the week haven't had their 7 days yet, so put a reminder in your calendar and check this number again a week after the week ends.

**Checkpoint:** four numbers: merged, still open, human minutes per merged pull request, and rework, with a reminder to re-check rework.

### 5. Let the agent write the arithmetic, not do it (10 minutes)

Don't paste your log into a chat and ask for totals. A language model can re-type a number wrong and still sound confident. Ask for a script, then run it yourself:

❌ **Weak prompt**

```text
here's my log, give me the averages
```

✅ **Better prompt**

```text
Write a Python script, summarize.py, standard library only, that reads
baseline-log.csv (columns: date,time,repo,task,kind,parallel,waited_min,
i_verified,re_explained) and prints: number of sessions, sessions per day,
maximum and median of (parallel + 1), total and per-day waited_min,
total i_verified, total re_explained, and a count of sessions by kind.
It also reads every merged-prs-*.json file in the folder (a JSON list of
objects with createdAt and mergedAt) and prints the number of merged pull
requests and the median hours from createdAt to mergedAt.
Print a warning for any row or entry it can't parse instead of skipping it
silently. Don't read or print anything else. I'll run it myself.
```

Run it:

```bash
python summarize.py baseline-log.csv
```

Spot-check one number by hand, for example the number of sessions on one day. If it doesn't match, fix the script, not the number.

**Checkpoint:** the script runs, reports no unexplained warnings, and one number matches your manual check.

### 6. Write the baseline (10 minutes)

Add this to `baseline.md`, filling every row or writing "no data":

```markdown
## Measured: week of YYYY-MM-DD
| Metric | Guess | Measured | Source |
|---|---|---|---|
| Merged pull requests | | | summarize.py |
| Cycle time, opened → merged (median hours) | — | | summarize.py |
| Human minutes per merged pull request (sample of five) | — | | my estimate |
| Cost per merged pull request (week's AI spend ÷ merged) | — | | step 3 fees and spend |
| Rework (merged PRs that needed a follow-up fix or revert within 7 days) | — | | gh pr list + memory, re-checked a week later |
| Sessions per day | — | | summarize.py |
| Typical sessions at the same time (median) | | | summarize.py |
| Maximum sessions at the same time | | | summarize.py |
| Minutes per day waiting for or watching an agent | | | summarize.py |
| Times I verified what the agent could have verified | | | summarize.py |
| Times I re-explained context | | | summarize.py |
| Plan usage at end of week, per tool | — | | usage view |
| Limits hit (when) | — | | usage view |

## Where I am today
One paragraph: autocomplete, chatbot, a few parallel sessions, or many tracks?
Which symptom from the module 01 diagnosis table fits me best?

## My target for the 30-day plan
- One practice number to move (for example: "I verify for the agent 15 times a week → 3"):
- One outcome number that must not get worse (for example: rework):
```

For the week's AI spend, prorate each plan's monthly fee to one week (fee × 12 ÷ 52) and add any extra usage or API spend from step 3. [Module 08](../08-token-economics/README.md) explains how to read cost per merged pull request without fooling yourself.

**Checkpoint:** the table is complete, and each target has a number.

### 7. Pick targets that can't be gamed (5 minutes)

Look at your targets again. A target like "run 5 sessions at once" is easy to hit and says nothing about results. Pair every activity target with an outcome that must hold: merged pull requests that didn't need rework, or review time per pull request.

**Checkpoint:** every activity target has an outcome number next to it.

## Done when

- [ ] `baseline-log.csv` covers five working days, with a row per session.
- [ ] `python summarize.py baseline-log.csv` runs without unexplained warnings.
- [ ] `baseline.md` has your guesses, the measured table with every row filled or marked "no data", and a short "Where I am today" paragraph.
- [ ] The table includes the numbers module 10 compares: merged pull requests, cycle time, human minutes per merged pull request, cost per merged pull request and rework (re-checked a week later).
- [ ] You wrote one practice target and one outcome target, each with a number.
- [ ] The files are saved somewhere you'll find them in module 10.

## Reflect

- **Where was the biggest gap between your guesses and the measurements?** Remember it the next time you feel faster.
- **Where did your time go?** Waiting, verifying for the agent or re-explaining? Each points to a module: [06](../06-run-sessions-in-parallel/README.md), [03](../03-close-the-loop/README.md) and [04](../04-context-is-infrastructure/README.md).
- **Did measuring change how you worked this week?** It often does. Note it, so you don't count that change as progress later.
- **Which single symptom would you fix first,** if you could fix only one?

## Stretch

- **A team baseline.** Run the lab with your team, and share only aggregates. Agree up front that nobody's numbers are used to judge performance, or people will log what they think you want to see.
- **Compare with lab 0.** Look at your three lines from [lab 0](../00-start-here/lab.md). Did the week confirm them?
