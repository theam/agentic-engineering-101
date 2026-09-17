# AI policy

[Leer en español](AI_POLICY.es.md)

This guide teaches people to build software with AI agents, so banning AI
contributions would make no sense. But a contribution costs maintainers review
time whoever or whatever wrote it. These rules keep that cost fair.

They are adapted from the policies of [LLVM](https://llvm.org/docs/AIToolPolicy.html),
[Ghostty](https://github.com/ghostty-org/ghostty/blob/main/AI_POLICY.md),
the [Linux kernel](https://docs.kernel.org/process/coding-assistants.html) and
[Fedora](https://docs.fedoraproject.org/en-US/council/policy/ai-contribution-policy/).

## The rules

1. **A human is accountable.** Every issue, pull request and comment is
   submitted by a person who stands behind it. Agents prepare work. People
   submit it. We don't accept pull requests opened autonomously by agents
   without a human who reviewed them first.
2. **Disclose the assistance.** Fill in the "AI assistance" section of the pull
   request template: which tool and model, and what it did (drafted text,
   translated, checked links, wrote code…). Add a trailer to commits where an
   agent contributed:

   ```text
   Assisted-by: Claude Code (<model>)
   ```

   Agents must never add `Signed-off-by` or any other attestation on behalf of
   a human.
3. **Understand and verify what you submit.** Read the whole diff. Run
   `python3 scripts/check_content.py`. If you changed a lab, do the lab. If you
   changed the practice project, run its tests. If a claim or quote came from an
   agent, open the source and confirm it says that.
4. **No extractive contributions.** A contribution should give more than it
   costs to review. Large, unrequested, lightly checked changes (a whole new
   module generated in one go, mass rewording, bulk issues) will be closed with
   a pointer to this policy. Propose big changes in an issue first.
5. **Translations may be drafted by agents, but reviewed by people.** A fluent
   human reviews every agent-drafted translation before merge. Use the
   `translation-review` label if you can't do that review yourself.
6. **Keep confidential material out.** Don't paste private code, client
   information or credentials into prompts used to write for this repository,
   and never into the repository itself.
7. **Maintainers use AI too, under the same rules.**

## Why "disclose" and not "forbid"

Disclosure helps reviewers put their attention where it is needed. It also
builds a public record of how people use agents to write educational material,
which is itself part of what this guide is about. Using an agent will never
count against you. Skipping disclosure or verification will.
