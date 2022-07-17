from django.db import models
from planlog.models.base import BaseUUIDTimeStampedModel
from planlog.models.user import User
from planlog.models.board import Board


class Member(BaseUUIDTimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_members')
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='board_members')

    class Meta:
        db_table = 'members'
        unique_together = ['user', 'board']

    def __str__(self):
        return str(self.id)
