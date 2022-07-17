from django.db import models
from planlog.models.base import BaseUUIDTimeStampedModel
from planlog.models.user import User
from planlog.models.card import Card


class Comment(BaseUUIDTimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='card_comments')
    comment_text = models.TextField()

    class Meta:
        db_table = 'comments'

    def __str__(self):
        return str(self.id)
