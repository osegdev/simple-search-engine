from app.infrastructure.document_loader import DocumentLoader
from app.domain.index import InvertedIndex

loader = DocumentLoader("documents")
documents = loader.load_documents()

index = InvertedIndex()
for doc in documents:
    index.add_document(doc.id, doc.content)

# Probar búsquedas
print("Buscar 'documento':", index.search("documento"))
print("Buscar 'texto':", index.search("texto"))
print("Buscar 'clave':", index.search("clave"))