from django.urls import path

from apps.staff.views import (
    DepartmentDetailAPIView,
    DepartmentListAPIView,
    EmployeeDetailsAPIView,
    EmployeeListAPIView,
    EmployeeRegisterAPIView,
)

urlpatterns = [
    path("register/", EmployeeRegisterAPIView.as_view(), name="staff-register"),
    path("", EmployeeListAPIView.as_view(), name="staff-list"),
    path("<uuid:pk>/", EmployeeDetailsAPIView.as_view(), name="staff-detail"),
    path("departments/", DepartmentListAPIView.as_view(), name="department-list"),
    path(
        "departments/<uuid:pk>/",
        DepartmentDetailAPIView.as_view(),
        name="department-detail",
    ),
]
