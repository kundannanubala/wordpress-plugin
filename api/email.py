from fastapi import APIRouter, HTTPException
from models.emailModel import EmailRequest
from services.emailServices import email_generation

router = APIRouter()

@router.post("/generate-email")
async def generate_email(email_request: EmailRequest):
    try:
        return await email_generation(email_request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))