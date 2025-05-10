from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, CommentBySlugView
from django.urls import path

router = DefaultRouter()
router.register("comments", CommentViewSet, basename="comments")

urlpatterns = router.urls + [
    path("get-comments/<slug:post_slug>/", CommentBySlugView.as_view(), name="comments-by-post-slug"),
]