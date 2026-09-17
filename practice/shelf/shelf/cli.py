"""The ``shelf`` command line (also available as ``python -m shelf``)."""

from __future__ import annotations

import argparse
import sys

from shelf import __version__, commands
from shelf.store import ShelfError, Store


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="shelf",
        description="Keep a list of the books you want to read.",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    subparsers = parser.add_subparsers(
        title="commands", dest="command", metavar="COMMAND", required=True
    )
    commands.register_all(subparsers)
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run one command and return its exit code.

    0 means success, 1 means the command failed. Invalid usage exits with 2
    (argparse raises ``SystemExit(2)`` and prints the usage).
    """
    args = build_parser().parse_args(argv)
    try:
        return args.handler(args, Store())
    except ShelfError as error:
        print(f"shelf: error: {error}", file=sys.stderr)
        return 1
