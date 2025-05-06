from rest_framework import serializers
from . import models
from ideas.models import Idea


class IdeaSubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.IdeaSubscription
        fields = '__all__'

class IdeaLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.IdeaLike
        fields = '__all__'

class IdeaCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.IdeaComment
        fields = '__all__'

class IdeaReactionsSerializer(serializers.Serializer):
    subscriptions = IdeaSubscriptionsSerializer(many=True)
    likes = IdeaLikesSerializer(many=True)
    comments = IdeaCommentsSerializer(many=True)

class IdeasReactionsSerializer(serializers.ModelSerializer):
    reactions = serializers.SerializerMethodField()

    class Meta:
        model = Idea
        fields = '__all__'

    def get_reactions(self, obj):
        return {
            'subscriptions': IdeaSubscriptionsSerializer(obj.ideaSubscriptions.all(), many=True).data,
            'likes': IdeaLikesSerializer(obj.ideaLikes.all(), many=True).data,
            'comments': IdeaCommentsSerializer(obj.ideaComments.all(), many=True).data,
        }
