from django.urls import path

from apps.users.views import LoginAPIView, RefreshTokenAPIView, RegisterAPIView

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="user-register"),
    path("login/", LoginAPIView.as_view(), name="user-login"),
    path("refresh/", RefreshTokenAPIView.as_view(), name="refresh-token"),
]
