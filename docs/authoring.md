# Authoring guide

[Leer en español](authoring.es.md)

How to write for *Agentic Engineering 101*, whether you are a person or an agent
working for one. [AGENTS.md](../AGENTS.md) has the short version.

## Who we write for

An engineer who knows git and at least one language, may or may not use a
coding agent today, and has limited time. They will skip anything that doesn't
change what they do on Monday.

## Voice

- **Concrete first.** Start from a real situation, a real prompt or a real
  failure, then generalize. Explain *why* something matters before *how*.
- **Short sentences, plain words.** No hype ("revolutionary", "game-changing",
  "10x" without context). No filler.
- **Second person singular:** "you" in English, "tú" in Spanish.
- **Label wrong approaches clearly.** Showing a bad prompt next to a better one
  teaches more than describing the good one alone. We follow
  [Julia Evans' advice on explanations](https://jvns.ca/blog/confusing-explanations/).
- **Honest.** Keep the costs, the failure modes and the counter-evidence. When
  respected practitioners disagree, present both positions and say what we do
  and why.

### Company practice and people

- Our practice is written in company voice: "At The Agile Monkeys we…",
  "one of our engineers…". We never name employees or clients. The practice
  belongs to the team, not to one person.
- Contributors from outside can describe their own practice under their name,
  if they want, or anonymously.
- Numbers from our own practice are marked as *indicative, not benchmarks*.

### Citing public voices

- Cite people and docs by name, with a link, at first mention in each file.
- Quotes: verbatim, at most 25 words, linked to the source (with a timestamp for
  audio and video when you have one).
- In Spanish, translate the quote and add "(traducción propia)":
  `> «…» — DHH en [Lex Fridman Podcast #501](https://lexfridman.com/dhh-2/) (traducción propia)`
- Add every new external source to `content/*/reference/sources.md`.

### Tools

- **Principles in lessons, tools as examples.** A lesson should still make sense
  if the tool it mentions disappears next month.
- **Never invent a flag, command or config key.** Check the official
  documentation and link it.
- `content/*/reference/tools.md` is the dated home for tool detail that
  changes often. Update its `last_reviewed` date when you touch it. Lessons
  use concrete tool examples (a hook, a flag, a config file) where they teach
  a principle, checked against the official docs and linked.
- Don't name specific model versions in lessons. Write "the strongest model you
  have access to".

### Confidentiality

Nothing that couldn't go on a public blog: no client names, internal URLs,
infrastructure identifiers, credentials, commercial information or personal
data.

The repository is public, and so is its history. Don't reference our internal
meetings, talks or sessions, or attribute a practice to the colleague who
shared it, in the content, commit messages, pull request titles and
descriptions, or branch names. Write our practice in company voice. Outside
contributors can still describe their own practice under their name.

## Templates

`scripts/check_content.py` enforces the front matter and the required headings
below. Everything else is up to you.

### Lesson: `content/<lang>/NN-slug/README.md`

```markdown
---
title: "Close the loop"
module: 3
kind: lesson
minutes: 40
level: foundation        # foundation | intermediate | advanced
last_reviewed: 2026-09-17
---

# 3. Close the loop

> **In one sentence:** …

## What you'll be able to do
## Why this matters
## <your concept sections>
## Other ways to see it          (optional, strongly encouraged)
## Watch out
## Check your understanding      (answers inside <details>)
## Key points
## Go further                    (ends with "Next: …")
```

### Lab: `content/<lang>/NN-slug/lab.md`

```markdown
---
title: "Lab 3 — Give the agent a way to check itself"
module: 3
kind: lab
minutes: 45
level: foundation
last_reviewed: 2026-09-17
---

## Goal
## Before you start
## Steps                  (numbered, each with an observable checkpoint)
## Done when              (a checklist, ideally verifiable with a command)
## Reflect
## Stretch                (optional)
```

Every lab works on the [practice project](../practice/shelf/) *and* on the
reader's own repository.

### Reference and appendix pages

Front matter with `title`, `kind` (`reference` or `appendix`) and
`last_reviewed`. Free structure.

### Required headings by language

| English | Spanish |
|---|---|
| What you'll be able to do | Lo que serás capaz de hacer |
| Why this matters | Por qué importa |
| Other ways to see it | Otras formas de verlo |
| Watch out | Ojo con |
| Check your understanding | Comprueba lo que has aprendido |
| Key points | Ideas clave |
| Go further | Para profundizar |
| Goal | Objetivo |
| Before you start | Antes de empezar |
| Steps | Pasos |
| Done when | Cómo saber que has terminado |
| Reflect | Reflexiona |
| Stretch | Para ir más allá |

## Conventions

### Callouts

We use [GitHub alerts](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#alerts):

```markdown
> [!NOTE]
> **At The Agile Monkeys** we keep the always-loaded index under 100 lines.

> [!TIP]
> A practical shortcut.

> [!WARNING]
> A risk the reader must not miss.

> [!IMPORTANT]
> A rule we don't bend.
```

### Prompt pairs

````markdown
❌ **Weak prompt**

```text
fix the bug
```

✅ **Better prompt**

```text
The export command crashes on books without an author. Reproduce it with a
failing test first, then fix it. Don't change the CSV format.
```
````

Spanish labels: `❌ **Prompt débil**` / `✅ **Prompt mejor**`.

### Diagrams and links

- [Mermaid](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams)
  diagrams are welcome. Keep them small. No binary images.
- Use descriptive link text, never "here". Use relative links inside the
  repository.

## Spanish conventions

- Neutral Spanish, "tú". Avoid regional forms, and avoid "vosotros" and
  "ustedes" where you can.
- Keep these terms in English: prompt, commit, merge, pull request (PR), issue,
  backlog, worktree, hook, skill, token, pipeline, CI, checkout, workshop.
- Translate these: branch → *rama*, subagent → *subagente*, session → *sesión*,
  context window → *ventana de contexto*, plan mode → *modo plan*, blast radius
  → *radio de impacto*, lab → *laboratorio*, file → *archivo* (not
  "fichero"), cost → *coste*, merged → *mergeado*, lethal trifecta →
  *trifecta letal*.
- *Loop* has two translations. The guide's three loops and "close the loop"
  are *ciclo*: *ciclo interno*, *ciclo de contexto*, *ciclo externo*, *cerrar
  el ciclo*. An agent's own loop, review loops, the Ralph loop and other loops
  that keep going until something stops them are *bucle*: *bucle agéntico*,
  *bucle de revisión*, *cerrar el bucle de revisión con una decisión*. *Cycle
  time* is *tiempo de ciclo*.
- Explain these at first mention: *base de conocimiento (knowledge base)*,
  *revisión de código (code review)*, *pista de trabajo (track)*, *barrera de
  seguridad (guardrail)*, *modo headless (no interactivo)*, *agentic
  engineering (ingeniería agéntica)*, *validación local completa (full gate)*.
- The [glossary](../content/es/reference/glossary.md) is the reference. If you
  add a term, add it in both languages.

## Translation

- **English is the source of truth.** Spanish lives at the same path under
  `content/es/` (root files use a `.es.md` sibling).
- **Same pull request.** Every content change updates both languages. The
  Spanish is a natural adaptation, not a literal translation: same structure,
  same examples, same links.
- **Agents may draft, people review.** An agent-drafted translation needs a
  fluent human reviewer. Add the `translation-review` label if you can't do the
  review yourself (see the [AI policy](../AI_POLICY.md)).
- **Staleness is tracked from git history.** The validator warns when an
  English file was committed after its Spanish counterpart. Treat the warning as
  a to-do.
- More languages are welcome later. Open an issue first. We would add a new
  `content/<lang>/` tree, following
  [the Kubernetes localization model](https://kubernetes.io/docs/contribute/localization/).

## Before you open a pull request

- [ ] Both languages updated, same structure.
- [ ] `python3 scripts/check_content.py` passes.
- [ ] New commands and flags are checked against official docs and linked.
- [ ] Quotes are verbatim, ≤ 25 words and linked. New sources are in `sources.md`.
- [ ] No employee names, client names or confidential details.
- [ ] AI assistance disclosed in the pull request and commit trailers.
