from app.domain.search_strategy import SearchStrategy
from typing import List

class SearchEngine:
    def __init__(self, strategy: SearchStrategy):
        self.strategy = strategy
    
    def search(self, query: str) -> List[str]:
        return self.strategy.search(query)
    
    def set_strategy(self, strategy: SearchStrategy):
        self.strategy = strategy