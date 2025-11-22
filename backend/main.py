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
# Allow all origins to prevent CORS issues on different Vercel domains
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(contact.router, prefix="/api")

