from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import RegisterAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register_api'),
    path('login/', TokenObtainPairView.as_view(), name='login_api'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh_api'),
]
