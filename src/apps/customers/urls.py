from django.urls import path

from apps.customers.views import (
    CustomerDetailsAPIView,
    CustomerListAPIView,
    CustomerRegisterAPIView,
)

urlpatterns = [
    path("register/", CustomerRegisterAPIView.as_view(), name="customer-register"),
    path("", CustomerListAPIView.as_view(), name="customer-list"),
    path("<uuid:pk>/", CustomerDetailsAPIView.as_view(), name="customer-detail"),
]
