import os
import json
import google.generativeai as genai
import numpy as np
from typing import List, Dict

# Configure Gemini
def configure_genai():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Warning: GEMINI_API_KEY not set")
        return False
    genai.configure(api_key=api_key)
    return True

# Load Knowledge Base
def load_knowledge_base() -> List[Dict]:
    try:
        # Try multiple possible locations for the JSON file
        base_dir = os.path.dirname(os.path.dirname(__file__)) # backend/
        possible_paths = [
            os.path.join(base_dir, "data", "projects.json"),
            os.path.join(os.getcwd(), "backend", "data", "projects.json"),
            os.path.join(os.getcwd(), "data", "projects.json"),
            "projects.json"
        ]
        
        json_path = None
        for path in possible_paths:
            if os.path.exists(path):
                json_path = path
                break
        
        if not json_path:
            print(f"CRITICAL: projects.json not found. Searched in: {possible_paths}")
            print(f"Current CWD: {os.getcwd()}")
            print(f"Directory listing: {os.listdir(os.getcwd())}")
            return []

        print(f"Loading knowledge base from: {json_path}")
        with open(json_path, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading knowledge base: {e}")
        return []

# Get Embedding (using Gemini)
def get_embedding(text: str) -> List[float]:
    try:
        result = genai.embed_content(
            model="models/embedding-001",
            content=text,
            task_type="retrieval_query"
        )
        return result['embedding']
    except Exception as e:
        print(f"Error getting embedding: {e}")
        raise e

# Calculate Cosine Similarity
def cosine_similarity(a: List[float], b: List[float]) -> float:
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Find Relevant Context
def find_relevant_context(query: str, knowledge_base: List[Dict], top_k: int = 3) -> str:
    if not configure_genai():
        return "Error: API Key not configured."

    try:
        query_embedding = get_embedding(query)
    except Exception:
        print("Embedding failed, falling back to keyword search")
        return keyword_search(query, knowledge_base, top_k)

    if not query_embedding:
        return keyword_search(query, knowledge_base, top_k)

    scored_docs = []
    for item in knowledge_base:
        # We cache embeddings in memory for this simple demo
        # In production, these should be pre-calculated and stored in the JSON or a DB
        if 'embedding' not in item:
            try:
                # Generate embedding for the content on the fly (slow for first run, but fine for demo)
                item['embedding'] = get_embedding(item['content'])
            except Exception:
                # If embedding generation fails for an item, skip it or use keyword search results mixed in?
                # For simplicity, if ANY embedding fails, we might want to abort to keyword search
                # But let's try to continue
                item['embedding'] = None
        
        if item.get('embedding'):
            score = cosine_similarity(query_embedding, item['embedding'])
            scored_docs.append((score, item['content']))
    
    # If we couldn't generate embeddings for enough items, fallback
    if not scored_docs:
        return keyword_search(query, knowledge_base, top_k)

    # Sort by score descending
    scored_docs.sort(key=lambda x: x[0], reverse=True)
    
    # Return top_k context
    context_parts = [doc[1] for doc in scored_docs[:top_k]]
    return "\n\n".join(context_parts)

def keyword_search(query: str, knowledge_base: List[Dict], top_k: int = 3) -> str:
    """Fallback search using simple keyword matching"""
    query_terms = query.lower().split()
    scored_docs = []
    
    for item in knowledge_base:
        score = 0
        content = item['content'].lower()
        title = item.get('title', '').lower()
        
        for term in query_terms:
            if term in title:
                score += 3 # Higher weight for title match
            if term in content:
                score += 1
        
        if score > 0:
            scored_docs.append((score, item['content']))
            
    scored_docs.sort(key=lambda x: x[0], reverse=True)
    return "\n\n".join([doc[1] for doc in scored_docs[:top_k]])

# Generate Answer
def generate_answer(query: str) -> str:
    if not configure_genai():
        return "Lo siento, no puedo responder en este momento (Falta configuración de API)."

    knowledge_base = load_knowledge_base()
    context = find_relevant_context(query, knowledge_base)
    
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
        # Re-raise exception to be caught by the router
        raise e
