---
title: "One agent, done well · Reading"
kind: reading
last_reviewed: 2026-11-27
---

# Module 02 · One agent, done well

<!-- Written version of the module for Agentic Engineer Academy. One part per video, in the same order. Format: docs/reading-format.md. -->

## Part 1 · Talk to it like a coworker

<!-- minutes: 4 -->

> The questions that matter can often be settled in a two-minute conversation, before any code exists. Talk to the agent like a coworker who shares your context.

### The most expensive place to find a problem

Here is how a small task goes wrong. Shelf is the small practice project you use in the labs.

You ask the agent to "add a stats command to shelf". It writes 150 lines, including a --json flag you didn't ask for. You open the diff, the list of changed lines, and start reading.

Twenty lines in, you find the real problem. "Books finished this year" counts every book whose status is done and whose date falls in the current year. But what about a book you added yesterday as already read, finished years ago? And "this year" in which time zone? The timestamps are stored in UTC, and you live in Madrid or in Bogotá.

You correct it. The agent patches it. A test in another file breaks. You correct again. Forty minutes later, the session is a pile of partial fixes, and you're no longer sure which ones are still needed.

**None of that was a model failure.** The two questions that mattered could have been asked in a two-minute conversation, before any code existed. Instead you found them inside a diff, which is the most expensive place to find anything.

This module is about one agent doing one task well, what the course calls the inner loop. The inner loop is about **moving corrections earlier**: from the diff to the plan, and from the plan to the conversation.

### A coworker, not a search box

How long your messages should be depends on how much the other side knows. A search box gets one long, self-contained query, because it knows nothing about you. A coworker gets short messages, because you share context: the codebase, the decisions you made last week, what you're trying to do.

A coding agent can be either, and you decide which. A session is one conversation with an agent. Instruction files are files in the repository that the agent reads at the start of every session. In a session opened in your repository, with instruction files and a few turns of conversation, short messages work: "what about books added as done?", "no, keep the output plain text".

**If you keep writing long "perfect prompts" that re-explain the project, treat that as a smell:** you're typing the context the session lacks. Fix the context, not the prompt. Module 04 shows how.

Tell the agent the problem you have, not the steps to take.

> I'm not telling it where we're going. I'm telling it the problem I have.
>
> David Heinemeier Hansson (DHH), the creator of Ruby on Rails, describing how he works with agents today.

Short is not vague about what matters. When you hand a task to a session with no history, structure helps: the Codex best practices, OpenAI's guide for its coding agent, suggest goal, context, constraints and "done when". Module 05 covers those handoff prompts. Inside a live conversation you rarely need them.

### In practice

At The Agile Monkeys, the company behind this course, the engineers who run many agents say they don't "write prompts" anymore. They plan as a conversation, inside a session opened in a repository that already holds the project's context and past decisions:

- "I want to do X, how would you do it?"
- "Do it like this."
- "No, I prefer this other way."

When the plan is ready: "put this plan into GitHub issues; if it's big, split it into an epic". An issue is a task written down in GitHub, and an epic is a large issue made of smaller ones. After a few weeks the repository has learned the conventions, and "create an issue" is enough.

### Speak your language, write in one

Planning by conversation suits voice. Speaking is faster than typing when you're thinking aloud, and agents make surprising sense of unpolished spoken thoughts.

**Think out loud with the agent rather than dictating to it.** You don't need finished sentences. Ramble, change your mind halfway ("no, forget that, try the other way"), and let the agent turn it into a structure you can correct. It recovers your intent even from a bad transcription: a tired "did that commit go straight to main?" can come out as "exit on commit direct to main", and the agent still asks back whether the commit went straight to main. People who haven't tried this tend to assume it needs clean, structured sentences. Try it for a week before you decide.

Dictation is one mode. Some tools also offer a real-time voice conversation, which some of us prefer for talking through a task or a piece of code. In Claude Code, Anthropic's coding agent, the /voice command turns on dictation: hold the space bar and speak.

At The Agile Monkeys many of us talk to agents in Spanish, often by voice. We keep a standing rule in our repositories that everything we keep is written in English: code, comments, commits, pull requests, issues and documentation. A pull request is a proposed change, sent for review before it joins the main code. We haven't seen problems from mixing the two languages.

Put the same rule in your instruction file, so every session follows it without being told: "Talk to the user in the language they use. Write every persisted artifact (code, comments, commit messages, pull request and issue text, documentation) in English."

**Watch out with identifiers, numbers and file names.** When they matter, paste them instead of saying them, and read the transcription before you send it.

### Key points

- Problems are cheapest to catch in the conversation, before any code exists.
- Long "perfect prompts" signal missing context. Fix the context.
- Think out loud in any language. Write what you keep in one.

## Part 2 · The cycle

<!-- minutes: 5 -->

> Explore, discuss, plan, build, verify, commit. Keep talking separate from building: the agent builds only when you say so.

### Six steps

Every task you give one agent goes through six steps: explore, discuss, plan, build, verify and commit. Each one is below, followed by when to skip a step and when to go back.

### Explore

The agent reads before it writes. Ask questions whose answers are in the code, and tell it not to change anything. In shelf, the model is the code that defines a book and the store is the code that saves it: "Read the model, the store and the list command. How is a book's status changed, and what gets recorded when that happens? Don't change anything."

When the agent asks you things the code could answer, send it back. Peter Steinberger, an engineer who runs many agents on a project he mostly builds alone, uses one sentence for that: "Read more code to answer your own questions." In lab 2, each time you have to send it back counts as a correction.

### Discuss

Ask for options and trade-offs, then choose. DHH calls it "Differential evaluation. You give me three options, I pick one of them." Picking among three concrete designs beats describing the right one from scratch.

Agents are eager to build, so be explicit about when they shouldn't. Steinberger relies on trigger phrases:

> as soon as I say, let's discuss or give me options, they will not build things until I say build.
>
> Peter Steinberger, on how he keeps agents from building too early.

Say "don't write code until I say build". If you're unsure it listened, run git status, which lists the files that changed.

If the agent misses a case you can see, don't hand it the answer yet. Ask "What data would make these counts wrong?" If it still misses it, tell it.

```prompt-weak
add a stats command
```

```prompt-strong
Let's discuss issue #3 (shelf stats) before building. Read the issue, the
model and the store first. Then tell me which cases the issue doesn't settle,
give me options for each with their trade-offs, and recommend one.
Don't write code until I say build.
```

The better prompt opens a discussion, not a build:

- **It reads first:** the issue, the model and the store.
- **It asks for the open cases,** with options and a recommendation.
- **It holds the build** until you say so.

Issue #3 is the stats task of the practice project. In your repository it may have another number. Lab 2 shows how to create it.

### Plan

Before it executes, ask the agent to explain what it will do. A plan you can review in a minute has:

- the files it will change,
- any change to data or storage,
- behavior at the edges,
- the tests that will prove it, and that would fail without the change,
- what it will not do.

Part 4 shows how to ask for the plan and how to correct it.

### Build and verify

**Build.** Say "build" explicitly. Ask the agent to write the tests first and run them to show they fail: a test that never failed doesn't prove the change. Then it implements, and you don't watch. If it runs the command by hand, point it at a temporary file, so it never touches your real data. In lab 2, that is what the SHELF_PATH environment variable is for.

**Verify.** The agent shows you the output of the tests it ran. The Claude Code best practices, Anthropic's guide for its coding agent, put it as: "Have Claude show evidence rather than asserting success". Don't accept "done" without evidence: ask for the command it ran and its output. Then:

- **Check the scope yourself.** git status and git diff --stat show which files changed.
- **See the real output** of the command, not a summary of it.
- **Work out the expected output yourself** before you read the agent's. If they differ, ask why before you accept any explanation.

Module 03 is entirely about this step.

### Commit

Small, with a message that records the decisions, not just the change. In lab 2, the pull request description also states each decision and its trade-offs.

Kent Beck, known for test-driven development, keeps structural and behavioral changes in separate commits: changes that reorganize the code, apart from changes that alter what it does. That habit makes agent work much easier to review.

### When to skip a step, and when to go back

Not every change needs a plan. Anthropic's rule of thumb: "If you could describe the diff in one sentence, skip the plan." Renaming a flag, fixing a typo in an error message or adding a log line can go straight to build and verify. A stats command with a date decision in it can't be described in one sentence, so it needs a plan.

The cycle also goes back:

- **Verify fails:** back to build.
- **The plan rests on a wrong assumption:** back to discuss.
- **The build is wrong at the root:** back to discuss.

### The cycle by default

At The Agile Monkeys we run this cycle on our laptops with claude-dev-kit, an open-source plugin we maintain. A plugin is an add-on that gives the agent ready-made commands. It runs in Claude Code and in Codex. In Claude Code, its /work-story command reads the issue, proposes a plan and writes no code until someone approves it. Then it builds, checks the project's own tests and the minimum test coverage the project asks for, runs a security review and a self-review, and opens the pull request with the evidence.

It doesn't replace the judgment in this module: you still discuss, correct the plan and throw work away when it's wrong at the root. What it changes is that the steps happen by default, instead of depending on a habit you have to remember. **You don't need it, or any plugin.** The course appendix "Build your own skills" shows how to write this same cycle as your own skill: a packaged set of instructions the agent loads when it is relevant.

### Key points

- Explore, discuss, plan, build, verify, commit.
- The agent builds only when you say "build".
- Ask for evidence, not "done".
- Skip the plan only when the diff fits in one sentence.

## Part 3 · How much to say

<!-- minutes: 2 -->

> There are two opposite pieces of advice about how much to say to an agent, and both are right, at different moments. Say little when you want ideas. Be precise about what the code can't tell the agent.

### Say less to discover

Say less when you don't know what you want yet. Steinberger does it deliberately:

> I purposefully under-prompt the agent so it would do something that would give me new ideas.
>
> Peter Steinberger

Most of what comes back isn't useful, he admits, but a couple of ideas usually are. DHH makes the same point from the agile tradition: nobody knows what software should do until they use it. In his words: "Be as vague as you can to manifest something, then interact with the something."

### Don't dictate every step

Experts can hurt results by over-prescribing. DHH relays, secondhand and unverified, that a coding-agent vendor cut its system prompt sharply because the agent "was actually being damaged by overly prescriptive humans". A system prompt is the standing instructions a vendor gives its own agent.

The pattern is familiar: dictate each step, and the agent follows your steps even where its own reading of the code would have found a better path. **Prescribe the outcome and the constraints the code can't tell it, not the steps.**

### What the code can't tell

The agent can't read these in the repository, so if you don't say them, it will guess:

- decisions already made,
- invariants, the things that must always hold true, and data rules,
- security constraints,
- interfaces other people depend on,
- what is out of scope.

### Three moments

| | Discovery | Delivery | Repair |
|---|---|---|---|
| | You don't know what you want. | You know what, not how. | It went wrong at the root. |
| How much to say | Little. Ask for options. | Precise on outcome and constraints. Silent on steps. | Explicit direction, in a fresh session. |

What each one sounds like with shelf:

- **Discovery:** "Shelf should be more useful for book clubs. Give me three directions, very different from each other."
- **Delivery:** "Stats print one line per status plus 'finished this year', calendar year in UTC like the stored timestamps. Plain text, no flags."
- **Repair:** "Start over. Keep storage unchanged; compute stats from existing fields only."

### Key points

- Under-prompt when you want ideas.
- Be precise about the outcome and the constraints the code can't tell.
- Don't dictate the steps, even as the expert.

## Part 4 · Review intent, not lines

<!-- minutes: 5 -->

> For any change that isn't trivial, the first thing you review is a plan, not a diff. Correct it in one sentence.

### A minute or twenty

A plan takes a minute to read. A 400-line diff takes twenty, and you can still miss the wrong assumption buried in it. The team that wrote HumanLayer's guide to context engineering for coding agents puts the economics plainly: "a bad line of a plan could lead to hundreds of bad lines of code."

How much code you read after that depends on risk, and module 07 explains how. What doesn't change: **never let the diff be the first place you discover what the agent decided.**

### Two ways to get a plan

| | Plan mode | Conversation |
|---|---|---|
| | A read-only mode. The agent explores and proposes a plan without editing files. | You talk it through, then say "explain what you're going to do", then "ok". |
| Where you find it | One of the permission modes in Claude Code. Codex has its own plan mode. | Any session |
| Who backs it | Anthropic, and the Codex guide for difficult or ambiguous work | Peter Steinberger, since late 2025 |
| When we use it | An agent that starts editing too early, or multi-file changes in unfamiliar code | A session that already has rich context |

Steinberger used to recommend plan mode. A few months later, in late 2025, he wrote that "Plan mode feels like a hack that was necessary for older generations of models", and now gets the same effect by talking and using trigger words. **His change of mind is the real lesson:** the best mechanism depends on this season's models. The goal doesn't change.

At The Agile Monkeys we use whichever mechanism keeps us reviewing intent rather than lines. Lab 2 invites you to try both on its first three steps, and to note which one kept you reviewing intent.

### Ask for the plan, then correct it

A plan review prompt that works: "Before building, write the plan in under 25 lines: files you'll change, any change to stored data and how existing files still load, the exact output (show an example), the tests you'll add and why each would fail without the change, and what you will not do. Then wait."

Answer with one-sentence corrections:

- "Don't add --json, that's another issue."
- "Use the calendar year in UTC, like the stored timestamps."
- "The tests must not depend on today's date; write the shelf file with fixed timestamps."

The last one is one of the two decisions lab 2 asks you to make: how to test "this year" whatever year the tests run in. Fixed timestamps are one option. Another is a counting function that takes today's date as a parameter, not a command-line option, because choosing a year is out of scope. You can also use both.

### Let the agent draw the system

Some problems are hard to see in plans or diffs, because they live in how pieces interact. For those, ask the agent to generate a visual description of the system from the code, read it, and correct it in a sentence or two.

At The Agile Monkeys, one of our engineers concluded the whole approach of a system was wrong and was about to redo it. Before that, they asked the agent for a visual architecture document generated from the code. It showed the real problem at once: when one step failed, nothing recorded it. The correction took one sentence. The agent proposed a plan, got an "ok", fixed the code and updated the document.

#### 1 · Don't edit it yourself

It is a thinking tool, not the deliverable. Editing it by hand costs your time and teaches the agent nothing. Tell the agent what's wrong, and let it fix the code and the document together.

#### 2 · Pictures, not paragraphs

Flowcharts, sequence diagrams and tables are faster to check than prose. You can spot a wrong arrow at a glance.

#### 3 · Ground it in the code

A generated diagram can show the design the agent expects rather than the one that exists. Ask it to cite file and line for every arrow.

For shelf, the prompt could be: "Read the code under shelf/ and write docs/architecture.md with: a Mermaid flowchart of how a command travels from the command line to the JSON file, a sequence diagram for 'shelf finish 3', and a table of every place that reads or writes the file. Cite file and line for each element. Mark anything you inferred rather than read." Mermaid is a text format that renders as diagrams. Lab 2 has this as an extra exercise.

### Make what comes back easy to read

The drawing rule works for everything you read, not only architecture. Your bandwidth limits you in both directions. Information goes in when you talk to the agent, give it whole goals, and point it at the sources instead of retelling them. Module 04 covers that side. It comes out as plans, explanations, reports and reviews, and a wall of text takes as long to read when an agent wrote it.

- **Explanations come with a picture.** A flowchart of what a pull request changes, a table of the cases an issue covers, a sequence diagram of a bug. If a paragraph needs a diagram to make sense, ask for the diagram.
- **Reports as a small HTML page.** For a status report, a comparison or a dashboard, ask for one self-contained HTML file with tables and charts. When something is wrong, you say so and the agent fixes a line. A generated image with three wrong words has to be generated again.
- **Write down once how you understand best,** as a personal skill, and reuse it on any issue, pull request or question. For example: start with one sentence on what changes for the user, then one diagram citing files and lines, tables rather than paragraphs, and end with what the agent is unsure about.

At The Agile Monkeys many of us stopped reading long text reports. We ask for a diagram or a small HTML page, review it in a fraction of the time, and answer with questions about the picture.

### Key points

- Review the plan before the diff, and correct it with one-sentence messages.
- When the problem is in how pieces interact, ask the agent to draw the system, and correct the drawing through the agent.
- Ask for what you read fastest: a diagram, a table or a small HTML page.

## Part 5 · Ask, then throw it away

<!-- minutes: 3 -->

> After building, a few short questions find problems nobody was looking for. When the work is wrong at the root, throw it away and start over. It's cheap.

### Questions that pay for themselves

A few short prompts find problems that neither you nor the agent was looking for.

#### 1 · "Do we have any side effects?"

Makes the agent look beyond the lines it changed. Steinberger found a hidden database-trigger bug only when he asked it.

#### 2 · "Now that you built it, what would you have done differently?"

After building, the agent knows the code better than when it planned. The answer often contains the refactor worth doing.

#### 3 · "Make it simpler."

Agents add layers and defensive code. DHH describes telling an agent a finished, reviewed change "looks a little too complicated", and watching it cut the code in half.

#### 4 · "What did you assume that you didn't check?"

Turns hidden guesses into a list you can review.

#### 5 · "What did you not run, and why?"

Separates "tests pass" from "the tests that exist and could run pass".

#### 6 · Not "is this correct?"

Agents tend to agree with the person asking. Ask "what is the strongest argument that this is wrong?" instead.

### Hindsight is a proposal

Treat the answers to "what would you have done differently?" as proposals, not orders. For each suggestion, decide:

- **Do it now,** if it's small and inside the scope of the change.
- **Write it down as a follow-up,** an issue for later.
- **Drop it.**

Don't let hindsight grow the change.

### Throwing work away is cheap

When code was expensive, patching a wrong implementation made sense. Now it often doesn't. Simon Willison, a developer who writes a guide to agentic engineering patterns, titles that chapter "Writing code is cheap now".

Steinberger changed a core architectural assumption of his project, from one agent to many, in about three hours with an agent. He estimates two weeks by hand.

### When to start over

Anthropic's Claude Code best practices give a concrete threshold: after two failed corrections on the same problem, stop, clear the session and start over with a better prompt.

> A clean session with a better prompt almost always outperforms a long session with accumulated corrections.
>
> Claude Code best practices, by Anthropic

Restart instead of patching when:

- the implementation is wrong at the root: wrong data model, wrong layer, wrong abstraction,
- you have corrected the same problem twice and it's still wrong,
- the agent is fixing its own fixes,
- the session is full of failed approaches that keep leaking back in.

Everything in a session shares its context window: the model's working memory for that session. It holds the conversation, the files the agent read and the output of its commands, and results get worse as it fills. That is also why mixing tasks hurts: one task, then an unrelated question, then back to the task. Keep one task per session, and clear it or start fresh between unrelated tasks.

### How to start over

Restarting well takes three steps:

- **Ask for the lessons.** In the failing session: "List in at most 10 bullets what we learned: constraints discovered, approaches that failed and why."
- **Discard the branch.** Nothing in it is precious. In lab 2 you remove the worktree and create a clean one, and the lab gives the commands.
- **Open a fresh session.** Paste the bullets and your decisions so far, and give explicit direction: plan first, then wait.

```prompt-weak
still wrong, the yearly count is off again. fix it
```

```prompt-strong
We're starting over on shelf stats. Lessons from the first attempt:
- finish timestamps are stored in UTC; "this year" means the calendar year in UTC
- the year-boundary tests failed depending on the day they ran; use fixed timestamps
- the first attempt changed storage and broke loading; storage stays unchanged
Plan first: compute stats only from existing fields, show me the plan and an
example of the output, and wait for my ok.
```

The better prompt gives the fresh session what the first one learned:

- **The constraints** it discovered.
- **What stays unchanged.**
- **A plan first,** and a wait for your ok.

In lab 2 the restart is optional: you practice it if two corrections on the same problem failed. It counts as a success. Log it as a correction.

### Key points

- After building, ask about side effects and what the agent would do differently.
- Don't ask "is this correct?". Ask for the strongest argument that it's wrong.
- After two failed corrections, collect the lessons and start a fresh session.

## Part 6 · Your correction log

<!-- minutes: 3 -->

> Every correction tells you something was missing. In lab 2, writing each one down is the real output.

### What lab 2 asks

In lab 2 you implement S3, an issue of the shelf practice project, called #3 in the lab's prompts: a stats command that prints four lines of counts. One agent, the full cycle. The issue fixes a lot: the four lines in order, zeros on an empty shelf, UTC, and that only the new command and its test file change. It also leaves things out of scope: statistics by author or tag, charts, and an option to choose a year.

S3 looks trivial. It isn't. It still leaves decisions open that are easy to miss:

- how to test "this year" without depending on the day the tests run,
- what to do with data the issue doesn't mention. A book can be added directly as done. And shelf doesn't check statuses yet, so a shelf file can already hold a status that isn't to-read, reading or done.

The point is to find those in the conversation, not in the diff.

### Before you start

You start from your own copy of the practice project from lab 0, with its tests passing on main. You work in a new worktree: an extra folder of the same repository, on its own branch. The lab gives you the commands. Open one session there. You can also do the lab on your own repository: pick a small feature that hides a definition question, such as a count, a date range or a time zone.

Use the strongest model you have access to, for planning, architecture, debugging and review. A weaker model's mistakes cost your attention, the scarcest resource you have. Move a job to a cheaper model only when you have evidence: an evaluation on your own tasks, or cost data showing it does as well.

Cheaper can work for well-specified volume. DHH describes a long port, rewriting existing code so it runs somewhere new, that several cheaper models completed at a fraction of the cost. One tried to cheat by wrapping an existing implementation and never finished. You find out by measuring. Module 08 goes deeper.

### The correction log

While you work, keep a correction log: one line every time you have to correct the agent. The pull request is the visible result, but the log is the real output of this lab. Lab 4 turns some of those lines into rules.

Keep it in your notes, not in the repository. Each row says:

- **Stage:** where in the cycle it happened.
- **What you corrected.**
- **What was missing.**
- **What would have prevented it.**

### What was missing

Every correction points to one of five causes:

- **Context:** the agent couldn't know.
- **Verification:** it could have checked and didn't.
- **Decision:** a product choice nobody had made.
- **Instruction:** it knew and ignored it.
- **Model:** a plain mistake.

### What would have prevented it

At the end of the lab, fill in the last column for every row:

- **A line in the instruction file,** for context or instruction. Module 04.
- **A check the agent runs itself,** for verification. Module 03.
- **A better question during discussion,** for a decision. This module.
- **Nothing:** it was a genuine judgment call.

### Where you correct

Then look at the whole log:

- **Where did most corrections happen?** In discussion and plan, or in build and verify? The earlier a correction happens, the cheaper it is.
- **Which cause dominated?** Many context rows mean your repository needs better instructions. Many verification rows mean the agent needs better checks. Many decision rows mean you are delegating choices that are yours.
- **What was your longest message?** Was it making up for context the session should already have had?
- **Did the agent find the open questions, or did you?** If you did, what would it have needed to find them itself?

### Key points

- In lab 2, the correction log is the real output.
- Each correction gets a stage, a cause and what would have prevented it.
- Use the strongest model unless you have evidence a cheaper one does as well.
