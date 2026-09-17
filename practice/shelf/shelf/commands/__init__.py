"""The subcommands of ``shelf``, one module per command.

Each module in this package defines ``register(subparsers)``. It adds its
subcommand to the parser and sets ``handler``: a function that takes the parsed
arguments and a ``Store`` and returns the exit code.

Modules are discovered automatically. Adding a command means adding a file
here, not editing a shared list, so work on different commands never touches
the same file.
"""

from __future__ import annotations

import importlib
import pkgutil


def register_all(subparsers) -> None:
    for module_info in sorted(pkgutil.iter_modules(__path__), key=lambda info: info.name):
        module = importlib.import_module(f"{__name__}.{module_info.name}")
        module.register(subparsers)
