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
        import traceback
        error_details = traceback.format_exc()
        print(f"Chat Error: {error_details}")
        raise HTTPException(status_code=500, detail=f"Internal Error: {str(e)}")
