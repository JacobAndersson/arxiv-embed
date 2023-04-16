from fastapi import FastAPI
from search import search as sim_search
from cache import MemoryCache
from rerank import rerank

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

    hits = sim_search(q)
    hits = rerank(q, hits)

    cache.set(q, hits)
    return {"hits": hits[:limit]}
