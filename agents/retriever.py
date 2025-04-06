from tools.vector_db import load_vector_db, search_similar
from tools.embedder import generate_embedding

def retrieve_similar_tickets(query: str, top_k: int = 3):
    """
    Retrieve top_k similar historical tickets from the vector DB
    based on semantic similarity of the query using embeddings.
    Returns a clean list of ticket dicts with consistent keys.
    """
    # Load pre-trained vector index and ticket mapping
    index, id_map = load_vector_db()

    # Get the embedding for the user's issue summary
    embedding = generate_embedding(query)

    # Perform similarity search
    raw_results = search_similar(index, id_map, embedding, top_k)

    # Normalize ticket fields to avoid KeyError
    normalized_results = []
    for ticket in raw_results:
        normalized_results.append({
            "description": ticket.get("Issue", ticket.get("description", "No description available")),
            "issue_category": ticket.get("Issue Category", "Unknown"),
            "sentiment": ticket.get("Sentiment", "N/A"),
            "team": ticket.get("team", "Unassigned"),
            "action": ticket.get("action", "No action recorded"),
            "solution": ticket.get("Solution", "No solution available")
        })

    return normalized_results
