from rest_framework import viewsets, permissions
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.generics import ListAPIView


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.select_related('user').all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_slug = self.request.query_params.get("post_slug")
        if post_slug:
            return self.queryset.filter(post_slug=post_slug)
        return self.queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentBySlugView(ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_slug = self.kwargs.get("post_slug")
        return Comment.objects.filter(post_slug=post_slug)