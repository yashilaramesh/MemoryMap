from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
import google.generativeai as genai

# Load your API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use Gemini 1.5 Pro model
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

# Start a chat session and include your "system message" as a user message
chat = model.start_chat(history=[
    {
        "role": "user",
        "parts": [
            "You are a friendly travel assistant. Only respond to travel-related questions. "
            "If someone asks something unrelated to travel, gently explain that you're here to help with trips, destinations, planning, or exploring new places."
        ]
    }
])

def chatbot_page(request):
    return render(request, 'chatbot/chatbot.html')

@csrf_exempt
def chatbot_query(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get("message", "")

        try:
            response = chat.send_message(message)
            return JsonResponse({"reply": response.text})
        except Exception as e:
            print("🔥 Gemini error:", repr(e))
            return JsonResponse({"reply": "Oops! Something went wrong with Gemini."})
