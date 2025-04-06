import ollama

def suggest_resolution(summary, similar_tickets):
    context = "\n".join([
        f"""🎫 Issue: {ticket.get('description', 'No description available')}
📂 Category: {ticket.get('issue_category', 'Unknown')}
📊 Sentiment: {ticket.get('sentiment', 'N/A')}
🛠 Suggested Action: {ticket.get('action', 'No action recorded')}
✅ Solution Provided: {ticket.get('solution', 'No solution available')}
"""
        for ticket in similar_tickets
    ])

    prompt = f"""
You are a senior AI support agent. Based on the issue summary provided by the user and the context from similar historical tickets, generate a complete, step-by-step resolution plan.

📝 User Issue Summary:
"{summary}"

📚 Relevant Historical Ticket Data:
{context}

💡 Generate a clear, actionable, and helpful resolution plan below:
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]
