from django.contrib import admin
from django.urls import include, path

from core.spectacular import urlpatterns as swagger_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("apps.users.urls")),
    path("customers/", include("apps.customers.urls")),
    path("staff/", include("apps.staff.urls")),
] + swagger_urls
