from django.db import models
from django.contrib.postgres.fields import ArrayField
from planlog.models.base import BaseUUIDTimeStampedModel
from planlog.models.board import Board


class List(BaseUUIDTimeStampedModel):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='board_lists')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    card_order = ArrayField(base_field=models.UUIDField(), blank=True, null=True)

    class Meta:
        db_table = 'lists'

    def __str__(self) -> str:
        return self.title
