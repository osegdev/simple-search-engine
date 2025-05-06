from typing import Dict, List

class InvertedIndex:
    def __init__(self):
        self.index: Dict[str, List[str]] = {}

    def add(self, word: str, doc_id: str):
        self.index.setdefault(word, []).append(doc_id)

    def search(self, word: str) -> List[str]:
        return self.index.get(word, [])