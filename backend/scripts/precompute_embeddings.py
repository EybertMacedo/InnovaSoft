import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
import time

# Load env vars
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

def configure_genai():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not found in .env")
        return False
    genai.configure(api_key=api_key)
    return True

def get_embedding(text):
    try:
        result = genai.embed_content(
            model="models/embedding-001",
            content=text,
            task_type="retrieval_query"
        )
        return result['embedding']
    except Exception as e:
        print(f"Error getting embedding: {e}")
        return None

def main():
    if not configure_genai():
        return

    data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "projects.json")
    
    with open(data_path, "r") as f:
        data = json.load(f)

    print(f"Found {len(data)} items. Generating embeddings...")
    
    for i, item in enumerate(data):
        print(f"Processing item {i+1}/{len(data)}: {item.get('title', 'Profile')}")
        if 'embedding' not in item:
            embedding = get_embedding(item['content'])
            if embedding:
                item['embedding'] = embedding
                # Sleep to avoid hitting rate limits during generation
                time.sleep(1)
            else:
                print("Failed to generate embedding.")
        else:
            print("Embedding already exists.")

    with open(data_path, "w") as f:
        json.dump(data, f, indent=2)
    
    print("Done! Embeddings saved to projects.json")

if __name__ == "__main__":
    main()
