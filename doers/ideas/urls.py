from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'ideas', views.IdeaViewSet, basename='idea')

urlpatterns = [
    path('api/ideas/categories/', views.IdeaCategoriesListView.as_view(), name='idea-categories-list'),
    path('api/', include(router.urls)),
]
