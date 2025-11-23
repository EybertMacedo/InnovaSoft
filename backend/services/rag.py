import os
import google.generativeai as genai
from typing import List, Dict
from qdrant_client import QdrantClient
from fastembed import TextEmbedding

# Configure Clients
QDRANT_URL = os.getenv("QDRANT_ENDPOINT")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
COLLECTION_NAME = "innovasoft_knowledge"

# Initialize Qdrant
qdrant = None
if QDRANT_URL and QDRANT_API_KEY:
    try:
        qdrant = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
    except Exception as e:
        print(f"Failed to init Qdrant: {e}")

# Initialize Local Embedding Model (FastEmbed)
# This uses ONNX and is much lighter than PyTorch
embedding_model = TextEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Configure Gemini (for Answer Generation only)
def configure_genai():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Warning: GEMINI_API_KEY not set")
        return False
    genai.configure(api_key=api_key)
    return True

def get_embedding(text: str) -> List[float]:
    try:
        embeddings = list(embedding_model.embed([text]))
        return embeddings[0].tolist()
    except Exception as e:
        print(f"Error getting embedding: {e}")
        raise e

def find_relevant_context(query: str, top_k: int = 3) -> str:
    if not qdrant:
        return "Error: Qdrant not configured."

    try:
        query_vector = get_embedding(query)
        
        search_result = qdrant.search(
            collection_name=COLLECTION_NAME,
            query_vector=query_vector,
            limit=top_k
        )
        
        context_parts = [hit.payload['content'] for hit in search_result]
        return "\n\n".join(context_parts)
        
    except Exception as e:
        print(f"Search failed: {e}")
        return ""

def generate_answer(query: str) -> str:
    if not configure_genai():
        return "Lo siento, no puedo responder en este momento (Falta configuración de API)."

    context = find_relevant_context(query)
    
    prompt = f"""
    Eres el asistente virtual del portafolio de Alexis (InnovaSoft).
    Usa la siguiente información de contexto para responder a la pregunta del usuario.
    Si la respuesta no está en el contexto, di amablemente que no tienes esa información, pero sugiere contactar a Alexis directamente.
    Responde de manera profesional, breve y entusiasta.

    Contexto:
    {context}

    Pregunta:
    {query}

    Respuesta:
    """

    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error generating answer: {e}")
        raise e
