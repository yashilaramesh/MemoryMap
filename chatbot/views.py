from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
import google.generativeai as genai

# Load API key securely
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def chatbot_page(request):
    return render(request, 'chatbot/chatbot.html')

@csrf_exempt
def chatbot_query(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get("message", "")

        # Optional: force travel-only questions
        if "travel" not in message.lower():
            return JsonResponse({
                "reply": "I’m your travel assistant. Ask me about destinations, planning, or things to do!"
            })

        try:
            response = model.generate_content(message)
            return JsonResponse({ "reply": response.text })
        except Exception as e:
            return JsonResponse({ "reply": "Oops! Something went wrong with Gemini." })

