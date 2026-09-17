---
title: "Lab 3 — Give the agent a way to check itself"
module: 3
kind: lab
minutes: 45
level: foundation
last_reviewed: 2026-09-17
---

# Lab 3 — Give the agent a way to check itself

## Goal

Add a deterministic guard to the practice project: a Stop hook that won't let the agent finish its turn while the tests fail. Then give an agent a task, tell it *not* to run the tests, and watch the hook catch its mistake and send it back to fix the code.

You will practice four ideas from [module 3](README.md): an executable specification (tests written first), a hook that blocks with exit code 2, testing a guard before trusting it, and proving that the tests fail when the change is reverted.

## Before you start

- Your own copy of the practice project, set up as in [Lab 0](../00-start-here/lab.md), with a clean `main` and passing tests. The steps assume it lives in `~/code/shelf`; use your own path if it differs.
- Python 3.10 or newer. The hook script uses only the standard library.
- Claude Code or Codex. Steps show Claude Code first. Codex differences are marked.
- About 45 minutes.

**On your own repo:** pick a small behavior change you can describe in two sentences and a test command that finishes in under a minute. The hook script below runs `python3 -m unittest`; change that one line to your fast test command (`npm test`, `pytest -q`, `go test ./...`). If your full suite is slow, gate on a fast subset and leave the rest to CI.

> [!TIP]
> The steps pin the exact error messages in the tests, following the S6 acceptance criteria in the [issue catalog](../../../practice/issues/en.md): this lab's pull request closes S6, so it must meet them. Pinning the wording is on purpose: the agent that implements the feature won't be told the wording, so its first attempt will probably miss, and you'll see the hook do its job.

## Steps

### 1. Record the baseline (2 minutes)

```bash
cd ~/code/shelf
git switch main && git pull
git switch -c lab-3-gate
python3 -m unittest
```

**Checkpoint:** the last lines say `Ran N tests` and `OK`. Write N down. It is 13 on a fresh copy, more if you merged pull requests from earlier labs.

### 2. Write the specification as failing tests (10 minutes)

Issue S6 ("Reject empty titles and unknown statuses") asks `shelf add` to reject bad input. Today `--status` accepts any text. Start a session in your copy and type:

```text
We are going to implement issue S6: `shelf add` must reject an empty or
whitespace-only title and an unknown --status. Don't implement anything yet.
Only write failing tests in tests/test_cli.py, in the AddCommandTest class,
using the existing ShelfTestCase helper. For each bad input, the tests must
expect exit code 2, a stderr that contains the usage line (usage: shelf add)
and ends with exactly one of these lines, and no shelf file afterwards:
  shelf add: error: title must not be empty
  shelf add: error: unknown status 'finished' (use to-read, reading or done)
Run python3 -m unittest and show me that only the new tests fail, and why.
Then stop.
```

**Look for:** the new tests fail *for the right reason*: the command currently accepts the input and exits 0, so the exit code or the message doesn't match. A test that fails because of a typo, an import error or a wrong helper name is a broken test, not a red one. If you see that, ask the agent to fix the test and run it again.

Commit the red tests on your branch, then **exit the session**:

```bash
git add tests
git commit -m "S6: failing tests for input validation"
```

**Checkpoint:** `python3 -m unittest` ends with `FAILED`, only the new tests appear in the failures, and `git status` is clean.

> [!IMPORTANT]
> Exit that session before step 3. Claude Code reloads hook settings while a session runs. An open session holding a red suite would be blocked by the new gate the next time it tries to stop.

### 3. Install the gate by hand (5 minutes)

Create the two files below yourself, by copying and pasting.

> [!TIP]
> Why by hand? The suite is red on purpose, and the gate runs at the end of every agent turn. An agent that creates the gate would be blocked by it at the end of that same turn and would start implementing S6. A guard and a deliberately red state don't mix, which is also why the red and green steps of TDD should happen in one agent turn once a gate exists.

`scripts/stop_gate.py`:

```python
#!/usr/bin/env python3
"""Stop hook: the agent can't finish its turn while the test suite fails.

Works as a Claude Code or Codex Stop hook. Standard library only.
"""

import json
import subprocess
import sys
import tempfile
from pathlib import Path

MAX_BLOCKS = 3   # consecutive blocks before we let the agent stop and warn you
TAIL_LINES = 40  # lines of test output sent back to the agent

event = json.load(sys.stdin)

# Test the project the agent is working in. `cwd` follows it into worktrees.
here = Path(event.get("cwd") or ".").resolve()
root = next((p for p in (here, *here.parents) if (p / "pyproject.toml").exists()), None)
if root is None:
    sys.exit(0)  # not inside the project: nothing to check

result = subprocess.run(
    [sys.executable, "-m", "unittest"], cwd=root, capture_output=True, text=True
)
counter = Path(tempfile.gettempdir()) / f"stop-gate-{event.get('session_id', 'unknown')}"

if result.returncode == 0:
    counter.unlink(missing_ok=True)
    sys.exit(0)  # silent success

# stop_hook_active is true when the agent is already continuing because a Stop hook blocked it.
blocks = int(counter.read_text()) if event.get("stop_hook_active") and counter.exists() else 0
if blocks >= MAX_BLOCKS:
    counter.unlink(missing_ok=True)
    warning = f"Stop gate: tests still fail after {MAX_BLOCKS} attempts. Don't trust this turn's work."
    print(json.dumps({"systemMessage": warning}))  # shown to you, not to the agent
    sys.exit(0)

counter.write_text(str(blocks + 1))
tail = "\n".join((result.stdout + result.stderr).strip().splitlines()[-TAIL_LINES:])
print(
    "The test suite fails, so you can't finish yet.\n"
    "Fix the code, not the tests: don't skip, delete or weaken a test.\n"
    f"Last lines of `python -m unittest`:\n{tail}",
    file=sys.stderr,
)
sys.exit(2)  # 2 blocks the stop; any other non-zero code would not
```

`.claude/settings.json` (for Claude Code):

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"${CLAUDE_PROJECT_DIR}/scripts/stop_gate.py\"",
            "timeout": 120
          }
        ]
      }
    ]
  }
}
```

**Codex:** create `.codex/hooks.json` instead, with the same structure and this command: `"python3 \"$(git rev-parse --show-toplevel)/scripts/stop_gate.py\""` ([Codex hooks](https://learn.chatgpt.com/docs/hooks)). Codex loads project hooks only in a trusted project, and runs a new hook only after you review and trust it with `/hooks`.

The retry cap matters most for Codex: Claude Code gives up after 8 consecutive blocks on its own, but the Codex documentation describes no such limit.

**Checkpoint:** both commands below print no errors.

```bash
python3 -m json.tool .claude/settings.json
python3 -m py_compile scripts/stop_gate.py
```

### 4. Test the gate before you trust it (5 minutes)

A guard you have never seen fail is not a guard. Feed the script a fake Stop event, the same JSON the agent tool would send:

```bash
echo '{"cwd": "'"$PWD"'", "session_id": "manual", "stop_hook_active": false}' \
  | python3 scripts/stop_gate.py
echo "exit code: $?"
```

On your branch the suite is red, so you should see the tail of the failures and `exit code: 2`.

Now check the passing path. Your untracked gate files come with you when you switch branches:

```bash
git switch main
echo '{"cwd": "'"$PWD"'", "session_id": "manual", "stop_hook_active": false}' \
  | python3 scripts/stop_gate.py
echo "exit code: $?"
git switch lab-3-gate
```

**Checkpoint:** you saw `exit code: 2` with failing test names on `lab-3-gate`, and `exit code: 0` with no other output on `main`. Commit the gate:

```bash
git add scripts .claude          # Codex: git add scripts .codex
git commit -m "Add a Stop hook that runs the tests"
```

### 5. Let the agent run into the gate (15 minutes)

Start a **new** session in your copy. In Claude Code, type `/hooks` and confirm a Stop hook from Project Settings is listed. In Codex, trust the hook in `/hooks`. Then:

```text
Implement this: `shelf add` must reject an empty or whitespace-only title and
an unknown --status. Report both as usage errors, like the rest of the command
line: the usage line, then a clear error message, exit code 2, and nothing
saved. Keep the change small. For this exercise only: don't read or run the
tests. Stop as soon as you think the code is done.
```

**Look for:**

- When the agent stops, the hook blocks it. In Claude Code the transcript shows the hook's message with the failing tests.
- The agent reads the failures and changes **the code**, most likely `shelf/commands/add.py` and possibly `shelf/cli.py`: the message wording, the usage line, the exit code (today `cli.py` turns a command error into exit code 1, not 2), or several of them. A common first attempt is argparse's `choices=` for `--status`: it exits with 2, but its own message doesn't match the specification.
- It tries to stop again, and the gate runs again. Count the rounds.

If the agent edits a test to match its own wording, interrupt it and type: `Revert your changes to tests/. The messages in the tests are the specification.` That is the verification ratchet from the lesson, happening live.

If the agent got everything right on the first try, the gate stayed silent, which is also correct. Confirm with `python3 -m unittest`.

**Checkpoint:** `python3 -m unittest` passes, and this prints nothing (the agent didn't touch the specification):

```bash
git diff HEAD -- tests/
```

### 6. Prove the tests can fail (3 minutes)

Remove the implementation, keep the tests, and run the suite. The implementation isn't committed yet, so use the stash recipe from [the lesson](README.md), which also stashes any file the agent added under `shelf/`:

```bash
git stash list           # note what is already there
git stash push --include-untracked -m revert-check -- shelf/
git stash list           # the top entry must say revert-check
python3 -m unittest      # expected: the S6 tests fail again
git stash pop            # only if the top entry is revert-check
python3 -m unittest      # expected: OK
```

**Checkpoint:** red without the change, green with it.

### 7. Commit and keep the gate (5 minutes)

```bash
git add shelf
git commit -m "S6: validate title and status in shelf add"
git push -u origin lab-3-gate
gh pr create --fill
```

Merge the pull request when you're happy with it. Later labs run many sessions at once, and each of them will inherit this gate. S6 is now done: when [Lab 5](../05-decompose-into-tracks/lab.md) turns the issue catalog into GitHub issues, it creates S6 and closes it with a link to this pull request.

## Done when

- [ ] `python3 -m unittest` prints `OK`, with more tests than the N you wrote down in step 1.
- [ ] `git log --oneline main..lab-3-gate` shows three commits: failing tests, the gate, the implementation.
- [ ] `git log --oneline main..lab-3-gate -- tests/` shows exactly one commit: the agent never changed the specification.
- [ ] You saw the gate return exit code 2 by hand (step 4), and you saw it block the agent at least once, or you confirmed the agent passed on the first try.
- [ ] With `shelf/` stashed, the suite fails (step 6).

## Reflect

- How many times did the gate block the agent, and what did it change each time? Was the failure output enough for it, or did it guess?
- The gate also stops the agent from pausing to ask you a question while the suite is red. Where would that hurt on your own repository, and is a cap of 3 right for it?
- Which rule in your own repository is still only prose, and has been missed at least twice? Which rung of the ladder (hook, validator, CI, server) would enforce it?
- Your gate lives in files the agent can edit. What stops an agent from weakening it, and who would notice?

## Stretch

- **Make the ratchet mechanical.** Extend `stop_gate.py` so it also fails when the number of tests drops or tests are skipped. `unittest` prints `Ran N tests`, and it counts skipped tests as run, so check for `skipped=` as well. Store the minimum in `scripts/min_tests.txt` and raise it, never lower it, when the suite grows.
- **Add permission tiers.** In `.claude/settings.json`, allow `Bash(python3 -m unittest *)`, ask for `Bash(git push *)` and `Bash(gh pr create *)`, and deny `Read(./.env)`. Check that the prompts you still get are the ones that matter ([permissions](https://code.claude.com/docs/en/permissions)).
- **Run the same gate in both tools.** If you have Claude Code and Codex, configure both files and give the same task to each. Compare how each tool shows the block and how each agent reacts.
- **On your own repo:** add the gate with your fastest test command, and keep it for a week. Note every block: was it a real mistake, a flaky test, or a gate that was too slow?
