import json
from sentence_transformers import SentenceTransformer, util

from pymilvus import Collection, connections

PTH = "arxiv-small.json"

connections.connect("default", host="localhost", port="19530")
papers_collection = Collection("papers")
papers_collection.load()

def load_json(path):
    with open(path, "r") as f:
        data = [json.loads(line) for line in f]
    return data

model = SentenceTransformer("sentence-transformers/multi-qa-mpnet-base-dot-v1")

data = load_json(PTH)
abstracts = [d["abstract"].strip() for d in data]
embeddings = model.encode(abstracts)

entities = [
    [ d['id'] for d in data],
    [ d['title'] for d in data],
    [ d['abstract'] for d in data],
    [ d['authors'] for d in data],
    [ d['categories'] for d in data],
    embeddings
]

papers_collection.insert(entities)
