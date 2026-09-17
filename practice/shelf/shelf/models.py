"""The data model: a book on your reading list."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone

STATUSES = ("to-read", "reading", "done")


def now() -> str:
    """The current time as an ISO 8601 timestamp in UTC, to the second."""
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


@dataclass
class Book:
    id: int
    title: str
    author: str
    status: str = "to-read"
    added_at: str = field(default_factory=now)
    finished_at: str | None = None

    def move_to(self, status: str) -> None:
        """Change the status and record when the book was finished."""
        self.status = status
        self.finished_at = now() if status == "done" else None

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> Book:
        return cls(**data)

    def __str__(self) -> str:
        return f"#{self.id} [{self.status}] {self.title} by {self.author}"
