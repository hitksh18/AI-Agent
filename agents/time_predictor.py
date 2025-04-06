# agents/time_predictor.py

import ollama

def predict_resolution_time(summary):
    prompt = f"""
You are an AI assistant that predicts how long a customer support issue might take to resolve.

Given the following issue summary:
\"\"\"{summary}\"\"\"

Estimate the resolution time in hours or days. Be realistic and concise. Reply in this format:
"Estimated time to resolve: X hours/days"
"""
    response = ollama.chat(
        model='llama3',
        messages=[{"role": "user", "content": prompt}]
    )

    return response['message']['content']
