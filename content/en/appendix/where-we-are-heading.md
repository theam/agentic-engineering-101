---
title: "Where we are heading"
kind: appendix
last_reviewed: 2026-09-17
---

# Where we are heading

This appendix is different from the rest of the guide. It's about the direction The Agile Monkeys is taking this practice, including two projects we are building.

> [!IMPORTANT]
> **You don't need either project to apply this guide.** Everything in modules 00–10 works with a terminal, git, a coding agent and a paid plan. Other approaches exist too, and we list some at the end.

## The practice in this guide runs on laptops

Look at what the guide has asked you to set up:

- terminals and a session manager, with sessions grouped by track;
- local repositories and git worktrees, one per track;
- a knowledge base of Markdown files in a git repository, loaded by each session;
- hooks and validators running on your machine;
- review loops driven from your own sessions;
- a subscription per person, sometimes two.

That setup is a good place to start. It's cheap, everything is plain text in git, you can inspect every piece, and you can undo any of it. For one engineer, or a small team, it may be all you ever need.

## Where it hits its limits

When we run this practice every day across a team, the same limits keep showing up:

- **One machine.** Full local stacks run out of memory at around five or six on a laptop (module 06). When the laptop sleeps, the sessions stop. After a restart, working out which session was doing what is slow and error-prone.
- **One person's attention.** Sessions report to whoever launched them. A teammate can't see your tracks in flight or steer one while you're away. A handoff needs a handoff pack.
- **Context that lives in one repository.** The knowledge base is a git repository that teammates must clone and query through their own agents. Meeting transcripts, documents and decisions only get in when someone brings them in.
- **Hard to share.** Skills, rules and guards get copied from repository to repository and drift apart.
- **Hard to audit.** The evidence exists, but it's scattered across local session logs, PR threads, CI runs and chat. Answering "who accepted this plan, which model wrote this change, and what did it cost?" takes archaeology. That's the regulated-industries question from module 09.
- **Credentials next to agents.** Laptop sessions run beside a person's own credentials, which is exactly the situation the s1ngularity attack exploited (module 09).
- **Accounts built for one person.** Subscriptions and usage limits are per person, and people discover that a machine is set up for one account (module 08).

None of these stop an individual from working this way. They're what gets in the way when a team wants to share context, see work in flight and show what happened.

## Direction 1: the knowledge base in the cloud

**ProductPlot** (productplot.ai) is in development. It's a shared product knowledge base that connects source material, decisions and delivery planning. People's own agents read and maintain it through MCP. The agents and subscriptions from this guide keep doing the work, but the knowledge lives in one shared place instead of one repository per person or team.

It targets two limits above: context that lives in one repository, and knowledge that is hard to share across a team.

It's early. We aren't listing features here because they are still changing. When there is something you can try, this appendix will say so.

## Direction 2: agent execution in the cloud

**[Facility](https://github.com/theam/facility)** is our vision of how a team works with agents across the delivery lifecycle: open-source (Apache 2.0), self-hosted tooling for running coding agents as part of a reviewable delivery process. Its repository describes it in detail. In short:

- You connect GitHub repositories, and their issues become **stories**.
- A story is a durable unit of work. It has one shared conversation that people and agents continue, one persistent workspace with the development environment the repository declares, resumable Claude Code or Codex sessions, and an ordinary branch and pull request.
- **Agents are defined in the repository** as Markdown files: prompt, engine, model and triggers (manual, the web application, MCP, GitHub events or a schedule). The starter set covers delivery roles: architect, builder, PR reviewer, review addresser, CI doctor and security audit.
- People steer the conversation and test the running result through authenticated previews. Agents deliver through normal branches and pull requests. **The repository's own gates stay the boundary:** protected branches, required CI, required reviews and a human decision to merge.
- Each agent turn records the agent, model, session and Git state before and after, linked to the resulting PRs, reviews and checks. Costs are attributed per project and agent, and monthly project budgets are checked before new model calls.

Here's how that maps to the guide. The worktrees and session juggling from module 06 become persistent workspaces that don't depend on one laptop. The human gates from module 09 stay in the repository. Cost per merged PR (module 08) and the audit evidence (module 09) are recorded as the work happens, instead of reconstructed afterwards.

What you should know before you look at it:

- **It's pre-1.0.** Its schema, APIs, agent manifests and deployment shape may change between `0.x` releases, and no upgrade path between them is promised.
- **It's young in production.** In its own words: "Facility runs the delivery of the team that builds it, and nowhere else yet." ([Facility README](https://github.com/theam/facility#readme))
- **Its trust model is a deliberate trade-off.** Every agent gets the same maintainer-level access to its workspace and the project's repositories. There are no per-agent permission profiles, and merge controls are the boundary. That is the "one trust model" option from module 09, not per-agent least-privilege identities. Its README advises pointing it at repositories "where a bad agent pull request is an inconvenience rather than an incident", and reading its security model and hardening notes before anything else.
- **You operate it.** Self-hosting means running its database, workers, GitHub App and workspace images.

## What moving to the cloud doesn't change

Neither project replaces the practice. You still need issues that work as prompts, checks an agent can run, decomposition into tracks, review that closes by decision and humans at the gates. Moving execution or knowledge off a laptop changes where things run and who can see them. It doesn't make a weak practice strong. As the [DORA 2025 report](https://dora.dev/dora-report-2025/) says of AI in general, it amplifies what's already there, good or bad.

## Other ways to get there

- **Hosted agents from the vendors.** The major coding-agent vendors offer cloud sessions, background tasks and scheduled or event-triggered agents. The [tools reference](../reference/tools.md) lists what we use and links the official docs.
- **Agents in your own CI.** Run an agent headless on issue or pull request events, for example with [Claude Code GitHub Actions](https://code.claude.com/docs/en/github-actions), and keep your existing gates.
- **Open-source orchestrators and session managers.** Several tools manage worktrees and parallel sessions for you (module 06).
- **Wait.** [DHH expects the big labs to absorb most of this](https://lexfridman.com/dhh-2-transcript): "We're not all gonna have to build our own coordination harnesses." He may well be right, and that's a good reason not to build your own unless you need to.
- **Stay on laptops.** For individuals and small teams, the practice in this guide is enough.

## Help us get this right

We're building in the open because we'd rather be corrected early. If you've hit these limits and solved them another way, or you think we've drawn them wrong, [tell us](../../../CONTRIBUTING.md). Feedback on Facility is welcome in [its issue tracker](https://github.com/theam/facility/issues).
