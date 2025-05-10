from rest_framework import viewsets, permissions
from .models import HelpRequest, HelpReply
from .serializers import HelpRequestSerializer, HelpReplySerializer


class HelpRequestViewSet(viewsets.ModelViewSet):
    queryset = HelpRequest.objects.select_related('user').prefetch_related('replies__responder')
    serializer_class = HelpRequestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HelpReplyViewSet(viewsets.ModelViewSet):
    queryset = HelpReply.objects.select_related('responder', 'request')
    serializer_class = HelpReplySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(responder=self.request.user)