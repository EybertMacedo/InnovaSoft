import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS immediately to ensure error responses are visible
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
def health_check():
    return {"status": "ok", "message": "Backend is running"}

try:
    from dotenv import load_dotenv
    
    # Load environment variables explicitly
    env_path = os.path.join(os.path.dirname(__file__), ".env")
    load_dotenv(env_path)
    
    print(f"Loading .env from: {env_path}")
    print(f"SENDER_EMAIL loaded: {'Yes' if os.getenv('SENDER_EMAIL') else 'No'}")

    from routers import contact
    
    # Include routers
    app.include_router(contact.router, prefix="/api")

except Exception as e:
    print(f"CRITICAL STARTUP ERROR: {str(e)}")
    import traceback
    traceback.print_exc()
    
    @app.get("/api/{catchall:path}")
    def startup_error(catchall: str):
        return {
            "status": "startup_error", 
            "error": str(e),
            "traceback": traceback.format_exc()
        }
    
    @app.post("/api/{catchall:path}")
    def startup_error_post(catchall: str):
        return {
            "status": "startup_error", 
            "error": str(e),
            "traceback": traceback.format_exc()
        }

