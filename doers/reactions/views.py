from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models
from ideas.models import Idea
from . import serializers


class IdeasReactionsAPIView(APIView):
    def get(self, request):
        ideas = Idea.objects.all().prefetch_related(
            'ideaSubscriptions', 
            'ideaLikes', 
            'ideaComments'
        )
        serializer = serializers.IdeasReactionsSerializer(ideas, many=True)
        return Response(serializer.data)

class IdeaReactionsAPIView(APIView):
    def get(self, request, idea_slug):
        try:
            idea = Idea.objects.get(id=idea_slug)
        except Idea.DoesNotExist:
            return Response({'error': f'Idea "{idea_slug}" not found'}, status=status.HTTP_404_NOT_FOUND)
        
        subscriptions = models.IdeaSubscription.objects.filter(idea=idea)
        likes = models.IdeaLike.objects.filter(idea=idea)
        comments = models.IdeaComment.objects.filter(idea=idea)

        serializer = serializers.IdeaReactionsSerializer({
            'subscriptions': subscriptions,
            'likes': likes,
            'comments': comments,
        })
        return Response(serializer.data)

class IdeaSubscriptionsAPIView(APIView):
    def get(self, request, idea_slug):
        try:
            idea = Idea.objects.get(id=idea_slug)
        except Idea.DoesNotExist:
            return Response({'error': f'Idea "{idea_slug}" not found'}, status=status.HTTP_404_NOT_FOUND)
        
        subscriptions = models.IdeaSubscription.objects.filter(idea=idea)
        serializer = serializers.IdeaSubscriptionsSerializer(subscriptions, many=True)
        return Response(serializer.data)
    
class IdeaLikesAPIView(APIView):
    def get(self, request, idea_slug):
        try:
            idea = Idea.objects.get(id=idea_slug)
        except Idea.DoesNotExist:
            return Response({'error': f'Idea "{idea_slug}" not found'}, status=status.HTTP_404_NOT_FOUND)
        
        likes = models.IdeaLike.objects.filter(idea=idea)
        serializer = serializers.IdeaSubscriptionsSerializer(likes, many=True)
        return Response(serializer.data)
    
class IdeaCommentsAPIView(APIView):
    def get(self, request, idea_slug):
        try:
            idea = Idea.objects.get(id=idea_slug)
        except Idea.DoesNotExist:
            return Response({'error': f'Idea "{idea_slug}" not found'}, status=status.HTTP_404_NOT_FOUND)
        
        comments = models.IdeaComment.objects.filter(idea=idea)
        serializer = serializers.IdeaSubscriptionsSerializer(comments, many=True)
        return Response(serializer.data)
