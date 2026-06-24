import chromadb


class ChromaHandler:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="vector_db"
        )

        self.collection = (
            self.client.get_or_create_collection(
                "memories"
            )
        )


    def add_memory(

            self,

            memory_id,

            text):

        self.collection.add(

            ids=[memory_id],

            documents=[text]

        )


    def search(

            self,

            query,

            n_results=5):

        result = self.collection.query(

            query_texts=[query],

            n_results=n_results

        )

        return result["documents"][0]