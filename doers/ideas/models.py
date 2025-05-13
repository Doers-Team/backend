from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from . import validators
from users.models import Doer


class IdeaCategory(models.TextChoices):
    BUSINESS_AND_STARTUPS = 'business_and_startups', 'Business and Startups'
    TECHNOLOGY_AND_INNOVATIONS = 'technology_and_innovations', 'Technology and Innovations'
    EDUCATION_AND_SELF_DEVELOPMENT = 'education_and_self_development', 'Education and Self-development'
    ECOLOGY_AND_SUSTAINABILITY = 'ecology_and_sustainability', 'Ecology and Sustainability'
    CULTURE_AND_ARTS = 'culture_and_arts', 'Culture and Arts'
    HEALTH_AND_WELL_BEING = 'health_and_well_being', 'Health and Well-being'
    SOCIAL_AND_CULTURAL_CHANGE = 'social_and_cultural_change', 'Social and Cultural Change'
    TRANSPORTATION_AND_LOGISTICS = 'transportation_and_logistics', 'Transportation and Logistics'
    SCIENCE_AND_RESEARCH = 'science_and_research', 'Science and Research'
    TRAVEL_AND_TOURISM = 'travel_and_tourism', 'Travel and Tourism'
    FINANCE_AND_INVESTMENT = 'finance_and_investment', 'Finance and Investment'
    INTERNET_AND_COMMUNICATIONS = 'internet_and_communications', 'Internet and Communications'
    AGRICULTURE_AND_ANIMAL_HUSBANDRY = 'agriculture_and_animal_husbandry', 'Agriculture and Animal Husbandry'
    PSYCHOLOGY_AND_RELATIONSHIPS = 'psychology_and_relationships', 'Psychology and Relationships'
    LAW_AND_LEGAL_AFFAIRS = 'law_and_legal_affairs', 'Law and Legal Affairs'
    GADGETS_AND_DEVICES = 'gadgets_and_devices', 'Gadgets and Devices'
    LEISURE_AND_ENTERTAINMENT = 'leisure_and_entertainment', 'Leisure and Entertainment'
    OTHER = 'other', 'Other'

class Idea(models.Model):
    id = models.SlugField(primary_key=True, unique=True, blank=True)
    title = models.CharField(max_length=255)
    slogan = models.CharField(max_length=500)
    description = models.TextField()
    logo = models.ImageField(blank=True, upload_to="ideas/logos")
    reference_video = models.FileField(upload_to="ideas/videos", validators=[validators.validate_video_file], blank=True)
    category = models.CharField(max_length=50, choices=IdeaCategory.choices)

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
    
class IdeaReferenceImage(models.Model):
    idea = models.ForeignKey(Idea, related_name='images', on_delete=models.CASCADE)
    reference_image = models.ImageField(upload_to='ideas/images')
    
    def clean(self):
        if self.idea.images.count() >= 5:
            raise ValidationError("You can upload a maximum of 5 images per idea")
    
    def __str__(self):
        return f"Image for {self.idea.title}"