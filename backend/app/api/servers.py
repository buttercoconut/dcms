# api/servers.py
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_async_session
from ..models.server import Server, ServerCreate, ServerUpdate
from ..services.server_service import ServerService

router = APIRouter(prefix="/servers", tags=["servers"])

async def get_server_service(db: AsyncSession = Depends(get_async_session)) -> ServerService:
    return ServerService(db)

@router.get("/", response_model=List[Server])
async def read_servers(service: ServerService = Depends(get_server_service)):
    return await service.get_servers()

@router.get("/{server_id}", response_model=Server)
async def read_server(server_id: int, service: ServerService = Depends(get_server_service)):
    server = await service.get_server(server_id)
    if not server:
        raise HTTPException(status_code=404, detail="Server not found")
    return server

@router.post("/", response_model=Server, status_code=status.HTTP_201_CREATED)
async def create_server(server_in: ServerCreate, service: ServerService = Depends(get_server_service)):
    return await service.create_server(server_in)

@router.put("/{server_id}", response_model=Server)
async def update_server(server_id: int, server_in: ServerUpdate, service: ServerService = Depends(get_server_service)):
    server = await service.update_server(server_id, server_in)
    if not server:
        raise HTTPException(status_code=404, detail="Server not found")
    return server

@router.delete("/{server_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_server(server_id: int, service: ServerService = Depends(get_server_service)):
    success = await service.delete_server(server_id)
    if not success:
        raise HTTPException(status_code=404, detail="Server not found")
    return None
