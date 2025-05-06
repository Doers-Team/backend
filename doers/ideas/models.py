from django.db import models
from django.utils.text import slugify
from users.models import Doer


class Idea(models.Model):
    id = models.SlugField(primary_key=True, unique=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(blank=True)
    reference_image = models.ImageField(blank=True)
    doer = models.ForeignKey(Doer, on_delete=models.CASCADE, related_name="ideas")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            base_slug = slugify(f"{self.title[:50]}")
            slug = base_slug
            counter = 1

            while self.__class__.objects.filter(id=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.id = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"