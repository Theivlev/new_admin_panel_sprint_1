from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from movies.mixins import TimeStampedMixin, UUIDMixin


class Genre(TimeStampedMixin, UUIDMixin):
    name = models.CharField(_('name'), max_length=255)
    description = models.TextField(_('description'), blank=True)

    class Meta:
        db_table = "content\".\"genre"
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Filmwork(TimeStampedMixin, UUIDMixin):
    title = models.CharField(
        _('title'),
        max_length=255,
        blank=False,
        null=False
    )
    description = models.TextField(_('description'), blank=True)
    creation_date = models.DateField(_('the date of the film\'s creation',))
    rating = models.FloatField(
        _('rating'),
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    class Type(models.TextChoices):
        MOVIE = "movie", _("Movie")
        TV_SHOW = "tv_show", _("TV Show")

    type = models.CharField(
        _('type'),
        max_length=50,
        choices=Type.choices,
        default=Type.MOVIE,
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = "content\".\"film_work"
        verbose_name = 'Кинопроизведение'
        verbose_name_plural = 'Кинопроизведения'


class GenreFilmwork(UUIDMixin):
    film_work = models.ForeignKey('Filmwork', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"genre_film_work"
        verbose_name = 'Жанр фильма'
        verbose_name_plural = 'Жанры фильма'


class Person(TimeStampedMixin, UUIDMixin):
    full_name = models.CharField(_('actor'), max_length=255)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "content\".\"person"
        verbose_name = 'Актёр'
        verbose_name_plural = 'Актёры'


class PersonFilmwork(UUIDMixin):
    film_work = models.ForeignKey('Filmwork', on_delete=models.CASCADE)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    role = models.TextField('role')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"person_film_work"
