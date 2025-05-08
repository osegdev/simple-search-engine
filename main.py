from app.infrastructure.document_loader import DocumentLoader
from app.domain.index import InvertedIndex
from app.use_cases.boolean_search import BooleanSearch
from app.use_cases.frequency_ranked_search import FrequencyRankedSearch
from app.use_cases.tfidf_search import TFIDFSearch
from app.use_cases.search_engine import SearchEngine

loader = DocumentLoader("documents")
docs = loader.load_documents()

index = InvertedIndex()
for doc in docs:
    index.add_document(doc.id, doc.content)

engine = SearchEngine(BooleanSearch(index))
print("Búsqueda booleana:", engine.search("documento prueba"))

engine.set_strategy(FrequencyRankedSearch(index))
print("Búsqueda por frecuencia:", engine.search("documento prueba"))

engine.set_strategy(TFIDFSearch(index))
print("Búsqueda TF-IDF:", engine.search("documento prueba"))