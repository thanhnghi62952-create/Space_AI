class RetrievalEngine:
    def __init__(self, chroma_handler):
        self.chroma_handler = chroma_handler

    def retrieve(self, query):
        return self.chroma_handler.search(query)