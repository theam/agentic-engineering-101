---
title: "Build your own skills"
kind: appendix
last_reviewed: 2026-10-01
---

# Build your own skills

At The Agile Monkeys we run our local workflow with [claude-dev-kit](https://github.com/theam/claude-dev-kit), an open-source plugin we maintain, and we're gathering the skills we share as a team into it. **You don't need it, or any other plugin, to follow this guide or to work as an agentic engineer.** Many engineers prefer to build their own skills, and building one is the best way to understand what any plugin does for you. This appendix shows how.

> [!IMPORTANT]
> **Checked against the official documentation on 2026-10-01.** Skill formats and folders are young and still change. Every path and field below links to its source. When the docs disagree with this page, the docs win: please [open a "tool drift" issue](https://github.com/theam/agentic-engineering-101/issues/new?template=tool-drift.yml).

## When a skill is worth it

A skill packages the craft of a recurring task: instructions the agent loads when the task comes up, plus any scripts or reference files it needs. [Module 4](../04-context-is-infrastructure/README.md) gives the rule we follow: create a skill when something already hurts, because every skill's description sits in the context on every turn. Good candidates:

- a workflow you run several times a week and keep re-explaining, such as taking an issue to a pull request or preparing a release;
- a correction you've made twice that needs judgment, so a script can't enforce it;
- a review checklist for one kind of change.

If a rule must hold every time, it isn't a skill. It's a hook, a validator or a CI check ([module 3](../03-close-the-loop/README.md)). Skills guide; guards enforce.

## Anatomy of a skill

A skill is a folder with a `SKILL.md` file inside: YAML front matter, then Markdown instructions. Claude Code and Codex both build on the [Agent Skills](https://agentskills.io/specification) open standard, so the same folder works in both.

```text
work-issue/
├── SKILL.md          # required: front matter and instructions
└── pr-template.md    # optional: loaded only when SKILL.md points to it
```

- **`name`** identifies the skill. The standard asks for lowercase letters, numbers and hyphens, matching the folder name. In Claude Code it's also the `/name` you type.
- **`description`** decides when the agent loads the skill on its own. Say what it does, when to use it and when not to. It's the part that costs context on every turn, so make every word count. The standard caps it at 1,024 characters.
- **The body** loads only when the skill is used. Keep it short: both the standard and the [Claude Code skills documentation](https://code.claude.com/docs/en/skills) say to keep `SKILL.md` under 500 lines and move reference material into files it links to.

Where skills live:

| Scope | Claude Code | Codex |
| --- | --- | --- |
| One repository, shared with the team | `.claude/skills/<name>/SKILL.md` | `.agents/skills/<name>/SKILL.md` |
| You, in every repository | `~/.claude/skills/<name>/SKILL.md` | `~/.agents/skills/<name>/SKILL.md` |
| Run it explicitly | `/<name>` | `$<name>`, or pick it with `/skills` |

Sources: [Claude Code skills](https://code.claude.com/docs/en/skills) and [Codex skills](https://learn.chatgpt.com/docs/build-skills).

To use one skill in both tools, keep the folder in `.agents/skills/` and add a symlink to it from `.claude/skills/`; Claude Code follows symlinked skill folders. Stick to the standard's fields (`name`, `description`, `license`, `compatibility`, `metadata` and `allowed-tools`) when you want a skill to stay portable. Fields such as `disable-model-invocation` are Claude Code extensions.

## Your first skill: from issue to pull request

Here's the cycle from [module 2](../02-one-agent-done-well/README.md) as a skill, written for the [practice project](../../../practice/shelf/). Save it as `.agents/skills/work-issue/SKILL.md`:

```markdown
---
name: work-issue
description: Take one GitHub issue to a pull request, with a plan the user approves before any code is written. Use when the user asks to work on, implement or fix a specific issue by number. Don't use it for questions about an issue or to review a pull request.
---

# Work an issue

The user gives you an issue number. Work on that issue only.

1. Read it with `gh issue view <number>`, then read the code it touches.
   Answer your own questions from the code before asking the user.
2. List what the issue doesn't settle, with options and a recommendation
   for each. Wait for the user's choices.
3. Write the plan in under 25 lines: the files you'll change, any change to
   stored data, an example of the output, the tests you'll add and why each
   would fail without the change, and what you won't do. Then wait. Don't
   write code until the user says "build".
4. Create a branch for the issue. Write the tests first and show them
   failing, then implement.
5. Run the whole suite with `python -m unittest` and show the output. If
   anything fails, fix it before you continue.
6. Answer two questions: do we have any side effects? What did you assume
   that you didn't check?
7. Open the pull request with `gh pr create`. In the description: what
   changes, the decisions from step 2, the command you ran to verify and its
   result, and "Closes #<number>".

Never merge, and never push to main.
```

Run it with `/work-issue 3` in Claude Code, `$work-issue 3` in Codex, or just ask "let's work on issue 3". Every line comes from a module:

| Step | What it does | Where it comes from |
| --- | --- | --- |
| 1 | Explore, and answer from the code | [Module 2](../02-one-agent-done-well/README.md) |
| 2–3 | Discuss, then review intent before any code exists | [Module 2](../02-one-agent-done-well/README.md) |
| 4–5 | Red first, and evidence instead of "done" | [Module 3](../03-close-the-loop/README.md) |
| 6 | Follow-up prompts that find what nobody looked for | [Module 2](../02-one-agent-done-well/README.md) |
| 7 | A pull request that carries its decisions and evidence | [Module 7](../07-agents-review-agents/README.md) |
| Last line | Humans merge | [Module 9](../09-teams-and-organizations/README.md) |

Two choices to make for your own version:

- **Who starts it.** A workflow that pushes branches and opens pull requests is one you may want to start yourself. In Claude Code, `disable-model-invocation: true` in the front matter means only `/work-issue` runs it; the docs recommend it for workflows with side effects, "You don't want Claude deciding to deploy because your code looks ready." ([Claude Code skills](https://code.claude.com/docs/en/skills))
- **What the skill can't promise.** "Show the output" is advice. Pair the skill with the Stop hook from [module 3](../03-close-the-loop/README.md), so the agent can't finish while the suite fails, whether or not it follows the skill.

## Let the agent draft it, then test it

You don't have to write the first version by hand. Codex has a built-in `$skill-creator` that drafts a skill with you. With any agent, describe the workflow and ask for a `SKILL.md` that follows the standard, then review it like a plan.

Then test it like code:

1. **Run it on a real issue in a fresh session.** Issue S3 from the practice project is a good one: it has decisions the issue doesn't settle.
2. **Watch where it goes off track.** Did it start building before "build"? Skip the failing test? Ask questions the code could answer?
3. **Fix the skill, not the session.** Sharpen the step it skipped. If the same step gets skipped twice, move it to a hook.
4. **Check when it triggers.** Ask a question about an issue and confirm the skill doesn't load. Ask to work on one and confirm it does.
5. **Ask the agent to review it.** "Read the work-issue skill. Which step is ambiguous, and what would you do differently?"

Keep the corrections in the same log you started in [lab 2](../02-one-agent-done-well/lab.md).

## Share it with your team

- **In one repository:** commit the skill folder. A team skill goes through a pull request and gets reviewed like code, because every agent on the team will follow it ([module 9](../09-teams-and-organizations/README.md)).
- **Across repositories:** package your skills as a plugin instead of copying them. In Claude Code, a plugin is a folder with a `.claude-plugin/plugin.json` manifest and its components, such as `skills/`, `agents/` and `hooks/`. A marketplace is a repository with a `.claude-plugin/marketplace.json` that lists your plugins. While you develop, load a plugin straight from its folder with `--plugin-dir` ([Claude Code plugins](https://code.claude.com/docs/en/plugins)). Codex can package skills as plugins too ([Codex skills](https://learn.chatgpt.com/docs/build-skills)).
- **Watch the cost:** an enabled plugin's skill descriptions are in the context on every turn, even in sessions that never use them. In Claude Code, `/skill-doctor` shows what each skill costs and how often it's used.

That is all claude-dev-kit is: a set of skills, agents and hooks in one plugin, installed once. If you want to see a larger skill set, [read its source](https://github.com/theam/claude-dev-kit). If you'd rather build your own, the pieces on this page are all you need.

## Watch out

- ❌ A skill for everything. ✅ Wait until a task hurts; each description costs context on every turn.
- ❌ A vague description, such as "helps with issues". ✅ Say what it does, when to use it and when not to.
- ❌ Rules that must always hold, written as skill prose. ✅ Hooks, validators and CI.
- ❌ The same skill copied into every repository. ✅ One home, a repository or a plugin, changed through reviewed pull requests.
- ❌ A 900-line `SKILL.md`. ✅ A short body that links to reference files.
- ❌ Installing someone else's skill or plugin without reading it. ✅ It runs with your permissions. Read it first ([plugin security](https://code.claude.com/docs/en/plugins/security)).

## Go further

- [Claude Code skills](https://code.claude.com/docs/en/skills): every front matter field, arguments, and what each skill costs.
- [Codex skills](https://learn.chatgpt.com/docs/build-skills): where Codex looks, explicit and implicit use, `$skill-creator`.
- [Agent Skills specification](https://agentskills.io/specification): the portable format both build on.
- [Claude Code plugins](https://code.claude.com/docs/en/plugins): when you need a plugin, install scopes and marketplaces.
- [claude-dev-kit](https://github.com/theam/claude-dev-kit): our plugin, open source, as one worked example.
