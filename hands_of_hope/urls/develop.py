from django.urls import include, path

from hands_of_hope import settings

urlpatterns = []

if settings.DEBUG:
    if settings.PROFILERS_ENABLED:
        urlpatterns.append(path("silk/", include("silk.urls", namespace="silk")))
