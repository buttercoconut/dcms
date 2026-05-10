# main.py
from fastapi import FastAPI
from .api import servers
from .config import settings

app = FastAPI(title="DCMS Backend", description="Data Center Management System API", version="0.1.0")

app.include_router(servers.router)

@app.get("/health")
async def health_check():
    return {"status": "ok"}
