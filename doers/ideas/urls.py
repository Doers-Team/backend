from django.urls import path
from . import views

urlpatterns = [
    path('api/ideas/', views.IdeasAPIView.as_view()),
    path('api/ideas/idea/<slug:idea_slug>/', views.IdeaAPIView.as_view()),
]
