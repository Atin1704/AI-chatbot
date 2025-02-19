from django.shortcuts import render
from django.http import JsonResponse

chat_history = []

def chat_view(request):
    return render(request, 'chatbot_app/chat.html')

def get_response(request):
    user_input = request.GET.get('msg')

    response = generate_bot_reply(user_input)

    chat_history.append({'sender': 'user', 'message': user_input})
    chat_history.append({'sender': 'bot', 'message': response})

    # save_chat_history(request.user.id, chat_history)
    return JsonResponse({'reply': response})

def generate_bot_reply(message):
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
    # return use_gpt_response(message)
    return "Hmm... I didn’t quite get that. Could you rephrase?"



# --- Placeholder Functions for Future Integration ---
def use_gpt_response(message):
    """
    TODO: Integrate OpenAI GPT or HuggingFace model.
    - Send `message` as prompt to model
    - Return the generated response
    """
    pass

def get_intent_from_nlp(message):
    """
    TODO: Use NLP (spaCy, NLTK, etc.) to detect user intent.
    - Classify input: greeting, info_request, joke, etc.
    - Return intent string
    """
    pass

def save_chat_history(user_id, chat_history):
    """
    TODO: Save chat history in the database per user session.
    - Use Django model to store messages and timestamps
    - Enable retrieval for later analysis or user chat logs
    """
    pass
