from django.shortcuts import render
from django.http import JsonResponse
import datetime

chat_history = []

def chat_view(request):
    return render(request, 'chatbot_app/chat.html')

def get_response(request):
    user_input = request.GET.get('msg')
    response = generate_bot_reply(user_input)

    chat_history.append({'sender': 'user', 'message': user_input})
    chat_history.append({'sender': 'bot', 'message': response})

    return JsonResponse({'reply': response})

def generate_bot_reply(message):
    """
    Simple rule-based reply logic.
    This can later be replaced or extended using NLP or ML models.
    """
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hey there! 😊 How can I assist you today?"
    elif "help" in message:
        return "Sure! I can answer questions, tell you jokes, or help you explore books. Try asking about books!"
    elif "joke" in message:
        return "Why did the developer go broke? Because he used up all his cache. 😄"
    elif "book" in message:
        return "Do you like fiction, non-fiction, or fantasy? I can recommend something!"
    elif "bye" in message:
        return "Goodbye! Hope to chat again soon. 👋"
    else:
        return fallback_response(message)

def fallback_response(message):
    return "Hmm... I didn’t quite get that. Could you rephrase?"
