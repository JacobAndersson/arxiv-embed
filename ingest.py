import json
from sentence_transformers import SentenceTransformer, util
import time
from pymilvus import Collection, connections

PTH = "arxiv-large.json"

connections.connect("default", host="localhost", port="19530")
papers_collection = Collection("papers")
papers_collection.load()

print('loading model')
model = SentenceTransformer("sentence-transformers/multi-qa-mpnet-base-dot-v1")

def load_json(path, batch_size=1000):
    # build and yield batches of data
    data = []
    with open(path, "r") as f:
        for lin in f:
            load = json.loads(lin)
            if (len(load['authors']) < 10000):
                data.append(load)

            if len(data) == batch_size:
                yield data
                data = []

    if len(data) > 0:
        yield data


print('ingensting')
i = 0

for data in load_json(PTH, 4096):
    print('step', i)
    t0 = time.time()
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

    t1 = time.time()
    i += len(data)
    papers_collection.insert(entities)
    print(f"ingested {len(data)} in {t1-t0} seconds ({i} total)")
