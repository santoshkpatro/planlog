from django.db import models
from planlog.models.base import BaseUUIDTimeStampedModel


class TemplateCategory(BaseUUIDTimeStampedModel):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'template_categories'

    def __str__(self):
        return self.name