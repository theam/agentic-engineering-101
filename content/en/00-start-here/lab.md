---
title: "Lab 0 — The whole game"
module: 0
kind: lab
minutes: 15
level: foundation
last_reviewed: 2026-11-27
---

# Lab 0 — The whole game

## Goal

Add a filter to Shelf, a small reading-list app. You’ll give one agent the task, try the filter on two books, and open a pull request in your own repository. Allow about 15 minutes for the exercise once your tools and project are ready.

## Before you start

You’ll need a terminal, Git, a GitHub account with the GitHub CLI signed in, Python 3.10 or newer, and one coding agent such as Claude Code or Codex. These commands assume a Bash-compatible shell (Git Bash or WSL on Windows). If your Python 3 executable is called `python`, use that throughout.

```sh
git --version
gh auth status
python3 --version
```

Open your usual coding agent once to check you can sign in. Keep command approvals on. If GitHub CLI needs a login, run [`gh auth login`](https://cli.github.com/manual/gh_auth_login).

### Make your practice repository

You’ll use this copy of Shelf again in later labs. If you already created your copy on GitHub, start at step 2. If you also cloned it, open its folder and go straight to **Check your setup**.

1. [Create my copy of Shelf](https://github.com/theam/shelf-starter/generate). Sign in to GitHub, choose your personal account as the owner and name the repository `shelf`. For an Academy hand-in, choose **Public** so the team can open your pull request. Click **Create repository**. You’ll land in your copy with the starter code and tests already in place.
2. [Clone your copy](https://cli.github.com/manual/gh_repo_clone) onto your computer. If you chose a different repository name, replace the first `shelf` in the clone command with that name. Keep the local folder `~/code/shelf` for the next labs.

   ```sh
   mkdir -p ~/code
   gh repo clone shelf ~/code/shelf
   cd ~/code/shelf
   ```

### Check your setup

Run these in your Shelf folder:

```sh
gh repo view --json nameWithOwner --jq .nameWithOwner
python3 -m shelf --help
python3 -m unittest
```

**Ready to start:** the first command prints your GitHub account and repository name, Shelf lists its commands, and the test run ends in `OK`. You can stop here and come back to this folder later. [GitHub CLI repository details](https://cli.github.com/manual/gh_repo_view)

## Steps

### 1. Give one agent a small change

Open your coding agent in the **Shelf** folder. Imagine you’ve added ten books and want to see just the ones you’re reading. Paste this task from the [S1 issue catalog](../../../practice/issues/en.md):

```text
Read README.md, AGENTS.md and the tests. In my Shelf repository, open an
issue titled "S1: Filter shelf list by status". Work on a new branch.
Add --status to shelf list. Keep the existing format and order. Accept
to-read, reading and done. For an invalid status, exit with code 2 and
list the valid values on stderr. If nothing matches, print
"No books with status reading." (use the requested status) and exit 0.
Keep shelf list without a filter working as before.
Add tests and run the full suite. Use temporary data for manual checks.
Show me your changes and test results before committing.
```

### 2. Try the change yourself

In another terminal, open the **same Shelf folder**, on the agent’s branch. Create a temporary reading list and compare the output of the two `shelf list` commands.

```sh
export SHELF_PATH="$(mktemp -d)/books.json"
python3 -m shelf add "Dune" "Frank Herbert"
python3 -m shelf add "Kindred" "Octavia E. Butler" --status reading
python3 -m shelf list
python3 -m shelf list --status reading
python3 -m unittest
```

The full list shows both books. The filter should print just `#2 [reading] Kindred by Octavia E. Butler`, and the tests should end in `OK`. If a check fails, give the agent the output and try again after its fix.

### 3. Open your pull request

Read the diff. Once the result matches what you expected, ask the agent to commit, push its branch and open a pull request against `main` **in your Shelf repository**. Ask it to include the test result and link the issue it opened. Open the URL and check the owner, the changed files and the test result.

## Done when

- [ ] The filter shows just the book you marked as reading, and all tests pass.
- [ ] You can open the pull request for S1 in your own Shelf repository.

**That completes Lab 00.** If you’re in Academy, paste the pull request URL into **Link to your work** and submit it. Keep your repository for later labs.

## Reflect

Save three lines for [Lab 1](../01-from-chatbot-to-system/lab.md): what you asked the agent to do, what you checked yourself, and where you spent time waiting.

## Stretch

**Optional, after module 03.** Try a second task, S2 (search by title or author), from the [issue catalog](../../../practice/issues/en.md). Open S2 as an issue in your practice repository. Give it to a second session in its own [Git worktree](../06-run-sessions-in-parallel/README.md). Ask a fresh session to [review a pull request](../07-agents-review-agents/README.md) against its issue and run the tests. Decide which findings to fix, merge the changes you accept, and remove the finished worktrees.

Start S2 from your Shelf folder. The second command opens a separate working folder on a new branch.

```sh
git fetch origin
git worktree add --no-track -b s2-search ../shelf-s2 origin/main
cd ../shelf-s2
```

Give the new session the actual S2 issue number. Ask it to show a test where searching for `GARCÍA` finds `García`, run the full suite and open its own pull request. Give the fresh reviewer the URL and ask: “Which acceptance criterion could still fail? Run the tests and show me the evidence.” For each finding, fix it, open a follow-up issue or record why you disagree. Once you’ve merged S2 and saved any work you want to keep, return to your main Shelf folder and run `git worktree remove ../shelf-s2`.
