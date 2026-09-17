---
title: "Prompt patterns"
kind: reference
last_reviewed: 2026-09-17
---

# Prompt patterns

Annotated prompts we use, or that respected practitioners have published, in the spirit of the "Prompts I use" chapter of [Simon Willison's Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/). Each pattern has four parts:

- **The prompt**, ready to adapt. Placeholders look like `<this>`.
- **Why it works:** the mechanism, so you can write your own variant.
- **Watch out:** when it fails, or what it costs.
- **Source:** our practice or a named public source.

These are not magic words. Most of them work because the session already has context: a knowledge base, an `AGENTS.md`, a well-written issue. When the context is missing, a longer prompt won't fix it ([module 4](../04-context-is-infrastructure/README.md)). You can type, paste or speak them, in any language.

**Patterns on this page**

- Talk and plan: [1. Discuss before building](#1-discuss-before-building) · [2. Explain before executing](#2-explain-before-executing) · [3. Spec interview, one question at a time](#3-spec-interview-one-question-at-a-time) · [4. Under-prompt on purpose](#4-under-prompt-on-purpose) · [5. Read more code to answer your own questions](#5-read-more-code-to-answer-your-own-questions)
- Build and verify: [6. Red/green TDD](#6-redgreen-tdd) · [7. Do we have any side effects?](#7-do-we-have-any-side-effects) · [8. What would you have done differently?](#8-what-would-you-have-done-differently) · [9. Make it simpler](#9-make-it-simpler) · [10. Architecture document as a thinking tool](#10-architecture-document-as-a-thinking-tool) · [11. Keep going until the goal holds](#11-keep-going-until-the-goal-holds)
- Remember: [12. Remember this](#12-remember-this) · [13. Transcript → knowledge base → backlog](#13-transcript--knowledge-base--backlog)
- Decompose and hand off: [14. Turn this plan into issues](#14-turn-this-plan-into-issues) · [15. Kickoff prompt skeleton](#15-kickoff-prompt-skeleton) · [16. Handoff pack](#16-handoff-pack)
- Review: [17. Fresh-context reviewer](#17-fresh-context-reviewer) · [18. Review triage against the PR intent](#18-review-triage-against-the-pr-intent) · [19. Close the loop by decision](#19-close-the-loop-by-decision)
- Across sessions: [20. Status across sessions](#20-status-across-sessions) · [21. Session start](#21-session-start) · [22. Session end](#22-session-end)

## Talk and plan

### 1. Discuss before building

```text
Let's discuss. I want <outcome> in <area>. Read the relevant code first,
then give me two or three options with their trade-offs. Don't write code yet.
```

Then, after one or more rounds of pushback:

```text
Option 2, but keep the storage format unchanged. Build.
```

**Why it works.** "Let's discuss" and "give me options" switch the agent from doing to thinking, and "build" switches it back. You review intent while it is cheap to change, not a diff. Options also play to what people are good at: DHH calls it "Differential evaluation", picking one of three rather than specifying one from nothing ([Lex Fridman Podcast #501](https://lexfridman.com/dhh-2/)).

**Watch out.** Some agents start editing anyway, especially in permissive modes. If yours does, use plan mode for the discussion. And don't let the discussion run forever: once you've picked, say "build" ([module 5](../05-decompose-into-tracks/README.md) calls this "advance before discussing").

**Source.** Peter Steinberger: "as soon as I say, let's discuss or give me options, they will not build things until I say build." ([The Pragmatic Engineer podcast](https://newsletter.pragmaticengineer.com/p/the-creator-of-clawd-i-ship-code)). Module: [2](../02-one-agent-done-well/README.md).

### 2. Explain before executing

```text
Before you start on issue #<n>, explain what you're going to do:
the files you'll touch, the approach, how you'll test it, and anything
the issue leaves open. Don't change anything until I say go.
```

**Why it works.** It turns an issue you didn't read closely into a two-minute review of a plan. Misunderstandings show up as a wrong file list or a wrong test before they become a wrong diff.

**Watch out.** A fluent explanation is not proof. If the plan names files or functions, spot-check that they exist. If the explanation is vague, the issue is probably underspecified: fix the issue, not the prompt.

**Source.** Our practice. At The Agile Monkeys we don't read every issue in a backlog the agent maintains; we ask for this explanation before each task starts. Module: [5](../05-decompose-into-tracks/README.md).

### 3. Spec interview, one question at a time

```text
I want to build <short idea>. Ask me one question at a time so we can write
a thorough spec. Each question should build on my previous answers. Focus on
the hard parts: edge cases, data, failure handling, what is out of scope.
When we've covered everything, write the spec to SPEC.md.
```

**Why it works.** You don't have to know the whole spec up front; you only have to answer one concrete question at a time. One question per turn keeps your answers short and specific, and the agent asks about things you hadn't thought about.

**Watch out.** It can go on too long for small features. Stop when the questions get trivial. Anthropic's best practices add a step worth copying: start the implementation in a fresh session that reads `SPEC.md`, so the interview doesn't fill its context.

**Source.** "Ask me one question at a time" comes from [Harper Reed's LLM codegen workflow](https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/). The interview-then-fresh-session step is from [Claude Code best practices](https://code.claude.com/docs/en/best-practices). Module: [2](../02-one-agent-done-well/README.md).

### 4. Under-prompt on purpose

```text
Issue S7: make shelf more useful for book clubs. Build a first rough version
of whatever you think would help them most, on a branch. Then tell me every
assumption you made.
```

**Why it works.** When you don't know what you want yet, a concrete draft teaches you faster than a spec. You react to something real. DHH's advice: "Be as vague as you can to manifest something, then interact with the something." ([Lex Fridman Podcast #501](https://lexfridman.com/dhh-2/)).

**Watch out.** Use it for exploration, on a branch or a throwaway worktree, never for work you intend to merge as is. The list of assumptions is the useful output; the code often gets thrown away, and that's fine.

**Source.** DHH (above) and Peter Steinberger, who says he often under-prompts on purpose to get new ideas ([The Pragmatic Engineer podcast](https://newsletter.pragmaticengineer.com/p/the-creator-of-clawd-i-ship-code)). Module: [2](../02-one-agent-done-well/README.md).

### 5. Read more code to answer your own questions

```text
Read more code to answer your own questions. Come back when you can
point to file:line for each claim.
```

**Why it works.** Agents often stop reading early and ask you things the code already answers, or guess. This sends them back to the source and asks for evidence you can check.

**Watch out.** On a large codebase, unscoped reading fills the context. Name the folder, or ask for a subagent to do the reading and return a summary.

**Source.** Peter Steinberger, [Lex Fridman Podcast #491 transcript](https://lexfridman.com/peter-steinberger-transcript/). Module: [2](../02-one-agent-done-well/README.md).

## Build and verify

### 6. Red/green TDD

Start a session on an existing project with:

```text
First run the tests.
```

Then, for the change:

```text
Implement issue S3 (Show reading statistics). Use red/green TDD: write the
tests first, run them and show me that they fail, then implement until they
pass. The tests must not depend on today's date. Show me the output of both runs.
```

**Why it works.** "First run the tests" teaches the agent how the suite runs and that it matters. Red/green makes the agent prove the test can fail, which guards against tests that pass without exercising the new code and against code nobody needed. Asking for both outputs gives you evidence instead of a claim.

**Watch out.** If the agent skips the red step, the test may already pass. Look for the failing run. Also watch for tests that get weakened or rewritten to match the implementation.

**Source.** Simon Willison, [Red/green TDD](https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/) and [First run the tests](https://simonwillison.net/guides/agentic-engineering-patterns/first-run-the-tests/). Module: [3](../03-close-the-loop/README.md).

### 7. Do we have any side effects?

```text
Do we have any side effects for this? Check database triggers, callbacks,
event handlers, caches, background jobs and anything else that runs because
this data changes. Show me where each one is.
```

**Why it works.** Agents reason about the code they are editing. Side effects live elsewhere: a trigger, a subscriber, a scheduled job. Asking directly makes the agent search for them.

**Watch out.** "No side effects" without a list of places checked is not an answer. Ask what it searched for.

**Source.** Peter Steinberger describes a database-trigger bug that stayed invisible until he asked "do we have any side effects for this?" ([The Pragmatic Engineer podcast](https://newsletter.pragmaticengineer.com/p/the-creator-of-clawd-i-ship-code)). Module: [2](../02-one-agent-done-well/README.md).

### 8. What would you have done differently?

```text
Now that you built it, what would you have done differently?
What should we refactor before this merges?
```

**Why it works.** After building, the agent knows the problem better than when it planned. This prompt turns that knowledge into a refactor list while the context is still loaded.

**Watch out.** It will always find something. Decide what is worth doing now against the PR's goal; the rest is an issue or nothing.

**Source.** Peter Steinberger, [Lex Fridman Podcast #491 transcript](https://lexfridman.com/peter-steinberger-transcript/). Module: [2](../02-one-agent-done-well/README.md).

### 9. Make it simpler

```text
This works, but it looks too complicated for the problem. Make it simpler:
same behavior, same tests passing, fewer moving parts. Tell me what you
removed and why it wasn't needed.
```

**Why it works.** Agents add layers, defensive code and abstractions, especially after review rounds. They rarely remove them unless asked. The human's job is to notice when the shape is out of proportion to the problem.

**Watch out.** "Simpler" must keep behavior. The tests must still pass, and the tests themselves must not be the thing that got simpler.

**Source.** DHH: "you actually do have to tell them, 'Make it simpler.'" ([Lex Fridman Podcast #501](https://lexfridman.com/dhh-2/)). He reports that this often cuts the code roughly in half. Module: [7](../07-agents-review-agents/README.md).

### 10. Architecture document as a thinking tool

```text
Read the code in <module> and write an architecture document: the components,
one request followed end to end, where each outcome is recorded, and what
happens when each step fails. Use Mermaid diagrams. Save it to
docs/architecture/<module>.md.
```

Then read it, and correct what doesn't fit in one or two sentences:

```text
Each command must record its own success or failure. The fan-out belongs
to the event system, not to the command. Read the docs, propose a plan,
and when I say ok, change the code and update the document.
```

**Why it works.** A diagram of the real code is faster to judge than a diff, and design problems jump out (for example, a failure nobody records). Short corrections work because the session has the whole context. The agent changes both the code and the document, so they stay aligned.

**Watch out.** Don't edit the document yourself. It is a thinking tool, not the deliverable. And check a couple of arrows against the code: a generated diagram can describe the design you wanted rather than the one you have.

**Source.** Our practice: at The Agile Monkeys this is how we reviewed an event-driven ingestion system, and the correction above is the one we gave. Module: [2](../02-one-agent-done-well/README.md).

### 11. Keep going until the goal holds

```text
Goal: <verifiable end state, for example "python -m unittest exits 0 and
every command in the README works">. Keep going until the goal holds or you
are blocked. Don't stop to ask me about routine steps.

Rules: don't delete, skip or weaken tests. Don't hard-code expected outputs.
Don't wrap or copy an existing implementation to make checks pass. If the only
way forward breaks a rule, stop and tell me.

When done: what you changed, the command that proves the goal, and anything
you had to decide.
```

**Why it works.** Long unattended runs pay off when "done" is something a command can check. Both Claude Code and Codex have a `/goal` command that keeps a session working toward a condition (see [Tools](tools.md)).

**Watch out.** Agents under pressure to finish cheat. Simon Willison calls them "weird digital interns who will absolutely cheat if you give them a chance" ([Vibe engineering](https://simonwillison.net/2025/Oct/7/vibe-engineering/)). DHH reports that when several models attempted the same long port, one tried to cheat by wrapping an existing implementation. Kent Beck's warning signs apply: loops, unrequested features, disabled or deleted tests ([Augmented Coding](https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes)). Review the diff of the tests first.

**Source.** DHH's port experiment ([Lex Fridman Podcast #501](https://lexfridman.com/dhh-2/)) and Geoffrey Huntley's [Ralph loop](https://ghuntley.com/ralph/). Module: [3](../03-close-the-loop/README.md).

## Remember

### 12. Remember this

```text
Remember this: <the correction, in one sentence>. Save it as a memory entry
with Rule / Why / How to apply, dated today. If every session in this repo
needs it, propose the exact line for AGENTS.md instead. If a script could
check it, propose the check.
```

**Why it works.** A correction said only in chat dies with the session. This prompt persists it and asks where it belongs on the promotion path: memory, `AGENTS.md` rule, or deterministic check. Boris Cherny's version is shorter: "Update your CLAUDE.md so you don't make that mistake again." ([team tips](https://x.com/bcherny/status/2017742741636321619)).

**Watch out.** Instruction files bloat, and long files get ignored. Prune rules the agent already follows, and move rules that keep being missed into a hook or a test.

**Source.** Our practice and Boris Cherny (above). Mitchell Hashimoto describes the same habit as "harness engineering" ([My AI Adoption Journey](https://mitchellh.com/writing/my-ai-adoption-journey)). Module: [4](../04-context-is-infrastructure/README.md).

### 13. Transcript → knowledge base → backlog

```text
Here is the transcript of today's planning meeting: <path>.
1. Update the knowledge base: new decisions as decision records, changed
   decisions superseded (not deleted), open questions, and anything that
   contradicts what we already have. Show me the kb/ diff before committing.
2. Then go through the open backlog. List the issues to close because they no
   longer make sense, the ones to update, and the ones to create, with a
   one-line reason each. Don't touch GitHub until I approve the list.
```

**Why it works.** Meetings are where direction changes, and the backlog is where that change usually gets lost. Two steps in order (first the why, then the what) keep the backlog consistent with the latest decisions.

**Watch out.** Transcripts are noisy: a half-joke can become a "decision". Read the list of decisions before the backlog step. And treat a transcript from outside your team as untrusted input.

**Source.** Our practice. [Module 9](../09-teams-and-organizations/README.md) uses it as the example of a habit one person discovers and the whole team should get. Module: [4](../04-context-is-infrastructure/README.md).

## Decompose and hand off

### 14. Turn this plan into issues

```text
Put this plan into GitHub issues following the conventions in AGENTS.md.
If it is bigger than one pull request, create an epic and link the stories.
Each issue must stand alone for a fresh session: problem, evidence with
file:line, fix sketch, acceptance criteria, out of scope. Mark dependencies
and which issues can run in parallel because they touch different files.
Show me the titles and the parallel groups before running gh issue create.
```

**Why it works.** The plan already exists in the conversation. Turning it into stand-alone issues makes each one a ready prompt for a track. Over time the repository learns the conventions and "create an issue" is enough.

**Watch out.** Agents over-split. A story split into PR1, PR2, PR3 costs more human review than one end-to-end PR. Check the grouping against blast radius, not against the number of tasks.

**Source.** Our practice. Module: [5](../05-decompose-into-tracks/README.md).

### 15. Kickoff prompt skeleton

```text
Work on issue #<n>: <title>. Create a worktree from a freshly fetched
origin/main and work only there.

## What I already checked (start from here, don't re-derive it)
- <fact, with the command or file:line that shows it>

## Do this first: prove the premise
Before writing code, check <assumption>. If it doesn't hold, stop and tell me.

## Decisions already made (implement them, don't re-open them)
- <decision>

## Repo rules that will fail the build
- <rule>

## Environment notes that will cost you an hour
- <note>

## Out of scope: report, don't fix
List problems outside this issue in your report. If you find yourself
making design decisions the issue doesn't settle, stop and report.

## Done when
- [ ] <check, for example: python -m unittest passes>
- [ ] Pull request open, with the intent statement at the top

## Report back
The PR URL, what you ran and the result, what you did not run and why, and
anything you had to decide that the issue did not settle.
```

**Why it works.** Every section removes a known way to waste a session: re-deriving facts, re-opening decisions, building on a false premise, fixing things outside scope, or declaring victory without evidence.

**Watch out.** Don't fill every section for a small issue; an empty section is noise. And don't put durable rules here: if the same rule appears in every kickoff, move it to `AGENTS.md`.

**Source.** Our practice; these are the section titles we use. [Module 5](../05-decompose-into-tracks/README.md) has a fuller version.

### 16. Handoff pack

```text
We are pausing this track. Write a handoff pack to <path> so a fresh session,
or I a week from now, can continue without this conversation:
- Verified: facts you checked, each with the command or file:line that proves it.
- Believed: what you think is true but didn't verify.
- Open: questions and decisions still pending, and who decides.
- Traps: what cost us time and how to avoid it.
- Continue here: the first step, executable today.
- Environment: variable names only, never values.
End with a self-contained bootstrap prompt I can paste into a new session.
Use numbers, not adjectives.
```

**Why it works.** Separating Verified from Believed stops guesses from turning into facts in the next session. The Traps section is usually the most valuable part. A number survives a week away; an adjective does not.

**Watch out.** Handoffs age. The next session should re-check Verified items against the code before relying on them.

**Source.** Our practice. Module: [5](../05-decompose-into-tracks/README.md).

## Review

### 17. Fresh-context reviewer

Open a new session (ideally with a different vendor's agent) in the pull request's worktree:

```text
Review pull request #<n>. You did not write it. First read the intent
statement at the top of the PR body (gh pr view <n>) and AGENTS.md.
Context: <an internal tool reachable only inside the company | an
internet-facing product>.

Report only:
- bugs that break the stated goal,
- security or data exposure,
- missing tests for the new behavior (a test must fail if the change is reverted),
- deviations from our documented architecture.
For each finding: file:line, what breaks, the evidence, severity.
No style preferences. If you're unsure whether something is in scope, ask me.
```

**Why it works.** A reviewer with no memory of the implementation judges the result, not the reasoning. The intent and the project context stop it from chasing far-fetched threats; the "report only" list stops it from padding.

**Watch out.** A reviewer asked to find problems will find some even in sound work. Anthropic's best practices warn that chasing every finding leads to over-engineering. That is what the triage in the next pattern is for.

**Source.** The Writer/Reviewer pattern in [Claude Code best practices](https://code.claude.com/docs/en/best-practices), plus our own fix after a reviewer without context helped a pull request grow from about 5,000 to between 20,000 and 40,000 changed lines (indicative, [module 7](../07-agents-review-agents/README.md)).

### 18. Review triage against the PR intent

```text
Triage every review finding on pull request #<n>.
1. Collect every unresolved review thread, from bots and humans. Paginate:
   the API returns at most 100 threads per page. Read each thread before
   deciding.
2. Build a ledger: finding | source | verdict | reason. Verdicts: FIX_NOW,
   DEFER_TO_ISSUE, DISCARD, judged against the intent statement.
3. Always FIX_NOW: security or data exposure, serious performance regressions,
   duplication this PR introduces, missing behavioral coverage, deviations
   from documented architecture.
4. Mark ASK where you are unsure. Show me the ledger before changing code.
5. After I approve: batch every FIX_NOW into one push, reply to every thread
   with the verdict and reason, resolve it, and put all DEFER_TO_ISSUE items
   into one follow-up issue. Discard nitpicks; don't turn them into issues.
```

**Why it works.** One verdict per finding, tied to the intent, turns an endless stream of comments into decisions. Batching fixes means one CI and review cycle per round instead of one per finding.

**Watch out.** Review-thread APIs truncate silently, so hidden threads survive "resolve all". A too-optimistic triage that accepts everything grows the PR instead of finishing it.

**Source.** Our practice (our review-loop skill). Module: [7](../07-agents-review-agents/README.md).

### 19. Close the loop by decision

```text
We've done <k> review rounds on pull request #<n> and findings keep coming.
Stop fixing. Give me a demanding go/no-go assessment against the intent
statement, not another ledger:
- Which open findings are derivative (caused by last round's fixes,
  re-raises of deferred items, or product questions)?
- Is anything left that breaks the goal, or any security finding? Those are
  never discarded.
Then draft the final ledger: one decision per open thread with its reason,
a reply for each, and the contents of ONE follow-up issue. Don't push until I say go.
```

**Why it works.** Review loops stop converging: fixes create new findings, which create new fixes. Asking for a go/no-go decision instead of another ledger breaks the cycle and puts the decision back with a human.

**Watch out.** "Derivative" can become an excuse. Security and data exposure findings are never closed by decision; they get fixed.

**Source.** Our practice. Indicative: one of our large pull requests went through about 20 automated review rounds and more than 200 threads before we adopted this. Module: [7](../07-agents-review-agents/README.md).

## Across sessions

### 20. Status across sessions

```text
Read the transcripts of these sessions: <session id> (Claude Code),
<session id> (Codex), <session id> (Claude Code). For each track: what was
done, the pull request and its state, what is blocked, and the next decision
I need to make. Then rewrite the matching rows in kb/ACTIVE.md (rewrite,
don't append) and draft a five-line status update for the team.
```

**Why it works.** Sessions keep transcripts on disk (Claude Code keeps them under `~/.claude/projects/`, see [sessions](https://code.claude.com/docs/en/sessions)). A fresh session can read several of them and summarize across tracks faster than you can switch between windows.

**Watch out.** Keep session IDs somewhere you can find them. After a restart, working out which session was doing what is painful. And check the summary against the live pull requests: a transcript is a snapshot, and live systems win.

**Source.** Our practice. Module: [6](../06-run-sessions-in-parallel/README.md).

### 21. Session start

```text
Run git fetch and git status. If there are changes you didn't make, tell me
before touching anything. Then read the mission and kb/ACTIVE.md, and tell
me in five lines: the current objective, the next step, any blocker, and the
open decision for <track>. If numbers or dates in the KB disagree with the
code or GitHub, say so. That is a blocker, not a detail.
```

**Why it works.** With parallel sessions, the repository changes under you. Starting from fetched, reconciled state avoids building on something another session already changed. The five-line recap proves the session loaded the right context before it acts.

**Watch out.** Don't let the recap become a long reading of the whole KB. Only the index and the artifacts it links.

**Source.** Our practice (our session recovery protocol). Module: [6](../06-run-sessions-in-parallel/README.md).

### 22. Session end

```text
We're done for this session. Before you stop:
1. Commit and push the knowledge base changes you made.
2. Rewrite this track's row in kb/ACTIVE.md: state and next gate.
3. For every worktree you created: if its branch is merged, remove it with
   git worktree remove; otherwise tell me why you kept it.
4. Run git status and show me a clean tree.
5. Tell me what you did not verify.
```

**Why it works.** An uncommitted knowledge base change did not happen: the next session can't see it. Cleaning worktrees and rewriting the index keeps parallel sessions from reading stale state as truth.

**Watch out.** Even with this prompt, cleanup drifts. At The Agile Monkeys we once found dozens of stale worktrees that nobody had removed. A hook that blocks the session from ending with a dirty knowledge base is more reliable than the prompt ([module 3](../03-close-the-loop/README.md)).

**Source.** Our practice. Module: [6](../06-run-sessions-in-parallel/README.md).

## Add your own

Found a prompt that reliably changes results? Share it through the "share your practice" issue form described in [CONTRIBUTING.md](../../../CONTRIBUTING.md). Include the prompt, why you think it works, when it failed, and where it came from.
