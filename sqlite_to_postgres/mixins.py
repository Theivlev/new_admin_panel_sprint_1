from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class IDMixin:
    id: UUID

    def __post_init__(self):
        if isinstance(self.id, str):
            self.id = UUID(self.id)


@dataclass
class TimestampMixin:
    created: datetime
    modified: datetime
