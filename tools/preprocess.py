import re

def clean_text(text):
    if not isinstance(text, str):
        return ""
    # Remove extra whitespace
    text = text.strip()
    # Normalize spaces
    text = re.sub(r"\s+", " ", text)
    # Remove unwanted characters (optional)
    text = re.sub(r"[^a-zA-Z0-9\s.,!?@:#/\-]", "", text)
    return text

def preprocess_ticket_text(description, team, action):
    description = clean_text(description)
    team = clean_text(team)
    action = clean_text(action)
    return f"{description} | Team: {team} | Action: {action}"
