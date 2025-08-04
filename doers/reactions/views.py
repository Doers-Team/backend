from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from django.shortcuts import get_object_or_404

from . import models
from ideas.models import Idea
from . import serializers


class IdeaLikeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.IdeaLikesSerializer

    def get_queryset(self):
        idea_id = self.kwargs.get('idea_id')
        try:
            idea = Idea.objects.get(pk=idea_id)
        except Idea.DoesNotExist:
            raise NotFound("Idea not found")
        return models.IdeaLike.objects.filter(idea=idea)
    
    def create(self, request, idea_id=None):
        idea = get_object_or_404(Idea, id=idea_id)
        user = request.user
        like, created = models.IdeaLike.objects.get_or_create(idea=idea, author=user)

        if not created:
            like.delete()
            return Response({"message": "Like removed."}, status=status.HTTP_200_OK)

        return Response({"message": "Like added."}, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        idea_id = self.kwargs.get('idea_id')
        idea = Idea.objects.get(pk=idea_id)
        serializer.save(idea=idea, author=self.request.user)


class IdeaSubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.IdeaSubscriptionsSerializer

    def get_queryset(self):
        idea_id = self.kwargs.get('idea_id')
        try:
            idea = Idea.objects.get(pk=idea_id)
        except Idea.DoesNotExist:
            raise NotFound("Idea not found")
        return models.IdeaSubscription.objects.filter(idea=idea)

    def perform_create(self, serializer):
        idea_id = self.kwargs.get('idea_id')
        idea = Idea.objects.get(pk=idea_id)
        serializer.save(idea=idea, author=self.request.user)


class IdeaCommentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.IdeaCommentsSerializer

    def get_queryset(self):
        idea_id = self.kwargs.get('idea_id')
        try:
            idea = Idea.objects.get(pk=idea_id)
        except Idea.DoesNotExist:
            raise NotFound("Idea not found")
        return models.IdeaComment.objects.filter(idea=idea)

    def perform_create(self, serializer):
        idea_id = self.kwargs.get('idea_id')
        idea = Idea.objects.get(pk=idea_id)
        serializer.save(idea=idea, author=self.request.user)

class IdeaReactionsAPIView(APIView):
    def get(self, request, idea_id):
        try:
            idea = get_object_or_404(Idea, id=idea_id)
        except Idea.DoesNotExist:
            return Response({'error': f'Idea "{idea_id}" not found'}, status=status.HTTP_404_NOT_FOUND)
        
        subscriptions = models.IdeaSubscription.objects.filter(idea=idea)
        likes = models.IdeaLike.objects.filter(idea=idea)
        comments = models.IdeaComment.objects.filter(idea=idea)

        serializer = serializers.IdeaReactionsSerializer({
            'subscriptions': subscriptions,
            'likes': likes,
            'comments': comments,
        })
        return Response(serializer.data)


"""
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
    
class IdeaCommentViewSet(viewsets.ModelViewSet):
    queryset = models.IdeaComment.objects.filter(parent__isnull=True).order_by('-created_at')
    serializer_class = serializers.IdeaCommentSerializer
"""
