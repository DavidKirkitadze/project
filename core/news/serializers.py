import io

from rest_framework import serializers
from .models import Articles
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class ArticlesSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    anons = serializers.CharField()
    full_text = serializers.CharField()
    date = serializers.DateTimeField(read_only=True)
    them_id = serializers.IntegerField()