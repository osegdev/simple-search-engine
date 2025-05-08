from collections import Counter
from app.domain.search_strategy import SearchStrategy
from typing import List

class FrequencyRankedSearch(SearchStrategy):
    def search(self, query: str) -> List[str]:
        terms = query.lower().split()
        counter = Counter()

        for term in terms:
            docs = self.index.search(term)
            for doc_id in docs:
                counter[doc_id] += 1

        ranked = [doc_id for doc_id, _ in counter.most_common()]
        return ranked