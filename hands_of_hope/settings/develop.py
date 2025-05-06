"""
Development settings for the finance tracker project.
"""

import logging

from hands_of_hope.settings.custom import *
from hands_of_hope.settings.django import *

if DEBUG:
    # configure docs and openapi
    INSTALLED_APPS.extend(("drf_spectacular",))

    REST_FRAMEWORK["DEFAULT_SCHEMA_CLASS"] = "drf_spectacular.openapi.AutoSchema"
    SPECTACULAR_SETTINGS = {
        "TITLE": "Hands of Hope API",
        "DESCRIPTION": "API for hands of hope project",
        "VERSION": "1.0.0",
        "SERVE_INCLUDE_SCHEMA": False,
    }

    # configure profilers if enabled
    if PROFILERS_ENABLED:
        profilers_apps = ("nplusone.ext.django", "silk")
        profilers_middlewares = (
            "nplusone.ext.django.NPlusOneMiddleware",
            "silk.middleware.SilkyMiddleware",
        )
        INSTALLED_APPS.extend(profilers_apps)
        MIDDLEWARE.extend(profilers_middlewares)

        NPLUSONE_LOGGER = logging.getLogger("nplusone")
        NPLUSONE_LOG_LEVEL = logging.INFO
