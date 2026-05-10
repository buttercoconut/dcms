# models/server.py
from pydantic import BaseModel, Field
from typing import Optional

class ServerBase(BaseModel):
    hostname: str = Field(..., example="srv-01")
    ip_address: str = Field(..., example="192.168.1.10")
    status: str = Field(..., example="online")
    cpu_usage: Optional[float] = Field(None, example=23.5)
    memory_usage: Optional[float] = Field(None, example=45.2)
    power_consumption: Optional[float] = Field(None, example=120.0)

class ServerCreate(ServerBase):
    pass

class ServerUpdate(ServerBase):
    pass

class Server(ServerBase):
    id: int

    class Config:
        orm_mode = True
