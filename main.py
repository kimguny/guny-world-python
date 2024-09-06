from fastapi import FastAPI
from routes.tts import tts_router
from routes.text_handler import text_handler_router

app = FastAPI(root_path="/api")

# 라우터 등록
app.include_router(tts_router, prefix="/tts")
app.include_router(text_handler_router, prefix="/text")

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI TTS Service!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
