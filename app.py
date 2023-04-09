from fastapi import FastAPI
from search import search as sim_search

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "Hello World"}

@app.get('/search')
def search(q: str, limit: int = 10):
    hits = sim_search(q, limit)
    return {"hits": hits}
