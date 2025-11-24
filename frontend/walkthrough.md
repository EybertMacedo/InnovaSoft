## Features Implemented

1.  **Tech Stack**:
    *   **Frontend**: Vue 3, Vite, Tailwind CSS, Lucide Icons.
    *   **Backend**: FastAPI, Python 3.11.
    *   **AI/RAG**: Qdrant (Vector DB), FastEmbed (Local Embeddings), Google Gemini (Generation).
    *   **Infrastructure**: Digital Ocean Droplet (Docker Compose), Cloudflare (DNS/SSL).

2.  **Core Functionality**:
    *   **RAG Chatbot**: Intelligent assistant capable of answering questions about InnovaSoft using a custom knowledge base.
    *   **Contact Form**: Integrated with Gmail API for sending real emails and auto-replies.
    *   **Interactive Demo Center**: Simulations of Chat, Vision AI, and Real-time Dashboards.

## Deployment Architecture

*   **Domain**: `innovalabs.studio` (Managed by Name.com, DNS via Cloudflare).
*   **SSL**: Full HTTPS via Cloudflare Flexible SSL.
*   **Server**: Digital Ocean Droplet (1GB RAM).
    *   **Frontend Container**: Nginx serving Vue 3 static files.
    *   **Backend Container**: Uvicorn running FastAPI.
    *   **Reverse Proxy**: Nginx handles routing `/api` requests internally to the backend.

## How to Run Locally

1.  **Start Full Stack**:
    ```bash
    docker compose up --build
    ```
2.  **Access**:
    *   Frontend: `http://localhost:80`
    *   Backend: `http://localhost:8000/docs`

## File Structure

*   `frontend/`: Vue.js application.
*   `backend/`: FastAPI application.
    *   `services/rag.py`: RAG logic with Qdrant and FastEmbed.
    *   `scripts/init_qdrant.py`: Script to index the knowledge base.
*   `docker-compose.yml`: Orchestration for local and production.
*   `DEPLOY_DIGITALOCEAN.md`: Detailed deployment guide.
