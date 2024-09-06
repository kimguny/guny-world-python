from fastapi import APIRouter

text_handler_router = APIRouter()

@text_handler_router.post("/process")
async def process_text(text: str):
    """
    받은 텍스트를 간단히 처리합니다. 예: 텍스트를 대문자로 변환
    """
    return {"processed_text": text.upper()}
