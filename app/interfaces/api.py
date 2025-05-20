from typing import List
from app.use_cases.search_engine import SearchEngine
from app.use_cases.boolean_search import BooleanSearch
from app.domain.index import InvertedIndex
from app.infrastructure.document_loader import DocumentLoader
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Query, HTTPException
from loguru import logger
import re
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi import status


app = FastAPI(title="Simple Search Engine API")

#Loads and indexes documents on start
loader = DocumentLoader("documents")
docs = loader.load_documents()
index = InvertedIndex()
for doc in docs:
    index.add_document(doc.id, doc.content)

engine = SearchEngine(BooleanSearch(index))

@app.get("/search")
def search(q: str = Query(..., min_length=2, max_length=100)):
    clean_q = re.sub(r"[^a-zA-Z0-9áéíóúüñ\s]", "", q.lower().strip())

    if not clean_q:
        logger.warning("Invalid query: '%s'", q)
        raise HTTPException(status_code=400, detail="Invalid query")
    
    logger.info("Consulta recibida: '%s'", clean_q)
    results = engine.search(clean_q)
    logger.info("Resultados encontrados: %s", results)
    return results

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    logger.error(f"Error inesperado: {exc}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Error interno del servidor"},
    )