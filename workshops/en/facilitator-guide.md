---
title: "Facilitator guide"
kind: facilitator-guide
last_reviewed: 2026-09-17
---

# Facilitator guide

[Leer en español](../es/facilitator-guide.md) ·
[Workshop formats and agendas](README.md) ·
[Guide contents](../../content/en/README.md)

This guide is for the people who teach the taster, the intensive or the
follow-up, and for their helpers. Read it together with the
[workshop page](README.md), which has the agendas, the pre-work and the
metrics.

It assumes one thing: **you have done every lab yourself, on the current
version of the tools you will demo, within the last two weeks.** Coding agents
change every week. A demo that worked last month can behave differently today,
and you want to find that out at home, not in front of twenty people.

Many of the techniques here come from
[The Carpentries](https://carpentries.github.io/instructor-training/17-live.html),
who have taught programming in workshops for years: live coding, sticky notes,
minute cards, helpers. We adapted them to a subject with one new property: the
tool gives a different answer every time.

## Principles

1. **Live coding with real agents.** Type (or speak) the prompts live, with the
   same tools participants use. Follow the Carpentries advice: go slowly, use a
   large font, show every step, let people follow along. Don't replace demos
   with recordings when the network works. A recording teaches that agents are
   predictable, which is the wrong lesson.
2. **Narrate your decisions, not your keystrokes.** The skill we teach is
   judgment. Say out loud what you read, what you skip and why, when you stop
   the agent, and when you throw work away. For example: "I'm not reading this
   test file line by line. I'm checking that one test fails if I revert the
   change. I *am* reading the storage code, because that's where data gets
   lost."
3. **Expect failures and use them.** Agents will claim they are done without
   running the tests, wander out of scope and hit plan limits, often on the one
   day you are presenting. When it happens: stop, name the failure, ask the
   room what they would do, and recover with the practice from the module. A
   failure recovered live teaches more than a demo that went smoothly. Each
   module below lists its common failures and a recovery. If the recovery fails
   too, switch to the backup (the catch-up kit or a recording, labeled as one)
   and debrief it.
4. **Hands on keyboards early; keep talks short.** No talk over 25 minutes. The
   first lab starts within 35 minutes of the opening.
5. **Principles over tools.** A room with several vendors is a good room. It
   shows that the practice isn't tied to a product. Don't let tool debates eat
   lab time: write them on a "parking lot" sheet and come back at a break.
6. **Honest numbers.** Our own numbers are indicative, not benchmarks, and the
   research is mixed. Say so every time a number appears.
7. **Model safe habits.** Never use a permission-bypass mode on your demo
   machine, never show a secret, never let an agent merge. What you do on the
   projector is what people copy.
8. **Protect people's energy.** Running several agents is, in
   [Simon Willison's words](https://simonwillison.net/2025/Oct/7/vibe-engineering/),
   "surprisingly effective, if mentally exhausting." Enforce the breaks. Never
   rank individuals.

## Before the workshop

### Pre-flight checklist

**Two weeks before:**

- [ ] You walked through every lab end to end, on the current versions of the
  tools you will demo, within the last 14 days.
- [ ] You checked the `last_reviewed` date of the
  [tools reference](../../content/en/reference/tools.md). If a command or feature
  changed, you opened a
  ["tool drift" issue](https://github.com/theam/agentic-engineering-101/issues/new?template=tool-drift.yml)
  and adjusted your demo.
- [ ] You prepared the catch-up kit (see below).
- [ ] You recorded short videos of four key demos, as a fallback for network
  failures: the whole game (Lab 0), the "done without tests" moment (module 03),
  three parallel worktrees (module 06) and a fresh-context review (module 07).
- [ ] You calculated the room's cost budget and arranged the emergency pool (see
  [Cost budgeting for the room](#cost-budgeting-for-the-room)).
- [ ] You briefed the helpers (30 minutes: this guide's failure lists, the
  five-minute rule, security).

**Three days before:**

- [ ] You reviewed the pre-work confirmations and contacted anyone stuck.
- [ ] You assigned learning paths from the registration answers and planned the
  pairs (see [Managing mixed levels](#managing-mixed-levels)).
- [ ] Remote: breakout rooms, the status board, the minute-card form and the
  survey form are ready.

**The day before, or that morning:**

- [ ] **Demo machine:** a separate operating-system user or a virtual machine
  with no production credentials; chat and email notifications off (agent
  notifications on, because you will demo the round-robin); a large terminal
  font; a clean shell history; a browser profile without personal accounts.
- [ ] **No private rules leaking into the demo.** User-level instruction and
  memory files apply to every session and can contain company rules or personal
  details. Check what your agent loads globally (for example
  [Claude Code memory](https://code.claude.com/docs/en/memory) and
  [AGENTS.md in Codex](https://learn.chatgpt.com/docs/agent-configuration/agents-md)),
  or use a clean user.
- [ ] Two agent vendors signed in, the strongest model you have access to
  selected, and you know how much of your plan is left.
- [ ] A fresh copy of the practice project for the demos, plus a spare copy in
  case the first one gets messy.
- [ ] The network tested in the room with several laptops running agent
  sessions; a charged hotspot.
- [ ] Printed or offline copies of the [issue catalog](../../practice/issues/en.md)
  and of the kickoff prompt anatomy from
  [lesson 05](../../content/en/05-decompose-into-tracks/README.md), for the
  unplugged activities.
- [ ] Sticky notes in two colors for everyone, index cards, markers, a timer,
  and a whiteboard or wall for the sprint board.

### Helpers

Helpers make or break a hands-on workshop. Plan one for every 8–10
participants.

- They have done every lab.
- They go to the "help" sticky notes first. They ask "What did you ask the
  agent?" and "What did it answer?" before touching anything.
- **They don't take the keyboard.** They guide.
- **Five-minute rule:** if a problem isn't solved in five minutes, pair the
  participant with a neighbor, write the problem down, and come back to it at the
  break.
- They collect failure stories for the debriefs, with the participant's
  permission.
- They watch for security slips: a secret on screen, a bypass mode on a laptop
  with credentials.

### The catch-up kit

Build it once from your own run-through and reuse it:

- A reference `AGENTS.md`, `kb/ACTIVE.md` and one decision record for the
  practice project (from your Lab 4).
- A working guard (from your Lab 3).
- Three kickoff prompts for Lab 6 (from your Lab 5), one per track: track A
  (S4 and S5), track B (C1) and track C (C2), with the note on how C1 and C2
  conflict.
- A pull request description with an intent statement, and a sample triage
  ledger (from your Lab 7).

Share the pieces in the room chat or a shared document when someone falls
behind. Issues S1–S6 are independent, so a participant who didn't finish one
lab can start the next from wherever they are: the labs say where a
still-open issue goes. Only two steps depend on earlier output. Lab 5 reuses the
C1/C2 decision record from Lab 4, and the start of Day 2 needs Lab 5's issues
and kickoff prompts. The kit covers both.

## Signals and feedback in the room

### Sticky notes and remote equivalents

Give every participant sticky notes in two colors. A note on the laptop lid
means "I need help". The other color means "I'm done" or "all good". No note
means "working".

- **Use them as instant polls:** "Put up your 'done' note when your tests pass
  on `main`." You see the state of the room in five seconds.
- **Pick colors that everyone can tell apart.** The Carpentries tradition is red
  and green, which many people with color-vision deficiency can't distinguish.
  Use two colors that differ in lightness (for example yellow and dark pink) and
  write **HELP** and **OK** on them.
- **Remote:** use the platform's reactions or raised hand, or better, a shared
  status board: a table with one row per participant and a status column with
  `OK`, `HELP` or `WORKING`. A dedicated chat channel where people post
  `HELP: <one line>` works too. One helper watches the board full time.

### Minute cards

At lunch and at the end of each day, every participant writes two things on an
index card, anonymously: **one thing that worked** and **one thing to change,
or that is still unclear**. Read them at the break. Open the next session by
spending two minutes on the top two themes. It shows people you listen, and it
catches confusion before it compounds. Remote: an anonymous two-question form,
with the link posted five minutes before the break.

### Timekeeping and the cut list

- Keep a visible timer for every lab. Announce when 10 minutes and 2 minutes
  are left.
- At the end of a lab, if more than half the room still has "help" notes up,
  extend once by up to 10 minutes. Then demo the finish and share the catch-up
  kit.
- When you run late, cut in this order:
  1. The debrief after Lab 0 goes down to 5 minutes.
  2. Lab 8 becomes homework, done in follow-up week 4 with real data.
  3. Lab 1 is finished at home (most of the baseline is pre-work anyway).
  4. The sprint shrinks to 60 minutes.
- **Never cut** Lab 3 (guards), Lab 5 (Day 2 depends on it) or Lab 7 (review).

## Managing mixed levels

Every room mixes the three learning paths from
[module 00](../../content/en/00-start-here/README.md). Ask these questions in
the registration form:

1. Last week, what is the largest number of agent sessions you had working at
   the same time? (0 / 1 / 2–4 / 5+)
2. How often do you use a coding agent? (never / weekly / daily)
3. Have you used git worktrees? (no / tried / regularly)
4. Do you lead a team or decide how your team works? (yes / no)
5. On a scale of 1–5, how confident are you at: designing tasks an agent can
   verify; keeping context between sessions; running three or more sessions in
   parallel; reviewing agent pull requests with agents; estimating cost per
   merged PR?
6. What do you want to leave with?

Newcomers are mostly "never/weekly" with 0–1 sessions. Daily single-agent users
are "daily" with 1 session. Tech leads answered yes to question 4, and anyone
already at 2–4 or 5+ sessions takes that path's stretch goals.

| | Newcomer to agents | Daily single-agent user | Tech lead, or already runs parallel sessions |
|---|---|---|---|
| **Before Day 1** | Pre-work, plus one small task with the agent on the practice project | Pre-work | Pre-work, and skim lessons 05–07 |
| **In labs** | Core steps only; pair up in labs 0–2 | Core steps, then "Stretch" if time allows | "Stretch" sections; the C1/C2 track; S7 |
| **Parallel target on Day 2** | 2 sessions | 3–4 sessions | 5 or more |
| **Role in the room** | Drives in pairs | — | Table lead: answers questions before helpers do, without taking keyboards |
| **Watch for** | Overwhelm; copying prompts without reading the output | Old habits: long "perfect" prompts, reading every line of every diff | Boredom; building tooling instead of doing the lab; taking over their pair |

Seat one tech lead at each table. Pair across levels for labs 0–2, where the
experienced person's questions help. Pair similar levels for labs 6–7, where
people run at very different speeds.

Peter Steinberger calls the tech-lead failure mode the agentic trap: spending
your time on orchestration, custom commands and home-made tooling instead of
shipping (see ["Just Talk To It"](https://steipete.me/posts/just-talk-to-it)).
Name it kindly and point back to the lab.

## Per-module notes

Each module has the same five parts: when it happens, what to demo, the "aha"
to land, the common failures and how to recover, and a question for the room.
Times refer to the intensive's agenda on the [workshop page](README.md).

### Taster

**Slot:** the whole 90 minutes.

**Demo:** the whole game, fast. Prepare a fresh practice copy, but do the
discussion, the plan and the build live.

**The aha to land:** *the engineer spent the session deciding, not typing.*

**Common failures:**

- **The agent is slow and the demo stalls.** Don't wait in silence. Move to the
  next part (create the worktree, start S2) and come back when the notification
  arrives. That *is* the lesson: DHH describes agents on the
  [Lex Fridman Podcast](https://lexfridman.com/dhh-2/) as "at once both too fast
  and too slow", and parallel sessions are the answer to the waiting.
- **The agent finishes S1 perfectly and runs the tests itself.** Good. For the
  failure moment, show the guard blocking a test you break on purpose.

**Ask the room:** "Which step felt like the agent's job, and which felt like
yours?"

### Module 00 — Start here (Lab 0)

**Slot:** Day 1, 09:20–10:35 (15-minute talk, 45-minute lab, 15-minute debrief).

**Demo:** don't demo the whole lab before people do it. Show only the first two
prompts (ask the agent to explain the project, discuss S1), then let the room go
and walk around. The pre-work covered the lab's "Before you start" section. For
anyone who skipped it, a helper runs those commands with them at the back of the
room while the lab starts.

**The aha to land:** *in 45 minutes you had one agent building, another working
in parallel and a third reviewing. You didn't understand every step, and you
didn't need to yet.*

**Common failures:**

- **`gh pr create` fails.** Usually the user isn't authenticated or the copy was
  never pushed. Check `gh auth status` and `gh repo view`. If it still fails,
  skip the PR and have the fresh session review the branch locally, from
  `git diff main...s1-status-filter`.
- **The agent asks permission for every test run.** Show how to allow the test
  command in the agent's permission settings (for Claude Code, see
  [permission modes](https://code.claude.com/docs/en/permission-modes)). Don't
  switch to a bypass mode.
- **Someone starts S2 in the same folder as S1.** Ask what happens when two
  agents edit files in the same checkout at the same time. Create the worktree
  now. That's module 06 in one question.
- **`python` is not found** (common on macOS). Use `python3 -m unittest`, and
  tell the agent in the session so it stops retrying.
- **The reviewer approves everything.** Fine for Lab 0. Ask the reviewer "What
  would make this PR fail review?" and point to module 07.

**Ask the room:** "What did the agent do that you didn't ask for?"

### Module 01 — From chatbot to system

**Slot:** Day 1, 10:50–11:30 (20-minute talk, 20-minute lab). Participants
logged their week at home, so the 20 minutes cover only the last part of Lab 1:
computing the numbers, writing the baseline and setting targets.

**Demo:** no code. Run the poll from the registration form again with sticky
notes on the wall (0 / 1 / 2–4 / 5+ sessions last week). Present the METR
results honestly: in the
[2025 study](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/),
experienced developers expected a speedup, were measured slower, and still
believed they had been faster.

**The aha to land:** *the ceiling is not the prompt, it's the system around the
agent. And feeling faster isn't evidence, which is why you measure your own
baseline.*

**Common failures:**

- **An evidence debate takes over.** Give both sides two minutes, write it on
  the parking lot, and come back to "you will measure your own numbers".
- **No baseline data** (the pre-work was skipped). Rebuild last week: merged PRs
  from `gh pr list`, sessions from memory, and mark every number as estimated.
- **Someone feels behind.** The baseline poll can sting. Say it plainly: nobody is being ranked, everyone arrives at a different point, and this gap closes in weeks, not years. Point to the DHH quote in module 00.
- **A skeptic feels the room is selling something.** Welcome it. The guide's
  claim is quality first, and each lesson has an "Other ways to see it" section
  with the open disagreements.
- **Our indicative numbers get treated as targets** (for example, stories per
  person per day). Repeat that they compare apples and oranges: a reference, not
  a benchmark.

**Ask the room:** "What would convince you, with your own numbers, that this is
working, or that it isn't?"

### Module 02 — One agent, done well

**Slot:** Day 1, 11:30–12:45 (20-minute demo, 55-minute lab).

**Demo:** use S7, the deliberately vague request, for the discussion only, so
you don't solve S3, which is the lab:

```text
Let's discuss issue S7 before building anything: "Make shelf more useful for
book clubs." Read the code first. Give me three options with trade-offs.
Don't change any files until I say build.
```

Pick one option out loud and say why. Ask for a plan. If time allows, build a
small slice, verify it, and finish with "Now that you built it, what would you
have done differently?"

Participants take S7 through this discussion themselves in the Day 2 sprint, so
present your option as one example, not as the answer.

**The aha to land:** *short messages work when the session has context. Review
the intent (the plan) before you review lines.*

**Common failures:**

- **The agent starts building during the discussion.** Stop it and say
  explicitly: "We're discussing; don't edit files." Discard the changes (for
  example `git restore .` for tracked files, and ask the agent to remove new
  files it created). Throwing work away is cheap. Say that out loud too.
- **Participants spend 15 minutes crafting a perfect prompt.** Ask them to send
  the rough version and let the agent ask the questions.
- **The correction log is empty.** Ask: "Which of its choices would you have
  questioned in a colleague's pull request?"
- **Plan mode versus conversation turns into an argument.** Both are fine. The
  test is whether you reviewed the intent before the code existed.
- **A participant can't judge the Python.** Pair them up, and have them ask the
  agent to explain the diff in plain language and show the test that proves it.
- **The S3 tests depend on today's date.** "Books finished this year" tests that
  build their data from the real clock pass today and can fail on January 1st.
  Ask the room: "Would this test still pass next year?" Then have the agent fix
  the date in the test instead of reading the clock.

**Ask the room:** "Where did you correct the agent, and could that correction
have gone into the context instead?"

### Module 03 — Close the loop

**Slot:** Day 1, 13:45–14:50 (20-minute demo, 45-minute lab).

**Demo:** use a request whose obvious implementation breaks an existing test.
In `shelf`, `tests/test_store.py` pins the exact fields stored for each book, so
something like this works:

```text
Add an optional --notes option to shelf add and store the notes with the book.
Keep it short.
```

Live, run it without a guard. If the agent reports "done" without running the
tests, run `python3 -m unittest` yourself on screen: the stored-format test
fails. Then add the guard, for example a Stop
[hook](https://code.claude.com/docs/en/hooks) that runs the tests or, for agents
without hooks, a git `pre-commit` hook, and run the request again.

The same demo shows the difference between updating a test and weakening it.
Adding a field on purpose means the pinned fields must change, and that's
correct. Deleting the pin so anything passes is not. Ask the room which one the
agent did.

Be honest when the agent behaves well: it may run the tests on its own and get
it right. Say "Today it did. The guard turns 'usually' into 'always'", then
break a test on purpose and show the guard blocking.

As Peter Steinberger says on
[The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/the-creator-of-clawd-i-ship-code):
"you have to close the loop. It needs to be able to debug and test itself.
That's the big secret."

**The aha to land:** *prose asks; hooks enforce. When a check fails, fix the
change, not the check.*

**Common failures:**

- **The agent says "done" but the tests weren't run.** Don't argue with the
  claim. Ask for evidence: "Show me the test output." Then add the guard. The
  lesson is to ask for evidence, not assertions.
- **The agent "fixes" the failure by weakening, skipping or deleting a test.**
  This is the best teaching moment of the day. Stop, show the diff of the test
  file, and name it. In ["Vibe engineering"](https://simonwillison.net/2025/Oct/7/vibe-engineering/),
  Simon Willison calls agents "weird digital interns who will absolutely cheat
  if you give them a chance." Restore the test, add a rule to `AGENTS.md`, and
  note that review (module 07) is the second line of defense.
- **The guard never fires.** Usually it's in the wrong place, not executable, or
  attached to the wrong event. Before trusting any guard, test it with a
  deliberately failing test. Start with a hook that only prints a line.
- **The guard blocks forever.** A flaky test, a broken environment or a missing
  interpreter keeps the agent looping and burning tokens. Stop the session. Make
  the guard tell "tests failed" apart from "tests could not run", and have the
  agent report exactly what was not run and why.
- **Someone wants a bypass mode "to go faster".** Not on this machine. Explain
  that bypassing permissions belongs only in an isolated environment with
  nothing to steal. Module 09 covers the rest.

**Ask the room:** "Which rule in your real project gets broken again and again,
and what check would catch it every time?"

### Module 04 — Context is infrastructure

**Slot:** Day 1, 15:05–16:10 (20-minute demo, 45-minute lab).

**Demo:** open a fresh session in a practice copy with no instruction files and
no knowledge base, and ask:

```text
What are we doing in this repository and why? What have we decided about tags
and about versioning the storage format?
```

Nothing in the code can answer the second question, so the answer is generic or
invented. Add the `AGENTS.md`, `kb/ACTIVE.md` and decision record from your
catch-up kit, start a new session, and ask again. Then show "remember this"
turning a correction into a note.

**The aha to land:** *every session starts with amnesia. A knowledge base makes
"a new session with full context" cheap, and the agent writes it, not you.*

**Common failures:**

- **Participants write the knowledge base by hand.** Redirect: talk to the agent
  and let it write; correct it in one sentence when it's wrong.
- **`AGENTS.md` grows long and generic** ("write clean code"). Apply the test
  from [Anthropic's best practices](https://code.claude.com/docs/en/best-practices)
  to each line: would removing it cause a mistake? Keep `ACTIVE.md` under 100
  lines.
- **The before/after comparison looks the same.** The practice project is small
  and the agent can read all of it in seconds. Ask about *why* and *what's next*
  (decisions, parked options), which code can't answer. Be honest that the gap
  is much bigger in real repositories with history.
- **The knowledge base isn't committed.** Run `git status` at the end of the lab:
  an uncommitted knowledge-base change did not happen.
- **Claude Code ignores `AGENTS.md`.** It reads `CLAUDE.md`; add a `CLAUDE.md`
  that imports `@AGENTS.md` (see [memory](https://code.claude.com/docs/en/memory)).
- **Tech leads start building a library of skills.** Create a skill when
  something hurts, not in advance: skills cost context.

**Ask the room:** "What did you explain to an agent this month that you'll have
to explain again tomorrow?"

### Module 05 — Decompose into tracks

**Slot:** Day 1, 16:10–17:10 (15-minute talk, 45-minute lab).

**Demo:** the first two minutes of the lab only. Ask the agent to explain how it
will create and group the issues *before* it creates any. Show that you review
the grouping, not every issue body.

The catalog's prompt deliberately leaves out each issue's "Parallel safety"
note, so the agent has to find the conflicts itself. The catalog ends with an
answer key (files per issue, verified overlaps and a suggested three-track
split). Read it before the workshop, and ask participants not to open it until
the lab is over.

**The aha to land:** *size by blast radius. Independent tracks touch disjoint
files, not disjoint titles. Merge order is not work order.*

**Common failures:**

- **The agent doesn't notice that C1 and C2 conflict.** Ask it to list the files
  and data structures each issue changes. It will see that both change
  `shelf/models.py`, `shelf/store.py` and the stored-format test in
  `tests/test_store.py`. That's the lesson: conflicts show up in the blast
  radius, not in the titles.
- **The agent flags every shared file as a conflict.** S5, C1 and C2 all touch
  `shelf/store.py`, but S5 only adds a method in a part of the file the other
  two don't change, and git merges it cleanly. If S1 or S6 is still open, each
  has a small textual overlap with C1 (`shelf/commands/list_books.py` and
  `shelf/commands/add.py`) that git or an agent resolves in minutes. C1 against
  C2 is different: a semantic conflict that needs a human decision. Ask the
  agent to tell the two kinds apart.
- **The agent splits one issue into PR1/PR2/PR3, or creates many micro-issues.**
  One PR end to end. Human review is the expensive step, and scope instructions
  don't survive phases.
- **Duplicate issues.** The agent retried a command that had actually succeeded.
  List them with `gh issue list` and close the duplicates with `gh issue close`.
  Lesson: after writing through a CLI or API, re-read and verify.
- **Kickoff prompts are one line, or three pages.** Check them against the
  anatomy in [lesson 05](../../content/en/05-decompose-into-tracks/README.md):
  what I already checked, decisions already made, done when, what to report
  back.
- **Filing lots of issues very quickly.** GitHub may treat it as spam: DHH's bot
  was flagged after filing 28 issues at once. The catalog is small; don't ask
  the agent to generate dozens more.
- **The room runs out of time.** Hand out the catch-up kit's kickoff prompts so
  everyone can start Day 2.

**Ask the room:** "Which of these tracks could run at the same time as the
others, and how do you know?"

### Day 2 opening

Spend two minutes on the minute cards. Then do a sticky-note check: working tree
clean, issues exist (`gh issue list`), three kickoff prompts committed, Day 1
plan usage written down. Hand out the catch-up kit to anyone missing a piece.

### Module 06 — Run sessions in parallel

**Slot:** Day 2, 09:15–11:00 (25-minute demo, 80-minute lab).

**Demo:** create Lab 6's three worktrees from a freshly fetched `origin/main`,
with `--no-track` so no branch tracks `origin/main`
([lesson 06](../../content/en/06-run-sessions-in-parallel/README.md#a-worktree-recipe-that-doesnt-bite)
explains why):

```bash
git fetch origin
git worktree add --no-track -b s4-export ../shelf-a origin/main
git worktree add --no-track -b c1-tags ../shelf-c1 origin/main
git worktree add --no-track -b c2-file-version ../shelf-c2 origin/main
git worktree list
```

(Claude Code can also create them for you with
[`claude --worktree <name>`](https://code.claude.com/docs/en/worktrees).) Start
one session per worktree with its kickoff prompt, and name each session. Keep a
plain shell next to each one. When notifications arrive, handle them
round-robin, highest priority first. Finish by removing a worktree with
`git worktree remove`.

Present the disagreement: we use notifications to drive the round-robin, while
Mitchell Hashimoto recommends the opposite in
["My AI Adoption Journey"](https://mitchellh.com/writing/my-ai-adoption-journey):
"Turn off agent desktop notifications. Context switching is very expensive."

**The aha to land:** *waiting on one agent kills flow. With three running you're
always deciding, and your attention, not the agents, sets the ceiling.*

**Common failures:**

- **Two parallel tracks conflict (C1 and C2).** It's planned, and it's subtler
  than it looks. Git merges `shelf/models.py` and `shelf/store.py` without
  complaint and stops only on `tests/test_store.py`. Whichever side of that test
  you take, a stored-format test fails, because nobody has decided what version 2
  of the file contains. A clean textual merge is not a resolved conflict: run the
  tests. Recovery: merge track A first. Then stop and make the human decision out
  loud. **C1 first:** version 2 includes `tags`, and the migration from version 1
  gives old books an empty tag list; one version, less code. **C2 first:** C1
  bumps `SCHEMA_VERSION` to 3 and adds a migration from version 2; more code,
  but it's what a real project does once version 2 has shipped. Write the
  decision down, then, in the second worktree, run `git fetch origin` and
  `git merge origin/main` and give the agent that decision with the tests as
  referee. Ask the room which order they would choose. Neither is wrong. The
  mistake is letting the agent choose by accident.
- **The agent "resolves" the C1/C2 conflict by deleting the other side's test.**
  The suite goes green and one pin is gone. Treat it like any weakened test:
  restore it, make the decision above, and have the agent update the pin
  deliberately.
- **All three sessions run in the same folder.** Files get overwritten and tests
  flip between passing and failing. Stop all three, run `git status`, discard
  anything nobody can explain, create the worktrees and restart from the kickoff
  prompts. Starting over is cheaper than untangling.
- **Sessions see each other's books.** The tests use a temporary file, but when
  an agent tries the command by hand it uses the default data file
  (`~/.shelf.json`), shared by every worktree. Set `SHELF_PATH` to a different
  file in each worktree. It's the small version of the shared databases and
  ports you'll meet on real projects.
- **Git refuses to create a worktree because the branch is already checked out
  elsewhere.** Run `git worktree list`, then pick a new branch name or remove the
  old worktree. After deleting worktree folders by hand, `git worktree prune`
  cleans up.
- **A participant freezes with three notifications waiting.** Drop to two
  sessions and handle the top of the list first. It's normal.
- **Plan limits hit mid-lab.** Pair up: the person with quota left drives the
  sessions; the other plans the merges, reads the diffs and keeps the log. Move
  a low-risk track to a second vendor if someone has one. Write down when it
  happened: it's data for Lab 8.
- **A prompt goes into the wrong session.** This is why sessions have names.
  If the session is confused, clear it (`/clear` in Claude Code) or start it
  again from its kickoff prompt.
- **Worktrees left behind.** `git worktree list` and `git worktree remove` are
  part of "done".

**Ask the room:** "What did you do while all three agents were working, and was
that a good use of your attention?"

### Module 07 — Agents review agents

**Slot:** Day 2, 11:15–12:30 (20-minute demo, 55-minute lab).

**Demo:** open a *fresh* session in the pull request's worktree:

```text
Review pull request <number> in this repository. You have no memory of how it
was built. Intent: <one sentence>. Context: shelf is a local, single-user
command-line tool; it is not internet-facing. Report only correctness bugs,
missing tests for the intended behavior, and deviations from the intent. For
anything else, ask me instead of recommending it. Give file:line and evidence
for each finding.
```

Then run a reviewer from a second vendor (see the
[tools reference](../../content/en/reference/tools.md)). Build the triage ledger
live, one verdict per finding: FIX_NOW, DEFER_TO_ISSUE or DISCARD, each with a
one-line reason. Close the loop by decision.

Lab 7 is written for 75 minutes of self-paced work. In the room's 55 minutes,
run one review round, apply one batch of fixes and go straight to the closing
decision. A second round is homework.

**The aha to land:** *the writer shouldn't be the only reviewer. The intent
statement is the ruler, and review loops end by decision, not by exhaustion.*

**Common failures:**

- **The reviewer causes scope creep.** For example, "sanitize input against SQL
  injection" in a tool that stores JSON, or "add a plugin system for exporters".
  Check each finding against the intent and DISCARD or DEFER_TO_ISSUE it with a
  reason. A good real example comes from S5: a reviewer may notice that removing
  the newest book lets its id be reused. The issue lists that as out of scope, so
  it's DEFER_TO_ISSUE, not FIX_NOW. Tell our story here.

  > [!NOTE]
  > **At The Agile Monkeys** our first review-triage agent accepted every
  > comment. One pull request of about 5,000 changed lines grew to 20,000–40,000
  > as the reviewer chased unlikely threats in an internal tool. The fix was to
  > give reviewers the PR's goal and the project context, and to make them ask a
  > human when unsure.

- **The reviewer approves everything.** Ask for evidence: "Which test fails if
  this behavior is reverted? Revert it and run that test." Or rely on the
  second-vendor reviewer.
- **Round three finds problems caused by round two's fixes.** Findings have
  become derivative. Classify, reply, resolve, and file one follow-up issue. In
  the workshop, allow two rounds at most. One of our large pull requests went
  through about 20 automated review rounds and more than 200 threads before we
  learned this (indicative).
- **Nobody at the table has a second vendor.** Use the same vendor in a fresh
  session with an adversarial role, or swap pull requests with a neighbor who
  uses a different vendor.
- **Review comments posted to GitHub flood everyone's notifications.** Keep the
  first round inside the session. Post to GitHub once, to practice replying to
  and resolving threads.
- **A security finding shows up on a toy project.** Security findings are never
  simply discarded. Classify it with the context (a single-user local tool) and
  write down the reasoning. That habit is the lesson.

**Ask the room:** "Which finding did you discard, and would you defend that
decision to a teammate?"

### Module 08 — Token economics

**Slot:** Day 2, 13:30–14:20 (20-minute talk, 30-minute lab).

**Demo:** your own numbers, prepared beforehand: plan fees prorated to one week,
divided by the PRs you merged that week. Then your top token sinks. Hide billing
and account details.

**The aha to land:** *measure cost per merged PR, not cost per token. Heavy
usage isn't waste if it merges, and light usage isn't thrift if nothing ships.*

> [!NOTE]
> **At The Agile Monkeys** one of our engineers used up a top-tier plan's weekly
> allowance in two days, running about 20 agents that coded, reviewed each other's pull
> requests and maintained the product knowledge base. Nothing was broken.
> Consumption follows skill.

**Common failures:**

- **Company-managed plans hide usage.** Estimate, mark the number as estimated,
  and ask the administrator later.
- **A debate about vendor prices.** Prices change every few months; the method
  doesn't. Point to the vendors' own pricing pages and move on.
- **Shame, in either direction.** High or low usage isn't a grade. The ratio to
  outcomes is what matters.
- **Workshop numbers look meaningless** (two PRs in a day). They are. Lab 8
  rehearses the calculation, and the real number comes in follow-up week 4.
- **Hitting plan limits as a badge of honor.** A limit is a signal to look for
  sinks: review loops chasing scope creep, bloated always-loaded context,
  sessions running long past their useful context.

**Ask the room:** "Which one change would cut your token use without cutting what
you merge?"

### Parallel sprint

**Slot:** Day 2, 14:20–16:30 (10-minute briefing, 90-minute sprint, 30-minute
review).

**Setup:** draw a board on the wall or in a shared document with four columns:
**Planning** (agent), **In progress** (agent), **Ready for a human** (human
decides), **Merged** (human). It previews module 09's human and agent columns.
Next to it, keep room totals without names: the most sessions any one person
sustained, PRs merged, review rounds, PRs reverted.

**Briefing:** read the sprint rules from the [workshop page](README.md) aloud,
and the targets per learning path.

**Variant for experienced groups:** trios share *one* repository. Merge races
become real. Appoint a merge captain who rotates every 30 minutes, and only the
captain merges.

**During the sprint:** walk the room. At minute 25, run a sticky-note poll:
"OK note if your S7 discussion outcome is written and your new issues exist."
At minute 45: "OK note if you have merged at least one PR." Collect failure
stories. Remind people to take a break while their sessions run.

**Sprint review:** show the totals, one triage ledger on screen (ask a volunteer
first) and the best recovered failure. Celebrate the recoveries.

**Common failures:**

- **Everyone hits plan limits around the same time.** Pair up, open the
  emergency pool, and move people with no quota left to reviewing others' pull
  requests.
- **Nothing merges because reviews never close.** Close by decision after two
  rounds.
- **`main` breaks after a merge** (shared-repository variant). Stop merges. The
  person who merged fixes forward with an agent, and then adds a guard for what
  broke.
- **Someone builds orchestration tooling instead of shipping.** Name the agentic
  trap and point back to the issues.
- **S7 gets built without a discussion.** Ask to see the discussion outcome. If
  there isn't one, that's the lesson.
- **The S7 discussion eats the sprint.** Stop it at about 20 minutes. A
  good-enough option split into two small issues teaches more than a perfect
  plan with nothing merged.
- **Two new S7 issues edit the same files.** Ask the agent to sort each overlap,
  as in Lab 5. Same lines but no shared contract, for example two new options
  on `shelf list`, is a textual overlap: run both and resolve it at merge time.
  Two issues that both add fields to the stored book are a semantic conflict,
  C1 and C2 again: only one of them can take the next `SCHEMA_VERSION`, so
  decide the order before either session starts.
- **An S7 option changes the file format.** Most book-club ideas do, and C2 has
  already versioned it. The new issue must bump `SCHEMA_VERSION` and add a
  migration. Good work for the most experienced participants.

### Follow-up: modules 09 and 10

**Slot:** four weekly check-ins (see the [workshop page](README.md)).

**How to run the check-ins:**

- Talk about numbers and patterns, not code. Real code goes on screen only with
  permission.
- Keep the one-number round short and never rank anyone.
- Demo on the practice project, never on a participant's repository.

**Optional security demo (week 3 clinic):** on your isolated demo machine, with
no secrets on it, create an issue in the practice repository whose body contains
instructions aimed at an agent (for example, asking it to print environment
variables). Then ask an agent to triage the open issues and watch whether it
follows them. Discuss untrusted input, the
[lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)
and why a human runs production-privileged commands. Never do this on a machine
with credentials.

**Where people stall, week by week:**

- **Week 1 (context).** They design the perfect knowledge base, or write
  documentation by hand all week. Budget one hour, and let the agent write it.
- **Week 2 (guards).** They spend days perfecting hooks. One guard, for one rule
  the agent actually broke, is enough. Mention the agentic trap again.
- **Week 3 (parallel tracks).** Real repositories need services: ports,
  databases and environment files for each worktree. On our machines, memory
  runs out at around five or six full local stacks (indicative). Start with
  tracks that don't need the stack (tests, documentation, command-line tools,
  refactors) and add per-branch stacks later. Teammates who weren't at the
  workshop may resist the working agreement: present it as a proposal backed by
  your numbers.
- **Week 4 (review and economics).** No numbers were collected. Rebuild them from
  `gh pr list` and the usage view, and mark them as estimated.

**Other common situations:**

- **The employer doesn't allow agents on the chosen repository.** Don't break the
  policy. Use an internal tool or an open-source project the participant
  contributes to, and bring the working agreement to the team as a pilot
  proposal.
- **People drop out.** Expect it. Send the weekly message with a single goal,
  and keep the trios going so people stay accountable to each other.
- **Regulated industries.** Nobody we know has a flow yet that is both efficient
  with agents and gives the control and traceability regulated work requires.
  Say so, collect ideas, and invite a "share your practice" issue.

## Fallback plans

| Problem | First move (5 minutes or less) | If it persists | Prevention |
|---|---|---|---|
| **The venue network fails** | Facilitator on the hotspot; participants pause their agents | Switch to an unplugged block: decompose the printed issue catalog, review a printed plan and diff, build a triage ledger from a printed review, draft an `AGENTS.md`. Show the recorded demos | Test the network with agents running; bring a hotspot and printouts |
| **A vendor has an outage** | Check the vendor's status page; switch to a second vendor | Reorder the agenda: talks and unplugged work now, labs later | Facilitators sign in to two vendors; ask participants with a second plan to bring it |
| **Rate or plan limits** | Pair up | Open the emergency pool; move people to review roles; lower the number of parallel sessions | Pre-work plan check; room budget |
| **Broken install** | A helper, five minutes | Pair with a neighbor; use a cloud development environment prepared in advance | Pre-work commands and a confirmation form |
| **Locked-down corporate laptop** (proxy, no admin rights, blocked CLI) | Pair up | A spare machine or virtual machine; ask the person to bring another machine on Day 2 | Ask about it in the registration form |
| **An agent does something destructive** | Stop the session; `git status`; restore from git | A fresh copy of the practice project | No production credentials; push the practice copy often |
| **Your demo fails badly** | Name it; try one recovery | Use the catch-up kit or the labeled recording; debrief the failure | Rehearse within 14 days |
| **GitHub rate limits or spam flags** | Stop bulk actions; slow down | Keep working on local branches and review diffs locally | Small issue catalog; no bulk generation |
| **Running late** | Apply the cut list | — | Visible timer |

The agents used in this guide run on cloud models, so the labs need the
network. There is no offline version of them, which is why the unplugged block
exists.

## Cost budgeting for the room

Somebody pays for the tokens. Decide who before registration opens.

**Three ways to pay:**

1. **Bring your own plan.** The default for open workshops. The pre-work asks
   people to check their limits. Expect some entry-level plans to run out on
   Day 2.
2. **Organization seats.** Provision one seat per person at least a week
   before, so participants can set up at home.
3. **API keys with hard spending caps.** One key per participant or per pair,
   each with a cap. Revoke all of them the same day the workshop ends.

Never share a personal subscription login with participants. It is a security
problem, and plans are usually meant for one person.

**Worksheet: measure, don't guess.**

| Line | How to get it |
|---|---|
| A. One participant's Day 1 | Run all Day 1 labs yourself at workshop pace, then read your usage view |
| B. One participant's Day 2 | Run labs 6–8 plus a 90-minute sprint with 3–5 sessions, then read your usage view. Day 2 usually costs several times Day 1, because sessions run in parallel and reviewers reread code |
| C. Per participant | (A + B) × a safety margin, for example 1.5, because participants retry more than you do |
| D. The room | C × number of participants |
| E. Emergency pool | Enough for about a fifth of the room to finish Day 2 on capped API keys |
| F. Facilitators | Your own A + B again, plus rehearsals |

**Rules:**

- Teach with the strongest model you have access to. A weaker model to save
  money teaches the wrong limits. If the budget forces a compromise, say so in
  the room.
- Cap every key, never put keys on slides or in chat, and revoke all workshop
  keys at the end.
- Ask participants to write down their usage at the end of each day. It's their
  data for Lab 8.
- Vendors publish typical usage figures, for example Anthropic's
  [costs page for Claude Code](https://code.claude.com/docs/en/costs). A
  workshop day with parallel sessions sits well above a typical day, so treat
  those figures as a floor.

## After the workshop

### Survey at the end of Day 2

Keep it under five minutes and anonymous.

1. How useful were the two days for your work? (1–5)
2. Pace of Day 1 and of Day 2: too slow / about right / too fast.
3. Which module helped you most? Which one least?
4. Did your setup work? If not, what broke?
5. The most sessions you kept working at the same time during the sprint.
6. Confidence now, 1–5, on the five skills from the registration form:
   designing tasks an agent can verify; keeping context between sessions;
   running three or more sessions in parallel; reviewing agent pull requests with
   agents; estimating cost per merged PR.
7. The one thing you will do differently next week.
8. What felt like hype, or wrong? What should we change?
9. May we use anonymous aggregates of your answers to improve the guide? (yes /
   no)

### Survey at the end of week 4

1. Your before/after table for the six metrics (from Lab 10).
2. Which practice stuck? Which did you drop, and why?
3. Did quality suffer? Reverted PRs, bugs, incidents, rework.
4. Confidence now, 1–5, on the same five skills.
5. Did your team adopt anything? What got in the way?
6. Would you recommend the workshop to a colleague? Why or why not?
7. May we use anonymous aggregates? (yes / no)

### Message templates

**Same day, after Day 2:**

```text
Subject: Agentic Engineering 101: your next four weeks

Hi <name>,

Thanks for these two days. Three things before tomorrow:

1. Survey (5 minutes, anonymous): <survey link>
2. Clean up: commit and push your practice repository, remove the worktrees
   you created (git worktree list), and make sure no workshop API keys remain
   on your machine. We revoke them tonight.
3. Week 1 of the follow-up starts now. Focus: context. On your real
   repository, create AGENTS.md and a kb/ with ACTIVE.md. Guide: <link to
   lesson 04> and <link to lesson 10>.

Check-ins: <day and time>, weekly for four weeks: <video link>.
Bring one number: the most sessions you kept working at the same time.

<facilitator name>
```

**Before each weekly check-in:**

```text
Subject: Check-in <n> of 4: <week focus>

Hi everyone,

This week's focus: <context | verification and guards | parallel tracks |
agent review and economics>.

The one thing to try before <day>: <single concrete goal>.
Bring: <what to bring, from the workshop page>.

Stuck? Post in <chat channel> with what you asked the agent and what it
answered.

Check-in: <day and time>, <video link>.
```

**After the final session:**

```text
Subject: Agentic Engineering 101: results and what's next

Hi everyone,

Thanks for four weeks of practice. The cohort's anonymous before/after:
<aggregate table>. Remember these numbers are indicative, not a benchmark.

Two asks:
1. Final survey (5 minutes): <survey link>
2. Share one practice you discovered with the guide's community, in a
   "share your practice" issue:
   https://github.com/theam/agentic-engineering-101/issues/new?template=share-your-practice.yml

The guide keeps changing as the practice does. Keep an eye on it and tell us
when something is wrong or out of date.

<facilitator name>
```
