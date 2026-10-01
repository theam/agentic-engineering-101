---
title: "Sources"
kind: reference
last_reviewed: 2026-09-17
---

# Sources

Every external source this guide draws on, grouped by kind. Each entry gives the title, the author or organization, the date, and one line on why it matters. Links were checked on 2026-09-17.

Two notes before you use this list:

- **Dates matter.** Advice about coding agents ages fast. A workflow from mid-2025 was designed for weaker models than a workflow from 2026, and some authors changed their minds between posts (we point it out where we know).
- **Vendors and practitioners have interests.** Vendor posts describe their own products, and famous practitioners work in unusual conditions (solo projects, unmetered tokens). We cite them because they are useful, not because they are neutral.

Our own practice, described throughout the guide as "At The Agile Monkeys", is not listed here: it comes from our internal work, and we mark our numbers as indicative.

> [!TIP]
> Know a source that should be here, or found a broken link? Open a pull request that adds it with the same format. [CONTRIBUTING.md](../../../CONTRIBUTING.md) explains how.

## Podcasts and talks

- **[DHH: Future of Programming, AI, Agentic Engineering, Vibe Coding & Linux](https://lexfridman.com/dhh-2/)** — Lex Fridman Podcast #501 with David Heinemeier Hansson, 2026-08-26 ([transcript](https://lexfridman.com/dhh-2-transcript)). A detailed agent-first workflow (no IDE, one vendor builds and another reviews, humans on decisions) with honest caveats about big codebases and sustainability.
- **[The creator of Clawd: "I ship code I don't read"](https://newsletter.pragmaticengineer.com/p/the-creator-of-clawd-i-ship-code)** — The Pragmatic Engineer podcast, Gergely Orosz with Peter Steinberger, 2026-01-28 ([video](https://www.youtube.com/watch?v=8lF7HmQ_RgY)). The source for "close the loop", blast radius and running 5 to 10 agents, plus the host's warning that it is a solo, "YOLO" project.
- **[OpenClaw: The Viral AI Agent that Broke the Internet (transcript)](https://lexfridman.com/peter-steinberger-transcript/)** — Lex Fridman Podcast #491 with Peter Steinberger, 2026-02. The follow-up prompts we use ("read more code", "what would you have done differently") and his warning about building tooling instead of shipping.
- **[DHH's new way of writing code](https://newsletter.pragmaticengineer.com/p/dhhs-new-way-of-writing-code)** — The Pragmatic Engineer podcast, Gergely Orosz with David Heinemeier Hansson, 2026-04-08. An earlier stage of the same shift, including why senior engineers benefit more today.
- **[Sequoia Ascent 2026 summary](https://karpathy.bearblog.dev/sequoia-ascent-2026/)** — Andrej Karpathy, 2026-04-30 (his summary of the talk). "LLMs can automate what you can verify", and a line he quotes and keeps returning to: you can outsource your thinking, but not your understanding.

## Essays and guides

### What agentic engineering is

- **[Post on X naming "agentic engineering"](https://x.com/karpathy/status/2019137879310836075)** — Andrej Karpathy, 2026-02-04. Separates vibe coding from professional work with agents "with more oversight and scrutiny".
- **[A quote from Andrej Karpathy](https://simonwillison.net/2026/Feb/26/andrej-karpathy/)** — Simon Willison, 2026-02-26. Records Karpathy's observation that coding agents basically started working at the end of 2025, which explains why older advice ages.
- **[Vibe engineering](https://simonwillison.net/2025/Oct/7/vibe-engineering/)** — Simon Willison, 2025-10-07. Agents amplify existing expertise; tests, planning, documentation and review culture matter more, not less.
- **[Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/)** — Simon Willison, ongoing guide started 2026-02-23. Short pattern essays and annotated prompts; the model for our [prompt patterns](prompt-patterns.md) page. Chapters we cite: [Red/green TDD](https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/) and [First run the tests](https://simonwillison.net/guides/agentic-engineering-patterns/first-run-the-tests/).
- **[Agentic Engineering](https://addyosmani.com/blog/agentic-engineering/)** — Addy Osmani, 2026-02-04. A clear contrast with vibe coding, and the argument that testing is the biggest differentiator.
- **[Augmented Coding: Beyond the Vibes](https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes)** — Kent Beck, 2025-06-25. TDD and "tidy first" with agents, and the warning signs of an agent going off track (loops, unrequested features, deleted tests).
- **[Vibe Coding: Production-Grade Software with AI](https://itrevolution.com/product/vibe-coding-book/)** (book) — Gene Kim and Steve Yegge, IT Revolution, 2025-10-21. Uses "vibe coding" for serious production work, unlike Karpathy and Willison; read with that difference in mind.
- **[The Three Developer Loops: A New Framework for AI-Assisted Coding](https://itrevolution.com/articles/the-three-developer-loops-a-new-framework-for-ai-assisted-coding/)** — Leah Brown on Gene Kim and Steve Yegge's framework, IT Revolution, 2025-10-20. The inner, middle and outer loops that our own spine adapts.

### How practitioners work

- **[Just Talk To It: the no-bs Way of Agentic Engineering](https://steipete.me/posts/just-talk-to-it)** — Peter Steinberger, 2025-10-14. Short prompts, blast radius, atomic commits in one folder, and ~800 lines of agent-written `AGENTS.md`.
- **[Shipping at Inference-Speed](https://steipete.me/posts/2025/shipping-at-inference-speed)** — Peter Steinberger, 2025-12-28. CLI-first design so agents close the loop, why he avoids worktrees (and his caveat that it won't work in bigger teams), and plan mode as a "hack".
- **[My Current AI Dev Workflow](https://steipete.me/posts/2025/optimal-ai-development-workflow)** — Peter Steinberger, 2025-08-25. An earlier workflow built on plan mode; useful to see how advice changes with model generations.
- **[Just One More Prompt](https://steipete.me/posts/just-one-more-prompt)** — Peter Steinberger, 2025-08-19. An honest account of the "slot machine" pull of agents and its effect on sleep.
- **[Promoting AI agents](https://world.hey.com/dhh/promoting-ai-agents-3ee04945)** — David Heinemeier Hansson, 2026-01-07. His position before the shift: far from agents writing most of his code.
- **[Let the agents democratize open source](https://world.hey.com/dhh/let-the-agents-democratize-open-source-9fd630a9)** — David Heinemeier Hansson, 2026-06-01. Argues against banning AI contributions, while admitting slop is a problem.
- **[Thread on X about his setup](https://x.com/bcherny/status/2007179832300581177)** — Boris Cherny, creator of Claude Code, 2026-01-02. A "surprisingly vanilla" setup: parallel sessions, plan mode first, and giving the agent a way to verify its work.
- **[Thread on X with tips from the Claude Code team](https://x.com/bcherny/status/2017742741636321619)** — Boris Cherny, 2026-01-31. Worktrees as the biggest productivity unlock, a second agent reviewing plans, and updating `CLAUDE.md` after every correction.
- **[Anthropic's Claude Code creator says he manages tens of thousands of AI agents at once](https://fortune.com/2026/06/08/anthropics-boris-cherny-creator-of-claude-code-says-there-are-days-he-manages-tens-of-thousands-of-ai-agents-at-once/)** — Fortune, 2026-06-08. Scale claims from an insider with effectively unmetered tokens; context, not a target.
- **[My AI Adoption Journey](https://mitchellh.com/writing/my-ai-adoption-journey)** — Mitchell Hashimoto, 2026-02-05. A strong counterweight: one agent at a time, notifications off, and "harness engineering" after every mistake.
- **[Embracing the parallel coding agent lifestyle](https://simonwillison.net/2025/Oct/5/parallel-coding-agents/)** — Simon Willison, 2025-10-05. Which tasks parallelize well, and why reviewing one significant change at a time is the real limit.
- **[The Code Agent Orchestra: what makes multi-agent coding work](https://addyosmani.com/blog/code-agent-orchestra/)** — Addy Osmani, 2026-03-26. From conductor to orchestrator: subagents, agent teams and cloud agents, with decomposition and verification as the bottlenecks.
- **[Gas Town](https://yegge.ai/gastown)** — Steve Yegge, 2026-01. An experimental extreme: orchestrating dozens of agents with a merge queue. Useful to see where the ceiling is, not a starting point.
- **[My LLM codegen workflow atm](https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/)** — Harper Reed, 2025-02-16. The "ask me one question at a time" spec interview, then a plan and small tested steps.
- **[Agentic Coding Recommendations](https://lucumr.pocoo.org/2025/6/12/agentic-coding/)** — Armin Ronacher, 2025-06-12. Simple stacks, fast tools, logs agents can read, and skipping permissions only inside a container.
- **[How to Build an Agent](https://ampcode.com/notes/how-to-build-an-agent)** — Thorsten Ball, 2025-04-15. An agent is a model, a loop and a few tools in a few hundred lines; the best way to demystify what you are running.

### Verification, review and security

- **[The lethal trifecta for AI agents: private data, untrusted content, and external communication](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)** — Simon Willison, 2025-06-16. Private data, untrusted content and external communication together make exfiltration possible.
- **[Ralph Wiggum as a "software engineer"](https://ghuntley.com/ralph/)** — Geoffrey Huntley, 2025-07-14. The original "run the same prompt in a loop" technique, with tests and types as back-pressure.
- **[Superpowers: How I'm using coding agents in October 2025](https://blog.fsck.com/2025/10/09/superpowers/)** — Jesse Vincent, 2025-10-09. A skills library that enforces brainstorm, plan, worktrees, TDD and review between tasks: a heavier process worth comparing with ours.
- **[Agentic Code Review](https://addyosmani.com/blog/agentic-code-review/)** — Addy Osmani, 2026-06-15. Tier review by risk, ask for evidence first, scrutinize rewritten tests; humans own merges.
- **[How Anthropic secures its AI-native software development lifecycle](https://claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle)** — Jason Clinton, Anthropic, 2026-07-21. Scoped review agents, risk-weighted human review, least-privilege agent identities. A vendor describing itself.
- **[S1ngularity: What Happened, How We Responded, What We Learned](https://nx.dev/blog/s1ngularity-postmortem)** — Nx, 2025-08 (with [Wiz's analysis](https://www.wiz.io/blog/s1ngularity-supply-chain-attack)). A supply-chain attack that used installed AI CLIs with permission-bypass flags to hunt for secrets.
- **[How we built Claude Code auto mode: a safer way to skip permissions](https://www.anthropic.com/engineering/claude-code-auto-mode)** — Anthropic Engineering, 2026-03-25. Why approval fatigue makes manual prompts weak protection, and the limits of a classifier.
- **[Making Claude Code more secure and autonomous with sandboxing](https://www.anthropic.com/engineering/claude-code-sandboxing)** — Anthropic Engineering, 2025-10-20. Filesystem plus network isolation, and the internal drop in permission prompts.

### Context, specs and harnesses

- **[Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)** — Anthropic Engineering, 2025-09-29. Smallest high-signal context, just-in-time retrieval, compaction, notes and subagents.
- **[Building effective agents](https://www.anthropic.com/research/building-effective-agents)** — Anthropic, 2024-12-19. Start simple; the evaluator-optimizer pattern is the writer/reviewer loop under another name.
- **[How Anthropic teams use Claude Code](https://claude.com/blog/how-anthropic-teams-use-claude-code)** — Anthropic, 2025-07-24. Autonomous loops for peripheral work, close supervision for core logic, and starting from a clean git state.
- **[Advanced Context Engineering for Coding Agents](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md)** — HumanLayer, 2025-08. Research, plan, implement with intentional compaction; review research and plans hardest.
- **[12-Factor Agents](https://github.com/humanlayer/12-factor-agents)** — HumanLayer, living repository. Own your context window; build small, focused agents.
- **[Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)** — Birgitta Böckeler, martinfowler.com, 2025-10-15. A critical look at spec-first tools and the false sense of control they can give.
- **[Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/)** — OpenAI, 2026-02-11 (summary on [InfoQ](https://www.infoq.com/news/2026/02/openai-harness-engineering-codex)). A short `AGENTS.md` as a table of contents, the repository as system of record, mechanical enforcement. A vendor's greenfield experiment.

### Writing and teaching

- **[Patterns in confusing explanations](https://jvns.ca/blog/confusing-explanations/)** — Julia Evans, 2021-08-19. The style this guide follows: concrete examples first, explain why, label wrong approaches.

## Official documentation

Tool home pages (terminals, session managers, sandboxes) are listed with context in [Tools](tools.md). All of these are living documents; the date is when we last checked them.

### Claude Code (Anthropic), checked 2026-09-17

- [Overview](https://code.claude.com/docs/en/overview), [Best practices](https://code.claude.com/docs/en/best-practices) and [Glossary](https://code.claude.com/docs/en/glossary): the official workflow (explore, plan, implement, commit), verification and context management.
- [Memory](https://code.claude.com/docs/en/memory): `CLAUDE.md`, importing `AGENTS.md`, auto memory.
- [Hooks](https://code.claude.com/docs/en/hooks), [Permission modes](https://code.claude.com/docs/en/permission-modes), [Sandboxing](https://code.claude.com/docs/en/sandboxing) and [Security](https://code.claude.com/docs/en/security): deterministic guardrails and safe autonomy.
- [Worktrees](https://code.claude.com/docs/en/worktrees), [Agent view](https://code.claude.com/docs/en/agent-view), [Agent teams](https://code.claude.com/docs/en/agent-teams), [Subagents](https://code.claude.com/docs/en/sub-agents) and [Sessions](https://code.claude.com/docs/en/sessions): running work in parallel.
- [Non-interactive mode](https://code.claude.com/docs/en/headless), [Goal](https://code.claude.com/docs/en/goal) and [Routines](https://code.claude.com/docs/en/routines): unattended runs.
- [Code Review](https://code.claude.com/docs/en/code-review) and [GitHub Actions](https://code.claude.com/docs/en/github-actions): automated pull request review.
- [Costs](https://code.claude.com/docs/en/costs): typical spend, and practical ways to reduce token use.

### Codex (OpenAI), checked 2026-09-17

- [Best practices](https://learn.chatgpt.com/guides/best-practices): prompt structure (goal, context, constraints, done when), short `AGENTS.md`, planning and review.
- [Codex CLI](https://learn.chatgpt.com/docs/codex/cli), [Commands and options](https://learn.chatgpt.com/docs/developer-commands?surface=cli) and [Non-interactive mode](https://learn.chatgpt.com/docs/non-interactive-mode).
- [AGENTS.md in Codex](https://learn.chatgpt.com/docs/agent-configuration/agents-md): how instruction files are discovered and combined.
- [Code review](https://learn.chatgpt.com/docs/code-review) and [Review GitHub pull requests with Codex](https://learn.chatgpt.com/docs/third-party/github).
- [Sandbox](https://learn.chatgpt.com/docs/sandboxing) and [Permissions](https://learn.chatgpt.com/docs/permission-modes).

### Standards and other tools

- [AGENTS.md](https://agents.md/) — Agentic AI Foundation (Linux Foundation). The open format for agent instructions.
- [Model Context Protocol](https://modelcontextprotocol.io/) — the open standard for connecting AI applications to tools and data.
- [Agents in VS Code](https://code.visualstudio.com/docs/agents/overview), [Copilot cloud agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent) and [Copilot code review](https://docs.github.com/en/copilot/concepts/agents/code-review) — GitHub and Microsoft.
- [git worktree](https://git-scm.com/docs/git-worktree) — Git project. The primitive behind every parallel-session tool.
- [GitHub CLI](https://cli.github.com/) — GitHub. How agents read and write issues and pull requests from the terminal.
- [Spec Kit](https://github.com/github/spec-kit) — GitHub; and [Kiro specs](https://kiro.dev/docs/specs/) — Kiro. Spec-driven workflows with a human approval per phase, for comparison.

## Research and data

- **[Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)** — METR, 2025-07-10. In a randomized trial, experienced developers were 19% slower with AI while believing they were faster. Read METR's own limits on what it shows.
- **[We are Changing our Developer Productivity Experiment Design](https://metr.org/blog/2026-02-24-uplift-update/)** — METR, 2026-02-24. The follow-up points to a speedup, but METR calls it very weak evidence, partly because developers refused to work without AI.
- **[Task Substitution and Uplift](https://metr.org/blog/2026-05-08-task-substitution-and-uplift/)** — METR, 2026-05-08. People shift toward tasks AI made cheap, so per-task speedups overstate value.
- **[Measuring the Self-Reported Impact of Early-2026 AI on Technical Worker Productivity](https://metr.org/blog/2026-05-11-ai-usage-survey/)** — METR, 2026-05-11. A survey of 349 workers; useful, and explicitly self-reported.
- **[State of AI-assisted Software Development 2025](https://dora.dev/dora-report-2025/)** — DORA (Google Cloud), 2025-09-23. AI amplifies what a team already is: more throughput, lower stability without strong practices.
- **[The AI Productivity Paradox Research Report](https://www.faros.ai/blog/ai-software-engineering)** — Faros AI, 2025-07-23. More merged PRs but much longer review times and bigger PRs; vendor data, correlational.
- **[Adoption and Impact of Command-Line AI Coding Agents: A Study of Microsoft's Early 2026 Rollout of Claude Code and GitHub Copilot CLI](https://arxiv.org/abs/2607.01418)** — Emerson Murphy-Hill et al. (Microsoft), arXiv preprint, 2026-07-01. Adoption spread peer to peer; adopters merged about 24% more PRs over four months. PR counts are not value.
- **[Stack Overflow Developer Survey 2025: AI](https://survey.stackoverflow.co/2025/ai)** — Stack Overflow, 2025. "Almost right, but not quite" is developers' top frustration with AI output.
- **[Cost per Shipped Outcome: The Engineering Metric That Makes the AI Budget Conversation Make Sense](https://larridin.com/blog/cost-per-shipped-outcome-engineering-metric)** — Larridin, undated vendor post. The definition of cost per accepted outcome, with the caveat that lower isn't automatically better.
- **[A First Look at Coding Agents' Compliance with AI Contribution Rules in Open-Source Communities](https://arxiv.org/abs/2607.26819)** — Wenhao Yang et al., arXiv preprint, 2026-07-29. Agents almost never look up contribution rules on their own, which is why our `AGENTS.md` restates our AI policy.
- **["We Permit the Use of AI, but \[...\]": The Landscape of AI Policies in Popular Open Source Projects](https://arxiv.org/abs/2609.07542)** — Andre Hora et al., arXiv preprint, 2026-09-07. 281 policies: most permit AI with conditions, many require disclosure.

## Courses

- **[Agentic Coding](https://missing.csail.mit.edu/2026/agentic-coding/)** — MIT, The Missing Semester of Your CS Education, 2026. A university lecture on the same topic, with exercises.
- **[Claude Code: A Highly Agentic Coding Assistant](https://learn.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant)** — DeepLearning.AI, built in partnership with Anthropic. A short hands-on course on one tool.
- **[Anthropic Academy](https://anthropic.skilljar.com/)** — Anthropic. Anthropic's own courses on Claude and Claude Code.
- **[Practical Deep Learning for Coders](https://course.fast.ai/)** — fast.ai. The "whole game first" teaching approach behind our Lab 0.
- **[Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners)** and **[AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)** — Microsoft. Numbered lessons with a fixed skeleton and knowledge checks, a structure we borrowed.
- **[Episode Structure](https://carpentries.github.io/sandpaper-docs/episodes.html)** and **[Live Coding is a Skill](https://carpentries.github.io/instructor-training/17-live.html)** — The Carpentries. Minutes per episode, key points, and workshop techniques our facilitator guide uses.

## Open-source policies and community practice

### AI contribution policies

- **[AI_POLICY.md](https://github.com/ghostty-org/ghostty/blob/main/AI_POLICY.md)** — Ghostty. A short, explicit policy; compare it with [our own AI policy](../../../AI_POLICY.md).
- **[LLVM AI Tool Use Policy](https://llvm.org/docs/AIToolPolicy.html)** — LLVM. A human in the loop, an `Assisted-by:` trailer, and rejection of "extractive contributions".
- **[AI Coding Assistants](https://docs.kernel.org/process/coding-assistants.html)** — Linux kernel documentation. Agents must not add `Signed-off-by`; disclosure through `Assisted-by:`.
- **[Policy on AI-Assisted Contributions](https://docs.fedoraproject.org/en-US/council/policy/ai-contribution-policy/)** — Fedora Council, 2025-10. A project-wide policy: the contributor is accountable for everything they submit, and substantial AI use is disclosed.
- **[On AI use in curl](https://curl.se/dev/contribute.html#on-ai-use-in-curl)** — curl. Disclose AI assistance, keep the quality bar, and expect a ban for fabricated reports.
- **[Use of AI-generated content](https://www.qemu.org/docs/master/devel/code-provenance.html#use-of-ai-generated-content)** — QEMU. The restrictive end of the spectrum: it declines AI-generated contributions because their licensing can't be certified.
- **[open-source-ai-contribution-policies](https://github.com/melissawm/open-source-ai-contribution-policies)** — GitHub user melissawm, living catalog. Many more projects' policies on AI-generated contributions, to compare.

### Open-source tools we maintain

- **[claude-dev-kit](https://github.com/theam/claude-dev-kit)** — The Agile Monkeys, open source. A plugin for Claude Code, Codex and Cursor that takes an issue to a pull request through quality gates. How we work on our laptops ([module 2](../02-one-agent-done-well/README.md)). You don't need it to apply this guide; [Build your own skills](../appendix/build-your-own-skills.md) shows how to write your own.
- **[Facility](https://github.com/theam/facility)** — The Agile Monkeys, open source. Self-hosted tooling to run coding agents inside a reviewable delivery process; our vision of how a team works with agents ([module 9](../09-teams-and-organizations/README.md)). You don't need it to apply this guide; the [appendix](../appendix/where-we-are-heading.md) explains where it fits.

### Building your own skills (appendix)

- **[Agent Skills specification](https://agentskills.io/specification)** — Agent Skills, open standard. The portable `SKILL.md` format that Claude Code and Codex build on.
- **[Claude Code skills](https://code.claude.com/docs/en/skills)**, **[Claude Code plugins](https://code.claude.com/docs/en/plugins)** and **[Codex skills](https://learn.chatgpt.com/docs/build-skills)** — Anthropic and OpenAI. Where skills live, how they're invoked and how to share them.

### How this guide is built

- **[Limina](https://github.com/theam/limina)** — The Agile Monkeys, open source. The research harness our mission repository grew from.
- **[Diátaxis](https://diataxis.fr/)** — Daniele Procida. Tutorials, how-to guides, reference and explanation as separate kinds of content.
- **[The Turing Way](https://github.com/the-turing-way/the-turing-way)** — The Turing Way community. A community handbook with CC BY content, MIT code and CI checks.
- **[The Rust Programming Language](https://doc.rust-lang.org/book/)** — The Rust project. Concept chapters plus project chapters, and marked examples of code that doesn't work.
- **[javascript.info](https://javascript.info/)** — Ilya Kantor and contributors. Tasks with solutions, and translations claimed through tracking issues.
- **[Hello Algo](https://github.com/krahets/hello-algo)** — krahets and contributors. AI-drafted translations reviewed by native speakers for accuracy and fluency.
- **[Site Reliability Engineering](https://sre.google/sre-book/table-of-contents/)** — Google. Principles before practices, and a closing part on teams.
- **[Localizing Kubernetes documentation](https://kubernetes.io/docs/contribute/localization/)** and **[Human-Centered Automation for Kubernetes Localization in the AI Era](https://www.kubernetes.dev/blog/2026/06/26/human-centered-automation-kubernetes-localization-ai-era/)** — Kubernetes, 2026-06-26 for the blog post. Parallel language trees with English as the source of truth.
- **[Lunaria](https://lunaria.dev/)** and **[Starlight internationalization](https://starlight.astro.build/guides/i18n/)** — Lunaria and Astro. Translation status tracking, and a possible future site for this guide.
- **[Contributor Covenant 3.0](https://www.contributor-covenant.org/version/3/0/code_of_conduct/)** — Organization for Ethical Source. Our code of conduct.
- **[Syntax for issue forms](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms)** and **[contributions under repository license](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service#6-contributions-under-repository-license)** — GitHub. How our issue forms work, and why inbound equals outbound licensing needs no CLA.
- **[Creative Commons FAQ](https://creativecommons.org/faq/)** — Creative Commons. Why prose is CC BY and code uses a software license.
- **[markdownlint-cli2-action](https://github.com/DavidAnson/markdownlint-cli2-action)** — David Anson; and **[lychee-action](https://github.com/lycheeverse/lychee-action)** — lychee. The Markdown style and link checks in our CI.
