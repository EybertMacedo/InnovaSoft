import os
from email.utils import formataddr
from fastapi import APIRouter, HTTPException
from models import ContactRequest
from services.gmail import get_gmail_service, create_message, send_message
from utils.templates import get_auto_reply_template

router = APIRouter()

@router.post("/contact")
def contact(request: ContactRequest):
    try:
        service = get_gmail_service()
        
        # Get configuration from environment variables
        sender_email = os.getenv("SENDER_EMAIL")
        admin_email = os.getenv("ADMIN_EMAIL")
        
        if not sender_email:
            raise ValueError("SENDER_EMAIL environment variable is not set")
        if not admin_email:
            # Fallback to sender_email if admin_email is not set
            admin_email = sender_email

        # 1. Send notification to Admin
        admin_subject = f"Nuevo Mensaje de Contacto de {request.name}"
        admin_body = f"""
        <p><strong>Nombre:</strong> {request.name}</p>
        <p><strong>Email:</strong> {request.email}</p>
        <p><strong>Mensaje:</strong></p>
        <p>{request.message}</p>
        """
        admin_msg = create_message(sender_email, admin_email, admin_subject, admin_body)
        send_message(service, "me", admin_msg)

        # 2. Send auto-reply to User
        user_subject = "Hemos recibido tu mensaje - InnovaSoft"
        user_body = get_auto_reply_template(request.name)
        
        # Use formataddr for robust "Name <email>" formatting
        formatted_sender = formataddr(("InnovaSoft", sender_email))
        
        user_msg = create_message(formatted_sender, request.email, user_subject, user_body)
        send_message(service, "me", user_msg)

        return {"status": "success", "message": "Messages sent successfully"}
        
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
