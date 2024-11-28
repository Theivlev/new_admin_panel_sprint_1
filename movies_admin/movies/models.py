import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class Genre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "content\".\"genre"
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Filmwork(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(
        _('Название'),
        max_length=255,
        blank=False,
        null=False
    )
    description = models.TextField(_('Описание'), blank=True)
    creation_date = models.DateField()
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1
    )

    class Type(models.TextChoices):
        MOVIE = "movie", _("Movie")
        TV_SHOW = "tv_show", _("TV Show")

    type = models.CharField(
        max_length=50,
        choices=Type.choices,
        default=Type.MOVIE,
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "content\".\"film_work"
        verbose_name = 'Кинопроизведение'
        verbose_name_plural = 'Кинопроизведения'
