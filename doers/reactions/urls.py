from django.urls import path
from . import views

urlpatterns = [
    path('api/ideas/reactions/', views.IdeasReactionsAPIView.as_view()),
    path('api/ideas/idea/<slug:idea_slug>/reactions/', views.IdeaReactionsAPIView.as_view()),
    path('api/ideas/idea/<slug:idea_slug>/reactions/subscriptions/', views.IdeaSubscriptionsAPIView.as_view()),
    path('api/ideas/idea/<slug:idea_slug>/reactions/likes/', views.IdeaLikesAPIView.as_view()),
    path('api/ideas/idea/<slug:idea_slug>/reactions/comments/', views.IdeaCommentsAPIView.as_view()),
]
