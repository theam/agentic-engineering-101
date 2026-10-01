# AGENTS.md

Instructions for AI coding agents working in this repository. Human
contributors: [CONTRIBUTING.md](CONTRIBUTING.md) covers the same rules at a
friendlier pace.

## What this repository is

**Agentic Engineering 101** is a bilingual (English and Spanish) educational
guide by The Agile Monkeys. It teaches software engineers to go from using one
coding agent to running many in parallel, without losing quality. It is
prose, not an application. The only runnable code is the practice project in
`practice/shelf/` and the validator in `scripts/`.

## Map

```text
content/en/NN-<slug>/README.md   lesson (front matter + required headings)
content/en/NN-<slug>/lab.md      hands-on lab (front matter + required headings)
content/en/reference/            glossary, tools, prompt patterns, sources
content/en/appendix/             appendix pages
content/es/...                   Spanish: same paths, same file names
workshops/{en,es}/               workshop agendas and facilitator guide
practice/shelf/                  practice project (Python 3.10+, stdlib only)
practice/issues/{en,es}.md       issue catalog the labs use
docs/authoring(.es).md           style guide, templates, translation workflow
scripts/check_content.py         structure, bilingual parity and link validator
```

## Commands

```bash
python3 scripts/check_content.py                            # must pass before you finish
npx markdownlint-cli2 "**/*.md"                             # Markdown style (CI runs it)
cd practice/shelf && python -m unittest                     # practice project tests
```

## Rules

1. **Both languages, same change.** Edit the English file and its Spanish
   counterpart (same path under `content/es/`, or the `.es.md` sibling at the
   root) in the same change. English is the source of truth. The Spanish text
   is a natural adaptation, not a literal translation. Follow the glossary and
   conventions in [docs/authoring.md](docs/authoring.md#spanish-conventions).
2. **Keep the templates.** Lessons and labs need the front matter keys and the
   H2 headings listed in [docs/authoring.md](docs/authoring.md#templates).
   The validator enforces them. Don't rename required headings.
3. **Company voice, no personal names.** Company practice is written as "At The
   Agile Monkeys we…". Never name employees or clients. Never include internal
   URLs, infrastructure identifiers, commercial information or anything
   confidential.
4. **Cite public voices by name, with a link.** Quotes must be verbatim, at most
   25 words, and linked to the source. In Spanish, translate the quote and add
   "(traducción propia)".
5. **Don't invent tool behavior.** Every CLI flag, command, config key or
   feature you mention must be checked against official documentation, with a
   link. `content/*/reference/tools.md` is the dated home for tool detail that
   changes often; update its `last_reviewed` date when you change it. Lessons
   may use concrete tool examples where they teach a principle, verified and
   linked the same way.
6. **Stay honest.** Keep the caveats, the counter-evidence and the "other ways
   to see it" sections. Don't turn disagreements into certainties, and don't
   add marketing language. ProductPlot, a product in development, appears only
   in the appendix. Open-source tools we maintain (claude-dev-kit, Facility,
   Limina) may appear where they teach a practice: say what we use them for,
   keep their limits and the alternatives, say that none of them is required
   to follow the guide, and never make the guide depend on them.
7. **Update links when you move things.** Relative links are validated.
   Renaming a module folder means updating every link to it, in both languages.
8. **Small, focused changes.** One topic per pull request. Don't reformat files
   you aren't changing.

## AI contributions (read this even if you think you know)

This repository welcomes AI-assisted work under our [AI policy](AI_POLICY.md):

- A **human is accountable** for every contribution. Don't open issues or pull
  requests on your own initiative. Prepare the change, then let your human
  review and submit it.
- **Disclose** the assistance: fill in the "AI assistance" section of the pull
  request template, and add an `Assisted-by: <tool> (<model>)` trailer to your
  commits. Never add `Signed-off-by` or any other human attestation for your
  human.
- **Verify before claiming done:** run `python3 scripts/check_content.py`. If
  you changed a lab, walk through its steps. If you changed the practice
  project, run its tests. Report exactly what you ran and what you did not.
- Don't paste confidential material into this repo or into prompts about it.

## Definition of done

- [ ] English and Spanish updated together, with the same structure.
- [ ] `python3 scripts/check_content.py` passes.
- [ ] New external claims have working links. New quotes are verbatim and ≤ 25 words.
- [ ] No employee names, client names or confidential details.
- [ ] Commits carry an `Assisted-by:` trailer, and the pull request description has an "AI assistance" section.
