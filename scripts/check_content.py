#!/usr/bin/env python3
"""Validate the structure of the Agentic Engineering 101 guide.

Checks (errors fail the run):
  * every English file has a Spanish counterpart at the same path, and vice versa
  * lesson and lab files carry the expected front matter
  * lesson and lab files contain the required H2 headings, in order
  * relative links point to files that exist

Warnings (reported, never fail the run unless --strict):
  * the English file was committed more recently than its Spanish counterpart,
    so the translation may be out of date

Usage:
  python3 scripts/check_content.py            # human-readable report, exit 1 on errors
  python3 scripts/check_content.py --strict   # warnings also fail
  python3 scripts/check_content.py --hook     # for agent Stop hooks: exit 2 on errors

Standard library only, so it runs anywhere Python 3.10+ runs.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANGS = ("en", "es")

# Files at the repository root (or under docs/) that exist in both languages.
BILINGUAL_PAIRS = [
    ("README.md", "README.es.md"),
    ("CONTRIBUTING.md", "CONTRIBUTING.es.md"),
    ("AI_POLICY.md", "AI_POLICY.es.md"),
    ("CODE_OF_CONDUCT.md", "CODE_OF_CONDUCT.es.md"),
    ("docs/authoring.md", "docs/authoring.es.md"),
    ("practice/issues/en.md", "practice/issues/es.md"),
]

# Directory trees mirrored per language: <tree>/<lang>/...
MIRRORED_TREES = ["content", "workshops"]

REQUIRED_HEADINGS = {
    "lesson": {
        "en": [
            "What you'll be able to do",
            "Why this matters",
            "Watch out",
            "Check your understanding",
            "Key points",
            "Go further",
        ],
        "es": [
            "Lo que serás capaz de hacer",
            "Por qué importa",
            "Ojo con",
            "Comprueba lo que has aprendido",
            "Ideas clave",
            "Para profundizar",
        ],
    },
    "lab": {
        "en": ["Goal", "Before you start", "Steps", "Done when", "Reflect"],
        "es": [
            "Objetivo",
            "Antes de empezar",
            "Pasos",
            "Cómo saber que has terminado",
            "Reflexiona",
        ],
    },
}

LESSON_KEYS = {"title", "module", "kind", "minutes", "level", "last_reviewed"}
PAGE_KEYS = {"title", "kind", "last_reviewed"}
LEVELS = {"foundation", "intermediate", "advanced"}
MODULE_DIR = re.compile(r"^(\d{2})-[a-z0-9-]+$")
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
FENCE = re.compile(r"^(```|~~~)")


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, path: Path | str, message: str) -> None:
        self.errors.append(f"{_rel(path)}: {message}")

    def warn(self, path: Path | str, message: str) -> None:
        self.warnings.append(f"{_rel(path)}: {message}")


def _rel(path: Path | str) -> str:
    try:
        return str(Path(path).resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def parse_front_matter(text: str) -> dict[str, str] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        line = line.split(" #", 1)[0].rstrip()
        if not line.strip() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def strip_code(text: str) -> str:
    """Remove fenced code blocks so headings and links inside them are ignored."""
    kept, in_fence = [], False
    for line in text.splitlines():
        if FENCE.match(line.lstrip()):
            in_fence = not in_fence
            continue
        if not in_fence:
            kept.append(line)
    return "\n".join(kept)


def h2_headings(text: str) -> list[str]:
    return [line[3:].strip() for line in strip_code(text).splitlines() if line.startswith("## ")]


def check_mirrors(report: Report) -> list[tuple[Path, Path]]:
    pairs: list[tuple[Path, Path]] = []
    for tree in MIRRORED_TREES:
        en_root, es_root = ROOT / tree / "en", ROOT / tree / "es"
        if not en_root.exists() and not es_root.exists():
            continue
        en_files = {p.relative_to(en_root) for p in en_root.rglob("*.md")} if en_root.exists() else set()
        es_files = {p.relative_to(es_root) for p in es_root.rglob("*.md")} if es_root.exists() else set()
        for missing in sorted(en_files - es_files):
            report.error(en_root / missing, f"no Spanish counterpart at {tree}/es/{missing}")
        for missing in sorted(es_files - en_files):
            report.error(es_root / missing, f"no English counterpart at {tree}/en/{missing}")
        pairs += [(en_root / p, es_root / p) for p in sorted(en_files & es_files)]
    for en, es in BILINGUAL_PAIRS:
        en_path, es_path = ROOT / en, ROOT / es
        if en_path.exists() != es_path.exists():
            present, absent = (en, es) if en_path.exists() else (es, en)
            report.error(present, f"bilingual pair is missing {absent}")
        elif en_path.exists():
            pairs.append((en_path, es_path))
    return pairs


def check_content_file(path: Path, lang: str, report: Report) -> None:
    text = path.read_text(encoding="utf-8")
    rel_parts = path.relative_to(ROOT / "content" / lang).parts
    if rel_parts == ("README.md",):
        return  # table of contents: free form

    front = parse_front_matter(text)
    if front is None:
        report.error(path, "missing front matter (--- ... ---) at the top of the file")
        return

    module_match = MODULE_DIR.match(rel_parts[0]) if len(rel_parts) == 2 else None
    if module_match and path.name in ("README.md", "lab.md"):
        expected_kind = "lesson" if path.name == "README.md" else "lab"
        missing = LESSON_KEYS - front.keys()
        if missing:
            report.error(path, f"front matter is missing: {', '.join(sorted(missing))}")
        if front.get("kind") != expected_kind:
            report.error(path, f"front matter kind should be '{expected_kind}', found '{front.get('kind')}'")
        if front.get("module", "").lstrip("0") != module_match.group(1).lstrip("0"):
            report.error(path, f"front matter module should be {int(module_match.group(1))}")
        if front.get("level") and front["level"] not in LEVELS:
            report.error(path, f"level must be one of {sorted(LEVELS)}")
        if front.get("minutes") and not front["minutes"].isdigit():
            report.error(path, "minutes must be a whole number")
        check_date(path, front, report)
        check_headings(path, text, REQUIRED_HEADINGS[expected_kind][lang], report)
    else:
        missing = PAGE_KEYS - front.keys()
        if missing:
            report.error(path, f"front matter is missing: {', '.join(sorted(missing))}")
        check_date(path, front, report)


def check_date(path: Path, front: dict[str, str], report: Report) -> None:
    value = front.get("last_reviewed")
    if not value:
        return
    try:
        date.fromisoformat(value)
    except ValueError:
        report.error(path, f"last_reviewed must be an ISO date (YYYY-MM-DD), found '{value}'")


def check_headings(path: Path, text: str, required: list[str], report: Report) -> None:
    found = h2_headings(text)
    position = 0
    for heading in required:
        try:
            position = found.index(heading, position) + 1
        except ValueError:
            where = "missing" if heading not in found else "out of order"
            report.error(path, f"required heading '## {heading}' is {where}")


def check_links(path: Path, report: Report) -> None:
    text = strip_code(path.read_text(encoding="utf-8"))
    text = re.sub(r"`[^`]*`", "", text)  # ignore inline code
    for target in LINK.findall(text):
        if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
            continue
        file_part = target.split("#", 1)[0]
        if not file_part:
            continue
        resolved = (path.parent / file_part).resolve()
        if not resolved.exists():
            report.error(path, f"broken relative link: {target}")


def last_commit_time(path: Path) -> int | None:
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%ct", "--", str(path)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None
    return int(out) if out else None


def check_staleness(pairs: list[tuple[Path, Path]], report: Report) -> None:
    for en, es in pairs:
        en_time, es_time = last_commit_time(en), last_commit_time(es)
        if en_time and es_time and en_time > es_time:
            report.warn(es, f"English source {_rel(en)} changed after this translation; review it")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--strict", action="store_true", help="treat warnings as errors")
    parser.add_argument("--hook", action="store_true", help="exit 2 on errors (agent Stop hooks)")
    args = parser.parse_args()

    report = Report()
    pairs = check_mirrors(report)

    for lang in LANGS:
        for path in sorted((ROOT / "content" / lang).rglob("*.md")):
            check_content_file(path, lang, report)

    markdown = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts and "node_modules" not in p.parts]
    for path in sorted(markdown):
        check_links(path, report)

    check_staleness(pairs, report)

    for warning in report.warnings:
        print(f"warning: {warning}")
    for error in report.errors:
        print(f"error: {error}", file=sys.stderr if args.hook else sys.stdout)

    failed = bool(report.errors) or (args.strict and bool(report.warnings))
    checked = len(markdown)
    if failed:
        print(
            f"\n{len(report.errors)} error(s), {len(report.warnings)} warning(s) in {checked} Markdown files.",
            file=sys.stderr if args.hook else sys.stdout,
        )
        if args.hook:
            print("Fix the files above before finishing (see docs/authoring.md).", file=sys.stderr)
            return 2
        return 1
    print(f"OK: {checked} Markdown files checked, {len(report.warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
