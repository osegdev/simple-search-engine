import os
from app.domain.document import Document
from typing import List

class DocumentLoader:
    def __init__(self, directory: str):
        self.directory = directory

    def load_documents(self) -> List[Document]:
        documents = []
        for filename in os.listdir(self.directory):
            if filename.endswith(".txt"):
                path = os.path.join(self.directory, filename)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                doc = Document(
                    id=filename,
                    content=content,
                    metadata={"filename": filename}
                )
                documents.append(doc)
        return documents