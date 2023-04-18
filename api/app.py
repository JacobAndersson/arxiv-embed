from fastapi import FastAPI
from search import search as sim_search
from cache import MemoryCache
from rerank import rerank
from models.paper import get_full_docs

app = FastAPI()

cache = MemoryCache(1000)

@app.get("/")
def read_root():
    return {"msg": "Hello World"}

@app.get('/api/search')
def search(q: str, limit: int = 10):
    cache_hit = cache.get(q)

    if cache_hit:
        return {"hits": cache_hit[:limit]}

    ids = sim_search(q)
    docs = get_full_docs(ids)
    docs = rerank(q, docs)

    cache.set(q, docs)
    return {"hits": docs[:limit]}
