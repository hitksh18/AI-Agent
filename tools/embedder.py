# tools/embedder.py

import ollama
import numpy as np
import hashlib
from typing import Union

def generate_embedding(text: str) -> np.ndarray:
    """
    Generates a fixed-size (384-dim) embedding for the input text.
    Currently uses a deterministic hash-based method.
    
    Args:
        text (str): The input text to embed.

    Returns:
        np.ndarray: A 384-dimensional embedding vector.
    """
    # Create a hash to simulate consistent embeddings
    hashed = hashlib.sha256(text.encode()).digest()

    # Set seed for reproducibility and generate embedding
    np.random.seed(int.from_bytes(hashed[:4], 'little'))
    return np.random.rand(384)

# Optional: Enable this once Ollama supports real embeddings
# def generate_embedding(text: str) -> Union[list, np.ndarray]:
#     response = ollama.embeddings(model="llama3", prompt=text)
#     return response["embedding"]
