import subprocess
import json

def query_ollama(prompt: str, model: str = "llama3") -> str:
    """
    Queries the locally running Ollama model with a prompt.
    Returns the generated response as text.
    """
    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt,
            text=True,
            capture_output=True,
            timeout=120  # Adjust as needed for bigger prompts
        )
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            print("Error querying Ollama:", result.stderr)
            return "Error: Failed to query Ollama."
    except Exception as e:
        return f"Exception: {str(e)}"
