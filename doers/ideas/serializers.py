from rest_framework import serializers
from . import models


class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Idea
        fields = '__all__'