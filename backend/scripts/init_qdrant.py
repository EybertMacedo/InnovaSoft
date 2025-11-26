import os
from qdrant_client import QdrantClient
from qdrant_client.http import models
from fastembed import TextEmbedding
from dotenv import load_dotenv

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

# Configuration
QDRANT_ENDPOINT = os.getenv("QDRANT_ENDPOINT")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
COLLECTION_NAME = "innovasoft_knowledge"

def init_qdrant():
    print("Initializing Qdrant...")
    
    if not QDRANT_ENDPOINT:
        raise ValueError("QDRANT_ENDPOINT is not set")

    client = QdrantClient(url=QDRANT_ENDPOINT, api_key=QDRANT_API_KEY)
    
    # Check if collection exists
    collections = client.get_collections().collections
    exists = any(c.name == COLLECTION_NAME for c in collections)
    
    if exists:
        print(f"Collection '{COLLECTION_NAME}' exists. Recreating...")
        client.delete_collection(COLLECTION_NAME)
    
    # Create collection
    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=models.VectorParams(
            size=384,  # FastEmbed BAAI/bge-small-en-v1.5 dimension
            distance=models.Distance.COSINE
        )
    )
    print(f"Collection '{COLLECTION_NAME}' created.")
    
    # Load and chunk data
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'knowledge_base.txt')
    if not os.path.exists(data_path):
        print(f"Warning: {data_path} not found.")
        return

    with open(data_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Simple chunking by paragraphs or sections
    chunks = [c.strip() for c in text.split('\n\n') if c.strip()]
    print(f"Found {len(chunks)} chunks.")
    
    # Embeddings
    print("Generating embeddings...")
    embedding_model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")
    embeddings = list(embedding_model.embed(chunks))
    
    # Upload points
    points = [
        models.PointStruct(
            id=idx,
            vector=emb.tolist(),
            payload={"text": chunk}
        )
        for idx, (chunk, emb) in enumerate(zip(chunks, embeddings))
    ]
    
    client.upload_points(
        collection_name=COLLECTION_NAME,
        points=points
    )
    print(f"Uploaded {len(points)} points to Qdrant.")

if __name__ == "__main__":
    init_qdrant()
