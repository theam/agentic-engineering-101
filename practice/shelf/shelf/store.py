"""Reading and writing the shelf file.

The shelf is one JSON file: ``~/.shelf.json``, or the file named by the
``SHELF_PATH`` environment variable. The file is a JSON list with one object
per book (see ``Book.to_dict``).
"""

from __future__ import annotations

import json
import os
from pathlib import Path

from shelf.models import Book

PATH_VARIABLE = "SHELF_PATH"


class ShelfError(Exception):
    """A problem the command line reports to the user without a traceback."""


class BookNotFound(ShelfError):
    def __init__(self, book_id: int) -> None:
        super().__init__(f"no book with id {book_id}")


def default_path() -> Path:
    """``$SHELF_PATH`` if it is set, otherwise ``~/.shelf.json``."""
    configured = os.environ.get(PATH_VARIABLE)
    return Path(configured).expanduser() if configured else Path.home() / ".shelf.json"


class Store:
    def __init__(self, path: Path | str | None = None) -> None:
        self.path = Path(path) if path is not None else default_path()

    def load(self) -> list[Book]:
        if not self.path.exists():
            return []
        records = json.loads(self.path.read_text(encoding="utf-8"))
        return [Book.from_dict(record) for record in records]

    def save(self, books: list[Book]) -> None:
        records = [book.to_dict() for book in books]
        # Write a temporary file and swap it in, so an interrupted save
        # never leaves a half-written shelf behind.
        temporary = self.path.with_name(self.path.name + ".tmp")
        temporary.write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")
        temporary.replace(self.path)

    def add(self, title: str, author: str, status: str = "to-read") -> Book:
        books = self.load()
        next_id = max((book.id for book in books), default=0) + 1
        book = Book(id=next_id, title=title, author=author)
        book.move_to(status)
        books.append(book)
        self.save(books)
        return book

    def move(self, book_id: int, status: str) -> Book:
        books = self.load()
        book = find(books, book_id)
        book.move_to(status)
        self.save(books)
        return book


def find(books: list[Book], book_id: int) -> Book:
    for book in books:
        if book.id == book_id:
            return book
    raise BookNotFound(book_id)
