import os
import sys
import pandas as pd

# Allow imports from project root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.embedder import generate_embedding
from tools.vector_db import save_vector_db
from tools.preprocess import preprocess_ticket_text

# Set base project root dynamically
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def train_vector_db(
    data_path=os.path.join(BASE_DIR, "data", "Historical_ticket_data.csv"),
    db_path=os.path.join(BASE_DIR, "data", "vector_db.pkl")
):
    # Load historical data
    df = pd.read_csv(data_path)

    # Normalize column names (strip, lowercase, underscores)
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # Check for necessary columns
    if "issue_category" not in df.columns or "solution" not in df.columns:
        raise ValueError("Missing required columns: 'Issue Category' and 'Solution'.")

    # Generate synthetic fields
    df["description"] = df["issue_category"].fillna("") + " | Sentiment: " + df.get("sentiment", "").fillna("")
    df["team"] = "General Support"
    df["action"] = df["solution"]

    df = df.dropna(subset=["description", "team", "action"])

    records = []
    for _, row in df.iterrows():
        content = preprocess_ticket_text(row['description'], row['team'], row['action'])
        embedding = generate_embedding(content)
        records.append({
            "embedding": embedding,
            "description": row["description"],
            "team": row["team"],
            "action": row["action"]
        })

    save_vector_db(records, db_path)
    print(f"✅ Vector DB trained and saved to {db_path}")

if __name__ == "__main__":
    train_vector_db()
