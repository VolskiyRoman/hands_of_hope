from django.urls import path
from .views import MistralChatView

urlpatterns = [
    path("api/chat/", MistralChatView.as_view(), name="mistral-chat"),
]
