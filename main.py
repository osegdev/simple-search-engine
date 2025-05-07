from app.domain.index import InvertedIndex

index = InvertedIndex()
index.add_document("doc1", "Hola mundo, este es un documento.")
index.add_document("doc2", "Hola, esto es otro ejemplo de texto.")

print("Buscar 'hola':", index.search("hola"))       # ['doc1', 'doc2']
print("Buscar 'documento':", index.search("documento"))  # ['doc1']
print("Buscar 'python':", index.search("python"))    # []