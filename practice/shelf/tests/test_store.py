import json
import os
from datetime import datetime
from unittest import mock

from shelf.store import BookNotFound, Store, default_path
from tests.support import ShelfTestCase


class StoreTest(ShelfTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.store = Store(self.shelf_path)

    def test_a_missing_file_is_an_empty_shelf(self):
        self.assertEqual(self.store.load(), [])

    def test_add_assigns_increasing_ids_and_persists(self):
        self.store.add("Dune", "Frank Herbert")
        self.store.add("Kindred", "Octavia E. Butler", "reading")

        books = Store(self.shelf_path).load()

        self.assertEqual([(b.id, b.title, b.status) for b in books], [
            (1, "Dune", "to-read"),
            (2, "Kindred", "reading"),
        ])

    def test_the_file_is_a_json_list_of_books(self):
        self.store.add("Dune", "Frank Herbert")

        data = json.loads(self.shelf_path.read_text(encoding="utf-8"))

        self.assertIsInstance(data, list)
        self.assertEqual(
            set(data[0]), {"id", "title", "author", "status", "added_at", "finished_at"}
        )

    def test_finishing_a_book_records_when(self):
        book = self.store.add("Dune", "Frank Herbert")
        self.assertIsNone(book.finished_at)

        finished = self.store.move(book.id, "done")

        self.assertEqual(finished.status, "done")
        datetime.fromisoformat(finished.finished_at)  # raises if not a timestamp

    def test_moving_an_unknown_book_fails(self):
        with self.assertRaises(BookNotFound):
            self.store.move(42, "reading")

    def test_path_comes_from_shelf_path_or_defaults_to_home(self):
        with mock.patch.dict(os.environ, {"SHELF_PATH": str(self.shelf_path)}):
            self.assertEqual(default_path(), self.shelf_path)
        with mock.patch.dict(os.environ, {"HOME": str(self.home), "USERPROFILE": str(self.home)}):
            os.environ.pop("SHELF_PATH", None)
            self.assertEqual(default_path(), self.home / ".shelf.json")
