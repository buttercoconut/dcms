from fastapi import FastAPI
from .api.servers import router as servers_router

app = FastAPI(title="DCMS Backend")
app.include_router(servers_router, prefix="/api")
