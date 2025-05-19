from requests import Response
from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination

from .models import HelpRequest, HelpReply
from .serializers import HelpRequestSerializer, HelpReplySerializer


class HelpRequestPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

class HelpRequestViewSet(viewsets.ModelViewSet):
    queryset = HelpRequest.objects.select_related('user').prefetch_related('replies__responder')
    serializer_class = HelpRequestSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = HelpRequestPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def my_activity(self, request):
        user = request.user

        queryset = HelpRequest.objects.filter(
            Q(user=user) | Q(replies__responder=user)
        ).distinct().order_by('-created') \
         .select_related('user') \
         .prefetch_related('replies__responder')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



class HelpReplyViewSet(viewsets.ModelViewSet):
    queryset = HelpReply.objects.select_related('responder', 'request')
    serializer_class = HelpReplySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(responder=self.request.user)
