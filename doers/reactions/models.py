from django.db import models
from ideas.models import Idea
from users.models import Doer


class IdeaSubscription(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name="ideaSubscriptions")
    author = models.ForeignKey(Doer, on_delete=models.CASCADE, related_name="ideaSubscriptions")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class IdeaLike(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name="ideaLikes")
    author = models.OneToOneField(Doer, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class IdeaComment(models.Model):
    text = models.TextField()
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name="ideaComments")
    author = models.ForeignKey(Doer, on_delete=models.CASCADE, related_name="ideaComments")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)