from django.db import models
from django.utils.text import slugify


"""class Doer(models.Model):
    id = models.SlugField(primary_key=True, unique=True, blank=True)
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    birth_date = models.DateField()
    bio = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            slug = slugify(f"{self.nickname}")
            self.id = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nickname}"""