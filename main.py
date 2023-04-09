import json
from sentence_transformers import SentenceTransformer, util


query = "Calculation of prompt diphoton production cross sections at"

def load_json(path):
    with open(path, "r") as f:
        data = [json.loads(line) for line in f]
    return data

model = SentenceTransformer("sentence-transformers/multi-qa-mpnet-base-dot-v1")

data = load_json("arxiv-small.json")
abstracts = [d["abstract"].strip() for d in data]
titles = [d["title"].strip() for d in data]

embeddings = model.encode(abstracts)
query_embedding = model.encode(query)

score = util.dot_score(embeddings, query_embedding)
print(titles)
print(score)
