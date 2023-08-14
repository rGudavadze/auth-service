from django.urls import path

from apps.users.views import LoginAPIView, RefreshTokenAPIView

urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="user-login"),
    path("refresh/", RefreshTokenAPIView.as_view(), name="refresh-token"),
]
