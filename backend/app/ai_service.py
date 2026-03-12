import os

def generate_ai_response(prompt: str):

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return "AI service not configured yet."

    # Placeholder for AI response
    return f"AI response to: {prompt}"