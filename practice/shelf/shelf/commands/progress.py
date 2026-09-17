"""shelf start ID and shelf finish ID"""

from __future__ import annotations

import argparse

from shelf.store import Store

# command name: (new status, verb for the confirmation, help text)
TRANSITIONS = {
    "start": ("reading", "Started", "mark a book as being read"),
    "finish": ("done", "Finished", "mark a book as read"),
}


def register(subparsers) -> None:
    for name, (status, verb, help_text) in TRANSITIONS.items():
        parser = subparsers.add_parser(name, help=help_text)
        parser.add_argument("id", type=int, help="the book id shown by 'shelf list'")
        parser.set_defaults(handler=run, status=status, verb=verb)


def run(args: argparse.Namespace, store: Store) -> int:
    book = store.move(args.id, args.status)
    print(f"{args.verb} {book}")
    return 0
