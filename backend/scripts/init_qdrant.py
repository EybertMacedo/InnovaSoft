import os
import re
import time
import uuid
from typing import List, Dict
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.http import models
# import google.generativeai as genai

# Load env vars
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

# Configuration
QDRANT_URL = os.getenv("QDRANT_ENDPOINT")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
COLLECTION_NAME = "innovasoft_knowledge"

print(f"Loading env from: {os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')}")
print(f"QDRANT_URL found: {'Yes' if QDRANT_URL else 'No'}")
print(f"QDRANT_API_KEY found: {'Yes' if QDRANT_API_KEY else 'No'}")
print(f"GEMINI_API_KEY found: {'Yes' if GEMINI_API_KEY else 'No'}")

if not QDRANT_URL or not QDRANT_API_KEY:
    raise ValueError("QDRANT_ENDPOINT or QDRANT_API_KEY not set in .env")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not set in .env")

# Initialize Clients
qdrant = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
# genai.configure(api_key=GEMINI_API_KEY)

def parse_knowledge_base(file_path: str) -> List[Dict]:
    """Parses the custom text format into chunks."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split by "CHUNK X — " pattern
    # Regex looks for "CHUNK" followed by number, dash, and captures the rest until next CHUNK
    chunks = []
    
    # Normalize newlines
    content = content.replace('\r\n', '\n')
    
    # Find all chunks
    pattern = r"CHUNK \d+ — (.*?)(?=CHUNK \d+ — |BLOQUE \d+:|$)"
    matches = re.finditer(pattern, content, re.DOTALL)
    
    for match in matches:
        full_text = match.group(1).strip()
        # Split title and content if possible (first line vs rest)
        lines = full_text.split('\n', 1)
        title = lines[0].strip()
        body = lines[1].strip() if len(lines) > 1 else ""
        
        # Combine for embedding
        combined_text = f"{title}\n{body}"
        
        chunks.append({
            "title": title,
            "content": combined_text,
            "metadata": {"source": "knowledge_base.txt"}
        })
        
    return chunks

# Use fastembed (ONNX) to avoid heavy PyTorch dependencies
from fastembed import TextEmbedding

# Initialize local model (lightweight ONNX version of MiniLM)
# fastembed downloads the model automatically (~80MB)
model = TextEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

def get_embedding(text: str) -> List[float]:
    try:
        # Generate embedding locally
        # fastembed returns a generator of vectors, we take the first one
        embeddings = list(model.embed([text]))
        return embeddings[0].tolist()
    except Exception as e:
        print(f"Error getting embedding: {e}")
        return None

def init_qdrant():
    print("Initializing Qdrant Collection...")
    
    # Re-create collection
    qdrant.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=models.VectorParams(size=384, distance=models.Distance.COSINE),
    )
    print(f"Collection '{COLLECTION_NAME}' created.")

    # Load Data
    # Note: User created 'knoledge_base.txt' (typo), so we look for that or the corrected one
    base_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_dir, "data", "knoledge_base.txt")
    
    if not os.path.exists(file_path):
        # Try corrected spelling just in case
        file_path = os.path.join(base_dir, "data", "knowledge_base.txt")
        
    if not os.path.exists(file_path):
        print(f"Error: Knowledge base file not found at {file_path}")
        return

    print(f"Reading data from {file_path}...")
    chunks = parse_knowledge_base(file_path)
    print(f"Found {len(chunks)} chunks.")

    points = []
    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i+1}/{len(chunks)}: {chunk['title']}")
        
        embedding = get_embedding(chunk['content'])
        if embedding:
            points.append(models.PointStruct(
                id=str(uuid.uuid4()),
                vector=embedding,
                payload=chunk
            ))
            time.sleep(1) # Rate limit protection
        else:
            print(f"Skipping chunk {i+1} due to embedding error.")

    if points:
        print(f"Uploading {len(points)} points to Qdrant...")
        qdrant.upsert(
            collection_name=COLLECTION_NAME,
            points=points
        )
        print("Upload complete!")
    else:
        print("No points to upload.")

if __name__ == "__main__":
    init_qdrant()
