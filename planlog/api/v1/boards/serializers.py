import shortuuid
from django.template.defaultfilters import slugify
from rest_framework import serializers
from planlog.models.board import Board


class BoardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = [
            'title',
            'slug',
            'description'
        ]


class BoardCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = [
            'id',
            'title',
            'slug',
            'description'
        ]
        read_only_fields = ['slug']

    def create(self, validated_data):
        slug = slugify(validated_data.get('title')) + '-' + shortuuid.uuid()
        return Board.objects.create(**validated_data, slug=slug)