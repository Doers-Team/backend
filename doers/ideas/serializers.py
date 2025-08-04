from rest_framework import serializers
from . import models
from reactions.serializers import IdeaSubscriptionsSerializer, IdeaLikesSerializer, IdeaCommentsSerializer


'''class IdeaReferenceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.IdeaReferenceImage
        fields = ['id', 'reference_image']'''

class IdeaCategoriesSerializer(serializers.Serializer):
    value = serializers.CharField()
    label = serializers.CharField()

class IdeaSerializer(serializers.ModelSerializer):
    #doer = serializers.SlugRelatedField(slug_field='username', read_only=True)
    doer = serializers.StringRelatedField()
    #images = IdeaReferenceImageSerializer(many=True, read_only=True)
    ideaSubscriptions = IdeaSubscriptionsSerializer(many=True, read_only=True)
    ideaLikes = IdeaLikesSerializer(many=True, read_only=True)
    ideaComments = IdeaCommentsSerializer(many=True, read_only=True)

    class Meta:
        model = models.Idea
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']