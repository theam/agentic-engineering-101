---
title: "Workshops"
kind: workshop
last_reviewed: 2026-09-17
---

# Agentic Engineering 101 workshops

[Leer en español](../es/README.md) ·
[Facilitator guide](facilitator-guide.md) ·
[Guide contents](../../content/en/README.md)

This page is for two groups of people: those who organize a workshop and those
who attend one. It describes three formats, what each one should achieve, what
to prepare, and how we find out whether anything changed afterwards.

There are no separate slides and no separate storyline. The workshop is the
guide: every slot in the agendas below points to a lesson and a lab in
[`content/en/`](../../content/en/). In the room we teach a short version of
each lesson and spend most of the time in the labs. The full lessons are for
reading before or after.

> [!NOTE]
> **At The Agile Monkeys** we use this material to onboard our own engineers
> and to run workshops. This is its first edition. The timings come from
> walking through every lab ourselves, not from averaging many cohorts. When you
> run a session, tell us what ran long and what broke in a
> ["share your practice" issue](https://github.com/theam/agentic-engineering-101/issues/new?template=share-your-practice.yml).

## The three formats

| Format | Length | Modules | Best for | Group size | You leave with |
|---|---|---|---|---|---|
| **Taster** | 90 minutes | 00, with short looks at 01, 03, 06 and 07 | Teams deciding whether to invest in the intensive | Up to 20 hands-on, up to 40 demo-only | A picture of the whole game and one change to try next week |
| **Intensive** | 2 days | Day 1 "The system, not the prompt": 00–05 · Day 2 "Orchestration": 06–08 + a parallel sprint | Engineers who will work this way on real code | 8–20 | A practice repository with context, guards, merged PRs and a review ledger, plus your baseline numbers |
| **Follow-up** | 4 weeks, one check-in per week | 09–10, applied to your own code | People who finished the intensive | The same cohort | Before/after numbers from your real work and a team working agreement |

The formats build on each other. The taster is a preview of the intensive's
first morning. The follow-up only makes sense after the intensive, or after
working through modules 00–08 on your own.

The guide rests on three loops and one bottleneck, and the agendas follow them:
the **inner loop** (one agent, one task, done well: modules 02–03), the
**context loop** (the system remembers: module 04), the **outer loop** (many
tracks in parallel: modules 05–07) and **human attention**, the bottleneck that
everything else exists to protect (modules 06–08).

## Who it is for

### Audience

The intensive works best for software engineers who write code every week and
have at least tried a coding agent. In a typical room you will find the three
learning paths described in [module 00](../../content/en/00-start-here/README.md):

- **Newcomers to agents.** They have used an agent a few times, or only as a
  chat assistant. They can take the intensive if they do the pre-work
  carefully. Expect them to finish the core steps of each lab and skip the
  stretch goals.
- **Daily single-agent users.** They use one agent every day, one task at a
  time. This is the core audience. The jump from one session to several is what
  the two days are designed for.
- **Tech leads**, and anyone who already runs a few sessions in parallel. They
  get the most from the stretch goals, from modules 07–09 and from helping their
  table. They also carry the practice back to their teams.

The taster works for any engineer, and for engineering managers who want to see
the practice before deciding. Managers can watch the demo-only version without
installing anything.

It is not a good fit for people who don't write code at all, or for teams that
are not allowed to use coding agents on any code. Those teams can still do the
intensive on the practice project, but the follow-up needs a real repository.

### Prerequisites

Skills:

- **git:** create a branch, commit, merge, resolve a simple conflict.
- **GitHub pull requests:** open, comment, merge.
- **A terminal:** move between folders, run commands, read error messages.
- **Reading Python, roughly.** The practice project is a small command-line
  tool written in Python using only the standard library. You don't need to be a
  Python developer. The agent writes the code, but you must be able to tell
  whether a change makes sense.

Tools and accounts are listed in the pre-work checklist below.

## Pre-work checklist

Participants: finish this at least three working days before Day 1. Organizers:
collect a confirmation (a short form is enough) so facilitators can help anyone
who is stuck before the room fills up. Setup problems solved at home cost five
minutes. In the room they cost the first hour.

### Accounts and plans

- [ ] **A paid plan for at least one capable coding agent**, for example
  [Claude Code](https://code.claude.com/docs/en/overview) or
  [Codex](https://learn.chatgpt.com/guides/best-practices), signed in on the
  machine you will bring. On Day 2 you will run several sessions at once, and
  entry-level plans can run out. Check your plan's usage limits in the vendor's
  documentation before you come. If you already have a second plan, bring it.
- [ ] **Optional: a second agent from a different vendor.** Module 07 uses it as
  a reviewer. Without one you will pair with someone who has it.
- [ ] **A GitHub account** where you can create a private repository.
  `gh auth status` says you are logged in.
- [ ] **Permission to use your plan for training**, if it is a company plan or a
  company account.

### Tools installed

Each of these commands must succeed:

```bash
git --version          # any recent git; worktrees are built in
gh --version
gh auth status
python3 --version      # 3.10 or newer
```

- [ ] Your coding agent starts in a terminal (for example `claude` or `codex`)
  and answers a trivial question.
- [ ] Optional: a terminal or app that shows several agent sessions side by
  side, and voice input you are comfortable with (the dictation built into your
  operating system is enough). The [tools reference](../../content/en/reference/tools.md)
  lists options.

### The practice repository

The labs run on [`shelf`](../../practice/shelf/), a tiny reading-list manager.
Copy it into a repository of your own, so agents can open issues and pull
requests on it. The practice project's README section
["Use it for the labs"](../../practice/shelf/README.md#use-it-for-the-labs)
explains every flag. From the root of your local clone of this guide:

```bash
mkdir -p ~/code
cp -r practice/shelf ~/code/shelf
cd ~/code/shelf
git init -b main
git add .
git commit -m "Start from the Agentic Engineering 101 practice project"
gh repo create shelf --private --source=. --remote=origin --push
python3 -m unittest
```

Then create issues S1 and S2 as the "Before you start" section of
[Lab 0](../../content/en/00-start-here/lab.md) describes, with their titles and
text from the [issue catalog](../../practice/issues/en.md). Lab 5 creates the
rest.

- [ ] `python3 -m unittest` in your copy ends with `OK` (it takes under a
  second).
- [ ] `gh repo view` shows your copy on GitHub.
- [ ] `gh issue list` shows S1 and S2.
- [ ] You keep the clone of this guide on your machine: several labs read the
  issue catalog from it.

### A real repository for the follow-up

- [ ] Choose one repository you will work on during the four weeks after the
  intensive. It should meet all of these:
  - You are **allowed to use coding agents on it**. Read your employer's or
    client's policy; don't assume.
  - Its **tests run locally**, in minutes, without production credentials.
  - **Real work is flowing:** there are issues you will actually do in the next
    month.
  - You can get pull requests **reviewed and merged within a day or two**.
  - It matters, but it is **not the system where a mistake is most
    expensive**. A bad merge should be recoverable.
- [ ] Don't use it during the intensive, except for stretch goals, and never
  show its code on a shared screen without permission.

### Security

- [ ] **No production credentials on the workshop machine.** No cloud
  credentials with production access in your environment or config files, no
  `.env` files with real secrets, no SSH keys or database URLs that reach
  production. If your everyday laptop has them, use a separate operating-system
  user, a virtual machine, a dev container or a cloud development environment
  for the workshop.
- [ ] **No permission-bypass modes on a machine with credentials.** Learn what
  your agent's permission settings do before the workshop (for Claude Code, see
  [permission modes](https://code.claude.com/docs/en/permission-modes)).
- [ ] **A GitHub login that reaches only what you need.** The practice
  repository, and later your follow-up repository.

> [!WARNING]
> During the labs, agents run shell commands you didn't write, read files, and
> process text from issues and pull requests that anyone could have written. In
> August 2025 a compromised npm package
> [invoked installed AI coding CLIs with permission-bypass flags to hunt for secrets](https://nx.dev/blog/s1ngularity-postmortem).
> Simon Willison's ["lethal trifecta"](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)
> explains the general risk: private data, untrusted content and a way to send
> data out, all in one place. A workshop machine should have nothing worth
> stealing.

### Baseline and reading

- [ ] **Start [Lab 1, your baseline](../../content/en/01-from-chatbot-to-system/lab.md),
  one week before Day 1.** Record a normal working week: sessions in parallel,
  PRs merged, time spent waiting on the agent, plan usage. On Day 1 you only
  finish it and set a target. This baseline is what the follow-up compares
  against.
- [ ] Read [module 00](../../content/en/00-start-here/README.md). If you have
  time, read the "Key points" of modules 01–05.

## Format 1: Taster (90 minutes)

### Learning outcomes

After the taster, participants can:

- Explain the difference between using an agent as a chatbot and building a
  system around it: context, verification, decomposition and review.
- Describe how one change goes from issue to reviewed pull request while a
  second change runs in parallel.
- Name one practice they will try on their own work next week.

### Setup

Two variants share the same agenda. **Hands-on:** participants did the "tools
installed" and "practice repository" parts of the pre-work and work in pairs
during the 25-minute block. **Demo-only:** nobody installs anything, and during
that block the room decides, together, how the agent should handle S2 and then
critiques the plan it produces.

### Agenda

| Time | Min | What happens | Material |
|---|---|---|---|
| 0:00 | 5 | Welcome. Quick poll: "Last week, how many agent sessions did you have working at the same time?" (0 / 1 / 2–4 / 5+) | — |
| 0:05 | 10 | The gap between chatbot use and a system; three loops and one bottleneck | [Lesson 00](../../content/en/00-start-here/README.md) · [Lesson 01](../../content/en/01-from-chatbot-to-system/README.md) |
| 0:15 | 15 | Live demo, part 1: the agent explains `shelf`; discuss, plan and build issue S1 with tests | [Lab 0](../../content/en/00-start-here/lab.md) · [Lesson 02](../../content/en/02-one-agent-done-well/README.md) |
| 0:30 | 5 | Live demo, part 2: while S1 runs, create a worktree and start a second session on S2 | [Lesson 06](../../content/en/06-run-sessions-in-parallel/README.md) |
| 0:35 | 25 | Hands-on in pairs: Lab 0 up to the first pull request. Demo-only: the room steers S2 | [Lab 0](../../content/en/00-start-here/lab.md) · [Issue catalog](../../practice/issues/en.md) |
| 1:00 | 10 | Live demo, part 3: a fresh session reviews the S1 pull request; triage one finding | [Lesson 07](../../content/en/07-agents-review-agents/README.md) |
| 1:10 | 8 | The failure moment: an agent claims "done" without running the tests, and a guard makes it prove it | [Lesson 03](../../content/en/03-close-the-loop/README.md) |
| 1:18 | 7 | Debrief with sticky notes: what surprised you, and where your ceiling is today | — |
| 1:25 | 5 | Next steps: the self-paced path, the intensive, minute cards | [Guide contents](../../content/en/README.md) |

## Format 2: Intensive (2 days)

### Learning outcomes

After **Day 1, "The system, not the prompt"** (modules 00–05), participants can:

- Describe their own starting point with numbers, and set a target (01).
- Take an issue through discuss → plan → build → verify with one agent, and
  list the corrections they had to make (02).
- Make an agent check its own work with a deterministic guard instead of a
  reminder in a prompt (03).
- Give a fresh session full context through `AGENTS.md`, a knowledge base and an
  `ACTIVE.md` index (04).
- Turn a list of requests into independent tracks, find the pair that
  conflicts, and write kickoff prompts (05).

After **Day 2, "Orchestration"** (modules 06–08 and the sprint), participants can:

- Run three tracks at once in separate worktrees and merge them in a planned
  order, including one conflict (06).
- Review agent pull requests with a fresh-context reviewer and a second-vendor
  reviewer, give every finding a verdict, and close the loop by decision (07).
- Calculate their cost per merged pull request and name their top token sinks
  (08).
- Turn a vague request into concrete issues, then keep several sessions
  productive on them during a 90-minute sprint without breaking the tests on
  `main`.

### How the time works

The time boxes below are shorter than the `minutes` written at the top of each
lesson and lab file. Those are for self-paced learners. In the room we teach a
condensed version of each lesson, the pre-work covers setup, and facilitators
point to the steps that can become homework when a lab runs long. The
[facilitator guide](facilitator-guide.md) says which ones.

### Day 1 — "The system, not the prompt" (modules 00–05)

| Time | Min | What happens | Material |
|---|---|---|---|
| 09:00 | 20 | Welcome, goals, how sticky notes work. Setup check: "OK" sticky note up when `python3 -m unittest` passes in your copy and your agent answers | Pre-work checklist (above) |
| 09:20 | 15 | The whole game: three loops, one bottleneck, and how the two days map to them | [Lesson 00](../../content/en/00-start-here/README.md) |
| 09:35 | 45 | **Lab 0:** plan and build S1 and open a PR; start S2 in a worktree while S1 runs; review the first PR in a fresh session | [Lab 0](../../content/en/00-start-here/lab.md) |
| 10:20 | 15 | Debrief: what the agent did without being asked, what went wrong, which module explains each step | — |
| 10:35 | 15 | Break | — |
| 10:50 | 20 | From chatbot to system: definition, the adoption ceiling, what the evidence says | [Lesson 01](../../content/en/01-from-chatbot-to-system/README.md) |
| 11:10 | 20 | **Lab 1 (finish):** consolidate the baseline you started a week ago and set a 30-day target | [Lab 1](../../content/en/01-from-chatbot-to-system/lab.md) |
| 11:30 | 20 | One agent, done well: live demo of discuss → plan → build → verify | [Lesson 02](../../content/en/02-one-agent-done-well/README.md) |
| 11:50 | 55 | **Lab 2:** issue S3 through the full cycle, keeping a log of every correction | [Lab 2](../../content/en/02-one-agent-done-well/lab.md) |
| 12:45 | 60 | Lunch | — |
| 13:45 | 20 | Close the loop: live demo of an agent claiming "done", then a guard that makes it prove it | [Lesson 03](../../content/en/03-close-the-loop/README.md) |
| 14:05 | 45 | **Lab 3:** add a deterministic guard that stops the agent from finishing while tests fail | [Lab 3](../../content/en/03-close-the-loop/lab.md) |
| 14:50 | 15 | Break | — |
| 15:05 | 20 | Context is infrastructure: instruction files, knowledge base, the `ACTIVE.md` index | [Lesson 04](../../content/en/04-context-is-infrastructure/README.md) |
| 15:25 | 45 | **Lab 4:** `AGENTS.md`, `kb/ACTIVE.md` and a decision record; compare a fresh session with and without them | [Lab 4](../../content/en/04-context-is-infrastructure/lab.md) |
| 16:10 | 15 | Decompose into tracks: issues as prompts, blast radius, merge order | [Lesson 05](../../content/en/05-decompose-into-tracks/README.md) |
| 16:25 | 45 | **Lab 5:** issues from the catalog, independent tracks, the conflicting pair, three kickoff prompts. Day 2 starts from these | [Lab 5](../../content/en/05-decompose-into-tracks/lab.md) · [Issue catalog](../../practice/issues/en.md) |
| 17:10 | 20 | Wrap-up: commit and push everything, minute cards, what to expect tomorrow | — |
| 17:30 | — | End | — |

**Between the days (15 minutes at most):** check that your working tree is
clean and pushed, that your three kickoff prompts are saved in the repository,
and write down your plan usage for Day 1. Lab 8 uses it.

### Day 2 — "Orchestration" (modules 06–08 and the parallel sprint)

| Time | Min | What happens | Material |
|---|---|---|---|
| 09:00 | 15 | Opening: top themes from the minute cards. Check: clean tree, issues exist (`gh issue list`), kickoff prompts ready | — |
| 09:15 | 25 | Run sessions in parallel: live demo with three worktrees, named sessions and a notification round-robin | [Lesson 06](../../content/en/06-run-sessions-in-parallel/README.md) |
| 09:40 | 80 | **Lab 6:** three tracks at once in three worktrees; merge in the planned order; resolve the conflict between C1 and C2 | [Lab 6](../../content/en/06-run-sessions-in-parallel/lab.md) |
| 11:00 | 15 | Break | — |
| 11:15 | 20 | Agents review agents: PR intent, fresh context, a second vendor, the triage ledger, closing by decision | [Lesson 07](../../content/en/07-agents-review-agents/README.md) |
| 11:35 | 55 | **Lab 7:** two reviewers on a PR from Lab 6; a verdict per finding; close the loop by decision | [Lab 7](../../content/en/07-agents-review-agents/lab.md) |
| 12:30 | 60 | Lunch | — |
| 13:30 | 20 | Token economics: cost per merged PR, where tokens go, model choice | [Lesson 08](../../content/en/08-token-economics/README.md) |
| 13:50 | 30 | **Lab 8:** cost per merged PR for your baseline week and for the workshop so far; top three token sinks | [Lab 8](../../content/en/08-token-economics/lab.md) |
| 14:20 | 10 | Sprint briefing: rules, board, targets per learning path | [Sprint rules](#the-parallel-sprint) |
| 14:30 | 90 | **Parallel sprint** on the practice project: discuss S7, split it into issues, run them in parallel. Take your break while your sessions run | [Issue catalog](../../practice/issues/en.md) · [Practice project](../../practice/shelf/) |
| 16:00 | 30 | Sprint review: room totals, one triage ledger on screen, the best failure of the day | — |
| 16:30 | 20 | Launch the follow-up: confirm your real repository and plan week 1 | [Lesson 10](../../content/en/10-your-30-day-plan/README.md) · [Lab 10](../../content/en/10-your-30-day-plan/lab.md) |
| 16:50 | 10 | Survey and minute cards | [Survey template](facilitator-guide.md) |
| 17:00 | — | End | — |

### The parallel sprint

Ninety minutes to put the whole system to work on the one issue no lab has
built: S7, "Make shelf more useful for book clubs", the deliberately vague
request. After Lab 6 it is usually the only issue left open.

1. **Discuss it** with your agent, in about 20 minutes: the questions that need
   answers and two or three options, as S7's acceptance criteria describe. Pick
   one and write the outcome on the issue.
2. **Split the option into new issues** written like S1–S6, then check them
   against each other for textual overlaps and semantic conflicts, and plan a
   merge order. Most book-club ideas change the shelf file format that C2
   versioned, which gives the most experienced participants plenty to do.
3. **Run the new issues in parallel,** one worktree each, and merge them in the
   order you planned.

Anything left over from earlier labs can join the sprint too.

Rules, read aloud at the briefing:

1. **Every pull request passes your guard locally**, gets a fresh-context
   review, and has a ledger with one verdict per finding.
2. **Humans merge. Agents never merge.**
3. **S7 needs a written discussion outcome before any code.** It is vague on
   purpose.
4. **No permission-bypass modes** on your machine.
5. **At 16:00, stop starting.** Finish or park what is running, and leave your
   worktrees clean (`git worktree list`).

Targets depend on the learning path. Newcomers: two sessions at once. Daily
single-agent users: three or four. Tech leads and people already running
parallel sessions: five or more. The room keeps one board with totals and no
names. The [facilitator guide](facilitator-guide.md) has a variant for trios
sharing one repository.

> [!IMPORTANT]
> The sprint is not a race. A pull request merged with its tests weakened
> counts as a failure, and a failure you caught and fixed counts as a win. We
> celebrate the best recovered failure, not the highest count.

## Format 3: Follow-up (4 weeks on your own code)

### Learning outcomes

After the follow-up, participants can:

- Apply context, guards, parallel tracks and agent review to their own
  repository, one practice per week (10).
- Compare their numbers with their baseline honestly, including what didn't
  improve (10).
- Propose a working agreement for their team: board columns, gates, review
  policy, security rules and disclosure (09).
- Share one practice back with the community.

### How it runs

Each week has one focus and a 60-minute remote check-in with the cohort. The
fourth check-in lasts 90 minutes. Between check-ins, participants work on their
real repository as usual, applying the week's practice, and fill in the
personal weekly check-in from [lesson 10](../../content/en/10-your-30-day-plan/README.md).
Plan for about 30 minutes a day of deliberate practice, on top of normal work,
not instead of it.

| Week | Focus | Read | Do on your real repository | Bring to the check-in |
|---|---|---|---|---|
| 1 | **Context** | [Lesson 04](../../content/en/04-context-is-infrastructure/README.md) · [Lesson 10](../../content/en/10-your-30-day-plan/README.md) | `AGENTS.md` (plus a `CLAUDE.md` that imports it, if you use Claude Code), a `kb/` with `ACTIVE.md` and your first decision records; commit them | A fresh session's answer to "what are we doing and why?" |
| 2 | **Verification and guards** | [Lesson 03](../../content/en/03-close-the-loop/README.md) · the security part of [lesson 09](../../content/en/09-teams-and-organizations/README.md) | A single local "gate" command; one deterministic guard for a rule the agent actually missed; permission tiers. Apply the security baseline before week 3 | One failure the guard caught, and one thing you can't check yet |
| 3 | **Parallel tracks** | [Lesson 05](../../content/en/05-decompose-into-tracks/README.md) · [Lesson 06](../../content/en/06-run-sessions-in-parallel/README.md) | Five or more sessions in worktrees on at least two days; start the draft of [Lab 9](../../content/en/09-teams-and-organizations/lab.md), the team working agreement | The most sessions you sustained, and what broke first |
| 4 | **Agent review and economics** | [Lesson 07](../../content/en/07-agents-review-agents/README.md) · [Lesson 08](../../content/en/08-token-economics/README.md) | Two agent reviewers and a triage ledger on every PR; cost per merged PR; the [Lab 10](../../content/en/10-your-30-day-plan/lab.md) retrospective | Your before/after table and one practice to share |

### Weekly check-in (weeks 1–3, 60 minutes)

| Time | Min | What happens |
|---|---|---|
| 0:00 | 5 | Round: one number each, the most sessions you kept working at the same time this week (from your personal check-in note) |
| 0:05 | 20 | Trios in breakout rooms: your numbers against your baseline, one thing that worked, one thing that broke |
| 0:25 | 20 | Clinic on the week's focus: a short facilitator demo on the practice project, then questions from the trios |
| 0:45 | 10 | Commitments: each person writes, in a shared document, the one thing they will do next week |
| 0:55 | 5 | Minute cards (an anonymous two-question form) |

### Final session (week 4, 90 minutes)

| Time | Min | What happens |
|---|---|---|
| 0:00 | 10 | Round: your before/after in one sentence |
| 0:10 | 25 | Trios: walk each other through your Lab 10 retrospective |
| 0:35 | 20 | The room's anonymous aggregate before/after, and what those numbers do and don't show |
| 0:55 | 20 | Two or three volunteers present their team working agreement (Lab 9) |
| 1:15 | 10 | Everyone drafts one ["share your practice" issue](https://github.com/theam/agentic-engineering-101/issues/new?template=share-your-practice.yml) |
| 1:25 | 5 | Final survey |

> [!WARNING]
> Participants work on code that may be confidential. At check-ins, talk about
> numbers and patterns, not code. Share a screen with real code only if you are
> allowed to, and facilitators demo on the practice project, never on a
> participant's repository.

## What we measure, before and after

The promise of this guide is more parallel work without losing quality. We check
that promise with six numbers. Each participant measures them on their own work.
[Lab 1](../../content/en/01-from-chatbot-to-system/lab.md) already logs sessions,
merged PRs, cycle time, human minutes per PR, cost per merged PR, rework,
waiting time and plan usage. Workshop cohorts add one column to that baseline
week, review wait, because it shows where human attention goes.

| Metric | What it means | How to collect it | Watch out |
|---|---|---|---|
| **Parallel sessions sustained** | Agent sessions you kept doing useful work at the same time on a typical day: the median, not your best moment. Record the peak too | The `parallel` column of the Lab 1 log, which you fill in every time you start a session | A session waiting an hour for your answer is not "running" |
| **PRs merged per week** | Pull requests you drove that merged into the main branch | `gh pr list --author "@me" --state merged --search "merged:>=YYYY-MM-DD"` | Counts are not value. Splitting a PR in three inflates it |
| **Cycle time** | From opening the pull request to merging it, median for the week | The `createdAt` and `mergedAt` fields Lab 1 saves with `gh pr list --json`, summarized by its script | Choose one start event and keep it for both measurements |
| **Review wait** | How long a PR sat ready for a human decision (checks green, automated review closed) before a human decided | Write down when you mark it ready and when someone decides; the PR timeline helps | Often the biggest number. It shows where human attention is the bottleneck |
| **Cost per merged PR** | Agent spend for the week divided by PRs merged | Plan fees prorated to the week, plus any API spend (automated reviewers included), divided by PRs merged | Lower is not automatically better: it can mean smaller, less valuable PRs |
| **Plan usage** | How close you run to your plans' limits, and how often you hit them | Your agent's usage view at the end of each day (see the [tools reference](../../content/en/reference/tools.md)) | Hitting a limit is not failure. It tells you where to look in module 08 |

Four extra signals keep the numbers honest: **rework** (merged PRs that needed
a follow-up fix or revert within 7 days), **human minutes per merged PR** (a
sample of five), **time spent waiting on an agent**, all three from Lab 1, and a
**confidence self-rating** in the surveys.
We don't measure lines of code. As DHH puts it on the
[Lex Fridman Podcast](https://lexfridman.com/dhh-2/), "lines of code is a stupid
metric in general".

### How we collect them

1. **Before:** [Lab 1](../../content/en/01-from-chatbot-to-system/lab.md), during
   a normal week before Day 1, before any workshop habits.
2. **During:** [Lab 8](../../content/en/08-token-economics/lab.md) on Day 2
   rehearses the calculation with workshop numbers. They are noisy and come from
   a toy project. That's fine, because the point is the method.
3. **After:** week 4 of the follow-up, with the same definitions and the same
   tools, in the [Lab 10](../../content/en/10-your-30-day-plan/lab.md)
   retrospective.
4. **Confidence:** the registration form asks for a self-rating, and the Day 2
   and week 4 surveys ask again (see the [facilitator guide](facilitator-guide.md)).

> [!IMPORTANT]
> The numbers belong to the participant. They exist for learning, never for
> performance reviews. Organizers see only anonymous aggregates, and only with
> consent. When people are ranked by a number, they optimize the number and
> the practice degrades.

Be honest about what one week before and one week after can show. Weeks differ:
holidays, incidents, a hard migration. Write down what was unusual about each
week. The research is mixed too. In
[METR's 2025 study](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/),
experienced open-source developers were slower with AI while believing they were
faster, and
[METR's 2026 follow-up](https://metr.org/blog/2026-02-24-uplift-update/)
points to a speedup but calls its own evidence very weak.
[Faros AI](https://www.faros.ai/blog/ai-software-engineering) (a vendor, with
correlational data) saw merged PRs go up and PR review time go up with them.
A [large rollout study at Microsoft](https://arxiv.org/abs/2607.01418) found
more merged PRs among adopters and notes that PR counts are not the same as
value. Treat your before/after as indicative, not as a benchmark, and treat the
survey's self-reports with the same caution.

## Logistics

### In the room

- **Seating:** tables for pairs, with power at every seat. Laptops running
  agents all day drain their batteries.
- **Network:** agents need a stable connection all day. Test the venue network
  beforehand with several laptops running agent sessions, not only a speed test.
  Guest networks that force a new login every hour, drop long-lived connections
  or block SSH break sessions and git. Keep a backup, at least a phone hotspot
  for the facilitator.
- **Projector:** check from the back row that the terminal font is readable.
- **Facilitator setup:** two screens (demo and notes), chat and email
  notifications off, a clean operating-system user. The
  [facilitator guide](facilitator-guide.md) has the full pre-flight checklist.
- **Materials:** sticky notes in two colors for each participant, index cards
  for minute cards, a whiteboard or wall for the sprint board, a visible timer.
- **Staff:** one lead facilitator plus one helper for every 8–10 participants.
  Helpers must have done every lab.
- **Breaks:** agents keep running while people eat. Announce breaks and take
  them: sustainability is part of the lesson.

### Remote

- **Split the intensive into four half-days** of about three and a half hours,
  on consecutive days or two per week: modules 00–02, 03–05, 06–07, and 08 plus
  the sprint. Two full remote days are too much screen time.
- **Platform:** video with breakout rooms, a chat channel for errors and links,
  and a shared status board as the sticky-note equivalent (see the
  [facilitator guide](facilitator-guide.md)).
- **Participants:** a large screen or two (terminal and video), headphones.
  Cameras on during labs help helpers see who is stuck.
- **Facilitators:** at least two, one teaching and one watching chat and
  breakout rooms.
- **Screen sharing:** before sharing a terminal to get help, check that no
  secrets or confidential code are visible.
- **Breaks** every 60–75 minutes.

### Language

The material exists in English and Spanish, and a workshop can run in either.
Participants can talk to their agents in whatever language they think best in.
Decide at the start which language the practice repositories use for
persisted artifacts (code, issues, commits, knowledge base), and write it into
`AGENTS.md`.

> [!NOTE]
> **At The Agile Monkeys** we often talk to agents in Spanish, frequently by
> voice, and keep a standing rule that every artifact in the repository is
> written in English. We haven't seen problems from the mix.

### Organizer timeline

| When | What |
|---|---|
| 4 weeks before | Date, venue or platform, facilitators and helpers. Registration form with the learning-path questions and consent for anonymous metrics |
| 2 weeks before | Send this page's pre-work checklist. Participants confirm plans and policy permissions |
| 1 week before | Participants start the Lab 1 baseline. Facilitators run the pre-flight checklist |
| 3 days before | Review pre-work confirmations; contact anyone who is stuck |
| Day before | Test the network in the room; prepare materials |
| After Day 2 | Send the follow-up message, schedule the four check-ins, share the survey |

## Adapting the material

The guide's content is licensed under [CC BY 4.0](../../LICENSE) and its code
under [MIT](../../LICENSE-CODE). You can run these workshops, change them and
translate them, in your company, your community or as paid training, as long
as you give attribution and say what you changed. For example:

```text
Based on "Agentic Engineering 101" by The Agile Monkeys and contributors
(https://github.com/theam/agentic-engineering-101), licensed under CC BY 4.0.
Changes: <what you changed>.
```

Common adaptations:

- **A different agent.** The principles don't depend on a tool. Swap the
  commands using the [tools reference](../../content/en/reference/tools.md), and
  rehearse every lab on the tool you will teach.
- **A different stack.** Replace `shelf` with a project in your language, but
  keep its properties: it runs and tests in seconds with no services; it has
  about six small independent issues, one pair of issues that change the same
  data model, and one vague request.
- **One day only.** Keep modules 00, 02, 03, 05 and 06 and a 60-minute sprint,
  and assign 01, 04, 07 and 08 as reading. Be clear about the cost: you drop the
  knowledge base and agent review, which are what keep the practice working
  after the workshop.
- **Spread over weeks.** One module per week in a two-hour slot: a 30-minute
  lesson, a 60-minute lab, a 30-minute debrief.
- **Inside one team, on its own code.** From Day 2, run the labs on the team's
  repository, after a security review of the machines and permissions, and
  replace the C1/C2 pair with two real issues that collide.

If you adapt it, tell us how it went in a
["share your practice" issue](https://github.com/theam/agentic-engineering-101/issues/new?template=share-your-practice.yml).
Improvements to these pages are welcome as pull requests; see
[CONTRIBUTING.md](../../CONTRIBUTING.md).
