# api/servers.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..services.server_service import ServerService
from ..models.server import ServerCreate, ServerRead

router = APIRouter(prefix="/servers", tags=["servers"])

@router.get("/", response_model=list[ServerRead])
async def read_servers(db: Session = Depends(get_db)):
    service = ServerService(db)
    return service.get_all()

@router.post("/", response_model=ServerRead)
async def create_server(server: ServerCreate, db: Session = Depends(get_db)):
    service = ServerService(db)
    return service.create(server)
