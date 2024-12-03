from dataclasses import dataclass, field
from uuid import UUID
from datetime import datetime
from typing import Optional
from mixins import IDMixin, TimestampMixin


@dataclass
class FilmWork(IDMixin, TimestampMixin):
    title: str
    type: str
    __table_name__: str = field(init=False, default='film_work')
    description: Optional[str] = None
    creation_date: Optional[datetime] = None
    rating: Optional[float] = None


@dataclass
class Genre(IDMixin, TimestampMixin):
    name: str
    description: Optional[str] = None
    __table_name__: str = field(init=False, default='genre')


@dataclass
class GenreFilmWork(IDMixin):
    id: UUID
    genre_id: UUID
    film_work_id: UUID
    created: datetime = field(default_factory=datetime.now)
    __table_name__: str = field(init=False, default='genre_film_work')


@dataclass
class Person(IDMixin, TimestampMixin):
    full_name: str
    __table_name__: str = field(init=False, default='person')


@dataclass
class PersonFilmWork(IDMixin):
    role: str
    person_id: UUID
    film_work_id: UUID
    reated: datetime = field(default_factory=datetime.now)
    __table_name__: str = field(init=False, default='person_film_work')
