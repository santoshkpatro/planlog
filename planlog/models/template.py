from django.db import models
from planlog.models.base import BaseUUIDTimeStampedModel
from planlog.models.board import Board
from planlog.models.template_category import TemplateCategory


class Template(BaseUUIDTimeStampedModel):
    category = models.ForeignKey(TemplateCategory, on_delete=models.SET_NULL, null=True)
    board = models.OneToOneField(Board, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'templates'

    def __str__(self):
        return self.name