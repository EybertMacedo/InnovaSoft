import os
from typing import List, Dict
from qdrant_client import QdrantClient
from fastembed import TextEmbedding
from groq import Groq

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
embedding_model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")

# Configure Groq (for Answer Generation only)
def get_groq_client():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("Warning: GROQ_API_KEY not set")
        return None
    return Groq(api_key=api_key)

def get_embedding(text: str) -> List[float]:
    try:
        embeddings = list(embedding_model.embed([text]))
        return embeddings[0].tolist()
    except Exception as e:
        print(f"Error getting embedding: {e}")
        raise e

def find_relevant_context(query: str, top_k: int = 5) -> str:
    # Instead of using Qdrant which is failing, just read the knowledge base directly
    # since it's a small file and fits well within the 8K context window of Llama 3
    try:
        data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'knowledge_base.txt')
        with open(data_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading knowledge base: {e}")
        return ""

def generate_answer(query: str) -> str:
    groq_client = get_groq_client()
    if not groq_client:
        return "Lo siento, no puedo responder en este momento (Falta configuración de API de Groq)."

    context = find_relevant_context(query)
    
    prompt = f"""
    Eres el asistente virtual oficial de InnovaSoft, la agencia de Eybert Alexis.
    Tu objetivo es responder de manera conversacional, cercana, amigable, clara y muy visualmente atractiva para el usuario.
    
    PAUTAS DE FORMATO Y ESTILO:
    1. Tono cercano y profesional: Habla en primera persona del plural ("En InnovaSoft desarrollamos...", "Creamos...").
    2. Respuestas estructuradas: Usa saltos de línea y viñetas (•) para que la lectura sea ligera y agradable.
    3. Proyectos: Si el usuario pregunta de forma general sobre proyectos o experiencia, presenta los 3 o 4 más destacados (como SentiData, SafetyMind/Cobbles, Poker Hand Classifier, SafetyModel) con una descripción breve de 1 línea por proyecto, seguida del enlace web/repo correspondiente en su propia línea. Al final, invita amablemente a preguntar por alguno en detalle o por el resto del portafolio.
    4. Enlaces: Si un proyecto tiene URL o enlace en el contexto, compártelo de forma clara.
    5. Concisión: Evita muros de texto interminables o explicaciones teóricas innecesarias.
    6. Límites: Si la información no está en el contexto, indícalo amablemente y sugiere contactar a Alexis directamente.

    Contexto sobre nuestros proyectos y experiencia:
    {context}
    """

    try:
        chat_completion = groq_client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": prompt,
                },
                {
                    "role": "user",
                    "content": query,
                }
            ],
            model=os.getenv("GROQ_MODEL", "openai/gpt-oss-120b"),
            temperature=0.4,
            max_tokens=600,
        )
        
        response_text = chat_completion.choices[0].message.content
        return response_text.strip()
    except Exception as e:
        print(f"Error generating answer: {e}")
        if "429" in str(e):
            return "Lo siento, en este momento estoy recibiendo muchas consultas (límite de cuota excedido). Por favor, intenta de nuevo más tarde o contáctanos a través del formulario."
        return "Lo siento, ha ocurrido un error al procesar tu solicitud. Por favor intenta nuevamente."
