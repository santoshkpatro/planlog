from rest_framework import serializers
from planlog.models.template import Template


class TemplateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = [
            'id',
            'name',
            'description',
            'created_at'
        ]