import time
from pymilvus import (
    connections,
    utility,
    FieldSchema, CollectionSchema, DataType,
    Collection,
)

dim = 768

connections.connect("default", host="localhost", port="19530")

fields = [
    FieldSchema(name="id", dtype=DataType.VARCHAR, is_primary=True, auto_id=False, max_length=20),
    FieldSchema(name="title", dtype=DataType.VARCHAR, max_length=1000),
    FieldSchema(name="abstract", dtype=DataType.VARCHAR, max_length=2000),
    FieldSchema(name="authors", dtype=DataType.VARCHAR, max_length=512),
    FieldSchema(name="categories", dtype=DataType.VARCHAR, max_length=512),
    FieldSchema(name="abstract_embeddings", dtype=DataType.FLOAT_VECTOR, dim=dim)
]

print('Creating collection...')
schema = CollectionSchema(fields)
papers = Collection("papers", schema, consistency_level="Strong")


print('Creating index...')
index = {
    "index_type": "IVF_FLAT",
    "metric_type": "IP",
    "params": {"nlist": 128 },
}

papers.create_index("abstract_embeddings", index)

