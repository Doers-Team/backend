from django.contrib import admin
from . import models


admin.site.register(models.IdeaSubscription)
admin.site.register(models.IdeaLike)
admin.site.register(models.IdeaComment)