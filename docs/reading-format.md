# Reading format

How to write `reading.md`, the written version of a module that
[Agentic Engineer Academy](https://academy.agentic-engineering.theagilemonkeys.com)
shows when a learner turns on **Reading mode**.

## What it is

- One `reading.md` per module, next to its lesson: `content/en/NN-<slug>/reading.md`,
  with its Spanish counterpart at `content/es/NN-<slug>/reading.md`.
- It is not the lesson and not the video script. It is the lesson understood
  and ordered for reading: one **part** per video of the module, in the same
  order and with the same title.
- Everything in it comes from the lesson, its lab and the glossary.
- Academy reads the English file from a pinned commit when it builds, and
  draws it with its own components. A module gets Reading mode only when
  Academy turns it on and its parts match the videos it publishes.

## Structure

```markdown
---
title: "From chatbot to system · Reading"
kind: reading
last_reviewed: 2026-11-27
---

# Module 01 · From chatbot to system

## Part 1 · What agentic engineering is

<!-- minutes: 4 -->

> The main idea of the part, in one or two sentences.

### First section

Paragraphs, bullet lists and **bold** as usual.

### Key points

- One line per idea the learner takes away. Nothing new here.

## Part 2 · …
```

- `## Part N · Title`: one per video, numbered 1, 2, 3… The title is the
  video's title. In Spanish, `## Parte N · Título`.
- `<!-- minutes: N -->`: reading time of the part. The only comment allowed
  inside a part.
- The first blockquote of a part, before any section, is its main idea.
- `### Title`: a section. Academy numbers sections 01, 02…
- `### Key points` (Spanish: `### Ideas clave`) closes the part with one
  bullet list.

## Special blocks

Only these. Anything else stops the Academy build with the file and line.

**Quote.** A blockquote of two paragraphs: the words, then who said them.

```markdown
> You can outsource your thinking, but you can't outsource your understanding.
>
> A line Andrej Karpathy quotes and keeps returning to.
```

**Comparison in columns.** A table whose first header cell is empty. The first
row, also with an empty first cell, holds one short sentence per option. Each
row after that asks the same question of every option.

```markdown
| | Autocomplete | Chatbot | System |
|---|---|---|---|
| | You type and accept. | You prompt, wait and read. | You design, decide and review. |
| Who writes | You | The agent | Agents, in parallel |
```

**Habits table.** A table of three columns: what you notice, what is missing,
and the module that teaches it.

**Cards.** One `#### Label · Title` heading followed by one paragraph. Cards in
a row form one group. The label can be a number (`#### 1 · Coherence`) or a
source and year (`#### METR · 2025 · 19% slower, felt 20% faster`).

**Weak and better prompt.** A `prompt-weak` code block, a `prompt-strong` code
block, one paragraph that says why the better one works, and one bullet list of
reasons.

````markdown
```prompt-weak
add csv export to shelf
```

```prompt-strong
Implement issue #4 (read it with gh issue view 4). …
```

The better prompt is short because it leans on a system:

- **An issue** that already holds the specification.
````

## Writing it

Follow the [authoring guide](authoring.md). Two extra rules for a reading:

- **The video is an extra. The text comes from the lesson and its lab.** A part
  usually carries a bit more than its video, summarized and structured for
  reading.
- **Introduce every person, study or term the first time it appears**, and keep
  each number with its limit when the lesson gives one.

Quotes and studies keep their links in the lesson. The reading cites them by
name, because Academy shows it without links.
