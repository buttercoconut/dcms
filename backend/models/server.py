# models/server.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from ..database import Base

class Server(Base):
    __tablename__ = "servers"

    id = Column(Integer, primary_key=True, index=True)
    hostname = Column(String, unique=True, index=True, nullable=False)
    ip_address = Column(String, unique=True, index=True, nullable=False)
    status = Column(String, default="unknown")
    cpu_usage = Column(Integer, default=0)
    memory_usage = Column(Integer, default=0)
    last_seen = Column(DateTime, server_default=func.now(), onupdate=func.now())
    is_active = Column(Boolean, default=True)

# Pydantic schemas
from pydantic import BaseModel

class ServerBase(BaseModel):
    hostname: str
    ip_address: str

class ServerCreate(ServerBase):
    pass

class ServerRead(ServerBase):
    id: int
    status: str
    cpu_usage: int
    memory_usage: int
    last_seen: str
    is_active: bool

    class Config:
        orm_mode = True
