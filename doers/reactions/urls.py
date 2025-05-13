from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'ideas/(?P<idea_id>[-\w]+)/reactions/subscribe', views.IdeaSubscriptionViewSet, basename='idea-subscribe')
router.register(r'ideas/(?P<idea_id>[-\w]+)/reactions/like', views.IdeaLikeViewSet, basename='idea-like')
router.register(r'ideas/(?P<idea_id>[-\w]+)/reactions/comment', views.IdeaCommentViewSet, basename='idea-comment')

urlpatterns = [
    path('api/ideas/<slug:idea_id>/reactions/', views.IdeaReactionsAPIView.as_view(), name='idea-reactions'),
    path('api/', include(router.urls))
]
