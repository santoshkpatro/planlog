from django.db import models
from django.contrib.postgres.fields import ArrayField
from planlog.models.base import BaseUUIDTimeStampedModel
from planlog.models.user import User


class Board(BaseUUIDTimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_boards')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, blank=True, null=True, unique=True)
    description = models.TextField(blank=True, null=True)
    list_order = ArrayField(base_field=models.UUIDField(), blank=True, null=True)

    class Meta:
        db_table = 'boards'

    def __str__(self) -> str:
        return self.title
