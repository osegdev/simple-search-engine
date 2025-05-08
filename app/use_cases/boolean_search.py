from app.domain.search_strategy import SearchStrategy
from typing import List

class BooleanSearch(SearchStrategy):
    def search(self, query: str) -> List[str]:
        terms = query.lower().split()
        if not terms:
            return []

        result = set(self.index.search(terms[0]))
        for term in terms[1:]:
            result &= set(self.index.search(term))
        return list(result)