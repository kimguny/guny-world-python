# routes/tts.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import chzzkpy

tts_router = APIRouter()

# 요청의 Body 구조 정의
class CookieData(BaseModel):
    NID_AUT: str
    NID_SES: str

@tts_router.post("/use_cookie_tts")
async def use_cookie_tts(data: CookieData):
    # chzzkpy에서 NID_AUT, NID_SES 사용
    try:
        result = chzzkpy.some_function_using_cookie(data.NID_AUT, data.NID_SES)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing TTS: {str(e)}")
