from django.urls import path
from .views import RegisterView, LoginView, profile_view
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('api/register/', RegisterView.as_view()),
    path('api/login/', LoginView.as_view()),
    path('api/profile/', profile_view),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]