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
    Tu objetivo es responder a los usuarios de manera conversacional, muy breve y natural, como si estuvieras chateando.
    
    REGLAS ESTRICTAS:
    1. Háblale al usuario directamente de forma concisa y amigable (MÁXIMO 1 o 2 párrafos cortos). NO des explicaciones enciclopédicas ni teóricas (ej. no expliques qué es PPE o qué es Machine Learning en general).
    2. Usa la información del contexto para responder. Si te preguntan por un proyecto (ej. PPE), habla en primera persona del plural ("Nosotros desarrollamos", "En InnovaSoft creamos...") y menciona qué hicimos exactamente nosotros en ese proyecto.
    3. Si la respuesta no está en el contexto, di amablemente que no tienes esa información y sugiere contactar a Alexis directamente.
    4. Responde SOLO con texto plano. NO uses formato Markdown (ni negritas **, ni cursivas *, ni listas con guiones - o asteriscos *).
    5. Si te piden un enlace, link, URL o sitio web de algún proyecto, búscalo en el contexto y entrégaselo directamente sin excusas.

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
            model="llama-3.1-8b-instant",
            temperature=0.5,
            max_tokens=512,
        )
        
        response_text = chat_completion.choices[0].message.content
        
        # Post-processing to ensure no Markdown remains
        clean_text = response_text.replace('**', '').replace('__', '')
        # Remove single asterisks but keep them if they are part of a math equation (unlikely here but safe to just remove for formatting)
        clean_text = clean_text.replace('* ', '- ').replace('*', '') 
        
        return clean_text
    except Exception as e:
        print(f"Error generating answer: {e}")
        if "429" in str(e):
            return "Lo siento, en este momento estoy recibiendo muchas consultas (límite de cuota excedido). Por favor, intenta de nuevo más tarde o contáctanos a través del formulario."
        return "Lo siento, ha ocurrido un error al procesar tu solicitud. Por favor intenta nuevamente."
