from django.shortcuts import render
from django.http import JsonResponse

def chat_view(request):
    return render(request, 'chatbot_app/chat.html')

def get_response(request):
    user_input = request.GET.get('msg')
    response = generate_bot_reply(user_input)
    return JsonResponse({'reply': response})

def generate_bot_reply(message):
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! How can I help you today?"
    elif "name" in message:
        return "I'm a chatbot built with Django!"
    elif "bye" in message:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that."
