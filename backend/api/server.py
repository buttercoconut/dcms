from fastapi import APIRouter
from ..services.server_service import get_server_status
from ..models import ServerStatus

router = APIRouter()

@router.get("/servers", response_model=list[ServerStatus])
def list_servers():
    return get_server_status()
