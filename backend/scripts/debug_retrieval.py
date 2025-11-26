import os
from qdrant_client import QdrantClient
from fastembed import TextEmbedding
from dotenv import load_dotenv

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

QDRANT_URL = os.getenv("QDRANT_ENDPOINT")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
COLLECTION_NAME = "innovasoft_knowledge"

def debug_retrieval(query):
    print(f"--- Debugging Query: '{query}' ---")
    
    # 1. Check Qdrant Connection
    try:
        client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
        collections = client.get_collections().collections
        print(f"Collections found: {[c.name for c in collections]}")
        
        if not any(c.name == COLLECTION_NAME for c in collections):
            print(f"ERROR: Collection '{COLLECTION_NAME}' not found!")
            return
            
        count = client.count(collection_name=COLLECTION_NAME)
        print(f"Points in collection: {count.count}")
        
    except Exception as e:
        print(f"ERROR Connecting to Qdrant: {e}")
        return

    # 2. Generate Embedding
    try:
        print("Generating embedding...")
        embedding_model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")
        query_vector = list(embedding_model.embed([query]))[0].tolist()
        print(f"Vector generated (len={len(query_vector)})")
    except Exception as e:
        print(f"ERROR Generating Embedding: {e}")
        return

    # 3. Search
    try:
        print("Searching Qdrant...")
        print(f"Client attributes: {dir(client)}")
        
        # Try search
        if hasattr(client, 'search'):
            search_result = client.search(
                collection_name=COLLECTION_NAME,
                query_vector=query_vector,
                limit=3
            )
        else:
            print("Method 'search' not found. Trying 'query_points'...")
            search_result = client.query_points(
                collection_name=COLLECTION_NAME,
                query=query_vector,
                limit=3
            ).points

        print(f"Found {len(search_result)} results:")
        for i, hit in enumerate(search_result):
            print(f"\nResult {i+1} (Score: {hit.score}):")
            print(f"Payload: {hit.payload}")
            
    except Exception as e:
        print(f"ERROR Searching: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("\n=== Test 1: 'experiencia profesional' ===")
    debug_retrieval("experiencia profesional")
    print("\n=== Test 2: 'trabajos anteriores' ===")
    debug_retrieval("trabajos anteriores")
    print("\n=== Test 3: 'Data Engineer' ===")
    debug_retrieval("Data Engineer")
