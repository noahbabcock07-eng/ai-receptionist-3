import os
from openai import OpenAI

# Create OpenAI client using your OPENAI_API_KEY environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = (
    "You are a warm, friendly human receptionist for Adrian's Barber Shop. "
    "You speak in a natural, casual tone, like a real person on the phone. "
    "You keep answers short and clear. Use contractions like I'm, it's, you'll. "
    "You do not mention that you are an AI or language model. "
    "Your goals:\n"
    "1) Greet callers politely and sound happy they called.\n"
    "2) Understand what they need: a haircut, questions about prices, hours, location, etc.\n"
    "3) If they want an appointment, ask for the day and time they prefer.\n"
    "4) Confirm the appointment details clearly before booking.\n"
    "5) If something is not clear, ask a simple follow up question.\n"
    "Keep responses under 3 short sentences unless the caller is very confused. "
    "Never dump a list of options, just guide them step by step."
)


def handle_input(text: str) -> str:
    """
    Take the caller's transcribed speech and return a friendly receptionist reply.
    This keeps the same function name your app.py already imports.
    """
    if not text:
        return "I did not hear anything. Can you say that again for me?"

    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": text},
            ],
            temperature=0.7,
        )

        reply = completion.choices[0].message.content
        if not reply:
            return "Sorry, something glitchy happened. Can you repeat that one more time?"

        return reply.strip()

    except Exception:
        # You can log the error here if you want
        return "Sorry, I am having trouble on my end. Can you try again in a moment?"
