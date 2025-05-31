import os
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from chatbot.prompts.prompt import MAIN_PROMPT


class OpenAIChatView(APIView):
    def post(self, request):
        content = request.data.get("content")

        if not content:
            return Response(
                {"error": "'content' field is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            api_key = os.getenv("OPEN_AI_API_KEY")
            if not api_key:
                return Response(
                    {"error": "OpenAI API key is not set."},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

            url = "https://api.openai.com/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            }
            data = {
                "model": "gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": MAIN_PROMPT},
                    {"role": "user", "content": content}
                ],
                "temperature": 0.3,
                "top_p": 0.9,
                "max_tokens": 512,
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
