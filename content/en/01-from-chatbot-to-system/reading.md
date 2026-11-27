---
title: "From chatbot to system · Reading"
kind: reading
last_reviewed: 2026-11-27
---

# Module 01 · From chatbot to system

<!-- Written version of the module for Agentic Engineer Academy. One part per video, in the same order. Format: docs/reading-format.md. -->

## Part 1 · What agentic engineering is

<!-- minutes: 4 -->

> What matters is not how much code the agent writes. It is whether someone designed a way to trust the result.

### Three ways to work with a coding agent

Most engineers move through three ways of working. They differ in who writes the code, who checks it and where the project's memory lives.

| | Autocomplete | Chatbot | System |
|---|---|---|---|
| | You type and accept. | You prompt, wait and read. | You design, decide and review. |
| Who writes | You | The agent | Agents, in parallel |
| Who checks | You | Usually you | The agent, then you |
| Memory | Your head | The chat | The repository |

The chatbot way is where most people stop. It works, but **you become the bottleneck and the memory**: every result waits for you to check it, and every new chat forgets the project. The system way moves both jobs out of your head.

### What agentic engineering means

The system way has a name: **agentic engineering**. Agents write most of the code, and you design the system around them. That system has four parts:

- **Context:** what the agent knows about the project when it starts.
- **Decomposition:** how the work is split into tasks.
- **Verification and review:** how results are checked, and by whom.
- **Decisions:** which ones stay with you.

Two things the definition leaves out on purpose:

- **How many agents you run.** One agent, run well, already counts.
- **That you stop reading code.** You decide, by risk, what deserves your reading.

### What it isn't: vibe coding

DHH, the creator of Ruby on Rails, gives the sharpest definition of vibe coding: "You do not look at the implementation. That, to me, is what separates vibe coding from programming."

Not everyone uses the term this way. Gene Kim and Steve Yegge, for example, use it for disciplined work with AI. So check what people mean. **In this course, vibe coding means nobody looks at the code.**

> You can outsource your thinking, but you can't outsource your understanding.
>
> A line Andrej Karpathy, the AI researcher who coined "vibe coding", quotes and keeps returning to.

### In practice

The difference shows up even in a single prompt. Shelf is the small practice project you use in the labs.

```prompt-weak
add csv export to shelf
```

```prompt-strong
Implement issue #4 (read it with gh issue view 4). Write the tests first and show me they fail, then implement. Run python -m unittest and paste the output. If something can't run, tell me exactly what didn't run and why. Open a pull request that closes #4.
```

The better prompt is short because it leans on a system:

- **An issue** that already holds the specification.
- **Tests** the agent can run to check its own work.
- **A pull request** where the result gets reviewed.

### Key points

- Agentic engineering is a system you design, not a better prompt.
- One agent, run well, already counts.
- Vibe coding means nobody looks at the code.

## Part 2 · The chatbot ceiling

<!-- minutes: 4 -->

> Many engineers get stuck at the chatbot stage. A better prompt won't move them. Changes outside the prompt will.

### The story

An engineer adopted a coding agent six months ago. The first weeks were exciting. Then progress flattened.

Today they paste the same project background into every new window. They run the tests themselves, because once the agent said "all tests pass" without running them. They feel faster. They aren't sure they are.

That flat spot is the **chatbot ceiling**: one window, one prompt, one task at a time.

### Why people stay there

It isn't laziness. The chatbot stage pays off quickly, so nothing hurts enough to push further.

Every next step is outside the prompt: tests the agent can run, a knowledge base (files that keep what the project knows between sessions), work split into tasks, a review routine. **Each one feels like extra work the week you add it, and only pays off weeks later.**

### Why the gap widens, and closes

People who make these changes see their gains add up. Corrections become rules the agent reads at the start of every session. Repeated checks become scripts. Their setup improves every week, while a chatbot session starts from zero. So the gap between them and those who stay at the ceiling keeps growing.

**The good news:** each change is small and learnable. A few focused weeks are enough. The rest of this course gives you the order.

### Find your own ceiling

Look at your own habits. Each one points to what is missing, and to the module that teaches it.

| If you notice | What's missing | Module |
|---|---|---|
| You paste the same background into new sessions | Instruction files and a knowledge base | 04 |
| You run the tests yourself after the agent says "done" | Checks the agent runs on its own | 03 |
| You write long "perfect prompts" | Context and a conversation, not one long prompt | 02 |
| You watch the agent work because there's nothing else to do | Work split into independent tasks | 05 and 06 |
| You read every change line by line | Review by risk, with agents reviewing first | 07 |
| You hit your plan's limits and don't know what you got for it | Cost per result | 08 |

### Key points

- The chatbot stage feels good enough. That is why people stay.
- What moves you is outside the prompt: checks, memory, tasks and review.
- The gap grows on its own. It closes in a few weeks once you start.

## Part 3 · Your job moves

<!-- minutes: 3 -->

> When agents write most of the code, your job doesn't disappear. It moves from writing lines to designing and judging the system.

### From writer to architect

Peter Steinberger, an engineer who runs five to ten agents on a project he mostly builds alone, puts it like this: "I don't have a line by line code understanding. That's, that's what Codex does for me, but I'm the architect." Codex is OpenAI's coding agent.

DHH compares it to a master whose students do the chiseling while he says when the proportions are wrong. That includes telling agents to "make it simpler", which they rarely do on their own.

### What stays human

Agents can take the typing. In every account the course trusts, four things stay with you:

#### 1 · Product judgment

Deciding what is worth building.

#### 2 · Coherence

Many reasonable changes can still wear down an architecture. Someone keeps the shape of the whole.

#### 3 · Verification and approvals

What "correct" means, and who approves plans and merges changes.

#### 4 · Understanding

Enough of it to tell when the agent is wrong.

### In practice

At The Agile Monkeys, the company behind this course, engineers who work this way describe their day as conversations, not prompts. They plan with an agent that already knows the project, ask it to turn the plan into issues, and spend their time accepting plans, deciding and reviewing.

### What it costs

It isn't good news for everyone. DHH: "you're gonna have a hard time coping with the new reality if the only thing you loved about programming was the mechanical bits." Steinberger found the opposite: "I always thought I liked coding, but really I like building."

It is also more tiring than it looks. Developer Simon Willison calls running several agents "surprisingly effective, if mentally exhausting".

### Key points

- Your role moves from writing lines to being the architect.
- Product judgment, coherence, verification and approvals, and understanding stay human.
- It is more tiring than it looks. Plan your pace.

## Part 4 · Don't trust your feeling of speed

<!-- minutes: 4 -->

> Your feeling of speed is not evidence. Measure your results before and after.

### What the studies found

Enthusiasm is easy to find. Solid evidence is not. Each study measured something different, so read each one with its limit.

#### METR · 2025 · 19% slower, felt 20% faster

16 experienced developers on code they knew well, with early-2025 tools. **Limit:** a 2026 follow-up points to a speedup, but isn't conclusive.

#### DORA · 2025 · AI amplifies what is there

Nearly 5,000 professionals. AI magnifies a team's existing strengths and weaknesses. **Limit:** more throughput, but also more instability.

#### Faros AI · 2025 · The bottleneck moves to review

Over 10,000 developers. More merged pull requests, longer reviews. **Limit:** vendor data, correlation only.

#### Microsoft · 2026 · About 24% more pull requests

Its own engineers, over four months. **Limit:** a merged pull request is not the value it delivers. Not peer reviewed yet.

### Why the results differ

The studies seem to disagree. Five things explain most of the difference:

- **Setting.** METR 2025 tested experts on code they know by heart, where humans are strongest.
- **Era.** Andrej Karpathy, the AI researcher who coined "vibe coding", said coding agents "basically didn't work before December and basically work since", meaning December 2025.
- **Setup and skill.** An agent that can run the tests behaves very differently from one that can't. And someone in their first weeks differs from someone in their second year.
- **What's measured.** Time, pull requests and value are different things. Self-reports are the weakest measure.
- **The rest of the system.** Gains vanish if review can't absorb more changes.

### What to measure instead

Don't measure lines of code or how many agents you run. Measure results:

- **Merged pull requests.**
- **Cycle time:** from opening a pull request to merging it.
- **Rework:** merged pull requests that needed a fix or a revert within 7 days.
- **Your minutes per merged pull request:** time you spend reading, deciding and unblocking.
- **Cost per merged pull request:** what you spent on AI, divided by what you merged.

Lab 1 has you log one normal week and write these numbers down. Don't change how you work until the week is logged.

### Key points

- People misjudge their own speed.
- AI amplifies what a team already does well and badly.
- Don't trust anyone's headline number. Measure your own.
