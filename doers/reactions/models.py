from django.db import models
from ideas.models import Idea
from django.contrib.auth.models import User


class IdeaSubscription(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name="ideaSubscriptions")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ideaSubscriptions")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class IdeaLike(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name="ideaLikes")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('idea', 'author')

class IdeaComment(models.Model):
    text = models.TextField()
    
    #parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name="replies")
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name="ideaComments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ideaComments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
