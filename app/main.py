from fastapi import FastAPI
from app.core.config import settings
from app.api.router import router

app = FastAPI(title=settings.APP_NAME, version="1.0.0")
app.include_router(router, prefix=settings.API_PREFIX)

@app.get("/health")
async def health():
    return {"status": "ok", "service": "agroclima-python"}
