from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.rag import generate_answer

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
def chat_endpoint(request: ChatRequest):
    try:
        response_text = generate_answer(request.message)
        return {"response": response_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
