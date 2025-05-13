from fastapi import FastAPI, Query
from typing import List
from app.use_cases.search_engine import SearchEngine
from app.use_cases.boolean_search import BooleanSearch
from app.domain.index import InvertedIndex
from app.infrastructure.document_loader import DocumentLoader
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Simple Search Engine API")

#Loads and indexes documents on start
loader = DocumentLoader("documents")
docs = loader.load_documents()
index = InvertedIndex()
for doc in docs:
    index.add_document(doc.id, doc.content)

engine = SearchEngine(BooleanSearch(index))

@app.get("/search", response_model=List[str])
def search(q: str = Query(..., min_length=1)):
    return engine.search(q)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)