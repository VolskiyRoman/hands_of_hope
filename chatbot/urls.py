from django.urls import path

from chatbot.views import OpenAIChatView

urlpatterns = [
    path("api/chat/", OpenAIChatView.as_view(), name="mistral-chat"),
]
