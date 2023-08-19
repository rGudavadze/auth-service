from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]


def preprocessing_filter_spec(endpoints):
    filtered = []
    for url, path_regex, method, callback in endpoints:
        if not url == "/api/schema/":
            filtered.append((url, path_regex, method, callback))
    return filtered
