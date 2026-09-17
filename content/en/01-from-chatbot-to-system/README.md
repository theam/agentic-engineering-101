---
title: "From chatbot to system"
module: 1
kind: lesson
minutes: 45
level: foundation
last_reviewed: 2026-09-17
---

# 1. From chatbot to system

> **In one sentence:** Agentic engineering is not a better prompt but a system you design (context, decomposition, verification, review and decisions), so agents can write most of the code without lowering the quality bar.

## What you'll be able to do

- Define agentic engineering, and tell it apart from autocomplete and from vibe coding, including where respected people use these words differently.
- Recognize the "one window, one prompt, one task" ceiling in your own habits, and name the missing piece behind each symptom.
- Describe how the engineer's role shifts from writing lines to designing and editing a system, and what stays human.
- Read productivity studies critically: what METR, DORA, Faros AI and Microsoft measured, and what they didn't.
- Measure your own starting point, so you can tell later whether anything changed.

## Why this matters

Think of an engineer who adopted a coding agent six months ago. The first weeks were exciting: boilerplate vanished and small bugs took minutes. Then progress flattened.

Today their day looks like this. They open a new window and paste the same paragraph of project background. They watch the agent work. They run the tests themselves, because the last time the agent said "all tests pass" it hadn't run them. Diffs got bigger, so reviews take longer. They feel faster. They aren't sure they are.

No better model or cleverer prompt fixes that. What's missing is outside the prompt box: a place where project knowledge lives, a way for the agent to check its own work, work split so several tasks run at once, and review that doesn't depend on reading every line. This module names that shift and looks honestly at the evidence.

## Three ways to work with a coding agent

| | Autocomplete | Chatbot | System |
|---|---|---|---|
| Who writes the code | You, with suggestions | The agent, one request at a time | Agents, on several tracks at once |
| Your main job | Typing and accepting | Prompting, waiting, reading diffs | Designing context, splitting work, deciding, reviewing |
| Unit of work | A line or a function | A prompt | A track that ends in a merged pull request |
| Who verifies | You | Usually you | The agent first, with checks you designed; then another agent; then you, where it matters |
| Where memory lives | Your head | The chat, until you close it | Files in the repository that every session loads |
| Where it breaks | Slow for large changes | You become the bottleneck and the memory | Weak verification or context gets multiplied |

We define **agentic engineering** as software engineering where agents write most of the code, and humans design the system around them: the context agents work with, how work is decomposed, how results are verified and reviewed, and which decisions stay human.

Two things this definition leaves out on purpose. It doesn't say how many agents you run; one well-run agent is already agentic engineering. And it doesn't say you stop reading code; it says you decide, by risk, what deserves your reading.

## What the words mean, and who disagrees

The vocabulary is new and people use it differently. You will read all of these terms, so it helps to know who means what.

**Vibe coding.** [Andrej Karpathy](https://karpathy.bearblog.dev/sequoia-ascent-2026/) coined the term in early 2025 for building software by prompting without caring about the code. [DHH](https://lexfridman.com/dhh-2/) gives the sharpest definition we know:

> "You do not look at the implementation. That, to me, is what separates vibe coding from programming" — DHH on [Lex Fridman Podcast #501](https://lexfridman.com/dhh-2/)

**Agentic engineering.** In early 2026 Karpathy [proposed "agentic engineering"](https://x.com/karpathy/status/2019137879310836075) for professional work with agents and more oversight. In a later talk he separated the two terms like this:

> "Agentic engineering is about preserving the quality bar of professional software." — Andrej Karpathy, [Sequoia Ascent 2026](https://karpathy.bearblog.dev/sequoia-ascent-2026/)

[Simon Willison](https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/) uses the term for developing software with coding agents, meaning agents that run tools in a loop, and draws the line at whether the author has brought the code up to a production-ready standard. [Addy Osmani](https://addyosmani.com/blog/agentic-engineering/) puts it in one line: "AI does the implementation, human owns the architecture, quality, and correctness."

**Augmented coding.** [Kent Beck](https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes) uses a different name for a similar idea: "In augmented coding you care about the code, its complexity, the tests, & their coverage."

**Vibe coding, the other meaning.** Gene Kim and Steve Yegge's book [*Vibe Coding*](https://itrevolution.com/product/vibe-coding-book/) uses "vibe coding" for disciplined, professional work with AI, which is close to what everyone above calls agentic engineering. [Peter Steinberger](https://lexfridman.com/peter-steinberger-transcript/) goes the other way and calls "vibe coding" a slur.

So when someone says "vibe coding", check which meaning they intend before you agree or disagree. In this guide, "vibe coding" means DHH's definition: nobody looks at the implementation. "Agentic engineering" means the system above.

> [!IMPORTANT]
> The line that matters is not how much code the agent writes. It is whether someone designed a way to trust the result. In a line Karpathy quotes and keeps returning to: "You can outsource your thinking, but you can't outsource your understanding."

## The adoption ceiling

Many engineers who adopt an agent stay at the chatbot stage for a while. It isn't laziness. The chatbot stage pays off quickly, so nothing hurts enough to push further, and every next step changes something *outside* the prompt: tests the agent can run, a knowledge base, issues a fresh session can execute, worktrees, a review routine. Each one feels like overhead the week you add it and pays off weeks later.

Those who make those changes compound. Corrections become rules in an instruction file, repeated checks become scripts the agent runs, repeated workflows become skills. Their setup improves every week, while a chatbot session starts from zero every time. That is why the gap widens instead of closing on its own.

The flip side is encouraging: each of those changes is small and learnable, so the gap also closes quickly once you start. You don't need a year. A few focused weeks, even in your spare time, are enough to put the first layers in place, and the rest of this guide shows you the order.

> [!NOTE]
> **At The Agile Monkeys** we have used AI coding tools for years, and every one of us has hit this ceiling at some point, usually more than once as the tools changed. What moved us past it was never a new tool. It was writing practices down and showing each other how we work. This guide is that write-up.

Adoption spreads from person to person, not through announcements: a [large study of Microsoft's early-2026 rollout](https://arxiv.org/abs/2607.01418) of Claude Code and GitHub Copilot CLI found that "first use spread primarily through social networks". To move a team past the ceiling, someone has to show them, not just tell them.

### Diagnose your own ceiling

| Symptom | What's missing | Where it's taught |
|---|---|---|
| You paste the same background into new sessions | A context loop: instruction files and a knowledge base | [Module 04](../04-context-is-infrastructure/README.md) |
| You run the tests yourself after the agent says "done" | Verification the agent runs on its own | [Module 03](../03-close-the-loop/README.md) |
| You write long "perfect prompts" | Context and conversation, not more words | [Module 02](../02-one-agent-done-well/README.md) |
| You watch the agent work because there's nothing else to do | Work decomposed into independent tracks | [Modules 05](../05-decompose-into-tracks/README.md) and [06](../06-run-sessions-in-parallel/README.md) |
| You read every diff line by line with the same attention | Review tiered by risk, with agents reviewing first | [Module 07](../07-agents-review-agents/README.md) |
| You hit plan limits and don't know what the tokens bought | A cost-per-outcome view | [Module 08](../08-token-economics/README.md) |

## The practice is converging

People who don't work together are arriving at a similar way of working. Details and caveats differ; the shape repeats.

- **DHH** ([Lex Fridman Podcast #501](https://lexfridman.com/dhh-2/)) works with agents in terminal tools, has one vendor's model do the work and another review it ("It's my favorite checker. It keeps finding stuff."), and keeps the final decision. His caveats matter as much: he still reviews the shape of all the code and the individual lines of critical parts, finds large products "surprisingly tricky to fully accelerate with agents", and calls his pace "not sustainable at all".
- **Peter Steinberger** ([The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/the-creator-of-clawd-i-ship-code)) runs five to ten agents on a project he mostly works on alone, and names the core idea: "you have to close the loop. It needs to be able to debug and test itself." His caveat, about running all his agents in one folder: "I usually work alone, if you work in a bigger team that workflow obv won't fly" ([Shipping at Inference-Speed](https://steipete.me/posts/2025/shipping-at-inference-speed)).
- **Andrej Karpathy** frames why verification is the lever: "LLMs and reinforcement learning automate what you can verify" ([Sequoia Ascent 2026](https://karpathy.bearblog.dev/sequoia-ascent-2026/)).
- **Simon Willison** is collecting the patterns in public, from red/green TDD to subagents, in his [Agentic Engineering Patterns guide](https://simonwillison.net/guides/agentic-engineering-patterns/).
- **The vendors' guidance** agrees. The [Claude Code best practices](https://code.claude.com/docs/en/best-practices) open with "Give Claude a way to verify its work" and describe a writer/reviewer split with fresh context. The [Codex best practices](https://learn.chatgpt.com/guides/best-practices) recommend planning complex work, a short and accurate AGENTS.md, and worktrees for parallel tasks.

The shared elements map onto this guide: the agent verifies its own work (modules 02–03), context lives in the repository (04), work splits into isolated tracks (05–06), another agent reviews (07), and humans own decisions and merges (09).

But convergence among early adopters is a signal, not proof. Most of these voices are experienced engineers, often working alone or on products they own: a kinder setting than a large team on a ten-year-old codebase with strict compliance rules.

## From writing lines to designing the system

When agents write most of the code, your job doesn't disappear. It moves.

> "I don't have a line by line code understanding. That's, that's what Codex does for me, but I'm the architect" — Peter Steinberger on [The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/the-creator-of-clawd-i-ship-code)

DHH uses a different image: a master whose studio of students does the chiseling while he says when the proportions are wrong. That includes telling agents something they rarely do on their own: "you actually do have to tell them, 'Make it simpler.'"

What stays human, in every account we trust:

- **Product judgment.** DHH: "They're bottlenecked on ideas. They're bottlenecked on vision. They're bottlenecked on taste."
- **Coherence.** Many agent changes, each reasonable alone, can erode an architecture. [Module 09](../09-teams-and-organizations/README.md) shows a real case.
- **Verification design and decisions at the gates.** What "correct" means; who accepts plans, merges and runs privileged commands.
- **Understanding.** Enough of it to tell when the agent is wrong.

> [!NOTE]
> **At The Agile Monkeys**, engineers who work this way describe their day as conversations, not prompts. They plan inside a session that already holds the project's context, ask the agent to turn the plan into issues, and ask it to explain what it will do before a task runs. Their time goes to accepting plans, deciding and reviewing, not to typing code.

This shift isn't good news for everyone. DHH puts it bluntly: "you're gonna have a hard time coping with the new reality if the only thing you loved about programming was the mechanical bits". Steinberger found the opposite about himself: "I always thought I liked coding, but really I like building." Many engineers loved both, and the craft is still there when you want it.

It is also more tiring than it looks. Willison calls running several agents "surprisingly effective, if mentally exhausting", and [module 06](../06-run-sessions-in-parallel/README.md) treats sustainability as part of the practice.

## What the evidence says, honestly

Enthusiasm is easy to find; solid evidence is not. Here is what the main studies found, with their limits.

**METR, 2025: experienced developers were slower, and believed they were faster.** In a [randomized controlled trial](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/), 16 experienced open-source developers did 246 real tasks in repositories they knew well, with early-2025 tools. With AI allowed, they took **19% longer**. They had expected to be 24% faster, and afterwards still believed they had been 20% faster. METR stresses that this doesn't show AI fails to speed up most developers. It shows something narrower and more uncomfortable: their sense of their own speed was wrong.

**METR, 2026 follow-up: probably faster now, but the study design broke.** In a [follow-up](https://metr.org/blog/2026-02-24-uplift-update/), returning developers took an estimated 18% less time with AI (confidence interval: 38% less to 9% more) and new developers 4% less (15% less to 9% more). Both point to a speedup; neither is statistically significant. Selection effects were serious: some developers wouldn't join because they didn't want to work without AI, 30% to 50% avoided submitting tasks they wanted AI for, and timings were unreliable for people running several agents at once. METR is redesigning the study.

**DORA 2025: AI amplifies what's already there.** The [DORA report](https://dora.dev/dora-report-2025/), from nearly 5,000 technology professionals, found about 90% use AI and over 80% say it made them more productive, yet 30% have little or no trust in AI-generated code. AI adoption is now linked to higher delivery throughput, and still to higher instability. In DORA's words: "AI's primary role is as an amplifier, magnifying an organization's existing strengths and weaknesses." The capabilities it says make AI pay off include small batches, strong version control and AI-accessible internal data.

**Faros AI 2025: individuals speed up, organizations don't (yet).** [Faros AI](https://www.faros.ai/blog/ai-software-engineering), a vendor analyzing data from over 10,000 developers, found that high-adoption teams completed 21% more tasks and merged 98% more pull requests, while review time rose 91%, PR size 154% and bugs per developer 9%, with no significant improvement at company level. It is correlational and vendor-run, but the pattern is plausible: the bottleneck moves to review.

**Microsoft 2026: more merged pull requests, sustained.** The [study of Microsoft's rollout](https://arxiv.org/abs/2607.01418) followed tens of thousands of engineers: adopters merged roughly 24% more pull requests than they otherwise would have, sustained over four months. The authors' caveat: "a merged PR is not the same as the value it delivers". It is a preprint.

### Why the results differ

- **Setting.** METR 2025 studied experts on large, mature repositories they knew intimately: where humans are strongest and implicit knowledge matters most.
- **Era.** Karpathy observed that coding agents "basically didn't work before December and basically work since" ([as quoted by Simon Willison](https://simonwillison.net/2026/Feb/26/andrej-karpathy/)), meaning December 2025.
- **Setup and skill.** An agent that can run the tests and has context behaves very differently from one that can't, and people in their first weeks differ from people in their second year. Few studies record either.
- **What's measured.** Time per task, pull requests, incidents and business value are different things. Self-reports are the weakest measure of all.
- **The rest of the system.** Individual gains vanish if review, CI and deployment can't absorb more changes (Faros, DORA).

The practical lesson for you: don't trust your feeling of speed, and don't trust anyone's headline number, including ours. Measure yourself before and after, with outcomes. That is [lab 1](lab.md).

### Our own numbers, and why they aren't benchmarks

> [!NOTE]
> **At The Agile Monkeys**, on our internal operations platform, engineers working the way this guide describes resolve on the order of **five stories per person per day**. The project reached **issue #1000 in about three months**. Several engineers hit the limits of **two top-tier subscriptions, one per vendor**, most weeks. *These numbers are indicative, not benchmarks.*

They compare apples to oranges, and here is why:

- Our stories are written by agents, so they tend to be smaller and more numerous than hand-written ones. Counting them favors us.
- It is an internal tool with a limited number of users, a kinder setting than a public product with strict uptime requirements.
- There is no control group.
- The subscription usage includes automated review and knowledge-base maintenance, not only coding, and not all of it was useful. That spend needs optimizing too ([module 08](../08-token-economics/README.md)).

Treat them as a reference point that this way of working is possible, not as a target.

## Other ways to see it

**"One agent is enough."** [Mitchell Hashimoto](https://mitchellh.com/writing/my-ai-adoption-journey) describes a careful path (drop the chatbot, reproduce your own work with an agent, turn every agent mistake into harness, always have one agent running), keeps notifications off because "Context switching is very expensive", and doesn't run multiple agents. [Simon Willison](https://simonwillison.net/2025/Oct/5/parallel-coding-agents/) can only focus on reviewing and landing one significant change at a time. Both are right about the cost: parallel work is limited by review and attention, not by how many agents you can start.

**"Don't chase the frontier."** DHH's advice to anxious developers: "Don't try to anticipate anything. You will literally go crazy." He also expects vendors to absorb most of the custom orchestration people build today.

**What we do.** We run many sessions, because in our work the leverage is real. But we treat parallelism as the last step, earned by verification and context, and we design the outer loop around protecting human attention. If your measurements show that two sessions is your best setup, that is a good result, not a failure.

## Watch out

- ❌ **Measuring lines of code or number of agents.** DHH: "lines of code is a stupid metric in general". ✅ Measure merged pull requests, cycle time, rework (merged pull requests that needed a follow-up fix or revert within 7 days), human minutes per pull request and cost per merged pull request.
- ❌ **Trusting your feeling of speed.** The METR developers misjudged their own speed by roughly 40 points. ✅ Log a real week before you change anything.
- ❌ **Scaling before verification.** More pull requests through the same review process turn review into the queue. ✅ Make the agent check its own work first.
- ❌ **Vibe coding a shared codebase.** DHH describes a product where letting people "vibe" produced "a lot of PRs that individually perhaps could have been justified for a hot moment, but taken all together, destroyed the architecture of the system." ✅ Keep someone accountable for the shape of the system.
- ❌ **Building your own orchestration platform before shipping anything.** Steinberger calls it "the agentic trap". ✅ Start with plain sessions, worktrees and tests.
- ❌ **Ignoring the human cost.** More output can mean more exhaustion. ✅ Decide your working hours before the agents decide them for you.

The difference between chatbot and system shows up even in a single prompt:

❌ **Weak prompt**

```text
add csv export to shelf
```

✅ **Better prompt**

```text
Implement issue #4 (read it with gh issue view 4). Write the tests first and
show me they fail, then implement. Run python -m unittest and paste the output.
If something can't run, tell me exactly what didn't run and why.
Open a pull request that closes #4.
```

The better prompt is short because it leans on a system: an issue that already holds the specification, tests the agent can run, and a pull request where the result will be reviewed.

## Check your understanding

1. A colleague says: "I do agentic engineering. The agent writes everything and I never look at the code." What would DHH call that, and what is missing according to Karpathy and Osmani?

   <details><summary>Answer</summary>

   By DHH's definition, not looking at the implementation is vibe coding. Karpathy and Osmani both tie agentic engineering to keeping the professional quality bar: someone owns architecture, quality and correctness. Not reading every line can be fine; having no system that makes the result trustworthy (verification, review by risk, a person accountable for the design) is what's missing.

   </details>

2. METR's 2025 study found experienced developers were 19% slower with AI. Give two reasons the result may not transfer to you, and one reason to take it seriously anyway.

   <details><summary>Answer</summary>

   It may not transfer because it used early-2025 tools, and because it studied experts on large repositories they knew intimately, the setting where humans have the biggest advantage. Take it seriously anyway because the developers believed they were faster while they were slower: your feeling of speed is not evidence.

   </details>

3. Faros AI found 98% more merged pull requests but 91% longer review time and no company-level improvement. What does that suggest you invest in next?

   <details><summary>Answer</summary>

   In what happens after the code is written: agents verifying their own work, smaller pull requests, automated review before human review, and review tiered by risk. Without that, more output just moves the queue to review.

   </details>

4. You notice that you re-explain the project at the start of most sessions. Which loop is missing, and where is it taught?

   <details><summary>Answer</summary>

   The context loop: instruction files and a knowledge base that every new session loads. It is taught in module 04.

   </details>

5. Why do we call our own numbers "apples to oranges"?

   <details><summary>Answer</summary>

   Because stories written by agents are smaller and more numerous, the setting is an internal tool with few users, there is no control group, and subscription usage includes review and knowledge-base work that isn't all useful. They show the practice is possible; they are not a benchmark.

   </details>

## Key points

- Agentic engineering means agents write most of the code while humans design the system around them: context, decomposition, verification, review and decisions.
- Vibe coding, in DHH's definition, means nobody looks at the implementation. Some authors use the term differently, so check the meaning.
- It's easy to stay at "one window, one prompt, one task", and the gap with those who go further keeps widening because their setup compounds. It also closes fast: the practices take weeks to learn, not years.
- The role shifts from writing lines to architect and editor. Product judgment, coherence, verification design, gate decisions and understanding stay human.
- The evidence is mixed: people misjudge their own speed, AI amplifies existing strengths and weaknesses, and individual gains can vanish in review.
- Numbers, ours included, are indicative. Measure your own before and after.

## Go further

- [Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/) by Simon Willison: short, practical pattern essays, kept up to date.
- [Sequoia Ascent 2026](https://karpathy.bearblog.dev/sequoia-ascent-2026/) by Andrej Karpathy: vibe coding versus agentic engineering, and why verifiability matters.
- [Augmented Coding: Beyond the Vibes](https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes) by Kent Beck: caring about code quality while an agent types.
- [Agentic Engineering](https://addyosmani.com/blog/agentic-engineering/) by Addy Osmani: why testing is the biggest differentiator.
- [METR's 2025 study](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) and [2026 update](https://metr.org/blog/2026-02-24-uplift-update/): the most careful attempt to measure speed, including what went wrong.
- [DORA State of AI-assisted Software Development 2025](https://dora.dev/dora-report-2025/): the capabilities that make AI pay off at team level.
- [How to Build an Agent](https://ampcode.com/notes/how-to-build-an-agent) by Thorsten Ball: an agent is a model, a loop and a few tools. Reading it removes the magic.
- [My AI Adoption Journey](https://mitchellh.com/writing/my-ai-adoption-journey) by Mitchell Hashimoto: a thoughtful counterweight to "more agents is better".

Next: [2. One agent, done well](../02-one-agent-done-well/README.md)
