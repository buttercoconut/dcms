# main.py
from fastapi import FastAPI
from .api import servers
from .database import engine, Base

app = FastAPI(title="DCMS Backend")

# Create tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(servers.router)

@app.get("/")
async def root():
    return {"message": "Welcome to DCMS API"}
