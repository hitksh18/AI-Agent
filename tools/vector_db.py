# tools/vector_db.py

import numpy as np
import pickle
from sklearn.neighbors import NearestNeighbors

def build_index(vectors):
    index = NearestNeighbors(n_neighbors=3, algorithm='auto', metric='cosine')
    index.fit(vectors)
    return index

def save_vector_db(records, path):
    vectors = [r['embedding'] for r in records]
    index = build_index(vectors)
    id_map = [ {k: r[k] for k in r if k != 'embedding'} for r in records ]

    with open(path, 'wb') as f:
        pickle.dump((index, id_map), f)

def load_vector_db(path="data/vector_db.pkl"):
    with open(path, 'rb') as f:
        return pickle.load(f)

def search_similar(index, id_map, query_embedding, top_k=3):
    distances, indices = index.kneighbors([query_embedding], n_neighbors=top_k)
    return [id_map[i] for i in indices[0]]
