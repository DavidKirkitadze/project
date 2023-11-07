from rest_framework import serializers
from .models import Articles


class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ('title', 'cat_id')