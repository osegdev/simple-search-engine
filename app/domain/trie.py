from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str):
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.is_end_of_word = True

    def _dfs(self, node: TrieNode, prefix: str, results: List):
        if node.is_end_of_word:
            results.append(prefix)
        for char, child in node.children.items():
            self._dfs(child, prefix + char, results)
    
    def autocomplete(self, prefix: str) -> list:
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        
        results = []
        self._dfs(node, prefix,results)
        return results
    