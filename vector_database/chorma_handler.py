import chromadb
client = chromadb.PersistentClient(path="vector_db")
collection = client.get_or_create_collection("memories")

def add_memory(user_id, text):
    collection.add(ids=[user_id], documents=[text])

def retrieve_memory(query):
    result = collection.query(
        query_texts=[query],
        n_results=3
    )
    return result