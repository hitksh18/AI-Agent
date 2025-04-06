# agents/router.py

import ollama
import json

def predict_routing(summary: str) -> dict:
    prompt = f"""
You are a smart support triage assistant. Based on the issue summary below, decide the most appropriate support team to handle it, and suggest a clear next action they should take.

Issue Summary:
\"\"\"{summary}\"\"\"

Respond ONLY in this JSON format:
{{
  "team": "<Team Name>",
  "action": "<Recommended action>"
}}
"""
    try:
        response = ollama.chat(
            model="llama3",
            messages=[{"role": "user", "content": prompt}]
        )
        return json.loads(response['message']['content'])
    except Exception as e:
        return {
            "team": "Unknown",
            "action": f"⚠️ Failed to parse routing info. Error: {str(e)}"
        }
