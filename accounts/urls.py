from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import CutomTokenBlacklistSerializer


app_name = "accounts"
urlpatterns = [
    path("login", TokenObtainPairView.as_view(), name="login"),
    path("refresh", TokenRefreshView.as_view(), name="refresh"),
    path("logout", CutomTokenBlacklistSerializer.as_view(), name="logout"),
]
