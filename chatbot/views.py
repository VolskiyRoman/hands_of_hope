import os
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from chatbot.prompts.prompt import MAIN_PROMPT


class MistralChatView(APIView):
    def post(self, request):
        prompt = MAIN_PROMPT
        content = request.data.get("content")

        if not prompt or not content:
            return Response(
                {"error": "Both 'prompt' and 'content' fields are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            url = "https://api.mistral.ai/v1/chat/completions"
            api_key = os.getenv("MISTRAL_API_KEY")
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            data = {
                "model": "mistral-small",
                "messages": [
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": content},
                ],
                "temperature": 0.7,
            }

            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            reply = response.json()["choices"][0]["message"]["content"]

            return Response({"reply": reply}, status=status.HTTP_200_OK)

        except requests.exceptions.RequestException as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_502_BAD_GATEWAY
            )
