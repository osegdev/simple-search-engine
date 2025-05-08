from abc import ABC, abstractmethod
from typing import List
from app.domain.index import InvertedIndex

class SearchStrategy(ABC):
    def __init__(self, index: InvertedIndex):
        self.index = index

    @abstractmethod
    def search(self, query: str) -> List[str]:
        pass