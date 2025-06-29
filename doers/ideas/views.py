from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import serializers


class IdeaViewSet(viewsets.ModelViewSet):
    queryset = models.Idea.objects.all()
    serializer_class = serializers.IdeaSerializer
    lookup_field = 'id'

class IdeaCategoriesListView(APIView):
    def get(self, request):
        data = [{'value': choice.value, 'label': choice.label} for choice in models.IdeaCategory]
        serializer = serializers.IdeaCategoriesSerializer(data, many=True)
        return Response(serializer.data)
