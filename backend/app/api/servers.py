from fastapi import APIRouter
from ..models.server import Server

router = APIRouter()

@router.get("/servers", response_model=list[Server])
async def list_servers():
    # placeholder data
    return [
        Server(id=1, hostname="srv01", status="online", cpu_usage=23.5, memory_usage=45.2),
        Server(id=2, hostname="srv02", status="offline", cpu_usage=0.0, memory_usage=0.0),
    ]
