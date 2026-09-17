"""Helpers shared by the tests."""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent


class ShelfTestCase(unittest.TestCase):
    """Gives every test its own temporary shelf file and home directory."""

    def setUp(self) -> None:
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.home = Path(directory.name)
        self.shelf_path = self.home / "shelf.json"

    def shelf(self, *args: str) -> subprocess.CompletedProcess[str]:
        """Run the real command line against the temporary shelf.

        HOME points at the temporary folder too, so even a bug that ignores
        SHELF_PATH cannot touch the real ~/.shelf.json.
        """
        env = dict(
            os.environ,
            SHELF_PATH=str(self.shelf_path),
            HOME=str(self.home),
            USERPROFILE=str(self.home),
        )
        return subprocess.run(
            [sys.executable, "-m", "shelf", *args],
            cwd=PROJECT_ROOT,
            env=env,
            capture_output=True,
            text=True,
            check=False,
        )
