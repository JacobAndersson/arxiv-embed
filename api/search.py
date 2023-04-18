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

def search(query, limit=50):
    query_embedding = model.encode(query)

    results = collection.search(
        data=[query_embedding],
        anns_field="abstract_embeddings",
        param=search_params,
        limit=limit,
        output_fields=["id"]
    )

    hits = results[0]
    ids = [hit.entity.get("id") for hit in hits]
    return ids 


if __name__ == "__main__":
    while True:
        print("#"*80)
        query = input("Enter query: ")
        if query == "exit" or query =='q':
            break

        hits = search(query)
        print(f"Found {len(hits)} hits")
        for hit in hits:
            print(f"Title: {hit['title']}")
            print(f"Abstract: {hit['abstract']}")
            print(f"Authors: {hit['authors']}")
            print(f"ID: {hit['id']}")
            print()
