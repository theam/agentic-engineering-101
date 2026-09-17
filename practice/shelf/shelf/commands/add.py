"""shelf add TITLE AUTHOR [--status STATUS]"""

from __future__ import annotations

import argparse

from shelf.store import Store


def register(subparsers) -> None:
    parser = subparsers.add_parser("add", help="add a book to your shelf")
    parser.add_argument("title")
    parser.add_argument("author")
    parser.add_argument("--status", default="to-read", help="to-read (default), reading or done")
    parser.set_defaults(handler=run)


def run(args: argparse.Namespace, store: Store) -> int:
    book = store.add(args.title, args.author, args.status)
    print(f"Added {book}")
    return 0
