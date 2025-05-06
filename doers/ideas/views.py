from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from . import serializers


class IdeasAPIView(APIView):
    def get(self, request):
        ideas = models.Idea.objects.all()
        serializer = serializers.IdeaSerializer(ideas, many=True)
        return Response(serializer.data)

class IdeaAPIView(APIView):
    def get(self, request, idea_slug):
        idea = models.Idea.objects.get(id=idea_slug)
        serializer = serializers.IdeaSerializer(idea)
        return Response(serializer.data)
