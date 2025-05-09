from typing import Dict, List
from collections import defaultdict
import re
from app.domain.trie import Trie

class InvertedIndex:
    def __init__(self):
        self.index: Dict[str, List[str]] = defaultdict(list)
        self.trie = Trie()

    def add_document(self, document_id: str, content: str):
        words = self._tokenize(content)
        for word in words:
            if document_id not in self.index[word]:
                self.index[word].append(document_id)
            self.trie.insert(word)

    def search(self, query: str) -> List[str]:
        return self.index.get(query.lower(), [])

    def _tokenize(self, text: str) -> List[str]:
        # Tokenización básica: elimina puntuación y convierte a minúsculas
        return re.findall(r'\b\w+\b', text.lower())