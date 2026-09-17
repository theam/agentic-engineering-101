"""shelf list"""

from __future__ import annotations

import argparse

from shelf.store import Store


def register(subparsers) -> None:
    parser = subparsers.add_parser("list", help="show the books on your shelf")
    parser.set_defaults(handler=run)


def run(args: argparse.Namespace, store: Store) -> int:
    books = store.load()
    if not books:
        print("Your shelf is empty. Add a book with: shelf add TITLE AUTHOR")
        return 0
    for book in books:
        print(book)
    return 0
