# Contributing

[Leer en español](CONTRIBUTING.es.md)

Thanks for helping. This guide exists because the practice of agentic
engineering is still being worked out, and no single team has seen enough of it.
Your experience, including what failed, makes the guide better for everyone who
reads it next.

## Ways to contribute

| You want to… | Do this |
|---|---|
| Fix a typo, a broken link or a wrong command | Open a pull request directly |
| Report something wrong or confusing | [Open a "content error" issue](https://github.com/theam/agentic-engineering-101/issues/new?template=content-error.yml) |
| Share how you or your team do something | [Open a "share your practice" issue](https://github.com/theam/agentic-engineering-101/issues/new?template=share-your-practice.yml). It is the most valuable contribution we get |
| Report that a tool changed (flag renamed, feature gone) | [Open a "tool drift" issue](https://github.com/theam/agentic-engineering-101/issues/new?template=tool-drift.yml) |
| Propose a new lesson, lab or section | [Open a "lesson proposal" issue](https://github.com/theam/agentic-engineering-101/issues/new?template=lesson-proposal.yml) and discuss it before you write |
| Improve the Spanish (or English) wording | [Open a "translation" issue](https://github.com/theam/agentic-engineering-101/issues/new?template=translation.yml) or a pull request |
| Run a workshop with this material | Go ahead (CC BY 4.0), then tell us what worked in a "share your practice" issue |

## How a change gets in

1. **Small fixes:** open a pull request.
2. **Anything bigger** (a new section, a changed recommendation, a new lab):
   open an issue first so we can agree on the direction before you write in two
   languages.
3. Create a branch, make the change in **English and Spanish**, and run the
   checks below.
4. Open a pull request using the template. Fill in the **AI assistance**
   section, even when the answer is "none".
5. A maintainer reviews it. We aim to reply within a week. Content changes need
   one maintainer approval. Changes to a recommendation, or to the structure of
   the guide, need the discussion in step 2.

### Both languages in the same pull request

English is the source of truth, but the Spanish version is not an afterthought.
Update both in the same pull request. If you can't write one of the two
languages well:

- write the one you can,
- let an agent draft the other (disclose it), and
- add the `translation-review` label so a fluent reviewer checks it before
  merge.

Details are in [docs/authoring.md](docs/authoring.md#translation).

### Local checks

```bash
python3 scripts/check_content.py                 # structure, bilingual parity, relative links
npx markdownlint-cli2 "**/*.md"                  # Markdown style (optional locally; CI runs it)
cd practice/shelf && python -m unittest          # only if you changed the practice project
```

CI runs the same checks and also tests external links.

## Style

Read [docs/authoring.md](docs/authoring.md) before writing. In short:

- Concrete first, short sentences, explain *why*, label wrong approaches.
- Company practice is written as "At The Agile Monkeys we…". Your own practice
  can be written as "one team we know…" or with your name, if you want the credit.
- Cite public voices by name with a link. Quotes must be verbatim and at most 25 words.
- Keep the caveats. When practitioners disagree, show both sides.
- Never include confidential information: client names, internal URLs,
  credentials, anything you couldn't post on a public blog.
- Don't reference internal meetings or sessions, or who shared a practice, in
  the content or in commit messages, pull requests and branch names. All of it
  is public.

## AI-assisted contributions

Welcome, under our [AI policy](AI_POLICY.md). The short version: a human is
accountable for every contribution, AI assistance is disclosed, and everything
is verified before it's submitted. Agents: read [AGENTS.md](AGENTS.md).

## Maintainers

This project is maintained by The Agile Monkeys. Current maintainers:

- [@javiertoledo](https://github.com/javiertoledo)

Maintainers review pull requests, triage issues and decide on changes to the
structure and recommendations of the guide. We decide by discussion in the
issue or pull request, and maintainers make the final call when there is no
consensus. We will open maintainer roles to regular contributors as the
community grows.

To report a Code of Conduct concern privately, message a maintainer through
their GitHub profile. If the concern involves a maintainer, contact another
maintainer.

## Recognition

Every merged contribution is credited in the git history. Contributors who
share practices that end up in a lesson are credited in that lesson's "Go
further" section, if they want to be.

## License of contributions

By contributing, you agree that your contributions are licensed under the
repository's licenses: [CC BY 4.0](LICENSE) for guide content and
[MIT](LICENSE-CODE) for code. This follows the "inbound = outbound" rule in
[GitHub's Terms of Service](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service#6-contributions-under-repository-license).
There is no CLA to sign.

Everyone who takes part agrees to our [Code of Conduct](CODE_OF_CONDUCT.md).
