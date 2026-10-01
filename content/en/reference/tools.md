---
title: "Tools"
kind: reference
last_reviewed: 2026-09-17
---

# Tools

> [!IMPORTANT]
> **Last reviewed: 2026-09-17.** Tools change monthly: flags get renamed, features graduate from preview or disappear. Every command on this page was checked against the official documentation on that date, and every entry links to it. If something here no longer matches the docs, please [open a "tool drift" issue](https://github.com/theam/agentic-engineering-101/issues/new?template=tool-drift.yml) with the link that shows the change.

This page is the dated home for tool detail that changes often. The lessons teach practices that work with any capable coding agent, and use concrete tool examples where they teach a principle, verified against the official docs and linked; this page tells you which buttons implement those practices today.

## Principles: tools change monthly, practices last

1. **Pick tools by the practice they support.** Ask what a tool does for context, verification, isolation or review. A new tool that doesn't improve one of those is a distraction, however good the demo looks.
2. **Use what your agent already has before adding a layer.** Worktrees, background sessions, subagents and review commands are now built into the main agents. Peter Steinberger [warns about the trap](https://steipete.me/posts/just-talk-to-it) of building orchestration instead of shipping, and DHH expects the labs to absorb coordination harnesses ([Lex Fridman Podcast #501](https://lexfridman.com/dhh-2/)).
3. **Keep one contract for every agent.** Put shared instructions in `AGENTS.md`, and keep each tool's own file (such as `CLAUDE.md`) as a thin adapter that points to it. Switching or mixing tools then costs almost nothing.
4. **Use two vendors: one writes, the other reviews.** A reviewer from another vendor doesn't share the writer's blind spots.
5. **Prefer a CLI to an MCP server when both exist.** The [Claude Code cost guide](https://code.claude.com/docs/en/costs) notes that CLI tools such as `gh` are more context-efficient than MCP servers, because they add no tool listings to the context.
6. **Isolate before you grant autonomy.** Never skip permission prompts on a machine that holds credentials. Use a sandbox, a container or a VM first.
7. **Give a new tool a real week.** Compare tools on the same tasks, on your code, with the same verification. First impressions from a toy project mislead.
8. **Trust the docs over this page.** Use the links. When they disagree with what you read here, the docs win and this page needs a drift issue.

## Coding agents

### Claude Code

- **What it is:** Anthropic's coding agent. It reads your codebase, edits files and runs commands. Available in the terminal, IDE extensions, a desktop app and the browser. Instructions come from `CLAUDE.md`; it supports hooks, skills, subagents, MCP and permission modes.
- **When we reach for it:** At The Agile Monkeys it is our main harness for thinking and planning. We open a session in the mission repository and talk through a design; it tends to explain more, which helps us think. We also use it to implement, often through a subagent working in a worktree.
- **Docs:** [Overview](https://code.claude.com/docs/en/overview) · [Best practices](https://code.claude.com/docs/en/best-practices) · [CLI reference](https://code.claude.com/docs/en/cli-reference) · [Commands](https://code.claude.com/docs/en/commands)

### Codex CLI

- **What it is:** OpenAI's coding agent for the terminal. It inspects code, makes changes and runs commands inside a sandbox, and can be scripted with `codex exec`. It reads `AGENTS.md`. Codex also runs in the ChatGPT desktop app, an IDE extension and the cloud. The CLI's source is [on GitHub](https://github.com/openai/codex).
- **When we reach for it:** When a task is well specified and we want the agent to take it and go. We use it a lot as the second-vendor reviewer on pull requests written with Claude Code.
- **Docs:** [Codex CLI](https://learn.chatgpt.com/docs/codex/cli) · [Best practices](https://learn.chatgpt.com/guides/best-practices) · [Commands and options](https://learn.chatgpt.com/docs/developer-commands?surface=cli)

### OpenCode

- **What it is:** An open-source coding agent available as a terminal interface, desktop app or IDE extension. It works with many model providers once you configure their API keys, and its `/init` command creates an `AGENTS.md`.
- **When we reach for it:** We don't use it daily. It is a good option when you want one harness across several model providers, including open-weight models; DHH mentions using it for those.
- **Docs:** [OpenCode documentation](https://opencode.ai/docs)

### GitHub Copilot agents

- **What it is:** GitHub Copilot runs agents in several places: in the VS Code Chat view (the Agent role implements a change; the Plan role proposes an approach first), in the terminal with Copilot CLI, and as a cloud agent on GitHub that works from an issue on its own branch, in an environment powered by GitHub Actions.
- **When we reach for it:** It is not our main agent. It makes sense when a team already lives in VS Code and GitHub and wants agents without adding another vendor. Copilot is also a pull request reviewer (see below).
- **Docs:** [Agents in VS Code](https://code.visualstudio.com/docs/agents/overview) · [Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli) · [About Copilot cloud agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent)

### Cursor

- **What it is:** An AI code editor. Its Agent completes multi-step coding tasks, runs terminal commands and edits code, with checkpoints to roll back changes.
- **When we reach for it:** We don't use it as our main tool, because we work from the terminal. It is a reasonable choice for engineers who want to review diffs inside an editor while agents work. The practices in this guide apply unchanged.
- **Docs:** [Cursor Agent](https://cursor.com/docs/agent/overview)

## Workflow plugins

### claude-dev-kit

- **What it is:** An open-source (Apache 2.0) plugin by The Agile Monkeys that packages an issue-to-pull-request workflow with quality gates. `/work-story <issue>` fetches the issue, proposes a plan and waits for approval, implements, checks the project's own test and coverage bar, runs a security review and a self-review, opens the pull request with the verification evidence and updates the issue. `/plan-backlog` turns an idea or a brief into epics and stories in your tracker after you approve them. It works with GitHub Issues, Jira, Linear and Azure DevOps. It runs in Claude Code, and also in Codex and Cursor. In Claude Code, install it with `claude plugin marketplace add theam/claude-dev-kit` and then `claude plugin install fullstack-dev-kit@claude-dev-kit`.
- **When we reach for it:** It is how we work on our laptops: one issue, one session, one pull request ([module 2](../02-one-agent-done-well/README.md)). We maintain it, and the engineering skills we share as a company live there instead of being copied between repositories ([module 9](../09-teams-and-organizations/README.md)).
- **Docs:** [claude-dev-kit README](https://github.com/theam/claude-dev-kit#readme) · [Claude Code plugins](https://code.claude.com/docs/en/plugins)

## Session managers and terminals

Principles first ([module 6](../06-run-sessions-in-parallel/README.md) explains them): group sessions by track, order them by priority, handle notifications round-robin from the top, name your sessions, keep their IDs, and keep a plain shell next to each agent. Any of the tools below can do that. Pick the one that gets out of your way.

### tmux

- **What it is:** A terminal multiplexer. It runs several programs in one terminal and lets you detach them (they keep running) and reattach later.
- **When we reach for it:** It is the lowest common denominator: it works with every CLI agent, on your laptop or a remote machine, with no new app. It doesn't know about agents, so you get no "needs input" notification unless you add one. DHH ran his agents in tmux panes before moving to an agent-aware tool ([Lex Fridman Podcast #501](https://lexfridman.com/dhh-2/)).
- **Docs:** [tmux wiki](https://github.com/tmux/tmux/wiki)

### Warp

- **What it is:** A terminal that its makers call an "Agentic Development Environment". It has its own agent, and it runs third-party CLI agents such as Claude Code, Codex and OpenCode with extras like notifications and code review.
- **When we reach for it:** It is where many of our sessions live today: grouped, ordered by importance, and handled when a notification says a session finished or needs a decision.
- **Docs:** [Warp documentation](https://docs.warp.dev/)

### Superset

- **What it is:** A desktop app for running many CLI coding agents in parallel, each task isolated in its own git worktree with its own branch and terminal. macOS, with experimental Linux builds. Source-available under the Elastic License 2.0.
- **When we reach for it:** We used it before our current terminal. Showing each session's pull request next to the session was very convenient. In our experience it was occasionally unstable when we used it; check the current release.
- **Docs:** [Superset on GitHub](https://github.com/superset-sh/superset)

### Conductor

- **What it is:** A Mac app that runs Claude Code, Codex and Cursor agents in parallel, in isolated workspaces, and lets you review and merge their changes.
- **When we reach for it:** We haven't adopted it. It is listed because it implements the same principle (one isolated workspace per task) with a visual interface.
- **Docs:** [conductor.build](https://www.conductor.build/)

### claude-squad

- **What it is:** A terminal app that manages several local agents (Claude Code, Codex, Gemini, Aider) in separate workspaces, using tmux sessions for the terminals and git worktrees for the code.
- **When we reach for it:** We haven't adopted it. It is a lightweight option if you like tmux and want worktree isolation without writing your own scripts.
- **Docs:** [claude-squad on GitHub](https://github.com/smtg-ai/claude-squad)

### Herdr

- **What it is:** A background runtime for coding agents: terminal sessions that keep agents such as Claude Code, Codex and OpenCode running even when you disconnect. Open source (Apache 2.0).
- **When we reach for it:** We haven't adopted it. DHH describes it as tmux plus agent notifications in [Lex Fridman Podcast #501](https://lexfridman.com/dhh-2/).
- **Docs:** [herdr.dev](https://herdr.dev/)

### Built-in: Claude Code agent view, background sessions and `--worktree`

- **What it is:** `claude agents` opens agent view, one screen that shows every background session and which ones need input (research preview). `claude --bg "…"` starts a session in the background. `claude --worktree <name>` starts a session in a new git worktree under `.claude/worktrees/<name>/`, on its own branch.
- **When we reach for it:** When you want parallel sessions without installing anything else. The worktree flag is the quickest way to follow our default of one worktree per code track.
- **Docs:** [Agent view](https://code.claude.com/docs/en/agent-view) · [Worktrees](https://code.claude.com/docs/en/worktrees) · [CLI reference](https://code.claude.com/docs/en/cli-reference)

> [!TIP]
> You don't need any of these tools to isolate work. Plain `git worktree add` works with every agent. See the [git worktree documentation](https://git-scm.com/docs/git-worktree). Codex offers worktrees from the ChatGPT desktop app: [Codex worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees).

## Automated reviewers

### Codex code review

- **What it is:** Three ways to get a Codex review. In the CLI, `/review` starts a dedicated reviewer against a base branch, uncommitted changes, a commit or custom instructions, without changing your working tree. `codex review` runs the same kind of review non-interactively. On GitHub, comment `@codex review` on a pull request or turn on automatic reviews; there it flags only P0 and P1 issues and follows a `## Code Review Rules` section in your `AGENTS.md`.
- **When we reach for it:** It is our default second-vendor reviewer. In our repositories it re-reviews every push, and its findings go into our triage ledger ([module 7](../07-agents-review-agents/README.md)).
- **Docs:** [Code review](https://learn.chatgpt.com/docs/code-review) · [Review GitHub pull requests with Codex](https://learn.chatgpt.com/docs/third-party/github)

### GitHub Copilot code review

- **What it is:** Copilot reviews pull requests, finds issues and suggests fixes you can apply. Reviews can run automatically when a pull request opens or on each push, and repository instructions in `.github/copilot-instructions.md` guide them. By default its reviews don't count toward required approvals.
- **When we reach for it:** As an extra independent reviewer on GitHub repositories, next to a second-vendor model. DHH says it "keeps finding stuff that's legitimately broken" ([Lex Fridman Podcast #501](https://lexfridman.com/dhh-2/)).
- **Docs:** [About Copilot code review](https://docs.github.com/en/copilot/concepts/agents/code-review)

### Claude Code GitHub Actions and Code Review

- **What it is:** Two products. [Claude Code GitHub Actions](https://github.com/anthropics/claude-code-action) runs Claude Code in your own workflows: mention `@claude` in an issue or pull request, or trigger it on any GitHub event; `/install-github-app` sets it up. Code Review is a managed service (research preview, Team and Enterprise plans) where several agents review each pull request and post findings tagged by severity; it never approves or blocks a merge, and a `REVIEW.md` or `CLAUDE.md` tunes it. Locally, `/code-review` (alias `/review`) reviews the current diff.
- **When we reach for it:** GitHub Actions when you want an agent job in CI that you define and control. The local `/code-review` as a quick fresh-context check before you open a pull request.
- **Docs:** [GitHub Actions](https://code.claude.com/docs/en/github-actions) · [Code Review](https://code.claude.com/docs/en/code-review)

> [!WARNING]
> An automated reviewer that isn't told the pull request's goal will chase far-fetched issues and grow the change. Give every reviewer the intent statement and the project context. [Module 7](../07-agents-review-agents/README.md) shows how.

## Standards

### AGENTS.md

- **What it is:** An open format for agent instructions: a predictable file where coding agents look for how to build, test and work in a project. Nested files apply to subfolders, and the nearest one wins. Stewarded by the Agentic AI Foundation under the Linux Foundation, and read by many agents, including Codex, GitHub Copilot, Cursor and OpenCode.
- **When we reach for it:** In every repository. It is our single shared contract. Claude Code reads `CLAUDE.md` instead, so our `CLAUDE.md` contains an `@AGENTS.md` import ([Claude Code memory docs](https://code.claude.com/docs/en/memory)).
- **Docs:** [agents.md](https://agents.md/) · [AGENTS.md in Codex](https://learn.chatgpt.com/docs/agent-configuration/agents-md)

### MCP (Model Context Protocol)

- **What it is:** An open-source standard for connecting AI applications to external systems: data sources, tools and workflows. Claude Code (`claude mcp`), Codex (`codex mcp`) and many editors support it.
- **When we reach for it:** For systems without a good CLI, and to let people's own agents read and write a shared system. Each connected server costs context, so connect only what a repository needs.
- **Docs:** [What is MCP?](https://modelcontextprotocol.io/)

## Sandboxing and isolation

### Claude Code sandboxing

- **What it is:** A sandbox for the Bash tool that the operating system enforces: you define which files and network domains commands can reach, and Claude runs commands inside that boundary without asking each time. Turn it on with `/sandbox`. Works on macOS, Linux and WSL2, not on native Windows. Anthropic reports it [cut permission prompts by 84%](https://www.anthropic.com/engineering/claude-code-sandboxing) internally.
- **When we reach for it:** When prompt fatigue tempts someone to skip permissions. The sandbox is the safer answer.
- **Docs:** [Sandboxing](https://code.claude.com/docs/en/sandboxing) · [Choose a sandbox environment](https://code.claude.com/docs/en/sandbox-environments)

### Codex sandbox

- **What it is:** Codex runs the agent's commands in a sandbox by default. `--sandbox` selects `read-only`, `workspace-write` or `danger-full-access`, and `codex exec` starts read-only. `/permissions` changes approvals during a session.
- **When we reach for it:** Keep it on. Codex's own [best practices](https://learn.chatgpt.com/guides/best-practices) say to keep approvals and sandboxing tight by default and loosen them only for trusted repositories. Use `danger-full-access` only in an isolated runner or container.
- **Docs:** [Sandbox](https://learn.chatgpt.com/docs/sandboxing) · [Permissions](https://learn.chatgpt.com/docs/permission-modes)

### Dev containers

- **What it is:** An [open specification](https://containers.dev/) for development containers defined in `devcontainer.json`. With the agent installed inside, the commands it runs execute in the container, not on your machine.
- **When we reach for it:** When a team wants the same isolated environment for every engineer, or to run an agent with fewer prompts. Read the warning in the Claude Code docs: with permissions skipped, a malicious project can still exfiltrate anything inside the container, including the agent's credentials.
- **Docs:** [Claude Code in dev containers](https://code.claude.com/docs/en/devcontainer)

### container-use

- **What it is:** An experimental open-source tool from Dagger that gives each agent a fresh container on its own git branch. It works with agents that support MCP.
- **When we reach for it:** We haven't adopted it. It is worth a look if you want container-level isolation per agent without building it yourself; expect changes, as its maintainers say it is in early development.
- **Docs:** [container-use on GitHub](https://github.com/dagger/container-use)

> [!WARNING]
> In the 2025 [s1ngularity supply-chain attack](https://nx.dev/blog/s1ngularity-postmortem), a malicious package invoked installed AI CLIs with permission-bypass flags to hunt for secrets. Never keep a permission-bypass alias on a machine with credentials.

## Claude Code ↔ Codex: equivalences

Only rows we verified against both vendors' documentation on 2026-09-17. When a row stops being true, open a tool drift issue.

| What you want | Claude Code | Codex CLI |
| --- | --- | --- |
| Project instruction file | `CLAUDE.md`; import `AGENTS.md` with `@AGENTS.md` ([memory](https://code.claude.com/docs/en/memory)) | `AGENTS.md` ([AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)) |
| Generate a starter instruction file | `/init` creates `CLAUDE.md` ([commands](https://code.claude.com/docs/en/commands)) | `/init` creates `AGENTS.md` ([commands](https://learn.chatgpt.com/docs/developer-commands?surface=cli)) |
| Run one prompt without an interactive session | `claude -p "…"` ([non-interactive](https://code.claude.com/docs/en/headless)) | `codex exec "…"` ([non-interactive](https://learn.chatgpt.com/docs/non-interactive-mode)) |
| Resume a previous session | `claude --resume`, `claude --continue`, `/resume` ([CLI](https://code.claude.com/docs/en/cli-reference)) | `codex resume`, `/resume` ([commands](https://learn.chatgpt.com/docs/developer-commands?surface=cli)) |
| Start over with an empty context | `/clear` | `/new` (or `/clear`, which also clears the terminal) |
| Summarize to free context | `/compact` | `/compact` |
| Plan before editing | Plan mode: `Shift+Tab`, `/plan` or `--permission-mode plan` ([permission modes](https://code.claude.com/docs/en/permission-modes)) | Plan mode: `/plan` or `Shift+Tab` ([best practices](https://learn.chatgpt.com/guides/best-practices)) |
| Keep working until a condition holds | `/goal <condition>` ([goal](https://code.claude.com/docs/en/goal)) | `/goal <objective>` ([commands](https://learn.chatgpt.com/docs/developer-commands?surface=cli)) |
| Review local changes | `/code-review` (alias `/review`) | `/review`; `codex review` non-interactively ([code review](https://learn.chatgpt.com/docs/code-review)) |
| Review a pull request on GitHub | `@claude review` with Code Review, or `@claude` with GitHub Actions | `@codex review` ([GitHub](https://learn.chatgpt.com/docs/third-party/github)) |
| Work in an isolated worktree | `claude --worktree <name>` ([worktrees](https://code.claude.com/docs/en/worktrees)) | Worktree option in the ChatGPT desktop app ([worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees)); plain `git worktree add` elsewhere |
| Control what runs without asking | Permission modes and `/permissions` rules; `/sandbox` | `/permissions`; `--sandbox` and `--ask-for-approval` ([CLI](https://learn.chatgpt.com/docs/codex/cli)) |
| Skip every prompt (isolated environments only) | `--dangerously-skip-permissions` | `--dangerously-bypass-approvals-and-sandbox` (alias `--yolo`) |
| Deterministic lifecycle scripts | [Hooks](https://code.claude.com/docs/en/hooks) | [Hooks](https://learn.chatgpt.com/docs/hooks) |
| Delegate to helper agents | [Subagents](https://code.claude.com/docs/en/sub-agents) | [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) |
| Connect external tools | `claude mcp` | `codex mcp` |

> [!NOTE]
> **At The Agile Monkeys** we keep hooks equivalent across both agents, so a rule enforced for Claude Code is enforced for Codex too. The shared rules live in `AGENTS.md`; each tool gets a thin adapter.

## Report tool drift

Something on this page stopped being true? That's expected, and it's the most useful contribution you can make to this page. [Open a "tool drift" issue](https://github.com/theam/agentic-engineering-101/issues/new?template=tool-drift.yml) with:

- the tool and the entry on this page,
- what changed (renamed flag, removed feature, new default),
- a link to the official documentation or changelog that shows it.

When you fix the page yourself, update `last_reviewed` in the front matter and in the notice at the top.
