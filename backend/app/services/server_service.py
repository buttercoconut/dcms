# services/server_service.py
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from ..models.server import ServerCreate, ServerUpdate, Server
from ..database import get_async_session

class ServerService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_servers(self) -> List[Server]:
        result = await self.db.execute(select(Server))
        return result.scalars().all()

    async def get_server(self, server_id: int) -> Server | None:
        result = await self.db.execute(select(Server).where(Server.id == server_id))
        return result.scalar_one_or_none()

    async def create_server(self, server_in: ServerCreate) -> Server:
        new_server = Server(**server_in.dict())
        self.db.add(new_server)
        await self.db.commit()
        await self.db.refresh(new_server)
        return new_server

    async def update_server(self, server_id: int, server_in: ServerUpdate) -> Server | None:
        server = await self.get_server(server_id)
        if not server:
            return None
        for key, value in server_in.dict(exclude_unset=True).items():
            setattr(server, key, value)
        await self.db.commit()
        await self.db.refresh(server)
        return server

    async def delete_server(self, server_id: int) -> bool:
        server = await self.get_server(server_id)
        if not server:
            return False
        await self.db.delete(server)
        await self.db.commit()
        return True
