---
title: "Token economics"
module: 8
kind: lesson
minutes: 45
level: advanced
last_reviewed: 2026-09-17
---

# 8. Token economics

> **In one sentence:** Spend tokens where they replace human attention, stop spending them where they only buy more rounds, and judge the result by cost per merged PR, not cost per token.

## What you'll be able to do

- Tell healthy high consumption apart from waste.
- Choose between subscriptions and pay-per-token API billing for each kind of usage.
- Calculate cost per merged PR, and read it together with rework rate and human minutes per PR.
- Find the common token sinks in your own work and fix them.
- Pick models by role, and decide when to parallelize, sequence or delegate to a subagent.
- Measure before and after without being misled by lines of code or self-reports.

## Why this matters

Here are two situations with roughly the same bill.

One of our engineers used up a top-tier plan's weekly allowance in two days. They were running about 20 agents: some writing code, some reviewing each other's PRs, some maintaining the product's knowledge base. Nothing was broken. That is what this way of working consumes.

In [module 7](../07-agents-review-agents/README.md) you met the other situation: a review loop that worked all night and grew a 5,000-line PR to tens of thousands of lines. It burned tokens just as fast and left a PR that was harder to merge than when it started.

A token counter can't tell these apart. Cost per merged PR, rework and human minutes can. This lesson is about spending freely on the first kind of work and cutting the second.

## Consumption follows skill

The more of this guide you practice, the more tokens you use. Each parallel session carries its own context, reviewers re-read the code, and knowledge-base upkeep happens in every session. Someone running 10 to 20 sessions can use an order of magnitude more than someone chatting with one agent.

Public reference points:

- The [Claude Code costs documentation](https://code.claude.com/docs/en/costs) reports that across enterprise deployments the average is around $13 per developer per active day and $150–250 per month, with 90% of users below $30 per active day. Heavy parallel users sit in the tail of those averages. The same page says agent teams use about 7 times more tokens than standard sessions when teammates run in plan mode.
- [Peter Steinberger](https://steipete.me/posts/just-talk-to-it) wrote in October 2025 that he paid for four OpenAI subscriptions and one Anthropic subscription, "around 1k/month for basically unlimited tokens".

> [!NOTE]
> **At The Agile Monkeys** several of our engineers hit the limits of two top-tier subscriptions, one per vendor, most weeks. That's indicative, not a benchmark. We're also honest that much of that spend probably isn't useful yet and needs optimizing.

So don't ask "how do I use fewer tokens?" Ask "what did each token buy?" Healthy spend buys things you'd otherwise pay for with your attention: a verified PR, a real review finding, a knowledge-base update that saves a future session an hour. Waste buys extra rounds, restarts and re-derivations.

## Subscriptions, API keys and the limits you'll hit

| | Subscription (per person) | API (pay per token) |
| --- | --- | --- |
| How you pay | A flat monthly fee, with usage limits over time windows | Per token, with no ceiling unless you set one |
| Good for | Heavy interactive use by one person | Automation (review bots, CI agents, scheduled jobs), light or bursty use, precise attribution |
| Watch out for | Limits that reset on windows; terms that define what the plan covers; tools that assume one signed-in account per machine user | A runaway loop becomes a bill: set spend limits before you automate |

**For heavy interactive use, subscriptions are usually much cheaper.** Steinberger estimated that paying per API call would have cost him around ten times more. [DHH](https://lexfridman.com/dhh-2/) ran a long library port inside his subscription and estimated it would have cost about $550 at per-token prices. These are individual estimates, and prices and limits change often. That's why tool specifics live in the [tools reference](../reference/tools.md), with a review date.

Patterns that work:

- **One top-tier subscription per vendor** for heavy practitioners. You get cross-vendor review ([module 7](../07-agents-review-agents/README.md)) and a fallback when one plan hits its limit.
- **API keys with spend limits for anything that runs without a person**, such as review bots, CI repair agents and scheduled jobs. Per-review services add up fast. Claude Code's managed review averages $15–25 per review ([docs](https://code.claude.com/docs/en/code-review)), and reviewing on every push multiplies that by the number of pushes.
- **Plan the second account before you need it.** People who buy a second subscription in a busy week find out that their tools assume one signed-in account per machine user.

> [!WARNING]
> "Basically unlimited" is never literal. Read your plan's terms before pointing a personal subscription at shared bots, CI or other people's work. That usage often belongs on API keys or an organization plan.

## Cost per merged PR

Cost per token tells you about your vendor. Cost per merged PR tells you about your system.

- **AI spend**: everything for the period. Subscriptions prorated to the period, extra usage, API keys for bots and CI, and per-review services.
- **Cost per merged PR** = AI spend ÷ PRs merged.
- **Rework rate** = reworked PRs ÷ PRs merged. A reworked PR is a merged PR that needed a follow-up fix or revert within 7 days.
- **Cost per net merged PR** = AI spend ÷ (PRs merged − reworked PRs).
- **Human minutes per merged PR**: your time reading, deciding and unblocking, from a timed sample.

### A worked example

> [!IMPORTANT]
> These are **invented round numbers** to show the calculation. They are not our costs and not real prices.

Between week A and week B an engineer changes three things: every PR gets an intent statement and review loops close by decision; the always-loaded instruction file is cut in half; and they run two more parallel tracks.

| | Week A | Week B |
| --- | --- | --- |
| Subscriptions, prorated to the week | $100 | $100 |
| Extra usage and API keys (bots, CI) | $40 | $80 |
| **AI spend** | **$140** | **$180** |
| PRs merged | 10 | 18 |
| Reworked PRs (fixed or reverted within 7 days) | 3 | 2 |
| Sampled review minutes per PR | 25 | 12 |

- Cost per merged PR: A = 140 ÷ 10 = **$14.00**. B = 180 ÷ 18 = **$10.00**.
- Rework rate: A = 3 ÷ 10 = **30%**. B = 2 ÷ 18 ≈ **11%**.
- Cost per net merged PR: A = 140 ÷ 7 = **$20.00**. B = 180 ÷ 16 = **$11.25**.
- Human review time: A = 25 × 10 = **250 minutes**. B = 12 × 18 = **216 minutes**, for almost twice the merged work.

Spend went **up** by about 29%, and every unit number improved. That's what "consumption follows skill" looks like when it works. Judged by the bill alone, week B would look like a failure.

The trade to avoid runs the other way: saving a few dollars of tokens per PR by adding minutes of your own work. Put a price on your minutes, and most token savings that cost review time stop looking like savings.

Caveats:

- **PRs aren't equal.** Compare similar work in the same repository, and read trends over several weeks.
- **Merged isn't the same as valuable.** In a [study of Microsoft's rollout](https://arxiv.org/abs/2607.01418) of command-line coding agents (a preprint), adopters merged roughly 24% more PRs, and the authors stress that a merged PR "is not the same as the value it delivers".
- **Goodhart's law.** Once cost per PR is a target, people split PRs, which undoes [one PR, end to end](../05-decompose-into-tracks/README.md). Watch PR size alongside it.
- **Some spend never becomes a PR.** Planning, research and knowledge-base upkeep are real work. Track them as a separate line instead of hiding them.

## Where tokens are wasted

| Sink | How you notice | Fix |
| --- | --- | --- |
| Review loops chasing scope creep | The diff grows every round; high-priority findings stop falling | Intent statement, triage ledger, close by decision, one push per round ([module 7](../07-agents-review-agents/README.md)) |
| Bloated always-loaded context | Rules get ignored; context is already large before you type | A short `AGENTS.md` that acts as a map; details in docs and skills loaded on demand ([module 4](../04-context-is-infrastructure/README.md)) |
| Too many tools, plugins and skills | Usage breakdowns attribute a big share to them | Add a skill when something hurts; remove unused ones; prefer CLIs the model already knows |
| Re-deriving known facts | Every session re-reads the same files and repeats the same investigation | "What I already checked" in kickoff prompts; decisions kept in the knowledge base |
| Long sessions past useful context | One session, many unrelated tasks; corrections pile up | One task per session; start fresh after two failed corrections |
| Verbose tool output | Test and build logs flood the context | A hook that filters output to failures; noisy work in a subagent |
| A model doing what code should | The model re-types numbers, polls CI in a loop, joins data | Deterministic scripts; call the model only after deterministic checks finish, with capped attempts |
| Background and idle usage | Usage grows while you're away | Stop idle loops and teammates; no scheduled prompts on large sessions |
| Work thrown away | PRs closed unmerged; parallel tracks collide | Prioritize by value; plan the merge order of conflicting tracks before they start ([module 5](../05-decompose-into-tracks/README.md)) |

Why long sessions cost so much, per the [Claude Code costs documentation](https://code.claude.com/docs/en/costs): every request resends the whole conversation, so a one-line question in a session open all day pays for the whole day. Compacting a large conversation is itself a large request, while starting fresh costs nothing. Tool definitions add up too. Steinberger wrote "Use GitHub's MCP and see 23k tokens gone" in 2025. Claude Code now loads MCP tool definitions on demand by default, so measure your own setup rather than trusting old numbers.

❌ **Weak prompt**

```text
The stats test is failing. Figure out why.
```

✅ **Better prompt**

```text
test_finished_this_year in tests/test_stats.py started failing today, on CI and on
my laptop. What I already checked, so start from here and don't re-derive it:
shelf/commands/stats.py hasn't changed since the test last passed (git log), and
every test gets its own temporary SHELF_PATH and HOME (tests/support.py), so
leftover files are ruled out. First hypothesis: the test hardcodes a year instead
of deriving it, and the year just changed. If that isn't it, stop and report what
you found before trying anything else.
```

The weak prompt pays for the whole investigation again. The better one pays only for what's still unknown.

## Model choice by role

**Default to the strongest model you have for planning, architecture, root-cause debugging and review.** Mistakes there multiply. A cheaper model that needs three corrections usually costs more in total: retried tokens plus your minutes. [Boris Cherny](https://x.com/bcherny/status/2007179832300581177), who created Claude Code, described using the strongest model with extended thinking for everything, because it's slower but needs less steering.

**Downgrade only with evidence.** Run both models on the same real issues in the same CI, and compare pass rate, corrections, review findings, total tokens and wall time.

> [!NOTE]
> **At The Agile Monkeys** the model is a setting, not a hard-coded choice: the strongest by default, downgraded only with evals or proven cost pressure. Our automated agents record per-run receipts with token and cost counters, but no prompts or transcripts. Our CI-repair agent calls the model only after the deterministic checks finish, with a capped number of attempts.

DHH's experiment shows both sides. He asked the strongest model he had to port a Python library to Rust. It started by writing a detailed eight-step plan. When his subscription tokens ran out, another model finished the port from that plan. He then gave the same plan to other models. Several completed the job at roughly a tenth of the cost, and one at about a twentieth, more slowly. The cheapest ones failed. One needed a dozen prompts just to start, and then:

> "The first thing it did was to cheat." — DHH on [Lex Fridman Podcast #501](https://lexfridman.com/dhh-2/)

It found an existing implementation outside its directory, wrapped it, and said it was done. What to take from this:

1. **The plan was the valuable artifact.** Spending on the strongest model for the plan made cheaper execution possible.
2. **Cheaper executors can work** when the plan is explicit and verification is strong.
3. **The cheapest can fail quietly or game the task.** Verify *how* the work was done, not just the output. [Simon Willison](https://simonwillison.net/2025/Oct/7/vibe-engineering/) calls agents "weird digital interns who will absolutely cheat if you give them a chance."
4. **It was one task in one domain.** Test on your own work before you switch.

| Role | Default | When a cheaper or faster model can fit | Evidence to ask for |
| --- | --- | --- | --- |
| Planning, architecture, debugging | Strongest | Rarely | None: stay on the strongest |
| Implementing an explicit, approved plan | Strongest | Mechanical work with strong tests | Same pass rate and review findings on real issues |
| Review | Strongest, from a different vendor than the writer | Narrow checklist specialists | Catches seeded bugs; tolerable false positives |
| Search, log triage, doc lookup in subagents | Fast model | Usually | Summaries stay accurate |

Vendors can differ by role as well. With current models, one vendor's agent tends to talk more and helps us think, while another takes a task and goes, so we use the second heavily for review. Many tools also let you lower reasoning effort for simple tasks. Thinking tokens are billed as output tokens.

## Parallelize, sequence or delegate

| Situation | Do this | Why |
| --- | --- | --- |
| Independent issues in different files, each verifiable alone (S1, S2, S4 in the [practice project](../../../practice/shelf/)) | Parallel sessions in worktrees | Spend grows linearly; your waiting drops |
| Two issues changing the same model or storage (C1 tags, C2 versioning) | Implement both in parallel; sequence the merges and write the order into both issues | The later track merges `origin/main` and adapts; waiting would turn two tracks into a queue, and an unplanned order into re-reviews and discarded work |
| The next step depends on what you learn (a spike, an unknown API) | One exploratory session, then fan out | Parallel guesses burn tokens on paths you'll discard |
| Your review queue is already full | Don't start more; review and merge | [Faros AI](https://www.faros.ai/blog/ai-software-engineering) measured review time up 91% in heavy-AI teams |
| A bounded, verbose task whose result is a summary | Subagent | Keeps the orchestrator's context small |
| Work you'll steer, or that ends in a PR | Separate session | Visibility, control, a reviewable PR |
| One mechanical change across many files | Fan out after a 2–3 file pilot | Fix the prompt before multiplying its mistakes |

Willison names the limit: "I can only focus on reviewing and landing one significant change at a time." ([Embracing the parallel coding agent lifestyle](https://simonwillison.net/2025/Oct/5/parallel-coding-agents/))

**Subagents protect context, not tokens.** A subagent may re-read files the orchestrator already saw, so total tokens can go up. What you buy is an orchestrator that stays small and focused. Anthropic describes subagents that explore with "tens of thousands of tokens or more" and return summaries of often 1,000–2,000 tokens ([Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)). Steinberger prefers separate windows: "What others do with subagents, I usually do with separate windows," because he can see and steer what comes back.

## Measure before and after

Start from your [Lab 1](../01-from-chatbot-to-system/lab.md) baseline, change one thing at a time, and measure for at least two weeks.

| Metric | Where it comes from | Trap |
| --- | --- | --- |
| PRs merged per week | `gh pr list --state merged` | Size and value vary; splitting inflates it |
| Cycle time (started → merged) | Issue and PR timestamps | Coding gets faster; waiting doesn't |
| Review wait (ready → merged) | PR timeline | Where AI throughput piles up |
| Rework rate | Follow-up fixes and reverts within 7 days of each merge | Needs honest classification, and a week's wait |
| Change failure rate, recovery time | Deploy and incident records | Shows up weeks later |
| AI spend per person and per merged PR | Billing and plan usage screens | Flat fees hide marginal cost |
| Human minutes per merged PR | A timed sample | Estimates drift; re-sample |

[DORA](https://dora.dev/dora-report-2025/) tracks five delivery metrics: lead time for changes, deployment frequency, failed deployment recovery time, change failure rate and deployment rework rate. Its 2025 research says "AI's primary role is as an amplifier, magnifying an organization's existing strengths and weaknesses", and links AI adoption to higher throughput but also more instability. Measure stability, not only speed.

What the evidence says about measuring:

- **Self-reports mislead.** In [METR's 2025 study](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/), experienced open-source developers took 19% longer with AI. They had expected a 24% speedup and still believed afterwards that they'd been about 20% faster.
- **Parallel work breaks simple timing.** [METR's 2026 follow-up](https://metr.org/blog/2026-02-24-uplift-update/) found estimates pointing toward a speedup but not statistically significant, and calls its timing unreliable for developers using multiple agents concurrently, which is exactly how this guide works.
- **Cheap tasks crowd out valuable ones.** METR's [task substitution analysis](https://metr.org/blog/2026-05-08-task-substitution-and-uplift/) found people drift toward tasks AI made cheap, so per-task speedups overstate value.
- **Throughput moves the bottleneck.** Faros AI (a vendor, with correlational data from more than 10,000 developers) found high-AI teams merged 98% more PRs, while review time rose 91%, PR size rose 154% and bugs per developer rose 9%, with no significant improvement at company level.
- **Lines of code mislead most.** DHH: "lines of code is a stupid metric in general". By that metric, module 7's 40,000-line PR was our most productive work that week.

Measure from systems: git, CI, billing, incidents. Use self-reports for how the work felt, not for how fast it went.

## Sustainable pace

- **A usage bar that resets is not a quota to fill.** Steinberger has written candidly about his "slot machine addiction" to agents ([Just One More Prompt](https://steipete.me/posts/just-one-more-prompt)). Starting a session at midnight whose PR nobody reviews until morning buys nothing.
- **The human runs out first.** DHH, on his own pace: "This is not sustainable at all." Stop starting tracks you can't review, and protect your sleep.
- **Budgets that follow skill.** Equal token budgets per person hold back the people furthest along. Give heavy users room, and review their unit numbers with them, not just the bill.

## Other ways to see it

- **Strongest model everywhere?** The Claude Code costs documentation recommends a mid-tier model for most coding tasks and the top tier for complex architecture and multi-step reasoning. Steinberger says "if you're a skilled driver, you can get good results with any of those latest gen models" ([Lex Fridman Podcast #491](https://lexfridman.com/peter-steinberger-transcript/)). We default to the strongest and downgrade per role with evidence, because our bottleneck is attention, not tokens.
- **Is parallel spend worth it at all?** [Mitchell Hashimoto](https://mitchellh.com/writing/my-ai-adoption-journey) describes a careful adoption path without multiple agents, with notifications off because context switching is expensive. For some people and some work, focus buys more.
- **Track tokens if human time dominates?** Some say no. We do, because the patterns that waste tokens (unbounded loops, bloated context, re-derivation) usually waste attention too.

## Watch out

- **Rationing tokens by verifying things yourself.** You swap cheap tokens for expensive minutes.
- **Downgrading a model because of price** without comparing results on your own tasks.
- **Reporting lines of code or "sessions run"** as productivity.
- **Reviewing on every push with no convergence rules.** Cost multiplies per push and rounds never end.
- **Starting more parallel tracks while your review queue grows.** You create queues, not throughput.
- **One session all day.** Every question pays for the whole day's conversation.

## Check your understanding

1. Week A: $100 spend, 10 PRs merged, 3 of them reworked. Week B: $140, 11 PRs merged, 1 of them reworked. Better or worse?

   <details><summary>Answer</summary>

   Cost per merged PR rose ($10.00 → $12.73), but cost per net merged PR stayed about the same (100 ÷ 7 ≈ $14.29 → 140 ÷ 10 = $14.00) while rework fell from 30% to about 9%. Probably better. Check human minutes and more than one week before deciding.

   </details>

2. A teammate proposes a cheaper model for all implementation to halve spend. What do you ask for?

   <details><summary>Answer</summary>

   A comparison on the same real issues in the same CI: pass rate, corrections, review findings, total tokens including retries, wall time, and a check that nothing was gamed (tests edited, existing code wrapped). Keep planning and review on the strongest model unless the evidence says otherwise.

   </details>

3. Which is most likely a token sink: (a) a subagent that reads 40 files and returns a 1,500-token summary; (b) a session open since morning that has handled six unrelated tasks; (c) 12 parallel sessions on independent issues?

   <details><summary>Answer</summary>

   (b). Every request resends the whole day's conversation, and the irrelevant context also lowers quality. (a) spends tokens to protect the orchestrator's context. (c) is fine if you have the review capacity.

   </details>

4. Why is time per task a poor measure for the way of working this guide teaches?

   <details><summary>Answer</summary>

   With several agents running at once, time on a task is neither continuous nor attributable, and METR calls its own timing unreliable in that setting. Measure outcomes from systems instead: merged PRs, cycle time, review wait, rework, incidents and spend.

   </details>

## Key points

- Consumption follows skill: high spend is healthy when it buys verified, merged work.
- Subscriptions are usually far cheaper for heavy interactive use. Anything that runs without a person gets API keys with spend limits.
- Judge by cost per merged PR, together with rework rate, human minutes and PR size.
- The biggest sinks are unbounded review loops, bloated always-loaded context, re-derivation and long sessions.
- Strongest model for plans and review. Downgrade per role with evidence, and check how the work was done.
- Parallelize independent work, sequence the merges of conflicting work, and use subagents to protect context.
- Measure from systems, not from lines of code or impressions, and protect your pace.

## Go further

- [Claude Code: manage costs effectively](https://code.claude.com/docs/en/costs): tracking usage, reducing tokens, agent team costs.
- [Just Talk To It](https://steipete.me/posts/just-talk-to-it) by Peter Steinberger: subscriptions vs API, CLIs vs MCP servers, windows vs subagents.
- [DHH on Lex Fridman Podcast #501](https://lexfridman.com/dhh-2/): the multi-model port experiment.
- [METR 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) and [METR 2026](https://metr.org/blog/2026-02-24-uplift-update/): controlled evidence and its limits.
- [DORA 2025](https://dora.dev/dora-report-2025/): AI as an amplifier; delivery metrics to watch.
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents): why small, high-signal context wins.

Next: [9. Teams and organizations](../09-teams-and-organizations/README.md)
