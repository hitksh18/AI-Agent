# agents/estimator.py

import ollama

def estimate_resolution_time(summary: str) -> str:
    prompt = f"""
You are an AI support assistant. Based on the issue described below, estimate how long it might take to resolve.

Issue Summary:
\"\"\"{summary}\"\"\"

Provide a realistic resolution time in hours or days.
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]
