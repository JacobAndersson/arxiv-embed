from pymilvus import Collection, connections
from sentence_transformers import SentenceTransformer

connections.connect("default", host="localhost", port="19530")

collection = Collection("papers")
collection.load()

model = SentenceTransformer("sentence-transformers/multi-qa-mpnet-base-dot-v1")

search_params = {
    "metric_type": "IP",
    "params": {"nprobe": 10},
}

while True:
    print("#"*80)
    query = input("Enter query: ")
    if query == "exit" or query =='q':
        break

    query_embedding = model.encode(query)

    results = collection.search(
        data=[query_embedding],
        anns_field="abstract_embeddings",
        param=search_params,
        limit=3,
        output_fields=["title", "abstract"]
    )

    hits = results[0]

    titles = [hit.entity.get("title") for hit in results[0]]

    for hit in hits:
        print("hit: ", hit)
        print("title: ", hit.entity.get("title"))
        print("abstract: ", hit.entity.get("abstract"))
        print()
