import math
from collections import defaultdict
from app.domain.search_strategy import SearchStrategy
from typing import List

class TFIDFSearch(SearchStrategy):
    def search(self, query: str) -> List[str]:
        terms = query.lower().split()
        doc_scores = defaultdict(float)
        total_docs = len({doc_id for docs in self.index.index.values() for doc_id in docs})

        for term in terms:
            docs = self.index.search(term)
            if not docs:
                continue
            tf = 1  # Simplificación: cada término cuenta igual
            idf = math.log((total_docs + 1) / (1 + len(docs)))
            for doc_id in docs:
                doc_scores[doc_id] += tf * idf

        return sorted(doc_scores, key=doc_scores.get, reverse=True)
