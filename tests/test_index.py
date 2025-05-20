from app.domain.index import InvertedIndex

def test_index_add_and_search():
    index = InvertedIndex()
    index.add_document("doc1", "Hello world, this is a test.")
    index.add_document("doc2", "Parallel world with other test")

    assert set(index.search("world")) == {"doc1", "doc2"}
    assert index.search("test") == ["doc1", "doc2"]
    assert index.search("does no exist") == []