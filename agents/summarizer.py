# agents/summarizer.py

import ollama

def summarize(text):
    prompt = f"""
You are an AI assistant for a customer support team. Your task is to summarize customer queries into a brief and clear problem description.

Here is the original message:
\"\"\"{text}\"\"\"

Provide a short summary highlighting the core issue. Avoid extra commentary.
"""
    response = ollama.chat(
        model='llama3',
        messages=[{"role": "user", "content": prompt}]
    )

    return response['message']['content']
