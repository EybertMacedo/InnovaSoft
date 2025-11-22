import os
from dotenv import load_dotenv

# Load environment variables explicitly
env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(env_path)

print(f"Loading .env from: {env_path}")
print(f"SENDER_EMAIL loaded: {'Yes' if os.getenv('SENDER_EMAIL') else 'No'}")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import contact

app = FastAPI()

# Configure CORS
# Get allowed origins from env, default to local and production URLs
allowed_origins_str = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173,https://innovasoft-landing.vercel.app")
allowed_origins = [origin.strip() for origin in allowed_origins_str.split(",")]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(contact.router, prefix="/api")

