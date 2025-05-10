from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("hands_of_hope.urls.swagger")),
    path("", include("hands_of_hope.urls.develop")),
    path("", include("safe_knowledge.urls")),
    path("", include("assistance.urls")),
    path("", include("chatbot.urls")),
    path("api/health-check/", include("health_check.urls")),
    path("api/", include("djoser.urls")),
    path("api/", include("djoser.urls.jwt")),
]
