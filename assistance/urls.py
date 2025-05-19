from rest_framework.routers import DefaultRouter
from .views import HelpRequestViewSet, HelpReplyViewSet

router = DefaultRouter()
router.register("api/help-requests", HelpRequestViewSet, basename="help-request")
router.register("api/help-replies", HelpReplyViewSet, basename="help-reply")

urlpatterns = router.urls