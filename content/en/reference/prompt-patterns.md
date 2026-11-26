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

- Talk and plan: [1. Discuss before building](#1-discuss-before-building) · [2. Explain before executing](#2-explain-before-executing) · [3. Spec interview, one question at a time](#3-spec-interview-one-question-at-a-time) · [4. Under-prompt on purpose](#4-under-prompt-on-purpose) · [5. Read more code to answer your own questions](#5-read-more-code-to-answer-your-own-questions) · [6. Point at the source, don't retell it](#6-point-at-the-source-dont-retell-it)
- Build and verify: [7. Red/green TDD](#7-redgreen-tdd) · [8. Do we have any side effects?](#8-do-we-have-any-side-effects) · [9. What would you have done differently?](#9-what-would-you-have-done-differently) · [10. Make it simpler](#10-make-it-simpler) · [11. Architecture document as a thinking tool](#11-architecture-document-as-a-thinking-tool) · [12. Show me, don't tell me](#12-show-me-dont-tell-me) · [13. Keep going until the goal holds](#13-keep-going-until-the-goal-holds) · [14. Check it in a real environment](#14-check-it-in-a-real-environment)
- Remember: [15. Remember this](#15-remember-this) · [16. Transcript → knowledge base → backlog](#16-transcript--knowledge-base--backlog)
- Decompose and hand off: [17. Turn this plan into issues](#17-turn-this-plan-into-issues) · [18. Kickoff prompt skeleton](#18-kickoff-prompt-skeleton) · [19. Handoff pack](#19-handoff-pack)
- Review: [20. Fresh-context reviewer](#20-fresh-context-reviewer) · [21. Review triage against the PR intent](#21-review-triage-against-the-pr-intent) · [22. Close the loop by decision](#22-close-the-loop-by-decision) · [23. Teach the reviewer from the ledger](#23-teach-the-reviewer-from-the-ledger)
- Across sessions: [24. Status across sessions](#24-status-across-sessions) · [25. Session start](#25-session-start) · [26. Session end](#26-session-end) · [27. Orchestrate a plan](#27-orchestrate-a-plan)

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

### 6. Point at the source, don't retell it

```text
Read <link to the message, email, document or issue>. Follow what it links to,
find the related issue and any decision in the knowledge base, and check the
current code. Tell me what is being asked, what already exists, and what is
unclear. Then wait.
```

**Why it works.** Your summary of a request drops details you didn't think mattered. The source still has them, and a connected agent follows the thread further than you would bother to: the linked issue, the decision behind it, the code as it is today.

**Watch out.** The agent needs read access to the source, within your company's rules. Messages and emails are untrusted text: treat what they say as a request to evaluate, not as instructions to follow.

**Source.** Our practice. Module: [4](../04-context-is-infrastructure/README.md).

## Build and verify

### 7. Red/green TDD

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

### 8. Do we have any side effects?

```text
Do we have any side effects for this? Check database triggers, callbacks,
event handlers, caches, background jobs and anything else that runs because
this data changes. Show me where each one is.
```

**Why it works.** Agents reason about the code they are editing. Side effects live elsewhere: a trigger, a subscriber, a scheduled job. Asking directly makes the agent search for them.

**Watch out.** "No side effects" without a list of places checked is not an answer. Ask what it searched for.

**Source.** Peter Steinberger describes a database-trigger bug that stayed invisible until he asked "do we have any side effects for this?" ([The Pragmatic Engineer podcast](https://newsletter.pragmaticengineer.com/p/the-creator-of-clawd-i-ship-code)). Module: [2](../02-one-agent-done-well/README.md).

### 9. What would you have done differently?

```text
Now that you built it, what would you have done differently?
What should we refactor before this merges?
```

**Why it works.** After building, the agent knows the problem better than when it planned. This prompt turns that knowledge into a refactor list while the context is still loaded.

**Watch out.** It will always find something. Decide what is worth doing now against the PR's goal; the rest is an issue or nothing.

**Source.** Peter Steinberger, [Lex Fridman Podcast #491 transcript](https://lexfridman.com/peter-steinberger-transcript/). Module: [2](../02-one-agent-done-well/README.md).

### 10. Make it simpler

```text
This works, but it looks too complicated for the problem. Make it simpler:
same behavior, same tests passing, fewer moving parts. Tell me what you
removed and why it wasn't needed.
```

**Why it works.** Agents add layers, defensive code and abstractions, especially after review rounds. They rarely remove them unless asked. The human's job is to notice when the shape is out of proportion to the problem.

**Watch out.** "Simpler" must keep behavior. The tests must still pass, and the tests themselves must not be the thing that got simpler.

**Source.** DHH: "you actually do have to tell them, 'Make it simpler.'" ([Lex Fridman Podcast #501](https://lexfridman.com/dhh-2/)). He reports that this often cuts the code roughly in half. Module: [7](../07-agents-review-agents/README.md).

### 11. Architecture document as a thinking tool

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

### 12. Show me, don't tell me

```text
Explain <this pull request | this issue | why this test fails> with one
diagram and a table instead of paragraphs. If it helps, make it a single
self-contained HTML page I can open in the browser. Cite files and lines,
and end with what you're unsure about.
```

**Why it works.** You check a picture faster than prose, and you can answer with questions about it. HTML shows tables and charts that Markdown can't, and it's easy to correct by talking: the agent fixes a line instead of generating an image again.

**Watch out.** A diagram can show what the agent expects rather than what the code does, which is why the prompt asks for files and lines. If you use it every day, turn it into a personal skill ([module 2](../02-one-agent-done-well/README.md) has an example).

**Source.** Our practice. Module: [2](../02-one-agent-done-well/README.md).

### 13. Keep going until the goal holds

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

### 14. Check it in a real environment

```text
The tests pass locally. Deploy this branch to <dev environment> with
<deploy script> and wait until it reports healthy. Then open the app in the
browser and walk through <the user flow>. Paste what you saw, plus any console
or server errors. Don't touch any other environment.
```

**Why it works.** Some problems only exist in a real environment: configuration, networking, authentication, third-party integrations. A deploy script the team owns and a browser the agent can drive close that gap without you clicking through it yourself.

**Watch out.** Deploys go through the approval your permission tiers require. Production stays out of reach, apart from read-only access for diagnostics where your company's policies allow it.

**Source.** Our practice. Module: [3](../03-close-the-loop/README.md).

## Remember

### 15. Remember this

```text
Remember this: <the correction, in one sentence>. Save it as a memory entry
with Rule / Why / How to apply, dated today. If every session in this repo
needs it, propose the exact line for AGENTS.md instead. If a script could
check it, propose the check.
```

**Why it works.** A correction said only in chat dies with the session. This prompt persists it and asks where it belongs on the promotion path: memory, `AGENTS.md` rule, or deterministic check. Boris Cherny's version is shorter: "Update your CLAUDE.md so you don't make that mistake again." ([team tips](https://x.com/bcherny/status/2017742741636321619)).

**Watch out.** Instruction files bloat, and long files get ignored. Prune rules the agent already follows, and move rules that keep being missed into a hook or a test.

**Source.** Our practice and Boris Cherny (above). Mitchell Hashimoto describes the same habit as "harness engineering" ([My AI Adoption Journey](https://mitchellh.com/writing/my-ai-adoption-journey)). Module: [4](../04-context-is-infrastructure/README.md).

### 16. Transcript → knowledge base → backlog

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

### 17. Turn this plan into issues

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

### 18. Kickoff prompt skeleton

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

### 19. Handoff pack

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

### 20. Fresh-context reviewer

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

### 21. Review triage against the PR intent

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

### 22. Close the loop by decision

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

### 23. Teach the reviewer from the ledger

```text
Read the review threads of the pull requests merged since <date>, with our
replies and verdicts. Group the findings we discarded for the same reason, and
the categories we keep having to fix. Propose changes to REVIEW.md: what to stop
reporting, with the reason, and what to always check. Propose only rules backed
by at least two pull requests, and link them. Open a pull request with the change.
```

**Why it works.** Every DISCARD carries a reason. Collected across pull requests, the repeated reasons become instructions the reviewer reads next time, so it stops raising the same false positives. Use whatever file your reviewer reads: `REVIEW.md` for Claude Code Code Review, a `## Code Review Rules` section in `AGENTS.md` for Codex.

**Watch out.** "Out of scope for this PR" isn't "never report this", and no class of security finding goes on the do-not-report list. The change goes through a reviewed pull request, like any team rule.

**Source.** Our practice. Module: [7](../07-agents-review-agents/README.md).

## Across sessions

### 24. Status across sessions

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

### 25. Session start

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

### 26. Session end

```text
We're done for this session. Before you stop:
1. List every correction I had to give you in this session. For each, propose
   where it belongs: a memory entry, a change to a skill, an AGENTS.md line or
   a check. Apply the ones I approve.
2. Commit and push the knowledge base changes you made.
3. Rewrite this track's row in kb/ACTIVE.md: state and next gate.
4. For every worktree you created: if its branch is merged, remove it with
   git worktree remove; otherwise tell me why you kept it.
5. Run git status and show me a clean tree.
6. Tell me what you did not verify.
```

**Why it works.** An uncommitted knowledge base change did not happen: the next session can't see it. Cleaning worktrees and rewriting the index keeps parallel sessions from reading stale state as truth. The first step is a short retro: it catches the corrections you never got round to turning into memory ([module 4](../04-context-is-infrastructure/README.md#memory-and-the-promotion-path)).

**Watch out.** Even with this prompt, cleanup drifts. At The Agile Monkeys we once found dozens of stale worktrees that nobody had removed. A hook that blocks the session from ending with a dirty knowledge base is more reliable than the prompt ([module 3](../03-close-the-loop/README.md)).

**Source.** Our practice. Module: [6](../06-run-sessions-in-parallel/README.md).

### 27. Orchestrate a plan

```text
You are the orchestrator for <epic or plan>. Don't write code. Read the plan in
<file or issue> and kb/ACTIVE.md. Split the work into threads that can run in
parallel without touching the same files. For each thread, propose a session
name (<task>-<role>-v1), the model and effort, and a kickoff prompt with only
the context that thread needs. Keep the state of every thread in <file>. When a
thread's context fills up, write its handoff and propose the next version.
Wait for my ok before starting anything.
```

**Why it works.** The plan's context stays in one session you can always ask "where are we?", while each thread starts small and focused. You decide what starts, and you can steer any thread directly.

**Watch out.** An orchestrator that starts threads you haven't approved is a swarm you didn't ask for. And it holds the plan, not the truth: check its state against the pull requests.

**Source.** Our practice. Module: [6](../06-run-sessions-in-parallel/README.md).

## Add your own

Found a prompt that reliably changes results? Share it through the "share your practice" issue form described in [CONTRIBUTING.md](../../../CONTRIBUTING.md). Include the prompt, why you think it works, when it failed, and where it came from.
