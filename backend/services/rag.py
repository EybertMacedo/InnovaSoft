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
        json_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "projects.json")
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
        return []

# Calculate Cosine Similarity
def cosine_similarity(a: List[float], b: List[float]) -> float:
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Find Relevant Context
def find_relevant_context(query: str, knowledge_base: List[Dict], top_k: int = 3) -> str:
    if not configure_genai():
        return "Error: API Key not configured."

    query_embedding = get_embedding(query)
    if not query_embedding:
        return ""

    scored_docs = []
    for item in knowledge_base:
        # We cache embeddings in memory for this simple demo
        # In production, these should be pre-calculated and stored in the JSON or a DB
        if 'embedding' not in item:
            # Generate embedding for the content on the fly (slow for first run, but fine for demo)
            item['embedding'] = get_embedding(item['content'])
        
        if item['embedding']:
            score = cosine_similarity(query_embedding, item['embedding'])
            scored_docs.append((score, item['content']))

    # Sort by score descending
    scored_docs.sort(key=lambda x: x[0], reverse=True)
    
    # Return top_k context
    context_parts = [doc[1] for doc in scored_docs[:top_k]]
    return "\n\n".join(context_parts)

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
        return "Lo siento, hubo un error al procesar tu pregunta."
