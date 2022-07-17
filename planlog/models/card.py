from django.db import models
from django.contrib.postgres.fields import ArrayField
from planlog.models.base import BaseUUIDTimeStampedModel
from planlog.models.user import User
from planlog.models.board import Board
from planlog.models.list import List


class Card(BaseUUIDTimeStampedModel):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='board_cards')
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='list_cards')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    labels = ArrayField(base_field=models.CharField(max_length=50), blank=True, null=True)
    checklist = ArrayField(base_field=models.JSONField(), blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'cards'

    def __str__(self) -> str:
        return self.title
